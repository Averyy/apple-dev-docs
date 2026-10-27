#!/usr/bin/env python3
"""Extract metadata from Apple Developer documentation markdown files."""

import re
import os
import json
import hashlib
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any, Set, Tuple
import argparse
from datetime import datetime
from urllib.parse import unquote

# The kind of an Apple page without a **Kind** line, by its **Role** line (Apple's
# roleHeading); any other role, or none, is an article. A Framework role always comes
# with **Kind**: module.
ROLE_KINDS = {"Article": "article", "API Collection": "collection", "Sample Code": "sample-code"}

# An overview's most characters (extract_overview); the cut never falls inside a link
OVERVIEW_MAX_CHARS = 500


class MetadataExtractor:
    """Extract structured metadata from Apple documentation markdown files."""

    def __init__(self):
        # Common platform mappings
        self.platform_mappings = {
            "ios": "iOS",
            "macos": "macOS",
            "mac os": "macOS",
            "mac os x": "macOS",
            "osx": "macOS",
            "os x": "macOS",
            "tvos": "tvOS",
            "watchos": "watchOS",
            "visionos": "visionOS",
            "vision os": "visionOS",
            "catalyst": "Mac Catalyst",
            "mac catalyst": "Mac Catalyst",
            "ipad": "iPadOS",
            "ipados": "iPadOS"
        }

        # Framework name normalization
        self.framework_aliases = {
            "swiftui": "SwiftUI",
            "swift ui": "SwiftUI",
            "uikit": "UIKit",
            "ui kit": "UIKit",
            "appkit": "AppKit",
            "app kit": "AppKit",
            "storekit": "StoreKit",
            "store kit": "StoreKit",
            "spritekit": "SpriteKit",
            "sprite kit": "SpriteKit",
            "scenekit": "SceneKit",
            "scene kit": "SceneKit",
            "coredata": "CoreData",
            "core data": "CoreData",
            "corelocation": "CoreLocation",
            "core location": "CoreLocation",
            "avfoundation": "AVFoundation",
            "av foundation": "AVFoundation",
            "foundation": "Foundation",
            "combine": "Combine",
            "metal": "Metal",
            "cloudkit": "CloudKit",
            "cloud kit": "CloudKit",
            "healthkit": "HealthKit",
            "health kit": "HealthKit",
            "gamekit": "GameKit",
            "game kit": "GameKit",
            "mapkit": "MapKit",
            "map kit": "MapKit",
            "webkit": "WebKit",
            "web kit": "WebKit",
            "realitykit": "RealityKit",
            "reality kit": "RealityKit",
            "arkit": "ARKit",
            "ar kit": "ARKit",
            # MLX ecosystem frameworks
            "mlx": "MLX",
            "mlx-swift": "MLX-Swift",
            "mlx swift": "MLX-Swift",
            "coremltools": "coremltools",
            "core ml tools": "coremltools",
            "ml-stable-diffusion": "ml-stable-diffusion",
            "ml stable diffusion": "ml-stable-diffusion"
        }

        # Apple's **Kind** values (the page's symbolKind, lowercased, including the legacy
        # reference's codes) -> kind. A value missing here is "unknown" (e.g. "uid", the
        # Installer JS and WebKit JS pseudo-symbols, which are objects, methods and
        # properties alike); a page with no **Kind** line is kinded by its **Role** line
        # (ROLE_KINDS), else an "article".
        self.kind_mappings = {
            # Types
            "class": "class",
            "cl": "class",
            "struct": "struct",
            "enum": "enum",
            "protocol": "protocol",
            "intf": "protocol",
            "actor": "actor",
            "extension": "extension",
            "union": "union",
            "typealias": "typealias",
            "tdef": "typealias",
            "associatedtype": "associatedtype",
            "tag": "type",  # a C struct, enum or union tag
            "namespace": "namespace",
            "module": "module",
            "macro": "macro",
            # Members and globals
            "method": "method",
            "instm": "method",
            "clm": "method",
            "intfm": "method",
            "func": "function",
            "init": "init",
            "structctr": "init",
            "instctr": "init",
            "intfctr": "init",
            "property": "property",
            "instp": "property",
            "structp": "property",
            "intfp": "property",
            "enump": "property",
            "unionp": "property",
            "cldata": "property",
            "structdata": "property",
            "clconst": "property",
            "pseudo": "property",  # a C++ class's member variable
            "var": "variable",
            "data": "variable",
            "case": "case",
            "enumelt": "case",
            "econst": "case",
            "subscript": "subscript",
            "instsub": "subscript",
            "op": "operator",
            "opfunc": "operator",
            # Web services and property lists
            "httprequest": "endpoint",
            "dictionary": "object",
        }

        # Pre-compile regex patterns for performance (called 334K+ times during indexing)
        self._compile_patterns()

    def _compile_patterns(self):
        """Pre-compile all regex patterns used during extraction."""
        # YAML frontmatter
        self._yaml_end_pattern = re.compile(r'\n---\s*\n')

        # Title extraction (extract_title): the page's "# " heading; a heading line of any
        # level, without its closing #s; a code fence's opening or closing line
        self._title_h1_pattern = re.compile(r'^#\s+(.+)$', re.MULTILINE)
        self._heading_line_pattern = re.compile(r'^(#{1,6})[ \t]+(.+?)(?:[ \t]+#+)?[ \t]*$')
        self._fence_pattern = re.compile(r'^[ \t]*(`{3,}|~{3,})')

        # The header under the title: "**Key**: value" lines (Apple pages: Framework,
        # Kind, Required; the HIG writes "**Key:** value"). An empty value heads a list
        # ("**Availability**:" and its "- ..." items).
        self._header_line_pattern = re.compile(
            r'^\*\*(?P<key>[^*:\n]+)(?:\*\*:|:\*\*)[ \t]*(?P<value>[^\n]*?)[ \t]*$')
        self._header_block_pattern = re.compile(
            r'(?:[ \t]*\n)+((?:\*\*[^*:\n]+(?:\*\*:|:\*\*)[^\n]*(?:\n|\Z))+)')

        # A symbol's base name: its title without argument labels or qualifier
        self._qualified_name_pattern = re.compile(r'[^\W\d]\w*(?:(?:\.|::)[^\W\d]\w*)+')
        self._qualifier_split_pattern = re.compile(r'\.|::')

        # The footer every DocC page ends with (markdown_converter.py): the URL it was
        # scraped from, as a link holds it (scraper/utils/links.py markdown_url: the
        # parentheses of a URL the site cut inside its argument list are encoded; an
        # older rendering has them as they are); Apple's says "View on Apple Developer",
        # another DocC site's its own name (e.g. "View on docs.swift.org")
        self._footer_pattern = re.compile(r'^\*\[View on [^\]\n]+\]\((https?://\S+)\)\*$')

        # Platform extraction patterns
        # Apple's **Availability** list, one platform per item:
        # "- <platform>[ <version>+][ (Beta)][ - Deprecated[ in <version>][: <message>]]".
        # The version is anything up to its "+" (legacy pages have "?+").
        self._availability_list_pattern = re.compile(
            r'^\*\*Availability\*\*:[ \t]*\n((?:- [^\n]*(?:\n|\Z))+)', re.MULTILINE)
        self._availability_item_pattern = re.compile(
            r'^- (?P<platform>.+?)(?: (?P<intro>[^\s+]+)\+)?(?: \(Beta\))?'
            r'(?P<deprecated> - Deprecated(?: in (?P<dep>[\w.]+))?(?:: .*| \(renamed: .*\))?)?$')
        # Apple's deprecation summary (markdown_converter.py): a "> **Deprecated**: …" quote
        # (and its "> " lines) after the abstract and the **Availability** list, before the
        # page's first section
        self._deprecation_summary_pattern = re.compile(r'^> \*\*Deprecated\*\*:[^\n]*(?:\n>[^\n]*)*', re.MULTILINE)
        self._section_heading_pattern = re.compile(r'^#{2,6}\s', re.MULTILINE)
        self._platform_patterns = [
            re.compile(r'(?:Platforms?|Available on|Supported on):\s*([^\n]+)', re.IGNORECASE),
            re.compile(r'!\[.*?\]\(.*?badge.*?(ios|macos|tvos|watchos|visionos|catalyst).*?\)', re.IGNORECASE),
            re.compile(r'`(?:iOS|macOS|tvOS|watchOS|visionOS|Mac Catalyst)(?:\s+[\d.]+)?`', re.IGNORECASE),
            re.compile(r'@available\s*\(([^)]+)\)', re.IGNORECASE),
        ]
        self._platform_split_pattern = re.compile(r'[,;|]')

        # Combined platform detection pattern for content scanning (single pass). Whole
        # words only, "IOService" and "IOSurface" don't name iOS, but a version may follow
        # ("iOS18", "macOS12+")
        platform_keys = '|'.join(re.escape(k) for k in self.platform_mappings.keys())
        self._platform_scan_pattern = re.compile(rf'(?<!\w)({platform_keys})(?![^\W\d])', re.IGNORECASE)

        # Overview extraction: a section heading, never the page's title (a symbol named
        # description or summary would get its header lines as its overview)
        self._overview_heading_pattern = re.compile(
            r'^#{2,}[ \t]*(?:Overview|Description|Summary|Introduction)[ \t]*$',
            re.IGNORECASE | re.MULTILINE
        )
        self._rule_pattern = re.compile(r'-{3,}|\*{3,}|_{3,}')
        # A markdown link or image, its text holding brackets two levels deep and its
        # destination balanced parentheses (cut_overview)
        self._markdown_link_pattern = re.compile(
            r'!?\[(?:[^\[\]]|\[(?:[^\[\]]|\[[^\[\]]*\])*\])*\]\((?:[^()\s]|\([^()\s]*\))*\)')
        self._whitespace_pattern = re.compile(r'\s+')
        self._word_pattern = re.compile(r'\w')

        # Framework main page indicators
        self._framework_indicator_patterns = [
            re.compile(r'^\s*#\s+\w+\s+Framework', re.IGNORECASE | re.MULTILINE),
            re.compile(r'^\s*#\s+\w+\s+Module', re.IGNORECASE | re.MULTILINE),
            re.compile(r'^\s*#\s+About\s+\w+', re.IGNORECASE | re.MULTILINE),
            re.compile(r'^\s*#\s+\w+\s+Overview', re.IGNORECASE | re.MULTILINE),
        ]

    def parse_yaml_frontmatter(self, content: str) -> Dict[str, Any]:
        """Parse YAML frontmatter from markdown content.

        Args:
            content: The markdown content

        Returns:
            Dictionary of frontmatter values, empty if none found
        """
        # Check for YAML frontmatter (starts with --- on first line)
        if not content.startswith('---'):
            return {}

        # Find the closing ---
        end_match = self._yaml_end_pattern.search(content[3:])
        if not end_match:
            return {}

        frontmatter_text = content[3:end_match.start() + 3]

        try:
            frontmatter = yaml.safe_load(frontmatter_text)
            if isinstance(frontmatter, dict):
                return frontmatter
        except yaml.YAMLError:
            pass

        return {}

    def extract_metadata(self, content: str, file_path: str) -> Dict[str, Any]:
        """Extract all metadata from a documentation file.

        Args:
            content: The markdown content
            file_path: Path to the file for context

        Returns:
            Dictionary containing extracted metadata
        """
        # Parse frontmatter first for overrides
        frontmatter = self.parse_yaml_frontmatter(content)

        metadata = {
            "id": self.generate_document_id(file_path),
            "file_path": self.normalize_file_path(file_path),
            "framework": self.extract_framework(content, file_path),
            "api_name": self.extract_api_name(content, file_path),
            "title": self.extract_title(content, file_path),
            "platforms": self.extract_platforms(content),
            "kind": self.extract_kind(content),
            "deprecated": self.extract_deprecated(content),
            "deprecation": self.extract_deprecation(content),
            "overview": self.extract_overview(content),
            "is_framework_main": self.is_framework_main_page(content, file_path),
            "last_modified": self.get_file_modified_time(file_path),
            "url": frontmatter.get("url") or self.extract_source_url(content) or self.generate_url(file_path),
            "file_size": os.path.getsize(file_path) if os.path.exists(file_path) else 0
        }

        # Clean up None values
        return {k: v for k, v in metadata.items() if v is not None}
    
    def normalize_file_path(self, file_path: str) -> str:
        """Convert absolute file path to relative path starting from documentation/"""
        path = Path(file_path)
        parts = list(path.parts)
        
        # Find the documentation directory and return path from there
        if "documentation" in parts:
            doc_index = parts.index("documentation")
            relative_parts = parts[doc_index:]  # Include 'documentation' itself
            return "/".join(relative_parts)
        
        # Fallback: if no documentation found, the whole path, so that files of the same
        # name (each index.md) keep distinct file_paths and ids
        return path.as_posix()
    
    def generate_document_id(self, file_path: str) -> str:
        """
        Document ID: the SHA-1 of the file's file_path (normalize_file_path), in hex.

        One per path, as file_path is (case and every character count), and always a
        valid Meilisearch id (40 of [0-9a-f]). An id built from the path's characters
        lowercased, with every other character replaced by "_", gave different files the
        same id, and the last one sent replaced the others in the index.
        """
        # A file name that isn't valid UTF-8 (Linux allows it) hashes as its bytes; the
        # indexer then leaves the file out for its file_path
        path_bytes = self.normalize_file_path(file_path).encode('utf-8', 'surrogateescape')
        return hashlib.sha1(path_bytes).hexdigest()
    
    def extract_framework(self, content: str, file_path: str) -> str:
        """Extract framework name from content or path."""
        # Try YAML frontmatter first (used by MLX scraper)
        frontmatter = self.parse_yaml_frontmatter(content)
        if frontmatter.get("framework"):
            return self.normalize_framework_name(frontmatter["framework"])

        # Try to get from file path
        path_parts = Path(file_path).parts

        # Look for documentation/FrameworkName pattern
        if "documentation" in path_parts:
            idx = path_parts.index("documentation")
            if idx + 1 < len(path_parts):
                framework = path_parts[idx + 1]
                # Normalize framework name
                return self.normalize_framework_name(framework)

        # Try to extract from content
        # Look for "Framework: Name" pattern
        framework_match = re.search(r'(?:Framework|Module):\s*(\w+)', content, re.IGNORECASE)
        if framework_match:
            return self.normalize_framework_name(framework_match.group(1))

        # Look for imports or module declarations
        import_match = re.search(r'import\s+(\w+)', content)
        if import_match:
            return self.normalize_framework_name(import_match.group(1))

        # Default to first directory under documentation
        if len(path_parts) > 1:
            return self.normalize_framework_name(path_parts[1])

        return "Unknown"
    
    def normalize_framework_name(self, name: str) -> str:
        """Normalize framework name to consistent casing."""
        name_lower = name.lower()
        return self.framework_aliases.get(name_lower, name)
    
    def extract_api_name(self, content: str, file_path: str) -> str:
        """
        API name: the base name of the page's title (base_name; is_nested_title tells a
        nested symbol's qualified name from a dotted name), e.g. "init" for
        init(viewControllerProvider:). Never a name from the page's code or prose, which
        named another symbol (or "An", "The"…) on a third of Apple's symbol pages.
        """
        title = self.extract_title(content)
        if title:
            return self.base_name(title, nested=self.is_nested_title(content, title))
        
        # Get from filename as last resort
        filename = Path(file_path).stem
        if filename and filename != "index":
            return filename
        
        return "Unknown"

    def base_name(self, title: str, nested: bool = True) -> str:
        """
        A title's base name: without its argument labels (init(frame:) -> init,
        ==(_:_:) -> ==) and, when it is a nested symbol's (nested), without its qualifier
        (Product.SubscriptionOffer -> SubscriptionOffer, IOHIDInterface::InterruptReportAction
        -> InterruptReportAction). Any other title (an article's, "Vector3 (Half)", an
        operator such as .<=) is kept whole.
        """
        name = title.strip()
        paren = name.find('(')
        if paren > 0 and name.endswith(')') and not name[paren - 1].isspace():
            name = name[:paren]
        if nested and self._qualified_name_pattern.fullmatch(name):
            name = self._qualifier_split_pattern.split(name)[-1]
        return name

    def is_nested_title(self, content: str, title: str) -> bool:
        """
        Whether the page's dotted (or ::) title is a nested symbol's qualified name rather
        than the page's own name. On an Apple page (the footer) it is not when the page is
        an article (no **Kind** line, e.g. the header file AXError.h) or when its URL names
        it by the whole title (a property list key such as com.apple.security.network.client,
        CloudKit JS's CloudKit.Database): Apple puts a nested symbol under its parent's page,
        named by its own name (arkit/accessory/chirality for Accessory.Chirality). Other
        sources' dotted titles are qualified API names (MLX's mlx.core.array).
        """
        name = self.base_name(title, nested=False)
        if not self._qualified_name_pattern.fullmatch(name):
            return False
        url = self.extract_source_url(content)
        if url is None:
            return True
        if 'Kind' not in self.header_fields(content):
            return False
        return url.rstrip('/').rsplit('/', 1)[-1].lower() != name.lower()
    
    def extract_title(self, content: str, file_path: str = "") -> str:
        """
        The page's title: its "# " heading, else its front matter's title, else its first
        heading of any level (a GitHub README can start at "## MLX LM"), never a line of
        code ("# install" in a shell block); else, when file_path is given, its file name,
        so a page is never indexed with an empty title. "" for a page without any of them
        when no file_path is given (extract_api_name then takes the file name its way).
        """
        # Most pages start with their title: no code before it
        title_match = self._title_h1_pattern.search(content)
        if title_match and '```' not in content[:title_match.start()] and '~~~' not in content[:title_match.start()]:
            return title_match.group(1).strip()

        headings = self.headings(content)
        title = next((text for level, text in headings if level == 1), "")
        if title:
            return title
        front_matter_title = self.parse_yaml_frontmatter(content).get("title")
        if isinstance(front_matter_title, str) and front_matter_title.strip():
            return front_matter_title.strip()
        if headings:
            return headings[0][1]
        return Path(file_path).stem if file_path else ""

    def headings(self, content: str) -> List[Tuple[int, str]]:
        """The page's headings outside code blocks, (level, text), in page order."""
        headings: List[Tuple[int, str]] = []
        fence = ""  # the open code block's fence (its character), "" outside one
        for line in content.split('\n'):
            fence_match = self._fence_pattern.match(line)
            if fence_match:
                marker = fence_match.group(1)[0]
                if not fence:
                    fence = marker
                elif marker == fence:
                    fence = ""
                continue
            if fence:
                continue
            heading = self._heading_line_pattern.match(line)
            if heading:
                headings.append((len(heading.group(1)), heading.group(2).strip()))
        return headings

    def extract_platforms(self, content: str) -> List[str]:
        """
        Extract supported platforms: those of the page's **Availability** list when it has
        one (Apple pages), otherwise the platforms its text names.
        """
        listed = self.extract_availability_platforms(content)
        if listed is not None:
            return sorted(listed)

        platforms = set()

        # Look for platform badges or lists using pre-compiled patterns
        for pattern in self._platform_patterns:
            matches = pattern.findall(content)
            for match in matches:
                if isinstance(match, tuple):
                    match = match[0]

                # Parse platform list
                for part in self._platform_split_pattern.split(match):
                    part = part.strip().lower()
                    for key, value in self.platform_mappings.items():
                        if key in part:
                            platforms.add(value)

        # Single-pass scan for platform keywords in content
        for match in self._platform_scan_pattern.finditer(content):
            key = match.group(1).lower()
            if key in self.platform_mappings:
                platforms.add(self.platform_mappings[key])

        return sorted(list(platforms))
    
    def extract_availability_platforms(self, content: str) -> Optional[Set[str]]:
        """
        The platforms of the page's **Availability** list, or None when it has none. A
        listed platform outside platform_mappings (DriverKit, Safari Mobile, Xcode, a web
        service API…) adds none, so a page available only there has no platform.
        """
        block = self._availability_list_pattern.search(content)
        if not block:
            return None
        platforms: Set[str] = set()
        for item in block.group(1).splitlines():
            match = self._availability_item_pattern.match(item.rstrip())
            if match:
                platform = self.platform_mappings.get(match.group('platform').strip().lower())
                if platform:
                    platforms.add(platform)
        return platforms

    def extract_deprecated(self, content: str) -> bool:
        """
        Whether the page is deprecated: it has Apple's deprecation summary ("> **Deprecated**:
        …", before its first section), or every platform of its **Availability** list is
        deprecated (" - Deprecated[ in <version>]"). A page deprecated on some platforms
        only, without a summary, is not.
        """
        if self._deprecation_summary(content):
            return True
        block = self._availability_list_pattern.search(self._head(content))
        if not block:
            return False
        items = [self._availability_item_pattern.match(item.rstrip()) for item in block.group(1).splitlines()]
        return bool(items) and all(match is not None and match.group('deprecated') for match in items)

    def extract_deprecation(self, content: str) -> Optional[str]:
        """The first paragraph of the page's deprecation summary ("Use `b` instead."), on one
        line, or None. The quote's later blocks aren't what to use instead: a code sample, or
        a stray heading of Apple's ("> #### Discussion")."""
        summary = self._deprecation_summary(content)
        if not summary:
            return None
        paragraph: List[str] = []
        for line in summary.group(0).splitlines():
            text = line[1:].strip()
            if not text:
                break
            paragraph.append(text)
        return ' '.join(paragraph)[len('**Deprecated**:'):].strip() or None

    def _head(self, content: str) -> str:
        """The page before its first section (## to ######)."""
        section = self._section_heading_pattern.search(content)
        return content[:section.start()] if section else content

    def _deprecation_summary(self, content: str) -> Optional["re.Match[str]"]:
        """The page's deprecation summary, before its first section."""
        return self._deprecation_summary_pattern.search(self._head(content))

    def header_fields(self, content: str) -> Dict[str, str]:
        """The "**Key**: value" lines right under the page's title (H1), by key"""
        title = self._title_h1_pattern.search(content)
        if not title:
            return {}
        block = self._header_block_pattern.match(content, title.end())
        if not block:
            return {}
        fields: Dict[str, str] = {}
        for line in block.group(1).splitlines():
            match = self._header_line_pattern.match(line)
            if match:
                fields.setdefault(match.group('key').strip(), match.group('value'))
        return fields

    def extract_kind(self, content: str) -> str:
        """
        Extract the kind of API: the page's **Kind** line through kind_mappings (e.g.
        instm -> method, econst -> case), "unknown" for a value it doesn't list. A page
        without one is kinded by its **Role** line through ROLE_KINDS (an API collection,
        sample code), and is an "article" for any other role or none (articles, other
        sources' docs).
        """
        fields = self.header_fields(content)
        kind = fields.get('Kind')
        if kind is None:
            return ROLE_KINDS.get(fields.get('Role', ''), 'article')
        return self.kind_mappings.get(kind.lower(), 'unknown')
    
    def extract_overview(self, content: str) -> str:
        """
        Extract overview or description: the first paragraph of the page's Overview
        (Description, Summary, Introduction) section, otherwise its first paragraph after
        the title, at most 500 characters.
        """
        # The first section whose first paragraph is a summary (section_paragraph)
        for heading in self._overview_heading_pattern.finditer(content):
            overview = self.section_paragraph(content, heading.end())
            if overview:
                return self.cut_overview(overview)

        # Try to get first non-empty paragraph after title, past the header's
        # "**Key**: value" lines (and the list an empty one heads, e.g. **Availability**:)
        # and any quote before the first paragraph: a banner, never the page's summary
        # (Apple's "> **Deprecated**: …", the HIG's "> **Updated …:**", a "> [!IMPORTANT]");
        # a page with no paragraph after it takes the first banner's text (banner_text)
        lines = content.split('\n')
        found_title = False
        overview_lines: List[str] = []
        skip_empty = True
        in_key_list = False
        banner: List[str] = []  # the first quote skipped, unless a deprecation summary
        quote: Optional[List[str]] = None  # the lines of the quote being skipped
        
        for i, line in enumerate(lines):
            # Found title
            if line.startswith('#') and not found_title:
                found_title = True
                continue
            
            # After title, collect non-empty lines
            if found_title:
                line_stripped = line.strip()
                
                # Skip initial empty lines
                if skip_empty and not line_stripped:
                    quote = None
                    continue
                if skip_empty:
                    if line_stripped.startswith('>'):
                        in_key_list = False
                        if quote is None:
                            quote = [] if banner or line_stripped.startswith('> **Deprecated**:') else banner
                        quote.append(line_stripped)
                        continue
                    quote = None
                    key_line = self._header_line_pattern.match(line_stripped)
                    if key_line:
                        in_key_list = not key_line.group('value')
                        continue
                    if in_key_list and line_stripped.startswith('- '):
                        continue
                if line_stripped:
                    skip_empty = False
                
                # Stop at next header, a horizontal rule (the footer's, on a page with
                # no abstract) or after paragraph break
                if line_stripped.startswith('#') or self._rule_pattern.fullmatch(line_stripped):
                    break
                elif not line_stripped and overview_lines:
                    # Paragraph break - we have our overview
                    break
                elif line_stripped:
                    overview_lines.append(line_stripped)
        
        # A paragraph without a letter or digit (a stray "**" or "}") is no summary
        overview = ' '.join(overview_lines)
        if self._word_pattern.search(overview):
            return self.cut_overview(overview)
        overview = self.banner_text(banner)
        if self._word_pattern.search(overview):
            return self.cut_overview(overview)
        
        return ""

    @staticmethod
    def banner_text(quote: List[str]) -> str:
        """A banner quote's first paragraph as a summary, without its markup: the "> "
        markers, an admonition's "[!IMPORTANT]" line and a leading bold label
        ("**Updated 2025-12-16:**", "**Note**:")."""
        paragraph: List[str] = []
        for line in quote:
            text = re.sub(r'^(?:>\s?)+', '', line).strip()
            if not text:
                if paragraph:
                    break
                continue
            if not paragraph and re.fullmatch(r'\[![A-Za-z]+\]', text):
                continue
            paragraph.append(text)
        return re.sub(r'^\*\*[^*]*?(?::\*\*|\*\*:)\s*', '', ' '.join(paragraph))

    def cut_overview(self, overview: str) -> str:
        """An overview cut to OVERVIEW_MAX_CHARS, before a link the cut would fall in: half a
        link is neither a link nor text (259 overviews ended in one)."""
        if len(overview) <= OVERVIEW_MAX_CHARS:
            return overview
        cut = OVERVIEW_MAX_CHARS
        for link in self._markdown_link_pattern.finditer(overview):
            if link.start() < cut < link.end():
                cut = link.start()
                break
        return overview[:cut].rstrip()
    
    def section_paragraph(self, content: str, start: int) -> str:
        """
        The first paragraph of the section that starts at start (a heading line's end),
        past horizontal rules (Apple puts one before some abstracts), whitespace collapsed.
        "" when the section has none before the next heading or the footer, or when it is no
        summary: a lone "**Label**:" line (one that heads a code block, e.g. **Request**: or
        **Swift**:), or without a letter or digit (a stray "}").
        """
        lines: List[str] = []
        for line in content[start:].split('\n'):
            line_stripped = line.strip()
            if line_stripped.startswith('#') or self._footer_pattern.match(line_stripped):
                break
            if not line_stripped or self._rule_pattern.fullmatch(line_stripped):
                if lines:
                    break
                continue
            lines.append(line_stripped)
        paragraph = self._whitespace_pattern.sub(' ', ' '.join(lines))
        label = self._header_line_pattern.match(paragraph)
        if (label and not label.group('value')) or not self._word_pattern.search(paragraph):
            return ""
        return paragraph

    def is_framework_main_page(self, content: str, file_path: str) -> bool:
        """Check if this is a framework's main page."""
        path = Path(file_path)

        # Check if it's an index file
        if path.stem.lower() in ['index', 'readme', 'overview']:
            return True

        # Check if file name matches framework name
        if path.parent.name == "documentation" and path.stem == path.parent.parent.name:
            return True

        # Check content for framework-level indicators using pre-compiled patterns
        for pattern in self._framework_indicator_patterns:
            if pattern.search(content):
                return True

        return False
    
    def get_file_modified_time(self, file_path: str) -> str:
        """Get file modification time."""
        try:
            if os.path.exists(file_path):
                mtime = os.path.getmtime(file_path)
                return datetime.fromtimestamp(mtime).isoformat()
        except OSError:
            pass
        return datetime.now().isoformat()
    
    def extract_source_url(self, content: str) -> Optional[str]:
        """
        The URL in the footer every DocC page ends with (*[View on Apple Developer](<url>)*,
        or the name of the page's own DocC site): the page's own URL, as it was scraped
        (its escapes decoded: a DocC page's URL holds no "%" of its own, and the footer
        encodes an unclosed "(" as %28). None for a page without one.
        """
        last_line = content[-4096:].rstrip().rsplit('\n', 1)[-1].strip()
        match = self._footer_pattern.match(last_line)
        return unquote(match.group(1)) if match else None

    def generate_url(self, file_path: str) -> str:
        """
        Generate Apple Developer documentation URL from file path: only for a page with
        neither a front-matter url nor the footer, since file names are sanitized (e.g.
        init-frame.md for init(frame:)) and the URL would be a 404 for half of the pages.
        """
        path = Path(file_path)
        
        # Extract path components
        parts = list(path.parts)
        
        # Find documentation index
        if "documentation" in parts:
            idx = parts.index("documentation")
            url_parts = parts[idx+1:]
        else:
            url_parts = parts[-2:] if len(parts) > 1 else parts
        
        # Remove .md extension
        if url_parts and url_parts[-1].endswith('.md'):
            url_parts[-1] = url_parts[-1][:-3]
        
        # Build URL
        url_path = "/".join(url_parts).lower()
        return f"https://developer.apple.com/documentation/{url_path}"

def main():
    """CLI for testing metadata extraction."""
    parser = argparse.ArgumentParser(description="Extract metadata from Apple documentation")
    parser.add_argument("file_path", help="Path to markdown file")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--debug", action="store_true", help="Show debug information")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file_path):
        print(f"Error: File not found: {args.file_path}")
        return 1
    
    extractor = MetadataExtractor()
    
    try:
        with open(args.file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata = extractor.extract_metadata(content, args.file_path)
        
        if args.json:
            print(json.dumps(metadata, indent=2))
        else:
            print(f"Metadata for: {args.file_path}\n")
            for key, value in metadata.items():
                if isinstance(value, list):
                    print(f"{key:20s}: {', '.join(value)}")
                else:
                    print(f"{key:20s}: {value}")
        
        return 0
        
    except Exception as e:
        print(f"Error processing file: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit(main())