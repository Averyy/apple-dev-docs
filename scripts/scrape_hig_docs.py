#!/usr/bin/env python3
"""
Apple Human Interface Guidelines (HIG) Scraper

Fetches design documentation from Apple's Human Interface Guidelines using
the same JSON API pattern as the main documentation scraper.

URL structure:
- JSON API: https://developer.apple.com/tutorials/data/design/human-interface-guidelines.json
- Web URL: https://developer.apple.com/design/human-interface-guidelines

Usage:
    python scripts/scrape_hig_docs.py
    python scripts/scrape_hig_docs.py --dry-run
    python scripts/scrape_hig_docs.py --force  # Re-download all files

Failures follow the policy shared with the MLX and Swift scrapers
(utilities/source_policy.py): requests are retried; a page Apple no longer
links, or that returns 404/410, is removed at once; other failures and
convert/save errors keep the page's file and block the orphan cleanup for up
to 3 runs; the root page follows the configured-root rules (404/410 keeps
every file for that run and removes them on the 2nd consecutive run; any
other failure keeps them until it recovers). The orphan cleanup uses
confirm-then-delete for mass removals (pending_orphans in the hash file's
metadata).

Exit codes: 0 clean (removals and valve holds included); 1 an error of ours
(a blocked cleanup, a failed root, a persistent failure, a failed save, an
unexpected exception); 130 interrupted.
"""

import argparse
import asyncio
import json
import logging
import posixpath
import re
import sys
import time
from collections import Counter, deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union

import httpx
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

# The repo root, for the asset URL helper shared with the Apple scraper
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scraper.utils.assets import hosting_root, variant_url
from scraper.utils.links import doc_link
from scraper.utils.markdown_converter import join_blocks, labeled, quote_blocks
from scraper.utils.naming import dirmap
from utilities.docc import emphasis
from utilities.hash_utils import HashFileError, compute_hash, read_hash_file, save_hashes, write_text_atomic
from utilities.source_policy import (
    FAILURE_COUNTS_KEY,
    PENDING_ORPHANS_KEY,
    RENDER_KEY,
    CleanupResult,
    FetchFailed,
    KeptLocation,
    ScrapeRun,
    fetch_with_retry,
    has_file_named,
    policy_metadata,
)

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
console = Console()

# =============================================================================
# CONFIGURATION
# =============================================================================

# Output directory (use short name - "HIG" is widely recognized)
OUTPUT_DIR = Path(__file__).parent.parent / "documentation" / "HIG"

# Hash file for incremental updates
HASH_FILE = Path(__file__).parent.parent / ".hashes" / "hig_docs_hashes.json"

# API URLs
JSON_BASE_URL = "https://developer.apple.com/tutorials/data/design"
WEB_BASE_URL = "https://developer.apple.com/design"
# A reference's root-relative URL ("/documentation/…") is under it
APPLE_HOST = "https://developer.apple.com"
# Root-relative image and video URLs ("/images/…") are served under it
ASSET_ROOT = hosting_root(JSON_BASE_URL)
HIG_ROOT = "human-interface-guidelines"

# Rate limiting
REQUEST_DELAY = 0.1  # seconds between requests
MAX_CONCURRENT = 10
REQUEST_TIMEOUT = 30.0

# Framework identifier for filtering
FRAMEWORK_ID = "HumanInterfaceGuidelines"
FRAMEWORK_NAME = "Human Interface Guidelines"

# Identifier patterns to match HIG content
HIG_IDENTIFIER_PATTERNS = [
    "com.apple.hig",
    "com.apple.HIG",
    "/design/human-interface-guidelines",
    "/design/Human-Interface-Guidelines",
]

# Hash-file metadata the failure policy keeps (saved whenever it changes),
# and the render version
POLICY_KEYS = (FAILURE_COUNTS_KEY, PENDING_ORPHANS_KEY, RENDER_KEY)

# The converter's output version (links included): bump it when a change to
# the conversion changes the files of pages whose JSON didn't change, so the
# next clean run renders every page again (source_policy's metadata.render)
RENDER_VERSION = 1

# The block and inline types the converter renders (_convert_content_to_markdown,
# _extract_text_from_inline_content). Any other, like a section kind the page
# conversion doesn't read, is rendered as its text (_fallback_parts) and
# counted: one WARN per type at the end of the run (unknown_content). In such
# an unknown item, these tell a list of blocks from one of inline content
# ("image" is both: there, inline content)
KNOWN_BLOCK_TYPES = frozenset({
    'paragraph', 'small', 'heading', 'codeListing', 'unorderedList', 'orderedList', 'aside',
    'row', 'tabNavigator', 'links', 'table', 'image', 'imageBlock', 'video', 'card', 'icon',
    'topic', 'termList', 'thematicBreak',
})
KNOWN_INLINE_TYPES = frozenset({
    'text', 'codeVoice', 'emphasis', 'strong', 'strikethrough', 'reference', 'link', 'image',
    'inlineHead', 'newTerm', 'superscript', 'subscript',
})


def one_line(text: str) -> str:
    """Text on one line (a list item's or table cell's): each line break, with
    the whitespace around it, as one space."""
    return re.sub(r'\s*\n\s*', ' ', text.strip())


def join_parts(parts: List[str]) -> str:
    """Rendered parts as one text, with at most one blank line where two meet:
    the newlines ending one part and starting the next (a paragraph's or
    list's blank line, a heading's or code listing's leading newline) are cut
    to two, so that no 3+ newlines run between blocks. A part's own text (a
    code listing's blank lines) is kept as it is."""
    text = ''
    for part in parts:
        trailing = len(text) - len(text.rstrip('\n'))
        leading = len(part) - len(part.lstrip('\n'))
        text += part[min(leading, max(0, trailing + leading - 2)):]
    return text


