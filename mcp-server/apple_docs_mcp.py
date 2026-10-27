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
import difflib
import fnmatch
import posixpath
import secrets
import time
import logging
import unicodedata
from collections import defaultdict
from typing import Annotated, Callable, Dict, List, Optional, Any, Tuple, TypeVar
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

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
SERVER_VERSION = "3.5.0"
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

# The characters a result link's URL holds as they are (link_url): RFC 3986's reserved ones
# and "%", so its delimiters and escapes stay, as the scrapers encode the URLs they build
# (scripts/utilities/source_policy.py encode_url) and a DocC page's footer
# (scraper/utils/links.py markdown_url, the same rule as link_url)
URL_SAFE_CHARACTERS = "!#$%&'()*+,/:;=?@[]~"

# The platforms a search filters on: the values the indexer gives a page's platforms
# (scripts/metadata_extractor.py platform_mappings), matched ignoring case
PLATFORMS = ("iOS", "iPadOS", "Mac Catalyst", "macOS", "tvOS", "visionOS", "watchOS")

# A summary_mode result's overview is cut to this many characters (summary_text)
SUMMARY_CHARS = 400
# Close framework names a search for an unknown framework suggests (difflib), and the
# sections an expand_result naming one its page doesn't have lists before "and N more"
FRAMEWORK_SUGGESTIONS = 3
SECTIONS_LISTED = 30

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
# Any markdown link or image, its text holding brackets two levels deep and its destination
# balanced parentheses; and one whose destination a text's end left unclosed (an indexer
# before PROCESSOR_VERSION 4 cut an overview at 500 characters, wherever that fell):
# summary_text never shows one in half. Only from "](" on: a "[" alone may open a range
# ("[min, max)") or a command's options ("[--disable-sandbox]")
MARKDOWN_LINK_RE = re.compile(r'!?\[(?:[^\[\]]|\[(?:[^\[\]]|\[[^\[\]]*\])*\])*\]\((?:[^()\s]|\([^()\s]*\))*\)')
UNCLOSED_LINK_RE = re.compile(r'!?\[(?:[^\[\]]|\[(?:[^\[\]]|\[[^\[\]]*\])*\])*\]\([^)\s]*$')
# A heading line of a page (expand_result's sections), and a code fence's line
HEADING_LINE_RE = re.compile(r'^(#{2,6})[ \t]+(.+?)[ \t]*$', re.MULTILINE)
FENCE_RE = re.compile(r'^[ \t]*(`{3,}|~{3,})')
# DocC's level-2 content sections (the headings Apple's pages start their content with),
# and the sections the converter writes before a page's content: its declaration, the
# possible values of a key or REST type, its mentions (pushed_down_headings)
DOCC_CONTENT_HEADINGS = frozenset({"Overview", "Discussion", "Return Value"})
DOCC_LEADING_SECTIONS = frozenset({"Declaration", "Possible Values", "Mentions"})

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
# A multi-word query no title boost applies to (a task, "tab bar design guidelines",
# "Keychain store password"): Meilisearch has no length normalization and ranks a title
# match only after proximity, so long pages holding every word somewhere (release notes,
# sample code lists, technotes) outrank the page whose title holds them. A page whose
# title holds at least TITLE_WORDS_MIN_SHARE of the query's words (QUESTION_STOP_WORDS
# left out, at least two) gets TITLE_WORDS_BOOST times that share: small, so an exact
# name (TITLE_FUNCTION_BOOST and up) still decides. A symbol's title is its api_name
# only (not its argument labels or its type's name, which hold everyday words). Words
# match with a short ending (TITLE_WORD_ENDING: bar/bars, request/requesting) when the
# shorter has TITLE_WORD_MIN letters.
TITLE_WORDS_BOOST = 0.05
TITLE_WORDS_MIN_SHARE = 0.5
TITLE_WORD_MIN = 3
TITLE_WORD_ENDING = 3
# A Swift attribute, property wrapper or macro written as used ('@State', '@MainActor',
# '#Preview'): Meilisearch reads '@' and '#' as separators, so the query's names are
# compared without them (strip_sigils), and such a name can only be a type (a property
# wrapper, result builder or global actor) or a macro (sigil_kinds), or a built-in
# attribute the Swift book documents ('@escaping', '@objc': ATTRIBUTE_SEARCH_WORD)
SIGIL_RE = re.compile(r"(?<!\S)[@#](?=\w)")
ATTRIBUTE_SEARCH_WORD = "attribute"
# A member written after its type ('Product.purchase', 'DispatchQueue.main.async'): its
# page is under the type's directory, which Apple suffixes with the symbol's language and
# kind when two symbols share the name ('text-swift.struct', 'uicontentunavailable
# configuration-c.class')
DOTTED_NAME_RE = re.compile(r"[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)+")
# The most dotted names of one query looked up (two searches each)
DOTTED_NAMES_MAX = 3
KIND_DIRECTORY_SUFFIX_RE = re.compile(r"-(?:swift|c|objc)\.[a-z.]+$")
# A prefixed type typed without its prefix ('Button' in UIKit for UIButton, 'Metal device'
# for MTLDevice, 'Speech recognizer' for SFSpeechRecognizer): the indexer's
# api_name_unprefixed (scripts/metadata_extractor.py). Looked up only within a framework
# the search filters on or the query names, where few types share it, and ranked as a
# title that is the name but for case (TITLE_NOCASE_BOOST) with a full score: after a
# page titled with the name itself, before every other page
UNPREFIXED_NAME_FIELD = "api_name_unprefixed"
UNPREFIXED_NAME_BOOST = TITLE_NOCASE_BOOST
# A file name ending in a DocC disambiguation suffix ('init(_)-1a4oh.md', 'frame-2ifgd.md'):
# a symbol's name (no '-': an article's name is words joined by '-', 'init-action-label')
# and a hash of 4-6 lowercase letters and digits, which holds a digit unless the name is a
# function's ('tab-bars' is an article's name). A link to an overload the scraper didn't
# write (without_disambiguation)
DISAMBIGUATION_SUFFIX_RE = re.compile(r"^([^/-]+)-([a-z0-9]{4,6})\.md$")

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
# The kinds a name written '@Name' can be (SIGIL_RE): a property wrapper or result
# builder (a struct, class or enum, or a typealias of one: Foundation's Published), a
# global actor (MainActor), or an attached macro; never a protocol or a C type. A name
# written '#Name' is a freestanding macro (sigil_kinds)
ATTRIBUTE_KINDS = ("class", "struct", "enum", "actor", "typealias", "macro")
MACRO_KINDS = ("macro",)
# Frameworks the "also matches pages in" note names before "and N more"
AMBIGUITY_FRAMEWORKS_SHOWN = 8

