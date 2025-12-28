#!/usr/bin/env python3
"""
Apple Docs MCP Server - Native HTTP Implementation

MCP server for Apple Developer Documentation with Meilisearch backend.
Supports both HTTP (streamable-http) and STDIO transports.

Usage:
    HTTP mode:  python apple_docs_mcp.py --port 8000
    STDIO mode: python apple_docs_mcp.py --transport stdio
"""

import os
import sys
import re
import secrets
import time
import logging
from collections import defaultdict
from typing import Dict, List, Optional, Any
from pathlib import Path

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
from mcp.types import ToolAnnotations

# =============================================================================
# CONFIGURATION
# =============================================================================

MEILISEARCH_URL = os.getenv("MEILI_HTTP_ADDR", "http://localhost:7700")
MEILISEARCH_API_KEY = os.getenv("MEILI_SEARCH_KEY", os.getenv("MEILI_MASTER_KEY", ""))
INDEX_NAME = "apple-docs"
SERVER_VERSION = "2.0.0"
HTTP_PORT = int(os.getenv("HTTP_PORT", "8000"))

# Rate limiting config
MCP_API_KEY = os.getenv("MCP_API_KEY", "")
RATE_LIMIT_REQUESTS = int(os.getenv("RATE_LIMIT_REQUESTS", "30"))

# Token optimization settings
MAX_TOKEN_BUDGET = 25000

# =============================================================================
# GLOBAL STATE
# =============================================================================

# Meilisearch connection (initialized on startup)
meili_client: Optional[meilisearch.Client] = None
meili_index: Optional[Any] = None

# Framework cache (populated on first use)
_frameworks_cache: Optional[Dict[str, int]] = None

# Note: active_framework is for STDIO mode only. In HTTP stateless mode,
# pass the 'framework' parameter explicitly to each tool call.
_active_framework: Optional[str] = None

# =============================================================================
# MEILISEARCH INITIALIZATION
# =============================================================================

def init_meilisearch() -> bool:
    """Initialize Meilisearch client."""
    global meili_client, meili_index
    try:
        meili_client = meilisearch.Client(MEILISEARCH_URL, MEILISEARCH_API_KEY)
        meili_index = meili_client.index(INDEX_NAME)

        health = meili_client.health()
        if health.get('status') != 'available':
            raise Exception(f"Meilisearch not available: {health}")

        # Test connection
        try:
            test_search = meili_index.search("", {"limit": 1})
            doc_count = test_search.get('estimatedTotalHits', 0)
            logger.info(f"Meilisearch connected: ~{doc_count:,} documents indexed")
        except Exception as e:
            logger.warning(f"Could not get document count: {e}")

        return True
    except Exception as e:
        logger.error(f"Failed to connect to Meilisearch: {e}")
        return False


def get_framework_counts() -> Dict[str, int]:
    """Get framework counts with caching."""
    global _frameworks_cache

    if _frameworks_cache is not None:
        return _frameworks_cache

    if not meili_index:
        return {}

    results = meili_index.search("", {"facets": ["framework"], "limit": 0})
    _frameworks_cache = results.get("facetDistribution", {}).get("framework", {})
    return _frameworks_cache


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


# =============================================================================
# FASTMCP SERVER SETUP
# =============================================================================

