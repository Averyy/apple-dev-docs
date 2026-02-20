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
"""

import argparse
import asyncio
import json
import logging
import os
import re
import sys
import time
from collections import deque
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import httpx
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

from utilities.hash_utils import compute_hash

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

        # Statistics
        self.stats = {
            "pages_scraped": 0,
            "pages_skipped": 0,
            "pages_failed": 0,
            "start_time": None,
            "end_time": None
        }

        # Topic hierarchy for organized file structure
        self.topic_hierarchy: Dict[str, Dict] = {}

    async def __aenter__(self):
        """Async context manager entry."""
        self.session = httpx.AsyncClient(
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "AppleDocsBot/1.0"},
            follow_redirects=True
        )
        self._load_hashes()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self.session:
            await self.session.aclose()
        self._save_hashes()

    def _load_hashes(self):
        """Load stored hashes for incremental updates."""
        if HASH_FILE.exists():
            try:
                with open(HASH_FILE, 'r') as f:
                    self.hashes = json.load(f)
                logger.info(f"Loaded {len(self.hashes)} existing hashes")
            except Exception as e:
                logger.warning(f"Could not load hash file: {e}")
                self.hashes = {}
        else:
            self.hashes = {}

    def _save_hashes(self):
        """Save hashes for next run."""
        if self.hashes_modified and not self.dry_run:
            try:
                HASH_FILE.parent.mkdir(parents=True, exist_ok=True)
                with open(HASH_FILE, 'w') as f:
                    json.dump(self.hashes, f, indent=2)
                logger.info(f"Saved {len(self.hashes)} hashes")
            except Exception as e:
                logger.error(f"Could not save hash file: {e}")

    def _compute_hash(self, content: str) -> str:
        """Compute SHA-256 hash of content."""
        return compute_hash(content)

    def _has_changed(self, url: str, content: str) -> bool:
        """Check if content has changed since last scrape."""
        if self.force:
            return True

        new_hash = self._compute_hash(content)
        old_data = self.hashes.get(url, {})
        old_hash = old_data.get('hash', '')

        return new_hash != old_hash

    def _update_hash(self, url: str, content: str, file_path: Path):
        """Update hash for a URL."""
        self.hashes[url] = {
            'hash': self._compute_hash(content),
            'file_path': str(file_path),
            'last_updated': datetime.utcnow().isoformat()
        }
        self.hashes_modified = True

    async def fetch_json(self, url: str) -> Optional[Dict]:
        """Fetch and parse JSON from URL."""
        if not self.session:
            raise RuntimeError("Scraper must be used as async context manager")

        await asyncio.sleep(REQUEST_DELAY)

        try:
            response = await self.session.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                logger.debug(f"Not found: {url}")
            else:
                logger.warning(f"HTTP error {e.response.status_code} for {url}")
            return None
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    def _convert_url_to_local_path(self, url: str) -> str:
        """Convert a URL to a local markdown path.

        HIG internal links: /design/human-interface-guidelines/X -> X.md
        HIG anchors: /design/human-interface-guidelines/X#anchor -> X.md#anchor
        Apple docs: /documentation/Framework/Symbol -> ../Framework/Symbol.md
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

        # Handle Apple documentation links - convert to relative path to our docs
        # /documentation/Framework/Symbol -> ../Framework/Symbol.md
        doc_pattern = r'^/documentation/(.+?)(?:#(.+))?$'
        match = re.match(doc_pattern, url)
        if match:
            doc_path = match.group(1)
            anchor = match.group(2)
            # Build relative path from HIG folder to documentation folder
            # HIG is at documentation/HIG/, other docs at documentation/{Framework}/
            local_path = f"../{doc_path}.md"
            if anchor:
                local_path += f"#{anchor}"
            return local_path

        # Keep external URLs as-is
        return url

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

    def _extract_urls_from_content(self, content: List, urls: List[str]):
        """Recursively extract URLs from content blocks."""
        for item in content:
            if isinstance(item, dict):
                # Check for links items
                if item.get('type') == 'links':
                    for link_id in item.get('items', []):
                        json_url = self._convert_identifier_to_json_url(link_id)
                        if json_url:
                            urls.append(json_url)

                # Recurse into nested content
                for key in ['content', 'items', 'columns']:
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
                    parts.append(f"*{inner}*")
                elif item_type == 'strong':
                    inner = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    parts.append(f"**{inner}**")
                elif item_type == 'reference':
                    # Resolve reference
                    ref_id = item.get('identifier', '')
                    ref = references.get(ref_id, {})
                    title = ref.get('title', item.get('overridingTitle', ref_id.split('/')[-1]))
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
                    # Resolve image from references to get URL
                    img_id = item.get('identifier', '')
                    img_ref = references.get(img_id, {})
                    variants = img_ref.get('variants', [])
                    if variants:
                        # Get highest resolution variant
                        img_url = variants[-1].get('url', '')
                        alt = img_ref.get('alt', img_id)
                        if img_url:
                            parts.append(f"![{alt}]({img_url})")
                elif item_type == 'inlineHead':
                    inner = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    parts.append(f"**{inner}**")
                elif item_type == 'newTerm':
                    inner = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    parts.append(f"*{inner}*")
                elif item_type == 'superscript':
                    inner = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    parts.append(f"<sup>{inner}</sup>")
                elif item_type == 'subscript':
                    inner = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    parts.append(f"<sub>{inner}</sub>")
        return ''.join(parts)

    def _resolve_image(self, identifier: str, references: Dict) -> str:
        """Resolve an image identifier to markdown."""
        ref = references.get(identifier, {})
        variants = ref.get('variants', [])
        if variants:
            # Get highest resolution variant
            img_url = variants[-1].get('url', '')
            alt = ref.get('alt', identifier)
            if img_url:
                return f"![{alt}]({img_url})"
        return ''

    def _resolve_video(self, identifier: str, references: Dict) -> str:
        """Resolve a video identifier to markdown link."""
        ref = references.get(identifier, {})
        variants = ref.get('variants', [])
        if variants:
            video_url = variants[-1].get('url', '')
            if video_url:
                return f"[Video: {identifier}]({video_url})"
        return ''

    def _convert_content_to_markdown(self, content: List, references: Dict, level: int = 2) -> str:
        """Convert content blocks to markdown."""
        parts = []

        for item in content:
            if isinstance(item, dict):
                item_type = item.get('type', '')

                if item_type == 'paragraph':
                    text = self._extract_text_from_inline_content(item.get('inlineContent', []), references)
                    if text:
                        parts.append(text + '\n')

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
                            # Format as list item
                            lines = list_text.strip().split('\n')
                            parts.append(f"- {lines[0]}\n")
                            for line in lines[1:]:
                                if line.strip():
                                    parts.append(f"  {line}\n")

                elif item_type == 'orderedList':
                    for i, list_item in enumerate(item.get('items', []), 1):
                        item_content = list_item.get('content', [])
                        list_text = self._convert_content_to_markdown(item_content, references, level)
                        if list_text.strip():
                            lines = list_text.strip().split('\n')
                            parts.append(f"{i}. {lines[0]}\n")
                            for line in lines[1:]:
                                if line.strip():
                                    parts.append(f"   {line}\n")

                elif item_type == 'aside':
                    style = item.get('style', 'note')
                    aside_content = self._convert_content_to_markdown(item.get('content', []), references, level)
                    parts.append(f"\n> **{style.title()}:** {aside_content.strip()}\n")

                elif item_type == 'row':
                    # Grid layout - process columns
                    for column in item.get('columns', []):
                        col_content = self._convert_content_to_markdown(column.get('content', []), references, level)
                        if col_content.strip():
                            parts.append(col_content)

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
                            if abstract_text:
                                parts.append(f" - {abstract_text}")
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
                                cells.append(cell_content.strip().replace('\n', ' '))
                            if cells:
                                parts.append('| ' + ' | '.join(cells) + ' |\n')
                                if i == 0 and header == 'row':
                                    parts.append('| ' + ' | '.join(['---'] * len(cells)) + ' |\n')
                        parts.append('\n')

                elif item_type in ('image', 'imageBlock'):
                    # Image block
                    img_id = item.get('identifier', '')
                    img_md = self._resolve_image(img_id, references)
                    if img_md:
                        parts.append(f"\n{img_md}\n")

                elif item_type == 'video':
                    # Video block
                    video_id = item.get('identifier', '')
                    video_md = self._resolve_video(video_id, references)
                    if video_md:
                        parts.append(f"\n{video_md}\n")

                elif item_type == 'card':
                    # Card (usually a thumbnail image)
                    card_id = item.get('identifier', '')
                    card_md = self._resolve_image(card_id, references)
                    if card_md:
                        parts.append(f"\n{card_md}\n")

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
                        if abstract_text:
                            parts.append(f" - {abstract_text}")
                        parts.append('\n')
                    elif title:
                        parts.append(f"- {title}")
                        if abstract_text:
                            parts.append(f" - {abstract_text}")
                        parts.append('\n')

                elif item_type == 'termList':
                    # Definition list
                    for term_item in item.get('items', []):
                        term = term_item.get('term', {})
                        term_text = self._extract_text_from_inline_content(term.get('inlineContent', []), references)
                        definition = term_item.get('definition', {})
                        def_content = self._convert_content_to_markdown(definition.get('content', []), references, level)
                        if term_text:
                            parts.append(f"**{term_text}**: {def_content.strip()}\n")

                # Handle nested content for any unhandled types
                if 'content' in item and isinstance(item['content'], list) and item_type not in (
                    'aside', 'table', 'unorderedList', 'orderedList', 'termList'
                ):
                    nested = self._convert_content_to_markdown(item['content'], references, level)
                    if nested.strip():
                        parts.append(nested)

        return ''.join(parts)

    def _extract_to_markdown(self, data: Dict, json_url: str) -> str:
        """Convert JSON data to markdown."""
        parts = []
        references = data.get('references', {})

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
                    parts.append(markdown + '\n')

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
                    if abstract_text:
                        parts.append(f" - {abstract_text}")
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

        return ''.join(parts)

    async def scrape_page(self, json_url: str, data: Optional[Dict] = None) -> bool:
        """Scrape a single page and save it.

        Args:
            json_url: URL of the JSON file
            data: Optional pre-fetched JSON data to avoid duplicate requests
        """
        if json_url in self.processed_urls:
            return False

        self.processed_urls.add(json_url)

        # Use pre-fetched data or fetch now
        if data is None:
            data = await self.fetch_json(json_url)
            if not data:
                self.stats['pages_failed'] += 1
                return False

        # Convert to markdown
        content = json.dumps(data)  # For hash checking

        # Check if content has changed
        if not self._has_changed(json_url, content):
            self.stats['pages_skipped'] += 1
            return False

        # Get file path
        file_path = self._get_file_path(json_url, data)

        # Convert to markdown
        markdown = self._extract_to_markdown(data, json_url)

        # Save file
        if not self.dry_run:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown)

            # Update hash
            self._update_hash(json_url, content, file_path)

        self.stats['pages_scraped'] += 1
        return True

    async def scrape_all(self):
        """Scrape all HIG documentation."""
        self.stats['start_time'] = time.time()

        console.print(f"[bold blue]Apple Human Interface Guidelines Scraper[/bold blue]")
        console.print(f"Output: {OUTPUT_DIR}")
        if self.dry_run:
            console.print("[yellow]DRY RUN - no files will be written[/yellow]")
        if self.force:
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

                # Fetch page
                data = await self.fetch_json(json_url)
                if not data:
                    self.processed_urls.add(json_url)
                    self.stats['pages_failed'] += 1
                    continue

                # Process and save (pass pre-fetched data to avoid duplicate request)
                await self.scrape_page(json_url, data=data)

                # Extract child URLs and add to queue
                child_urls = self._extract_urls_from_json(data)
                for child_url in child_urls:
                    if child_url not in self.processed_urls:
                        url_queue.append(child_url)

                # Update progress
                total_processed = self.stats['pages_scraped'] + self.stats['pages_skipped'] + self.stats['pages_failed']
                progress.update(task, completed=total_processed, description=f"Scraping HIG... (queue: {len(url_queue)})")

        self.stats['end_time'] = time.time()

        # Print summary
        duration = self.stats['end_time'] - self.stats['start_time']
        console.print()
        console.print("[bold green]Scraping Complete![/bold green]")
        console.print(f"  Scraped: {self.stats['pages_scraped']}")
        console.print(f"  Skipped (unchanged): {self.stats['pages_skipped']}")
        console.print(f"  Failed: {self.stats['pages_failed']}")
        console.print(f"  Duration: {duration:.1f}s")


async def main():
    parser = argparse.ArgumentParser(description="Scrape Apple Human Interface Guidelines")
    parser.add_argument('--dry-run', action='store_true', help="Don't write files, just show what would be done")
    parser.add_argument('--force', action='store_true', help="Re-download all files regardless of cache")
    args = parser.parse_args()

    async with HIGDocsScraper(force=args.force, dry_run=args.dry_run) as scraper:
        await scraper.scrape_all()


if __name__ == "__main__":
    asyncio.run(main())
