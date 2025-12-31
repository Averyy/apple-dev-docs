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
import hashlib
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

def compute_hash(content: str) -> str:
    """Compute SHA-256 hash of content."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def load_hashes() -> Dict[str, str]:
    """Load stored file hashes for incremental updates."""
    if HASH_FILE.exists():
        try:
            with open(HASH_FILE, 'r') as f:
                data = json.load(f)
                # Support both old format (flat dict) and new format (with metadata)
                if "hashes" in data:
                    return data["hashes"]
                return data
        except Exception as e:
            logger.warning(f"Could not load hash file: {e}")
    return {}


def save_hashes(hashes: Dict[str, str]):
    """Save file hashes with metadata for next run."""
    from datetime import datetime

    HASH_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Include metadata with last_updated timestamp
    # This allows startup_check.py to detect when docs were updated
    data = {
        "metadata": {
            "last_updated": datetime.now().isoformat(),
            "total_files": len(hashes),
            "source": "scrape_swift_docs.py"
        },
        "hashes": hashes
    }

    with open(HASH_FILE, 'w') as f:
        json.dump(data, f, indent=2)


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

async def fetch_directory_contents(
    session: aiohttp.ClientSession,
    repo: str,
    branch: str,
    path: str
) -> List[dict]:
    """Fetch directory listing from GitHub API."""
    url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={branch}"

    headers = {"Accept": "application/vnd.github.v3+json"}

    # Add token if available (for higher rate limits)
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    async with session.get(url, headers=headers) as response:
        if response.status == 404:
            logger.warning(f"Path not found: {path}")
            return []
        response.raise_for_status()
        return await response.json()


async def fetch_file_content(
    session: aiohttp.ClientSession,
    repo: str,
    branch: str,
    path: str
) -> Optional[str]:
    """Fetch raw file content from GitHub."""
    url = f"{GITHUB_RAW}/{repo}/{branch}/{path}"

    async with session.get(url) as response:
        if response.status == 404:
            return None
        response.raise_for_status()
        return await response.text()


async def discover_markdown_files(
    session: aiohttp.ClientSession,
    source: DocSource,
    recursive: bool = True
) -> List[str]:
    """Discover all markdown files in a source path."""
    files = []

    contents = await fetch_directory_contents(
        session, source.repo, source.branch, source.path
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
            sub_files = await discover_markdown_files(session, sub_source, recursive=True)
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
    stats = {"downloaded": 0, "skipped": 0, "errors": 0, "files": []}

    # For root-level sources, don't recurse into subdirs
    recursive = source.output_subdir != "" or source.path.count('/') > 1

    # Discover all markdown files
    try:
        if source.output_subdir == "" and "TSPL.docc" in source.path:
            # Special case: only get top-level files from TSPL.docc
            contents = await fetch_directory_contents(
                session, source.repo, source.branch, source.path
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

        # Determine output path
        if source.output_subdir:
            # Calculate relative path within source
            relative_path = file_path.replace(source.path + "/", "")
            output_path = OUTPUT_DIR / source.output_subdir / relative_path
        else:
            output_path = OUTPUT_DIR / filename

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

            # Check if content changed
            content_hash = compute_hash(content)
            if not force and hash_key in hashes and hashes[hash_key] == content_hash:
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
    hashes = {} if force else load_hashes()

    # Ensure output directory exists
    if not dry_run:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_stats = {"downloaded": 0, "skipped": 0, "errors": 0}

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

                if stats["downloaded"] > 0:
                    console.print(f"  [green]{source_name}:[/green] {stats['downloaded']} files")

                progress.advance(task)

    # Save updated hashes
    if not dry_run and total_stats["downloaded"] > 0:
        save_hashes(hashes)

    # Print summary
    console.print("\n[bold]Summary:[/bold]")
    console.print(f"  Downloaded: [green]{total_stats['downloaded']}[/green]")
    console.print(f"  Skipped (unchanged): [dim]{total_stats['skipped']}[/dim]")
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