# Initialize FastMCP - stateless for HTTP scalability
mcp = FastMCP(
    name="apple-docs",
    stateless_http=True,
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
    )
)
def search_apple_docs(
    query: str,
    framework: str = "",
    strict_framework: bool = False,
    platform: str = "all",
    limit: int = 10,
    relevance_threshold: float = 0.0,
    token_budget: int = 10000,
    summary_mode: bool = False,
    offset: int = 0
) -> str:
    """Search Apple Developer Documentation.

    Args:
        query: Search query (e.g., 'Button', 'async await', 'NavigationStack')
        framework: Filter by framework (e.g., 'SwiftUI', 'UIKit', 'CarPlay')
        strict_framework: Only return results from the specified framework
        platform: Filter by platform: 'ios', 'macos', 'tvos', 'watchos', 'visionos', or 'all'
        limit: Number of results (1-20, default: 10)
        relevance_threshold: Minimum relevance score (0.0-1.0)
        token_budget: Response size limit in tokens (1000-25000)
        summary_mode: Return condensed summaries instead of full content
        offset: Skip N results for pagination

    Returns:
        Formatted search results with relevance scores and documentation content
    """
    global _active_framework

    if not meili_index:
        return "Error: Meilisearch not connected"

    if not query.strip():
        return "Error: Query cannot be empty"

    # Use active framework for STDIO mode (HTTP mode should pass framework explicitly)
    if not framework and _active_framework:
        framework = _active_framework
        strict_framework = True

    # Clamp values
    limit = min(20, max(1, limit))
    token_budget = min(MAX_TOKEN_BUDGET, max(1000, token_budget))
    offset = max(0, offset)

    # Handle wildcards
    original_query = query
    has_wildcards = '*' in query or '?' in query
    wildcard_pattern = None

    if has_wildcards:
        escaped = re.escape(query)
        wildcard_pattern = re.compile(
            f'^{escaped.replace(chr(92)+"*", ".*").replace(chr(92)+"?", ".")}$',
            re.IGNORECASE
        )
        query = query.replace('*', ' ').replace('?', ' ').strip() or "a"

    # Build Meilisearch filter
    filters = []
    if framework:
        filters.append(f'framework = "{framework.strip()}"')
    if platform and platform.lower() != "all":
        filters.append(f'platforms = "{platform.lower()}"')

    # Search attributes
    attrs = ["title", "framework", "api_name", "overview", "url", "platforms", "kind", "file_path"]
    if not summary_mode:
        attrs.append("content")

    search_params = {
        "limit": max(100, limit * 5),
        "attributesToRetrieve": attrs,
        "attributesToHighlight": ["title", "api_name"],
        "highlightPreTag": "**",
        "highlightPostTag": "**",
        "showRankingScore": True,
    }
    if filters:
        search_params["filter"] = " AND ".join(filters)

    results = meili_index.search(query, search_params)
    hits = results.get("hits", [])

    # Apply wildcard filter
    if has_wildcards and wildcard_pattern and hits:
        hits = [h for h in hits if
                wildcard_pattern.match(h.get("api_name", "")) or
                wildcard_pattern.match(h.get("title", ""))]

    if not hits:
        return _build_no_results_response(original_query, framework, platform, has_wildcards)

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

    scored_hits.sort(key=lambda x: x['_relevance'], reverse=True)
    paginated = scored_hits[offset:offset + limit]

    if not paginated:
        return f"No results above relevance threshold {relevance_threshold}"

    # Build output
    output = [f"Search Results: {original_query if has_wildcards else query}"]
    output.append(f"Showing {offset + 1}-{min(offset + len(paginated), len(scored_hits))} of {len(scored_hits)} results")

    if framework:
        output.append(f"Framework: {framework}{' (strict)' if strict_framework else ''}")
    if platform != "all":
        output.append(f"Platform: {platform}")
    output.append("")

    token_count = estimate_tokens("\n".join(output))
    results_included = 0

    for i, hit in enumerate(paginated, 1):
        if token_count >= token_budget * 0.9:
            remaining = len(scored_hits) - offset - results_included
            if remaining > 0:
                output.append(f"\nToken budget reached. {remaining} more results available.")
                output.append(f"Use offset={offset + results_included} to continue")
            break

        result_lines = []
        relevance = hit.get('_relevance', 0)

        result_lines.append(f"## {i}. {hit.get('title', 'Untitled')} ({int(relevance * 100)}%)")
        result_lines.append(f"Framework: {hit.get('framework', 'Unknown')} | Type: {hit.get('kind', '')}")

        if hit.get("file_path"):
            result_lines.append(f"Path: `{hit.get('file_path')}`")
        if hit.get("url"):
            result_lines.append(f"[View on Apple Developer]({hit.get('url')})")
        result_lines.append("")

        if not summary_mode and hit.get("content"):
            result_lines.append(transform_internal_links(hit.get("content", "")))
        elif hit.get("overview"):
            overview = hit.get("overview", "")[:400]
            if overview:
                result_lines.append(overview)

        result_lines.append("\n---\n")
        result_text = "\n".join(result_lines)
        result_tokens = estimate_tokens(result_text)

        if results_included > 0 and token_count + result_tokens > token_budget:
            continue

        output.extend(result_lines)
        token_count += result_tokens
        results_included += 1

    if offset + results_included < len(scored_hits):
        remaining = len(scored_hits) - offset - results_included
        output.append(f"\n{remaining} more results available. Use offset={offset + results_included} to continue")

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
        lines.append("   - Try a different wildcard pattern (e.g., *View, UI*)")
    else:
        lines.append("   - Try simpler keywords")
        lines.append("   - Use wildcards: Button* or *View")
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
    )
)
def expand_result(
    file_path: str,
    sections: List[str] = None
) -> str:
    """Get full documentation for a symbol or file.

    Args:
        file_path: Symbol name (e.g., 'Button') or file path from search results
        sections: Specific sections to include (e.g., ['overview', 'declaration'])

    Returns:
        Full documentation content
    """
    global _active_framework

    if not meili_index:
        return "Error: Meilisearch not connected"

    if not file_path:
        return "Error: file_path is required"

    sections = sections or []
    input_value = file_path.strip().strip('`')
    is_symbol = bool(re.match(r'^[A-Z][a-zA-Z0-9]*$', input_value)) and '/' not in input_value

    if is_symbol:
        search_params = {
            "limit": 10,
            "attributesToRetrieve": ["title", "content", "framework", "kind", "url", "file_path", "api_name"]
        }
        if _active_framework:
            search_params["filter"] = f'framework = "{_active_framework}"'

        results = meili_index.search(input_value, search_params)
        hits = results.get("hits", [])

        # Find exact match
        match = None
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
            if _active_framework:
                output.append(f"   Searched in: {_active_framework}")
            if suggestions:
                output.extend(["", "Similar:"] + suggestions)
            return "\n".join(output)

        hit = match
    else:
        # File path lookup
        relative_path = input_value
        if input_value.startswith('/') and 'documentation/' in input_value:
            relative_path = input_value[input_value.find('documentation/'):]

        results = meili_index.search("", {
            "filter": f'file_path = "{relative_path}"',
            "limit": 1,
            "attributesToRetrieve": ["title", "content", "framework", "kind", "url", "file_path"]
        })
        hits = results.get("hits", [])

        if not hits:
            return f"File not found: {relative_path}"

        hit = hits[0]

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
    )
)
def list_frameworks(query: str = "") -> str:
    """List available Apple frameworks with document counts.

    Args:
        query: Optional filter to search framework names (e.g., 'UI', 'Core')

    Returns:
        Formatted list of frameworks with document counts
    """
    global _active_framework

    framework_counts = get_framework_counts()
    if not framework_counts:
        return "No frameworks found"

    if query:
        filtered = {k: v for k, v in framework_counts.items() if query.lower() in k.lower()}
    else:
        filtered = framework_counts

    sorted_frameworks = sorted(filtered.items(), key=lambda x: (-x[1], x[0]))

    output = []
    if _active_framework:
        output.append(f"Currently selected: **{_active_framework}**\n")

    if query:
        output.append(f"Frameworks matching '{query}' ({len(sorted_frameworks)} of {len(framework_counts)}):")
    else:
        output.append(f"Available Frameworks ({len(sorted_frameworks)}):")
    output.append("")

    for i, (fw, count) in enumerate(sorted_frameworks, 1):
        marker = "-> " if fw == _active_framework else "   "
        output.append(f"{marker}{i:3d}. {fw:<30} ({count:,} docs)")

    output.extend(["", "Use: search_apple_docs(query=\"Button\", framework=\"SwiftUI\")"])
    return "\n".join(output)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Select Framework",
        readOnlyHint=False,  # Modifies state
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def choose_framework(framework: str) -> str:
    """Select a framework to scope subsequent searches (STDIO mode only).

    Note: In HTTP mode, pass 'framework' parameter directly to search_apple_docs.

    Args:
        framework: Framework name (e.g., 'SwiftUI'). Use 'clear' to remove selection.

    Returns:
        Confirmation message
    """
    global _active_framework

    if not framework:
        return "Error: framework parameter required"

    framework = framework.strip()

    if framework.lower() == "clear":
        old = _active_framework
        _active_framework = None
        return f"Cleared framework selection{f' (was: {old})' if old else ''}"

    framework_counts = get_framework_counts()

    # Find matching framework
    matched = None
    for fw in framework_counts:
        if fw.lower() == framework.lower():
            matched = fw
            break

    if not matched:
        partial = [fw for fw in framework_counts if framework.lower() in fw.lower()]
        if len(partial) == 1:
            matched = partial[0]
        elif partial:
            return f"Multiple matches for '{framework}':\n" + "\n".join(f"   - {fw}" for fw in partial[:10])
        else:
            return f"Framework '{framework}' not found. Use list_frameworks() to see all."

    _active_framework = matched
    doc_count = framework_counts.get(matched, 0)
    return f"Selected: **{matched}** ({doc_count:,} documents)\n\nNote: Framework selection only persists in STDIO mode."