# Meilisearch v1.49 never matches a filter string longer than this
# (MAX_FACET_VALUE_LENGTH = 500 - 32 bytes), so longer file paths can't be looked up. It
# measures the value normalized (filter_value_bytes), as the indexer checks it
# (scripts/index_to_meilisearch.py)
MAX_FILTER_VALUE_BYTES = 468

# Health check thresholds
MINIMUM_EXPECTED_DOCS = int(os.getenv("MIN_EXPECTED_DOCS", "363000"))
EXPECTED_FULL_INDEX_SIZE = int(os.getenv("EXPECTED_FULL_INDEX_SIZE", "404000"))

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

# The live index's filterable attributes (filterable_attributes), refreshed after the
# framework cache's TTL: a rebuild by swap brings a new indexer's fields
_filterable_cache: Optional[List[str]] = None
_filterable_cache_time: float = 0
# After a failed read, when to try again (the error is logged once until a read succeeds)
_filterable_retry_at: float = 0
_filterable_failing = False
FILTERABLE_RETRY_SECONDS = 30.0

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


def filterable_attributes() -> List[str]:
    """The live index's filterable attributes, cached for _frameworks_cache_ttl ([] when
    they can't be read; a failed refresh keeps the last ones read, and the next read is
    FILTERABLE_RETRY_SECONDS later).

    A new server starts beside an index the previous indexer built until its rebuild is
    swapped in (UNPREFIXED_NAME_FIELD comes with PROCESSOR_VERSION 5), and a filter on an
    attribute the index can't filter fails the whole search."""
    global _filterable_cache, _filterable_cache_time, _filterable_retry_at, _filterable_failing
    now = time.time()
    if _filterable_cache is not None and now - _filterable_cache_time < _frameworks_cache_ttl:
        return _filterable_cache
    client = meili_client
    if client is None or now < _filterable_retry_at:
        return _filterable_cache or []
    try:
        # Not meili_index: a GET on the index object the searches share drops its
        # Content-Type header (see health_check)
        index = client.index(INDEX_NAME)
        settings: List[Any] = _with_retries("settings fetch", index.get_filterable_attributes, 0)
    except Exception as e:
        # Tried again after FILTERABLE_RETRY_SECONDS, not on every search
        _filterable_retry_at = now + FILTERABLE_RETRY_SECONDS
        if not _filterable_failing:
            logger.error(f"Failed to get filterable attributes (retrying every {FILTERABLE_RETRY_SECONDS:.0f} s): {e}")
        _filterable_failing = True
        return _filterable_cache or []
    _filterable_failing = False
    attributes: List[str] = []
    for setting in settings or []:
        # Meilisearch lists a setting with features as {"attributePatterns": [...], ...}
        attributes += [setting] if isinstance(setting, str) else list(setting.get("attributePatterns") or [])
    _filterable_cache, _filterable_cache_time = attributes, time.time()
    return attributes


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

def framework_key(text: str) -> str:
    """A framework name or query word compared as letters and digits, ignoring case."""
    return re.sub(r"[\W_]", "", text.lower())


def framework_names(framework: str) -> List[str]:
    """The names a query can call a framework value by: the value, and each part of a
    nested module's or package's ('CareKit/CareKitStore': CareKit and CareKitStore;
    'swift-log/Logging': swift-log and Logging)."""
    return [framework] + (framework.split("/") if "/" in framework else [])


def without_framework_words(query: str, framework: str) -> str:
    """query without the words that name framework (framework_names), in one word or
    several ('SwiftUI' for SwiftUI, 'Core Data' for CoreData, 'App Intents' for AppIntents,
    'CareKit' for CareKit/CareKitStore; letters and digits compared, ignoring case), or all
    of it when nothing else is left."""
    for name in framework_names(framework):
        query = _without_name_words(query, framework_key(name))
    return query


def _without_name_words(query: str, name_key: str) -> str:
    """query without the runs of words whose keys join into name_key, or all of it when
    nothing else is left."""
    words = query.split()
    keys = [framework_key(word) for word in words]
    kept: List[str] = []
    start = 0
    while start < len(words):
        joined, end = "", 0
        for i in range(start, len(words)):
            joined += keys[i]
            if not keys[i] or not name_key.startswith(joined):
                break
            if joined == name_key:
                end = i + 1
                break
        if end:
            start = end
        else:
            kept.append(words[start])
            start += 1
    return " ".join(kept or words)


# The most words a framework's name is typed in ('Core Data', 'App Intents',
# 'Swift Argument Parser' for swift-argument-parser)
FRAMEWORK_NAME_MAX_WORDS = 4


def named_frameworks(query: str) -> Tuple[str, List[str]]:
    """The frameworks a query of several words names, and the rest of it: a run of one to
    FRAMEWORK_NAME_MAX_WORDS words that spells a framework value or one of its names
    (framework_names, compared as framework_key; the longest run from each word), every
    framework of that name ('CareKit OCKTask' -> ('OCKTask', ['CareKit/CareKitStore',
    'CareKit/CareKitUI', …]), 'WidgetKit timeline provider' -> ('timeline provider',
    ['WidgetKit'])). The query and no frameworks when it is one word, names none, or
    holds nothing else."""
    words = query.split()
    if len(words) < 2:
        return query, []
    names: Dict[str, List[str]] = defaultdict(list)
    for value in get_framework_counts():
        for name in framework_names(value):
            if framework_key(name):
                names[framework_key(name)].append(value)
    keys = [framework_key(word) for word in words]
    kept: List[str] = []
    named: List[str] = []
    start = 0
    while start < len(words):
        joined, end = "", 0
        for i in range(start, min(len(words), start + FRAMEWORK_NAME_MAX_WORDS)):
            if not keys[i]:
                break
            joined += keys[i]
            if joined in names:
                end = i + 1
        if end:
            named += names["".join(keys[start:end])]
            start = end
        else:
            kept.append(words[start])
            start += 1
    if not kept:
        return query, []
    return " ".join(kept), sorted(set(named))


