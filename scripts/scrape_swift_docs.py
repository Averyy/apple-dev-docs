#!/usr/bin/env python3
"""
Swift Language Documentation Scraper

Fetches Swift language documentation from official swiftlang GitHub repositories
and saves them locally for indexing alongside Apple Developer Documentation.

Sources:
- swiftlang/swift-book (The Swift Programming Language book)
- swiftlang/swift-org-website (API guidelines, server docs, C++ interop)

Usage:
    python scripts/scrape_swift_docs.py
    python scripts/scrape_swift_docs.py --dry-run
    python scripts/scrape_swift_docs.py --force  # Re-download all files
"""

import argparse
import asyncio
import json
import logging
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import aiohttp
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

from utilities.hash_utils import compute_hash, load_hashes as load_hashes_from_file, save_hashes as save_hashes_to_file

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
console = Console()

# =============================================================================
# CONFIGURATION
# =============================================================================

# Output directory (relative to project root)
OUTPUT_DIR = Path(__file__).parent.parent / "documentation" / "Swift-Book"

# Hash file for incremental updates
HASH_FILE = Path(__file__).parent.parent / ".hashes" / "swift_docs_hashes.json"

# GitHub raw content base URL
GITHUB_RAW = "https://raw.githubusercontent.com"

# Rate limiting
REQUEST_DELAY = 0.1  # seconds between requests

# Retry transient GitHub failures (502s are common on api.github.com)
MAX_ATTEMPTS = 4
RETRY_BASE_DELAY = 2.0  # seconds; doubles per retry
RETRY_AFTER_CAP = 120.0  # seconds; upper bound on honoring a server Retry-After
RETRYABLE_STATUSES = {429, 500, 502, 503, 504}


@dataclass
class DocSource:
    """Represents a documentation source to scrape."""
    repo: str  # e.g., "swiftlang/swift-book"
    branch: str
    path: str  # e.g., "TSPL.docc/LanguageGuide"
    output_subdir: str  # e.g., "LanguageGuide"
    file_pattern: str = "*.md"


# Documentation sources to fetch
SOURCES: List[DocSource] = [
    # The Swift Programming Language book
    DocSource(
        repo="swiftlang/swift-book",
        branch="main",
        path="TSPL.docc/LanguageGuide",
        output_subdir="LanguageGuide",
    ),
    DocSource(
        repo="swiftlang/swift-book",
        branch="main",
        path="TSPL.docc/ReferenceManual",
        output_subdir="ReferenceManual",
    ),
    DocSource(
        repo="swiftlang/swift-book",
        branch="main",
        path="TSPL.docc/GuidedTour",
        output_subdir="GuidedTour",
    ),
    # Note: Skipping TSPL.docc root files (The-Swift-Programming-Language.md)
    # as it's just a table of contents with internal links
    # Swift.org website documentation
    DocSource(
        repo="swiftlang/swift-org-website",
        branch="main",
        path="documentation/api-design-guidelines",
        output_subdir="APIDesignGuidelines",
    ),
    # Note: Skipping documentation/server - niche content with broken swift.org links
    DocSource(
        repo="swiftlang/swift-org-website",
        branch="main",
        path="documentation/cxx-interop",
        output_subdir="CxxInterop",
    ),
]


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def _load_hashes() -> Dict[str, str]:
    """Load stored file hashes for incremental updates."""
    return load_hashes_from_file(HASH_FILE)


def _save_hashes(hashes: Dict[str, str]):
    """Save file hashes with metadata for next run."""
    save_hashes_to_file(HASH_FILE, hashes, source="scrape_swift_docs.py")


def _output_path_for_hash_key(hash_key: str) -> Optional[Path]:
    """Map a stored hash key ("repo:file_path") to its local output path.

    Returns None if the key doesn't match any configured source
    (e.g. a source that was removed from SOURCES).
    """
    repo, _, file_path = hash_key.partition(":")
    for source in SOURCES:
        if source.repo == repo and file_path.startswith(source.path + "/"):
            if source.output_subdir:
                relative_path = file_path[len(source.path) + 1:]
                return OUTPUT_DIR / source.output_subdir / relative_path
            return OUTPUT_DIR / Path(file_path).name
    return None