@mcp.tool(
    annotations=ToolAnnotations(
        title="Current Framework",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def current_framework() -> str:
    """Show the currently selected framework (STDIO mode only).

    Returns:
        Current framework status
    """
    if _active_framework:
        counts = get_framework_counts()
        doc_count = counts.get(_active_framework, 0)
        return f"**Current:** {_active_framework} ({doc_count:,} documents)"
    return "**No framework selected** - searches include all frameworks"


@mcp.tool(
    annotations=ToolAnnotations(
        title="Server Version",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def get_version() -> str:
    """Get server version and status.

    Returns:
        Version info and Meilisearch status
    """
    counts = get_framework_counts()
    total_docs = sum(counts.values())

    return f"""**Apple Docs MCP Server** v{SERVER_VERSION}

**Status:**
   Meilisearch: {'Connected' if meili_index else 'Disconnected'}
   Frameworks: {len(counts)}
   Documents: {total_docs:,}

**Tools:** search_apple_docs, expand_result, list_frameworks, choose_framework, current_framework, get_version"""


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

    def _get_client_ip(self, request) -> str:
        forwarded = request.headers.get("x-forwarded-for")
        if forwarded:
            return forwarded.split(",")[0].strip()
        return request.client.host if request.client else "unknown"

    def _is_authenticated(self, request) -> bool:
        if not self.api_key:
            return False
        auth = request.headers.get("authorization", "")
        if auth.startswith("Bearer "):
            return secrets.compare_digest(auth[7:], self.api_key)
        return False

    def _check_rate_limit(self, client_ip: str) -> bool:
        now = time.time()
        window_start = now - 60

        # Clean old entries
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
    """Health check endpoint."""
    from starlette.responses import JSONResponse
    return JSONResponse({
        "status": "healthy",
        "service": "apple-docs-mcp",
        "version": SERVER_VERSION,
        "meilisearch": "connected" if meili_index else "disconnected"
    })


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Main entry point."""
    import argparse
    import uvicorn
    from starlette.middleware import Middleware

    parser = argparse.ArgumentParser(description="Apple Docs MCP Server")
    parser.add_argument("--transport", "-t", choices=["http", "stdio"], default="http")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", "-p", type=int, default=HTTP_PORT)
    args = parser.parse_args()

    logger.info(f"Apple Docs MCP Server v{SERVER_VERSION}")

    # Initialize Meilisearch
    if not init_meilisearch():
        logger.error("Meilisearch connection failed")
        if args.transport == "stdio":
            sys.exit(1)

    if args.transport == "stdio":
        logger.info("Running in STDIO mode")
        mcp.run(transport="stdio")
    else:
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

        # Create ASGI app with middleware attached
        app = mcp.http_app(
            path="/mcp",
            middleware=middleware,
            transport="streamable-http",
        )

        # Run with uvicorn
        uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
