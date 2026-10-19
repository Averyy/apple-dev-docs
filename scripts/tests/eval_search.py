#!/usr/bin/env python3
"""
Golden-query search eval: scores search_apple_docs by hit@3 and MRR, and
expand_result's symbol lookups by how many return an expected page.

Runs on the host against the local compose stack
(mcp-server/docker-compose.local.yml serves http://localhost:8001/mcp, and its
MCP_API_KEY=test123 skips the rate limit). It can't run in the container:
.dockerignore drops **/tests/, and the image carries no .hashes.

    python scripts/tests/eval_search.py [--url URL] [--api-key KEY] [--save FILE]

Each entry of mcp-server/tests/golden_queries.json is
    {"query": str, "framework"?: str, "platform"?: str,
     "expected_top3": [canonical_url, ...], "expand"?: bool}
with 1-3 canonical URLs, any of which is a right answer. Expectations are keyed
by canonical URL rather than file path, so they survive path changes:

- An Apple documentation URL (https://developer.apple.com/documentation/...)
  resolves, case-insensitively, through the doc-URL keys of the repo's .hashes
  to the file the scraper wrote for it, whose footer must name that URL. A hit
  matches when its `Path:` line names that file (case-insensitively).
- Any other URL (HIG, Swift-Book, MLX, coremltools...) is a doc's front-matter
  url, which the index stores as the hit's url field. A hit matches when its
  link line carries exactly that URL.

An expectation that resolves to no doc stops the run, so a stale entry can
never pass as a ranking miss.

Each query is searched with summary_mode on and RESULT_LIMIT results. Its rank
is that of the first result matching any expected URL: hit@3 counts ranks 1-3,
and MRR averages 1/rank (0 when no result matches). Every result must carry a
Path line and a link line to an absolute http(s) URL.

An entry with "expand": true (a symbol name, with no platform) is also looked
up with expand_result(file_path=<query>, framework=<framework>), which picks
its page through its own candidate search, not search_apple_docs' ranking. The
page it returns is named by its canonical URL (an Apple page's footer, another
doc's front-matter url) and must be an expected one; expand@1 is the share of
lookups that return one ("Symbol ... not found" counts as a miss). A page too
long for one response comes in parts, and when the first reply doesn't reach
its last part, which ends with the footer, that part is fetched too
(expand_result with its path and part).

Exit status: 0 when every query was scored (and --save wrote its file); 1,
with an ERROR line naming the cause, when the golden file is invalid, the
repo's .hashes or docs can't be read, an expectation doesn't resolve, the
server can't be reached or answers with an error, or a response can't be
parsed (nothing is scored then), or when --save can't write its file (after
the report).
"""

import argparse
import json
import logging
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple

import httpx

REPO_ROOT = Path(__file__).resolve().parents[2]
# Imported top-level, as scripts/tests/test_metadata_extractor.py does: a
# `scripts.` import would resolve to mcp-server/scripts when that package comes
# first on sys.path (a pytest run that collects mcp-server/tests first)
sys.path.append(str(REPO_ROOT / "scripts"))
# The indexer's own front-matter parser, so a non-Apple expectation is checked
# against exactly the url the index stores
from metadata_extractor import MetadataExtractor  # noqa: E402

logger = logging.getLogger(__name__)

GOLDEN_FILE = Path("mcp-server") / "tests" / "golden_queries.json"
DEFAULT_URL = "http://localhost:8001/mcp"
DEFAULT_API_KEY = "test123"  # MCP_API_KEY in mcp-server/docker-compose.local.yml
APPLE_DOC_PREFIX = "https://developer.apple.com/documentation/"

TOP_K = 3
RESULT_LIMIT = 10  # the server's default limit; MRR is over these results
TOKEN_BUDGET = 25000  # the server's maximum, so the budget never hides a result
PROTOCOL_VERSION = "2025-06-18"
ENTRY_KEYS = {"query", "framework", "platform", "expected_top3", "expand"}

