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
import secrets
import time
import logging
from collections import defaultdict
from typing import Annotated, Dict, List, Optional, Any
from pathlib import Path

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
SERVER_VERSION = "3.0.2"
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

# Meilisearch v1.49 never matches a filter string longer than this
# (MAX_FACET_VALUE_LENGTH = 500 - 32 bytes), so longer file paths can't be looked up
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

# Stats cache for health check (avoid repeated Meilisearch calls)
_stats_cache: Dict[str, Any] = {"value": None, "timestamp": 0}
_stats_cache_ttl: float = 5.0  # seconds

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


def safe_search(query: str, params: dict, retries: int = MEILI_MAX_RETRIES) -> dict:
    """Execute a Meilisearch search with error handling and retry logic."""
    last_error = None

    for attempt in range(retries + 1):
        try:
            # Ensure connection is healthy
            if not ensure_meilisearch_connection():
                raise MeilisearchSetupError("Failed to establish Meilisearch connection")

            # Execute search
            result = meili_index.search(query, params)

            # Log recovery after successful retry
            if attempt > 0:
                logger.info(f"Meilisearch search recovered after {attempt} retry(ies)")

            return result

        except Exception as e:
            last_error = e
            is_retryable = _is_retryable_error(e)
            logger.warning(
                f"Meilisearch search failed (attempt {attempt + 1}/{retries + 1}): {e} "
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
    raise Exception(f"Meilisearch search failed after {retries + 1} attempts: {last_error}")


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

def calculate_relevance_score(hit: Dict, query: str, search_framework: str = "") -> float:
    """Calculate relevance score based on query match quality."""
    query_lower = query.lower()
    query_words = query_lower.split()

    title = hit.get("title", "").lower()
    api_name = hit.get("api_name", "").lower()
    overview = hit.get("overview", "").lower()
    framework = hit.get("framework", "").lower()

    score = 0.0

    # Framework matching boost
    if search_framework:
        target = search_framework.lower()
        if framework == target:
            score += 0.2
        elif target:
            score -= 0.3

    # Core component boost
    core_components = ["button", "text", "image", "view", "list", "stack",
                       "navigation", "alert", "sheet", "picker", "toggle"]
    if any(c in api_name for c in core_components):
        if len(api_name) <= 20 and "store" not in api_name:
            score += 0.1
        else:
            score -= 0.2

    # Match quality scoring
    if api_name == query_lower or title == query_lower:
        score += 1.0
    elif query_words and api_name == query_words[-1]:
        score += 0.95
    elif api_name and query_lower in api_name:
        score += 0.9
    elif all(word in title for word in query_words):
        score += 0.85
    elif query_words and query_words[-1] in title:
        score += 0.75
    elif any(word in title for word in query_words):
        score += 0.7
    elif overview and query_lower in overview:
        score += 0.6
    else:
        score += 0.4

    return max(0.0, min(1.0, score))


def estimate_tokens(text: str) -> int:
    """Estimate token count (~4 chars per token)."""
    return len(text) // 4


def transform_internal_links(content: str) -> str:
    """Transform internal markdown links to search hints."""
    def replace_link(match):
        link_text = match.group(1)
        link_path = match.group(2)
        if link_path.startswith('http'):
            return match.group(0)
        search_term = link_path.replace('.md', '').replace('/', ' ').replace('-', ' ')
        return f"{link_text} (-> search: {' '.join(search_term.split())})"

    return re.sub(r'\[([^\]]+)\]\(([^)]+\.md)\)', replace_link, content)


def extract_section(content: str, section_name: str) -> str:
    """Extract a specific section from content."""
    pattern = re.escape(section_name.replace('_', ' ').title())
    match = re.search(rf'##?\s*{pattern}\s*\n(.*?)(?=##|\Z)', content, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""


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

    Args:
        query: Search query (e.g., 'Button', 'async await', 'NavigationStack'). Wildcards: '*' matches
            any characters and '?' one character in single-word queries (e.g., 'UIView*', 'NS*Button',
            'Button?'); they filter the top matches for the literal text, so start with a literal prefix
        framework: Filter by framework (e.g., 'SwiftUI', 'UIKit', 'CarPlay')
        strict_framework: Only return results from the specified framework
        platform: Filter by platform: 'ios', 'macos', 'tvos', 'watchos', 'visionos', or 'all'
        limit: Number of results (1-20, default: 10)
        relevance_threshold: Minimum relevance score (0.0-1.0)
        token_budget: Response size limit in tokens (1000-25000, default: 5000)
        summary_mode: Return condensed summaries instead of full content
        offset: Skip N results for pagination

    Returns:
        Formatted search results with relevance scores and documentation content
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

    if has_wildcards:
        # fnmatch emits atomic groups, so a pattern can't backtrack
        # catastrophically (a hand-built '.*' per '*' let '******Q' freeze the
        # whole server). Runs of '*' collapse; '[' is escaped to stay literal.
        # Matched against lowercased fields (case-insensitive, as before).
        wildcard_pattern = re.compile(
            fnmatch.translate(re.sub(r'\*+', '*', query).lower().replace('[', '[[]'))
        )
        query = query.replace('*', ' ').replace('?', ' ').strip() or "a"

    # Build Meilisearch filter
    filters = []
    if framework:
        filters.append(f'framework = "{escape_filter_value(framework)}"')
    if platform_filter:
        filters.append(f'platforms = "{escape_filter_value(platform_filter)}"')

    # Search attributes
    attrs = ["title", "framework", "api_name", "overview", "url", "platforms", "kind", "file_path"]
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
    }
    if filters:
        search_params["filter"] = " AND ".join(filters)

    try:
        results = safe_search(query, search_params)
        hits = results.get("hits", [])
    except Exception as e:
        logger.error(f"Search failed for query '{query}': {e}")
        raise ToolError("Search temporarily unavailable. Please try again in a moment.") from e

    window_full = len(hits) >= window

    # Apply wildcard filter
    if has_wildcards and wildcard_pattern and hits:
        hits = [h for h in hits if
                wildcard_pattern.match(h.get("api_name", "").lower()) or
                wildcard_pattern.match(h.get("title", "").lower())]

    if not hits:
        return _build_no_results_response(original_query, framework, platform if platform_filter else "", has_wildcards)

    # Score and filter results
    scored_hits = []
    for hit in hits:
        if strict_framework and framework:
            if hit.get("framework", "").lower() != framework.lower():
                continue

        score = calculate_relevance_score(hit, query, framework)
        if score >= relevance_threshold:
            hit['_relevance'] = score
            scored_hits.append(hit)

    if not scored_hits:
        if relevance_threshold > 0:
            return f"No results above relevance threshold {relevance_threshold}"
        return _build_no_results_response(original_query, framework, platform if platform_filter else "", has_wildcards)

    scored_hits.sort(key=lambda x: x['_relevance'], reverse=True)
    total_text = f"{len(scored_hits)} results"
    if window_full:
        total_text += f" (ranked from the top {window} matches)"

    paginated = scored_hits[offset:offset + limit]
    if not paginated:
        return f"No more results: offset {offset} is past the last of {total_text}."

    # Build output ("Showing" line is filled in once we know what fit the budget)
    output = [f"Search Results: {original_query}", ""]

    if framework:
        output.append(f"Framework: {framework}{' (strict)' if strict_framework else ''}")
    if platform_filter:
        output.append(f"Platform: {platform}")
    output.append("")

    # Reserve room for the "Showing" line and the "more results" footer, which
    # are only written after the results are chosen
    token_count = estimate_tokens("\n".join(output)) + 40
    results_included = 0
    budget_reached = False

    # Results are numbered by overall rank, so numbers continue across pages
    for rank, hit in enumerate(paginated, offset + 1):
        result_lines = []
        relevance = hit.get('_relevance', 0)

        result_lines.append(f"## {rank}. {hit.get('title', 'Untitled')} ({int(relevance * 100)}%)")
        result_lines.append(f"Framework: {hit.get('framework', 'Unknown')} | Type: {hit.get('kind', '')}")

        if hit.get("file_path"):
            result_lines.append(f"Path: `{hit.get('file_path')}`")
        if hit.get("url"):
            result_lines.append(f"[View on Apple Developer]({hit.get('url')})")
        result_lines.append("")

        body = ""
        if not summary_mode and hit.get("content"):
            body = transform_internal_links(hit.get("content", ""))
        elif hit.get("overview"):
            body = hit.get("overview", "")[:400]

        result_text = "\n".join(result_lines + ([body] if body else []) + ["\n---\n"])
        result_tokens = estimate_tokens(result_text)

        if token_count + result_tokens > token_budget:
            if results_included > 0:
                # Stop at the first result that doesn't fit, so the next
                # offset resumes exactly here (nothing skipped or repeated)
                budget_reached = True
                break
            # A single result larger than the whole budget: truncate its body
            room = (token_budget - token_count - estimate_tokens("\n".join(result_lines)) - 60) * 4
            body = body[:max(0, room)].rstrip()
            if body.count("```") % 2:
                body += "\n```"  # close a code block the cut left open
            body += (
                f"\n\n[Truncated to fit token_budget={token_budget}. "
                "Use expand_result with the Path above for the full document.]"
            )
            result_text = "\n".join(result_lines + [body, "\n---\n"])
            result_tokens = estimate_tokens(result_text)

        output.append(result_text)
        token_count += result_tokens
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
    if has_wildcards:
        lines.append("   - Try a pattern that starts with a literal prefix (e.g., UIView*, NS*Button)")
    else:
        lines.append("   - Try simpler keywords")
        lines.append("   - Use wildcards: Button* or NSTable*")
    if framework:
        lines.append("   - Try without framework filter")
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
    sections: Optional[Annotated[List[Annotated[str, Field(max_length=64)]], Field(max_length=20)]] = None
) -> str:
    """Get full documentation for a symbol or file.

    Args:
        file_path: Symbol name (e.g., 'Button') or file path from search results
        sections: Specific sections to include (e.g., ['overview', 'declaration'])

    Returns:
        Full documentation content
    """
    # Validate connection
    if not ensure_meilisearch_connection():
        raise ToolError("Unable to connect to search backend. Please try again in a moment.")

    sections = sections or []
    input_value = file_path.strip().strip('`').strip()
    if not input_value:
        raise ToolError("file_path is required")

    # Anything that isn't a path is a symbol name, including lowercase ones
    # like 'withAnimation' or 'viewDidLoad'
    is_symbol = '/' not in input_value and not input_value.lower().endswith('.md')

    try:
        if is_symbol:
            search_params = {
                "limit": 10,
                "attributesToRetrieve": ["title", "content", "framework", "kind", "url", "file_path", "api_name"]
            }

            results = safe_search(input_value, search_params)
            hits = results.get("hits", [])

            # Prefer an exact, case-sensitive title ('Button' over 'Button tags'),
            # then that name's function page ('withAnimation' ->
            # 'withAnimation(_:_:)'), before the looser case-insensitive matches
            match = next((h for h in hits if h.get("title", "") == input_value), None)
            if not match:
                match = next((h for h in hits if h.get("title", "").startswith(input_value + "(")), None)

            if not match:
                for h in hits:
                    if h.get("api_name", "").lower() == input_value.lower():
                        match = h
                        break
                    if h.get("title", "").lower() == input_value.lower():
                        match = h
                        break

            if not match:
                for h in hits:
                    if input_value.lower() in h.get("api_name", "").lower():
                        match = h
                        break

            if not match:
                suggestions = [f"   - {h.get('api_name', h.get('title'))} ({h.get('framework')})" for h in hits[:5]]
                output = [f"Symbol '{input_value}' not found"]
                if suggestions:
                    output.extend(["", "Similar:"] + suggestions)
                return "\n".join(output)

            hit = match
        else:
            # File path lookup
            relative_path = input_value
            if input_value.startswith('/') and 'documentation/' in input_value:
                relative_path = input_value[input_value.find('documentation/'):]

            if len(relative_path.encode('utf-8')) > MAX_FILTER_VALUE_BYTES:
                raise ToolError(
                    f"file_path is too long ({len(relative_path.encode('utf-8'))} bytes; "
                    f"max {MAX_FILTER_VALUE_BYTES}). Use the Path shown in search results."
                )

            # Full path, never truncated: a cut path matches no document
            results = safe_search("", {
                "filter": f'file_path = "{escape_filter_value(relative_path, max_length=None)}"',
                "limit": 1,
                "attributesToRetrieve": ["title", "content", "framework", "kind", "url", "file_path"]
            })
            hits = results.get("hits", [])

            if not hits:
                return f"File not found: {relative_path}"

            hit = hits[0]

    except ToolError:
        raise
    except Exception as e:
        logger.error(f"Expand failed for '{file_path}': {e}")
        raise ToolError("Unable to retrieve documentation. Please try again in a moment.") from e

    content = hit.get("content", "")
    if not content:
        return "No content available"

    if sections:
        output = [f"# {hit.get('title', 'Documentation')}", ""]
        for section in sections:
            section_content = extract_section(content, section)
            if section_content:
                output.append(f"## {section.title()}")
                output.append(section_content)
                output.append("")
        return "\n".join(output)

    return transform_internal_links(content)


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
            stats = meili_index.get_stats()
            total_docs = getattr(stats, 'number_of_documents', 0)

            # Detect indexing: stats.is_indexing (during batch) OR recent indexing task (between batches)
            is_actively_indexing = getattr(stats, 'is_indexing', False)
            has_recent_indexing = False

            try:
                from datetime import datetime, timezone
                tasks = meili_client.get_tasks({
                    "types": ["documentAdditionOrUpdate"],
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

    # last_index_full: When last full rebuild ran (--force flag, from metadata)
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