class HIGDocsScraper:
    """Scraper for Apple Human Interface Guidelines using JSON API."""

    def __init__(self, force: bool = False, dry_run: bool = False):
        self.force = force
        self.dry_run = dry_run
        self.session: Optional[httpx.AsyncClient] = None

        # URL tracking
        self.processed_urls: Set[str] = set()
        self.discovered_urls: Set[str] = set()

        # Hash management for incremental updates
        self.hashes: Dict[str, Dict] = {}
        self.hashes_modified = False
        self.stored_metadata: Dict[str, Any] = {}
        self.load_error: Optional[str] = None
        # The file is still in the old flat format (no metadata): the next save converts it
        self.flat_hash_file = False

        # The run's failures and cleanup (utilities/source_policy.py), and its
        # policy metadata once the scrape completed (else the stored one is kept)
        self.run: Optional[ScrapeRun] = None
        self.final_metadata: Optional[Dict[str, Any]] = None
        self.exit_code = 1

        # Statistics
        self.stats: Dict[str, Any] = {
            "pages_scraped": 0,
            "pages_skipped": 0,
            "pages_gone": 0,
            "pages_failed": 0,
            "start_time": None,
            "end_time": None
        }

        # Topic hierarchy for organized file structure
        self.topic_hierarchy: Dict[str, Dict] = {}

        # JSON the converter doesn't know, (what, name) -> count, logged at the
        # end of the run, with the page it was first seen on
        self.unknown_content: Counter[Tuple[str, str]] = Counter()
        self.unknown_examples: Dict[Tuple[str, str], str] = {}
        self.current_url = ''

        # The Apple framework docs dirs whose pages are linked locally,
        # {name.lower(): name}: naming.dirmap over the hash files, read on
        # the first link (_link_dirs)
        self.doc_dirs: Optional[Dict[str, str]] = None

    async def __aenter__(self) -> "HIGDocsScraper":
        """Async context manager entry."""
        self.session = httpx.AsyncClient(
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "AppleDocsBot/1.0"},
            follow_redirects=True
        )
        self._load_hashes()
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Async context manager exit: save the page hashes of an interrupted
        run (a completed run saved already); its counters stay as stored."""
        if self.session:
            await self.session.aclose()
        if self.final_metadata is None:
            self._save_hashes()

    def _load_hashes(self) -> None:
        """Load stored hashes (and metadata) for incremental updates.

        Reads both the shared {"metadata", "hashes"} format and the old flat
        dict. A file that can't be read loads as empty, with the error: the
        run then blocks its cleanup and its save replaces the file.
        """
        try:
            self.hashes, self.stored_metadata = read_hash_file(HASH_FILE)
        except HashFileError as e:
            logger.warning(f"Could not load hash file: {e}")
            self.hashes, self.stored_metadata, self.load_error = {}, {}, str(e)
            return
        self.flat_hash_file = HASH_FILE.exists() and not self.stored_metadata
        if HASH_FILE.exists():
            logger.info(f"Loaded {len(self.hashes)} existing hashes")

    def _save_hashes(self) -> bool:
        """Save hashes for next run, in the shared format with this run's
        policy metadata, whenever either changed.

        Returns:
            False if the save failed
        """
        if self.dry_run:
            return True
        metadata = (self.final_metadata if self.final_metadata is not None
                    else policy_metadata(self.stored_metadata, POLICY_KEYS))
        if not (self.hashes_modified or self.flat_hash_file or self.load_error is not None
                or metadata != policy_metadata(self.stored_metadata, POLICY_KEYS)):
            return True
        if not save_hashes(HASH_FILE, self.hashes, source="scrape_hig_docs.py", metadata=metadata):
            return False
        logger.info(f"Saved {len(self.hashes)} hashes")
        return True

    def _compute_hash(self, content: str) -> str:
        """Compute SHA-256 hash of content."""
        return compute_hash(content)

    def _has_changed(self, url: str, content: str, file_path: Path) -> bool:
        """Check if content has changed since last scrape (or its file is missing)."""
        if self.force or not file_path.exists():
            return True

        new_hash = self._compute_hash(content)
        old_data = self.hashes.get(url, {})
        old_hash = old_data.get('hash', '')

        return bool(new_hash != old_hash)

    def _previously_good(self, url: str, file_path: Path) -> bool:
        """We have this page: a hash entry with its content hash and file, or
        its file on disk under exactly its name (a hash file that was lost or
        couldn't be read loses entries, not files)."""
        entry = self.hashes.get(url)
        if isinstance(entry, dict) and bool(entry.get('hash')) and bool(entry.get('file_path')):
            return True
        return has_file_named(file_path)

    def _update_hash(self, url: str, content: str, file_path: Path) -> None:
        """Update hash for a URL."""
        self.hashes[url] = {
            'hash': self._compute_hash(content),
            'file_path': str(file_path),
            # Naive UTC, as utcnow() wrote it (deprecated on the scrape workflow's Python 3.12)
            'last_updated': datetime.now(timezone.utc).replace(tzinfo=None).isoformat()
        }
        self.hashes_modified = True

    async def fetch_json(self, url: str) -> Union[Dict[str, Any], FetchFailed]:
        """Fetch and parse JSON from URL, retrying transient failures.

        Returns:
            The JSON object, or FetchFailed with the status: 404/410 is a
            removal; a body that isn't a JSON object is a transient failure
        """
        session = self.session
        if not session:
            raise RuntimeError("Scraper must be used as async context manager")

        await asyncio.sleep(REQUEST_DELAY)

        async def attempt() -> Tuple[int, Optional[str], str]:
            response = await session.get(url)
            return response.status_code, response.headers.get("Retry-After"), response.text

        # RequestError: timeouts, network and protocol errors, redirect loops, undecodable bodies
        body = await fetch_with_retry(attempt, url, (httpx.RequestError,))
        if isinstance(body, FetchFailed):
            if body.gone:
                logger.debug(f"Not found: {url}")
            else:
                logger.warning(f"Error fetching {url}: {body.error}")
            return body
        try:
            data = json.loads(body)
        except ValueError:
            data = None
        if not isinstance(data, dict):
            logger.warning(f"Invalid JSON from {url}")
            return FetchFailed(status=200, error="invalid json", transient=True)
        return data

    def _convert_url_to_local_path(self, url: str) -> str:
        """Convert a URL to a local markdown path.

        HIG internal links: /design/human-interface-guidelines/X -> X.md
        HIG anchors: /design/human-interface-guidelines/X#anchor -> X.md#anchor
        Apple docs: /documentation/Framework/Symbol -> the page's file
            relative to this page's (links.doc_link: the Apple scraper's own
            path rule, e.g. ../SwiftUI/button.md), when its framework is a
            docs dir we have (_link_dirs); else its Apple URL
        External links: keep as-is
        """
        if not url:
            return url

        # Handle HIG internal links
        hig_pattern = r'^/design/human-interface-guidelines/([^#]+)(#.*)?$'
        match = re.match(hig_pattern, url, re.IGNORECASE)
        if match:
            page_name = match.group(1).lower()
            anchor = match.group(2) or ''
            return f"{page_name}.md{anchor}"

        # Handle links to /design/human-interface-guidelines (root)
        if url.lower() in ['/design/human-interface-guidelines', '/design/human-interface-guidelines/']:
            return "index.md"

        # Apple documentation links: relative to this page's folder under
        # the docs root (HIG/, the folder of _get_file_path's file)
        if url.startswith('/documentation/'):
            page_file = self._get_file_path(self.current_url, {}).relative_to(OUTPUT_DIR.parent)
            return doc_link(f"{APPLE_HOST}{url}", posixpath.dirname(page_file.as_posix()), self._link_dirs())

        # Keep external URLs as-is
        return url

    def _link_dirs(self) -> Dict[str, str]:
        """The docs dirs linked locally (doc_dirs), from the hash files next to ours on first use.

        The HIG scrape runs after the Apple one, so a framework that run
        scraped for the first time has its hash file by then.
        """
        if self.doc_dirs is None:
            self.doc_dirs = dirmap(HASH_FILE.parent)
        return self.doc_dirs

    def _convert_identifier_to_json_url(self, identifier: str) -> Optional[str]:
        """Convert a doc:// identifier to a JSON URL.

        HIG identifiers look like:
        - doc://com.apple.HIG/design/Human-Interface-Guidelines/foundations
        - doc://com.apple.HIG/design/Human-Interface-Guidelines/color
        """
        if not identifier.startswith('doc://'):
            return None

        # Check if this is an HIG identifier
        is_hig = any(pattern in identifier for pattern in HIG_IDENTIFIER_PATTERNS)
        if not is_hig:
            return None

        try:
            # Extract path after /design/
            if '/design/' in identifier:
                path = identifier.split('/design/', 1)[1]
                # Normalize: Human-Interface-Guidelines -> human-interface-guidelines
                path_lower = path.lower()
                return f"{JSON_BASE_URL}/{path_lower}.json"

            return None
        except Exception as e:
            logger.debug(f"Could not convert identifier {identifier}: {e}")
            return None

    def _convert_json_url_to_web_url(self, json_url: str) -> str:
        """Convert JSON URL to web URL."""
        # https://developer.apple.com/tutorials/data/design/human-interface-guidelines/color.json
        # -> https://developer.apple.com/design/human-interface-guidelines/color
        path = json_url.replace(JSON_BASE_URL + '/', '')
        # Remove .json suffix properly (not rstrip which removes chars)
        if path.endswith('.json'):
            path = path[:-5]
        return f"{WEB_BASE_URL}/{path}"

    def _slugify(self, text: str) -> str:
        """Convert text to URL-safe folder name."""
        slug = re.sub(r'[^\w\s-]', '', text.lower())
        slug = re.sub(r'[\s_-]+', '-', slug)
        return slug.strip('-')

    def _get_file_path(self, json_url: str, data: Dict) -> Path:
        """Get organized file path for a document."""
        # Extract path from JSON URL
        path = json_url.replace(JSON_BASE_URL + '/', '')
        # Remove .json suffix properly (not rstrip which removes chars)
        if path.endswith('.json'):
            path = path[:-5]

        # Remove the human-interface-guidelines prefix for cleaner structure
        path = path.replace('human-interface-guidelines/', '')
        path = path.replace('human-interface-guidelines', '')

        if not path:
            # Root HIG page
            return OUTPUT_DIR / "index.md"

        # Convert path to file path
        parts = path.strip('/').split('/')

        if len(parts) == 1:
            # Top-level section (foundations, patterns, etc.)
            return OUTPUT_DIR / f"{parts[0]}.md"
        else:
            # Nested page
            return OUTPUT_DIR / '/'.join(parts[:-1]) / f"{parts[-1]}.md"

    def _extract_urls_from_json(self, data: Dict) -> List[str]:
        """Extract child URLs from JSON data."""
        urls = []

        # Sections that contain child page identifiers
        sections_to_check = [
            'topicSections',
            'seeAlsoSections',
        ]

        for section_name in sections_to_check:
            sections = data.get(section_name, [])
            if isinstance(sections, list):
                for section in sections:
                    identifiers = section.get('identifiers', [])
                    for identifier in identifiers:
                        json_url = self._convert_identifier_to_json_url(identifier)
                        if json_url:
                            urls.append(json_url)

        # Also check primaryContentSections for links
        for section in data.get('primaryContentSections', []):
            content = section.get('content', [])
            self._extract_urls_from_content(content, urls)

        return urls

    def _extract_urls_from_content(self, content: List, urls: List[str]) -> None:
        """Recursively extract URLs from content blocks."""
        for item in content:
            if isinstance(item, dict):
                # Check for links items
                if item.get('type') == 'links':
                    for link_id in item.get('items', []):
                        json_url = self._convert_identifier_to_json_url(link_id)
                        if json_url:
                            urls.append(json_url)

                # Recurse into nested content (a tab navigator's tabs included)
                for key in ['content', 'items', 'columns', 'tabs']:
                    nested = item.get(key, [])
                    if isinstance(nested, list):
                        self._extract_urls_from_content(nested, urls)

    def _extract_text_from_inline_content(self, content: List, references: Dict) -> str:
        """Extract plain text from inline content."""
        parts = []
        for item in content:
            if isinstance(item, dict):
                item_type = item.get('type', '')
                if item_type == 'text':
                    parts.append(item.get('text', ''))
                elif item_type == 'codeVoice':
                    parts.append(f"`{item.get('code', '')}`")
                elif item_type == 'emphasis':
                    inner = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    parts.append(emphasis(inner, '*'))
                elif item_type == 'strong':
                    inner = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    parts.append(emphasis(inner, '**'))
                elif item_type == 'reference':
                    # Resolve reference: the prose's own wording (its overriding
                    # title) as the link text, else the target's title
                    ref_id = item.get('identifier', '')
                    ref = references.get(ref_id, {})
                    if item.get('overridingTitleInlineContent'):
                        title = self._extract_text_from_inline_content(item['overridingTitleInlineContent'], references)
                    elif item.get('overridingTitle'):
                        title = item['overridingTitle']
                    else:
                        title = ref.get('title', ref_id.split('/')[-1])
                    url = ref.get('url', '')
                    if url:
                        local_path = self._convert_url_to_local_path(url)
                        parts.append(f"[{title}]({local_path})")
                    else:
                        parts.append(title)
                elif item_type == 'link':
                    # External links (not doc:// references)
                    title = item.get('title', '')
                    url = item.get('url', item.get('identifier', ''))
                    # Try to get title from titleInlineContent if not set
                    if not title:
                        title_content = item.get('titleInlineContent', [])
                        title = self._extract_text_from_inline_content(title_content, references)
                    if url and title:
                        # External links stay as-is
                        parts.append(f"[{title}]({url})")
                    elif title:
                        parts.append(title)
                elif item_type == 'image':
                    # Resolve image from references to get URL: its 2x light
                    # variant, under the hosting root; its caption under it
                    img_md = self._resolve_image(item.get('identifier', ''), references)
                    figure = self._figure(img_md, item, references)
                    if figure:
                        parts.append(figure)
                elif item_type == 'inlineHead':
                    inner = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    parts.append(emphasis(inner, '**'))
                elif item_type == 'newTerm':
                    inner = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    parts.append(emphasis(inner, '*'))
                elif item_type == 'superscript':
                    inner = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    parts.append(f"<sup>{inner}</sup>")
                elif item_type == 'subscript':
                    inner = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    parts.append(f"<sub>{inner}</sub>")
                elif item_type == 'strikethrough':
                    inner = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    parts.append(f"~~{inner}~~")
                else:
                    # Not rendered above: its text, never silently dropped, and a
                    # WARN. On one line (each line break a space, its other spaces
                    # kept): a block under it (a code listing, a list) can't break
                    # the paragraph
                    self._note_unknown('inline type', item_type)
                    fallback = ' '.join(self._fallback_parts(item, references, inline=True))
                    parts.append(re.sub(r'\s*\n\s*', ' ', fallback))
        return ''.join(parts)

    def _note_unknown(self, what: str, name: Any) -> None:
        """Count JSON the converter doesn't know (a block or inline type, a
        section kind); logged at the end of the run (_log_unknown_content)."""
        key = (what, str(name))
        if key not in self.unknown_content:
            self.unknown_examples[key] = self.current_url
        self.unknown_content[key] += 1

    def _log_unknown_content(self) -> None:
        """One WARN per unknown block or inline type or section kind seen this run, with its count."""
        for (what, name), count in sorted(self.unknown_content.items()):
            logger.warning(f"unknown_content: {what} {name!r} x{count}, rendered as its text "
                           f"(e.g. {self.unknown_examples.get((what, name), '')})")

    def _fallback_parts(self, item: Dict[str, Any], references: Dict, inline: bool = False) -> List[str]:
        """The text of a block, inline item or section the converter doesn't
        render: every value under it but its type name, in order, recursively
        (_fallback_value). inline: the item is inline content (code lines
        stay inline code)."""
        return [part for key, value in item.items() if not (key == 'type' and isinstance(value, str))
                for part in self._fallback_value(key, value, references, inline)]

    def _fallback_value(self, key: str, value: Any, references: Dict, inline: bool) -> List[str]:
        """The text a value under key holds, recursively. A list holding known
        blocks (KNOWN_BLOCK_TYPES) is rendered as blocks, one holding known
        inline items (KNOWN_INLINE_TYPES) as one text, and a dict of a known
        type as such; a list of untyped text fragments (tokens) is one text; in
        any other dict or list, each value the same way. A "text" string is
        text and a "code" string inline code; a "code" list of lines is an
        untagged code listing (inline code when inline). Other strings
        (identifiers, anchors, styles, syntax names) aren't text."""
        blocks_only = KNOWN_BLOCK_TYPES - KNOWN_INLINE_TYPES
        if isinstance(value, dict):
            if str(value.get('type')) in blocks_only:
                return [self._convert_content_to_markdown([value], references)]
            if str(value.get('type')) in KNOWN_INLINE_TYPES:
                return [self._extract_text_from_inline_content([value], references)]
            return self._fallback_parts(value, references, inline)
        if isinstance(value, list):
            items = [v for v in value if isinstance(v, dict)]
            types = {v['type'] for v in items if isinstance(v.get('type'), str)}
            if types & blocks_only:
                return [self._convert_content_to_markdown(items, references)]
            if types & KNOWN_INLINE_TYPES:
                return [self._extract_text_from_inline_content(items, references)]
            if key == 'code' and value and all(isinstance(line, str) for line in value):
                return [f"`{' '.join(value)}`" if inline else '```\n' + '\n'.join(value) + '\n```']
            if items and len(items) == len(value) and not types and all(
                    isinstance(v.get('text'), str) for v in items):
                return [''.join(v['text'] for v in items)]
            return [part for v in value for part in self._fallback_value(key, v, references, inline)]
        if isinstance(value, str) and key == 'text':
            return [value]
        if isinstance(value, str) and key == 'code' and value:
            return [f"`{value}`"]
        return []

    def _fallback_markdown(self, item: Dict[str, Any], references: Dict) -> str:
        """The text of a block or section the converter doesn't render
        (_fallback_parts), as blocks with a blank line after each."""
        return ''.join(f"{part.strip()}\n\n" for part in self._fallback_parts(item, references) if part.strip())

    def _resolve_image(self, identifier: str, references: Dict) -> str:
        """Resolve an image identifier to markdown: its 2x light variant, under the hosting root."""
        ref = references.get(identifier, {})
        img_url = variant_url(ref, ASSET_ROOT)
        if img_url:
            alt = ref.get('alt') or ''
            return f"![{alt}]({img_url})"
        return ''

    def _resolve_video(self, identifier: str, references: Dict) -> str:
        """Resolve a video identifier to markdown link: its light variant, under the hosting root,
        named by its alt text (else its identifier), as the Apple converter does."""
        ref = references.get(identifier, {})
        video_url = variant_url(ref, ASSET_ROOT)
        if video_url:
            name = one_line(ref.get('alt') or '') or identifier
            return f"[Video: {name}]({video_url})"
        return ''

    def _figure(self, media_md: str, item: Dict[str, Any], references: Dict) -> str:
        """An image or video (its markdown) and, on the line under it, its
        caption: Apple's text under the figure (the item's metadata abstract),
        on one line. A table cell, one line, holds both."""
        metadata = item.get('metadata') or {}
        caption = one_line(self._extract_text_from_inline_content(metadata.get('abstract') or [], references))
        return '\n'.join(part for part in (media_md, caption) if part)

    def _convert_content_to_markdown(self, content: List, references: Dict, level: int = 2) -> str:
        """Convert content blocks to markdown."""
        parts = []

        for item in content:
            if isinstance(item, dict):
                item_type = item.get('type', '')

                if item_type in ('paragraph', 'small'):
                    # A paragraph, or small print (a footnote under a table)
                    text = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    if text:
                        # A blank line after it: the next paragraph would otherwise continue it
                        parts.append(text + '\n\n')

                elif item_type == 'heading':
                    text = item.get('text', '')
                    # Also try inlineContent for heading text
                    if not text:
                        text = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    # Fallback to anchor
                    if not text and item.get('anchor'):
                        text = item['anchor'].replace('-', ' ').title()
                    heading_level = item.get('level', level)
                    prefix = '#' * heading_level
                    if text:
                        parts.append(f"\n{prefix} {text}\n")

                elif item_type == 'codeListing':
                    code = '\n'.join(item.get('code', []))
                    lang = item.get('syntax', 'swift')
                    parts.append(f"\n```{lang}\n{code}\n```\n")

                elif item_type == 'unorderedList':
                    for list_item in item.get('items', []):
                        item_content = list_item.get('content', [])
                        # Process all content in list item, not just paragraphs
                        list_text = self._convert_content_to_markdown(item_content, references, level)
                        if list_text.strip():
                            # Format as list item: its blocks (a blank line between
                            # them) with every later line indented under the marker
                            parts.append(f"- {join_blocks([list_text.strip()], 2)}\n")
                    # A blank line after the list: the next paragraph would otherwise
                    # continue its last item
                    parts.append('\n')

                elif item_type == 'orderedList':
                    for i, list_item in enumerate(item.get('items', []), 1):
                        item_content = list_item.get('content', [])
                        list_text = self._convert_content_to_markdown(item_content, references, level)
                        if list_text.strip():
                            marker = f"{i}. "
                            parts.append(f"{marker}{join_blocks([list_text.strip()], len(marker))}\n")
                    parts.append('\n')

                elif item_type == 'aside':
                    # Its name ("Developer note"…), or else its style's
                    label = item.get('name') or item.get('style', 'note').title()
                    aside_content = self._convert_content_to_markdown(item.get('content', []), references, level)
                    # Every line quoted, and a blank line after it: the next paragraph
                    # would otherwise continue the quote
                    parts.append(f"\n{quote_blocks(f'**{label}:**', [aside_content.strip()])}\n\n")

                elif item_type == 'row':
                    # Grid layout - process columns
                    for column in item.get('columns', []):
                        col_content = self._convert_content_to_markdown(column.get('content', []), references, level)
                        if col_content.strip():
                            parts.append(col_content)

                elif item_type == 'tabNavigator':
                    # Tabbed content (e.g. one tab per platform): each tab's
                    # title as a bold label, then its content
                    for tab in item.get('tabs', []):
                        tab_content = self._convert_content_to_markdown(tab.get('content', []), references, level)
                        if tab_content.strip():
                            title = tab.get('title', '')
                            if title:
                                parts.append(f"**{title}**:\n\n")
                            parts.append(tab_content)

                elif item_type == 'links':
                    # Links section - resolve and list
                    for link_id in item.get('items', []):
                        ref = references.get(link_id, {})
                        title = ref.get('title', link_id.split('/')[-1])
                        url = ref.get('url', '')
                        abstract = ref.get('abstract', [])
                        abstract_text = self._extract_text_from_inline_content(abstract, references) if abstract else ''

                        if url:
                            parts.append(f"- [{title}]({url})")
                            if abstract_text.strip():
                                # On the item's line: a line break in Apple's text
                                # would continue or end the list
                                parts.append(f" - {one_line(abstract_text)}")
                            parts.append('\n')
                    # A blank line after the list, as after any list
                    parts.append('\n')

                elif item_type == 'table':
                    # Render table
                    header = item.get('header', 'none')
                    rows = item.get('rows', [])
                    if rows:
                        # Assume first row is header if header='row'
                        for i, row in enumerate(rows):
                            cells = []
                            # Handle both formats: list of cells or dict with 'cells' key
                            row_cells = row.get('cells', row) if isinstance(row, dict) else row
                            for cell in row_cells:
                                if isinstance(cell, list):
                                    cell_content = self._convert_content_to_markdown(cell, references, level)
                                else:
                                    cell_content = str(cell)
                                # One line: its line breaks and blank lines (between
                                # paragraphs) as single spaces
                                cells.append(one_line(cell_content))
                            if cells:
                                parts.append('| ' + ' | '.join(cells) + ' |\n')
                                if i == 0 and header == 'row':
                                    parts.append('| ' + ' | '.join(['---'] * len(cells)) + ' |\n')
                        parts.append('\n')

                elif item_type in ('image', 'imageBlock'):
                    # Image block, its caption under it
                    img_id = item.get('identifier', '')
                    img_md = self._figure(self._resolve_image(img_id, references), item, references)
                    if img_md:
                        parts.append(f"\n{img_md}\n\n")

                elif item_type == 'video':
                    # Video block, its caption under it
                    video_id = item.get('identifier', '')
                    video_md = self._figure(self._resolve_video(video_id, references), item, references)
                    if video_md:
                        parts.append(f"\n{video_md}\n\n")

                elif item_type == 'card':
                    # Card (usually a thumbnail image)
                    card_id = item.get('identifier', '')
                    card_md = self._resolve_image(card_id, references)
                    if card_md:
                        parts.append(f"\n{card_md}\n\n")

                elif item_type == 'icon':
                    # Icon/SVG
                    icon_id = item.get('identifier', '')
                    icon_md = self._resolve_image(icon_id, references)
                    if icon_md:
                        parts.append(icon_md)

                elif item_type == 'topic':
                    # Full topic entry with title, abstract, URL
                    title = item.get('title', '')
                    url = item.get('url', '')
                    abstract = item.get('abstract', [])
                    abstract_text = self._extract_text_from_inline_content(abstract, references) if abstract else ''

                    if url and title:
                        local_path = self._convert_url_to_local_path(url)
                        parts.append(f"- [{title}]({local_path})")
                        if abstract_text.strip():
                            parts.append(f" - {one_line(abstract_text)}")
                        parts.append('\n')
                    elif title:
                        parts.append(f"- {title}")
                        if abstract_text.strip():
                            parts.append(f" - {one_line(abstract_text)}")
                        parts.append('\n')

                elif item_type == 'termList':
                    # Definition list
                    for term_item in item.get('items', []):
                        term = term_item.get('term', {})
                        term_text = self._extract_text_from_inline_content(term.get('inlineContent', []), references)
                        definition = term_item.get('definition', {})
                        def_content = self._convert_content_to_markdown(definition.get('content', []), references, level)
                        if term_text:
                            # Its definition after the term (after a blank line when it
                            # starts with a list, code listing, table, quote or heading), and
                            # a blank line after it: the next term would otherwise continue it
                            parts.append(f"{labeled(f'**{term_text}**:', def_content.strip(), 0)}\n\n")

                elif item_type == 'thematicBreak':
                    parts.append('\n---\n\n')

                else:
                    # Not rendered above: its text, never silently dropped, and a WARN
                    self._note_unknown('block type', item_type)
                    parts.append(self._fallback_markdown(item, references))
                    continue

                # Content nested under a type rendered above that doesn't render its own
                if 'content' in item and isinstance(item['content'], list) and item_type not in (
                    'aside', 'table', 'unorderedList', 'orderedList', 'termList'
                ):
                    nested = self._convert_content_to_markdown(item['content'], references, level)
                    if nested.strip():
                        parts.append(nested)

        return join_parts(parts)

    def _extract_to_markdown(self, data: Dict, json_url: str) -> str:
        """Convert JSON data to markdown."""
        parts = []
        references = data.get('references', {})
        # For the WARN of JSON the converter doesn't know
        self.current_url = json_url

        # Get the correct web URL for this page
        web_url = self._convert_json_url_to_web_url(json_url)

        # YAML frontmatter with correct URL and framework
        parts.append("---\n")
        parts.append(f"url: {web_url}\n")
        parts.append("framework: HIG\n")
        parts.append("---\n\n")

        # Title
        metadata = data.get('metadata', {})
        title = metadata.get('title', 'Untitled')
        parts.append(f"# {title}\n\n")

        # Metadata
        role = metadata.get('role', '')
        if role:
            parts.append(f"**Type:** {role}\n\n")

        # Platforms (from customMetadata)
        custom_meta = metadata.get('customMetadata', {})
        platforms = custom_meta.get('supported-platforms', '')
        if platforms:
            platform_list = platforms.replace(',', ', ')
            parts.append(f"**Platforms:** {platform_list}\n\n")

        # Alert (update notices)
        alert_text = custom_meta.get('alert-text', '')
        alert_date = custom_meta.get('alert-date', '')
        if alert_text:
            parts.append(f"> **Updated {alert_date}:** {alert_text}\n\n")

        # Abstract
        abstract = data.get('abstract', [])
        if abstract:
            abstract_text = self._extract_text_from_inline_content(abstract, references)
            if abstract_text:
                parts.append(f"{abstract_text}\n\n")

        # Primary content sections
        for section in data.get('primaryContentSections', []):
            kind = section.get('kind', '')

            if kind == 'content':
                content = section.get('content', [])
                markdown = self._convert_content_to_markdown(content, references)
                if markdown.strip():
                    # One blank line after it (join_parts: one before it)
                    parts.append(markdown.rstrip('\n') + '\n\n')
            else:
                # Not read above: its text, never silently dropped, and a WARN
                self._note_unknown('section kind', kind)
                parts.append(self._fallback_markdown(section, references))

        # Sections (additional content sections in HIG docs)
        for section in data.get('sections', []):
            section_kind = section.get('kind', '')
            if section_kind == 'hero':
                # Hero section - may have images
                hero_image = section.get('image', '')
                if hero_image:
                    img_md = self._resolve_image(hero_image, references)
                    if img_md:
                        parts.append(f"\n{img_md}\n\n")
            elif section_kind == 'volume':
                # Volume section - has chapters
                vol_name = section.get('name', '')
                if vol_name:
                    parts.append(f"\n## {vol_name}\n\n")
                for chapter in section.get('chapters', []):
                    ch_name = chapter.get('name', '')
                    if ch_name:
                        parts.append(f"### {ch_name}\n\n")
                    for topic_id in chapter.get('topicIdentifiers', []):
                        ref = references.get(topic_id, {})
                        ref_title = ref.get('title', topic_id.split('/')[-1])
                        ref_url = ref.get('url', '')
                        if ref_url:
                            local_path = self._convert_url_to_local_path(ref_url)
                            parts.append(f"- [{ref_title}]({local_path})\n")
                        else:
                            parts.append(f"- {ref_title}\n")
                    parts.append('\n')
            else:
                # Not read above: its text, never silently dropped, and a WARN
                self._note_unknown('section kind', section_kind)
                parts.append(self._fallback_markdown(section, references))

        # Topic sections (child pages)
        topic_sections = data.get('topicSections', [])
        if topic_sections:
            parts.append("\n## Topics\n\n")
            for section in topic_sections:
                section_title = section.get('title', '')
                if section_title:
                    parts.append(f"### {section_title}\n\n")

                for identifier in section.get('identifiers', []):
                    ref = references.get(identifier, {})
                    ref_title = ref.get('title', identifier.split('/')[-1])
                    url = ref.get('url', '')
                    ref_abstract = ref.get('abstract', [])
                    abstract_text = self._extract_text_from_inline_content(ref_abstract, references) if ref_abstract else ''

                    if url:
                        local_path = self._convert_url_to_local_path(url)
                        parts.append(f"- [{ref_title}]({local_path})")
                    else:
                        parts.append(f"- {ref_title}")
                    if abstract_text.strip():
                        # On the item's line, as in a links list
                        parts.append(f" - {one_line(abstract_text)}")
                    parts.append('\n')
                parts.append('\n')

        # See also
        see_also = data.get('seeAlsoSections', [])
        if see_also:
            parts.append("\n## See Also\n\n")
            for section in see_also:
                for identifier in section.get('identifiers', []):
                    ref = references.get(identifier, {})
                    ref_title = ref.get('title', identifier.split('/')[-1])
                    url = ref.get('url', '')
                    if url:
                        local_path = self._convert_url_to_local_path(url)
                        parts.append(f"- [{ref_title}]({local_path})\n")
                    else:
                        parts.append(f"- {ref_title}\n")

        # Resources section (related links, developer docs, videos)
        resources_sections = [
            ('Related', custom_meta.get('related', [])),
            ('Developer documentation', custom_meta.get('developerDocumentation', [])),
            ('Videos', custom_meta.get('videos', []))
        ]

        has_resources = any(items for _, items in resources_sections)
        if has_resources:
            parts.append("\n## Resources\n\n")
            for section_name, items in resources_sections:
                if items:
                    parts.append(f"#### {section_name}\n")
                    for item in items:
                        if isinstance(item, str):
                            # It's a reference identifier
                            ref = references.get(item, {})
                            ref_title = ref.get('title', item.split('/')[-1])
                            ref_url = ref.get('url', '')
                            if ref_url:
                                local_path = self._convert_url_to_local_path(ref_url)
                                parts.append(f"[{ref_title}]({local_path})\n")
                            else:
                                parts.append(f"{ref_title}\n")
                        elif isinstance(item, dict):
                            item_title = item.get('title', '')
                            item_url = item.get('url', '')
                            if item_url and item_title:
                                local_path = self._convert_url_to_local_path(item_url)
                                parts.append(f"[{item_title}]({local_path})\n")

        # Change log from customMetadata
        change_log = custom_meta.get('changeLog', [])
        if change_log:
            parts.append("\n## Change log\n")
            parts.append("| Date | Changes |\n")
            parts.append("| --- | --- |\n")
            for entry in change_log:
                date = entry.get('date', '')
                changes = entry.get('change', '')
                parts.append(f"| {date} | {changes} |\n")

        # Source URL
        parts.append(f"\n\n---\n*Source: [{web_url}]({web_url})*\n")

        # No 3+ newlines where the sections meet
        return join_parts(parts)

    async def scrape_page(self, json_url: str, data: Optional[Dict] = None) -> bool:
        """Scrape a single page and save it.

        Args:
            json_url: URL of the JSON file
            data: Optional pre-fetched JSON data to avoid duplicate requests

        Returns:
            True if the page's file was written

        Raises:
            Exception: The page failed to convert or save (an error of ours;
                its hash entry is left as it was)
        """
        if json_url in self.processed_urls and data is None:
            return False

        self.processed_urls.add(json_url)

        # Use pre-fetched data or fetch now
        if data is None:
            fetched = await self.fetch_json(json_url)
            if isinstance(fetched, FetchFailed):
                self.stats['pages_gone' if fetched.gone else 'pages_failed'] += 1
                return False
            data = fetched

        # Convert to markdown
        content = json.dumps(data)  # For hash checking

        # Get file path
        file_path = self._get_file_path(json_url, data)

        # Check if content has changed (or its file is missing)
        if not self._has_changed(json_url, content, file_path):
            self.stats['pages_skipped'] += 1
            return False

        # Convert to markdown
        markdown = self._extract_to_markdown(data, json_url)

        # Save file (whole or not at all: a failed write keeps the old doc)
        if not self.dry_run:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            write_text_atomic(file_path, markdown)

            # Update hash
            self._update_hash(json_url, content, file_path)

        self.stats['pages_scraped'] += 1
        return True

    def _prune_hashes(self, run: ScrapeRun) -> int:
        """After a clean run, drop the hash entries of deleted files: pages
        this run didn't produce or keep whose file is gone. Returns how many."""
        stale = [
            url for url in self.hashes
            if url not in run.produced and not run.keeps_key(url) and not self._get_file_path(url, {}).exists()
        ]
        for url in stale:
            del self.hashes[url]
        if stale:
            self.hashes_modified = True
        return len(stale)

    async def scrape_all(self) -> None:
        """Scrape all HIG documentation, clean up orphans and save (sets exit_code)."""
        self.stats['start_time'] = time.time()
        run = ScrapeRun("HIG", OUTPUT_DIR.parent, self.stored_metadata, self.load_error,
                        render_version=RENDER_VERSION)
        self.run = run
        # Rendered by another converter version: every page again, as --force
        rerender = run.render_stale and not self.force
        self.force = self.force or run.render_stale

        console.print(f"[bold blue]Apple Human Interface Guidelines Scraper[/bold blue]")
        console.print(f"Output: {OUTPUT_DIR}")
        if self.dry_run:
            console.print("[yellow]DRY RUN - no files will be written[/yellow]")
        if rerender:
            console.print(f"[yellow]RENDER VERSION {RENDER_VERSION} - rendering all files again[/yellow]")
        elif self.force:
            console.print("[yellow]FORCE MODE - re-downloading all files[/yellow]")
        console.print()

        # Ensure output directory exists
        if not self.dry_run:
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Start with the HIG root page
        root_url = f"{JSON_BASE_URL}/{HIG_ROOT}.json"

        # Use iterative BFS to discover and scrape all pages
        url_queue = deque([root_url])

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("{task.completed} pages"),
            console=console
        ) as progress:
            task = progress.add_task("Scraping HIG...", total=None)

            while url_queue:
                json_url = url_queue.popleft()

                if json_url in self.processed_urls:
                    continue
                self.processed_urls.add(json_url)
                file_path = self._get_file_path(json_url, {})

                # Fetch page
                data = await self.fetch_json(json_url)
                if isinstance(data, FetchFailed):
                    self.stats['pages_gone' if data.gone else 'pages_failed'] += 1
                    if json_url == root_url:
                        # The root: nothing else is reached this run; every key and file stays
                        run.source_failed(json_url, data, KeptLocation(OUTPUT_DIR, reason=""), key_prefix="")
                    elif run.page_failed(json_url, data, previously_good=self._previously_good(json_url, file_path)):
                        run.keep_file(json_url, file_path)
                    continue
                if json_url == root_url:
                    run.source_ok(json_url)
                run.page_ok(json_url, file_path)

                # Links first: queue the children before converting, so a page
                # that fails to convert or save still leads to them
                try:
                    child_urls = self._extract_urls_from_json(data)
                except Exception as e:
                    self.stats['pages_failed'] += 1
                    run.unprocessed(json_url, file_path, f"{type(e).__name__}: {e}")
                    continue
                for child_url in child_urls:
                    if child_url not in self.processed_urls:
                        url_queue.append(child_url)

                # Process and save (pass pre-fetched data to avoid duplicate request)
                try:
                    await self.scrape_page(json_url, data=data)
                except Exception as e:
                    self.stats['pages_failed'] += 1
                    run.local_error(json_url, file_path, f"{type(e).__name__}: {e}")
                else:
                    run.page_saved(json_url)

                # Update progress
                total_processed = (self.stats['pages_scraped'] + self.stats['pages_skipped'] + self.stats['pages_gone']
                                   + self.stats['pages_failed'])
                progress.update(task, completed=total_processed, description=f"Scraping HIG... (queue: {len(url_queue)})")

        # One WARN per block or inline type or section kind the converter doesn't know
        self._log_unknown_content()

        # Clean up orphaned files (pages Apple no longer links, or that
        # returned 404/410), unless a failure of ours blocks it
        cleanup: CleanupResult = run.cleanup([OUTPUT_DIR], dry_run=self.dry_run)
        pruned = 0
        if not cleanup.skipped and not self.dry_run:
            pruned = self._prune_hashes(run)
        # Storing a new render version: a file this run didn't render (e.g. held
        # by the valve) has the old rendering, so its key loses its source hash
        for url in run.unrendered_keys(self.hashes):
            entry = self.hashes[url]
            if isinstance(entry, dict) and entry.get('hash'):
                entry['hash'] = ''
                self.hashes_modified = True

        # Save whenever the hashes or the failure policy's metadata changed
        self.final_metadata = run.metadata(self.hashes)
        if not self._save_hashes():
            run.error(f"hash_save_failed: {HASH_FILE}")

        self.stats['end_time'] = time.time()

        # Print summary
        duration = self.stats['end_time'] - self.stats['start_time']
        console.print()
        console.print("[bold green]Scraping Complete![/bold green]")
        console.print(f"  Scraped: {self.stats['pages_scraped']}")
        console.print(f"  Skipped (unchanged): {self.stats['pages_skipped']}")
        if self.stats['pages_gone']:
            console.print(f"  Gone (404/410): {self.stats['pages_gone']}")
        console.print(f"  Failed: {self.stats['pages_failed']}")
        if cleanup.deleted:
            console.print(f"  Deleted (orphaned): {len(cleanup.deleted)}")
        if pruned:
            console.print(f"  Pruned hash entries: {pruned}")
        for line in run.summary_lines(cleanup):
            console.print(f"  {line}", markup=False)
        console.print(f"  Duration: {duration:.1f}s")

        self.exit_code = run.exit_code()


async def main() -> int:
    parser = argparse.ArgumentParser(description="Scrape Apple Human Interface Guidelines")
    parser.add_argument('--dry-run', action='store_true', help="Don't write files, just show what would be done")
    parser.add_argument('--force', action='store_true', help="Re-download all files regardless of cache")
    args = parser.parse_args()

    async with HIGDocsScraper(force=args.force, dry_run=args.dry_run) as scraper:
        await scraper.scrape_all()
    return scraper.exit_code


if __name__ == "__main__":
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted[/yellow]")
        sys.exit(130)
