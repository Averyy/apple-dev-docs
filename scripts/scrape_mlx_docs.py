#!/usr/bin/env python3
"""
MLX and Apple ML Documentation Scraper

Fetches documentation from Apple's ML open source projects:

Sphinx HTML Sites:
- MLX (ml-explore/mlx) - Array framework for Apple silicon
- MLX-Data (ml-explore/mlx-data) - Data loading utilities
- coremltools (apple/coremltools) - Core ML model conversion tools

GitHub Markdown:
- mlx-lm - LLM inference and fine-tuning
- mlx-examples - Example implementations
- mlx-c - C API bindings
- mlx-onnx - ONNX support
- ml-stable-diffusion - Stable Diffusion on Core ML

Usage:
    python scripts/scrape_mlx_docs.py
    python scripts/scrape_mlx_docs.py --dry-run
    python scripts/scrape_mlx_docs.py --force  # Re-download all files
"""

import argparse
import asyncio
import hashlib
import json
import logging
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set
from urllib.parse import urljoin, urlparse

import aiohttp
from bs4 import BeautifulSoup
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
OUTPUT_BASE = Path(__file__).parent.parent / "documentation"

# Hash file for incremental updates
HASH_FILE = Path(__file__).parent.parent / ".hashes" / "mlx_docs_hashes.json"

# Rate limiting
REQUEST_DELAY = 0.15  # seconds between requests
MAX_CONCURRENT = 10  # max concurrent requests


@dataclass
class SphinxDocSource:
    """Represents a Sphinx documentation site to scrape."""
    name: str  # e.g., "MLX"
    base_url: str  # e.g., "https://ml-explore.github.io/mlx/build/html/"
    output_dir: str  # e.g., "MLX"
    framework: str = ""  # Framework name for indexing (defaults to name)
    # CSS selectors for content extraction
    content_selector: str = "main, article, .body, [role='main']"
    # Paths to skip (relative to base_url)
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
]

