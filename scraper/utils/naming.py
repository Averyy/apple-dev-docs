"""File and folder names of Apple documentation pages.

seg_name is the single naming function, for folders and files alike (so a
page's folder always has its file's stem): the Apple scraper's
_get_organized_file_path, local links, the filename migration
(scripts/utilities/migrate_filenames.py) and the write-time tripwire all name
pages through it. page_path is the whole path rule. Both are pure functions
of the URL, so a link target is known without the page's data.

Its output alphabet is [a-z0-9._(),-]: legal on Windows except for the
reserved device names, and never a hidden file.
"""

import hashlib
import re
from pathlib import Path
from typing import Dict, Final, Match, Optional, Set

from scraper.utils.hash_manager import read_hash_file
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

# Apple's documentation pages, and their JSON (the hash files' keys)
DOC_URL_PREFIX: Final = "https://developer.apple.com/documentation/"
JSON_URL_PREFIX: Final = "https://developer.apple.com/tutorials/data/documentation/"
HASH_FILE_SUFFIX: Final = "_hashes.json"

# The longest segment, in UTF-8 bytes with ".md". It leaves room under the
# 255-byte NAME_MAX for the tripwire's "-<8 hex>" and an atomic write's ".tmp"
SEGMENT_MAX: Final = 230
# A segment over the cap keeps this many bytes, then "-<8 hex>"
SEGMENT_KEPT: Final = 218

# A page named like its framework (XCTest/XCTest) gets this suffix, in the
# folder position too, so it never shares a name with the framework's root
# page <Dir>/<Dir>.md in any casing
FRAMEWORK_NAMED_SUFFIX: Final = "-page"

_ARGUMENT_LIST: Final = re.compile(r'\(([^()]*)\)')
_LABELS: Final = re.compile(r'(?:[^():,]*:)*')
# An operator's characters, before its "(": each spelled out
_OPERATOR_CHARS: Final = {
    '=': 'eq', '!': 'not', '+': 'plus', '-': 'minus', '*': 'star', '&': 'amp',
    '.': 'dot', '~': 'tilde', '_': 'op',
}
# The other special characters anywhere in a segment ("'" is dropped)
_SPECIAL_CHARS: Final = {
    ':': '_', '*': 'star', '=': 'eq', '!': 'not', '+': 'plus', '&': 'amp',
    '~': 'tilde', '$': 'dollar', '@': 'at', "'": '',
}
_WHITESPACE: Final = re.compile(r'\s+')
_OUTSIDE_ALPHABET: Final = re.compile(r'[^a-z0-9._(),-]')

# The characters outside the alphabet already logged (once each per process)
_warned_chars: Set[str] = set()


def _labels(match: Match[str]) -> str:
    """An argument list "(a:b:)" as "(a,b)"; one that isn't only labels stays as it is."""
    inner = match.group(1)
    if _LABELS.fullmatch(inner):
        return '(' + ','.join(inner.split(':')[:-1]) + ')'
    return match.group(0)


def _outside_alphabet(match: Match[str]) -> str:
    char = match.group(0)
    if char not in _warned_chars:
        _warned_chars.add(char)
        logger.warning("seg_name_unmapped_char", char=char, codepoint=f"U+{ord(char):04X}")
    return '_'