def clean_docc_content(content: str, filename: str) -> str:
    """
    Clean DocC-specific syntax from markdown content.

    Transforms:
    - <doc:Topic> links to readable format
    - @Metadata blocks (remove)
    - HTML test comments (remove)
    """
    import re

    # Remove @Metadata blocks
    content = re.sub(r'@Metadata\s*\{[^}]*\}', '', content, flags=re.DOTALL)

    # Remove HTML test comments like <!-- test: xxx -->
    content = re.sub(r'<!--\s*test:[^>]*-->', '', content)

    def transform_doc_link(match):
        """Transform <doc:Document#Section> to [Section](Document.md#Section)"""
        link_target = match.group(1)

        if '#' in link_target:
            # Has section anchor: <doc:Functions#Nested-Functions>
            doc, section = link_target.split('#', 1)
            # Humanize section name: "Nested-Functions" -> "Nested Functions"
            section_text = section.replace('-', ' ')
            return f'[{section_text}]({doc}.md#{section})'
        else:
            # Simple document link: <doc:Functions>
            # Humanize: "ClassesAndStructures" -> "Classes And Structures"
            doc_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', link_target)
            return f'[{doc_text}]({link_target}.md)'

    # Transform <doc:Topic> and <doc:Topic#Section> links
    content = re.sub(r'<doc:([^>]+)>', transform_doc_link, content)

    # Remove @Comment blocks
    content = re.sub(r'@Comment\s*\{[^}]*\}', '', content, flags=re.DOTALL)

    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.strip()


def add_source_header(content: str, source: DocSource, filename: str) -> str:
    """Add a source attribution header to the content."""
    # Extract title from content if present
    title_match = None
    for line in content.split('\n')[:10]:
        if line.startswith('# '):
            title_match = line[2:].strip()
            break

    # Build source URL
    source_url = f"https://github.com/{source.repo}/blob/{source.branch}/{source.path}/{filename}"

    # Only add header if there isn't already one
    if not content.startswith('---'):
        header = f"""---
source: {source.repo}
url: {source_url}
---

"""
        return header + content

    return content


# =============================================================================
# GITHUB API FUNCTIONS
# =============================================================================

async def _get_with_retry(
    session: aiohttp.ClientSession,
    url: str,
    headers: Optional[dict] = None
) -> tuple[int, str]:
    """GET a URL, retrying transient failures (5xx/429/network errors) with backoff.

    Returns (status, body_text). Non-retryable statuses (e.g. 404) are returned
    as-is; retryable failures raise the last error after MAX_ATTEMPTS.
    """
    last_error: Optional[Exception] = None
    retry_after: Optional[float] = None
    for attempt in range(MAX_ATTEMPTS):
        if attempt:
            delay = RETRY_BASE_DELAY * (2 ** (attempt - 1))
            if retry_after is not None:
                # Rate-limit responses say how long to wait; honor that (capped)
                delay = max(delay, min(retry_after, RETRY_AFTER_CAP))
            logger.warning(
                f"Retrying {url} in {delay:.0f}s "
                f"(attempt {attempt + 1}/{MAX_ATTEMPTS}): {last_error}"
            )
            await asyncio.sleep(delay)
        retry_after = None
        try:
            async with session.get(url, headers=headers) as response:
                if response.status in RETRYABLE_STATUSES:
                    header = response.headers.get("Retry-After", "")
                    if header.isdigit():
                        retry_after = float(header)
                    last_error = RuntimeError(
                        f"HTTP {response.status} {response.reason or ''} for {url}"
                    )
                    continue
                return response.status, await response.text()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            last_error = e
    assert last_error is not None  # loop can only fall through after a failure
    raise last_error


async def fetch_directory_contents(
    session: aiohttp.ClientSession,
    repo: str,
    branch: str,
    path: str,
    missing_ok: bool = True
) -> List[dict]:
    """Fetch directory listing from GitHub API.

    A 404 returns [] when missing_ok, else raises. A configured source root
    must not 404 silently: an empty listing there marks every local file of
    that source as an orphan, so it has to count as an error instead.
    """
    url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={branch}"

    headers = {"Accept": "application/vnd.github.v3+json"}

    # Add token if available (for higher rate limits)
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    status, body = await _get_with_retry(session, url, headers=headers)
    if status == 404:
        if not missing_ok:
            raise RuntimeError(f"Source path not found (404): {repo}/{path}")
        logger.warning(f"Path not found: {path}")
        return []
    if status >= 400:
        raise RuntimeError(f"GitHub API {status} for {url}")
    data = json.loads(body)
    if not isinstance(data, list):
        raise RuntimeError(f"Unexpected GitHub API response for {url}: expected a list")
    return data


