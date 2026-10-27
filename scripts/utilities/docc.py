"""
DocC catalog markup in the markdown files of a DocC catalog (a *.docc dir).

Shared by the scrapers that take a catalog's articles as they are on GitHub
(Swift: swift-book's TSPL.docc; MLX: the MLX Swift Documentation.docc
catalogs). The rules are DocC's, the same for every catalog:

- <doc:Name> finds its target by name anywhere in the page's own catalog
  (never in another one), <doc:Name#Anchor> a heading of that target, and
  <doc:#Anchor> a heading of the page itself;
- an image named by its bare asset name (![alt](name)) is the catalog's asset;
- @Metadata and @Comment blocks hold no page text.

Also two markdown rules of the scrapers that write their own markdown: HTML
comments hold no page text (strip_html_comments: the Swift and MLX
scrapers' GitHub files, in a catalog or not), and emphasis keeps its
markers against its text (emphasis: the MLX scraper's HTML, the HIG's).

Dependency-free: each scraper says where a catalog's articles are on disk
(catalog_articles) and where its assets are on GitHub (DocCPage.assets_url).
"""

import os
import re
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

# A <doc:Name>, <doc:Name#Anchor> or <doc:#Anchor> link
DOC_LINK_PATTERN = re.compile(r'<doc:([^>]+)>')
# An image named by its bare asset name (no path, no extension)
ASSET_IMAGE_PATTERN = re.compile(r'!\[([^\]]*)\]\(([^)\s/:.#?]+)\)')
# Directive blocks that hold no page text
METADATA_PATTERN = re.compile(r'@Metadata\s*\{[^}]*\}', re.DOTALL)
COMMENT_PATTERN = re.compile(r'@Comment\s*\{[^}]*\}', re.DOTALL)
HEADING_PATTERN = re.compile(r'(#{1,6})\s+(.+?)(?:\s+#+)?\s*$')
# A fenced code block's fence line: the fence (``` or ~~~, 3 or more) and the rest of the line
FENCE_PATTERN = re.compile(r'[ \t]*(`{3,}|~{3,})(.*)')
CODE_SPAN_PATTERN = re.compile(r'(`+).+?\1')
# A line's blockquote markers ("> ", "> > ")
QUOTE_MARKERS_PATTERN = re.compile(r'^(?:[ ]{0,3}>[ ]?)+')

Headings = List[Tuple[int, str]]


@dataclass
class DocCPage:
    """A page of a DocC catalog: where its <doc:> links and asset images point."""
    path: Path  # the page's output file
    targets: Dict[str, Path]  # {article name: its output file} over the page's catalog
    assets_url: str  # the raw URL of the catalog's Assets dir
    _headings: Dict[Path, Headings] = field(default_factory=dict)

    def headings(self, path: Path) -> Headings:
        """A target's headings, (level, text), read once per page."""
        if path not in self._headings:
            self._headings[path] = page_headings(path.read_text(encoding='utf-8'))
        return self._headings[path]


def docc_catalog(repo_path: str) -> Optional[str]:
    """The DocC catalog a repo path is in: the path through its first *.docc
    part (None outside a catalog)."""
    parts = PurePosixPath(repo_path).parts
    for index, part in enumerate(parts):
        if part.endswith('.docc'):
            return '/'.join(parts[:index + 1])
    return None


def catalog_articles(directories: Iterable[Path]) -> Dict[str, Path]:
    """A catalog's articles as they are on disk now, {name: file}: the .md
    files under its output dirs (in the order given, sorted within each; the
    first file with a name wins)."""
    articles: Dict[str, Path] = {}
    for directory in directories:
        if directory.is_dir():
            for path in sorted(directory.rglob("*.md")):
                if path.is_file():
                    articles.setdefault(path.stem, path)
    return articles


def page_headings(markdown: str) -> Headings:
    """A markdown page's headings, (level, text), outside code blocks."""
    headings: Headings = []
    fence: Optional[str] = None
    for line in markdown.split('\n'):
        stripped = line.lstrip()
        if stripped.startswith(('```', '~~~')):
            if fence is None:
                fence = stripped[:3]
            elif stripped.startswith(fence):
                fence = None
            continue
        if fence is None:
            match = HEADING_PATTERN.match(line)
            if match:
                headings.append((len(match.group(1)), match.group(2)))
    return headings


def docc_fragment(heading: str) -> str:
    """A heading's anchor as DocC writes it: its words (split at runs of
    whitespace and dashes) joined by '-', without quotes and backticks."""
    words = [word for word in re.split(r'[\s\-–—]+', heading.strip()) if word]
    return re.sub(r'[\'"`]', '', '-'.join(words))


def doc_link(target: str, docc: Optional[DocCPage], headings: Sequence[Tuple[int, str]] = ()) -> str:
    """A <doc:Name>, <doc:Name#Anchor> or <doc:#Anchor> link as a markdown link.

    <doc:#Anchor> is a heading of the page itself (headings: the page's
    own), linked as #Anchor under that heading's text. In a DocC catalog,
    the target found by name (DocCPage.targets) is linked relative to the
    page, under the title of its file (its "# " heading) or, with an anchor,
    the heading the anchor names. A target with no file yet (or outside a
    catalog) is linked as Name.md in the page's own dir, under a text made
    from its name or anchor.
    """
    doc, _, anchor = target.partition('#')
    suffix = f"#{anchor}" if anchor else ""
    # Humanized: "Nested-Functions" -> "Nested Functions", "ClassesAndStructures" -> "Classes And Structures"
    text = anchor.replace('-', ' ') if anchor else re.sub(r'([a-z])([A-Z])', r'\1 \2', doc)
    if not doc:
        named = [heading for _, heading in headings if docc_fragment(heading) == anchor]
        return f'[{named[0] if named else text}]({suffix})'
    href = f"{doc}.md{suffix}"
    path = docc.targets.get(doc) if docc is not None else None
    if docc is not None and path is not None:
        href = Path(os.path.relpath(path, docc.path.parent)).as_posix() + suffix
        target_headings = docc.headings(path)
        if anchor:
            named = [heading for _, heading in target_headings if docc_fragment(heading) == anchor]
        else:
            named = [heading for level, heading in target_headings if level == 1]
        if named:
            text = named[0]
    return f'[{text}]({href})'


