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
removals (pending_orphans in the hash file's metadata). A Jekyll redirect
stub (front matter redirect_to) is a page that moved: it isn't kept, so its
old file goes with the cleanup.

Exit codes: 0 clean (removals and valve holds included); 1 an error of ours
(a blocked cleanup, a configured directory that failed, a persistent
failure, a failed save, an unexpected exception); 130 interrupted.
"""

import argparse
import asyncio
import logging
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple
from urllib.parse import urljoin

import aiohttp
import yaml  # type: ignore[import-untyped]  # requirements.txt pins PyYAML without its stubs
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

from utilities.docc import DocCPage, catalog_articles, convert_docc, docc_catalog
from utilities.hash_utils import (
    HashFileError,
    compute_hash,
    read_hash_file,
    save_hashes as save_hashes_to_file,
    write_text_atomic,
)
from utilities.source_policy import (
    FAILURE_COUNTS_KEY,
    GITHUB_RAW,
    PENDING_ORPHANS_KEY,
    RENDER_KEY,
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

# Hash-file metadata the failure policy keeps (saved whenever it changes),
# and the render version
POLICY_KEYS = (FAILURE_COUNTS_KEY, PENDING_ORPHANS_KEY, RENDER_KEY)

# The converter's output version: bump it when a change to the conversion
# changes the files of sources that didn't change, so the next clean run
# renders every file again (source_policy's metadata.render)
RENDER_VERSION = 1


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
    # Swift.org website documentation. The API Design Guidelines come from
    # docs.swift.org's DocC copy (scraper/site.py SWIFT_ORG, root
    # apiguidelines), so documentation/api-design-guidelines isn't imported
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


def docc_page(source: DocSource, file_path: str, output_path: Path) -> Optional[DocCPage]:
    """A file's page in its DocC catalog (file_path: its repo path), with the
    catalog's articles as they are on disk now (None outside a catalog).

    DocC finds a <doc:Name> target by name anywhere in the catalog, so the
    articles of every configured source in the same catalog are targets (in
    SOURCES order: the first file with a name wins).
    """
    catalog = docc_catalog(file_path)
    if catalog is None:
        return None
    directories = [
        OUTPUT_DIR / other.output_subdir if other.output_subdir else OUTPUT_DIR
        for other in SOURCES
        if other.repo == source.repo and other.branch == source.branch and docc_catalog(other.path) == catalog
    ]
    return DocCPage(output_path, catalog_articles(directories),
                    f"{GITHUB_RAW}/{source.repo}/{source.branch}/{catalog}/Assets")


def clean_docc_content(content: str, filename: str, docc: Optional[DocCPage] = None) -> str:
    """
    Clean DocC-specific syntax from markdown content.

    Transforms:
    - HTML test comments (remove)
    - DocC markup (utilities/docc.py convert_docc): <doc:> links, in a DocC
      catalog (docc) asset images, @Metadata and @Comment blocks
    """
    # Remove HTML test comments like <!-- test: xxx -->
    content = re.sub(r'<!--\s*test:[^>]*-->', '', content)

    content = convert_docc(content, docc)

    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.strip()


# Jekyll front matter: the YAML between the --- lines that open a page
FRONT_MATTER_PATTERN = re.compile(r'\A---[ \t]*\n(.*?)^---[ \t]*$\n?', re.DOTALL | re.MULTILINE)
# Liquid: raw blocks (kept as they are), comment blocks, and tags and outputs
LIQUID_RAW_PATTERN = re.compile(r'\{%-?\s*raw\s*-?%\}(.*?)\{%-?\s*endraw\s*-?%\}', re.DOTALL)
LIQUID_COMMENT_PATTERN = re.compile(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}', re.DOTALL)
LIQUID_TOKEN_PATTERN = re.compile(r'\{%-?\s*(\w+)(.*?)-?%\}|\{\{-?(.*?)-?\}\}', re.DOTALL)
LIQUID_ASSIGN_PATTERN = re.compile(r'\s*(\w+)\s*=\s*(.*?)\s*$', re.DOTALL)
# A value that is markup (HTML or kramdown), not text
MARKUP_PATTERN = re.compile(r'<[A-Za-z/!]|\{:')
# A kramdown block IAL ({:.class}, {:#id}, {:toc}) on a line of its own, and a class it sets
KRAMDOWN_IAL_PATTERN = re.compile(r'([ \t]*)\{:([^}\n]*)\}[ \t]*')
IAL_CLASS_PATTERN = re.compile(r'(?<!\S)\.([\w-]+)')
LIST_ITEM_PATTERN = re.compile(r'[ \t]*([*+-]|\d+\.)[ \t]')
# A fenced code block's fence line: the fence (``` or ~~~, 3 or more) and the rest of the line
FENCE_PATTERN = re.compile(r'[ \t]*(`{3,}|~{3,})(.*)')
# A root-relative link target: a markdown link's (](/...)) or an HTML href's (href="/...")
ROOT_RELATIVE_LINK_PATTERN = re.compile(r'''(\]\(|\bhref=["'])(/[^\s)"']*)''')
CODE_SPAN_PATTERN = re.compile(r'(`+).+?\1')


def split_front_matter(content: str) -> Tuple[Optional[Dict[str, Any]], str]:
    """A Jekyll page's front matter and its body: (None, content) for a page
    without front matter, or whose front matter can't be read as a YAML
    mapping."""
    match = FRONT_MATTER_PATTERN.match(content)
    if match is None:
        return None, content
    try:
        front_matter = yaml.safe_load(match.group(1))
    except Exception:  # yaml.YAMLError, or e.g. ValueError for an invalid date (date: 2024-13-45)
        return None, content
    if front_matter is None:
        front_matter = {}
    if not isinstance(front_matter, dict):
        return None, content
    return front_matter, content[match.end():]


def redirect_target(content: str) -> Optional[str]:
    """Where a Jekyll redirect stub (front matter redirect_to) sends its
    readers; None for a page."""
    front_matter, _ = split_front_matter(content)
    target = front_matter.get('redirect_to') if front_matter is not None else None
    if isinstance(target, list):
        target = target[0] if target else None
    return str(target) if target else None


def render_liquid(text: str) -> str:
    """A Jekyll page's Liquid, rendered as text.

    Comments are dropped. A variable set by assign (to a quoted string or
    another variable) or capture is output where {{ it }} is, unless its
    value is markup (HTML or kramdown, which the page uses for presentation
    only); an unknown variable outputs nothing, and every other tag is
    dropped. A raw block is kept as it is.
    """
    variables: Dict[str, str] = {}
    parts = LIQUID_RAW_PATTERN.split(text)  # text, raw, text, raw, ..., text
    return ''.join(part if index % 2 else _render_liquid_text(part, variables)
                   for index, part in enumerate(parts))


def _render_liquid_text(text: str, variables: Dict[str, str]) -> str:
    text = LIQUID_COMMENT_PATTERN.sub('', text)
    out: List[str] = []
    capture: Optional[Tuple[str, List[str]]] = None
    position = 0
    for match in LIQUID_TOKEN_PATTERN.finditer(text):
        sink = capture[1] if capture is not None else out
        sink.append(text[position:match.start()])
        position = match.end()
        tag, arguments, expression = match.groups()
        if expression is not None:
            value = variables.get(expression.split('|')[0].strip(), '')
            if not MARKUP_PATTERN.search(value):
                sink.append(value)
        elif tag == 'capture':
            capture = (arguments.strip(), [])
        elif tag == 'endcapture' and capture is not None:
            variables[capture[0]] = ''.join(capture[1])
            capture = None
        elif tag == 'assign':
            assignment = LIQUID_ASSIGN_PATTERN.match(arguments)
            if assignment:
                name, value = assignment.groups()
                if len(value) >= 2 and value[0] in '\'"' and value[-1] == value[0]:
                    variables[name] = value[1:-1]
                else:
                    variables[name] = variables.get(value.split('|')[0].strip(), '')
    (capture[1] if capture is not None else out).append(text[position:])
    if capture is not None:  # never closed: its text stays
        out.extend(capture[1])
    return ''.join(out)


def strip_kramdown_ials(text: str) -> str:
    """Drop the kramdown block IALs on lines of their own, and the list a
    {:toc} IAL is on (kramdown replaces it with the page's table of contents).

    A class IAL on the line right after a fenced code block's closing fence
    styles that block (e.g. swift.org's good and bad examples): it is kept
    as a line naming its classes under the block, "*(bad)*". The lines of a
    code block are code, kept as they are.
    """
    lines: List[str] = []
    fence: Optional[str] = None  # the open code block's fence
    after_fence = False  # the previous line closed a code block
    for line in text.split('\n'):
        closed, after_fence = after_fence, False
        fence_line = FENCE_PATTERN.fullmatch(line)
        if fence is not None:
            lines.append(line)
            # Closed by a fence of its own character, at least as long, alone on its line
            if fence_line is not None and fence_line.group(1).startswith(fence) and not fence_line.group(2).strip():
                fence, after_fence = None, True
            continue
        # Opened by a fence (a ``` fence's info string holds no backtick)
        if fence_line is not None and not (fence_line.group(1)[0] == '`' and '`' in fence_line.group(2)):
            fence = fence_line.group(1)
            lines.append(line)
            continue
        ial = KRAMDOWN_IAL_PATTERN.fullmatch(line)
        if ial is None:
            lines.append(line)
            continue
        indent, attributes = ial.groups()
        classes = IAL_CLASS_PATTERN.findall(attributes)
        if closed and classes:
            lines.append(f"{indent}*({', '.join(classes)})*")
        elif attributes.strip() == 'toc' and lines and LIST_ITEM_PATTERN.match(lines[-1]):
            lines.pop()
    return '\n'.join(lines)


def map_outside_code(text: str, rewrite: Callable[[str], str]) -> str:
    """text with rewrite applied to its prose only: fenced code blocks (with
    their fences) and inline code spans are kept as they are."""
    lines: List[str] = []
    fence: Optional[str] = None  # the open code block's fence
    for line in text.split('\n'):
        fence_line = FENCE_PATTERN.fullmatch(line)
        if fence is not None:
            if fence_line is not None and fence_line.group(1).startswith(fence) and not fence_line.group(2).strip():
                fence = None
            lines.append(line)
            continue
        if fence_line is not None and not (fence_line.group(1)[0] == '`' and '`' in fence_line.group(2)):
            fence = fence_line.group(1)
            lines.append(line)
            continue
        pieces: List[str] = []
        position = 0
        for span in CODE_SPAN_PATTERN.finditer(line):
            pieces += [rewrite(line[position:span.start()]), span.group(0)]
            position = span.end()
        pieces.append(rewrite(line[position:]))
        lines.append(''.join(pieces))
    return '\n'.join(lines)


def clean_jekyll_body(body: str) -> str:
    """A Jekyll page's body without its Liquid (render_liquid), kramdown
    IALs, <style> blocks and the HTML comments left empty."""
    body = render_liquid(body)
    body = re.sub(r'<style\b[^>]*>.*?</style>', '', body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r'<!--\s*-->', '', body)
    body = strip_kramdown_ials(body)
    # Lines left holding only whitespace are blank lines
    body = re.sub(r'^[ \t]+$', '', body, flags=re.MULTILINE)
    body = re.sub(r'\n{3,}', '\n\n', body)
    return body.strip()


def add_source_header(content: str, source: DocSource, file_path: str) -> str:
    """Add a source attribution header to the content (file_path: the
    file's repo-relative path).

    A Jekyll page's front matter is replaced: its url is the page's
    official_url (else its GitHub URL), its title its "# " heading, and its
    body is cleaned (clean_jekyll_body). A root-relative link on a page with
    an official_url is on that page's site: resolved against it.
    """
    url = f"https://github.com/{source.repo}/blob/{source.branch}/{file_path}"
    front_matter, body = split_front_matter(content)
    if front_matter is not None:
        content = clean_jekyll_body(body)
        official_url = front_matter.get('official_url')
        if isinstance(official_url, str) and official_url.startswith(('http://', 'https://')):
            url = official_url
            content = map_outside_code(content, lambda prose: ROOT_RELATIVE_LINK_PATTERN.sub(
                lambda match: match.group(1) + urljoin(official_url, match.group(2)), prose))
        title = front_matter.get('title')
        if isinstance(title, str) and title.strip() and not content.startswith('# '):
            content = f"# {title.strip()}\n\n{content}"
    elif content.startswith('---'):
        logger.warning(f"front_matter_unreadable: {source.repo}:{file_path}; kept as text")

    header = f"""---
source: {source.repo}
url: {url}
---

"""
    return header + content


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
    stats = {"downloaded": 0, "skipped": 0, "gone": 0, "failed": 0, "redirected": 0}
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

        # A Jekyll redirect stub is a page that moved (its target is scraped
        # where a configured directory has it): not reported as produced, so
        # the cleanup removes its old file and its key is pruned
        target = redirect_target(content)
        if target is not None:
            logger.warning(f"source_redirected: {hash_key} redirects to {target}; not kept, "
                           "its old file goes with the cleanup")
            stats["redirected"] += 1
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
            content = clean_docc_content(content, filename, docc_page(source, file_path, output_path))
            content = add_source_header(content, source, file_path)

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
    run = ScrapeRun("Swift", OUTPUT_DIR.parent, metadata, load_error, render_version=RENDER_VERSION)
    if run.render_stale and not force:
        # Rendered by another converter version: every file again, as --force
        console.print(f"[yellow]Render version {RENDER_VERSION}: rendering every file again[/yellow]")
        force = True

    # Ensure output directory exists
    if not dry_run:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_stats: Dict[str, Any] = {"downloaded": 0, "skipped": 0, "gone": 0, "failed": 0, "redirected": 0,
                                   "deleted": 0, "pruned": 0}

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

                for name in ("downloaded", "skipped", "gone", "failed", "redirected"):
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
    # Storing a new render version: a file this run didn't render (e.g. held
    # by the valve) has the old rendering, so its key loses its source hash
    for key in run.unrendered_keys(hashes):
        hashes[key] = ""

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
    if total_stats["redirected"] > 0:
        console.print(f"  Redirected (moved): [yellow]{total_stats['redirected']}[/yellow]")
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
