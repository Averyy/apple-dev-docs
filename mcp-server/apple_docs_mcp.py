#!/usr/bin/env python3
"""
Apple Docs MCP Server - Native HTTP Implementation

MCP server for Apple Developer Documentation with Meilisearch backend.
Uses Streamable HTTP transport for stateless operation.

Usage:
    python apple_docs_mcp.py --port 8000

For STDIO clients, use mcp-remote: npx -y mcp-remote https://xdocs.dev/mcp
"""

import os
import sys
import re
import fnmatch
import posixpath
import secrets
import time
import logging
import unicodedata
from collections import defaultdict
from typing import Annotated, Callable, Dict, List, Optional, Any, Tuple, TypeVar
from pathlib import Path
from urllib.parse import unquote, urlsplit

from pydantic import Field

# Load environment variables
from dotenv import load_dotenv
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import meilisearch
try:
    import meilisearch
except ImportError:
    logger.error("meilisearch not installed. Run: pip install meilisearch")
    sys.exit(1)

# Import FastMCP (standalone package) and MCP types
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from mcp.types import ToolAnnotations

# =============================================================================
# CONFIGURATION
# =============================================================================

MEILISEARCH_URL = os.getenv("MEILI_HTTP_ADDR", "http://localhost:7700")
MEILISEARCH_API_KEY = os.getenv("MEILI_SEARCH_KEY", os.getenv("MEILI_MASTER_KEY", ""))
INDEX_NAME = "apple-docs"
SERVER_VERSION = "3.4.0"
HTTP_PORT = int(os.getenv("HTTP_PORT", "8000"))
BUILD_TIME = os.getenv("BUILD_TIME", "unknown")
DOCS_UPDATED = os.getenv("DOCS_UPDATED", "unknown")

# Host header validation (fastmcp 3.x DNS rebinding protection)
# localhost/127.0.0.1/::1 are always allowed; these are additional public hostnames
_DEFAULT_ALLOWED_HOSTS = "xdocs.dev,www.xdocs.dev"
ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", _DEFAULT_ALLOWED_HOSTS).split(",") if h.strip()]
if not ALLOWED_HOSTS:
    # An empty list would 421 all public traffic (localhost-only) — fail safe
    logger.warning("ALLOWED_HOSTS is empty; falling back to defaults %s", _DEFAULT_ALLOWED_HOSTS)
    ALLOWED_HOSTS = [h.strip() for h in _DEFAULT_ALLOWED_HOSTS.split(",")]

# Rate limiting config
MCP_API_KEY = os.getenv("MCP_API_KEY", "")
# Increased from 30 to 60 - Claude Desktop makes rapid tool calls
RATE_LIMIT_REQUESTS = int(os.getenv("RATE_LIMIT_REQUESTS", "60"))

# Token optimization settings
MAX_TOKEN_BUDGET = 25000

# Largest expand_result reply, in estimate_tokens units (~4 characters per token). Claude
# Code's default cap on an MCP tool's output is 25,000 tokens, and code-heavy pages
# tokenize denser than 4 characters per token, so this leaves room under it. A longer
# page comes in parts, its indexed chunks (each at most ~52 KB, ~13K tokens): a reply
# holds as many whole parts as fit under it.
EXPAND_TOKEN_CAP = 20000

# The fields expand_result reads from each document (chunk) of a file. index_gen is the
# indexer run that sent it (scripts/index_to_meilisearch.py: INDEX_GEN_ATTRIBUTE).
EXPAND_FIELDS = ["title", "content", "framework", "kind", "url", "file_path",
                 "chunk_index", "total_chunks", "index_gen"]

# Documents fetched for one file at first (the largest file has ~20 chunks); a file with
# more is fetched again with its total
FILE_CHUNKS_LIMIT = 100

# Display names of the hosts the indexed docs come from; a result link from any other host
# is labelled with the host itself
LINK_HOST_NAMES = {"developer.apple.com": "Apple Developer", "github.com": "GitHub"}

# The docs the index is built from (the image's copy, /data/documentation; outside it, the
# checkout's documentation/ beside mcp-server/): a page's local links are resolved against
# them (transform_internal_links). The image's docs are the ones its start indexes, so until
# that update or rebuild is in, a link can name a page the live index doesn't hold yet
DOCUMENTATION_PATH = os.getenv("DOCUMENTATION_PATH", str(Path(__file__).parent.parent / "documentation"))

# A markdown link to a local page. Its text may hold brackets two levels deep (a Topics
# link to `var locations: [Accessory.LocationName]`); its destination is a .md path,
# percent-encoded or not, and may end with a #fragment
LOCAL_LINK_RE = re.compile(r'\[((?:[^\[\]]|\[(?:[^\[\]]|\[[^\[\]]*\])*\])*)\]\(([^)\s]+?\.md)(#[^)\s]*)?\)')
# A destination with a URL scheme (https://github.com/…/0001-keywords.md) is no local link
URL_SCHEME_RE = re.compile(r'[A-Za-z][A-Za-z0-9+.-]*://')

# Search ranking (calculate_relevance_score): Meilisearch's _rankingScore, scaled into
# 1 - TITLE_BOOST_MAX, plus a boost for a page whose title is the name the query asks for.
# Meilisearch scores a type and every method named after it alike (URLSession and
# urlSession(_:didReceive:) both match the word exactly), so the title decides between them.
# A name typed all in lower case ("color", "accessibility") says nothing about case, so
# every page titled so gets the exact boost, and the more general page comes first (Color
# the type, not the color properties of hundreds of types).
TITLE_BOOST_MAX = 0.2
TITLE_EXACT_BOOST = 0.2  # the title is the name, case and all (any case for a lowercase name)
TITLE_NOCASE_BOOST = 0.15  # the same but for case
TITLE_FUNCTION_BOOST = 0.1  # a function of that name: name(...)
# A symbol page (not an article) named by one word of a longer query, a word typed with a
# capital as a symbol name is ("Concurrency Task", "date formatting DateFormatter",
# "Core Graphics CGPoint"): Meilisearch ranks the articles holding more of the words
# first, while the query asks for the symbol. Not the first word of a query that reads as
# a sentence when only its first letter is a capital: that may just start the sentence
# ("Color picker in SwiftUI")
NAMED_SYMBOL_BOOST = 0.1
# A deprecated page whose deprecation summary (the indexer's deprecation) holds every word
# of the query ranks with its Meilisearch score scaled by this, unless the query names it
# (a title or named-symbol boost): the summary tells what to use instead, so it holds the
# words of the replacement's task ("Use the UNUserNotificationCenter class to schedule
# local notifications instead" on five UIKit methods), and they matched there, not the
# page's own text. Meilisearch scores the pages a query matches within a few hundredths
DEPRECATED_RANKING_FACTOR = 0.9
# The kinds of pages that aren't symbols (scripts/metadata_extractor.py: a page without a
# **Kind** line, by its **Role** line in ROLE_KINDS, else an article)
NON_SYMBOL_KINDS = ("article", "collection", "sample-code")

# A question ("What is NavigationStack?", "How do I present a sheet in SwiftUI?") is
# searched without its question and function words: every word must match, and pages
# holding "what", "is", "how", "do" and the subject close together (release notes, long
# articles) outranked the subject's own page. Only for a question (several words, ending
# with "?", or starting with one of QUESTION_START_WORDS followed by another of
# QUESTION_STOP_WORDS), since some of these words are Swift keywords a plain query
# searches for ("is operator", "for in", "do catch"), and titles start with them too
# ("What’s New").
QUESTION_START_WORDS = frozenset({"what", "what's", "whats", "how", "why", "when", "which", "who", "whose"})
QUESTION_STOP_WORDS = frozenset({
    "what", "what's", "whats", "how", "why", "when", "where", "which", "who", "whom", "whose",
    "is", "are", "was", "were", "be", "been", "am", "do", "does", "did", "can", "could", "should",
    "would", "will", "shall", "may", "might", "must",
    "i", "me", "my", "we", "us", "our", "you", "your", "it", "its", "they", "them", "their",
    "a", "an", "the", "this", "that", "these", "those",
    "to", "of", "in", "on", "at", "by", "for", "with", "from", "into", "about", "between", "and", "or",
})

# A wildcard pattern that starts with this many literal characters ('UI*Controller') is
# matched against the pages whose api_name starts with them (ignoring case), besides the
# top matches for its literal text. At most WILDCARD_NAME_LIMIT names are listed, and the
# result says when there were more. On the full index (325K documents) a type prefix lists
# a few thousand ('CL' 3,880, 'MT' 3,602, 'NS' 2,733, 'UI' 1,173), but the commonest
# lowercase prefixes list more ('se' 7,955, 'co' 8,760, 're' 17,666, 'in' 30,268, of
# which 'init', every initializer's name, 24,350), and their patterns take ~0.1-0.5 s
# (up to ~1 s on a cold cache) against ~20-70 ms for a type prefix's.
WILDCARD_PREFIX_MIN = 2
WILDCARD_NAME_LIMIT = 10000