async def fetch_file_content(
    session: aiohttp.ClientSession,
    repo: str,
    branch: str,
    path: str
) -> Optional[str]:
    """Fetch raw file content from GitHub."""
    url = f"{GITHUB_RAW}/{repo}/{branch}/{path}"

    status, body = await _get_with_retry(session, url)
    if status == 404:
        return None
    if status >= 400:
        raise RuntimeError(f"HTTP {status} for {url}")
    return body


async def discover_markdown_files(
    session: aiohttp.ClientSession,
    source: DocSource,
    recursive: bool = True,
    is_root: bool = True
) -> List[str]:
    """Discover all markdown files in a source path."""
    files = []

    contents = await fetch_directory_contents(
        session, source.repo, source.branch, source.path,
        missing_ok=not is_root
    )

    for item in contents:
        if item["type"] == "file" and item["name"].endswith(".md"):
            files.append(item["path"])
        elif item["type"] == "dir" and recursive:
            # Recursively search subdirectories
            sub_source = DocSource(
                repo=source.repo,
                branch=source.branch,
                path=item["path"],
                output_subdir=source.output_subdir,
            )
            sub_files = await discover_markdown_files(
                session, sub_source, recursive=True, is_root=False
            )
            files.extend(sub_files)

    await asyncio.sleep(REQUEST_DELAY)  # Rate limiting
    return files


# =============================================================================
# MAIN SCRAPING LOGIC
# =============================================================================

async def scrape_source(
    session: aiohttp.ClientSession,
    source: DocSource,
    hashes: Dict[str, str],
    dry_run: bool = False,
    force: bool = False
) -> Dict[str, any]:
    """Scrape a single documentation source."""
    stats = {"downloaded": 0, "skipped": 0, "errors": 0, "files": [], "expected_files": []}

    # For root-level sources, don't recurse into subdirs
    recursive = source.output_subdir != "" or source.path.count('/') > 1

    # Discover all markdown files
    try:
        if source.output_subdir == "" and "TSPL.docc" in source.path:
            # Special case: only get top-level files from TSPL.docc
            contents = await fetch_directory_contents(
                session, source.repo, source.branch, source.path,
                missing_ok=False
            )
            file_paths = [item["path"] for item in contents
                         if item["type"] == "file" and item["name"].endswith(".md")]
        else:
            file_paths = await discover_markdown_files(session, source, recursive=recursive)
    except Exception as e:
        logger.error(f"Error discovering files in {source.path}: {e}")
        stats["errors"] += 1
        return stats

    for file_path in file_paths:
        filename = Path(file_path).name

        # Determine output path (keep in sync with _output_path_for_hash_key)
        if source.output_subdir:
            # Calculate relative path within source
            relative_path = file_path[len(source.path) + 1:]
            output_path = OUTPUT_DIR / source.output_subdir / relative_path
        else:
            output_path = OUTPUT_DIR / filename

        # Track expected files for orphan cleanup
        stats["expected_files"].append(str(output_path))

        # Create unique key for hashing
        hash_key = f"{source.repo}:{file_path}"

        try:
            # Fetch content
            content = await fetch_file_content(
                session, source.repo, source.branch, file_path
            )

            if content is None:
                stats["errors"] += 1
                continue

            await asyncio.sleep(REQUEST_DELAY)  # Rate limiting

            # Check if content changed (re-download if the local file vanished)
            content_hash = compute_hash(content)
            if (not force and hash_key in hashes and hashes[hash_key] == content_hash
                    and output_path.exists()):
                stats["skipped"] += 1
                continue

            # Clean and enhance content
            content = clean_docc_content(content, filename)
            content = add_source_header(content, source, filename)

            if dry_run:
                console.print(f"  [dim]Would write:[/dim] {output_path}")
                stats["downloaded"] += 1
                stats["files"].append(str(output_path))
            else:
                # Write file
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)

                # Update hash
                hashes[hash_key] = content_hash
                stats["downloaded"] += 1
                stats["files"].append(str(output_path))

        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            stats["errors"] += 1

    return stats