# GitHub markdown sources
GITHUB_SOURCES: List[GitHubDocSource] = [
    GitHubDocSource(
        name="mlx-lm",
        repo="ml-explore/mlx-lm",
        branch="main",
        output_dir="MLX/mlx-lm",
        framework="MLX",
        files=["README.md", "mlx_lm/LORA.md"],
    ),
    GitHubDocSource(
        name="mlx-examples",
        repo="ml-explore/mlx-examples",
        branch="main",
        output_dir="MLX/mlx-examples",
        framework="MLX",
        files=["README.md"],
        directories=["llms", "stable_diffusion", "whisper", "lora"],
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
        files=["README.md"],
        directories=["Source/MLX/Documentation.docc"],  # Full DocC documentation
    ),
    GitHubDocSource(
        name="mlx-swift-lm",
        repo="ml-explore/mlx-swift-lm",
        branch="main",
        output_dir="MLX-Swift/mlx-swift-lm",
        framework="MLX-Swift",
        files=["README.md"],
        directories=["Libraries/MLXLMCommon/Documentation.docc"],  # Full DocC documentation
    ),
    GitHubDocSource(
        name="mlx-swift-examples",
        repo="ml-explore/mlx-swift-examples",
        branch="main",
        output_dir="MLX-Swift/mlx-swift-examples",
        framework="MLX-Swift",
        files=["README.md"],
        directories=["Applications"],
    ),
    GitHubDocSource(
        name="ml-stable-diffusion",
        repo="apple/ml-stable-diffusion",
        branch="main",
        output_dir="ml-stable-diffusion",
        framework="ml-stable-diffusion",
        files=["README.md"],
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
                if "hashes" in data:
                    return data["hashes"]
                return data
        except Exception as e:
            logger.warning(f"Could not load hash file: {e}")
    return {}


def save_hashes(hashes: Dict[str, str]):
    """Save file hashes with metadata for next run."""
    HASH_FILE.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "metadata": {
            "last_updated": datetime.now().isoformat(),
            "total_files": len(hashes),
            "source": "scrape_mlx_docs.py"
        },
        "hashes": hashes
    }

    with open(HASH_FILE, 'w') as f:
        json.dump(data, f, indent=2)


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


def url_to_filepath(url: str, base_url: str, output_dir: Path) -> Path:
    """Convert a URL to a local file path."""
    # Get path relative to base
    base_parsed = urlparse(base_url)
    url_parsed = urlparse(url)

    # Remove base path prefix
    rel_path = url_parsed.path
    if base_parsed.path and rel_path.startswith(base_parsed.path):
        rel_path = rel_path[len(base_parsed.path):]

    # Clean up path
    rel_path = rel_path.lstrip('/')

    # Change .html to .md
    if rel_path.endswith('.html'):
        rel_path = rel_path[:-5] + '.md'
    elif not rel_path or rel_path.endswith('/'):
        rel_path = rel_path.rstrip('/') + '/index.md' if rel_path else 'index.md'

    return output_dir / rel_path


def html_to_markdown(html: str, source: SphinxDocSource, url: str) -> str:
    """Convert Sphinx HTML to clean markdown."""
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
    for selector in ['nav', '.sidebar', '.sphinxsidebar', '.related',
                     '.footer', 'footer', '.headerlink', '.toctree-wrapper',
                     'script', 'style', '.skip-link', '#searchbox']:
        for elem in content.select(selector):
            elem.decompose()

    # Convert to markdown
    md_lines = []

    # Extract title
    title = soup.find('h1')
    if title:
        title_text = title.get_text(strip=True)
        # Remove pilcrow/link symbols
        title_text = re.sub(r'[¶#]$', '', title_text).strip()
        md_lines.append(f"# {title_text}\n")

    # Process content
    md_content = convert_element_to_markdown(content)
    md_lines.append(md_content)

    # Add source header
    result = f"""---
source: {source.name}
url: {url}
---

{"".join(md_lines)}"""

    # Clean up excessive whitespace
    result = re.sub(r'\n{3,}', '\n\n', result)

    return result.strip() + '\n'


def convert_element_to_markdown(element) -> str:
    """Recursively convert HTML element to markdown."""
    if element.name is None:  # Text node
        text = str(element)
        # Normalize whitespace but preserve some structure
        return text

    result = []

    # Handle specific tags
    tag = element.name.lower()

    if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(tag[1])
        text = element.get_text(strip=True)
        text = re.sub(r'[¶#]$', '', text).strip()  # Remove anchor symbols
        if text:
            result.append(f"\n{'#' * level} {text}\n")

    elif tag == 'p':
        text = process_inline_elements(element)
        if text.strip():
            result.append(f"\n{text}\n")

    elif tag in ['pre', 'code']:
        if tag == 'pre' or element.find('code'):
            code_elem = element.find('code') or element
            # Try to detect language from class
            lang = ''
            classes = code_elem.get('class', [])
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
            result.append(f"\n```{lang}\n{code_text}\n```\n")
        else:
            result.append(f"`{element.get_text()}`")

    elif tag == 'a':
        href = element.get('href', '')
        text = element.get_text(strip=True)
        if href and text:
            # Clean up internal links
            if href.startswith('#'):
                result.append(f"[{text}]({href})")
            elif not href.startswith(('http://', 'https://', 'mailto:')):
                # Convert .html to .md for internal links
                if href.endswith('.html'):
                    href = href[:-5] + '.md'
                result.append(f"[{text}]({href})")
            else:
                result.append(f"[{text}]({href})")
        elif text:
            result.append(text)

    elif tag in ['ul', 'ol']:
        for i, li in enumerate(element.find_all('li', recursive=False)):
            prefix = '- ' if tag == 'ul' else f"{i+1}. "
            li_text = process_inline_elements(li)
            if li_text.strip():
                result.append(f"{prefix}{li_text.strip()}\n")
        result.append('\n')

    elif tag == 'dl':
        for dt in element.find_all('dt', recursive=False):
            term = process_inline_elements(dt)
            result.append(f"\n**{term.strip()}**\n")
            dd = dt.find_next_sibling('dd')
            if dd:
                desc = process_inline_elements(dd)
                result.append(f": {desc.strip()}\n")

    elif tag == 'blockquote':
        text = process_inline_elements(element)
        lines = text.strip().split('\n')
        quoted = '\n'.join(f"> {line}" for line in lines)
        result.append(f"\n{quoted}\n")

    elif tag == 'table':
        result.append(convert_table_to_markdown(element))

    elif tag in ['strong', 'b']:
        text = element.get_text()
        result.append(f"**{text}**")

    elif tag in ['em', 'i']:
        text = element.get_text()
        result.append(f"*{text}*")

    elif tag == 'br':
        result.append('\n')

    elif tag in ['div', 'section', 'article', 'main', 'span']:
        # Container elements - process children
        for child in element.children:
            result.append(convert_element_to_markdown(child))

    elif tag == 'img':
        alt = element.get('alt', '')
        src = element.get('src', '')
        if src:
            result.append(f"![{alt}]({src})")

    else:
        # Default: process children
        for child in element.children:
            result.append(convert_element_to_markdown(child))

    return ''.join(result)


def process_inline_elements(element) -> str:
    """Process inline elements within a block."""
    result = []
    for child in element.children:
        if child.name is None:  # Text node
            result.append(str(child))
        elif child.name in ['code']:
            result.append(f"`{child.get_text()}`")
        elif child.name in ['strong', 'b']:
            result.append(f"**{child.get_text()}**")
        elif child.name in ['em', 'i']:
            result.append(f"*{child.get_text()}*")
        elif child.name == 'a':
            href = child.get('href', '')
            text = child.get_text(strip=True)
            if href.endswith('.html'):
                href = href[:-5] + '.md'
            result.append(f"[{text}]({href})" if href else text)
        elif child.name == 'br':
            result.append('\n')
        else:
            result.append(process_inline_elements(child))
    return ''.join(result)


def convert_table_to_markdown(table) -> str:
    """Convert HTML table to markdown table."""
    rows = []

    # Process header
    thead = table.find('thead')
    if thead:
        header_cells = [th.get_text(strip=True) for th in thead.find_all(['th', 'td'])]
        if header_cells:
            rows.append('| ' + ' | '.join(header_cells) + ' |')
            rows.append('| ' + ' | '.join(['---'] * len(header_cells)) + ' |')

    # Process body
    tbody = table.find('tbody') or table
    for tr in tbody.find_all('tr'):
        cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
        if cells:
            # Add header separator if first row and no thead
            if not thead and len(rows) == 0:
                rows.append('| ' + ' | '.join(cells) + ' |')
                rows.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')
            else:
                rows.append('| ' + ' | '.join(cells) + ' |')

    return '\n' + '\n'.join(rows) + '\n' if rows else ''


# =============================================================================
# GITHUB MARKDOWN SCRAPING
# =============================================================================

GITHUB_RAW = "https://raw.githubusercontent.com"


async def fetch_github_file(
    session: aiohttp.ClientSession,
    repo: str,
    branch: str,
    path: str
) -> Optional[str]:
    """Fetch raw file content from GitHub."""
    url = f"{GITHUB_RAW}/{repo}/{branch}/{path}"
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
            if response.status == 200:
                return await response.text()
            elif response.status == 404:
                logger.debug(f"File not found: {path}")
                return None
            else:
                logger.warning(f"HTTP {response.status} for {url}")
                return None
    except Exception as e:
        logger.warning(f"Error fetching {url}: {e}")
        return None


async def fetch_github_directory(
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

    try:
        async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=30)) as response:
            if response.status == 200:
                return await response.json()
            elif response.status == 404:
                return []
            else:
                logger.warning(f"GitHub API {response.status} for {path}")
                return []
    except Exception as e:
        logger.warning(f"Error fetching directory {path}: {e}")
        return []