def convert_docc(content: str, docc: Optional[DocCPage]) -> str:
    """A DocC page's markup as markdown: <doc:> links (doc_link), in a
    catalog (docc) its asset images as the asset's URL, and its @Metadata
    and @Comment blocks removed."""
    content = METADATA_PATTERN.sub('', content)
    headings = page_headings(content)
    content = DOC_LINK_PATTERN.sub(lambda match: doc_link(match.group(1), docc, headings), content)
    # An image named by its bare asset name (no path, no extension) is in the
    # catalog's Assets dir: its light, 2x file
    if docc is not None:
        content = ASSET_IMAGE_PATTERN.sub(
            lambda match: f"![{match.group(1)}]({docc.assets_url}/{match.group(2)}@2x.png)", content)
    return COMMENT_PATTERN.sub('', content)


def strip_html_comments(text: str) -> str:
    """text without its HTML comments (<!-- ... -->, on one line or across
    several): a source's notes to its editors, its test code, its licence
    footer, which neither DocC nor GitHub shows.

    The comments are CommonMark's: one that starts its line (an HTML block)
    runs to its "-->" or the end of the text; one inside a line is a comment
    only when its "-->" comes before its paragraph ends (a blank line), and
    text otherwise ("Write <!-- to start one" stays). Code is kept as it is:
    a fenced code block (in a quote too), an indented one (4 columns after a
    blank line) and a code span; a fence inside a comment is the comment's.
    A line the removal leaves blank goes; a comment that starts its line ends
    a markdown paragraph, so where one stood between two lines of text a
    blank line keeps them apart, and where it stood between two blank lines
    one of them goes."""
    source = text.split('\n')
    lines: List[str] = []
    fence: Optional[str] = None  # the open code block's fence
    indented = False  # in an indented code block
    in_comment = False
    block = False  # the open comment started its line
    removed = False  # a comment that started its line was removed since the last line kept

    def keep(line: str) -> None:
        nonlocal removed
        if removed and lines:
            if line.strip() and lines[-1].strip():
                lines.append('')
            elif not line.strip() and not lines[-1].strip():
                return
        removed = False
        lines.append(line)

    def closes_in_paragraph(index: int) -> bool:
        """Whether a "-->" comes on the lines from index before the paragraph ends."""
        for line in source[index:]:
            if not line.strip():
                return False
            if '-->' in line:
                return True
        return False

    for index, line in enumerate(source):
        if in_comment:
            end = line.find('-->')
            removed = removed or block
            if end < 0:
                continue
            in_comment = False
            line = line[end + 3:]
            if not line.strip():
                continue
        else:
            # A fence line, in a quote or not
            fence_line = FENCE_PATTERN.fullmatch(QUOTE_MARKERS_PATTERN.sub('', line, count=1))
            if fence is not None:
                # Closed by a fence of its own character, at least as long, alone on its line
                if fence_line is not None and fence_line.group(1).startswith(fence) and not fence_line.group(2).strip():
                    fence = None
                keep(line)
                continue
            # Opened by a fence (a ``` fence's info string holds no backtick)
            if fence_line is not None and not (fence_line.group(1)[0] == '`' and '`' in fence_line.group(2)):
                fence = fence_line.group(1)
                keep(line)
                continue
            # Indented code: indented 4 columns, after a blank line or in the block
            if line.strip():
                expanded = line.expandtabs(4)
                indented = len(expanded) - len(expanded.lstrip()) >= 4 and (
                    indented or not lines or not lines[-1].strip())
            if indented:
                keep(line)
                continue
        if '<!--' not in line:
            keep(line)
            continue
        # Prose: its comments outside code spans removed; the last may run on past the line
        spans = {span.start(): span.end() for span in CODE_SPAN_PATTERN.finditer(line)}
        pieces: List[str] = []
        position = 0
        while position < len(line):
            if position in spans:
                pieces.append(line[position:spans[position]])
                position = spans[position]
            elif line.startswith('<!--', position):
                starts_line = not ''.join(pieces).strip()
                end = line.find('-->', position + 4)
                if end >= 0:
                    block = starts_line
                    position = end + 3
                elif starts_line or closes_in_paragraph(index + 1):
                    block = starts_line
                    in_comment = True
                    break
                else:
                    pieces.append('<!--')
                    position += 4
            else:
                pieces.append(line[position])
                position += 1
        prose = ''.join(pieces)
        if prose == line:
            keep(line)
        elif prose.strip():
            keep(prose.rstrip())
        else:
            removed = removed or block
    return '\n'.join(lines)


def emphasis(text: str, marker: str) -> str:
    """text emphasized with marker ('**' or '*'), its leading and trailing
    whitespace outside the markers: CommonMark reads markers with a space on
    their inner side as text ('**(i) Privacy Policies: **All' shows its
    asterisks). Text without a letter or digit (Sphinx emphasizes each
    punctuation token of a parameter's type, '(' and ', ') is no emphasis:
    it stays as it is, where markers would run into their neighbours'."""
    core = text.strip()
    if not re.search(r'\w', core):
        return text
    return f"{text[:len(text) - len(text.lstrip())]}{marker}{core}{marker}{text[len(text.rstrip()):]}"
