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

Failures follow the policy shared with the MLX and HIG scrapers
(utilities/source_policy.py): a configured directory that returns 404/410
keeps its files for that run and is removed on the 2nd consecutive run; any
other failure of a configured directory keeps its files until it recovers; a
file GitHub no longer lists or that returns 404/410 is removed at once; other
failures and convert/save errors keep the file and block the orphan cleanup
for up to 3 runs. The orphan cleanup uses confirm-then-delete for mass
removals (pending_orphans in the hash file's metadata).

Exit codes: 0 clean (removals and valve holds included); 1 an error of ours
(a blocked cleanup, a configured directory that failed, a persistent
failure, a failed save, an unexpected exception); 130 interrupted.
"""

import argparse
import asyncio
import logging
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import aiohttp
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

from utilities.hash_utils import (
    HashFileError,
    compute_hash,
    read_hash_file,
    save_hashes as save_hashes_to_file,
    write_text_atomic,
)
from utilities.source_policy import (
    FAILURE_COUNTS_KEY,
    PENDING_ORPHANS_KEY,
    FetchFailed,
    KeptLocation,
    ScrapeRun,
    discover_github_markdown,
    fetch_github_raw,
    has_file_named,
    is_under,
    list_github_directory,
    policy_metadata,
)

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

# Rate limiting
REQUEST_DELAY = 0.1  # seconds between requests

# Hash-file metadata the failure policy keeps (saved whenever it changes)
POLICY_KEYS = (FAILURE_COUNTS_KEY, PENDING_ORPHANS_KEY)


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

def _load_hash_file() -> Tuple[Dict[str, str], Dict[str, Any], Optional[str]]:
    """Load stored file hashes and metadata for incremental updates.

    Returns:
        (hashes, metadata, load error): a file that can't be read loads as
        empty, with the error (the run then blocks its cleanup)
    """
    try:
        hashes, metadata = read_hash_file(HASH_FILE)
    except HashFileError as e:
        return {}, {}, str(e)
    return hashes, metadata, None


def _save_hashes(hashes: Dict[str, str], metadata: Dict[str, Any]) -> bool:
    """Save file hashes with metadata for next run."""
    return save_hashes_to_file(HASH_FILE, hashes, source="scrape_swift_docs.py", metadata=metadata)


def _output_path(source: "DocSource", file_path: str) -> Path:
    """The local output path of a source's file (repo-relative file_path)."""
    if source.output_subdir:
        relative_path = file_path[len(source.path) + 1:]
        return OUTPUT_DIR / source.output_subdir / relative_path
    return OUTPUT_DIR / Path(file_path).name


def _source_location(source: "DocSource") -> KeptLocation:
    """Where a source's files live: its output subdir (or, for a root-level
    source, the output dir without the other sources' subdirs)."""
    path = OUTPUT_DIR / source.output_subdir if source.output_subdir else OUTPUT_DIR
    excluded = tuple(
        other_path for other in SOURCES
        if other is not source
        and (other_path := (OUTPUT_DIR / other.output_subdir if other.output_subdir else OUTPUT_DIR)) != path
        and is_under(other_path, path)
    )
    return KeptLocation(path, reason="", excluded=excluded)


def _directory_key(repo: str, path: str) -> str:
    """The failure-counts key of a GitHub directory (file keys are "repo:path")."""
    return f"{repo}:{path}/"


def _output_path_for_hash_key(hash_key: str) -> Optional[Path]:
    """Map a stored hash key ("repo:file_path") to its local output path.

    Returns None if the key doesn't match any configured source
    (e.g. a source that was removed from SOURCES).
    """
    repo, _, file_path = hash_key.partition(":")
    for source in SOURCES:
        if source.repo == repo and file_path.startswith(source.path + "/"):
            return _output_path(source, file_path)
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
# MAIN SCRAPING LOGIC
# =============================================================================

async def _discover_source_files(
    session: aiohttp.ClientSession,
    source: DocSource,
) -> Tuple[List[str], Dict[str, FetchFailed]]:
    """A source's markdown files, and {directory: failure} for listings that failed."""
    # For root-level sources, don't recurse into subdirs
    recursive = source.output_subdir != "" or source.path.count('/') > 1

    if source.output_subdir == "" and "TSPL.docc" in source.path:
        # Special case: only get top-level files from TSPL.docc
        contents = await list_github_directory(session, source.repo, source.branch, source.path)
        await asyncio.sleep(REQUEST_DELAY)  # Rate limiting
        if isinstance(contents, FetchFailed):
            return [], {source.path: contents}
        return [item["path"] for item in contents
                if item.get("type") == "file" and str(item.get("name", "")).endswith(".md")
                and isinstance(item.get("path"), str)], {}
    return await discover_github_markdown(
        session, source.repo, source.branch, source.path, recursive=recursive, delay=REQUEST_DELAY
    )


async def scrape_source(
    session: aiohttp.ClientSession,
    source: DocSource,
    hashes: Dict[str, str],
    run: ScrapeRun,
    dry_run: bool = False,
    force: bool = False
) -> Dict[str, int]:
    """Scrape a single documentation source, reporting every outcome to run."""
    stats = {"downloaded": 0, "skipped": 0, "gone": 0, "failed": 0}
    location = _source_location(source)
    source_key = _directory_key(source.repo, source.path)

    # Discover all markdown files
    file_paths, failures = await _discover_source_files(session, source)

    # The configured directory itself: on failure nothing of it was found
    root_failure = failures.pop(source.path, None)
    if root_failure is not None:
        run.source_failed(source_key, root_failure, location, key_prefix=source_key)
        stats["gone" if root_failure.gone else "failed"] += 1
        return stats
    run.source_ok(source_key)

    # Subdirectories found by a listing
    for directory, failure in sorted(failures.items()):
        directory_key = _directory_key(source.repo, directory)
        directory_path = (location.path / directory[len(source.path) + 1:]
                          if source.output_subdir else location.path)
        run.directory_failed(directory_key, failure, KeptLocation(directory_path, reason=""),
                             key_prefix=directory_key)
        stats["gone" if failure.gone else "failed"] += 1

    for file_path in dict.fromkeys(file_paths):
        filename = Path(file_path).name

        # Determine output path (keep in sync with _output_path_for_hash_key)
        output_path = _output_path(source, file_path)

        # Create unique key for hashing
        hash_key = f"{source.repo}:{file_path}"

        # Fetch content
        content = await fetch_github_raw(session, source.repo, source.branch, file_path)
        if isinstance(content, FetchFailed):
            stats["gone" if content.gone else "failed"] += 1
            # A file we have: its key, or its file (a lost hash file loses keys, not files)
            if run.page_failed(hash_key, content,
                               previously_good=hash_key in hashes or has_file_named(output_path)):
                run.keep_file(hash_key, output_path)
            continue
        run.page_ok(hash_key, output_path)

        await asyncio.sleep(REQUEST_DELAY)  # Rate limiting

        # Check if content changed (re-download if the local file vanished)
        content_hash = compute_hash(content)
        if (not force and hash_key in hashes and hashes[hash_key] == content_hash
                and output_path.exists()):
            run.page_saved(hash_key)
            stats["skipped"] += 1
            continue

        # Convert and save; an error here is ours: the file is kept, never deleted
        try:
            # Clean and enhance content
            content = clean_docc_content(content, filename)
            content = add_source_header(content, source, filename)

            if dry_run:
                console.print(f"  [dim]Would write:[/dim] {output_path}")
            else:
                # Write file (whole or not at all: a failed write keeps the old doc)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                write_text_atomic(output_path, content)

                # Update hash
                hashes[hash_key] = content_hash
        except Exception as e:
            run.local_error(hash_key, output_path, f"{type(e).__name__}: {e}")
            stats["failed"] += 1
            continue

        run.page_saved(hash_key)
        stats["downloaded"] += 1

    return stats


def _prune_stale_keys(hashes: Dict[str, str]) -> int:
    """Drop hash entries whose local file is gone or whose source is no
    longer configured. Returns how many were dropped."""
    stale_keys = [
        k for k in hashes
        if (p := _output_path_for_hash_key(k)) is None or not p.exists()
    ]
    for key in stale_keys:
        del hashes[key]
    return len(stale_keys)


async def scrape_all(dry_run: bool = False, force: bool = False) -> Dict[str, Any]:
    """Scrape all configured documentation sources.

    Returns:
        The run's totals, with "exit_code" (0 clean, 1 an error of ours)
    """
    console.print("\n[bold blue]Swift Language Documentation Scraper[/bold blue]\n")

    # Load existing hashes (also with --force: the failure policy needs to
    # know which files we already have; --force only rewrites unchanged ones)
    hashes, metadata, load_error = _load_hash_file()
    stored_hashes = dict(hashes)
    run = ScrapeRun("Swift", OUTPUT_DIR.parent, metadata, load_error)

    # Ensure output directory exists
    if not dry_run:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_stats: Dict[str, Any] = {"downloaded": 0, "skipped": 0, "gone": 0, "failed": 0, "deleted": 0, "pruned": 0}

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
                    session, source, hashes, run, dry_run=dry_run, force=force
                )

                for name in ("downloaded", "skipped", "gone", "failed"):
                    total_stats[name] += stats[name]

                if stats["downloaded"] > 0:
                    console.print(f"  [green]{source_name}:[/green] {stats['downloaded']} files")

                progress.advance(task)

    # Clean up orphaned files (files that exist locally but that no source
    # produced or keeps this run), unless a failure of ours blocks it
    cleanup = run.cleanup([OUTPUT_DIR], dry_run=dry_run)
    total_stats["deleted"] = len(cleanup.deleted)
    if cleanup.deleted and not dry_run:
        console.print(f"\n[yellow]Deleted {len(cleanup.deleted)} orphaned files[/yellow]")
    if not cleanup.skipped and not dry_run:
        # Prune hash entries whose local file no longer exists
        total_stats["pruned"] = _prune_stale_keys(hashes)

    # Save whenever the hashes or the failure policy's metadata changed (a
    # count or a pending list set on a run with no downloads must persist)
    new_metadata = run.metadata(hashes)
    if not dry_run and (hashes != stored_hashes or load_error is not None
                        or new_metadata != policy_metadata(metadata, POLICY_KEYS)):
        if not _save_hashes(hashes, new_metadata):
            run.error(f"hash_save_failed: {HASH_FILE}")

    # Print summary
    console.print("\n[bold]Summary:[/bold]")
    console.print(f"  Downloaded: [green]{total_stats['downloaded']}[/green]")
    console.print(f"  Skipped (unchanged): [dim]{total_stats['skipped']}[/dim]")
    if total_stats["deleted"] > 0:
        console.print(f"  Deleted (orphaned): [yellow]{total_stats['deleted']}[/yellow]")
    if total_stats["gone"] > 0:
        console.print(f"  Gone (404/410): [yellow]{total_stats['gone']}[/yellow]")
    if total_stats["failed"] > 0:
        console.print(f"  Failed: [red]{total_stats['failed']}[/red]")
    for line in run.summary_lines(cleanup):
        console.print(f"  {line}", markup=False)

    console.print(f"\n[dim]Output directory: {OUTPUT_DIR}[/dim]")

    if not dry_run and total_stats["downloaded"] > 0:
        console.print("\n[yellow]Next step:[/yellow] Run the indexer to add these docs to Meilisearch:")
        console.print("  [dim]cd scripts && python index_to_meilisearch.py[/dim]")

    total_stats["exit_code"] = run.exit_code()
    return total_stats


# =============================================================================
# CLI ENTRY POINT
# =============================================================================

def main() -> int:
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
        return int(stats["exit_code"])
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted[/yellow]")
        return 130
    except Exception as e:
        console.print(f"\n[red]Error:[/red] {e}")
        logger.exception("Unexpected error")
        return 1


if __name__ == "__main__":
    sys.exit(main())