def strip_sigils(text: str) -> str:
    """text without the '@' or '#' starting its words ('@State' -> 'State', '#Preview' ->
    'Preview'): SIGIL_RE."""
    return SIGIL_RE.sub("", text)


def sigil_kinds(text: str) -> Tuple[str, ...]:
    """The kinds a name text writes with '@' or '#' can be: ATTRIBUTE_KINDS for '@Name',
    MACRO_KINDS for '#Name' only, () without either (SIGIL_RE)."""
    sigils = {match.group(0) for match in SIGIL_RE.finditer(text)}
    return ATTRIBUTE_KINDS if "@" in sigils else MACRO_KINDS if sigils else ()


def kinds_filter(kinds: Tuple[str, ...]) -> str:
    """The filter for pages of these kinds."""
    return "kind IN [" + ", ".join(f'"{kind}"' for kind in kinds) + "]"


def title_boost(title: str, name: str, kind: str = "", sigil: Tuple[str, ...] = ()) -> float:
    """The boost for a page whose title is name: case and all (any case when name is all
    lowercase), ignoring case, or a function of that name (name(...)).

    sigil: the kinds the query's name can be when it wrote it '@Name' or '#Name'
    (sigil_kinds): no other symbol gets a boost (a page that is no symbol still can),
    and a macro titled 'Name(…)' is that name ('@Model' is SwiftData's Model())."""
    if sigil:
        if kind not in sigil + NON_SYMBOL_KINDS:
            return 0.0
        if kind == "macro" and title.lower().startswith(name.lower() + "("):
            return TITLE_EXACT_BOOST if title.startswith(name + "(") else TITLE_NOCASE_BOOST
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

    Names are compared without a leading '@' or '#' ('@State'), and then only a page of
    the kinds such a name can be, or one that is no symbol, is named (sigil_kinds,
    title_boost). A member the query names after its type ('Product.purchase': the hit's
    '_dotted', NamedPages) is boosted as a title that is the name but for case when that
    is the whole query, else as a named symbol. A multi-word query that names no page
    gives the pages whose title holds most of its words a small boost (title_words_boost).
    """
    ranking = float(hit.get("_rankingScore") or 0.0)
    title = str(hit.get("title", ""))
    kind = str(hit.get("kind", ""))
    sigil = sigil_kinds(query)
    rest = strip_sigils(without_framework_words(query, str(hit.get("framework", ""))))
    boost = title_boost(title, rest, kind, sigil)
    if asked.strip():
        boost = max(boost, title_boost(title.rstrip("?"), strip_sigils(asked.strip().rstrip("?")), kind, sigil))
    if hit.get("_dotted"):
        boost = max(boost, TITLE_NOCASE_BOOST if hit["_dotted"] == "whole" else NAMED_SYMBOL_BOOST)
    if not boost and not (sigil and kind not in sigil):
        boost = named_symbol_boost(hit, rest.split(), strip_sigils(asked.strip() or query))
    if not boost and deprecation_matches(str(hit.get("deprecation") or ""), query):
        ranking *= DEPRECATED_RANKING_FACTOR
    if not boost and len(query.split()) > 1:
        boost = title_words_boost(hit, rest)
    # Rounded, so that hits Meilisearch ranks alike compare equal (see rank_hits)
    return round(ranking * (1 - TITLE_BOOST_MAX) + boost, 6)


def title_word_match(query_word: str, title_word: str) -> bool:
    """Whether a query word is a title's word, or the same but for a short ending
    (TITLE_WORD_ENDING letters: bar/bars, request/requesting, notification/notifications),
    the shorter one of at least TITLE_WORD_MIN letters: shorter words (the 's' of "user's",
    'ML', 'to') match the titles of too many unrelated pages (measured: a how-to question's
    page fell behind one titled "…a user's location history")."""
    short, long = sorted((query_word, title_word), key=len)
    return len(short) >= TITLE_WORD_MIN and long.startswith(short) and len(long) - len(short) <= TITLE_WORD_ENDING


def title_words_share(title: str, query: str) -> float:
    """The share of a query's words (QUESTION_STOP_WORDS left out; 0 for fewer than two)
    that title holds (title_word_match), its CamelCase names split into words
    ('TimelineProvider' holds 'timeline' and 'provider')."""
    words = [word for word in re.findall(r"\w+", query.lower()) if word not in QUESTION_STOP_WORDS]
    if len(words) < 2:
        return 0.0
    title_words = re.findall(r"[a-z0-9_]+", re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", title).lower())
    return sum(any(title_word_match(word, title_word) for title_word in title_words) for word in words) / len(words)


def title_words_boost(hit: Dict, query: str) -> float:
    """TITLE_WORDS_BOOST times the share of query's words the hit's title holds
    (title_words_share), when that is at least TITLE_WORDS_MIN_SHARE; a symbol's title is
    its api_name ('requestWhenInUseAuthorization', not its argument labels), else 0."""
    kind = str(hit.get("kind", ""))
    title = str(hit.get("title", ""))
    name = title if kind in NON_SYMBOL_KINDS else str(hit.get("api_name") or title)
    share = title_words_share(name, query)
    return TITLE_WORDS_BOOST * share if share >= TITLE_WORDS_MIN_SHARE else 0.0


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


# The fields of a symbol lookup's candidates (symbol_candidates)
SYMBOL_FIELDS = ["title", "framework", "kind", "url", "file_path", "api_name", "platforms"]


def symbol_candidates(name: str, framework: str = "",
                      kinds_filter: str = TYPE_KINDS_FILTER) -> Tuple[List[Dict[str, Any]], List[str]]:
    """The pages expand_result's symbol lookup chooses from, one hit per page: the types
    whose api_name is name (ignoring case; the kinds of kinds_filter), the other pages named
    so, then the top matches for name (SYMBOL_CANDIDATES of each), within framework when
    given. Also, without a framework, every framework that has a page whose api_name is
    name (its pages can outnumber the candidates: 'init' names ~24,000)."""
    if not searchable_filter_value(framework):
        return [], []
    base = [f'framework = "{escape_filter_value(framework)}"'] if framework else []
    named = api_name_filter(name)
    # No page is named with a backslash, and a search can't filter on one
    searches = [base + [named, kinds_filter], base + [named], base] if searchable_filter_value(name) else [base]
    candidates: List[Dict[str, Any]] = []
    frameworks: List[str] = []
    seen = set()
    for filters in searches:
        params: Dict[str, Any] = {
            "limit": SYMBOL_CANDIDATES,
            "attributesToRetrieve": SYMBOL_FIELDS,
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


def generality(hit: Dict[str, Any]) -> Tuple[int, int, int]:
    """A sort key for pages that otherwise tie, the more general first: the shallower path
    within its framework, then the shorter (a type before its members, a base class's
    method before a subclass's override; Foundation Models' LanguageModelSession before
    the Python SDK's api/session), then the page available on more platforms
    (Foundation's UserDefaults before TVMLKit JS's, UIKit's viewDidLoad() before
    AppKit's). The whole path would favor the framework with the shorter directory name."""
    in_framework = str(hit.get("file_path", "")).split("/", 2)[-1]
    return in_framework.count("/"), len(in_framework), -len(hit.get("platforms") or [])


def pick_symbol(candidates: List[Dict[str, Any]], name: str,
                sigil: Tuple[str, ...] = ()) -> Optional[Dict[str, Any]]:
    """The candidate that is name's page, or None.

    In order: an exact, case-sensitive title ('Button' over 'Button tags'), that name's
    function page ('withAnimation' -> 'withAnimation(_:_:)'), then the looser
    case-insensitive matches. Among the candidates of the first of these that has any: a
    type before a member, then the shortest title (the simplest overload), then the more
    general page (generality), then the candidates' order.

    sigil: the kinds name can be when it was written '@Name' or '#Name' (sigil_kinds):
    only a candidate of these can be its page, and a macro titled 'Name(…)' is the exact
    name ('@Model' -> SwiftData's Model()).
    """
    lower = name.lower()
    if sigil:
        candidates = [h for h in candidates if h.get("kind") in sigil]
    tiers: List[Callable[[Dict[str, Any]], bool]] = [
        lambda h: h.get("title", "") == name or (
            bool(sigil) and h.get("kind") == "macro" and h.get("title", "").startswith(name + "(")),
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
    relevant hits go a deprecated page after the others (RealityKit's deprecated
    accessibilityLabel after the current ones), then the more general page first
    (generality), then in Meilisearch's order."""
    return sorted(hits, key=lambda hit: (hit.get('_case_rank', 0), -hit['_relevance'], bool(hit.get("deprecated")),
                                         *generality(hit)))


def parent_name(file_path: str) -> str:
    """The name of the directory a page is in, within its framework's ('product' for
    StoreKit/product/purchase(options).md), without the language and kind suffix Apple
    gives a directory when two symbols share its name ('text-swift.struct' -> 'text'); for
    a page at its framework's root, the framework's ('SwiftUI.Text' names SwiftUI/text.md)."""
    parts = file_path.split("/")
    if len(parts) < 3:
        return ""
    return KIND_DIRECTORY_SUFFIX_RE.sub("", parts[-2].lower())


def dotted_member_pages(token: str, filters: List[str], params: Dict[str, Any]) -> List[Dict[str, Any]]:
    """The pages a dotted name names ('Product.purchase', 'DispatchQueue.main.async'): the
    pages whose api_name is its last component and whose directory (parent_name) is one
    of the others, from the top SYMBOL_CANDIDATES matches for its components as words,
    within the filters (params: the search's other parameters). Each is scored as a page
    named after the member is (its _rankingScore from a search for that name within
    those pages), not by the type's name, which their text may not hold."""
    parts = token.split(".")
    member, parents = parts[-1], {part.lower() for part in parts[:-1]}
    if not searchable_filter_value(member):
        return []
    # Only their paths: the pages under a parent are fetched whole by the second search
    candidates = safe_search(" ".join(parts), {"limit": SYMBOL_CANDIDATES, "attributesToRetrieve": ["file_path"],
                                               "distinct": "file_path",
                                               "filter": " AND ".join(filters + [api_name_filter(member)])})
    paths = [str(hit.get("file_path", "")) for hit in candidates.get("hits", [])
             if parent_name(str(hit.get("file_path", ""))) in parents]
    paths = [path for path in paths
             if searchable_filter_value(path) and filter_value_bytes(path) <= MAX_FILTER_VALUE_BYTES]
    if not paths:
        return []
    values = ", ".join(f'"{escape_filter_value(path, max_length=None)}"' for path in paths)
    return list(safe_search(member, dict(params, limit=len(paths),
                                         filter=" AND ".join(filters + [f"file_path IN [{values}]"]))).get("hits", []))


def unprefixed_type_pages(names: List[str], filters: List[str], params: Dict[str, Any]) -> List[Dict[str, Any]]:
    """The types whose name without its prefix (UNPREFIXED_NAME_FIELD) is one of names,
    ignoring case, within the filters (at most SYMBOL_CANDIDATES; params: the search's
    other parameters)."""
    names = [name for name in dict.fromkeys(names) if name and searchable_filter_value(name)]
    if not names or UNPREFIXED_NAME_FIELD not in filterable_attributes():
        # (An index built before the field: none of its types is found so)
        return []
    values = ", ".join(f'"{escape_filter_value(name, max_length=None)}"' for name in names)
    flt = " AND ".join(filters + [f"{UNPREFIXED_NAME_FIELD} IN [{values}]", TYPE_KINDS_FILTER])
    return list(safe_search("", dict(params, limit=SYMBOL_CANDIDATES, filter=flt)).get("hits", []))


def framework_filter(frameworks: List[str]) -> List[str]:
    """The filter for pages in any of frameworks ([] for none)."""
    if not frameworks:
        return []
    return ["framework IN [" + ", ".join(f'"{escape_filter_value(name)}"' for name in frameworks) + "]"]


def choose_part(hit: Dict[str, Any], query: str, with_content: bool) -> None:
    """A result from a page in several parts shows the part that best matches query.

    Search keeps one document per page (distinct), the first of those it scores alike, and
    every part carries the page's title, so a query holding the title's words ('in-app
    purchase App Store review guidelines') scores many parts alike. So the page's parts
    are searched for query and for its words the title doesn't hold (their scores only),
    and the hit becomes the part with the best score (to 0.01), then the best for those
    words, then the first. A part differs from the others only by its content (the
    indexer copies the page's fields to each), which is fetched by its id when the
    result shows it (with_content: not summary_mode)."""
    total = hit.get("total_chunks")
    path = str(hit.get("file_path", ""))
    if not (isinstance(total, int) and total > 1):
        return
    title_words = set(re.findall(r"\w+", str(hit.get("title", "")).lower()))
    words = [word for word in re.findall(r"\w+", strip_sigils(query).lower()) if word not in title_words]
    if not words or not searchable_filter_value(path) or filter_value_bytes(path) > MAX_FILTER_VALUE_BYTES:
        return
    params: Dict[str, Any] = {"limit": total, "filter": f'file_path = "{escape_filter_value(path, max_length=None)}"',
                              "showRankingScore": True, "attributesToRetrieve": ["chunk_index", "id"]}
    try:
        parts = safe_search(query, params).get("hits", [])
        rest = {part.get("chunk_index"): float(part.get("_rankingScore") or 0.0)
                for part in safe_search(" ".join(words), params).get("hits", [])}
        if not parts:
            return
        best = max(parts, key=lambda part: (round(float(part.get("_rankingScore") or 0.0), 2),
                                            rest.get(part.get("chunk_index"), 0.0), -int(part.get("chunk_index") or 0)))
        if best.get("chunk_index") == hit.get("chunk_index"):
            return
        if with_content:
            documents = safe_get_documents({"ids": [best.get("id")], "fields": ["content", "chunk_index"]})
            chosen = [dict(doc) for doc in documents.results]
            if not chosen or chosen[0].get("chunk_index") != best.get("chunk_index"):
                return
            hit["content"] = chosen[0].get("content", "")
    except Exception as e:
        # The part search already found stays shown
        logger.error(f"Part search failed for '{query}' in {path}: {e}")
        return
    hit["chunk_index"] = best.get("chunk_index")


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


def without_disambiguation(path: str) -> str:
    """A page path without the DocC disambiguation suffix ending its file name
    ('…/text/init(_)-1a4oh.md' -> '…/text/init(_).md'; DISAMBIGUATION_SUFFIX_RE), else
    path as it is.

    Apple lists every overload of a symbol on its group page, and links to each by its
    suffixed path, but the preferred overload has no page of its own: its content is the
    group page, at the unsuffixed path. So a suffixed path that isn't in the docs falls
    back to that page (link_hints, expand_result)."""
    folder, slash, name = path.rpartition("/")
    match = DISAMBIGUATION_SUFFIX_RE.match(name)
    if match and (match.group(1).endswith(")") or any(char.isdigit() for char in match.group(2))):
        return f"{folder}{slash}{match.group(1)}.md"
    return path


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
    return link_hints(content, file_path)[0]


def link_hints(content: str, file_path: str) -> Tuple[str, List[Tuple[int, int]]]:
    """transform_internal_links' text, and where each local link went in it: the (start,
    end) of its hint, or of the link itself when it stays (summary_text cuts neither)."""
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
        # A link to an overload the scraper wrote no page for: its group's preferred one
        for candidate in candidates:
            unsuffixed = without_disambiguation(candidate)
            page = local_page(unsuffixed) if unsuffixed != candidate else None
            if page:
                return f"{text} (-> expand_result: {page})"
        # The path's names, without a file-relative link's "." and ".." segments (the path
        # itself when it has no other) and without a disambiguation suffix, which no page's
        # text holds
        path = without_disambiguation(target).replace('.md', '')
        names = [name for name in path.split('/') if name not in ('', '.', '..')] or [path]
        search_term = ' '.join(names).replace('-', ' ')
        return f"{text} (-> search: {' '.join(search_term.split())})"

    pieces: List[str] = []
    spans: List[Tuple[int, int]] = []
    length = last = 0
    for match in LOCAL_LINK_RE.finditer(content):
        hint = replace_link(match)
        start = length + match.start() - last
        pieces += [content[last:match.start()], hint]
        spans.append((start, start + len(hint)))
        length, last = start + len(hint), match.end()
    pieces.append(content[last:])
    return "".join(pieces), spans


def summary_text(overview: str, file_path: str, max_chars: int = SUMMARY_CHARS) -> str:
    """A summary_mode result's overview: its local links made hints (transform_internal_links),
    then cut to max_chars, never inside a hint or a link (half of one is neither), and
    without a link the indexer's own cut left unclosed at its end."""
    text, spans = link_hints(overview, file_path)
    if len(text) > max_chars:
        spans += [match.span() for match in MARKDOWN_LINK_RE.finditer(text)]
        cut = max_chars
        while any(start < cut < end for start, end in spans):
            cut = min(start for start, end in spans if start < cut < end)
        text = text[:cut]
    return UNCLOSED_LINK_RE.sub("", text.rstrip()).rstrip()


def pushed_down_headings(content: str) -> bool:
    """Whether a page has the DocC layout of render versions before 5, which wrote Apple's
    content headings two levels down: its level-2 ones (Overview, Discussion, Return Value,
    or an article's own) at '####', as siblings of the converter's '## Declaration' and
    '## Mentions'. Such a page has '#### Overview', '#### Discussion' or '#### Return
    Value', or a '####' heading right after one of the sections the converter writes
    before the content (DOCC_LEADING_SECTIONS): Apple's content starts at level 2, so in
    the current layout a '## ' heading follows them."""
    previous: Tuple[int, str] = (0, "")
    for match in HEADING_LINE_RE.finditer(content):
        level, name = len(match.group(1)), match.group(2)
        if level == 4 and (name in DOCC_CONTENT_HEADINGS
                           or (previous[0] == 2 and previous[1] in DOCC_LEADING_SECTIONS)):
            return True
        previous = (level, name)
    return False


def extract_section(content: str, section_name: str) -> str:
    """A section of a page: the text under its heading, a line of level 2-6 (the '# ' line
    is the page's title: a property named 'parameters' would give its whole page), up to
    the next heading of the same or a higher level.

    Level-1 lines end no section: after the title they are comments in code. On a page in
    the older DocC layout (pushed_down_headings), a level-2 section also ends at a '####'
    heading: Apple's level-2 content headings (Overview, Discussion, Return Value) are at
    that level, as siblings that follow '## Declaration' and '## Mentions'. So '## Topics'
    keeps its '###' groups, and '#### Overview' its '#####' subsections. Unless its '####'
    headings are its children: when its first sub-heading is a '###', or a '####' with no
    text before it, a level-2 section runs to the next '## '. On any other page (the
    current DocC layout, where '## Overview' holds Apple's level-4 '####' headings, and
    the other sources' pages: HIG's '## Platform considerations' / '### macOS' / '#### …')
    a section holds every deeper heading."""
    name = re.escape(section_name.replace('_', ' ').title())
    heading = re.search(rf'^(#{{2,6}})[ \t]*{name}[ \t]*$', content, re.MULTILINE | re.IGNORECASE)
    if not heading:
        return ""
    level = len(heading.group(1))
    body = content[heading.end():]
    end = rf'^#{{2,{level}}}\s'
    if level == 2 and pushed_down_headings(content):
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


def link_url(url: str) -> str:
    """A result's URL as a markdown link holds it: every character a URL can't hold as it is
    percent-encoded (a space ends a link's destination: sourcekit-lsp's "Configuration
    File.md"), and its parentheses too when they don't pair up (Apple cuts a long symbol's
    URL inside its argument list, and an unclosed "(" leaves no link). Paired ones stay, as
    in Apple's URLs (init(_:)). The index's URL, as the scraper wrote it, is left as it is."""
    url = quote(url, safe=URL_SAFE_CHARACTERS)
    depth = 0
    for char in url:
        depth += {"(": 1, ")": -1}.get(char, 0)
        if depth < 0:
            break
    if depth:
        url = url.replace("(", "%28").replace(")", "%29")
    return url


def page_title(hit: Dict[str, Any]) -> str:
    """A page's title, as indexed; its file name for a page indexed without one (by an
    indexer before PROCESSOR_VERSION 4: a README that starts at '## ')."""
    name = posixpath.basename(str(hit.get("file_path") or "")).removesuffix(".md")
    return str(hit.get("title") or "") or name or "Untitled"


def page_sections(content: str) -> List[str]:
    """The sections of a page expand_result's sections can name: its headings of level
    2-6 outside code, lowercased with '_' for spaces (as in 'platform_considerations'),
    each once, in page order."""
    names: List[str] = []
    fence = ""  # the open code block's fence character, "" outside one
    for line in content.split("\n"):
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)[0]
            fence = "" if fence == marker else fence or marker
            continue
        heading = None if fence else HEADING_LINE_RE.match(line)
        if heading:
            name = "_".join(heading.group(2).lower().split())
            if name not in names:
                names.append(name)
    return names


def link_label(url: str) -> str:
    """A result link's label, named by the URL's host: "View on Apple Developer" only for
    Apple's own pages (the index also holds GitHub, MLX and coremltools docs)."""
    host = (urlsplit(url).hostname or "").removeprefix("www.")
    return f"View on {LINK_HOST_NAMES.get(host, host or 'source')}"


def unprefixed_relevance() -> float:
    """The relevance of a type found by its name without its prefix (UNPREFIXED_NAME_FIELD):
    a title that is the name but for case, with a full score (after a page titled with the
    name itself, before every other page)."""
    return round((1 - TITLE_BOOST_MAX) + UNPREFIXED_NAME_BOOST, 6)


class NamedPages:
    """The pages a (non-wildcard) query names that its top matches can miss, joined to them.

    Meilisearch matches words: a name the query spells differently from the index (as
    words, with '@', after its type, without its prefix), or a common name whose pages it
    scores alike, can leave the page asked for out of the top matches or below pages that
    hold the words apart. Each lookup searches for that name within the search's filters
    and, when the query names frameworks ('CareKit OCKTask', 'Metal device':
    named_frameworks), within them, using the rest of the query as the name:

    - a one-word name: the types (and, written '@Name' / '#Name', the macros) named so
      (only when the top matches were cut, or the query named a framework);
    - a name typed as words ('async image'): the types and frameworks it spells
      (spelled_name; scored by spelled_relevance), and with a framework named, also the
      whole query's ('photos picker' -> PhotosPicker, 'Translation session');
    - a one-word '@name' no type or macro has ('@escaping', '@objc'): a built-in
      attribute, which Swift's book documents, so 'name attribute' is searched instead;
    - 'Type.member' ('Product.purchase', 'DispatchQueue.main.async'): the member's pages
      under the type (dotted_member_pages; '_dotted' for calculate_relevance_score);
    - with a framework (the search's or named), the types named so without their prefix
      ('Button' in UIKit -> UIButton; '_unprefixed', unprefixed_relevance).

    hits: the top matches, joined by the pages found; added: what joined them, for the
    results' total; attribute_search: the search run instead, if any."""

    def __init__(self, hits: List[Dict[str, Any]], query: str, filters: List[str],
                 search_params: Dict[str, Any], framework_given: bool) -> None:
        self.hits = hits
        self.query = query
        self.filters = filters
        self.search_params = search_params
        self.framework_given = framework_given
        self.added: List[str] = []
        self.attribute_search = ""
        self.rest, self.frameworks = named_frameworks(query)
        self.name = strip_sigils(self.rest)
        self.sigil = sigil_kinds(self.rest)
        self.in_frameworks = self.filters + framework_filter(self.frameworks)
        self.position = {hit.get("file_path"): i for i, hit in enumerate(hits)}

    def search(self, query: str, filters: List[str], limit: int = SYMBOL_CANDIDATES) -> List[Dict[str, Any]]:
        params = dict(self.search_params, limit=limit)
        params.pop("filter", None)
        if filters:
            params["filter"] = " AND ".join(filters)
        return list(safe_search(query, params).get("hits", []))

    def join(self, hit: Dict[str, Any], replace: bool = False) -> bool:
        """Add hit unless its page is there (replace: put it in that page's place);
        whether it was added."""
        path = hit.get("file_path")
        if path in self.position:
            if replace:
                self.hits[self.position[path]] = hit
            return False
        self.position[path] = len(self.hits)
        self.hits.append(hit)
        return True

    def join_all(self, window_full: bool) -> None:
        # Words with an '@' spell no name (spelled_name), as words with any other character
        spelled = spelled_name(self.rest)
        one_word = bool(re.fullmatch(r"\w+", self.name))
        if one_word and (window_full or self.frameworks):
            self.join_types()
        elif spelled:
            self.join_spelled(spelled, self.in_frameworks)
        whole = spelled_name(self.query)
        if self.frameworks and whole and whole != spelled:
            self.join_spelled(whole, self.filters)
        if re.fullmatch(r"@\w+", self.rest.strip()):
            self.attribute_instead()
        for token in list(dict.fromkeys(DOTTED_NAME_RE.findall(self.name)))[:DOTTED_NAMES_MAX]:
            self.join_dotted(token)
        if self.framework_given or self.frameworks:
            names = [self.name if one_word else spelled] + ([whole] if self.frameworks else [])
            self.join_unprefixed([name for name in names if name])

    def join_types(self) -> None:
        # Meilisearch scores every page with the word as its title alike, in index order:
        # for a common name (String, Data, Color, State) the type's own page can be past
        # the top matches, so the types named so join them
        kinds = kinds_filter(self.sigil) if self.sigil else TYPE_KINDS_FILTER
        joined = [self.join(hit) for hit in self.search(
            self.name, self.in_frameworks + [api_name_filter(self.name), kinds])]
        if any(joined):
            self.added.append(f"the {'symbols' if self.sigil else 'types'} named '{self.name}'")

    def join_spelled(self, spelled: str, filters: List[str]) -> None:
        # A name typed as words ('vision entitlement services', 'async image') is one word
        # in the index (Meilisearch doesn't split CamelCase), which the words match only
        # joined, and its typo rule counts each joined word as a typo: every page holding
        # the words apart outranks the named page, even within the top matches. So the
        # types and frameworks named what the words spell are searched by that name, and
        # replace or join the top matches (spelled_relevance)
        joined = False
        for hit in self.search(spelled, filters + [api_name_filter(spelled)]):
            if spells_title(str(hit.get("title", "")), spelled):
                hit["_spelled"] = True
                joined = self.join(hit, replace=True) or joined
        if joined:
            self.added.append(f"the pages named '{spelled}'")

    def attribute_instead(self) -> None:
        # '@name' that declares nothing in the docs is one of Swift's built-in attributes
        name = self.name.strip()
        if any(str(hit.get("api_name", "")).lower() == name.lower() and hit.get("kind") in ATTRIBUTE_KINDS
               for hit in self.hits):
            return
        search = f"{name} {ATTRIBUTE_SEARCH_WORD}"
        hits = self.search(search, self.filters, limit=int(self.search_params.get("limit") or SYMBOL_CANDIDATES))
        if hits:
            self.hits = hits
            self.position = {hit.get("file_path"): i for i, hit in enumerate(hits)}
            self.added = []
            self.attribute_search = search

    def join_dotted(self, token: str) -> None:
        # 'Type.member': Meilisearch splits the dot into words, so every page holding both
        # ranks alike (Product.PurchaseError before purchase(options:))
        flag = "whole" if self.name.strip() == token else "part"
        joined = False
        for hit in dotted_member_pages(token, self.in_frameworks, self.search_params):
            path = hit.get("file_path")
            if path in self.position:
                known = self.hits[self.position[path]]
                if known.get("_dotted") != "whole":
                    known["_dotted"] = flag
            else:
                hit["_dotted"] = flag
                joined = self.join(hit) or joined
        if joined:
            self.added.append(f"the members '{token}' names")

    def join_unprefixed(self, names: List[str]) -> None:
        joined = False
        for hit in unprefixed_type_pages(names, self.in_frameworks, self.search_params):
            path = hit.get("file_path")
            if path in self.position:
                self.hits[self.position[path]]["_unprefixed"] = True
            else:
                hit["_unprefixed"] = True
                joined = self.join(hit) or joined
        if joined:
            self.added.append("the types named " + " or ".join(f"'{name}'" for name in dict.fromkeys(names))
                              + " after a prefix")


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
        platform: Filter by platform: 'ios', 'ipados', 'macos', 'mac catalyst', 'tvos', 'watchos',
            'visionos', or 'all'
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
    wildcard_kinds: Tuple[str, ...] = ()  # the kinds a pattern written '@State*' can match

    if has_wildcards:
        # '@State*', '#Preview?': the names without the sigil, of the kinds so written
        wildcard_kinds = sigil_kinds(query)
        query = strip_sigils(query)
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

    # Build Meilisearch filter
    filters = []
    if framework:
        filters.append(f'framework = "{escape_filter_value(framework)}"')
    if platform_filter:
        filters.append(f'platforms = "{escape_filter_value(platform_filter)}"')
    if not (searchable_filter_value(framework) and searchable_filter_value(platform_filter)) or (
            platform_filter and platform_filter not in [name.lower() for name in PLATFORMS]):
        # No framework or platform has a backslash, and a search can't filter on one; a
        # platform no page has matches nothing (the reply names the platforms)
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
    added: List[str] = []  # the pages named by the query that joined the top matches
    attribute_search = ""  # the search a built-in attribute's name ran instead (NamedPages)
    try:
        results = safe_search(query, search_params)
        hits = results.get("hits", [])
        window_full = len(hits) >= window

        if has_wildcards and wildcard_pattern and same_case_pattern:
            # The pattern's literal text, searched as words, finds a name like
            # UIViewController (one word) only by its first letters, so the top matches
            # are joined by the pages whose name starts with the pattern's prefix
            kinds = [kinds_filter(wildcard_kinds)] if wildcard_kinds else []
            hits = wildcard_matches([hit for hit in hits if not wildcard_kinds or hit.get("kind") in wildcard_kinds],
                                    wildcard_pattern, same_case_pattern, literal_chars)
            if len(name_prefix) >= WILDCARD_PREFIX_MIN:
                listed, names_total = list_names_by_prefix(name_prefix, filters + kinds)
                seen = {hit.get("file_path") for hit in hits}
                for doc in wildcard_matches(listed, wildcard_pattern, same_case_pattern, literal_chars):
                    if doc.get("file_path") not in seen:
                        seen.add(doc.get("file_path"))
                        hits.append(dict(doc, _listed=True))
        else:
            named_pages = NamedPages(hits, query, filters, search_params, bool(framework))
            named_pages.join_all(window_full)
            hits, added, attribute_search = named_pages.hits, named_pages.added, named_pages.attribute_search
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
            if hit.get('_unprefixed'):
                score = max(score, unprefixed_relevance())
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
    if names_total:
        # Every page whose name starts with the prefix was matched, unless there were more
        added = [f"the first {WILDCARD_NAME_LIMIT:,} of the {names_total:,} names starting with '{name_prefix}'"
                 if names_capped else f"every name starting with '{name_prefix}'"]
    if window_full:
        # Matches past the top ones were never seen, unless something else found them: a
        # title such as 'Publishers.Map' (api_name 'Map') comes only from the top matches
        total_text += f" (ranked from the top {window} matches" + "".join(f" and {part}" for part in added) + ")"
    elif names_capped:
        total_text += f" (matched against {added[0]})"

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
    if attribute_search:
        name = attribute_search.split()[0]
        output.append(f"No type or macro is named '{name}': results for '{attribute_search}' "
                      "(Swift's built-in attributes are documented in The Swift Programming Language)")
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
        if not has_wildcards:
            # Only for a result written out (choose_part's searches)
            choose_part(hit, query, not summary_mode)
        result_lines = []
        relevance = hit.get('_relevance', 0)

        result_lines.append(f"## {rank}. {page_title(hit)} ({int(relevance * 100)}%)")
        # A hit from a long page is one of its parts: expand_result's part reads it
        part = part_label(hit)
        result_lines.append(f"Framework: {hit.get('framework', 'Unknown')} | Type: {hit.get('kind', '')}"
                            + (" | Deprecated" if hit.get("deprecated") else "")
                            + (f" | {part}" if part else ""))
        if hit.get("file_path"):
            result_lines.append(f"Path: `{hit.get('file_path')}`")
        if hit.get("url"):
            result_lines.append(f"[{link_label(hit['url'])}]({link_url(hit['url'])})")
        result_lines.append("")

        body = ""
        if not summary_mode and hit.get("content"):
            body = transform_internal_links(hit.get("content", ""), str(hit.get("file_path", "")))
        elif hit.get("overview"):
            # Its links as hints, as the content's and the deprecation's
            body = summary_text(str(hit["overview"]), str(hit.get("file_path", "")))
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
        names = {name.lower(): name for name in get_framework_counts()}
        if names and framework.lower() not in names:
            # A name no page has (no names: the counts are unavailable, so nothing is said)
            close = difflib.get_close_matches(framework.lower(), list(names), n=FRAMEWORK_SUGGESTIONS)
            lines.append(f"   - '{framework}' is not a framework in the index"
                         + (f": did you mean {', '.join(repr(names[name]) for name in close)}?" if close else ""))
            lines.append("   - list_frameworks lists every framework's name (its query filters them)")
        lines.append("   - Try without framework filter")
    if platform and platform != "all":
        if platform.lower() not in [name.lower() for name in PLATFORMS]:
            lines.append(f"   - '{platform}' is not a platform: use one of "
                         + ", ".join(name.lower() for name in PLATFORMS) + ", or all")
        else:
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
            whole page (part is ignored); a name the page has no section for is reported with
            the names it has
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
    fallback_note = ""  # a path not in the docs, and the page shown instead

    try:
        if is_symbol:
            # '@State' and '#Preview' are State and Preview, of the kinds so written
            sigil = sigil_kinds(input_value)
            name = strip_sigils(input_value).strip() or input_value
            hits, named_frameworks = symbol_candidates(name, framework,
                                                       kinds_filter(sigil) if sigil else TYPE_KINDS_FILTER)
            match = pick_symbol(hits, name, sigil)
            if not match and not sigil and DOTTED_NAME_RE.fullmatch(name) and searchable_filter_value(framework):
                # 'Product.purchase': the member under its type (a dotted title, such as
                # 'Publishers.Map', is matched above)
                members = dotted_member_pages(name, [f'framework = "{escape_filter_value(framework)}"']
                                              if framework else [], {"attributesToRetrieve": SYMBOL_FIELDS,
                                                                     "distinct": "file_path"})
                name = name.rsplit(".", 1)[1]
                match = pick_symbol(members, name)
                if match:
                    hits, named_frameworks = members, []

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
                # (Written '@Name', only the pages of the kinds so written)
                others = sorted(({
                    h.get("framework", "") for h in hits
                    if (h.get("title", "").lower() == title
                        or h.get("title", "").lower().startswith(name.lower() + "("))
                    and (not sigil or h.get("kind") in sigil)
                } | (set() if sigil else set(named_frameworks))) - {hit.get("framework", "")})
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
            unsuffixed = without_disambiguation(relative_path)
            if not chunks and unsuffixed != relative_path:
                # An overload with no page of its own: its group's preferred one
                chunks = get_file_chunks(unsuffixed)
                if chunks:
                    fallback_note = (f"`{relative_path}` is not in the docs (an overload with no page of "
                                     f"its own): showing `{chunks[0].get('file_path', unsuffixed)}`, the page "
                                     "of that symbol's overloads.")
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
    notes = [note for note in (fallback_note, ambiguity_note) if note]

    if sections:
        # From the whole page, so a section that spans two chunks comes whole
        content = "\n".join(pieces)
        output = [f"# {page_title(chunks[0])}", ""]
        available = page_sections(content)
        missing = []
        for section in sections:
            section_content = transform_internal_links(extract_section(content, section), doc_path)
            if section_content:
                output.append(f"## {section.title()}")
                output.append(section_content)
                output.append("")
            elif "_".join(section.lower().replace("_", " ").split()) not in available:
                missing.append(section)
        if missing:
            # Name what the page has, so the next call can ask for it
            listed = ", ".join(available[:SECTIONS_LISTED]) + (
                f" and {len(available) - SECTIONS_LISTED} more" if len(available) > SECTIONS_LISTED else "")
            notes.insert(0, f"No section {', '.join(repr(name) for name in missing)} in `{doc_path}`. "
                         + (f"Its sections: {listed}." if available else
                            "It has no sections: expand_result without sections returns it whole."))
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
