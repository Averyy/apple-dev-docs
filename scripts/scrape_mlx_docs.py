#!/usr/bin/env python3
"""
MLX and Apple ML Documentation Scraper

Fetches documentation from Apple's ML open source projects:

Sphinx HTML Sites:
- MLX (ml-explore/mlx) - Array framework for Apple silicon
- MLX-Data (ml-explore/mlx-data) - Data loading utilities
- coremltools (apple/coremltools) - Core ML model conversion tools
- apple-fm-sdk (apple/python-apple-fm-sdk) - Foundation Models SDK for Python

GitHub Markdown:
- mlx-lm - LLM inference and fine-tuning, its server and model management
- mlx-c - C API bindings
- mlx-onnx - ONNX support
- mlx-swift, mlx-swift-lm - MLX Swift (READMEs, and the DocC catalogs the Swift Package Index has no rendering of)
- game-porting-toolkit - Metal shader converter docs
- container, sourcekit-lsp, swift-format - their docs directories

Web Pages (configured one by one, no crawl):
- App-Store - App Review Guidelines, App privacy details, User privacy and data use

A GitHub file's HTML comments (editor notes, licence headers) are removed
outside code, and one in a DocC catalog (a *.docc dir) has its DocC markup
converted (utilities/docc.py): its <doc:> links point to the articles of its
own catalog.

A Sphinx signature (an API's <dt class="sig">) is a code block of its text
(```python, MLX's C++ API ```cpp), and a definition that holds blocks (a
parameter list) keeps them.

The Sphinx pages and web pages are fetched with wafer-py, one at a time so
its per-host rate limit spaces them, with its retries; so this script needs
Python 3.12 and requirements-scrape.txt on top of requirements.txt (the
scheduled scrape workflow installs both). The GitHub fetches use aiohttp,
with retries.

Failures follow the policy shared with the HIG and Swift scrapers
(utilities/source_policy.py): a configured Sphinx root, GitHub directory or
file, or web page, that returns 404/410 keeps its files for that run and is
removed on the 2nd consecutive run; any other failure of a configured root,
directory, file or web page keeps its files until it recovers (it never
reaches D8); a page that is no longer linked or listed, or returns 404/410,
is removed at once; other failures and convert/save errors keep the file of
a page we have (its key, or its file on disk) and block the orphan cleanup
for up to 3 runs; a page whose links can't be read keeps its file and
blocks it, uncounted. The
orphan cleanup scans each configured source's top-level dir, plus every
output dir no longer configured (a source dropped from the config, or a
source's old dir after its output_dir changed; metadata.sources) until its
files are gone, with confirm-then-delete for mass removals per dir
(pending_orphans). After a clean run, every hash key this run didn't produce
is pruned, except on a run whose valve held files (their keys wait with them).

Usage:
    python scripts/scrape_mlx_docs.py
    python scripts/scrape_mlx_docs.py --dry-run
    python scripts/scrape_mlx_docs.py --force  # Re-download all files

Exit codes: 0 clean (removals and valve holds included); 1 an error of ours
(a blocked cleanup, a configured source that failed, a persistent failure, a
failed save, an unexpected exception); 130 interrupted.
"""

import argparse
import asyncio
import hashlib
import logging
import posixpath
import re
import sys
import textwrap
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union
from urllib.parse import unquote, urljoin, urlparse, urlunparse

import aiohttp
from bs4 import BeautifulSoup, Comment, PageElement, Tag
from rich.console import Console
from wafer import AsyncSession, WaferError

from utilities.docc import (
    CODE_SPAN_PATTERN,
    FENCE_PATTERN,
    DocCPage,
    catalog_articles,
    convert_docc,
    docc_catalog,
    emphasis,
    strip_html_comments,
)
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
    CleanupResult,
    FetchFailed,
    KeptLocation,
    ScrapeRun,
    discover_github_markdown,
    encode_url,
    fetch_github_raw,
    github_file_url,
    has_file_named,
    is_under,
    policy_metadata,
    quote_path,
    status_failure,
)

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
console = Console()

# =============================================================================
# CONFIGURATION
# =============================================================================

# Output directory (relative to project root)
OUTPUT_BASE = Path(__file__).parent.parent / "documentation"

# A markdown link or image: "!" for an image, its text, its target, its "title"
MARKDOWN_LINK_PATTERN = re.compile(r'(!?)\[([^\]]*)\]\(([^)\s]*)((?:\s+"[^"]*")?)\)')
# A URL's scheme ("https:", "mailto:")
URL_SCHEME_PATTERN = re.compile(r'[A-Za-z][A-Za-z0-9+.-]*:')

# Hash file for incremental updates
HASH_FILE = Path(__file__).parent.parent / ".hashes" / "mlx_docs_hashes.json"

# Rate limiting
REQUEST_DELAY = 0.15  # seconds between requests (Sphinx and web pages: wafer's per-host rate_limit)
MAX_CONCURRENT = 10  # max concurrent requests (GitHub)

# HTTP timeout (GitHub, per attempt)
HTTP_TIMEOUT = aiohttp.ClientTimeout(total=30)

# Sphinx and web pages (wafer): the total budget per page, all retries included, and
# the cap on each attempt (so a hung attempt is retried instead of eating the budget)
SPHINX_TIMEOUT = 120.0
SPHINX_ATTEMPT_TIMEOUT = 30.0
SPHINX_MAX_RETRIES = 3  # wafer's retries for 5xx, connection errors and empty bodies

# GitHub directories that can't contain markdown (Xcode-specific)
XCODE_DIR_SUFFIXES = ('.xcassets', '.xcworkspace', '.xcodeproj', '.playground')

# HTML conversion: heading levels, and the blocks of a list item converted
# block by block (list_item_markdown)
HEADING_TAGS = ('h1', 'h2', 'h3', 'h4', 'h5', 'h6')
BLOCK_TAGS = ('p', 'ul', 'ol', 'pre', 'table', 'blockquote', 'dl', 'div', 'section', 'figure', *HEADING_TAGS)
# A Sphinx signature's code block language, by its domain (the signature's class:
# MLX's C++ API is the cpp domain, the Python APIs the py domain)
SIGNATURE_LANGUAGES = {'py': 'python', 'cpp': 'cpp', 'c': 'c', 'js': 'javascript'}

# Hash-file metadata: each configured source's output dir ({name: output_dir}),
# plus every output dir no longer configured until its files are deleted: a
# source dropped from the config, or a source's old dir after its output_dir
# changed (under "<name>@<old output_dir>": its name records the new dir)
SOURCES_KEY = "sources"
# Hash-file metadata saved whenever it changes
POLICY_KEYS = (FAILURE_COUNTS_KEY, PENDING_ORPHANS_KEY, SOURCES_KEY, RENDER_KEY)

# The converter's output version: bump it when a change to the conversion
# changes the files of pages that didn't change, so the next clean run
# renders every page again (source_policy's metadata.render)
# 4: GitHub files without their HTML comments, their links to repo files
#    we don't take as GitHub URLs; emphasis with its edge
#    whitespace outside the markers and its own asterisks escaped, none on
#    punctuation; Sphinx signatures
#    as code blocks (```python, ```cpp), definitions that hold blocks
#    (parameter lists) kept block by block, a description shared by several
#    signatures written once; table captions
RENDER_VERSION = 4


@dataclass
class SphinxDocSource:
    """Represents a Sphinx documentation site to scrape."""
    name: str  # e.g., "MLX"
    base_url: str  # e.g., "https://ml-explore.github.io/mlx/build/html/"
    output_dir: str  # e.g., "MLX"
    framework: str = ""  # Framework name for indexing (defaults to name)
    # CSS selectors for content extraction, the first match wins (article
    # first: the theme's header bar, with its theme switcher and source
    # links, is in main but outside the article)
    content_selector: str = "article, .body, [role='main'], main"
    # Paths to skip (relative to base_url), each matched where a path
    # segment starts: "search.html" skips search.html and api/search.html,
    # never CharTrie.search.html; "_modules/" everything under _modules
    skip_paths: List[str] = field(default_factory=list)
    # Only include paths matching these patterns (empty = include all)
    include_patterns: List[str] = field(default_factory=list)


@dataclass
class GitHubDocSource:
    """Represents a GitHub repository with markdown documentation."""
    name: str  # e.g., "mlx-lm"
    repo: str  # e.g., "ml-explore/mlx-lm"
    branch: str  # e.g., "main"
    output_dir: str  # e.g., "MLX/mlx-lm"
    framework: str  # e.g., "MLX"
    # Files to fetch (relative to repo root)
    files: List[str] = field(default_factory=list)
    # Directories to crawl for markdown files
    directories: List[str] = field(default_factory=list)
    # Take only the README.md files the directory crawls find (e.g. an
    # examples tree whose other .md files are test data, not docs)
    readme_only: bool = False
    # Directories another scraper's copy replaces, each with that copy's docs
    # dir (under documentation/): crawled only while the copy has no file, so
    # the docs are never missing (active_directories)
    superseded_directories: Dict[str, str] = field(default_factory=dict)