# search_apple_docs output: a result starts with "## <rank>. <title> (<n>%)"
# followed by "Framework: ... | Type: ...", then the Path and link lines up to
# the first blank line
_HEADER_RE = re.compile(r"^## (\d+)\. (.*)$")
_RELEVANCE_RE = re.compile(r" \(\d+%\)$")
_SHOWING_RE = re.compile(r"^Showing (\d+)-(\d+) of ")
_PATH_RE = re.compile(r"^Path: `([^`]+)`$")
# Link targets must be absolute http(s) URLs: another form (e.g. CommonMark's
# "[label](<url>)" or a relative path) would never equal an expected URL, so it
# is a format change to handle here, not a miss
_LINK_RE = re.compile(r"^\[[^\]]*\]\((https?://\S+)\)$")
RESULTS_PREFIX = "Search Results: "
NO_RESULTS_PREFIX = "No results found for "
# The last line of every Apple page (markdown_converter.py): its canonical URL
_FOOTER_RE = re.compile(r"^\*\[View on Apple Developer\]\((https?://\S+)\)\*$")
# expand_result output for a symbol: the page's content, then "\n\n---\n" and
# its notes, one per line: for a page too long for one response, which of its
# parts the reply holds ("Part <i> of <n> of `<file_path>`..." or "Parts
# <i>-<j> of <n> of `<file_path>`..."), and when the name also matches pages in
# other frameworks, "Note: '<name>' also matches pages in ..."; or "Symbol
# '<name>' not found ..." when nothing matches
_SYMBOL_NOT_FOUND_RE = re.compile(r"^Symbol '.*' not found")
_AMBIGUITY_NOTE_RE = re.compile(r"^Note: '.*' also matches pages in ")
_PART_NOTE_RE = re.compile(r"^Parts? (\d+)(?:-(\d+))? of (\d+) of `([^`]+)`")
# A query an "expand" entry looks up: one word, not a path or wildcard pattern
_SYMBOL_RE = re.compile(r"[^\s/*?]+")
# An event stream's line ends (the SSE spec; sse_starlette splits data on the
# same). Not str.splitlines(): it also breaks at U+2028, U+2029 and U+0085,
# which JSON leaves raw inside a string, so it would cut a data line in two
_SSE_LINE_END_RE = re.compile(r"\r\n|\r|\n")


class EvalError(Exception):
    """The eval can't produce a trustworthy score; the message names the cause."""


@dataclass(frozen=True)
class GoldenQuery:
    query: str
    framework: str
    platform: str
    expected: Tuple[str, ...]
    expand: bool = False  # also look the query up as a symbol with expand_result

    @property
    def label(self) -> str:
        filters = [f"framework={self.framework}"] if self.framework else []
        if self.platform:
            filters.append(f"platform={self.platform}")
        return f"{self.query} [{', '.join(filters)}]" if filters else self.query


@dataclass(frozen=True)
class Hit:
    rank: int
    title: str
    path: str
    url: str


@dataclass(frozen=True)
class Expectation:
    url: str
    paths: FrozenSet[str]  # lowercased doc paths of an Apple URL; empty otherwise

    def matches(self, hit: Hit) -> bool:
        if self.paths:
            return hit.path.lower() in self.paths
        return hit.url == self.url

    def matches_page(self, url: str) -> bool:
        """Whether a page's canonical URL (what expand_result returned) is this one.

        An Apple page's footer URL is the one its expectation resolved through
        (resolve_expectations checks it), compared case-insensitively.
        """
        if self.paths:
            return url.lower() == self.url.lower()
        return url == self.url


@dataclass(frozen=True)
class QueryResult:
    golden: GoldenQuery
    hits: Tuple[Hit, ...]
    rank: Optional[int]
    # expand_result's symbol lookup (golden.expand only): the canonical URL of
    # the page it returned (None when it found no such symbol), and whether
    # that page is an expected one
    expand_page: Optional[str] = None
    expand_hit: bool = False

    @property
    def hit_at_k(self) -> bool:
        return self.rank is not None and self.rank <= TOP_K

    @property
    def reciprocal_rank(self) -> float:
        return 1.0 / self.rank if self.rank else 0.0


def is_apple_doc_url(url: str) -> bool:
    return url.lower().startswith(APPLE_DOC_PREFIX)