# expand_result's symbol lookup (symbol_candidates): candidates per search, one per page;
# also the most types a one-word search adds (search_apple_docs). Meilisearch scores every
# page named "data" alike (a property of hundreds of types, and Foundation's Data), so its
# top matches for the name alone often miss the type.
SYMBOL_CANDIDATES = 100
# Kinds that are types (scripts/metadata_extractor.py kind_mappings): a type is preferred
# over members of the same name (SwiftUI's Text struct over AVCaption.Ruby's text)
TYPE_KINDS = ("class", "struct", "enum", "protocol", "actor", "typealias", "union", "type", "namespace")
TYPE_KINDS_FILTER = "kind IN [" + ", ".join(f'"{kind}"' for kind in TYPE_KINDS) + "]"
# Frameworks the "also matches pages in" note names before "and N more"
AMBIGUITY_FRAMEWORKS_SHOWN = 8

# Meilisearch v1.49 never matches a filter string longer than this
# (MAX_FACET_VALUE_LENGTH = 500 - 32 bytes), so longer file paths can't be looked up. It
# measures the value normalized (filter_value_bytes), as the indexer checks it
# (scripts/index_to_meilisearch.py)
MAX_FILTER_VALUE_BYTES = 468

# Health check thresholds
MINIMUM_EXPECTED_DOCS = int(os.getenv("MIN_EXPECTED_DOCS", "290000"))
EXPECTED_FULL_INDEX_SIZE = int(os.getenv("EXPECTED_FULL_INDEX_SIZE", "322000"))

# Meilisearch connection settings
MEILI_TIMEOUT = int(os.getenv("MEILI_TIMEOUT", "10"))  # seconds
MEILI_MAX_RETRIES = int(os.getenv("MEILI_MAX_RETRIES", "2"))

# =============================================================================
# GLOBAL STATE
# =============================================================================

# Meilisearch connection (initialized on startup)
meili_client: Optional[meilisearch.Client] = None
meili_index: Optional[Any] = None

# Framework cache (refreshed after the TTL, so counts taken while the index
# was still building don't stick for the life of the process)
_frameworks_cache: Optional[Dict[str, int]] = None
_frameworks_cache_time: float = 0
_frameworks_cache_ttl: float = 300.0  # seconds

# The directories of a docs root by lowercased name, per root (framework_dirs)
_framework_dirs: Dict[str, Dict[str, str]] = {}

# =============================================================================
# MEILISEARCH INITIALIZATION
# =============================================================================


class MeilisearchSetupError(Exception):
    """Raised when Meilisearch connection setup fails (non-retryable)."""
    pass


# Track connection health
_last_health_check: float = 0
_health_check_interval: float = 30  # seconds


def init_meilisearch() -> bool:
    """Initialize Meilisearch client with timeout configuration."""
    global meili_client, meili_index, _last_health_check
    try:
        # Create client with timeout
        meili_client = meilisearch.Client(
            MEILISEARCH_URL,
            MEILISEARCH_API_KEY,
            timeout=MEILI_TIMEOUT
        )
        meili_index = meili_client.index(INDEX_NAME)

        health = meili_client.health()
        if health.get('status') != 'available':
            raise Exception(f"Meilisearch not available: {health}")

        # Test connection
        try:
            test_search = meili_index.search("", {"limit": 1})
            doc_count = test_search.get('estimatedTotalHits', 0)
            logger.info(f"Meilisearch connected: ~{doc_count:,} documents indexed (timeout={MEILI_TIMEOUT}s)")
        except Exception as e:
            logger.warning(f"Could not get document count: {e}")

        _last_health_check = time.time()
        return True
    except Exception as e:
        logger.error(f"Failed to connect to Meilisearch: {e}")
        return False


def ensure_meilisearch_connection() -> bool:
    """Check and restore Meilisearch connection if needed."""
    global meili_client, meili_index, _last_health_check

    # Quick check if client exists
    if not meili_client or not meili_index:
        logger.warning("Meilisearch client not initialized, attempting reconnection")
        return init_meilisearch()

    # Periodic health check (every 30 seconds)
    now = time.time()
    if now - _last_health_check > _health_check_interval:
        try:
            health = meili_client.health()
            if health.get('status') == 'available':
                _last_health_check = now
                return True
            else:
                logger.warning(f"Meilisearch health check failed: {health}")
                return init_meilisearch()
        except Exception as e:
            logger.warning(f"Meilisearch health check failed: {e}, attempting reconnection")
            return init_meilisearch()

    return True


def _is_retryable_error(e: Exception) -> bool:
    """Determine if an error is transient and worth retrying."""
    # Check meilisearch-specific exception types first
    error_type = type(e).__name__
    if error_type in ('MeilisearchCommunicationError', 'MeilisearchTimeoutError'):
        return True

    # Don't retry setup failures (ensure_meilisearch_connection already tried)
    if error_type == 'MeilisearchSetupError':
        return False

    # Don't retry API errors (bad queries, auth issues, etc.)
    if error_type == 'MeilisearchApiError':
        return False

    # Fallback: check error message for network-related keywords
    error_msg = str(e).lower()
    return any(keyword in error_msg for keyword in [
        'connection', 'timeout', 'refused', 'reset', 'broken pipe',
        'network', 'socket', 'eof', 'closed', 'unavailable'
    ])


T = TypeVar("T")


def _with_retries(operation: str, call: Callable[[], T], retries: int) -> T:
    """Run a Meilisearch call with error handling and retry logic.

    call reads meili_index when it runs, so a retry uses the reconnected index.
    """
    last_error = None

    for attempt in range(retries + 1):
        try:
            # Ensure connection is healthy
            if not ensure_meilisearch_connection():
                raise MeilisearchSetupError("Failed to establish Meilisearch connection")

            result = call()

            # Log recovery after successful retry
            if attempt > 0:
                logger.info(f"Meilisearch {operation} recovered after {attempt} retry(ies)")

            return result

        except Exception as e:
            last_error = e
            is_retryable = _is_retryable_error(e)
            logger.warning(
                f"Meilisearch {operation} failed (attempt {attempt + 1}/{retries + 1}): {e} "
                f"[{type(e).__name__}, retryable={is_retryable}]"
            )

            if is_retryable and attempt < retries:
                # Wait briefly before retry (exponential backoff)
                time.sleep(0.5 * (attempt + 1))
                # Force reconnection for network errors
                init_meilisearch()
            else:
                break

    # All retries exhausted
    raise Exception(f"Meilisearch {operation} failed after {retries + 1} attempts: {last_error}")


def _connected_index() -> Any:
    """The index object, which a successful ensure_meilisearch_connection has set."""
    if meili_index is None:
        raise MeilisearchSetupError("Meilisearch index not initialized")
    return meili_index


def safe_search(query: str, params: dict, retries: int = MEILI_MAX_RETRIES) -> dict:
    """Execute a Meilisearch search with error handling and retry logic."""
    return _with_retries("search", lambda: _connected_index().search(query, params), retries)


def safe_get_documents(params: dict, retries: int = MEILI_MAX_RETRIES) -> Any:
    """Fetch documents (a DocumentsResults) with error handling and retry logic.

    A POST, like a search: a GET would drop the Content-Type of the headers the index
    object shares with concurrent searches (see health_check).
    """
    return _with_retries("document fetch", lambda: _connected_index().get_documents(params), retries)


def get_framework_counts() -> Dict[str, int]:
    """Get framework counts with caching (TTL; empty results aren't cached,
    and a failed refresh keeps serving the last good counts)."""
    global _frameworks_cache, _frameworks_cache_time

    if _frameworks_cache and time.time() - _frameworks_cache_time < _frameworks_cache_ttl:
        return _frameworks_cache

    try:
        if not ensure_meilisearch_connection():
            logger.warning("Cannot get framework counts: Meilisearch not connected")
            return _frameworks_cache or {}

        results = safe_search("", {"facets": ["framework"], "limit": 0})
        counts: Dict[str, int] = results.get("facetDistribution", {}).get("framework", {})
        if counts:
            _frameworks_cache = counts
            _frameworks_cache_time = time.time()
        return counts
    except Exception as e:
        logger.error(f"Failed to get framework counts: {e}")
        return _frameworks_cache or {}


def get_index_metadata() -> Optional[Dict]:
    """Get metadata about the last indexing run."""
    if not meili_client:
        return None

    try:
        meta_index = meili_client.index(f"{INDEX_NAME}-meta")
        doc = meta_index.get_document("index_metadata")
        # get_document returns Document object, not dict - must convert
        return dict(doc) if doc else None
    except Exception as e:
        logger.debug(f"Could not get index metadata: {e}")
        return None


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def without_framework_words(query: str, framework: str) -> str:
    """query without the words that name framework, in one word or several ('SwiftUI' for
    SwiftUI, 'Core Data' for CoreData, 'App Intents' for AppIntents; letters and digits
    compared, ignoring case), or all of it when nothing else is left."""
    def key(text: str) -> str:
        return re.sub(r"[\W_]", "", text.lower())

    framework_key = key(framework)
    words = query.split()
    keys = [key(word) for word in words]
    kept: List[str] = []
    start = 0
    while start < len(words):
        joined, end = "", 0
        for i in range(start, len(words)):
            joined += keys[i]
            if not keys[i] or not framework_key.startswith(joined):
                break
            if joined == framework_key:
                end = i + 1
                break
        if end:
            start = end
        else:
            kept.append(words[start])
            start += 1
    return " ".join(kept or words)