def active_directories(source: "GitHubDocSource", docs_root: Optional[Path] = None) -> List[str]:
    """The directories a GitHub source crawls this run: its directories, and each
    superseded one whose replacement (under docs_root, OUTPUT_BASE by default) holds
    no file yet. Once the replacement exists, the directory isn't crawled and its
    files leave through the normal cleanup; were it ever gone, it is crawled again."""
    root = docs_root or OUTPUT_BASE
    return [*source.directories, *(
        directory for directory, copy in source.superseded_directories.items()
        if not ((root / copy).is_dir() and any((root / copy).rglob("*.md")))
    )]


@dataclass
class WebPageSource:
    """Represents web pages configured one by one (no crawl), each converted
    from its HTML as a Sphinx page is."""
    name: str  # e.g., "App-Store"
    base_url: str  # e.g., "https://developer.apple.com/app-store/"
    output_dir: str  # e.g., "App-Store"
    framework: str  # e.g., "App-Store"
    # The pages, relative to base_url (e.g. "review/guidelines/"); each is
    # saved under its path without the trailing slash (review/guidelines.md)
    pages: List[str] = field(default_factory=list)
    # CSS selectors for content extraction, the first match wins
    content_selector: str = "main"


# The sources whose pages are converted from HTML (html_to_markdown)
HTMLSource = Union[SphinxDocSource, WebPageSource]


# Sphinx documentation sites
SPHINX_SOURCES: List[SphinxDocSource] = [
    SphinxDocSource(
        name="MLX",
        base_url="https://ml-explore.github.io/mlx/build/html/",
        output_dir="MLX",
        framework="MLX",
        skip_paths=["genindex.html", "search.html", "py-modindex.html"],
    ),
    SphinxDocSource(
        name="MLX-Data",
        base_url="https://ml-explore.github.io/mlx-data/build/html/",
        output_dir="MLX/mlx-data",
        framework="MLX",
        skip_paths=["genindex.html", "search.html", "py-modindex.html"],
    ),
    SphinxDocSource(
        name="coremltools",
        base_url="https://apple.github.io/coremltools/docs-guides/",
        output_dir="coremltools",
        framework="coremltools",
        skip_paths=["genindex.html", "search.html"],
    ),
    SphinxDocSource(
        name="apple-fm-sdk",
        base_url="https://apple.github.io/python-apple-fm-sdk/",
        output_dir="apple-fm-sdk",
        framework="apple-fm-sdk",
        # _modules/: the viewcode source pages every API page links as [source]
        skip_paths=["genindex.html", "search.html", "_modules/"],
    ),
]

# GitHub markdown sources
GITHUB_SOURCES: List[GitHubDocSource] = [
    GitHubDocSource(
        name="mlx-lm",
        repo="ml-explore/mlx-lm",
        branch="main",
        output_dir="MLX/mlx-lm",
        framework="MLX",
        files=["README.md", "mlx_lm/LORA.md", "mlx_lm/SERVER.md", "mlx_lm/MANAGE.md",
               "mlx_lm/LEARNED_QUANTS.md", "mlx_lm/BENCHMARKS.md"],
    ),
    GitHubDocSource(
        name="mlx-c",
        repo="ml-explore/mlx-c",
        branch="main",
        output_dir="MLX/mlx-c",
        framework="MLX",
        files=["README.md"],
    ),
    GitHubDocSource(
        name="mlx-onnx",
        repo="ml-explore/mlx-onnx",
        branch="main",
        output_dir="MLX/mlx-onnx",
        framework="MLX",
        files=["README.md"],
    ),
    GitHubDocSource(
        name="mlx-swift",
        repo="ml-explore/mlx-swift",
        branch="main",
        output_dir="MLX-Swift/mlx-swift",
        framework="MLX-Swift",
        # Its DocC catalogs (MLX, MLXNN, MLXOptimizers…) come rendered from
        # the Swift Package Index (scraper/site.py SPI_PACKAGES) once the
        # Apple scrape has written them; until then from here
        files=["README.md"],
        superseded_directories={"Source/MLX/Documentation.docc": "SPI/mlx-swift/MLX"},
    ),
    GitHubDocSource(
        name="mlx-swift-lm",
        repo="ml-explore/mlx-swift-lm",
        branch="main",
        output_dir="MLX-Swift/mlx-swift-lm",
        framework="MLX-Swift",
        files=["README.md"],
        # The catalogs of the libraries that aren't documentation targets on
        # the Swift Package Index, whose rendering of the others (MLXLLM,
        # MLXVLM, MLXLMCommon, MLXEmbedders, MLXScriptedLM) is scraped from
        # there (scraper/site.py SPI_PACKAGES)
        directories=[
            "Libraries/MLXHuggingFace/Documentation.docc",
            "Libraries/MLXRerankers/Documentation.docc",
        ],
        superseded_directories={"Libraries/MLXLMCommon/Documentation.docc": "SPI/mlx-swift-lm/MLXLMCommon"},
    ),
    GitHubDocSource(
        name="game-porting-toolkit",
        repo="apple/game-porting-toolkit",
        branch="main",
        output_dir="game-porting-toolkit",
        framework="game-porting-toolkit",
        directories=["docs"],  # Metal shader converter
    ),
    GitHubDocSource(
        name="container",
        repo="apple/container",
        branch="main",
        output_dir="container",
        framework="container",
        directories=["docs"],
    ),
    GitHubDocSource(
        name="sourcekit-lsp",
        repo="swiftlang/sourcekit-lsp",
        branch="main",
        output_dir="sourcekit-lsp",
        framework="sourcekit-lsp",
        directories=["Documentation"],
    ),
    GitHubDocSource(
        name="swift-format",
        repo="swiftlang/swift-format",
        branch="main",
        output_dir="swift-format",
        framework="swift-format",
        directories=["Documentation"],
    ),
]