def seg_name(segment: str) -> str:
    """The file or folder name of one URL path segment (without ".md").

    1. Lowercase; drop one leading "'" (Apple's escape of a segment that
       starts with ".").
    2. An argument list "(a:b:)" becomes "(a,b)"; "()" stays. A list that
       isn't only labels ending in ":" is kept verbatim.
    3. When everything before the first "(" is operator characters
       (=!+-*&.~_), each is spelled out: "==(_:_:)" -> "eqeq(_,_)".
    4. The other special characters: ":" -> "_", "*" star, "=" eq, "!" not,
       "+" plus, "&" amp, "~" tilde, "$" dollar, "@" at; "'" is dropped.
    5. Closure: whitespace runs -> "-"; any other character outside
       [a-z0-9._(),-] -> "_" (logged once per character); "-" stripped at
       both ends, then "." at the end; a leading "." -> "dot"; empty ->
       "unnamed".
    6. "api-" before a leading digit.
    7. Cap: a name over SEGMENT_MAX bytes with ".md" keeps its first
       SEGMENT_KEPT characters, then "-" and 8 hex digits of the raw
       segment's sha256 (after the closure the name is ASCII).

    Examples: "setNeedsDisplay(_:)" -> "setneedsdisplay(_)",
    "init(_:count:)" -> "init(_,count)", "'...(_:_:)" -> "dotdotdot(_,_)",
    "3180904-merge" -> "api-3180904-merge", "$state" -> "dollarstate",
    "Editor Integration" -> "editor-integration".
    """
    name = segment.lower()
    if name.startswith("'"):
        name = name[1:]
    name = _ARGUMENT_LIST.sub(_labels, name)
    if '(' in name:
        head, paren, tail = name.partition('(')
        if head and all(char in _OPERATOR_CHARS for char in head):
            name = ''.join(_OPERATOR_CHARS[char] for char in head) + paren + tail
    name = ''.join(_SPECIAL_CHARS.get(char, char) for char in name)
    name = _WHITESPACE.sub('-', name)
    name = _OUTSIDE_ALPHABET.sub(_outside_alphabet, name)
    name = name.strip('-').rstrip('.')
    if name.startswith('.'):
        name = 'dot' + name[1:]
    if not name:
        name = 'unnamed'
    if name[0].isdigit():
        name = f'api-{name}'
    if len(name.encode('utf-8')) + len('.md') > SEGMENT_MAX:
        digest = hashlib.sha256(segment.encode('utf-8')).hexdigest()[:8]
        name = f'{name[:SEGMENT_KEPT]}-{digest}'
    return name


def page_path(dir_name: str, doc_url: str) -> Optional[str]:
    """A documentation page's file, relative to the docs root: "<Dir>/….md".

    <Dir>/ and the seg_name of each URL segment after the framework, with
    ".md" on the last. The root page is <Dir>/<Dir>.md. A page whose first
    segment is named like the framework gets FRAMEWORK_NAMED_SUFFIX in both
    the file and the folder position (XCTest/XCTest -> XCTest/xctest-page.md,
    its children under XCTest/xctest-page/), so a folder name always equals
    its file's stem.

    Args:
        dir_name: The framework's docs dir (its id, in the dir's casing)
        doc_url: The page's URL, https://developer.apple.com/documentation/…
            (the framework segment in any casing)

    Returns:
        The path, or None for a URL that isn't the framework's
    """
    prefix = (DOC_URL_PREFIX + dir_name).lower()
    if doc_url[:len(prefix)].lower() != prefix:
        return None
    rest = doc_url[len(prefix):]
    if rest and not rest.startswith('/'):
        return None
    rest = rest.lstrip('/')
    if not rest:
        return f'{dir_name}/{dir_name}.md'
    names = [seg_name(segment) for segment in rest.split('/')]
    if names[0] == dir_name.lower():
        names[0] += FRAMEWORK_NAMED_SUFFIX
    return f"{dir_name}/{'/'.join(names)}.md"


def clash_suffix(json_url: str) -> str:
    """What the write-time tripwire appends to the stem of a page whose file name another page's file has.

    "-" and 8 hex digits of the sha256 of the page's lowercased JSON URL
    (its identity): stable run to run, and unique to the page.
    """
    return '-' + hashlib.sha256(json_url.lower().encode('utf-8')).hexdigest()[:8]


def dirmap(hash_dir: Path) -> Dict[str, str]:
    """The Apple framework docs dirs: {name.lower(): name}.

    Over the hash files in hash_dir with a key under JSON_URL_PREFIX, where
    name is the file name minus "_hashes.json": the framework's docs dir, in
    the same casing (the HIG, Swift and MLX hash files have no such key). A
    hash file that can't be read is left out (logged).
    """
    dirs: Dict[str, str] = {}
    for path in sorted(hash_dir.glob(f'*{HASH_FILE_SUFFIX}')):
        try:
            hashes, _ = read_hash_file(path)
        except (OSError, ValueError) as e:
            logger.warning("dirmap_hash_file_unreadable", file=str(path), error=str(e))
            continue
        if not any(url.startswith(JSON_URL_PREFIX) for url in hashes):
            continue
        name = path.name[:-len(HASH_FILE_SUFFIX)]
        if name.lower() in dirs:
            logger.warning("dirmap_ambiguous", names=sorted([dirs[name.lower()], name]))
        dirs[name.lower()] = name
    return dirs