def title_boost(title: str, name: str) -> float:
    """The boost for a page whose title is name: case and all (any case when name is all
    lowercase), ignoring case, or a function of that name (name(...))."""
    if title == name or (name.islower() and title.lower() == name):
        return TITLE_EXACT_BOOST
    if title.lower() == name.lower():
        return TITLE_NOCASE_BOOST
    if title.lower().startswith(name.lower() + "("):
        return TITLE_FUNCTION_BOOST
    return 0.0


def named_symbol_boost(hit: Dict, words: List[str], typed: str = "") -> float:
    """NAMED_SYMBOL_BOOST for a symbol page (not an article, API collection or sample code,
    NON_SYMBOL_KINDS) whose api_name is one of several query words, a word with a capital
    letter, case and all; else 0.

    typed is the query as typed. When it reads as a sentence (another of its words starts
    in lower case), the capital of its first word may only start it ("Color picker in
    SwiftUI", "Error handling Swift"): that word names a symbol only with another capital
    after its first letter ("NavigationView navigationBarTitle"). "Button SwiftUI" is no
    sentence."""
    name = str(hit.get("api_name", ""))
    if len(words) > 1 and hit.get("kind") not in NON_SYMBOL_KINDS and name in words and name != name.lower():
        typed_words = typed.split()
        if (typed_words and name == typed_words[0].rstrip("?!.,:;") and name[1:] == name[1:].lower()
                and any(word[:1].islower() for word in typed_words[1:])):
            return 0.0
        return NAMED_SYMBOL_BOOST
    return 0.0


def deprecation_matches(deprecation: str, query: str) -> bool:
    """Whether a deprecation summary holds every word of query, each as the start of one of
    its words (as Meilisearch matches 'notification' in 'notifications'), in the text it
    shows: a link's destination ("(./view/alert%28…%29.md)") isn't read."""
    words = re.findall(r"\w+", query.lower())
    if not deprecation or not words:
        return False
    shown = re.findall(r"\w+", re.sub(r"\]\([^)]*\)", "]", deprecation).lower())
    return all(any(word.startswith(query_word) for word in shown) for query_word in words)


def calculate_relevance_score(hit: Dict, query: str, asked: str = "") -> float:
    """A search hit's relevance (0.0-1.0): Meilisearch's _rankingScore (from its ranking
    rules: matched words, typos, proximity, attribute, position, exactness), plus a
    boost when the page's title is the name asked for, or a smaller one when the page is
    the symbol one word of a longer query names (named_symbol_boost).

    The query may also name the page's framework ("Button SwiftUI", "Core Data
    NSPersistentContainer"): the title is compared with the rest of it. asked is the query
    as asked: a question is searched without its question words (question_terms), and a
    page titled with the question itself ("What Is Core ML Tools?") keeps its boost.

    A deprecated page the query doesn't name (no boost) ranks lower when its deprecation
    summary holds the query's words (deprecation_matches): DEPRECATED_RANKING_FACTOR.
    """
    ranking = float(hit.get("_rankingScore") or 0.0)
    title = str(hit.get("title", ""))
    rest = without_framework_words(query, str(hit.get("framework", "")))
    boost = title_boost(title, rest)
    if asked.strip():
        boost = max(boost, title_boost(title.rstrip("?"), asked.strip().rstrip("?")))
    if not boost:
        boost = named_symbol_boost(hit, rest.split(), asked.strip() or query)
    if not boost and deprecation_matches(str(hit.get("deprecation") or ""), query):
        ranking *= DEPRECATED_RANKING_FACTOR
    # Rounded, so that hits Meilisearch ranks alike compare equal (see rank_hits)
    return round(ranking * (1 - TITLE_BOOST_MAX) + boost, 6)


def spelled_name(query: str) -> str:
    """The name a query of two or more words spells, its words joined ('vision entitlement
    services' -> 'visionentitlementservices'), when each word is letters, digits or '_';
    else ''."""
    words = query.split()
    if len(words) > 1 and all(re.fullmatch(r"\w+", word) for word in words):
        return "".join(words)
    return ""


def spells_title(title: str, spelled: str) -> bool:
    """Whether title is a type's or framework's name (a capital first, no whitespace) that
    spelled is, ignoring case. A member's name (lowerCamelCase) is left out: members are
    named with everyday phrases ('table view' would spell the tableView properties and
    tableView(...) methods of hundreds of types)."""
    return title[:1].isupper() and not re.search(r"\s", title) and title.lower() == spelled.lower()


def spelled_relevance(hit: Dict) -> float:
    """The relevance of a page whose name a query's words spell: as for a title that is the
    name but for case (TITLE_NOCASE_BOOST), from the _rankingScore of the name's own search
    (1.0 for its exact title). So it ranks after a page titled with the query itself ('text
    field': AppKit's "Text Field", then SwiftUI's TextField) and above every other page."""
    return round(float(hit.get("_rankingScore") or 0.0) * (1 - TITLE_BOOST_MAX) + TITLE_NOCASE_BOOST, 6)


def question_terms(original_query: str, query: str) -> str:
    """The words to search for: query without QUESTION_STOP_WORDS when original_query is a
    question (all of query when every word is one), else query unchanged.

    A question ends with "?", or starts with one of QUESTION_START_WORDS and has another of
    QUESTION_STOP_WORDS ("how do I present a sheet"); a title like "What’s New" is not one.
    """
    def plain(word: str) -> str:
        return re.sub(r"[^\w']", "", word.lower().replace("\u2019", "'"))

    words = query.split()
    original_words = [plain(word) for word in original_query.split()]
    is_question = original_query.rstrip().endswith("?") or (
        bool(original_words) and original_words[0] in QUESTION_START_WORDS
        and any(word in QUESTION_STOP_WORDS for word in original_words[1:]))
    if len(words) < 2 or not is_question:
        return query
    return " ".join(w for w in words if plain(w) not in QUESTION_STOP_WORDS) or query


def wildcard_prefix(pattern: str) -> str:
    """A wildcard pattern's literal text before its first '*' or '?'."""
    return re.split(r'[*?]', pattern)[0].strip()


def wildcard_matches(hits: List[Dict], pattern: "re.Pattern[str]", same_case: "re.Pattern[str]",
                     literal_chars: int) -> List[Dict]:
    """The hits whose title or api_name the wildcard pattern matches ignoring case (pattern
    is lowercased), each with its '_relevance', how closely the name fits the pattern: the
    share of the name the pattern's literal characters make up, ignoring case (UIView*
    gives UIView 1.0 and UIViewController 0.375), and its '_case_rank': 0 for a name in the
    pattern's own case (same_case matches it), 1 for any other, which rank_hits puts after
    the names in the pattern's case ('UI*' lists UIKey before uid; a pattern all in lower
    case matches every case, see search_apple_docs). The case orders the matches but leaves
    their relevance alone, so 'nsview*' shows NSView at 100% as 'NSView*' does, and
    relevance_threshold keeps it."""
    matches = []
    for hit in hits:
        for field in ("title", "api_name"):
            name = str(hit.get(field, ""))
            if pattern.match(name.lower()):
                hit['_relevance'] = round(min(1.0, literal_chars / max(1, len(name))), 6)
                hit['_case_rank'] = 0 if same_case.match(name) else 1
                matches.append(hit)
                break
    return matches


def list_names_by_prefix(prefix: str, filters: List[str]) -> Tuple[List[Dict[str, Any]], int]:
    """The pages whose api_name starts with prefix (ignoring case), within the filters: at
    most WILDCARD_NAME_LIMIT of their documents (file_path, title, api_name and platforms,
    for rank_hits), and how many documents there are."""
    params = {
        "filter": " AND ".join(filters + [f'api_name STARTS WITH "{escape_filter_value(prefix)}"']),
        "fields": ["file_path", "title", "api_name", "platforms"],
        "limit": WILDCARD_NAME_LIMIT,
    }
    results = safe_get_documents(params)
    return [dict(doc) for doc in results.results], int(results.total)


def fetch_hits_by_path(paths: List[str], filters: List[str], attrs: List[str]) -> Dict[str, Dict[str, Any]]:
    """One search hit (attrs) per page of these paths, by file_path."""
    values = ", ".join(f'"{escape_filter_value(path, max_length=None)}"' for path in paths)
    params = {
        "limit": len(paths),
        "attributesToRetrieve": attrs,
        "distinct": "file_path",
        "filter": " AND ".join(filters + [f"file_path IN [{values}]"]),
    }
    return {str(hit.get("file_path")): hit for hit in safe_search("", params).get("hits", [])}


def api_name_filter(name: str) -> str:
    """The filter for the pages whose api_name is name (ignoring case, as filters compare)."""
    return f'api_name = "{escape_filter_value(name, max_length=None)}"'


def searchable_filter_value(value: str) -> bool:
    """Whether a search's filter can hold value. Meilisearch v1.49's search reads a quoted
    filter value twice (it parses the filter, then parses its own rendering of it, where
    a backslash is no longer escaped): a backslash at the end of a value, or before
    anything but a quote, fails the search (invalid_search_filter), and any other is
    misread. No indexed name, path, framework or platform has one, so such a value matches
    nothing. (A documents fetch reads its filter once, so escape_filter_value suffices.)"""
    return "\\" not in value