# Web pages, configured one by one
WEB_SOURCES: List[WebPageSource] = [
    WebPageSource(
        name="App-Store",
        base_url="https://developer.apple.com/app-store/",
        output_dir="App-Store",
        framework="App-Store",
        pages=["review/guidelines/", "app-privacy-details/", "user-privacy-and-data-use/"],
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
    return save_hashes_to_file(HASH_FILE, hashes, source="scrape_mlx_docs.py", metadata=metadata)


def configured_sources() -> Dict[str, str]:
    """Every configured source's output dir, {name: output_dir} (metadata.sources).

    Raises:
        ValueError: Two sources share a name (their files couldn't be told
            apart), or a web source's pages aren't distinct pages under its
            base URL (web_page_paths)
    """
    sources: Dict[str, str] = {}
    all_sources: List[Union[SphinxDocSource, GitHubDocSource, WebPageSource]] = [
        *SPHINX_SOURCES, *GITHUB_SOURCES, *WEB_SOURCES,
    ]
    for source in all_sources:
        if source.name in sources:
            raise ValueError(f"Duplicate MLX source name: {source.name}")
        sources[source.name] = source.output_dir
    for web_source in WEB_SOURCES:
        web_page_paths(web_source)
    return sources


def web_page_paths(source: WebPageSource) -> Dict[str, Path]:
    """A web source's pages, {url: file}: each page's path under the base
    URL without its trailing slash, as a .md file (review/guidelines/ ->
    review/guidelines.md).

    Raises:
        ValueError: A page outside the base URL, with an unsafe path, or
            whose file another page has (in any casing)
    """
    output_dir = OUTPUT_BASE / source.output_dir
    paths: Dict[str, Path] = {}
    folded: Dict[str, str] = {}
    for page in source.pages:
        url = urljoin(source.base_url, page)
        filepath = None
        if page and url.startswith(source.base_url) and url != source.base_url:
            filepath = url_to_filepath(url.rstrip('/'), source.base_url, output_dir)
        if filepath is None:
            raise ValueError(f"Web source {source.name}: {page!r} is not a page under {source.base_url}")
        other = folded.setdefault(str(filepath).lower(), url)
        if other != url:
            raise ValueError(f"Web source {source.name}: {other} and {url} both map to {filepath}")
        paths[url] = filepath
    return paths


def valid_output_dir(output_dir: Any) -> bool:
    """A stored output dir is safe to scan and clean: a relative path strictly
    inside OUTPUT_BASE (never OUTPUT_BASE itself, never outside it)."""
    if not isinstance(output_dir, str) or not output_dir or "\\" in output_dir:
        return False
    path = PurePosixPath(output_dir)
    if path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        return False
    target = OUTPUT_BASE / output_dir
    return target != OUTPUT_BASE and is_safe_path(OUTPUT_BASE, target)


def source_location(output_dir: str, all_output_dirs: Iterable[str]) -> KeptLocation:
    """A source's files: everything under its output dir except the other
    sources' own dirs nested inside it (strictly: a dir that differs from it
    only in casing, e.g. its own old dir, is not excluded)."""
    path = OUTPUT_BASE / output_dir
    excluded = tuple(sorted({
        OUTPUT_BASE / other for other in all_output_dirs
        if is_under(OUTPUT_BASE / other, path) and not is_under(path, OUTPUT_BASE / other)
    }))
    return KeptLocation(path, reason="", excluded=excluded)


def is_safe_path(base_dir: Path, target_path: Path) -> bool:
    """Check if target_path is safely within base_dir (prevents path traversal)."""
    try:
        resolved_base = base_dir.resolve()
        resolved_target = target_path.resolve()
        return resolved_target.is_relative_to(resolved_base)
    except (ValueError, RuntimeError):
        return False


def normalize_url(base_url: str, href: str) -> Optional[str]:
    """Normalize a URL relative to base, return None if external."""
    if not href or href.startswith('#') or href.startswith('mailto:'):
        return None

    # Handle absolute URLs
    if href.startswith('http://') or href.startswith('https://'):
        # Check if it's within the same site
        base_parsed = urlparse(base_url)
        href_parsed = urlparse(href)
        if href_parsed.netloc != base_parsed.netloc:
            return None  # External link
        return href

    # Relative URL
    return urljoin(base_url, href)


def normalize_link(page_url: str, href: str, source: SphinxDocSource) -> Optional[str]:
    """The page a link on page_url points to, as one canonical URL; None if
    it isn't a page of source.

    Every spelling of a page maps to one URL, so no two URLs map to the same
    file: the #fragment and ?query are stripped (the link is kept), a
    directory (".../") is its index.html, and an extensionless page is its
    .html (the site serves both). Other files (images, sources) are skipped,
    and so is a link whose host part urllib rejects (e.g. a placeholder like
    "http://[your-host]:8080/"): it can't be on the source's own host.
    """
    try:
        normalized = normalize_url(page_url, href)
        if normalized is None:
            return None
        normalized = urlunparse(urlparse(normalized)._replace(query="", fragment=""))
    except ValueError as e:
        logger.debug(f"Skipping malformed link {href!r} on {page_url}: {e}")
        return None

    # Check if within base URL (the base without its trailing slash is the root too)
    if normalized + "/" == source.base_url:
        normalized = source.base_url
    if not normalized.startswith(source.base_url):
        return None

    # Check skip paths (where a path segment starts)
    rel_path = normalized[len(source.base_url):]
    if any(f"/{skip}" in f"/{rel_path}" for skip in source.skip_paths):
        return None

    # Only include .html pages
    name = rel_path.split('/')[-1]
    if not name:
        return normalized + "index.html"
    if name.endswith('.html'):
        return normalized
    if '.' in name:
        return None
    return normalized + ".html"


def sphinx_root_url(source: SphinxDocSource) -> str:
    """A Sphinx source's root page (where discovery starts): its index.html."""
    return urljoin(source.base_url, "index.html")


def url_to_filepath(url: str, base_url: str, output_dir: Path) -> Optional[Path]:
    """Convert a URL to a local file path. Returns None if path is unsafe."""
    # Get path relative to base
    base_parsed = urlparse(base_url)
    url_parsed = urlparse(url)

    # Remove base path prefix
    rel_path = url_parsed.path
    if base_parsed.path and rel_path.startswith(base_parsed.path):
        rel_path = rel_path[len(base_parsed.path):]

    # Clean up path - remove leading slashes and any path traversal attempts
    rel_path = rel_path.lstrip('/')

    # Reject paths with .. sequences
    if '..' in rel_path:
        logger.warning(f"Rejecting path with traversal sequence: {rel_path}")
        return None

    # Change .html to .md
    if rel_path.endswith('.html'):
        rel_path = rel_path[:-5] + '.md'
    elif not rel_path or rel_path.endswith('/'):
        rel_path = rel_path.rstrip('/') + '/index.md' if rel_path else 'index.md'
    else:
        # URLs without extension - add .md
        if '.' not in Path(rel_path).name:
            rel_path = rel_path + '.md'

    filepath = output_dir / rel_path

    # Validate path is within output directory
    if not is_safe_path(output_dir, filepath):
        logger.warning(f"Rejecting unsafe path: {rel_path}")
        return None

    return filepath


def heading_text(heading: Tag) -> str:
    """A heading's text on one line, without its pilcrow/link symbol: its
    words kept apart as rendered ("5. Legal", not "5.Legal"), a
    non-breaking space as a space (a title is matched as typed)."""
    text = ' '.join(heading.get_text().split())
    return re.sub(r'[¶#]$', '', text).strip()


def raise_headings(content: Tag) -> None:
    """Raise the content's headings so that its top level is h2, under the
    page's title (# is the title only): e.g. the App Review Guidelines'
    sections are h3. The indexer splits a large page at its ## headings."""
    headings = [heading for heading in content.find_all(HEADING_TAGS) if heading_text(heading)]
    if not headings:
        return
    shift = min(int(heading.name[1]) for heading in headings) - 2
    if shift > 0:
        for heading in content.find_all(HEADING_TAGS):
            heading.name = f"h{int(heading.name[1]) - shift}"


def html_to_markdown(html: str, source: HTMLSource, url: str) -> str:
    """Convert Sphinx HTML (or a web page's) to clean markdown."""
    soup = BeautifulSoup(html, 'html.parser')

    # Find main content area
    content = None
    for selector in source.content_selector.split(', '):
        content = soup.select_one(selector)
        if content:
            break

    if not content:
        content = soup.body or soup

    # Remove navigation, sidebar, footer elements
    # (a:has(.viewcode-link): a Sphinx [source] link, to a page's Python
    # source, which isn't documentation)
    for selector in ['nav', '.sidebar', '.sphinxsidebar', '.related',
                     '.footer', 'footer', '.headerlink', '.toctree-wrapper',
                     'script', 'style', '.skip-link', '#searchbox', 'a:has(.viewcode-link)']:
        for elem in content.select(selector):
            elem.decompose()
    resolve_links(content, source, url)

    # Convert to markdown
    md_lines = []

    # Extract title: the content's first h1, taken out of the content so it
    # isn't converted a second time (else the page's first h1, outside it)
    content_title = content.find('h1')
    title = content_title or soup.find('h1')
    if isinstance(title, Tag):
        md_lines.append(f"# {heading_text(title)}\n")
    if isinstance(content_title, Tag):
        content_title.decompose()
    raise_headings(content)

    # Process content
    md_content = convert_element_to_markdown(content, url)
    md_lines.append(md_content)

    # Add source header with framework (consistent with GitHub sources)
    framework = source.framework or source.name
    result = f"""---
source: {source.name}
framework: {framework}
url: {encode_url(url)}
---

{"".join(md_lines)}"""

    # Clean up excessive whitespace
    result = re.sub(r'\n{3,}', '\n\n', result)

    return result.strip() + '\n'


def absolute_url(url: str, href: str) -> str:
    """href resolved against the page's URL (url); as it is when urllib
    rejects its host part (e.g. a placeholder like "//[your-host]/x")."""
    try:
        return urljoin(url, href)
    except ValueError:
        return href


def resolve_links(content: Tag, source: HTMLSource, url: str) -> None:
    """Make absolute (against the page's URL) every link that can't point
    to one of our docs: one from the host's root (/path, //host/path; the
    docs don't mirror it), and a relative one to anything but a page of the
    source (a Sphinx index or search page, an image, a download; a web
    page's other pages, which aren't crawled). local_href then leaves them
    as they are."""
    for link in content.find_all('a', href=True):
        href = attribute(link, 'href')
        if not href or href.startswith(('#', 'http://', 'https://', 'mailto:')):
            continue
        if (href.startswith('/') or not isinstance(source, SphinxDocSource)
                or normalize_link(url, href, source) is None):
            link['href'] = absolute_url(url, href)


def local_href(href: str) -> str:
    """A link's target in our docs: a relative link to a page
    (<path>.html, with or without a #fragment) points to its .md file. An
    absolute link (http://, https://, mailto:) is another site's page, and
    a bare #fragment this page's: both are left as they are."""
    if href.startswith(('http://', 'https://', 'mailto:')):
        return href
    path, sep, fragment = href.partition('#')
    if path.endswith('.html'):
        path = path[:-5] + '.md'
    return f"{path}{sep}{fragment}"


def attribute(element: Tag, name: str) -> str:
    """An attribute's value ('' if missing; a multi-valued one, e.g. class,
    space-separated)."""
    value = element.get(name)
    if isinstance(value, list):
        return ' '.join(value)
    return value or ''


def image_markdown(img: Tag, url: str) -> str:
    """An img as markdown ('' without a src). A relative src is resolved
    against the page's URL (a Sphinx page's images are relative to it)."""
    src = attribute(img, 'src')
    if not src:
        return ''
    return f"![{attribute(img, 'alt')}]({absolute_url(url, src)})"


def only_image(link: Tag) -> Optional[Tag]:
    """The img that is a link's only content (whitespace aside), if it is one
    (linked_image_markdown)."""
    children = [child for child in link.children if isinstance(child, Tag) or str(child).strip()]
    if len(children) == 1 and isinstance(children[0], Tag) and children[0].name == 'img':
        return children[0]
    return None


def linked_image_markdown(image: Tag, href: str, url: str) -> str:
    """An img that is a link's only content: the image itself when the link
    points to the image's own file (Sphinx wraps a figure in a link to its
    full-size file), else the image linked to the link's target (e.g. a
    badge, [![alt](src)](href))."""
    markdown = image_markdown(image, url)
    if markdown and href and absolute_url(url, href) != absolute_url(url, attribute(image, 'src')):
        return f"[{markdown}]({local_href(href)})"
    return markdown


def convert_code_block(element: Tag) -> str:
    """A code block (a pre, or an element holding a code) as a fenced block
    on its own lines."""
    code = element.find('code')
    code_elem = code if isinstance(code, Tag) else element
    # Try to detect language from class
    lang = ''
    classes = attribute(code_elem, 'class').split()
    for cls in classes:
        if cls.startswith('language-') or cls.startswith('highlight-'):
            lang = cls.split('-', 1)[1]
            break
        if cls in ['python', 'swift', 'cpp', 'c', 'bash', 'shell', 'json', 'yaml']:
            lang = cls
            break

    code_text = code_elem.get_text()
    # Remove leading/trailing blank lines but preserve internal structure
    code_text = code_text.strip('\n')
    return f"\n```{lang}\n{code_text}\n```\n"


def convert_element_to_markdown(element: PageElement, url: str) -> str:
    """Recursively convert HTML element to markdown (url: the page's URL)."""
    if isinstance(element, Comment):  # An HTML comment is no page text
        return ''
    if not isinstance(element, Tag):  # Text node
        text = str(element)
        # Normalize whitespace but preserve some structure
        return text

    result = []

    # Handle specific tags
    tag = element.name.lower()

    if tag in HEADING_TAGS:
        level = int(tag[1])
        text = heading_text(element)
        if text:
            result.append(f"\n{'#' * level} {text}\n")

    elif tag == 'p':
        text = process_inline_elements(element, url)
        if text.strip():
            result.append(f"\n{text}\n")

    elif tag in ['pre', 'code']:
        if tag == 'pre' or element.find('code'):
            result.append(convert_code_block(element))
        else:
            result.append(f"`{element.get_text()}`")

    elif tag == 'a':
        image = only_image(element)
        href = attribute(element, 'href')
        text = element.get_text(strip=True)
        if image is not None:
            result.append(linked_image_markdown(image, href, url))
        elif href and text:
            result.append(f"[{text}]({local_href(href)})")
        elif text:
            result.append(text)

    elif tag in ['ul', 'ol']:
        for i, li in enumerate(element.find_all('li', recursive=False)):
            prefix = '- ' if tag == 'ul' else f"{i+1}. "
            # The item's lines after the first (a code block, its other
            # blocks) are indented under it
            li_text = list_item_markdown(li, url, indent=' ' * len(prefix))
            if li_text:
                # An item of several blocks is set apart from the next one
                result.append(f"{prefix}{li_text}\n" + ('\n' if holds_blocks(li) else ''))
        result.append('\n')

    elif tag == 'dl':
        # Each dd once, under the dt's before it (an overloaded API's signatures share one)
        language: Optional[str] = None
        for item in element.find_all(['dt', 'dd'], recursive=False):
            if item.name == 'dt':
                language = signature_language(item)
                if language is not None:
                    result.append(f"\n```{language}\n{signature_text(item)}\n```\n")
                else:
                    # Bold, unless it holds its own bold (a list's "**Train**: ..." item)
                    term = process_inline_elements(item, url).strip()
                    result.append(f"\n{term if '**' in term else emphasis(term, '**')}\n")
                continue
            if holds_blocks(item):
                # Its blocks under the term (a field list's parameters keep their bullets)
                result.append(f"\n{list_item_markdown(item, url, indent='')}\n")
            elif language is not None:
                result.append(f"\n{process_inline_elements(item, url).strip()}\n")
            else:
                desc = process_inline_elements(item, url, indent='  ')
                result.append(f": {desc.strip()}\n")

    elif tag == 'blockquote':
        text = process_inline_elements(element, url)
        lines = text.strip().split('\n')
        quoted = '\n'.join(f"> {line}" for line in lines)
        result.append(f"\n{quoted}\n")

    elif tag == 'table':
        result.append(convert_table_to_markdown(element, url))

    elif tag in ['strong', 'b']:
        result.append(emphasized(element, '**'))

    elif tag in ['em', 'i']:
        result.append(emphasized(element, '*'))

    elif tag == 'br':
        result.append('\n')

    elif tag in ['div', 'section', 'article', 'main', 'span']:
        # Container elements - process children
        for child in element.children:
            result.append(convert_element_to_markdown(child, url))

    elif tag == 'img':
        result.append(image_markdown(element, url))

    else:
        # Default: process children
        for child in element.children:
            result.append(convert_element_to_markdown(child, url))

    return ''.join(result)


def emphasized(element: Tag, marker: str) -> str:
    """A strong or em element's text emphasized with marker (utilities/docc.py
    emphasis), its own asterisks escaped: Sphinx's "<strong>*args</strong>"
    read "***args**"."""
    return emphasis(element.get_text().replace('*', '\\*'), marker)


def signature_language(dt: Tag) -> Optional[str]:
    """The code block language of a definition term that is a Sphinx API
    signature (its name, parameters and return type: class "sig", in a
    domain SIGNATURE_LANGUAGES lists); None for any other term (e.g. an
    environment variable's, in Sphinx's std domain), which stays a bold term."""
    classes = attribute(dt, 'class').split()
    if 'sig' not in classes:
        return None
    return next((SIGNATURE_LANGUAGES[name] for name in classes if name in SIGNATURE_LANGUAGES), None)


def signature_text(dt: Tag) -> str:
    """A Sphinx signature's text as code, each of its lines (a C++ template
    line ends at a <br>) on one line: Sphinx marks each parameter, the / and
    * separators included, as emphasis, which as markdown ran into '*/*' and
    '***'."""
    for br in dt.find_all('br'):
        br.replace_with('\n')
    lines = [' '.join(line.split()) for line in dt.get_text().split('\n')]
    text = '\n'.join(line for line in lines if line)
    return re.sub(r'\s+\)', ')', re.sub(r'\(\s+', '(', text))


def holds_blocks(item: Tag) -> bool:
    """Whether a list item (or a definition's description) is converted block
    by block (list_item_markdown): it holds a nested list, a table, a quote
    or a definition list (inline conversion has no case for them), more than
    one paragraph, or a paragraph and inline content beside it (e.g. a
    rule's title before its text)."""
    names = [child.name for child in item.children if isinstance(child, Tag)]
    if any(name in names for name in ('ul', 'ol', 'table', 'blockquote', 'dl')) or names.count('p') > 1:
        return True
    return 'p' in names and any(
        child.get_text(strip=True) if isinstance(child, Tag) else str(child).strip()
        for child in item.children
        if not (isinstance(child, Tag) and child.name in BLOCK_TAGS) and not isinstance(child, Comment)
    )


def list_item_markdown(item: Tag, url: str, indent: str) -> str:
    """A list item's text, its lines after the first indented by indent (its
    bullet's width), so that all of it stays inside the item.

    An item that holds blocks (holds_blocks; e.g. an App Review Guidelines
    rule: its title, its text, its sub-rules in a nested list) is converted
    block by block: each block (a paragraph, a nested list, a code block, a
    table) and each run of inline content between them is a paragraph of
    the item, so the nested list keeps its items. Any other item is one run
    of inline content.
    """
    if not holds_blocks(item):
        return process_inline_elements(item, url, indent=indent).strip()
    parts: List[str] = []
    run: List[PageElement] = []
    for child in [*item.children, None]:
        if child is not None and not (isinstance(child, Tag) and child.name in BLOCK_TAGS):
            run.append(child)
            continue
        text = inline_markdown(run, url).strip()
        if text:
            parts.append(text)
        run = []
        if child is not None:
            text = convert_element_to_markdown(child, url).strip()
            if text:
                parts.append(text)
    first, _, rest = '\n\n'.join(parts).partition('\n')
    return first + ('\n' + textwrap.indent(rest, indent) if rest else '')


def process_inline_elements(element: Tag, url: str, indent: str = '') -> str:
    """Process inline elements within a block (url: the page's URL).

    A code block inside it is fenced on its own lines, each prefixed with
    indent (a list item's: the block stays inside the item).
    """
    return inline_markdown(element.children, url, indent)


def inline_markdown(nodes: Iterable[PageElement], url: str, indent: str = '') -> str:
    """Inline content (process_inline_elements), from a sequence of nodes."""
    result = []
    for child in nodes:
        if isinstance(child, Comment):  # An HTML comment is no page text
            continue
        if not isinstance(child, Tag):  # Text node
            result.append(str(child))
        elif child.name in ['code']:
            result.append(f"`{child.get_text()}`")
        elif child.name in ['strong', 'b']:
            result.append(emphasized(child, '**'))
        elif child.name in ['em', 'i']:
            result.append(emphasized(child, '*'))
        elif child.name == 'a':
            image = only_image(child)
            href = attribute(child, 'href')
            text = child.get_text(strip=True)
            if image is not None:
                result.append(linked_image_markdown(image, href, url))
            else:
                result.append(f"[{text}]({local_href(href)})" if href else text)
        elif child.name == 'img':
            result.append(image_markdown(child, url))
        elif child.name == 'pre':
            result.append(textwrap.indent(convert_code_block(child), indent))
        elif child.name == 'br':
            result.append('\n')
        else:
            result.append(process_inline_elements(child, url, indent))
    return ''.join(result)


def table_cell_text(cell: Tag, url: str) -> str:
    """A table cell's text on one line, its words kept apart as rendered."""
    return ' '.join(process_inline_elements(cell, url).split())


def convert_table_to_markdown(table: Tag, url: str) -> str:
    """Convert HTML table to markdown table (url: the page's URL)."""
    rows = []

    # Process header
    thead = table.find('thead')
    if isinstance(thead, Tag):
        header_cells = [table_cell_text(th, url) for th in thead.find_all(['th', 'td'])]
        if header_cells:
            rows.append('| ' + ' | '.join(header_cells) + ' |')
            rows.append('| ' + ' | '.join(['---'] * len(header_cells)) + ' |')

    # Process body
    tbody = table.find('tbody')
    for tr in (tbody if isinstance(tbody, Tag) else table).find_all('tr'):
        cells = [table_cell_text(td, url) for td in tr.find_all(['td', 'th'])]
        if cells:
            # Add header separator if first row and no thead
            if not thead and len(rows) == 0:
                rows.append('| ' + ' | '.join(cells) + ' |')
                rows.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')
            else:
                rows.append('| ' + ' | '.join(cells) + ' |')

    # Its caption above it (the target of a link to the table: "Quantization modes")
    caption = table.find('caption')
    title = table_cell_text(caption, url) if isinstance(caption, Tag) else ''
    if title:
        rows = [emphasis(title, '**'), '', *rows]
    return '\n' + '\n'.join(rows) + '\n' if rows else ''


# =============================================================================
# GITHUB MARKDOWN SCRAPING
# =============================================================================

async def fetch_github_file(
    session: aiohttp.ClientSession,
    repo: str,
    branch: str,
    path: str
) -> Union[str, FetchFailed]:
    """Fetch raw file content from GitHub (retrying transient failures).

    Returns the content, or FetchFailed with the status (404/410 is a
    removal, anything else a failure of the fetch).
    """
    return await fetch_github_raw(session, repo, branch, path, timeout=HTTP_TIMEOUT)


def github_directory_key(repo: str, directory: str) -> str:
    """The failure-counts key of a GitHub directory (its files' keys start with it)."""
    return f"github:{repo}:{directory}/"


def add_github_source_header(content: str, source: GitHubDocSource, file_path: str) -> str:
    """Add source attribution header to GitHub markdown content."""
    source_url = github_file_url(source.repo, source.branch, file_path)

    # Don't add duplicate header
    if content.startswith('---'):
        return content

    header = f"""---
source: {source.name}
framework: {source.framework}
url: {source_url}
---

"""
    return header + content


def docc_page(source: GitHubDocSource, catalog: str, output_path: Path) -> DocCPage:
    """A GitHub file's page in its DocC catalog (catalog: the catalog's repo
    path), with the catalog's articles as they are on disk now: the .md files
    under its dir in the source's output dir (a discovered file keeps its
    repo path there)."""
    return DocCPage(output_path, catalog_articles([OUTPUT_BASE / source.output_dir / catalog]),
                    f"{GITHUB_RAW}/{source.repo}/{source.branch}/{quote_path(catalog)}/Assets")


def repo_links(content: str, source: GitHubDocSource, file_path: str, fetched: Iterable[str]) -> str:
    """A GitHub file's relative links (a link's or an image's, repo-relative when they
    start with "/", as on GitHub) to repo files we don't take (a CONTRIBUTING.md, an
    example's source, a directory) as their GitHub URL: the file's page, an image's
    raw file. A link to a file the source takes (fetched: their repo paths) stays
    relative: its file is at the same path in the source's output dir. Code is left
    as it is (fenced blocks, code spans), and so is a link that leaves the repo."""
    taken = set(fetched)
    base = posixpath.dirname(file_path)

    def absolute(match: "re.Match[str]") -> str:
        image, label, target, title = match.groups()
        if not target or target.startswith('#') or URL_SCHEME_PATTERN.match(target):
            return match.group(0)
        path, hash_mark, fragment = target.partition('#')
        path = path.partition('?')[0]
        repo_path = posixpath.normpath(unquote(path.lstrip('/')) if path.startswith('/')
                                       else posixpath.join(base, unquote(path)))
        if repo_path in taken or repo_path.startswith('..') or repo_path == '.':
            return match.group(0)
        kind = 'raw' if image else 'blob'
        url = f"https://github.com/{source.repo}/{kind}/{source.branch}/{quote_path(repo_path)}"
        return f"{image}[{label}]({url}{hash_mark}{fragment}{title})"

    lines = content.split('\n')
    fence: Optional[str] = None
    for index, line in enumerate(lines):
        fence_match = FENCE_PATTERN.match(line)
        if fence is not None:
            if fence_match and fence_match.group(1)[0] == fence[0] and len(fence_match.group(1)) >= len(fence) \
                    and not fence_match.group(2).strip():
                fence = None
            continue
        if fence_match:
            fence = fence_match.group(1)
            continue
        # A link that starts inside a code span is code; one whose text is a
        # code span ([`Token.swift`](…)) is a link
        spans = [span.span() for span in CODE_SPAN_PATTERN.finditer(line)]

        def outside_code(match: "re.Match[str]") -> str:
            if any(start <= match.start() < end for start, end in spans):
                return match.group(0)
            return absolute(match)

        lines[index] = MARKDOWN_LINK_PATTERN.sub(outside_code, line)
    return '\n'.join(lines)


def validate_github_path(file_path: str) -> bool:
    """Validate that a GitHub file path is safe (no path traversal)."""
    # Reject paths with .. sequences
    if '..' in file_path:
        logger.warning(f"Rejecting GitHub path with traversal sequence: {file_path}")
        return False
    # Reject absolute paths
    if file_path.startswith('/'):
        logger.warning(f"Rejecting absolute GitHub path: {file_path}")
        return False
    return True


async def scrape_github_source(
    session: aiohttp.ClientSession,
    source: GitHubDocSource,
    hashes: Dict[str, str],
    run: ScrapeRun,
    dry_run: bool = False,
    force: bool = False
) -> Dict[str, int]:
    """Scrape a GitHub markdown documentation source, reporting every outcome to run."""
    stats = {"downloaded": 0, "skipped": 0, "gone": 0, "failed": 0}

    output_dir = OUTPUT_BASE / source.output_dir

    # Collect all files to fetch: repo path -> whether it is a configured file
    files_to_fetch: Dict[str, bool] = {file_path: True for file_path in source.files}

    # Discover files in directories (in parallel)
    directories = active_directories(source)
    if directories:
        results = await asyncio.gather(*(
            discover_github_markdown(
                session, source.repo, source.branch, directory,
                skip_dir_suffixes=XCODE_DIR_SUFFIXES, delay=REQUEST_DELAY, timeout=HTTP_TIMEOUT,
            )
            for directory in directories
        ))
        for directory, (discovered, failures) in zip(directories, results, strict=True):
            directory_key = github_directory_key(source.repo, directory)
            # The configured directory itself: on failure nothing of it was found
            root_failure = failures.pop(directory, None)
            if root_failure is not None:
                run.source_failed(directory_key, root_failure, KeptLocation(output_dir / directory, reason=""),
                                  key_prefix=directory_key)
                stats["gone" if root_failure.gone else "failed"] += 1
                continue
            run.source_ok(directory_key)
            # Subdirectories found by a listing
            for subdirectory, failure in sorted(failures.items()):
                subdirectory_key = github_directory_key(source.repo, subdirectory)
                run.directory_failed(subdirectory_key, failure, KeptLocation(output_dir / subdirectory, reason=""),
                                     key_prefix=subdirectory_key)
                stats["gone" if failure.gone else "failed"] += 1
            for file_path in discovered:
                if source.readme_only and PurePosixPath(file_path).name.lower() != "readme.md":
                    continue
                files_to_fetch.setdefault(file_path, False)

    console.print(f"  Found {len(files_to_fetch)} markdown files")

    for file_path, configured in files_to_fetch.items():
        # Validate path is safe
        if not validate_github_path(file_path):
            logger.warning(f"unsafe_path_skipped: {source.repo}:{file_path}")
            continue

        # Determine output path
        # Convert path like "mlx_lm/LORA.md" to "LORA.md" (flatten structure a bit)
        filename = Path(file_path).name
        if "/" in file_path:
            # Keep subdirectory structure for discovered files
            rel_path = file_path
        else:
            rel_path = filename

        output_path = output_dir / rel_path

        # Validate output path is within output directory
        if not is_safe_path(output_dir, output_path):
            logger.warning(f"unsafe_path_skipped: {output_path}")
            continue

        hash_key = f"github:{source.repo}:{file_path}"

        # Fetch content
        content = await fetch_github_file(
            session, source.repo, source.branch, file_path
        )

        if isinstance(content, FetchFailed):
            stats["gone" if content.gone else "failed"] += 1
            if configured:
                # A configured file is a source: only 404/410 x2 removes it, never D8
                kept = run.configured_file_failed(hash_key, content, output_path)
            else:
                # A file we have: its key, or its file (a lost hash file loses keys, not files)
                kept = run.page_failed(hash_key, content,
                                       previously_good=hash_key in hashes or has_file_named(output_path))
            if kept:
                run.keep_file(hash_key, output_path)
            continue
        run.page_ok(hash_key, output_path)

        await asyncio.sleep(REQUEST_DELAY)

        # Check if content changed (re-download if the local file vanished)
        content_hash = compute_hash(content)
        if not force and hash_key in hashes and hashes[hash_key] == content_hash and output_path.exists():
            run.page_saved(hash_key)
            stats["skipped"] += 1
            continue

        # Convert and save; an error here is ours: the file is kept, never deleted
        try:
            # Its HTML comments removed (outside code); a DocC catalog's page: its
            # DocC markup converted, within its own catalog
            content = strip_html_comments(content)
            catalog = docc_catalog(file_path)
            if catalog is not None:
                content = convert_docc(content, docc_page(source, catalog, output_path))
            content = repo_links(content, source, file_path, files_to_fetch)

            # Add source header
            content = add_github_source_header(content, source, file_path)

            if dry_run:
                console.print(f"  [dim]Would write:[/dim] {output_path}")
            else:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                write_text_atomic(output_path, content)  # a failed write keeps the old doc
                hashes[hash_key] = content_hash
        except Exception as e:
            run.local_error(hash_key, output_path, f"{type(e).__name__}: {e}")
            stats["failed"] += 1
            continue

        run.page_saved(hash_key)
        stats["downloaded"] += 1

    return stats


# =============================================================================
# SPHINX HTML CRAWLING
# =============================================================================

class DuplicatePathError(ValueError):
    """Two page URLs map to the same output file (a bug of ours)."""


async def fetch_page(session: AsyncSession, url: str) -> Union[str, FetchFailed]:
    """Fetch a single page (wafer retries 5xx and connection errors, and
    rotates its identity on a 403 or challenge).

    Returns the HTML, or FetchFailed with the status (404/410 is a removal).
    """
    try:
        response = await session.get(url, timeout=SPHINX_TIMEOUT, attempt_timeout=SPHINX_ATTEMPT_TIMEOUT)
    except WaferError as e:
        # Timeout, connection error, challenge, rate limit or empty body after all retries
        status = getattr(e, "status_code", None)
        logger.warning(f"Error fetching {url}: {type(e).__name__}: {e}")
        return FetchFailed(
            status=status if isinstance(status, int) else None,
            error=f"{type(e).__name__}: {e}",
            transient=True,
        )
    if response.ok:
        html: str = response.text
        return html
    if response.status_code not in (404, 410):
        logger.warning(f"HTTP {response.status_code} for {url}")
    return status_failure(response.status_code)


def extract_links(html: str, url: str, source: SphinxDocSource) -> List[str]:
    """The source's pages a page links to (normalize_link)."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        link = normalize_link(url, a['href'], source)
        if link is not None:
            links.append(link)
    return links


async def discover_pages(
    session: AsyncSession,
    source: SphinxDocSource,
    start_url: str,
) -> Tuple[Dict[str, str], Dict[str, FetchFailed], Dict[str, str]]:
    """Discover all pages by crawling from start URL, fetching each once.

    The pages are fetched one at a time: wafer's rate_limit spaces a request
    from the previous one to its host only when they don't overlap
    (concurrent requests would all wait on the same last request and go out
    together).

    Returns:
        ({url: html} for every page that loaded, {url: failure} for every
        page that didn't, {url: error} for every page that loaded but whose
        links couldn't be read; the links of the last two are unknown this run)
    """
    to_visit = deque([start_url])
    queued = {start_url}
    pages: Dict[str, str] = {}
    failures: Dict[str, FetchFailed] = {}
    unprocessed: Dict[str, str] = {}

    while to_visit:
        url = to_visit.popleft()
        result = await fetch_page(session, url)
        if isinstance(result, FetchFailed):
            failures[url] = result
            continue
        try:
            links = extract_links(result, url, source)
        except Exception as e:
            # A bug of ours, raised before the page's links were read: the
            # rest of the crawl goes on, and the page keeps its file and
            # blocks the cleanup (ScrapeRun.unprocessed)
            unprocessed[url] = f"{type(e).__name__}: {e}"
            continue
        pages[url] = result
        for link in links:
            if link not in queued:
                queued.add(link)
                to_visit.append(link)

    return pages, failures, unprocessed


def collision_path(path: Path, output_dir: Path) -> Path:
    """A page's file name in a case-insensitive collision set: its stem plus a
    suffix derived from its own relative path (url_to_filepath's)."""
    suffix = hashlib.sha1(str(path.relative_to(output_dir)).encode()).hexdigest()[:5]
    return path.with_name(f"{path.stem}-{suffix}{path.suffix}")


def other_name(url: str, planned: Path, source: SphinxDocSource, output_dir: Path) -> Optional[Path]:
    """A page's other file name: with its collision suffix when it is planned
    without it, else without it (None if its path is unsafe).

    A page has two names (plan_paths adds the suffix only while another page
    collides with it), so a collision partner added or removed upstream
    moves the page to its other name; until it is written there, its doc is
    under the old one.
    """
    unsuffixed = url_to_filepath(url, source.base_url, output_dir)
    if unsuffixed is None:
        return None
    return collision_path(unsuffixed, output_dir) if planned == unsuffixed else unsuffixed


def has_page_file(url: str, source: SphinxDocSource, output_dir: Path) -> bool:
    """A file of the page is on disk under one of its two names (other_name),
    exactly (has_file_named): a page we have, also when its hash key was lost."""
    unsuffixed = url_to_filepath(url, source.base_url, output_dir)
    return unsuffixed is not None and any(
        has_file_named(path) for path in (unsuffixed, collision_path(unsuffixed, output_dir))
    )


def keep_unwritten_page(run: ScrapeRun, url: str, planned: Path, source: SphinxDocSource, output_dir: Path) -> None:
    """Also keep the file under the other name of a page this run keeps
    without writing it (its fetch failed, it failed to convert or save, its
    links couldn't be read), if there is one (other_name).

    A file under the planned name (left by an earlier run under that name)
    may be older than the one under the other name, so whether the planned
    file exists doesn't tell which one holds the doc: both are kept.
    """
    other = other_name(url, planned, source, output_dir)
    if other is not None and has_file_named(other):
        logger.info(f"previous_name_kept: {run.rel(other)} may hold {url} until it is written as {run.rel(planned)}")
        run.expect(other)


def plan_paths(urls: Iterable[str], source: SphinxDocSource, output_dir: Path) -> Dict[str, Optional[Path]]:
    """Map every page to its target file (None if its path is unsafe).

    Raises:
        DuplicatePathError: Two URLs map to the same file
    """
    # Map every page to its target file, disambiguating names that collide
    # case-insensitively (e.g. mlx.core.PrintOptions vs mlx.core.printoptions)
    # so the tree stays usable on case-insensitive filesystems. EVERY member
    # of a collision set gets a suffix derived from its own relative path —
    # per-page deterministic, so set membership changes never rename siblings
    # that stay in a set (a page that leaves or joins one drops or gains its
    # suffix: other_name, keep_unwritten_page, and scrape_source's skip check).
    planned: Dict[str, Optional[Path]] = {
        url: url_to_filepath(url, source.base_url, output_dir) for url in sorted(urls)
    }
    by_folded: Dict[str, List[str]] = {}
    for page_url, fp in planned.items():
        if fp is not None:
            by_folded.setdefault(str(fp).lower(), []).append(page_url)
    for colliding in by_folded.values():
        if len(colliding) < 2:
            continue
        for page_url in colliding:
            fp = planned[page_url]
            assert fp is not None
            planned[page_url] = collision_path(fp, output_dir)

    # Links are normalized (normalize_link), so no two URLs may share a file
    by_path: Dict[Path, str] = {}
    for page_url, fp in planned.items():
        if fp is None:
            continue
        if fp in by_path:
            raise DuplicatePathError(f"{by_path[fp]} and {page_url} both map to {fp}")
        by_path[fp] = page_url
    return planned


def write_page(run: ScrapeRun, filepath: Path, markdown: str) -> None:
    """Write a converted page under exactly its name (a failed write keeps the old doc)."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    if filepath.is_file() and not has_file_named(filepath):
        # A case-insensitive filesystem: a file named in another
        # casing is this same path, and writing would overwrite it
        # but keep its name, so it is replaced by one with this name
        logger.info(f"case_twin_replaced: {run.rel(filepath)} was held by a file named in another casing")
        filepath.unlink()
    write_text_atomic(filepath, markdown)


async def scrape_source(
    session: AsyncSession,
    source: SphinxDocSource,
    hashes: Dict[str, str],
    run: ScrapeRun,
    location: KeptLocation,
    dry_run: bool = False,
    force: bool = False
) -> Dict[str, int]:
    """Scrape a single documentation source, reporting every outcome to run.

    Args:
        location: The source's files (kept whole when its root fails)
    """
    stats = {"downloaded": 0, "skipped": 0, "gone": 0, "failed": 0}

    output_dir = OUTPUT_BASE / source.output_dir
    root_url = sphinx_root_url(source)
    root_key = f"{source.name}:{root_url}"

    console.print(f"\n[cyan]Discovering pages for {source.name}...[/cyan]")

    # Discover all pages
    pages, failures, unprocessed = await discover_pages(session, source, root_url)

    # The configured root: on failure nothing of the source was found
    root_failure = failures.pop(root_url, None)
    if root_failure is not None:
        run.source_failed(root_key, root_failure, location, key_prefix=f"{source.name}:")
        stats["gone" if root_failure.gone else "failed"] += 1
        return stats
    run.source_ok(root_key)

    console.print(f"  Found {len(pages)} pages" + (f" ({len(failures)} more not fetched)" if failures else "")
                  + (f" ({len(unprocessed)} more whose links couldn't be read)" if unprocessed else ""))

    # Pages that failed: removed (404/410), or kept and blocking (page_failed)
    kept_failed: List[str] = []
    for url, failure in sorted(failures.items()):
        stats["gone" if failure.gone else "failed"] += 1
        hash_key = f"{source.name}:{url}"
        # A page we have: its key, or its file under either name (a lost hash file loses keys, not files)
        previously_good = hash_key in hashes or has_page_file(url, source, output_dir)
        if run.page_failed(hash_key, failure, previously_good=previously_good):
            kept_failed.append(url)

    try:
        planned = plan_paths([*pages, *kept_failed, *unprocessed], source, output_dir)
    except DuplicatePathError as e:
        run.error(f"duplicate_output_path: {source.name}: {e}")
        run.keep_location(KeptLocation(location.path, "duplicate_output_path", location.excluded),
                          key_prefix=f"{source.name}:")
        return stats

    for url in kept_failed:
        filepath = planned[url]
        if filepath is not None:
            run.keep_file(f"{source.name}:{url}", filepath)
            keep_unwritten_page(run, url, filepath, source, output_dir)

    # Pages whose links couldn't be read: kept as they are (not converted)
    # and blocking, uncounted, as HIG's (the outer except of the plan's
    # "links first" rule): lifting it would orphan their live children
    for url, error in sorted(unprocessed.items()):
        stats["failed"] += 1
        hash_key = f"{source.name}:{url}"
        filepath = planned[url]
        if filepath is not None:
            run.page_ok(hash_key, filepath)  # its fetch did succeed
            keep_unwritten_page(run, url, filepath, source, output_dir)
        run.unprocessed(hash_key, filepath, error)

    # Process each page
    for url in sorted(pages):
        filepath = planned[url]

        # Skip if path validation failed
        if filepath is None:
            logger.warning(f"unsafe_path_skipped: {url}")
            continue

        hash_key = f"{source.name}:{url}"
        run.page_ok(hash_key, filepath)
        html = pages[url]

        # Check if content changed (hash the HTML). The stored hash says this
        # content was written, not under which of the page's two names
        # (plan_paths), so only honor the skip when the planned file exists
        # under exactly its name and the other name holds no file (left by a
        # blocked or held cleanup, it may hold the newer content). Otherwise a
        # renamed target (collision disambiguation), a deleted file, or a case
        # twin's leftover that a case-insensitive filesystem reports under the
        # planned name would never be written.
        content_hash = compute_hash(html)
        other = other_name(url, filepath, source, output_dir)
        if (not force and hash_key in hashes and hashes[hash_key] == content_hash and has_file_named(filepath)
                and not (other is not None and has_file_named(other))):
            run.page_saved(hash_key)
            stats["skipped"] += 1
            continue

        # Convert and save; an error here is ours: the file is kept, never deleted
        try:
            markdown = html_to_markdown(html, source, url)

            if dry_run:
                console.print(f"  [dim]Would write:[/dim] {filepath}")
            else:
                write_page(run, filepath, markdown)
                hashes[hash_key] = content_hash
        except Exception as e:
            run.local_error(hash_key, filepath, f"{type(e).__name__}: {e}")
            keep_unwritten_page(run, url, filepath, source, output_dir)
            stats["failed"] += 1
            continue

        run.page_saved(hash_key)
        stats["downloaded"] += 1

    return stats


# =============================================================================
# WEB PAGES
# =============================================================================

async def scrape_web_source(
    session: AsyncSession,
    source: WebPageSource,
    hashes: Dict[str, str],
    run: ScrapeRun,
    dry_run: bool = False,
    force: bool = False
) -> Dict[str, int]:
    """Scrape a source's configured web pages, reporting every outcome to run.

    Nothing is crawled: each page is a configured file (it may be all its
    source has), so a 404/410 keeps its file for that run and removes it on
    the 2nd consecutive run, and any other failure keeps it until it
    recovers (ScrapeRun.configured_file_failed).
    """
    stats = {"downloaded": 0, "skipped": 0, "gone": 0, "failed": 0}

    console.print(f"  {len(source.pages)} configured pages")

    for url, filepath in web_page_paths(source).items():
        hash_key = f"{source.name}:{url}"
        html = await fetch_page(session, url)
        if isinstance(html, FetchFailed):
            stats["gone" if html.gone else "failed"] += 1
            if run.configured_file_failed(hash_key, html, filepath):
                run.keep_file(hash_key, filepath)
            continue
        run.page_ok(hash_key, filepath)

        # Convert and save; an error here is ours: the file is kept, never deleted
        try:
            markdown = html_to_markdown(html, source, url)

            # Check if content changed: the markdown is hashed, not the HTML,
            # which changes between requests in parts the conversion drops
            # (e.g. a script URL's cache-busting query). Re-written if the
            # file isn't there under exactly its name.
            content_hash = compute_hash(markdown)
            if (not force and hash_key in hashes and hashes[hash_key] == content_hash
                    and has_file_named(filepath)):
                run.page_saved(hash_key)
                stats["skipped"] += 1
                continue

            if dry_run:
                console.print(f"  [dim]Would write:[/dim] {filepath}")
            else:
                write_page(run, filepath, markdown)
                hashes[hash_key] = content_hash
        except Exception as e:
            run.local_error(hash_key, filepath, f"{type(e).__name__}: {e}")
            stats["failed"] += 1
            continue

        run.page_saved(hash_key)
        stats["downloaded"] += 1

    return stats


# =============================================================================
# SOURCES AND CLEANUP
# =============================================================================

def stored_sources(metadata: Dict[str, Any]) -> Dict[str, str]:
    """metadata.sources as saved, without entries that are malformed or unsafe to clean."""
    stored = metadata.get(SOURCES_KEY)
    if stored is None:
        return {}
    if not isinstance(stored, dict):
        logger.warning(f"Ignoring malformed metadata.{SOURCES_KEY} in {HASH_FILE}")
        return {}
    sources: Dict[str, str] = {}
    for name, output_dir in stored.items():
        if isinstance(name, str) and valid_output_dir(output_dir):
            sources[name] = output_dir
        else:
            logger.warning(f"Ignoring metadata.{SOURCES_KEY} entry {name!r}: {output_dir!r} is not a safe output dir")
    return sources


def dropped_sources(stored: Dict[str, str], configured: Dict[str, str]) -> Dict[str, str]:
    """The stored output dirs that no configured source has any more,
    {name: output_dir}: a source dropped from the config, or the old dir of a
    source whose output_dir changed (named "<name>@<old output_dir>", since
    its own name now records its new dir). Dirs are compared exactly: one
    renamed only in casing is another dir on a case-sensitive filesystem."""
    configured_dirs = set(configured.values())
    dropped: Dict[str, str] = {}
    for name, output_dir in stored.items():
        if output_dir in configured_dirs:
            continue
        dropped[f"{name}@{output_dir}" if name in configured else name] = output_dir
    return dropped


def scan_dirs(configured: Dict[str, str], dropped: Dict[str, str]) -> List[Path]:
    """The dirs the orphan cleanup scans: each configured source's top-level
    dir, and each dropped source's own dir (never a shared parent)."""
    dirs = {OUTPUT_BASE / Path(output_dir).parts[0] for output_dir in configured.values()}
    dirs.update(OUTPUT_BASE / output_dir for output_dir in dropped.values())
    return sorted(dirs)


def _md_files(directory: Path) -> Dict[Tuple[int, int], Path]:
    """The .md files under a dir, by directory entry (st_dev, st_ino)."""
    files: Dict[Tuple[int, int], Path] = {}
    if directory.is_dir():
        for file in directory.rglob("*.md"):
            if file.is_file():
                entry = file.lstat()
                files[(entry.st_dev, entry.st_ino)] = file
    return files


def dropped_source_files(output_dir: str, configured: Dict[str, str]) -> List[Path]:
    """The .md files a dropped source still has: those under its own dir that
    no configured source's dir (nested in it, or the same) holds.

    Told apart by directory entry, not by name: a configured dir that differs
    from it only in casing holds its files only where the filesystem makes it
    the same dir (macOS); on a case-sensitive one (CI) they are the old files.
    """
    path = OUTPUT_BASE / output_dir
    files = _md_files(path)
    for other in configured.values():
        if is_under(OUTPUT_BASE / other, path):
            for entry in _md_files(OUTPUT_BASE / other):
                files.pop(entry, None)
    return sorted(files.values())


def prune_hashes(hashes: Dict[str, str], run: ScrapeRun, cleanup: CleanupResult) -> int:
    """After a clean run, drop every key this run didn't produce or keep
    (removed pages, renamed paths, sources dropped from the config, stale
    keys). Returns how many were dropped.

    Not on a run whose valve held files: a key can't be mapped back to its
    file (the Sphinx collision suffixes; a dropped GitHub source's repo isn't
    stored), so every key waits until the run that deletes the held files or
    finds them linked again. Otherwise a held page linked again would look
    new (a 403 on it wouldn't block, and its file would be deleted) and be
    rewritten, and a dropped source's keys would go before its files.
    """
    if cleanup.held:
        logger.info(f"prune_deferred: the valve holds files this run ({', '.join(sorted(cleanup.held))}); "
                    "hash keys are pruned on the run that deletes them")
        return 0
    stale = [key for key in hashes if key not in run.produced and not run.keeps_key(key)]
    for key in stale:
        del hashes[key]
    return len(stale)


def add_stats(total_stats: Dict[str, Any], stats: Dict[str, int]) -> None:
    """Add a source's stats to the run's totals, and print them."""
    for name in ("downloaded", "skipped", "gone", "failed"):
        total_stats[name] += stats[name]

    console.print(f"  [green]Downloaded:[/green] {stats['downloaded']}")
    console.print(f"  [dim]Skipped:[/dim] {stats['skipped']}")
    if stats["gone"] > 0:
        console.print(f"  [yellow]Gone (404/410):[/yellow] {stats['gone']}")
    if stats["failed"] > 0:
        console.print(f"  [red]Failed:[/red] {stats['failed']}")


async def scrape_all(dry_run: bool = False, force: bool = False) -> Dict[str, Any]:
    """Scrape all configured documentation sources.

    Returns:
        The run's totals, with "exit_code" (0 clean, 1 an error of ours)
    """
    console.print("\n[bold blue]MLX / coremltools Documentation Scraper[/bold blue]\n")

    configured = configured_sources()

    # Load existing hashes (also with --force: the failure policy needs to
    # know which files we already have; --force only rewrites unchanged ones)
    hashes, metadata, load_error = _load_hash_file()
    stored_hashes = dict(hashes)
    run = ScrapeRun("MLX", OUTPUT_BASE, metadata, load_error, render_version=RENDER_VERSION)
    if run.render_stale and not force:
        # Rendered by another converter version: every page again, as --force
        console.print(f"[yellow]Render version {RENDER_VERSION}: rendering every page again[/yellow]")
        force = True

    # Output dirs no longer configured (a source dropped from the config, or
    # moved to another output_dir) are cleaned until their files are gone
    dropped = dropped_sources(stored_sources(metadata), configured)
    all_output_dirs = [*configured.values(), *dropped.values()]

    total_stats: Dict[str, Any] = {"downloaded": 0, "skipped": 0, "gone": 0, "failed": 0, "deleted": 0, "pruned": 0}

    connector = aiohttp.TCPConnector(limit=MAX_CONCURRENT)
    async with AsyncSession(rate_limit=REQUEST_DELAY, max_retries=SPHINX_MAX_RETRIES) as wafer_session, \
            aiohttp.ClientSession(connector=connector) as session:
        # Scrape Sphinx HTML documentation sites
        console.print("[bold cyan]═══ Sphinx HTML Documentation ═══[/bold cyan]")
        for sphinx_source in SPHINX_SOURCES:
            console.print(f"\n[bold]{sphinx_source.name}[/bold] ({sphinx_source.base_url})")

            stats = await scrape_source(
                wafer_session, sphinx_source, hashes, run,
                source_location(sphinx_source.output_dir, all_output_dirs), dry_run=dry_run, force=force
            )

            add_stats(total_stats, stats)

        # Scrape GitHub markdown documentation
        console.print("\n[bold cyan]═══ GitHub Markdown Documentation ═══[/bold cyan]")
        for github_source in GITHUB_SOURCES:
            console.print(f"\n[bold]{github_source.name}[/bold] (github.com/{github_source.repo})")

            stats = await scrape_github_source(
                session, github_source, hashes, run, dry_run=dry_run, force=force
            )

            add_stats(total_stats, stats)

        # Scrape the configured web pages
        console.print("\n[bold cyan]═══ Web Pages ═══[/bold cyan]")
        for web_source in WEB_SOURCES:
            console.print(f"\n[bold]{web_source.name}[/bold] ({web_source.base_url})")

            stats = await scrape_web_source(
                wafer_session, web_source, hashes, run, dry_run=dry_run, force=force
            )

            add_stats(total_stats, stats)

    # Clean up orphaned files, unless a failure of ours blocks it: in each
    # scanned dir, every .md file this run neither produced nor keeps
    for name, output_dir in dropped.items():
        logger.info(f"source_dropped: {name} is no longer configured; cleaning {output_dir}")
    cleanup = run.cleanup(
        scan_dirs(configured, dropped),
        removable_dirs=[OUTPUT_BASE / output_dir for output_dir in dropped.values()],
        dry_run=dry_run,
    )
    total_stats["deleted"] = len(cleanup.deleted)
    if cleanup.deleted and not dry_run:
        console.print(f"\n[yellow]Deleted {len(cleanup.deleted)} orphaned files[/yellow]")
    if not cleanup.skipped and not dry_run:
        total_stats["pruned"] = prune_hashes(hashes, run, cleanup)
    # Storing a new render version: a file this run didn't render (e.g. held
    # by the valve) has the old rendering, so its key loses its source hash
    for key in run.unrendered_keys(hashes):
        hashes[key] = ""

    # A dropped output dir stays in metadata.sources until its files are gone,
    # so the next run still scans it (e.g. while the valve holds them)
    sources = dict(configured)
    for name, output_dir in dropped.items():
        if dropped_source_files(output_dir, configured):
            sources[name] = output_dir
        else:
            logger.info(f"source_removed: {name} ({output_dir}) has no files left; dropped from metadata.{SOURCES_KEY}")

    # Save whenever the hashes or this metadata changed (a count, a pending
    # list or a source set on a run with no downloads must persist)
    new_metadata = {SOURCES_KEY: sources, **run.metadata(hashes)}
    if not dry_run and (hashes != stored_hashes or load_error is not None
                        or new_metadata != policy_metadata(metadata, POLICY_KEYS)):
        if not _save_hashes(hashes, new_metadata):
            run.error(f"hash_save_failed: {HASH_FILE}")

    # Print summary
    console.print("\n[bold]Summary:[/bold]")
    console.print(f"  [dim]Output directory:[/dim] {OUTPUT_BASE}")
    console.print(f"  Downloaded: [green]{total_stats['downloaded']}[/green]")
    console.print(f"  Skipped (unchanged): [dim]{total_stats['skipped']}[/dim]")
    if total_stats["deleted"] > 0:
        console.print(f"  Deleted (orphaned): [yellow]{total_stats['deleted']}[/yellow]")
    if total_stats["pruned"] > 0:
        console.print(f"  Pruned hash keys: [dim]{total_stats['pruned']}[/dim]")
    if total_stats["gone"] > 0:
        console.print(f"  Gone (404/410): [yellow]{total_stats['gone']}[/yellow]")
    if total_stats["failed"] > 0:
        console.print(f"  Failed: [red]{total_stats['failed']}[/red]")
    for line in run.summary_lines(cleanup):
        console.print(f"  {line}", markup=False)

    # Print next step guidance
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
        description="Scrape MLX and coremltools documentation"
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