def is_symbol_name(query: str) -> bool:
    """A query expand_result looks up as one symbol name, not a path or pattern."""
    return bool(_SYMBOL_RE.fullmatch(query)) and not query.lower().endswith(".md")


def text_lines(text: str) -> List[str]:
    """The lines of a doc or a tool's text, which the scraper and server join with "\\n".

    Not str.splitlines(): it also breaks at U+2028, U+2029, U+0085, form feeds
    and other characters a title, overview or page can hold inside a line.
    """
    return text.split("\n") if text else []


def load_golden(path: Path) -> List[GoldenQuery]:
    """Load and validate the golden queries."""
    try:
        entries = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise EvalError(f"can't read golden queries {path}: {e}") from e
    if not isinstance(entries, list) or not entries:
        raise EvalError(f"{path}: expected a non-empty JSON list of entries")

    queries: List[GoldenQuery] = []
    seen: Set[Tuple[str, str, str]] = set()
    for number, entry in enumerate(entries, 1):
        where = f"{path.name} entry {number}"
        if not isinstance(entry, dict):
            raise EvalError(f"{where}: not a JSON object")
        unknown = sorted(set(entry) - ENTRY_KEYS)
        if unknown:
            raise EvalError(f"{where}: unknown key(s) {', '.join(unknown)}")
        query = entry.get("query")
        if not isinstance(query, str) or not query.strip():
            raise EvalError(f"{where}: 'query' must be a non-empty string")
        where = f"{where} ({query!r})"
        filters = []
        for name in ("framework", "platform"):
            value = entry.get(name, "")
            if not isinstance(value, str) or (name in entry and not value.strip()):
                raise EvalError(f"{where}: '{name}' must be a non-empty string when present")
            filters.append(value.strip())
        expected = entry.get("expected_top3")
        if (not isinstance(expected, list) or not 1 <= len(expected) <= TOP_K
                or not all(isinstance(u, str) and u.startswith(("https://", "http://"))
                           for u in expected)):
            raise EvalError(f"{where}: 'expected_top3' must list 1-{TOP_K} http(s) URLs")
        if len({u.lower() for u in expected}) != len(expected):
            raise EvalError(f"{where}: 'expected_top3' repeats a URL")
        expand = entry.get("expand", False)
        if not isinstance(expand, bool):
            raise EvalError(f"{where}: 'expand' must be true or false")
        if expand and filters[1]:
            raise EvalError(f"{where}: 'expand' takes no platform (expand_result has no "
                            "platform filter)")
        if expand and not is_symbol_name(query.strip()):
            raise EvalError(f"{where}: 'expand' needs a symbol name (one word, no '/', "
                            "wildcard or .md)")
        key = (query.strip(), filters[0], filters[1])
        if key in seen:
            raise EvalError(f"{where}: duplicate query and filters")
        seen.add(key)
        queries.append(GoldenQuery(key[0], key[1], key[2], tuple(expected), expand))
    return queries