def symbol_candidates(name: str, framework: str = "") -> Tuple[List[Dict[str, Any]], List[str]]:
    """The pages expand_result's symbol lookup chooses from, one hit per page: the types
    whose api_name is name (ignoring case), the other pages named so, then the top matches
    for name (SYMBOL_CANDIDATES of each), within framework when given. Also, without a
    framework, every framework that has a page whose api_name is name (its pages can
    outnumber the candidates: 'init' names ~24,000)."""
    if not searchable_filter_value(framework):
        return [], []
    base = [f'framework = "{escape_filter_value(framework)}"'] if framework else []
    named = api_name_filter(name)
    # No page is named with a backslash, and a search can't filter on one
    searches = [base + [named, TYPE_KINDS_FILTER], base + [named], base] if searchable_filter_value(name) else [base]
    candidates: List[Dict[str, Any]] = []
    frameworks: List[str] = []
    seen = set()
    for filters in searches:
        params: Dict[str, Any] = {
            "limit": SYMBOL_CANDIDATES,
            "attributesToRetrieve": ["title", "framework", "kind", "url", "file_path", "api_name", "platforms"],
            # One candidate per page, so the chunks of one long page can't fill the window
            "distinct": "file_path",
        }
        if filters:
            params["filter"] = " AND ".join(filters)
        if filters == [named]:
            # Without a framework: every framework that has a page of that name, for the note
            params["facets"] = ["framework"]
        results = safe_search(name, params)
        if "facets" in params:
            frameworks = sorted(results.get("facetDistribution", {}).get("framework", {}))
        for hit in results.get("hits", []):
            if hit.get("file_path") not in seen:
                seen.add(hit.get("file_path"))
                candidates.append(hit)
    return candidates, frameworks


def generality(hit: Dict[str, Any]) -> Tuple[int, int]:
    """A sort key for pages that otherwise tie, the more general first: the shorter path
    within its framework (a type before its members, a base class's method before a
    subclass's override), then the page available on more platforms (Foundation's
    UserDefaults before TVMLKit JS's, UIKit's viewDidLoad() before AppKit's). The whole
    path would favor the framework with the shorter directory name."""
    in_framework = str(hit.get("file_path", "")).split("/", 2)[-1]
    return len(in_framework), -len(hit.get("platforms") or [])


def pick_symbol(candidates: List[Dict[str, Any]], name: str) -> Optional[Dict[str, Any]]:
    """The candidate that is name's page, or None.

    In order: an exact, case-sensitive title ('Button' over 'Button tags'), that name's
    function page ('withAnimation' -> 'withAnimation(_:_:)'), then the looser
    case-insensitive matches. Among the candidates of the first of these that has any: a
    type before a member, then the shortest title (the simplest overload), then the more
    general page (generality), then the candidates' order.
    """
    lower = name.lower()
    tiers: List[Callable[[Dict[str, Any]], bool]] = [
        lambda h: h.get("title", "") == name,
        lambda h: h.get("title", "").startswith(name + "("),
        lambda h: h.get("title", "").lower() == lower or h.get("api_name", "").lower() == lower,
        lambda h: h.get("title", "").lower().startswith(lower + "("),
        lambda h: lower in h.get("api_name", "").lower(),
    ]
    for tier in tiers:
        matches = [h for h in candidates if tier(h)]
        if matches:
            return min(matches, key=lambda h: (h.get("kind") not in TYPE_KINDS, len(h.get("title", "")),
                                               *generality(h)))
    return None


def rank_hits(hits: List[Dict]) -> List[Dict]:
    """Hits by relevance (their '_relevance'), best first, a wildcard match not in the
    pattern's case after those that are (its '_case_rank', wildcard_matches). Equally
    relevant hits go the more general page first (generality), then in Meilisearch's order."""
    return sorted(hits, key=lambda hit: (hit.get('_case_rank', 0), -hit['_relevance'], *generality(hit)))


def estimate_tokens(text: str) -> int:
    """Estimate token count (~4 chars per token)."""
    return len(text) // 4


def framework_dirs(root: str) -> Dict[str, str]:
    """The directories of the docs root by lowercased name ({'swift': 'Swift'}), listed
    once per root (an unreadable root gives {} and is listed again next time)."""
    if root not in _framework_dirs:
        try:
            _framework_dirs[root] = {name.lower(): name for name in os.listdir(root)}
        except OSError:
            return {}
    return _framework_dirs[root]


def local_page(candidate: str) -> Optional[str]:
    """The page a link candidate names (a normalized path, documentation/<framework>/...),
    with its framework directory in its case on disk, when that file is in the docs
    (DOCUMENTATION_PATH); else None, as for a path outside documentation/.

    Links lowercase the framework of a page in another one (../swift/equatable.md), and the
    image's file system is case-sensitive."""
    parts = candidate.split("/")
    if len(parts) < 3 or parts[0] != "documentation":
        return None
    parts[1] = framework_dirs(DOCUMENTATION_PATH).get(parts[1].lower(), parts[1])
    if not os.path.isfile(os.path.join(DOCUMENTATION_PATH, *parts[1:])):
        return None
    return "/".join(parts)


def transform_internal_links(content: str, file_path: str) -> str:
    """The local links of the page at file_path made hints: the path of the page a link
    leads to, for expand_result, when that page is in the docs; else a search for the
    link's file name. A link with a URL scheme stays as it is.

    A link's destination, percent-encoded or not, is relative to the page's framework
    directory (the legacy base, how links have been written) or to the page itself
    (file-relative), and both are tried: a bare destination against the legacy base first,
    one starting with '../' against the page first, and one starting with './' only
    against the page (no legacy link starts so), so a link whose page is gone never
    resolves to a page of the same name at the framework's root. The hint leaves out the
    link's #fragment: expand_result takes a file path."""
    parts = file_path.split("/")
    framework_dir = f"documentation/{parts[1]}" if len(parts) > 2 else ""

    def replace_link(match: "re.Match[str]") -> str:
        text, dest = match.group(1), match.group(2)
        if URL_SCHEME_RE.match(dest):
            return match.group(0)
        target = unquote(dest)
        candidates = [posixpath.normpath(posixpath.join(posixpath.dirname(file_path), target))]
        if framework_dir and not dest.startswith("./"):
            legacy = posixpath.normpath(f"{framework_dir}/{target}")
            candidates.insert(1 if dest.startswith("../") else 0, legacy)
        for candidate in candidates:
            page = local_page(candidate)
            if page:
                return f"{text} (-> expand_result: {page})"
        # The path's names, without a file-relative link's "." and ".." segments (the path
        # itself when it has no other)
        path = target.replace('.md', '')
        names = [name for name in path.split('/') if name not in ('', '.', '..')] or [path]
        search_term = ' '.join(names).replace('-', ' ')
        return f"{text} (-> search: {' '.join(search_term.split())})"

    return LOCAL_LINK_RE.sub(replace_link, content)


def extract_section(content: str, section_name: str) -> str:
    """A section of a page: the text under its heading, a line of level 2-6 (the '# ' line
    is the page's title: a property named 'parameters' would give its whole page), up to
    the next heading of the same or a higher level.

    Level-1 lines end no section: after the title they are comments in code. A level-2
    section also ends at a '####' heading: the converter writes Apple's level-2 content
    headings (Overview, Discussion, Return Value) at that level, as siblings that follow
    '## Declaration' and '## Mentions'. So '## Topics' keeps its '###' groups, and
    '#### Overview' its '#####' subsections. Unless its '####' headings are its children:
    when its first sub-heading is a '###', or a '####' with no text before it (HIG's
    '## Platform considerations' / '### macOS' / '#### …', '## Resources' / '#### Related'),
    a level-2 section runs to the next '## '."""
    name = re.escape(section_name.replace('_', ' ').title())
    heading = re.search(rf'^(#{{2,6}})[ \t]*{name}[ \t]*$', content, re.MULTILINE | re.IGNORECASE)
    if not heading:
        return ""
    level = len(heading.group(1))
    body = content[heading.end():]
    end = rf'^#{{2,{level}}}\s'
    if level == 2:
        first = re.search(r'^(#{2,6})\s', body, re.MULTILINE)
        children = first is not None and (
            len(first.group(1)) == 3 or (len(first.group(1)) == 4 and not body[:first.start()].strip())
        )
        if not children:
            end += r'|^####\s'
    stop = re.search(end, body, re.MULTILINE)
    return (body[:stop.start()] if stop else body).strip()


def escape_filter_value(value: str, max_length: Optional[int] = 100) -> str:
    """
    Escape and sanitize filter values to prevent injection.

    Args:
        value: The filter value to escape
        max_length: Maximum allowed length (default 100 chars; None = no truncation)

    Returns:
        Sanitized and escaped string safe for use in Meilisearch filters
    """
    if not value:
        return value

    # Truncate to max length to prevent abuse
    value = value[:max_length]

    # Remove any control characters
    value = ''.join(c for c in value if c.isprintable())

    # Escape backslashes first, then double quotes
    value = value.replace('\\', '\\\\').replace('"', '\\"')

    return value