async def scrape_all(dry_run: bool = False, force: bool = False):
    """Scrape all configured documentation sources."""
    console.print("\n[bold blue]Swift Language Documentation Scraper[/bold blue]\n")

    # Load existing hashes
    hashes = {} if force else _load_hashes()

    # Ensure output directory exists
    if not dry_run:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_stats = {"downloaded": 0, "skipped": 0, "errors": 0}
    all_expected_files: set = set()

    async with aiohttp.ClientSession() as session:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console,
        ) as progress:
            task = progress.add_task("Scraping sources...", total=len(SOURCES))

            for source in SOURCES:
                source_name = f"{source.repo.split('/')[-1]}/{source.output_subdir or 'root'}"
                progress.update(task, description=f"[cyan]{source_name}[/cyan]")

                stats = await scrape_source(
                    session, source, hashes, dry_run=dry_run, force=force
                )

                total_stats["downloaded"] += stats["downloaded"]
                total_stats["skipped"] += stats["skipped"]
                total_stats["errors"] += stats["errors"]
                all_expected_files.update(stats["expected_files"])

                if stats["downloaded"] > 0:
                    console.print(f"  [green]{source_name}:[/green] {stats['downloaded']} files")

                progress.advance(task)

    # Clean up orphaned files (files that exist locally but weren't in source).
    # Skipped whenever any error occurred: a failed directory listing means
    # expected_files is incomplete and cleanup would delete legitimate files.
    if total_stats["errors"] > 0:
        console.print(
            f"\n[yellow]Skipping orphan cleanup due to {total_stats['errors']} error(s)[/yellow]"
        )
    elif not dry_run and OUTPUT_DIR.exists():
        existing_files = set(str(f) for f in OUTPUT_DIR.rglob("*.md"))
        orphaned_files = existing_files - all_expected_files

        if orphaned_files:
            console.print(f"\n[yellow]Cleaning up {len(orphaned_files)} orphaned files...[/yellow]")
            deleted_count = 0
            for orphan_path in orphaned_files:
                try:
                    Path(orphan_path).unlink()
                    deleted_count += 1
                except Exception as e:
                    logger.warning(f"Could not delete orphan {orphan_path}: {e}")

            # Prune hash entries whose local file no longer exists
            stale_keys = [
                k for k in hashes
                if (p := _output_path_for_hash_key(k)) is None or not p.exists()
            ]
            for key in stale_keys:
                del hashes[key]

            # Remove empty directories
            for dirpath in sorted(OUTPUT_DIR.rglob("*"), key=lambda p: len(str(p)), reverse=True):
                if dirpath.is_dir() and not any(dirpath.iterdir()):
                    try:
                        dirpath.rmdir()
                    except Exception:
                        pass

            console.print(f"  [dim]Deleted {deleted_count} orphaned files[/dim]")
            total_stats["deleted"] = deleted_count

    # Save updated hashes (also save if files were deleted to update hash file)
    if not dry_run and (total_stats["downloaded"] > 0 or total_stats.get("deleted", 0) > 0):
        _save_hashes(hashes)

    # Print summary
    console.print("\n[bold]Summary:[/bold]")
    console.print(f"  Downloaded: [green]{total_stats['downloaded']}[/green]")
    console.print(f"  Skipped (unchanged): [dim]{total_stats['skipped']}[/dim]")
    if total_stats.get("deleted", 0) > 0:
        console.print(f"  Deleted (orphaned): [yellow]{total_stats['deleted']}[/yellow]")
    if total_stats["errors"] > 0:
        console.print(f"  Errors: [red]{total_stats['errors']}[/red]")

    console.print(f"\n[dim]Output directory: {OUTPUT_DIR}[/dim]")

    if not dry_run and total_stats["downloaded"] > 0:
        console.print("\n[yellow]Next step:[/yellow] Run the indexer to add these docs to Meilisearch:")
        console.print("  [dim]cd scripts && python index_to_meilisearch.py[/dim]")

    return total_stats


# =============================================================================
# CLI ENTRY POINT
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Scrape Swift language documentation from GitHub"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be downloaded without writing files"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-download all files, ignoring cached hashes"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        stats = asyncio.run(scrape_all(dry_run=args.dry_run, force=args.force))
        return 0 if stats["errors"] == 0 else 1
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted[/yellow]")
        return 130
    except Exception as e:
        console.print(f"\n[red]Error:[/red] {e}")
        logger.exception("Unexpected error")
        return 1


if __name__ == "__main__":
    sys.exit(main())