async def discover_markdown_files(
    session: aiohttp.ClientSession,
    repo: str,
    branch: str,
    directory: str,
    recursive: bool = True
) -> List[str]:
    """Discover all markdown files in a GitHub directory."""
    files = []

    contents = await fetch_github_directory(session, repo, branch, directory)

    for item in contents:
        if item.get("type") == "file" and item.get("name", "").endswith(".md"):
            files.append(item["path"])
        elif item.get("type") == "dir" and recursive:
            sub_files = await discover_markdown_files(
                session, repo, branch, item["path"], recursive=True
            )
            files.extend(sub_files)

    await asyncio.sleep(REQUEST_DELAY)
    return files


def add_github_source_header(content: str, source: GitHubDocSource, file_path: str) -> str:
    """Add source attribution header to GitHub markdown content."""
    source_url = f"https://github.com/{source.repo}/blob/{source.branch}/{file_path}"

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


async def scrape_github_source(
    session: aiohttp.ClientSession,
    source: GitHubDocSource,
    hashes: Dict[str, str],
    dry_run: bool = False,
    force: bool = False
) -> Dict[str, any]:
    """Scrape a GitHub markdown documentation source."""
    stats = {"downloaded": 0, "skipped": 0, "errors": 0, "expected_files": []}

    output_dir = OUTPUT_BASE / source.output_dir

    # Collect all files to fetch
    files_to_fetch: List[str] = list(source.files)

    # Discover files in directories
    for directory in source.directories:
        discovered = await discover_markdown_files(
            session, source.repo, source.branch, directory
        )
        files_to_fetch.extend(discovered)

    console.print(f"  Found {len(files_to_fetch)} markdown files")

    for file_path in files_to_fetch:
        # Determine output path
        # Convert path like "mlx_lm/LORA.md" to "LORA.md" (flatten structure a bit)
        filename = Path(file_path).name
        if "/" in file_path:
            # Keep subdirectory structure for discovered files
            rel_path = file_path
        else:
            rel_path = filename

        output_path = output_dir / rel_path
        hash_key = f"github:{source.repo}:{file_path}"

        stats["expected_files"].append(str(output_path))

        # Fetch content
        content = await fetch_github_file(
            session, source.repo, source.branch, file_path
        )

        if content is None:
            stats["errors"] += 1
            continue

        await asyncio.sleep(REQUEST_DELAY)

        # Check if content changed
        content_hash = compute_hash(content)
        if not force and hash_key in hashes and hashes[hash_key] == content_hash:
            stats["skipped"] += 1
            continue

        # Add source header
        content = add_github_source_header(content, source, file_path)

        if dry_run:
            console.print(f"  [dim]Would write:[/dim] {output_path}")
        else:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            hashes[hash_key] = content_hash

        stats["downloaded"] += 1

    return stats