def filter_value_bytes(value: str) -> int:
    """Length of a filter value as Meilisearch's 468-byte limit counts it: trimmed,
    NFKD-normalized and lowercased (verified on v1.49), as the indexer measures file_path
    (scripts/index_to_meilisearch.py: filter_value_bytes)."""
    return len(unicodedata.normalize("NFKD", value.strip()).lower().encode("utf-8"))


def cut_text(text: str, max_chars: int) -> str:
    """Cut text to at most max_chars, closing a code block the cut left open."""
    text = text[:max(0, max_chars)].rstrip()
    if text.count("```") % 2:
        text += "\n```"
    return text


def get_file_chunks(file_path: str) -> List[Dict[str, Any]]:
    """Every document of one file, in chunk order (empty if the file isn't indexed).

    The indexer stores a file over its chunk size as several documents (chunks), one
    piece each: joined with "\\n" in chunk_index order, they are the file.
    """
    params: Dict[str, Any] = {
        # Full path, never truncated: a cut path matches no document
        "filter": f'file_path = "{escape_filter_value(file_path, max_length=None)}"',
        "fields": EXPAND_FIELDS,
        "limit": FILE_CHUNKS_LIMIT,
    }
    results = safe_get_documents(params)
    if results.total > len(results.results):
        params["limit"] = results.total
        results = safe_get_documents(params)
    chunks = [dict(doc) for doc in results.results]

    # A filter compares paths ignoring case and Unicode forms, so it can also match
    # another file's documents: keep one file's, the path asked for when it's there
    paths = sorted({str(chunk.get("file_path", "")) for chunk in chunks})
    if len(paths) > 1:
        keep = file_path if file_path in paths else paths[0]
        chunks = [chunk for chunk in chunks if chunk.get("file_path", "") == keep]

    # An update deletes a changed file's old documents only after every add of the run (a
    # run that stops first leaves them until the next): until then the file has two runs'
    # documents. Keep the newest run's, which are all of the file (the indexer sends a
    # file's documents in one batch). index_gen is a fixed-width UTC timestamp; documents
    # without one (an index built before it) count as the oldest.
    newest = max(str(chunk.get("index_gen") or "") for chunk in chunks) if chunks else ""
    chunks = [chunk for chunk in chunks if str(chunk.get("index_gen") or "") == newest]

    chunks.sort(key=lambda chunk: chunk.get("chunk_index") or 0)
    return chunks


def link_label(url: str) -> str:
    """A result link's label, named by the URL's host: "View on Apple Developer" only for
    Apple's own pages (the index also holds GitHub, MLX and coremltools docs)."""
    host = (urlsplit(url).hostname or "").removeprefix("www.")
    return f"View on {LINK_HOST_NAMES.get(host, host or 'source')}"


def part_label(hit: Dict[str, Any]) -> str:
    """"Part i of N" for a chunk of a file indexed as several documents, else ""."""
    index, total = hit.get("chunk_index"), hit.get("total_chunks")
    if isinstance(index, int) and isinstance(total, int) and total > 1:
        return f"Part {index + 1} of {total}"
    return ""


# =============================================================================
# FASTMCP SERVER SETUP
# =============================================================================

# Initialize FastMCP with instructions
mcp = FastMCP(
    name="apple-docs",
    version=SERVER_VERSION,  # serverInfo.version (defaults to the fastmcp version)
    instructions="""Apple Developer Documentation search server.
No authentication required. Rate limit: 60 requests/minute.
For unlimited access, contact info@xdocs.dev for an API key.""",
    # Unexpected exceptions reach clients as a generic isError result; the
    # details stay in the server log. ToolError messages are sent as written.
    mask_error_details=True,
)

# =============================================================================
# MCP TOOLS
# =============================================================================