def load_doc_url_index(hashes_dir: Path) -> Dict[str, Set[str]]:
    """Map every lowercased Apple doc-URL key in the hash files to its doc path(s)."""
    extractor = MetadataExtractor()
    index: Dict[str, Set[str]] = {}
    hash_files = sorted(hashes_dir.glob("*.json"))
    if not hash_files:
        raise EvalError(f"no hash files in {hashes_dir}")
    for hash_file in hash_files:
        try:
            data = json.loads(hash_file.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            raise EvalError(f"can't read {hash_file}: {e}") from e
        entries = data.get("hashes", data) if isinstance(data, dict) else None
        if not isinstance(entries, dict):
            continue
        for url, entry in entries.items():
            # Only Apple scraper entries carry a doc-URL key; JSON-URL keys,
            # error entries and bare digests (Swift/MLX) have no doc path here
            if not (is_apple_doc_url(url) and isinstance(entry, dict)
                    and entry.get("file_path")):
                continue
            path = extractor.normalize_file_path(entry["file_path"])
            index.setdefault(url.lower(), set()).add(path)
    return index


def load_front_matter_urls(docs_dir: Path, skip_dirs: Set[str]) -> Set[str]:
    """Every front-matter url of a doc under docs_dir.

    Top-level dirs in skip_dirs (lowercased; the Apple framework dirs) are not
    scanned: their docs are resolved through the hash files.
    """
    extractor = MetadataExtractor()
    urls: Set[str] = set()
    try:
        for top in sorted(docs_dir.iterdir()):
            if not top.is_dir() or top.name.lower() in skip_dirs:
                continue
            for md in sorted(top.rglob("*.md")):
                content = md.read_text(encoding="utf-8", errors="replace")
                url = extractor.parse_yaml_frontmatter(content).get("url")
                if isinstance(url, str) and url:
                    urls.add(url)
    except OSError as e:
        # A missing docs dir or an unreadable doc (the error names it)
        raise EvalError(f"can't read the docs under {docs_dir}: {e}") from e
    return urls


def is_doc_file(path: Path) -> bool:
    """Whether a doc exists at path; an error other than its absence raises EvalError."""
    try:
        return path.is_file()
    except OSError as e:
        raise EvalError(f"can't read {path}: {e}") from e


def footer_url(path: Path) -> Optional[str]:
    """The canonical URL in an Apple page's footer, or None if it has none."""
    try:
        with path.open("rb") as f:
            f.seek(max(0, path.stat().st_size - 2048))
            tail = f.read().decode("utf-8", errors="replace")
    except OSError as e:
        raise EvalError(f"can't read {path}: {e}") from e
    lines = [line.strip() for line in text_lines(tail) if line.strip()]
    match = _FOOTER_RE.match(lines[-1]) if lines else None
    return match.group(1) if match else None


def resolve_expectations(
    queries: Sequence[GoldenQuery], repo_root: Path
) -> List[Tuple[Expectation, ...]]:
    """Resolve each query's expected URLs against the repo's .hashes and docs."""
    doc_index = load_doc_url_index(repo_root / ".hashes")
    logger.info(f"Loaded {len(doc_index):,} Apple doc URLs from {repo_root / '.hashes'}")
    docs_dir = repo_root / "documentation"
    front_matter: Set[str] = set()
    if any(not is_apple_doc_url(u) for q in queries for u in q.expected):
        apple_dirs = {p.split("/")[1].lower() for paths in doc_index.values()
                      for p in paths if p.count("/") >= 2}
        front_matter = load_front_matter_urls(docs_dir, apple_dirs)

    resolved: List[Tuple[Expectation, ...]] = []
    problems: List[str] = []
    for query in queries:
        expectations = []
        for url in query.expected:
            if is_apple_doc_url(url):
                paths = doc_index.get(url.lower(), set())
                if not paths:
                    problems.append(f"{query.query!r}: {url} is not a doc-URL key in .hashes")
                    continue
                missing = [p for p in sorted(paths) if not is_doc_file(repo_root / p)]
                if missing:
                    problems.append(f"{query.query!r}: {url} resolves to "
                                    f"{', '.join(missing)}, which doesn't exist")
                    continue
                # A file several pages map to (case collisions) holds only the
                # page its footer names; the others would match the wrong page
                other = [f"{p} (footer: {footer})" for p in sorted(paths)
                         if (footer := footer_url(repo_root / p)) is None
                         or footer.lower() != url.lower()]
                if other:
                    problems.append(f"{query.query!r}: {url} resolves to "
                                    f"{', '.join(other)}, which holds another page")
                    continue
                expectations.append(Expectation(url, frozenset(p.lower() for p in paths)))
            elif url in front_matter:
                expectations.append(Expectation(url, frozenset()))
            else:
                problems.append(f"{query.query!r}: {url} is no doc's front-matter url "
                                f"under {docs_dir}")
        resolved.append(tuple(expectations))
    if problems:
        raise EvalError("unresolved expectations:\n  " + "\n  ".join(problems))
    return resolved


def parse_search_results(text: str) -> List[Hit]:
    """Parse search_apple_docs output into its ranked hits.

    A no-results answer gives []. Anything that isn't a well-formed result
    list raises EvalError rather than scoring as a miss.
    """
    lines = text_lines(text)
    if not lines:
        raise EvalError("empty search response")
    if lines[0].startswith(NO_RESULTS_PREFIX):
        return []
    if not lines[0].startswith(RESULTS_PREFIX):
        raise EvalError(f"unrecognized search response, starting {lines[0][:120]!r}")
    showing = _SHOWING_RE.match(lines[1]) if len(lines) > 1 else None
    if showing is None:
        raise EvalError("search response has no 'Showing <a>-<b> of ...' line")

    hits: List[Hit] = []
    i = 2
    while i < len(lines):
        header = _HEADER_RE.match(lines[i])
        if not header or i + 1 >= len(lines) or not lines[i + 1].startswith("Framework: "):
            i += 1
            continue
        rank = int(header.group(1))
        title = _RELEVANCE_RE.sub("", header.group(2))
        path: Optional[str] = None
        url: Optional[str] = None
        i += 2
        # The header is exactly one Path line and one link line: a line read as
        # neither would silently drop the url non-Apple expectations match on
        while i < len(lines) and lines[i].strip():
            path_match = _PATH_RE.match(lines[i])
            link_match = _LINK_RE.match(lines[i])
            if path_match and path is None:
                path = path_match.group(1)
            elif link_match and url is None:
                url = link_match.group(1)
            else:
                raise EvalError(f"result {rank} ({title!r}): unexpected header line "
                                f"{lines[i][:120]!r} (expected one 'Path:' line and one "
                                "'[label](http(s) URL)' line)")
            i += 1
        if path is None:
            raise EvalError(f"result {rank} ({title!r}) has no 'Path:' line")
        if url is None:
            raise EvalError(f"result {rank} ({title!r}) has no link line")
        hits.append(Hit(rank, title, path, url))

    first, last = int(showing.group(1)), int(showing.group(2))
    ranks = [hit.rank for hit in hits]
    if ranks != list(range(first, last + 1)):
        raise EvalError(f"parsed result ranks {ranks}, but the response shows {first}-{last}")
    return hits


@dataclass(frozen=True)
class ExpandPart:
    """The parts of a long page an expand_result reply holds: first to last, of total."""
    first: int
    last: int
    total: int
    path: str


def split_expand_notes(text: str) -> Tuple[str, List[str]]:
    """An expand_result reply's content, and the note lines after its final "---"."""
    lines = text_lines(text.rstrip())
    end = len(lines)
    while end > 0 and (_AMBIGUITY_NOTE_RE.match(lines[end - 1]) or _PART_NOTE_RE.match(lines[end - 1])):
        end -= 1
    if 0 < end < len(lines) and lines[end - 1] == "---":
        return "\n".join(lines[:end - 1]).rstrip(), lines[end:]
    return "\n".join(lines).rstrip(), []


def expand_part(text: str) -> Optional[ExpandPart]:
    """Which parts of a long page an expand_result reply holds; None for a whole page."""
    for line in split_expand_notes(text)[1]:
        match = _PART_NOTE_RE.match(line)
        if match:
            first = int(match.group(1))
            return ExpandPart(first, int(match.group(2) or first), int(match.group(3)), match.group(4))
    return None


def parse_expand_result(text: str, last_part: Optional[str] = None) -> Optional[str]:
    """The canonical URL of the page expand_result returned for a symbol.

    An Apple page ends with its footer; any other doc starts with front matter
    whose url the index stores. A page too long for one response comes in
    parts: text is then the reply holding its first, and last_part the reply
    holding its last, which ends with the footer. "Symbol ... not found" gives None. A reply
    that names no page this way raises EvalError rather than scoring as a miss.
    """
    lines = text_lines(text.rstrip())
    if not lines:
        raise EvalError("empty expand_result response")
    first = lines[0]
    if _SYMBOL_NOT_FOUND_RE.match(first):
        return None
    content = split_expand_notes(text)[0]
    end = split_expand_notes(last_part)[0] if last_part is not None else content
    footer = _FOOTER_RE.match(text_lines(end)[-1].strip()) if end else None
    if footer:
        return footer.group(1)
    url = MetadataExtractor().parse_yaml_frontmatter(content).get("url")
    if isinstance(url, str) and url:
        return url
    raise EvalError("expand_result response names no page (no Apple footer or front-matter "
                    f"url), starting {first[:120]!r}")


def first_match_rank(hits: Sequence[Hit], expectations: Sequence[Expectation]) -> Optional[int]:
    for hit in hits:
        if any(expectation.matches(hit) for expectation in expectations):
            return hit.rank
    return None


def summarize(results: Sequence[QueryResult]) -> Tuple[float, float]:
    """Mean hit@TOP_K and MRR over the results."""
    if not results:
        return 0.0, 0.0
    hit_rate = sum(r.hit_at_k for r in results) / len(results)
    mrr = sum(r.reciprocal_rank for r in results) / len(results)
    return hit_rate, mrr


def summarize_expand(results: Sequence[QueryResult]) -> Tuple[int, int]:
    """expand_result lookups that returned an expected page, and lookups made."""
    lookups = [r for r in results if r.golden.expand]
    return sum(r.expand_hit for r in lookups), len(lookups)


class McpClient:
    """Minimal MCP client over Streamable HTTP (JSON-RPC POSTs; JSON or SSE replies)."""

    def __init__(self, url: str, api_key: str = "", timeout: float = 60.0,
                 transport: Optional[httpx.BaseTransport] = None) -> None:
        self.url = url
        self.server_info: Dict[str, Any] = {}
        self._headers = {
            "Accept": "application/json, text/event-stream",
            "Content-Type": "application/json",
        }
        if api_key:
            self._headers["Authorization"] = f"Bearer {api_key}"
        self._next_id = 1
        self._session_id: Optional[str] = None
        self._http = httpx.Client(timeout=timeout, transport=transport)

    def __enter__(self) -> "McpClient":
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        if self._session_id:
            try:
                self._http.delete(self.url, headers=self._headers)
            except httpx.HTTPError:
                pass  # the server drops idle sessions on its own
        self._http.close()

    def initialize(self) -> None:
        result = self._request("initialize", {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {},
            "clientInfo": {"name": "eval-search", "version": "1.0"},
        })
        info = result.get("serverInfo")
        self.server_info = info if isinstance(info, dict) else {}
        version = result.get("protocolVersion")
        if isinstance(version, str) and version:
            self._headers["MCP-Protocol-Version"] = version
        self._notify("notifications/initialized")

    def call_tool(self, name: str, arguments: Dict[str, Any]) -> str:
        """Call a tool and return its text content; a tool error raises EvalError."""
        result = self._request("tools/call", {"name": name, "arguments": arguments})
        content = result.get("content")
        items = content if isinstance(content, list) else []
        texts = [str(item.get("text", "")) for item in items
                 if isinstance(item, dict) and item.get("type") == "text"]
        if result.get("isError"):
            raise EvalError(f"{name} returned an error: {' '.join(texts)[:300]}")
        if not texts:
            raise EvalError(f"{name} returned no text content: {json.dumps(result)[:300]}")
        return "\n".join(texts)

    def _post(self, payload: Dict[str, Any]) -> httpx.Response:
        try:
            response = self._http.post(self.url, json=payload, headers=self._headers)
        except httpx.HTTPError as e:
            raise EvalError(f"can't reach {self.url}: {type(e).__name__}: {e}") from e
        session_id = response.headers.get("mcp-session-id")
        if session_id:
            self._session_id = session_id
            self._headers["Mcp-Session-Id"] = session_id
        return response

    def _notify(self, method: str) -> None:
        response = self._post({"jsonrpc": "2.0", "method": method})
        if not response.is_success:
            raise EvalError(f"HTTP {response.status_code} from {self.url} for {method}: "
                            f"{response.text[:300]}")

    def _request(self, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
        request_id = self._next_id
        self._next_id += 1
        response = self._post({"jsonrpc": "2.0", "id": request_id,
                               "method": method, "params": params})
        if response.status_code != 200:
            raise EvalError(f"HTTP {response.status_code} from {self.url} for {method}: "
                            f"{response.text[:300]}")
        reply = self._find_reply(response, request_id, method)
        error = reply.get("error")
        if error is not None:
            raise EvalError(f"{method} failed: JSON-RPC error {json.dumps(error)[:300]}")
        result = reply.get("result")
        if not isinstance(result, dict):
            raise EvalError(f"{method} reply has no result object: {json.dumps(reply)[:300]}")
        return result

    def _find_reply(self, response: httpx.Response, request_id: int,
                    method: str) -> Dict[str, Any]:
        content_type = response.headers.get("content-type", "")
        try:
            if content_type.startswith("application/json"):
                body = response.json()
                messages = body if isinstance(body, list) else [body]
            elif content_type.startswith("text/event-stream"):
                messages = _sse_messages(response.text)
            else:
                raise EvalError(f"{method}: unexpected Content-Type {content_type!r} "
                                f"from {self.url}")
        except ValueError as e:
            raise EvalError(f"{method}: can't parse the reply from {self.url}: {e}") from e
        for message in messages:
            if isinstance(message, dict) and message.get("id") == request_id:
                return message
        raise EvalError(f"{method}: no JSON-RPC reply to request {request_id} in "
                        f"{response.text[:300]!r}")


def _sse_messages(body: str) -> List[Any]:
    """The JSON payloads of a text/event-stream body's events."""
    messages: List[Any] = []
    data: List[str] = []
    for line in _SSE_LINE_END_RE.split(body) + [""]:
        if line.startswith("data:"):
            data.append(line[5:].removeprefix(" "))
        elif not line and data:
            messages.append(json.loads("\n".join(data)))
            data = []
    return messages


def run_eval(client: McpClient, queries: Sequence[GoldenQuery],
             expectations: Sequence[Tuple[Expectation, ...]],
             delay: float = 0.0) -> List[QueryResult]:
    results: List[QueryResult] = []
    calls = 0

    def call_tool(name: str, arguments: Dict[str, Any]) -> str:
        nonlocal calls
        if delay and calls:
            time.sleep(delay)
        calls += 1
        return client.call_tool(name, arguments)

    for query, expected in zip(queries, expectations, strict=True):
        arguments: Dict[str, Any] = {"query": query.query, "summary_mode": True,
                                     "limit": RESULT_LIMIT, "token_budget": TOKEN_BUDGET}
        if query.framework:
            arguments["framework"] = query.framework
        if query.platform:
            arguments["platform"] = query.platform
        page: Optional[str] = None
        try:
            hits = parse_search_results(call_tool("search_apple_docs", arguments))
            if query.expand:
                # The symbol lookup has its own candidate search (apple_docs_mcp.py
                # expand_result), separate from search_apple_docs' ranking
                expand_arguments: Dict[str, Any] = {"file_path": query.query}
                if query.framework:
                    expand_arguments["framework"] = query.framework
                reply = call_tool("expand_result", expand_arguments)
                part = expand_part(reply)
                last_part: Optional[str] = None
                if part and part.last < part.total:
                    # A long page comes in parts, and an Apple page's footer ends the last
                    last_part = call_tool("expand_result", {"file_path": part.path, "part": part.total})
                page = parse_expand_result(reply, last_part)
        except EvalError as e:
            raise EvalError(f"query {query.label!r}: {e}") from e
        expand_hit = page is not None and any(x.matches_page(page) for x in expected)
        results.append(QueryResult(query, tuple(hits), first_match_rank(hits, expected),
                                   page, expand_hit))
    return results


def format_report(results: Sequence[QueryResult]) -> List[str]:
    lines = []
    for number, result in enumerate(results, 1):
        rank = str(result.rank) if result.rank else "-"
        status = "hit " if result.hit_at_k else "MISS"
        lines.append(f"{number:3d} {status} rank {rank:>2}  RR {result.reciprocal_rank:.3f}  "
                     f"{result.golden.label}")
        if not result.hit_at_k:
            top = [h.path if is_apple_doc_url(h.url) else h.url for h in result.hits[:TOP_K]]
            lines.append(f"      top {TOP_K}: {' | '.join(top) if top else '(no results)'}")
    hit_rate, mrr = summarize(results)
    hits = sum(r.hit_at_k for r in results)
    lines.append("")
    lines.append(f"hit@{TOP_K}:  {hits}/{len(results)} = {hit_rate:.3f}")
    lines.append(f"MRR@{RESULT_LIMIT}: {mrr:.3f}")

    expand_hits, lookups = summarize_expand(results)
    if lookups:
        lines.append("")
        lines.append("expand_result symbol lookups (the page it returns for the query):")
        for number, result in enumerate(results, 1):
            if result.golden.expand:
                status = "hit " if result.expand_hit else "MISS"
                lines.append(f"{number:3d} {status} {result.golden.label} -> "
                             f"{result.expand_page or '(symbol not found)'}")
        lines.append("")
        lines.append(f"expand@1: {expand_hits}/{lookups} = {expand_hits / lookups:.3f}")
    return lines


def results_json(results: Sequence[QueryResult], url: str,
                 server_info: Dict[str, Any]) -> Dict[str, Any]:
    hit_rate, mrr = summarize(results)
    expand_hits, lookups = summarize_expand(results)
    return {
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "server": {"url": url, **server_info},
        "limit": RESULT_LIMIT,
        "queries": len(results),
        f"hit_at_{TOP_K}": round(hit_rate, 4),
        "mrr": round(mrr, 4),
        "expand_lookups": lookups,
        "expand_hit_at_1": round(expand_hits / lookups, 4) if lookups else 0.0,
        "results": [
            {
                "query": r.golden.query,
                "framework": r.golden.framework,
                "platform": r.golden.platform,
                "rank": r.rank,
                f"hit_at_{TOP_K}": r.hit_at_k,
                "reciprocal_rank": round(r.reciprocal_rank, 4),
                "top": [{"path": h.path, "url": h.url} for h in r.hits[:TOP_K]],
                **({"expand": {"page": r.expand_page, "hit": r.expand_hit}}
                   if r.golden.expand else {}),
            }
            for r in results
        ],
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Score search_apple_docs (hit@3, MRR) and expand_result's symbol "
                    "lookups (expand@1) on the golden queries.")
    parser.add_argument("--url", default=DEFAULT_URL,
                        help=f"MCP endpoint (default: local compose, {DEFAULT_URL})")
    parser.add_argument("--api-key", default=DEFAULT_API_KEY,
                        help="Bearer token; '' sends none (default: the local compose key)")
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT,
                        help="repo whose .hashes and documentation/ resolve the expectations")
    parser.add_argument("--golden", type=Path, default=None,
                        help=f"golden queries (default: <repo-root>/{GOLDEN_FILE})")
    parser.add_argument("--delay", type=float, default=0.0,
                        help="seconds between tool calls (searches and expand_result "
                             "lookups), for a rate-limited server")
    parser.add_argument("--timeout", type=float, default=60.0,
                        help="HTTP timeout per request in seconds")
    parser.add_argument("--save", type=Path, default=None,
                        help="also write the scores and per-query results as JSON")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logging.getLogger("httpx").setLevel(logging.WARNING)  # one INFO line per request

    try:
        queries = load_golden(args.golden or args.repo_root / GOLDEN_FILE)
        expectations = resolve_expectations(queries, args.repo_root)
        logger.info(f"Resolved {len(queries)} golden queries "
                    f"({sum(q.expand for q in queries)} with an expand_result lookup)")
        with McpClient(args.url, args.api_key, args.timeout) as client:
            client.initialize()
            logger.info(f"Server: {client.server_info.get('name', '?')} "
                        f"{client.server_info.get('version', '?')} at {args.url}")
            results = run_eval(client, queries, expectations, args.delay)
            server_info = client.server_info
    except EvalError as e:
        logger.error(str(e))
        return 1
    except OSError as e:  # e.g. --repo-root without documentation/, or an unreadable doc
        logger.error(f"can't read the repo's docs or hash files: {e}")
        return 1

    print("\n".join(format_report(results)))
    if args.save:
        try:
            args.save.write_text(
                json.dumps(results_json(results, args.url, server_info), indent=2) + "\n",
                encoding="utf-8")
        except OSError as e:
            logger.error(f"can't save results to {args.save}: {e}")
            return 1
        logger.info(f"Saved results to {args.save}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