# =============================================================================
# SPHINX HTML CRAWLING
# =============================================================================

async def fetch_page(session: aiohttp.ClientSession, url: str) -> Optional[str]:
    """Fetch a single page."""
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
            if response.status == 200:
                return await response.text()
            elif response.status == 404:
                return None
            else:
                logger.warning(f"HTTP {response.status} for {url}")
                return None
    except Exception as e:
        logger.warning(f"Error fetching {url}: {e}")
        return None


async def discover_pages(
    session: aiohttp.ClientSession,
    source: SphinxDocSource,
    start_url: str,
    visited: Set[str],
    semaphore: asyncio.Semaphore
) -> Set[str]:
    """Discover all pages by crawling from start URL."""
    to_visit = {start_url}
    discovered = set()

    while to_visit:
        # Get next batch
        batch = set()
        while to_visit and len(batch) < MAX_CONCURRENT:
            batch.add(to_visit.pop())

        # Fetch batch concurrently
        tasks = []
        for url in batch:
            if url in visited:
                continue
            visited.add(url)
            tasks.append(fetch_and_extract_links(session, url, source, semaphore))

        results = await asyncio.gather(*tasks)

        for url, links in zip(batch, results):
            if links is not None:
                discovered.add(url)
                for link in links:
                    if link not in visited:
                        to_visit.add(link)

        await asyncio.sleep(REQUEST_DELAY)

    return discovered


async def fetch_and_extract_links(
    session: aiohttp.ClientSession,
    url: str,
    source: SphinxDocSource,
    semaphore: asyncio.Semaphore
) -> Optional[List[str]]:
    """Fetch page and extract internal links."""
    async with semaphore:
        html = await fetch_page(session, url)
        if html is None:
            return None

        soup = BeautifulSoup(html, 'html.parser')
        links = []

        for a in soup.find_all('a', href=True):
            href = a['href']
            normalized = normalize_url(url, href)

            if normalized is None:
                continue

            # Check if within base URL
            if not normalized.startswith(source.base_url):
                continue

            # Check skip paths
            rel_path = normalized[len(source.base_url):]
            if any(skip in rel_path for skip in source.skip_paths):
                continue

            # Only include .html files
            if not normalized.endswith('.html') and '.' in rel_path.split('/')[-1]:
                continue

            links.append(normalized)

        return links


async def scrape_source(
    session: aiohttp.ClientSession,
    source: SphinxDocSource,
    hashes: Dict[str, str],
    dry_run: bool = False,
    force: bool = False
) -> Dict[str, any]:
    """Scrape a single documentation source."""
    stats = {"downloaded": 0, "skipped": 0, "errors": 0, "expected_files": []}

    output_dir = OUTPUT_BASE / source.output_dir
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    console.print(f"\n[cyan]Discovering pages for {source.name}...[/cyan]")

    # Discover all pages
    visited: Set[str] = set()
    pages = await discover_pages(session, source, source.base_url, visited, semaphore)

    # Also try index.html explicitly
    index_url = urljoin(source.base_url, "index.html")
    if index_url not in pages:
        pages.add(index_url)

    console.print(f"  Found {len(pages)} pages")

    # Process each page
    for url in sorted(pages):
        filepath = url_to_filepath(url, source.base_url, output_dir)
        hash_key = f"{source.name}:{url}"

        stats["expected_files"].append(str(filepath))

        async with semaphore:
            html = await fetch_page(session, url)

        if html is None:
            stats["errors"] += 1
            continue

        # Check if content changed (hash the HTML)
        content_hash = compute_hash(html)
        if not force and hash_key in hashes and hashes[hash_key] == content_hash:
            stats["skipped"] += 1
            continue

        # Convert to markdown
        try:
            markdown = html_to_markdown(html, source, url)
        except Exception as e:
            logger.warning(f"Error converting {url}: {e}")
            stats["errors"] += 1
            continue

        if dry_run:
            console.print(f"  [dim]Would write:[/dim] {filepath}")
        else:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown)
            hashes[hash_key] = content_hash

        stats["downloaded"] += 1
        await asyncio.sleep(REQUEST_DELAY)

    return stats