@mcp.tool(
    annotations=ToolAnnotations(
        title="Search Apple Documentation",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    ),
    output_schema=None,  # text only; a str return would otherwise be sent twice
)
def search_apple_docs(
    query: Annotated[str, Field(max_length=256)],
    framework: Annotated[str, Field(max_length=100)] = "",
    strict_framework: bool = False,
    platform: Annotated[str, Field(max_length=100)] = "all",
    limit: int = 10,
    relevance_threshold: float = 0.0,
    token_budget: int = 5000,
    summary_mode: bool = False,
    offset: int = 0
) -> str:
    """Search Apple Developer Documentation.

    IMPORTANT: Use summary_mode=true for initial exploration, then expand_result for specific docs.
    Only increase token_budget when comprehensive coverage is needed.

    Returns one result per page. A result from a long page shows which part of it matched
    (e.g. 'Part 3 of 6'): expand_result with that part reads the page from there.

    Args:
        query: Search query (e.g., 'Button', 'async await', 'NavigationStack', or a question).
            Wildcards: '*' matches any characters and '?' one character in single-word queries
            (e.g., 'UIView*', 'UI*Controller', 'Button?'), ignoring case, names in the pattern's
            case first (unless it is all lowercase). A pattern is matched against the top
            matches for its literal text and, when it starts with 2+ literal characters, every
            API name starting with them (the first 10,000 when there are more); the results say
            when either was cut
        framework: Only return results from this framework (e.g., 'SwiftUI', 'UIKit', 'CarPlay')
        strict_framework: Deprecated, no effect (framework always filters); accepted for older clients
        platform: Filter by platform: 'ios', 'macos', 'tvos', 'watchos', 'visionos', or 'all'
        limit: Number of results (1-20, default: 10)
        relevance_threshold: Minimum relevance score (0.0-1.0)
        token_budget: Response size limit in tokens (1000-25000, default: 5000)
        summary_mode: Return condensed summaries instead of full content
        offset: Skip N results for pagination

    Returns:
        Formatted search results, one per page, with relevance scores and documentation content
    """
    # Validate connection
    if not ensure_meilisearch_connection():
        raise ToolError("Unable to connect to search backend. Please try again in a moment.")

    original_query = query.strip()
    # '?' is a one-character wildcard only in single-word queries ('Button?');
    # in a multi-word query it's a question mark ('What is NavigationStack?')
    if '?' in query and len(query.split()) > 1:
        query = query.replace('?', ' ')
    query = query.strip()

    if not query:
        raise ToolError("Query cannot be empty")

    # Clamp values
    limit = min(20, max(1, limit))
    token_budget = min(MAX_TOKEN_BUDGET, max(1000, token_budget))
    offset = max(0, offset)
    framework = framework.strip()
    platform = platform.strip()
    platform_filter = platform.lower() if platform.lower() not in ("", "all") else ""

    # Handle wildcards
    has_wildcards = '*' in query or '?' in query
    wildcard_pattern = None
    same_case_pattern = None
    literal_chars = 0
    name_prefix = ""
    spelled = ""  # the name the query's words spell (spelled_name)

    if has_wildcards:
        # fnmatch emits atomic groups, so a pattern can't backtrack
        # catastrophically (a hand-built '.*' per '*' let '******Q' freeze the
        # whole server). Runs of '*' collapse; '[' is escaped to stay literal.
        # Matched against lowercased fields (case-insensitive, as before); a name in
        # the pattern's own case ranks first (wildcard_matches).
        glob = re.sub(r'\*+', '*', query).replace('[', '[[]')
        wildcard_pattern = re.compile(fnmatch.translate(glob.lower()))
        # A pattern typed all in lower case says nothing about case: every case is its own
        same_case_pattern = re.compile(fnmatch.translate(glob), re.IGNORECASE if glob.islower() else 0)
        literal_chars = len(re.sub(r'[*?]', '', query))
        name_prefix = wildcard_prefix(query)
        query = query.replace('*', ' ').replace('?', ' ').strip() or "a"
    else:
        query = question_terms(original_query, query)
        spelled = spelled_name(query)

    # Build Meilisearch filter
    filters = []
    if framework:
        filters.append(f'framework = "{escape_filter_value(framework)}"')
    if platform_filter:
        filters.append(f'platforms = "{escape_filter_value(platform_filter)}"')
    if not (searchable_filter_value(framework) and searchable_filter_value(platform_filter)):
        # No framework or platform has a backslash, and a search can't filter on one
        return _build_no_results_response(original_query, framework, platform if platform_filter else "", has_wildcards)

    # Search attributes
    attrs = ["title", "framework", "api_name", "overview", "url", "platforms", "kind", "deprecated",
             "deprecation", "file_path", "chunk_index", "total_chunks"]
    if not summary_mode:
        attrs.append("content")

    window = max(100, limit * 5)  # results are ranked from this many top matches
    search_params = {
        "limit": window,
        "attributesToRetrieve": attrs,
        "attributesToHighlight": ["title", "api_name"],
        "highlightPreTag": "**",
        "highlightPostTag": "**",
        "showRankingScore": True,
        # One hit per file: its best-matching chunk, not every chunk of a long page
        "distinct": "file_path",
    }
    if filters:
        search_params["filter"] = " AND ".join(filters)

    names_total: Optional[int] = None  # names listed for a wildcard pattern's prefix
    types_added = False  # types named as a one-word query, past the top matches
    spelled_added = False  # pages named what the query's words spell, past the top matches
    try:
        results = safe_search(query, search_params)
        hits = results.get("hits", [])
        window_full = len(hits) >= window

        if has_wildcards and wildcard_pattern and same_case_pattern:
            # The pattern's literal text, searched as words, finds a name like
            # UIViewController (one word) only by its first letters, so the top matches
            # are joined by the pages whose name starts with the pattern's prefix
            hits = wildcard_matches(hits, wildcard_pattern, same_case_pattern, literal_chars)
            if len(name_prefix) >= WILDCARD_PREFIX_MIN:
                listed, names_total = list_names_by_prefix(name_prefix, filters)
                seen = {hit.get("file_path") for hit in hits}
                for doc in wildcard_matches(listed, wildcard_pattern, same_case_pattern, literal_chars):
                    if doc.get("file_path") not in seen:
                        seen.add(doc.get("file_path"))
                        hits.append(dict(doc, _listed=True))
        elif window_full and re.fullmatch(r"\w+", query):
            # Meilisearch scores every page with the word as its title alike, in index
            # order: for a common name (String, Data, Color, State) the type's own page can
            # be past the top matches, so the types named so join them
            type_params = dict(search_params, limit=SYMBOL_CANDIDATES,
                               filter=" AND ".join(filters + [api_name_filter(query), TYPE_KINDS_FILTER]))
            seen = {hit.get("file_path") for hit in hits}
            for hit in safe_search(query, type_params).get("hits", []):
                if hit.get("file_path") not in seen:
                    seen.add(hit.get("file_path"))
                    hits.append(hit)
                    types_added = True
        elif spelled:
            # A name typed as words ('vision entitlement services', 'async image') is one
            # word in the index (Meilisearch doesn't split CamelCase), which the words match
            # only joined, and its typo rule counts each joined word as a typo: every page
            # holding the words apart outranks the named page, even within the top matches.
            # So the types and frameworks named what the words spell are searched by that
            # name, and replace or join the top matches (spelled_relevance)
            name_params = dict(search_params, limit=SYMBOL_CANDIDATES,
                               filter=" AND ".join(filters + [api_name_filter(spelled)]))
            position = {hit.get("file_path"): i for i, hit in enumerate(hits)}
            for hit in safe_search(spelled, name_params).get("hits", []):
                if spells_title(str(hit.get("title", "")), spelled):
                    hit["_spelled"] = True
                    if hit.get("file_path") in position:
                        hits[position[hit.get("file_path")]] = hit
                    else:
                        position[hit.get("file_path")] = len(hits)
                        hits.append(hit)
                        spelled_added = True
    except Exception as e:
        logger.error(f"Search failed for query '{query}': {e}")
        raise ToolError("Search temporarily unavailable. Please try again in a moment.") from e

    if not hits:
        return _build_no_results_response(original_query, framework, platform if platform_filter else "", has_wildcards)

    # Score and filter results (framework is already a hard filter in the
    # search, so strict_framework has nothing left to do). A wildcard match's
    # relevance is how closely its name fits the pattern (wildcard_matches).
    scored_hits = []
    for hit in hits:
        if has_wildcards:
            score = hit['_relevance']
        elif hit.get('_spelled'):
            score = spelled_relevance(hit)
        else:
            score = calculate_relevance_score(hit, query, original_query)
        if score >= relevance_threshold:
            hit['_relevance'] = score
            scored_hits.append(hit)

    if not scored_hits:
        if relevance_threshold > 0:
            return f"No results above relevance threshold {relevance_threshold}"
        return _build_no_results_response(original_query, framework, platform if platform_filter else "", has_wildcards)

    scored_hits = rank_hits(scored_hits)
    total_text = f"{len(scored_hits)} results"
    names_capped = names_total is not None and names_total > WILDCARD_NAME_LIMIT
    added = ""  # what joined the top matches
    if names_total:
        # Every page whose name starts with the prefix was matched, unless there were more
        added = (f"the first {WILDCARD_NAME_LIMIT:,} of the {names_total:,} names starting with '{name_prefix}'"
                 if names_capped else f"every name starting with '{name_prefix}'")
    elif types_added:
        added = f"the types named '{query}'"
    elif spelled_added:
        added = f"the pages named '{spelled}'"
    if window_full:
        # Matches past the top ones were never seen, unless something else found them: a
        # title such as 'Publishers.Map' (api_name 'Map') comes only from the top matches
        total_text += f" (ranked from the top {window} matches" + (f" and {added}" if added else "") + ")"
    elif names_capped:
        total_text += f" (matched against {added})"

    paginated = scored_hits[offset:offset + limit]
    if not paginated:
        return f"No more results: offset {offset} is past the last of {total_text}."

    # A name listed by its prefix carries only its title and path: fetch what a result shows
    listed_paths = [str(hit.get("file_path")) for hit in paginated if hit.get("_listed")]
    if listed_paths:
        try:
            details = fetch_hits_by_path(listed_paths, filters, attrs)
        except Exception as e:
            logger.error(f"Search failed for query '{query}': {e}")
            raise ToolError("Search temporarily unavailable. Please try again in a moment.") from e
        for hit in paginated:
            if hit.get("_listed"):
                hit.update(details.get(str(hit.get("file_path")), {}))

    # Build output ("Showing" line is filled in once we know what fit the budget)
    output = [f"Search Results: {original_query}", ""]

    if framework:
        output.append(f"Framework: {framework}")
    if platform_filter:
        output.append(f"Platform: {platform}")
    output.append("")

    # The reply's length in characters, counted whole (estimate_tokens of each piece,
    # floored and without the newlines joining them, undercounts), with room for the
    # "Showing" line and the longest "more results" footer, which are only written after
    # the results are chosen: neither can end past offset + limit
    showing = f"Showing {offset + 1}-{offset + limit} of {total_text}"
    footer = (f"\nToken budget reached. {len(scored_hits)} more results available. "
              f"Use offset={offset + limit} to continue")
    used = len("\n".join(output)) + len(showing) + 1 + len(footer)
    results_included = 0
    budget_reached = False

    # Results are numbered by overall rank, so numbers continue across pages
    for rank, hit in enumerate(paginated, offset + 1):
        result_lines = []
        relevance = hit.get('_relevance', 0)

        result_lines.append(f"## {rank}. {hit.get('title', 'Untitled')} ({int(relevance * 100)}%)")
        # A hit from a long page is one of its parts: expand_result's part reads it
        part = part_label(hit)
        result_lines.append(f"Framework: {hit.get('framework', 'Unknown')} | Type: {hit.get('kind', '')}"
                            + (" | Deprecated" if hit.get("deprecated") else "")
                            + (f" | {part}" if part else ""))
        if hit.get("file_path"):
            result_lines.append(f"Path: `{hit.get('file_path')}`")
        if hit.get("url"):
            result_lines.append(f"[{link_label(hit['url'])}]({hit['url']})")
        result_lines.append("")

        body = ""
        if not summary_mode and hit.get("content"):
            body = transform_internal_links(hit.get("content", ""), str(hit.get("file_path", "")))
        elif hit.get("overview"):
            body = hit.get("overview", "")[:400]
        if summary_mode and hit.get("deprecation"):
            # What to use instead, its links as hints (the content holds it as the page does)
            deprecation = transform_internal_links(str(hit["deprecation"]), str(hit.get("file_path", "")))
            body = "\n".join(["Deprecated: " + deprecation] + ([body] if body else []))

        result_text = "\n".join(result_lines + ([body] if body else []) + ["\n---\n"])

        # The result and the newline joining it
        if (used + len(result_text) + 1) // 4 > token_budget:
            if results_included > 0:
                # Stop at the first result that doesn't fit, so the next
                # offset resumes exactly here (nothing skipped or repeated)
                budget_reached = True
                break
            # A single result larger than the whole budget: truncate its body
            room = (token_budget - used // 4 - estimate_tokens("\n".join(result_lines)) - 60) * 4
            body = cut_text(body, room)
            body += (
                f"\n\n[Truncated to fit token_budget={token_budget}. "
                "Use expand_result with the Path above for the full document.]"
            )
            result_text = "\n".join(result_lines + [body, "\n---\n"])

        output.append(result_text)
        used += len(result_text) + 1
        results_included += 1

    shown_end = offset + results_included
    output[1] = f"Showing {offset + 1}-{shown_end} of {total_text}"
    remaining = len(scored_hits) - shown_end
    if remaining > 0:
        note = "Token budget reached. " if budget_reached else ""
        output.append(f"\n{note}{remaining} more results available. Use offset={shown_end} to continue")

    return "\n".join(output)


def _build_no_results_response(query: str, framework: str, platform: str, has_wildcards: bool) -> str:
    """Build helpful response when no results found."""
    lines = [f"No results found for '{query}'"]
    if framework:
        lines.append(f"   Framework: {framework}")
    if platform and platform != "all":
        lines.append(f"   Platform: {platform}")
    lines.append("")
    lines.append("Suggestions:")
    prefix = wildcard_prefix(query) if has_wildcards else ""
    if has_wildcards and len(prefix) >= WILDCARD_PREFIX_MIN:
        # Such a pattern is matched against the names starting with its prefix already
        lines.append(f"   - Check the spelling, or use fewer literal characters (the pattern is matched "
                     f"against the API names starting with '{prefix}')")
    elif has_wildcards:
        lines.append("   - Try a pattern that starts with 2+ literal characters (e.g., UIView*, UI*Controller)")
    else:
        lines.append("   - Try simpler keywords")
        lines.append("   - Use wildcards: Button* or NSTable*")
    if framework:
        lines.append("   - Try without framework filter")
    if platform and platform != "all":
        lines.append("   - Try without platform filter")
    return "\n".join(lines)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Expand Documentation Result",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    ),
    output_schema=None,  # text only; a str return would otherwise be sent twice
)
def expand_result(
    file_path: Annotated[str, Field(max_length=1024)],
    sections: Optional[Annotated[List[Annotated[str, Field(max_length=64)]], Field(max_length=20)]] = None,
    framework: Annotated[str, Field(max_length=100)] = "",
    part: int = 0
) -> str:
    """Get full documentation for a symbol or file.

    A page too long for one response comes in parts: a reply holds as many whole parts
    as fit and ends with which ones (e.g. 'Parts 1-4 of 12 of `<path>`') and the part
    to pass with that path for the rest (part=5).

    Args:
        file_path: Symbol name (e.g., 'Button') or file path from search results
        sections: Specific sections to include (e.g., ['overview', 'declaration']), taken from the
            whole page (part is ignored)
        framework: Framework to look a symbol up in (e.g., 'SwiftUI'); use it for names that exist
            in many frameworks, like 'List', 'Text' or 'View'. Ignored for file paths
        part: Part of a long page to start from, from 1 (a search result from a long page shows
            its part, e.g. 'Part 3 of 6'); the reply holds it and as many of the next parts as
            fit. Default 0: the whole page if it fits in one response, else from part 1

    Returns:
        Full documentation content
    """
    # Validate connection
    if not ensure_meilisearch_connection():
        raise ToolError("Unable to connect to search backend. Please try again in a moment.")

    sections = sections or []
    framework = framework.strip()
    part = max(0, part)
    input_value = file_path.strip().strip('`').strip()
    if not input_value:
        raise ToolError("file_path is required")

    # Anything that isn't a path is a symbol name, including lowercase ones
    # like 'withAnimation' or 'viewDidLoad'
    is_symbol = '/' not in input_value and not input_value.lower().endswith('.md')
    ambiguity_note = ""

    try:
        if is_symbol:
            hits, named_frameworks = symbol_candidates(input_value, framework)
            match = pick_symbol(hits, input_value)

            if not match:
                suggestions = [f"   - {h.get('api_name', h.get('title'))} ({h.get('framework')})" for h in hits[:5]]
                output = [f"Symbol '{input_value}' not found" + (f" in framework '{framework}'" if framework else "")]
                if suggestions:
                    output.extend(["", "Similar:"] + suggestions)
                return "\n".join(output)

            hit = match
            if not framework:
                # Same name in other frameworks (a candidate's title, or any page's api_name):
                # say so, so the caller can pick one
                title = hit.get("title", "").lower()
                others = sorted(({
                    h.get("framework", "") for h in hits
                    if h.get("title", "").lower() == title
                    or h.get("title", "").lower().startswith(input_value.lower() + "(")
                } | set(named_frameworks)) - {hit.get("framework", "")})
                if others:
                    named = ", ".join(others[:AMBIGUITY_FRAMEWORKS_SHOWN]) + (
                        f" and {len(others) - AMBIGUITY_FRAMEWORKS_SHOWN} more"
                        if len(others) > AMBIGUITY_FRAMEWORKS_SHOWN else "")
                    ambiguity_note = (
                        f"Note: '{input_value}' also matches pages in {named}; showing "
                        f"{hit.get('framework', 'Unknown')}. Pass framework (e.g. framework=\"{others[0]}\") "
                        "to choose another."
                    )
            # The hit is one chunk of its page: the page is all of them
            chunks = get_file_chunks(hit["file_path"]) if hit.get("file_path") else []
        else:
            # File path lookup
            relative_path = input_value
            if input_value.startswith('/') and 'documentation/' in input_value:
                relative_path = input_value[input_value.find('documentation/'):]

            path_bytes = filter_value_bytes(relative_path)
            if path_bytes > MAX_FILTER_VALUE_BYTES:
                raise ToolError(
                    f"file_path is too long ({path_bytes} bytes; "
                    f"max {MAX_FILTER_VALUE_BYTES}). Use the Path shown in search results."
                )

            chunks = get_file_chunks(relative_path)
            if not chunks:
                return f"File not found: {relative_path}"

    except ToolError:
        raise
    except Exception as e:
        logger.error(f"Expand failed for '{file_path}': {e}")
        raise ToolError("Unable to retrieve documentation. Please try again in a moment.") from e

    pieces = [chunk.get("content") or "" for chunk in chunks]
    if not any(pieces):
        return "No content available"
    doc_path = chunks[0].get("file_path", "")
    notes = [ambiguity_note] if ambiguity_note else []

    if sections:
        # From the whole page, so a section that spans two chunks comes whole
        content = "\n".join(pieces)
        output = [f"# {chunks[0].get('title', 'Documentation')}", ""]
        for section in sections:
            section_content = transform_internal_links(extract_section(content, section), doc_path)
            if section_content:
                output.append(f"## {section.title()}")
                output.append(section_content)
                output.append("")
        text = "\n".join(output)
        if estimate_tokens(text) > EXPAND_TOKEN_CAP:
            text = cut_text(text, EXPAND_TOKEN_CAP * 4) + (
                "\n\n[Truncated to fit one response. Read the whole page in parts: "
                f"expand_result(file_path=\"{doc_path}\", part=1).]\n"
            )
        return "\n".join([text] + (["---"] + notes if notes else []))

    total_parts = len(pieces)
    if part > total_parts:
        return f"No part {part}: `{doc_path}` has {total_parts} part{'' if total_parts == 1 else 's'}."

    text = transform_internal_links("\n".join(pieces), doc_path)
    if part or estimate_tokens(text) > EXPAND_TOKEN_CAP:
        first = last = part or 1
        if total_parts > 1:
            # Parts are the page's chunks, so a search result's "Part i of N" is part=i
            # here: the reply holds that part and, whole, as many of the next as fit
            texts = [transform_internal_links(pieces[first - 1], doc_path)]
            while last < total_parts:
                more = texts + [transform_internal_links(pieces[last], doc_path)]
                if estimate_tokens("\n".join(more)) > EXPAND_TOKEN_CAP:
                    break
                texts, last = more, last + 1
            text = "\n".join(texts)
            notes.insert(0, (
                (f"Part {first}" if first == last else f"Parts {first}-{last}")
                + f" of {total_parts} of `{doc_path}`"
                + (": the page is too long for one response" if not part else "")
                + (f". For the next part, pass this file_path with part={last + 1}."
                   if last < total_parts else " (the end of the page).")
            ))
        if estimate_tokens(text) > EXPAND_TOKEN_CAP:
            # Chunks are at most ~52 KB (~13K tokens), but an index built by an older
            # indexer can hold longer ones
            text = cut_text(text, EXPAND_TOKEN_CAP * 4) + (
                "\n\n[Truncated: this part is longer than one response allows.]"
            )

    if notes:
        return f"{text}\n\n---\n" + "\n".join(notes)
    return text


@mcp.tool(
    annotations=ToolAnnotations(
        title="List Apple Frameworks",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    ),
    output_schema=None,  # text only; a str return would otherwise be sent twice
)
def list_frameworks(query: Annotated[str, Field(max_length=256)] = "") -> str:
    """List available Apple frameworks with document counts.

    Args:
        query: Optional filter to search framework names (e.g., 'UI', 'Core')

    Returns:
        Formatted list of frameworks with document counts
    """
    # Validate connection first
    if not ensure_meilisearch_connection():
        raise ToolError("Unable to connect to search backend. Please try again in a moment.")

    framework_counts = get_framework_counts()
    if not framework_counts:
        return "No frameworks found. The search index may be rebuilding - please try again in a moment."

    if query:
        filtered = {k: v for k, v in framework_counts.items() if query.lower() in k.lower()}
    else:
        filtered = framework_counts

    sorted_frameworks = sorted(filtered.items(), key=lambda x: (-x[1], x[0]))

    output = []
    if query:
        output.append(f"Frameworks matching '{query}' ({len(sorted_frameworks)} of {len(framework_counts)}):")
    else:
        output.append(f"Available Frameworks ({len(sorted_frameworks)}):")
    output.append("")

    for i, (fw, count) in enumerate(sorted_frameworks, 1):
        output.append(f"   {i:3d}. {fw:<30} ({count:,} docs)")

    output.extend(["", "Use: search_apple_docs(query=\"Button\", framework=\"SwiftUI\")"])
    return "\n".join(output)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Server Version",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    ),
    output_schema=None,  # text only; a str return would otherwise be sent twice
)
def get_version() -> str:
    """Get server version and status.

    Returns:
        Version info and Meilisearch status
    """
    # Check connection status
    connection_ok = ensure_meilisearch_connection()
    counts = get_framework_counts() if connection_ok else {}
    total_docs = sum(counts.values())

    status = "Connected" if connection_ok and meili_index else "Disconnected"
    if not connection_ok:
        status = "Reconnecting..."

    return f"""**Apple Docs MCP Server** v{SERVER_VERSION}

**Status:**
   Meilisearch: {status}
   Frameworks: {len(counts)}
   Documents: {total_docs:,}

**Tools:** search_apple_docs, expand_result, list_frameworks, get_version"""