async def scrape_all(dry_run: bool = False, force: bool = False):
    """Scrape all configured documentation sources."""
    console.print("\n[bold blue]MLX / coremltools Documentation Scraper[/bold blue]\n")

    # Load existing hashes
    hashes = {} if force else load_hashes()

    total_stats = {"downloaded": 0, "skipped": 0, "errors": 0}
    all_expected_files: Set[str] = set()

    connector = aiohttp.TCPConnector(limit=MAX_CONCURRENT)
    async with aiohttp.ClientSession(connector=connector) as session:
        # Scrape Sphinx HTML documentation sites
        console.print("[bold cyan]═══ Sphinx HTML Documentation ═══[/bold cyan]")
        for source in SPHINX_SOURCES:
            console.print(f"\n[bold]{source.name}[/bold] ({source.base_url})")

            stats = await scrape_source(
                session, source, hashes, dry_run=dry_run, force=force
            )

            total_stats["downloaded"] += stats["downloaded"]
            total_stats["skipped"] += stats["skipped"]
            total_stats["errors"] += stats["errors"]
            all_expected_files.update(stats["expected_files"])

            console.print(f"  [green]Downloaded:[/green] {stats['downloaded']}")
            console.print(f"  [dim]Skipped:[/dim] {stats['skipped']}")
            if stats["errors"] > 0:
                console.print(f"  [red]Errors:[/red] {stats['errors']}")

        # Scrape GitHub markdown documentation
        console.print("\n[bold cyan]═══ GitHub Markdown Documentation ═══[/bold cyan]")
        for source in GITHUB_SOURCES:
            console.print(f"\n[bold]{source.name}[/bold] (github.com/{source.repo})")

            stats = await scrape_github_source(
                session, source, hashes, dry_run=dry_run, force=force
            )

            total_stats["downloaded"] += stats["downloaded"]
            total_stats["skipped"] += stats["skipped"]
            total_stats["errors"] += stats["errors"]
            all_expected_files.update(stats["expected_files"])

            console.print(f"  [green]Downloaded:[/green] {stats['downloaded']}")
            console.print(f"  [dim]Skipped:[/dim] {stats['skipped']}")
            if stats["errors"] > 0:
                console.print(f"  [red]Errors:[/red] {stats['errors']}")

    # Clean up orphaned files
    if not dry_run:
        # Collect all output directories from both source types
        all_sources = [(s.name, s.output_dir) for s in SPHINX_SOURCES] + \
                      [(s.name, s.output_dir) for s in GITHUB_SOURCES]

        for name, output_subdir in all_sources:
            output_dir = OUTPUT_BASE / output_subdir
            if output_dir.exists():
                existing = set(str(f) for f in output_dir.rglob("*.md"))
                orphaned = existing - all_expected_files

                if orphaned:
                    console.print(f"\n[yellow]Cleaning up {len(orphaned)} orphaned files in {name}...[/yellow]")
                    for orphan_path in orphaned:
                        try:
                            Path(orphan_path).unlink()
                        except Exception as e:
                            logger.warning(f"Could not delete {orphan_path}: {e}")

    # Save hashes
    if not dry_run and total_stats["downloaded"] > 0:
        save_hashes(hashes)

    # Print summary
    console.print("\n[bold]Summary:[/bold]")
    console.print(f"  Downloaded: [green]{total_stats['downloaded']}[/green]")
    console.print(f"  Skipped (unchanged): [dim]{total_stats['skipped']}[/dim]")
    if total_stats["errors"] > 0:
        console.print(f"  Errors: [red]{total_stats['errors']}[/red]")

    return total_stats


# =============================================================================
# CLI ENTRY POINT
# =============================================================================

def main():
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