# =============================================================================
# RATE LIMITING MIDDLEWARE
# =============================================================================

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse as StarletteJSONResponse


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Rate limiting with API key bypass."""

    def __init__(self, app, requests_per_minute: int = 30, api_key: str = ""):
        super().__init__(app)
        self.requests_per_minute = requests_per_minute
        self.api_key = api_key
        self.request_counts: Dict[str, List[float]] = defaultdict(list)
        self._last_cleanup = time.time()
        self._cleanup_interval = 300  # Clean up all stale entries every 5 minutes

    def _get_client_ip(self, request) -> str:
        # Use the RIGHTMOST X-Forwarded-For token: Caddy appends the real
        # client IP as the last value, while leftmost tokens are
        # client-supplied and would let attackers rotate rate-limit buckets.
        forwarded = request.headers.get("x-forwarded-for")
        if forwarded:
            return forwarded.split(",")[-1].strip()
        return request.client.host if request.client else "unknown"

    def _is_authenticated(self, request) -> bool:
        if not self.api_key:
            return False
        auth = request.headers.get("authorization", "")
        if auth.startswith("Bearer "):
            return secrets.compare_digest(auth[7:], self.api_key)
        return False

    def _cleanup_stale_entries(self, now: float, window_start: float) -> None:
        """Remove all stale entries from all IPs to prevent memory growth."""
        stale_ips = []
        for ip, timestamps in self.request_counts.items():
            # Filter old timestamps
            self.request_counts[ip] = [t for t in timestamps if t > window_start]
            # Mark empty entries for removal
            if not self.request_counts[ip]:
                stale_ips.append(ip)
        # Remove empty entries
        for ip in stale_ips:
            del self.request_counts[ip]
        self._last_cleanup = now

    def _check_rate_limit(self, client_ip: str) -> bool:
        now = time.time()
        window_start = now - 60

        # Periodically clean up all stale entries to prevent memory growth
        if now - self._last_cleanup > self._cleanup_interval:
            self._cleanup_stale_entries(now, window_start)

        # Clean old entries for current IP
        self.request_counts[client_ip] = [
            t for t in self.request_counts[client_ip] if t > window_start
        ]

        if len(self.request_counts[client_ip]) >= self.requests_per_minute:
            return True

        self.request_counts[client_ip].append(now)
        return False

    async def dispatch(self, request, call_next):
        # Skip for health checks
        if request.url.path == "/health":
            return await call_next(request)

        # Authenticated requests bypass rate limit
        if self._is_authenticated(request):
            return await call_next(request)

        client_ip = self._get_client_ip(request)
        if self._check_rate_limit(client_ip):
            # Log rate limit hits for debugging
            logger.warning(f"Rate limit exceeded for {client_ip}: {len(self.request_counts[client_ip])} requests in last minute")
            return StarletteJSONResponse(
                status_code=429,
                content={
                    "error": "Rate limit exceeded",
                    "message": f"Limit: {self.requests_per_minute}/minute. Use API key to bypass.",
                    "retry_after": 60
                },
                headers={"Retry-After": "60"}
            )

        return await call_next(request)


# =============================================================================
# CUSTOM ROUTES
# =============================================================================

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    """Health check endpoint with stats and indexing progress."""
    from starlette.responses import JSONResponse

    # Get FRESH stats directly from Meilisearch (don't use cache for health checks)
    total_docs = 0
    has_pending_tasks = False
    framework_count = 0

    if meili_index and meili_client:
        try:
            # Not meili_index: the client keeps one headers dict per index object, and a
            # GET drops its Content-Type, so a GET on the object the searches share can
            # send a concurrent search without one (missing_content_type, a failed search)
            stats = meili_client.index(INDEX_NAME).get_stats()
            total_docs = getattr(stats, 'number_of_documents', 0)

            # Detect indexing: stats.is_indexing (during batch) OR recent indexing task (between batches)
            is_actively_indexing = getattr(stats, 'is_indexing', False)
            has_recent_indexing = False

            try:
                from datetime import datetime, timezone
                # Only the live index's tasks: a rebuild's adds go to apple-docs-build
                # while the live index serves every search, and the indexer writes
                # apple-docs-meta on every start. A swap moves the build's tasks to the
                # live index, so the window after a swap still shows as indexing.
                tasks = meili_client.get_tasks({
                    "types": ["documentAdditionOrUpdate"],
                    "indexUids": [INDEX_NAME],
                    "limit": 1
                })
                if tasks.results:
                    task = tasks.results[0]
                    if task.status in ["enqueued", "processing"]:
                        has_recent_indexing = True
                    elif task.status == "succeeded" and task.finished_at:
                        # finished_at is already a datetime object from the library
                        finished = task.finished_at
                        if finished.tzinfo is None:
                            finished = finished.replace(tzinfo=timezone.utc)
                        age = (datetime.now(timezone.utc) - finished).total_seconds()
                        has_recent_indexing = age < 210  # Task finished within 3.5 min
            except Exception:
                pass  # Fall back to is_actively_indexing only

            has_pending_tasks = is_actively_indexing or has_recent_indexing

            # Get unique framework count from fresh facet query (bypass cache)
            try:
                results = meili_index.search("", {"facets": ["framework"], "limit": 0})
                facets = results.get("facetDistribution", {}).get("framework", {})
                framework_count = len(facets)
            except Exception:
                framework_count = 0
        except Exception as e:
            logger.warning(f"Failed to get Meilisearch stats: {e}")

    # Get index metadata
    metadata = get_index_metadata()

    # Determine status based on state
    if not meili_index:
        status = "unhealthy"
    elif has_pending_tasks:
        status = "indexing"
    elif total_docs < MINIMUM_EXPECTED_DOCS:
        status = "degraded"
    else:
        status = "healthy"

    response_data = {
        "status": status,
        "service": "apple-docs-mcp",
        "version": SERVER_VERSION,
        "meilisearch": "connected" if meili_index else "disconnected",
        "frameworks": framework_count,
        "documents": total_docs
    }

    # Add indexing progress if actively indexing
    if has_pending_tasks:
        response_data["is_indexing"] = True
        # Estimate progress based on expected full index size
        progress_pct = min(100, int(total_docs * 100 / EXPECTED_FULL_INDEX_SIZE))
        response_data["progress"] = f"{progress_pct}%"

    # Add timestamps
    # docs_updated: When documentation was last changed (from git, set at build time)
    if DOCS_UPDATED and DOCS_UPDATED != "unknown":
        response_data["docs_updated"] = DOCS_UPDATED

    # last_indexed: When Meilisearch indexing last completed (from metadata)
    if metadata and metadata.get("last_indexed"):
        response_data["last_indexed"] = metadata["last_indexed"]

    # last_index_full: When the last full rebuild was swapped in (from metadata)
    if metadata and metadata.get("last_index_full"):
        response_data["last_index_full"] = metadata["last_index_full"]

    # image_built: When Docker image was created (from BUILD_TIME env var)
    if BUILD_TIME and BUILD_TIME != "unknown":
        response_data["image_built"] = BUILD_TIME

    # Return appropriate HTTP status code
    http_status = 200 if status == "healthy" else 503
    return JSONResponse(response_data, status_code=http_status, headers={"Access-Control-Allow-Origin": "*"})


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Main entry point."""
    import argparse
    import uvicorn
    from starlette.middleware import Middleware

    parser = argparse.ArgumentParser(description="Apple Docs MCP Server")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", "-p", type=int, default=HTTP_PORT)
    args = parser.parse_args()

    logger.info(f"Apple Docs MCP Server v{SERVER_VERSION}")

    # Initialize Meilisearch
    if not init_meilisearch():
        logger.error("Meilisearch connection failed")

    logger.info(f"HTTP mode: http://0.0.0.0:{args.port}/mcp")
    logger.info(f"Rate limit: {RATE_LIMIT_REQUESTS}/min (bypass with API key)")

    # Create middleware list with rate limiting
    middleware = [
        Middleware(
            RateLimitMiddleware,
            requests_per_minute=RATE_LIMIT_REQUESTS,
            api_key=MCP_API_KEY,
        )
    ]

    logger.info(f"Allowed hosts: {ALLOWED_HOSTS} (+ localhost)")

    # Create ASGI app with middleware attached
    app = mcp.http_app(
        path="/mcp",
        middleware=middleware,
        transport="streamable-http",
        stateless_http=True,  # Stateless for HTTP scalability
        allowed_hosts=ALLOWED_HOSTS,  # fastmcp 3.x rejects unknown Host headers with 421
    )

    # Run with uvicorn
    # limit_concurrency: max concurrent connections
    uvicorn.run(
        app,
        host=args.host,
        port=args.port,
        log_level="info",
        limit_concurrency=100,
    )


if __name__ == "__main__":
    main()
