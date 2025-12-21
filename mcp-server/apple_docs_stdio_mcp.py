#!/usr/bin/env python3
"""
Apple Docs MCP Server - STDIO Implementation with Smart Token Optimization
MCP server for Apple Developer Documentation with token budget management
"""

import os
import sys
import json
import asyncio
import logging
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path

# Load environment variables from parent directory
from dotenv import load_dotenv
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

# Configure logging to stderr
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger(__name__)

# Import meilisearch
try:
    import meilisearch
except ImportError:
    logger.error("meilisearch not installed. Run: pip install meilisearch")
    sys.exit(1)

# Configuration
MEILISEARCH_URL = os.getenv("MEILI_HTTP_ADDR", "http://localhost:7700")
MEILISEARCH_API_KEY = os.getenv("MEILI_SEARCH_KEY", os.getenv("MEILI_MASTER_KEY", ""))
INDEX_NAME = "apple-docs"

# Server version
SERVER_VERSION = "1.1.0"

# Debug logging
logger.info(f"Using Meilisearch URL: {MEILISEARCH_URL}")
logger.info(f"Using API Key: {MEILISEARCH_API_KEY[:8]}... (first 8 chars)")

# Token optimization settings
DEFAULT_TOKEN_BUDGET = 10000  # Roughly 40k characters
MAX_TOKEN_BUDGET = 25000     # Roughly 100k characters

# Global client
meili_client = None
meili_index = None

# Stateful framework selection
active_framework: Optional[str] = None
available_frameworks_cache: Optional[Dict[str, int]] = None


def calculate_relevance_score(hit: Dict, query: str, search_framework: str = "") -> float:
    """Calculate a relevance score based on query match quality with improved framework prioritization."""
    query_lower = query.lower()
    query_words = query_lower.split()
    
    title = hit.get("title", "").lower()
    api_name = hit.get("api_name", "").lower()
    overview = hit.get("overview", "").lower()
    framework = hit.get("framework", "").lower()
    kind = hit.get("kind", "").lower()
    
    score = 0.0
    
    # Extract framework from query if present
    query_framework = ""
    common_frameworks = ["swiftui", "uikit", "foundation", "combine", "appkit", "mapkit", 
                        "coredata", "corelocation", "avfoundation", "urlsession", "storekit"]
    for fw in common_frameworks:
        if fw in query_lower:
            query_framework = fw
            break
    
    # Framework matching boost
    framework_boost = 0.0
    if query_framework or search_framework:
        target_framework = search_framework.lower() or query_framework
        if framework == target_framework:
            framework_boost = 0.2  # Exact framework match
        elif framework != target_framework and target_framework:
            framework_boost = -0.3  # Wrong framework penalty
    
    # Core component detection
    is_core_component = False
    core_ui_components = ["button", "text", "image", "view", "list", "stack", "navigation", 
                         "alert", "sheet", "picker", "toggle", "slider", "textfield"]
    
    # Check if this is a core component vs specialized variant
    if any(component in api_name for component in core_ui_components):
        # Penalize specialized variants (like SubscriptionStoreButton)
        if len(api_name) > 20 or api_name.count("store") > 0 or api_name.count("subscription") > 0:
            is_core_component = False
            score -= 0.2  # Penalty for specialized variants
        else:
            is_core_component = True
            score += 0.1  # Boost for core components
    
    # Exact matches get highest scores
    if api_name == query_lower or title == query_lower:
        score = 1.0
    # API name matches primary search term (e.g., "Button" in "SwiftUI Button")
    elif query_words and api_name == query_words[-1]:  # Last word often the key term
        score = 0.95
    # API name contains query
    elif api_name and query_lower in api_name:
        score = 0.9
    # Title contains all query words
    elif all(word in title for word in query_words):
        score = 0.85
    # Title contains main search term
    elif query_words and query_words[-1] in title:
        score = 0.75
    # Partial title match
    elif any(word in title for word in query_words):
        score = 0.7
    # Overview contains query
    elif overview and query_lower in overview:
        score = 0.6
    else:
        score = 0.4
    
    # Apply framework boost/penalty
    score += framework_boost
    
    # Ensure score stays in valid range
    score = max(0.0, min(1.0, score))
    
    return score

def estimate_tokens(text: str) -> int:
    """Estimate token count (roughly 1 token per 4 characters)."""
    return len(text) // 4

def transform_internal_links(content: str) -> str:
    """Transform internal markdown links to search hints."""
    import re
    
    def replace_link(match):
        link_text = match.group(1)
        link_path = match.group(2)
        
        # Skip external links
        if link_path.startswith('http://') or link_path.startswith('https://'):
            return match.group(0)  # Keep as-is
        
        # For internal links, convert to search hint
        # Remove .md extension and path separators
        search_term = link_path.replace('.md', '').replace('/', ' ').replace('-', ' ')
        search_term = ' '.join(search_term.split())  # Clean up whitespace
        
        # Return formatted search hint
        return f"{link_text} (→ search: {search_term})"
    
    # Replace [text](path.md) with text (→ search: path)
    content = re.sub(r'\[([^\]]+)\]\(([^)]+\.md)\)', replace_link, content)
    
    return content

def enhance_swift_content(content):
    """Enhance Swift content with proper code block formatting."""
    if not content:
        return content
    
    # Add Swift syntax highlighting to code blocks that don't have it
    import re
    
    # Find code blocks and ensure they have Swift syntax highlighting
    content = re.sub(
        r'```(\n(?:(?!```).)*?\n)```', 
        r'```swift\1```', 
        content, 
        flags=re.DOTALL
    )
    
    # Enhance protocol conformance sections
    content = re.sub(
        r'(Conforms to:?\s*)(.*?)(\n)', 
        r'**\1** `\2`\3', 
        content, 
        flags=re.IGNORECASE
    )
    
    # Enhance inheritance information
    content = re.sub(
        r'(Inherits from:?\s*)(.*?)(\n)', 
        r'**\1** `\2`\3', 
        content, 
        flags=re.IGNORECASE
    )
    
    return content

def extract_see_also_simple(content: str, limit: int = 8) -> List[str]:
    """Extract see also references with improved pattern matching."""
    import re
    references = []
    seen = set()  # Avoid duplicates
    
    # Find See Also section (multiple possible headings)
    see_also_patterns = [
        r'##?\s*(?:See Also|Related Documentation|Related Topics?)\s*\n(.*?)(?=##|\Z)',
        r'##?\s*(?:Related|References?)\s*\n(.*?)(?=##|\Z)'
    ]
    
    for pattern in see_also_patterns:
        see_also_match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if see_also_match:
            see_also_content = see_also_match.group(1)
            
            # Extract text from various markdown link formats
            # Standard links: [text](url)
            links = re.findall(r'\[([^\]]+)\](?:\([^)]+\))?', see_also_content)
            for link_text in links:
                clean_text = link_text.strip('`').replace("class ", "").replace("protocol ", "").replace("struct ", "")
                if clean_text and clean_text not in seen and len(clean_text) > 2:
                    references.append(clean_text)
                    seen.add(clean_text)
            
            # Also look for bulleted items without links
            bullets = re.findall(r'^\s*[-*•]\s*`?([^`\n]+)`?', see_also_content, re.MULTILINE)
            for bullet_text in bullets:
                clean_text = bullet_text.strip().strip('`')
                if clean_text and clean_text not in seen and len(clean_text) > 2:
                    references.append(clean_text)
                    seen.add(clean_text)
    
    # Also look for inline "See <reference>" patterns in the content
    if len(references) < limit:
        inline_refs = re.findall(r'(?:See|see also|refer to)\s+`([^`]+)`', content)
        for ref in inline_refs:
            if ref not in seen and len(ref) > 2:
                references.append(ref)
                seen.add(ref)
                if len(references) >= limit:
                    break
    
    return references[:limit]

def init_meilisearch():
    """Initialize Meilisearch client."""
    global meili_client, meili_index
    try:
        meili_client = meilisearch.Client(MEILISEARCH_URL, MEILISEARCH_API_KEY)
        meili_index = meili_client.index(INDEX_NAME)
        
        # Test connection
        health = meili_client.health()
        if health.get('status') != 'available':
            raise Exception(f"Meilisearch not available: {health}")
            
        # Use search to test connection and get document count (stats requires admin permissions)
        try:
            test_search = meili_index.search("", {"limit": 1})
            doc_count = test_search.get('estimatedTotalHits', 0)
            logger.info(f"Connected to Meilisearch. Index has ~{doc_count} documents")
        except Exception as e:
            # Search failed, but we might still be connected
            logger.warning(f"Could not get document count: {e}")
            logger.info("Connected to Meilisearch")
        return True
    except Exception as e:
        logger.error(f"Failed to connect to Meilisearch: {e}")
        return False

def handle_initialize(params):
    """Handle initialize request."""
    return {
        "protocolVersion": "2024-11-05",
        "capabilities": {
            "tools": {
                "list": True
            }
        },
        "serverInfo": {
            "name": "apple-docs",
            "version": SERVER_VERSION
        }
    }

def handle_list_tools(params):
    """Handle list_tools request."""
    return {
        "tools": [
            {
                "name": "search_apple_docs",
                "description": "Search Apple Developer Documentation",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query (e.g., 'Button', 'async await', 'CPPointOfInterestTemplate')"
                        },
                        "framework": {
                            "type": "string",
                            "description": "Optional framework filter. Use exact names like 'SwiftUI', 'UIKit', 'CarPlay', 'Foundation'. Leave empty to search all frameworks."
                        },
                        "strict_framework": {
                            "type": "boolean",
                            "description": "If true, only return results from the specified framework (requires framework parameter). Default: false",
                            "default": False
                        },
                        "platform": {
                            "type": "string",
                            "description": "Platform filter: 'ios' (iPhone/iPad), 'macos' (Mac), 'tvos' (Apple TV), 'watchos' (Apple Watch), 'visionos' (Vision Pro), or 'all' (default)",
                            "enum": ["ios", "macos", "tvos", "watchos", "visionos", "all"],
                            "default": "all"
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Number of results to return (1-20, default: 10)",
                            "default": 10,
                            "minimum": 1,
                            "maximum": 20
                        },
                        "relevance_threshold": {
                            "type": "number",
                            "description": "Minimum relevance score (0.0-1.0, default: 0.0 - no filtering)",
                            "default": 0.0,
                            "minimum": 0.0,
                            "maximum": 1.0
                        },
                        "token_budget": {
                            "type": "integer",
                            "description": "Approximate token budget for response (1000-25000, default: 10000)",
                            "default": 10000,
                            "minimum": 1000,
                            "maximum": 25000
                        },
                        "summary_mode": {
                            "type": "boolean",
                            "description": "Return condensed summaries instead of full content (default: false)",
                            "default": False
                        },
                        "offset": {
                            "type": "integer",
                            "description": "Number of results to skip for pagination (default: 0). Use offset=5 to get results 6-10, etc.",
                            "default": 0,
                            "minimum": 0
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "expand_result",
                "description": "Get full documentation for a symbol or file. Accepts symbol names (e.g., 'Button', 'TabView') or file paths from search results. Uses active framework if set.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "Symbol name (e.g., 'Button', 'NavigationStack') or file path from search results"
                        },
                        "sections": {
                            "type": "array",
                            "description": "Specific sections to include (e.g., ['overview', 'declaration', 'parameters'])",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["file_path"]
                }
            },
            {
                "name": "list_frameworks",
                "description": "List available Apple frameworks with document counts. Use this to discover frameworks before searching.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Optional filter to search framework names (e.g., 'UI', 'Core', 'Kit')"
                        }
                    }
                }
            },
            {
                "name": "choose_framework",
                "description": "Select a framework to scope all subsequent searches. Once set, searches will default to this framework unless overridden.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "framework": {
                            "type": "string",
                            "description": "Framework name to select (e.g., 'SwiftUI', 'UIKit', 'Foundation'). Use 'clear' to remove selection."
                        }
                    },
                    "required": ["framework"]
                }
            },
            {
                "name": "current_framework",
                "description": "Show the currently selected framework and available next steps",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "get_version",
                "description": "Get the Apple Docs MCP server version and status information",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            }
        ]
    }

def handle_call_tool(params):
    """Handle tools/call request."""
    tool_name = params.get("name")
    arguments = params.get("arguments", {})
    
    if not meili_index:
        return {
            "content": [{"type": "text", "text": "Error: Meilisearch not connected"}],
            "isError": True
        }
    
    try:
        if tool_name == "search_apple_docs":
            return search_apple_docs(arguments)
        elif tool_name == "expand_result":
            return expand_result(arguments)
        elif tool_name == "list_frameworks":
            return list_frameworks(arguments)
        elif tool_name == "choose_framework":
            return choose_framework(arguments)
        elif tool_name == "current_framework":
            return current_framework(arguments)
        elif tool_name == "get_version":
            return get_version(arguments)
        else:
            return {
                "content": [{"type": "text", "text": f"Unknown tool: {tool_name}"}],
                "isError": True
            }
    except Exception as e:
        logger.error(f"Tool error: {e}")
        return {
            "content": [{"type": "text", "text": f"Error: {str(e)}"}],
            "isError": True
        }

def build_no_results_response(query: str, framework: str, platform: str, has_wildcards: bool) -> Dict:
    """Build a helpful response when no results are found."""
    output = [f"No results found for '{query}'"]

    # Add context about current filters
    if framework:
        output.append(f"   Framework: {framework}")
    if platform and platform != "all":
        output.append(f"   Platform: {platform}")

    output.append("")
    output.append("💡 **Suggestions:**")

    # Check if query looks like a specific symbol (PascalCase)
    import re
    is_symbol_like = bool(re.match(r'^[A-Z][a-zA-Z0-9]*$', query.replace('*', '').replace('?', '')))

    if has_wildcards:
        output.extend([
            "   • Try a different wildcard pattern (e.g., `*View`, `UI*`, `*Controller`)",
            "   • Remove wildcards for broader search",
        ])
    elif is_symbol_like:
        output.extend([
            f"   • Try `expand_result` if you have a file path",
            f"   • Try wildcard: `*{query}*` to find variations",
            f"   • Check spelling - Apple uses specific naming conventions",
        ])
    else:
        output.extend([
            "   • Try simpler keywords (e.g., 'button' instead of 'custom button style')",
            "   • Use wildcards: `Button*` or `*View`",
            "   • Try synonyms (e.g., 'modal' vs 'sheet', 'alert' vs 'dialog')",
        ])

    if framework:
        output.append(f"   • Try `choose_framework {{ \"framework\": \"clear\" }}` to search all frameworks")
    else:
        output.append("   • Try `choose_framework` to focus on a specific framework")

    output.extend([
        "",
        "**Common patterns:**",
        "   • `Button` - Direct symbol search",
        "   • `*View` - Find all View types",
        "   • `UI*` - Find all UI-prefixed types",
        "   • `async await` - Search concepts",
    ])

    return {
        "content": [{"type": "text", "text": "\n".join(output)}]
    }


def search_apple_docs(args):
    """Search Apple docs with smart token optimization."""
    global active_framework

    query = args.get("query", "")
    framework = args.get("framework", "")
    strict_framework = args.get("strict_framework", False)
    platform = args.get("platform", "all")
    limit = min(20, max(1, args.get("limit", 10)))
    relevance_threshold = args.get("relevance_threshold", 0.0)
    token_budget = min(MAX_TOKEN_BUDGET, max(1000, args.get("token_budget", DEFAULT_TOKEN_BUDGET)))
    summary_mode = args.get("summary_mode", False)
    offset = max(0, args.get("offset", 0))

    if not query.strip():
        return {
            "content": [{"type": "text", "text": "Error: Query cannot be empty"}],
            "isError": True
        }

    # Use active framework if no framework specified
    if not framework and active_framework:
        framework = active_framework
        # When using active framework, default to strict mode for better relevance
        if not args.get("strict_framework"):
            strict_framework = True

    # Handle wildcard patterns (*, ?)
    original_query = query
    has_wildcards = '*' in query or '?' in query
    wildcard_pattern = None

    if has_wildcards:
        import re
        # Convert wildcard pattern to regex for post-filtering
        # First escape all regex special chars, then convert wildcards
        escaped = re.escape(query)
        wildcard_pattern = escaped.replace(r'\*', '.*').replace(r'\?', '.')
        wildcard_pattern = re.compile(f'^{wildcard_pattern}$', re.IGNORECASE)
        # For Meilisearch, strip wildcards and search for the non-wildcard parts
        search_query = query.replace('*', ' ').replace('?', ' ').strip()
        if not search_query:
            search_query = ""  # Will match all, then filter
        query = search_query if search_query else ""
    
    # Build filter
    filters = []
    if framework and framework.strip():
        filters.append(f'framework = "{framework.strip()}"')
    if platform and platform.lower() != "all":
        filters.append(f'platforms = "{platform.lower()}"')
    
    filter_str = " AND ".join(filters) if filters else None
    
    # Search params - get MORE results than needed so we can sort them properly
    attrs_to_retrieve = ["title", "framework", "api_name", "overview", "url", "platforms", "kind", "file_path"]
    if not summary_mode:
        attrs_to_retrieve.append("content")
    
    search_params = {
        "limit": max(100, limit * 5),  # Get many more results for better sorting
        "attributesToRetrieve": attrs_to_retrieve,
        "attributesToHighlight": ["title", "api_name", "content"] if not summary_mode else ["title", "api_name", "overview"],
        "highlightPreTag": "**",
        "highlightPostTag": "**",
        "showRankingScore": True,
        "rankingScoreThreshold": 0.0
    }
    if filter_str:
        search_params["filter"] = filter_str
    
    # Perform search
    results = meili_index.search(query, search_params)
    hits = results.get("hits", [])

    # Apply wildcard filtering if pattern was used
    if has_wildcards and wildcard_pattern and hits:
        filtered_hits = []
        for hit in hits:
            api_name = hit.get("api_name", "")
            title = hit.get("title", "")
            # Match against api_name or title
            if wildcard_pattern.match(api_name) or wildcard_pattern.match(title):
                filtered_hits.append(hit)
        hits = filtered_hits

    if not hits:
        return build_no_results_response(original_query, framework, platform, has_wildcards)

    # Calculate relevance scores and filter
    scored_hits = []
    for hit in hits:
        # Strict framework filtering
        if strict_framework and framework:
            hit_framework = hit.get("framework", "")
            if hit_framework.lower() != framework.lower():
                continue  # Skip hits from other frameworks
        
        score = calculate_relevance_score(hit, query, framework)
        if score >= relevance_threshold:
            hit['computed_relevance'] = score
            scored_hits.append(hit)
    
    # Sort by relevance
    scored_hits.sort(key=lambda x: x['computed_relevance'], reverse=True)
    
    # Apply offset and limit
    total_relevant = len(scored_hits)
    paginated_hits = scored_hits[offset:offset + limit]
    
    if not paginated_hits:
        return {
            "content": [{"type": "text", "text": f"No results above relevance threshold {relevance_threshold}"}]
        }
    
    # Format output with token budget management
    output = []
    token_count = 0

    # Header with metadata
    display_query = original_query if has_wildcards else query
    output.append(f"🔍 Search Results: {display_query}")

    # Calculate result range for clearer display
    if total_relevant > 0:
        start_num = offset + 1
        end_num = min(offset + len(paginated_hits), total_relevant)
        output.append(f"Showing {start_num}-{end_num} of {total_relevant} results")
    else:
        output.append(f"No results found")

    if has_wildcards:
        output.append(f"🔤 Wildcard pattern matching enabled")
    if relevance_threshold > 0:
        output.append(f"Relevance threshold: {relevance_threshold}")
    if framework:
        # Indicate if using active framework vs explicit
        is_from_active = (not args.get("framework") and active_framework == framework)
        mode_parts = []
        if strict_framework:
            mode_parts.append("strict")
        if is_from_active:
            mode_parts.append("from active selection")
        mode = f" ({', '.join(mode_parts)})" if mode_parts else ""
        output.append(f"Framework: {framework}{mode}")
    if platform != "all":
        output.append(f"Platform: {platform}")
    output.append("")
    
    # Track tokens
    header_text = "\n".join(output)
    token_count += estimate_tokens(header_text)
    
    # Process each result
    results_included = 0
    for i, hit in enumerate(paginated_hits, 1):
        title = hit.get("title", "Untitled")
        framework_name = hit.get("framework", "Unknown")
        api_name = hit.get("api_name", "")
        content = hit.get("content", "")
        kind = hit.get("kind", "")
        file_path = hit.get("file_path", "")
        url = hit.get("url", "")
        
        # Check token budget
        if token_count >= token_budget * 0.9:  # Leave 10% buffer
            remaining = total_relevant - offset - results_included
            if remaining > 0:
                output.append("")
                output.append(f"⚠️ Token budget reached. {remaining} more results available.")
                output.append(f"💡 Use offset={offset + results_included} to continue")
            break
        
        # Build this result in a temporary buffer first
        result_output = []
        
        # Get computed relevance score
        relevance = hit.get('computed_relevance', 0)
        
        result_output.append(f"## {i}. {title} ({int(relevance * 100)}%)")
        result_output.append(f"Framework: {framework_name} | Type: {kind}")
        
        # Add file path for transparency
        if file_path:
            result_output.append(f"Path: `{file_path}`")
        
        # Add Apple Developer URL prominently
        if url:
            result_output.append(f"📖 [View on Apple Developer]({url})")
        
        result_output.append("")
        
        if not summary_mode and content:
            # Transform internal links to search hints
            content = transform_internal_links(content)
            # Return the enhanced markdown content
            result_output.append(content)
            
            # Simple extraction of See Also links - only show if meaningful
            see_also_refs = extract_see_also_simple(content, limit=5)  # Reduced from 8
            # Only show if we have more than 2 meaningful references
            if len(see_also_refs) > 2:
                result_output.append("")
                result_output.append("💡 Related documentation:")
                # Show only first 5 to reduce clutter
                for ref in see_also_refs[:5]:
                    result_output.append(f"   • {ref}")
                if len(see_also_refs) > 5:
                    result_output.append(f"   • ...and {len(see_also_refs) - 5} more")
                result_output.append("")
            
        else:
            # Summary mode - just overview with proper truncation
            overview = hit.get("overview", "")
            if overview:
                # Skip metadata lines like "**Framework**: Swift **Kind**: struct"
                lines = overview.split('\n')
                content_lines = []
                for line in lines:
                    # Skip lines that look like metadata
                    if not (line.startswith("**Framework**:") or 
                           line.startswith("**Kind**:") or
                           line.startswith("**Type**:")):
                        content_lines.append(line)
                
                overview = '\n'.join(content_lines).strip()
                
                # Ensure overview ends at sentence boundary
                if len(overview) > 400 and overview and not overview[-1] in '.!?':
                    # Find last sentence boundary
                    last_period = overview.rfind('.', 0, 400)
                    last_question = overview.rfind('?', 0, 400)
                    last_exclaim = overview.rfind('!', 0, 400)
                    
                    # Use the latest sentence boundary
                    boundary = max(last_period, last_question, last_exclaim)
                    if boundary > 200:  # Only truncate if we have reasonable content
                        overview = overview[:boundary + 1]
                    else:
                        # No good boundary, truncate at word
                        words = overview[:400].rsplit(' ', 1)
                        if len(words) > 1:
                            overview = words[0] + "..."
                        else:
                            overview = overview[:400] + "..."
                
                if overview:  # Only add if we have content after filtering
                    result_output.append(overview)
                    result_output.append("")
        
        result_output.append("---")
        result_output.append("")
        
        # Calculate tokens for this result
        result_text = "\n".join(result_output)
        result_tokens = estimate_tokens(result_text)
        
        # Skip if it would exceed budget (unless it's the first result)
        if results_included > 0 and token_count + result_tokens > token_budget:
            continue
            
        # If first result exceeds budget, truncate it
        if results_included == 0 and token_count + result_tokens > token_budget:
            if not summary_mode and content:
                # Truncate content to fit
                available_tokens = token_budget - token_count - 100  # Buffer
                if available_tokens > 0:
                    max_chars = available_tokens * 4
                    truncated_content = content[:max_chars] + "\n\n... [Content truncated due to token budget]"
                    result_output = []
                    result_output.append(f"## {i}. {title} ({int(relevance * 100)}%)")
                    result_output.append(f"Framework: {framework_name} | Type: {kind}")
                    result_output.append("")
                    result_output.append(truncated_content)
                    result_output.append("")
                    result_output.append("---")
                    result_output.append("")
        
        # Add the result to output
        output.extend(result_output)
        token_count += estimate_tokens("\n".join(result_output))
        results_included += 1
    
    # Add pagination info if there are more results
    if offset + results_included < total_relevant:
        remaining = total_relevant - offset - results_included
        next_start = offset + results_included + 1
        next_end = min(offset + results_included + limit, total_relevant)
        output.append("")
        output.append(f"📄 {remaining} more results available")
        output.append(f"   Next page will show results {next_start}-{next_end}")
        output.append(f"   Use offset={offset + results_included} to continue")
    
    return {
        "content": [{"type": "text", "text": "\n".join(output)}]
    }

def expand_result(args):
    """Expand a specific result to get full content. Accepts file paths or symbol names."""
    global active_framework

    file_path = args.get("file_path", "")
    sections = args.get("sections", [])

    if not file_path:
        return {
            "content": [{"type": "text", "text": "Error: file_path is required"}],
            "isError": True
        }

    # Clean up input - remove backticks if present
    input_value = file_path.strip().strip('`')

    # Detect if this looks like a symbol name vs a file path
    # Symbol names are typically PascalCase without path separators or extensions
    import re
    is_symbol_name = bool(re.match(r'^[A-Z][a-zA-Z0-9]*$', input_value)) and '/' not in input_value and '.' not in input_value

    hits = []

    if is_symbol_name:
        # Search for symbol by name, optionally scoped to active framework
        search_params = {
            "limit": 10,
            "attributesToRetrieve": ["title", "content", "framework", "kind", "url", "file_path", "api_name"]
        }

        # If we have an active framework, filter to it
        if active_framework:
            search_params["filter"] = f'framework = "{active_framework}"'

        symbol_results = meili_index.search(input_value, search_params)
        symbol_hits = symbol_results.get("hits", [])

        # Find exact match on api_name or title
        for h in symbol_hits:
            api_name = h.get("api_name", "")
            title = h.get("title", "")
            if api_name.lower() == input_value.lower() or title.lower() == input_value.lower():
                hits = [h]
                break

        # If no exact match, try the best match
        if not hits and symbol_hits:
            # Prefer matches where api_name contains the symbol
            for h in symbol_hits:
                if input_value.lower() in h.get("api_name", "").lower():
                    hits = [h]
                    break

        # Still no match? Return helpful error with suggestions
        if not hits:
            suggestions = []
            for h in symbol_hits[:5]:
                suggestions.append(f"   • {h.get('api_name', h.get('title', 'Unknown'))} ({h.get('framework', '')})")

            output = [f"Symbol '{input_value}' not found"]
            if active_framework:
                output.append(f"   Searched in: {active_framework}")

            if suggestions:
                output.extend(["", "Similar results:", *suggestions])
            else:
                output.extend([
                    "",
                    "💡 Try:",
                    f"   • `search_apple_docs {{ \"query\": \"{input_value}\" }}`",
                    "   • Check spelling (Apple uses specific naming)",
                ])

            return {
                "content": [{"type": "text", "text": "\n".join(output)}],
                "isError": True
            }
    else:
        # Original file path logic
        # Normalize the input path to relative format (documentation/...)
        if input_value.startswith('/'):
            # Convert absolute to relative path
            if 'documentation/' in input_value:
                relative_path = input_value[input_value.find('documentation/'):]
            else:
                relative_path = Path(input_value).name
        else:
            relative_path = input_value

        # Search by exact file path
        results = meili_index.search("", {
            "filter": f'file_path = "{relative_path}"',
            "limit": 1,
            "attributesToRetrieve": ["title", "content", "framework", "kind", "url", "file_path"]
        })

        hits = results.get("hits", [])
        if not hits:
            # Fallback: try searching by filename only
            filename = Path(relative_path).name
            fallback_results = meili_index.search(filename, {
                "limit": 10,
                "attributesToRetrieve": ["title", "content", "framework", "kind", "url", "file_path"]
            })

            # Look for exact path match in fallback results
            for h in fallback_results.get("hits", []):
                if h.get("file_path") == relative_path:
                    hits = [h]
                    break

            if not hits:
                return {
                    "content": [{"type": "text", "text": f"File not found: {relative_path}\n\n💡 If this is a symbol name, try: `expand_result {{ \"file_path\": \"Button\" }}`"}],
                    "isError": True
                }
    
    hit = hits[0]
    content = hit.get("content", "")
    
    if not content:
        return {
            "content": [{"type": "text", "text": "No content available for this file"}]
        }
    
    # If specific sections requested, extract them
    if sections:
        output = [f"# {hit.get('title', 'Documentation')}", ""]
        
        for section in sections:
            section_content = extract_section(content, section)
            if section_content:
                output.append(f"## {section.title()}")
                output.append(section_content)
                output.append("")
        
        return {
            "content": [{"type": "text", "text": "\n".join(output)}]
        }
    
    # Transform internal links and return full content
    content = transform_internal_links(content)
    return {
        "content": [{"type": "text", "text": content}]
    }

def extract_section(content: str, section_name: str) -> str:
    """Extract a specific section from content."""
    import re
    
    # Normalize section name
    section_pattern = re.escape(section_name.replace('_', ' ').title())
    
    # Look for the section
    match = re.search(
        rf'##?\s*{section_pattern}\s*\n(.*?)(?=##|\Z)', 
        content, 
        re.DOTALL | re.IGNORECASE
    )
    
    if match:
        return match.group(1).strip()
    
    return ""

def get_framework_counts() -> Dict[str, int]:
    """Get framework counts, using cache if available."""
    global available_frameworks_cache

    if available_frameworks_cache is not None:
        return available_frameworks_cache

    results = meili_index.search("", {
        "facets": ["framework"],
        "limit": 0
    })
    framework_counts = results.get("facetDistribution", {}).get("framework", {})
    available_frameworks_cache = framework_counts
    return framework_counts


def list_frameworks(args):
    """List available frameworks with optional filtering."""
    global active_framework

    try:
        query_filter = args.get("query", "").lower().strip()
        framework_counts = get_framework_counts()

        if not framework_counts:
            return {
                "content": [{"type": "text", "text": "No frameworks found in the index"}]
            }

        # Filter frameworks if query provided
        if query_filter:
            filtered = {k: v for k, v in framework_counts.items()
                       if query_filter in k.lower()}
        else:
            filtered = framework_counts

        # Sort by count then name
        sorted_frameworks = sorted(filtered.items(), key=lambda x: (-x[1], x[0]))

        output = []

        # Show current framework status
        if active_framework:
            output.append(f"📍 Currently selected: **{active_framework}**")
            output.append("")

        if query_filter:
            output.append(f"Frameworks matching '{query_filter}' ({len(sorted_frameworks)} of {len(framework_counts)} total):")
        else:
            output.append(f"Available Apple Frameworks ({len(sorted_frameworks)} total):")
        output.append("")

        for i, (framework, count) in enumerate(sorted_frameworks, 1):
            marker = "→ " if framework == active_framework else "  "
            output.append(f"{marker}{i:3d}. {framework:<30} ({count:,} documents)")

        # Add helpful hints
        output.append("")
        output.append("💡 **Next steps:**")
        output.append("   • `choose_framework { \"framework\": \"SwiftUI\" }` - Select a framework")
        output.append("   • `search_apple_docs { \"query\": \"Button\" }` - Search within selected framework")

        return {
            "content": [{"type": "text", "text": "\n".join(output)}]
        }

    except Exception as e:
        logger.error(f"List frameworks error: {e}")
        return {
            "content": [{"type": "text", "text": f"Error listing frameworks: {str(e)}"}],
            "isError": True
        }


def choose_framework(args):
    """Select a framework to scope subsequent searches."""
    global active_framework, available_frameworks_cache

    framework = args.get("framework", "").strip()

    if not framework:
        return {
            "content": [{"type": "text", "text": "Error: framework parameter is required"}],
            "isError": True
        }

    # Handle clear command
    if framework.lower() == "clear":
        old_framework = active_framework
        active_framework = None
        if old_framework:
            return {
                "content": [{"type": "text", "text": f"✓ Cleared framework selection (was: {old_framework})\n\nSearches will now include all frameworks."}]
            }
        else:
            return {
                "content": [{"type": "text", "text": "No framework was selected."}]
            }

    # Get available frameworks
    try:
        framework_counts = get_framework_counts()

        # Case-insensitive match
        matched_framework = None
        for fw in framework_counts.keys():
            if fw.lower() == framework.lower():
                matched_framework = fw
                break

        if not matched_framework:
            # Try partial match
            partial_matches = [fw for fw in framework_counts.keys()
                             if framework.lower() in fw.lower()]

            if len(partial_matches) == 1:
                matched_framework = partial_matches[0]
            elif len(partial_matches) > 1:
                suggestions = "\n".join([f"   • {fw}" for fw in partial_matches[:10]])
                return {
                    "content": [{"type": "text", "text": f"Multiple frameworks match '{framework}':\n{suggestions}\n\nPlease be more specific."}]
                }
            else:
                # Show similar frameworks
                similar = [fw for fw in framework_counts.keys()
                          if any(c in fw.lower() for c in framework.lower())][:5]
                suggestion_text = ""
                if similar:
                    suggestion_text = "\n\nDid you mean:\n" + "\n".join([f"   • {fw}" for fw in similar])
                return {
                    "content": [{"type": "text", "text": f"Framework '{framework}' not found.{suggestion_text}\n\nUse `list_frameworks` to see all available frameworks."}],
                    "isError": True
                }

        # Set the active framework
        old_framework = active_framework
        active_framework = matched_framework
        doc_count = framework_counts.get(matched_framework, 0)

        output = [
            f"✓ Selected framework: **{matched_framework}**",
            f"   {doc_count:,} documents available",
            ""
        ]

        if old_framework and old_framework != matched_framework:
            output.append(f"   (Changed from: {old_framework})")
            output.append("")

        output.extend([
            "💡 **Next steps:**",
            f"   • `search_apple_docs {{ \"query\": \"Button\" }}` - Search within {matched_framework}",
            f"   • `search_apple_docs {{ \"query\": \"*View\" }}` - Wildcard search for types ending in 'View'",
            "   • `choose_framework { \"framework\": \"clear\" }` - Clear selection",
            "   • `current_framework` - Check current selection"
        ])

        return {
            "content": [{"type": "text", "text": "\n".join(output)}]
        }

    except Exception as e:
        logger.error(f"Choose framework error: {e}")
        return {
            "content": [{"type": "text", "text": f"Error selecting framework: {str(e)}"}],
            "isError": True
        }


def current_framework(args):
    """Show current framework selection and status."""
    global active_framework

    output = []

    if active_framework:
        try:
            framework_counts = get_framework_counts()
            doc_count = framework_counts.get(active_framework, 0)

            output.extend([
                f"📍 **Current Framework:** {active_framework}",
                f"   {doc_count:,} documents available",
                "",
                "💡 **Available actions:**",
                f"   • `search_apple_docs {{ \"query\": \"your search\" }}` - Search within {active_framework}",
                "   • `search_apple_docs { \"query\": \"Button\", \"framework\": \"UIKit\" }` - Override with different framework",
                "   • `choose_framework { \"framework\": \"clear\" }` - Clear selection",
                "   • `list_frameworks` - Browse all frameworks"
            ])
        except Exception:
            output.extend([
                f"📍 **Current Framework:** {active_framework}",
                "",
                "💡 **Available actions:**",
                "   • `search_apple_docs { \"query\": \"your search\" }` - Search",
                "   • `choose_framework { \"framework\": \"clear\" }` - Clear selection"
            ])
    else:
        output.extend([
            "📍 **No framework selected**",
            "",
            "Searches will include all frameworks unless you specify one.",
            "",
            "💡 **Getting started:**",
            "   • `list_frameworks` - Browse available frameworks",
            "   • `list_frameworks { \"query\": \"UI\" }` - Filter frameworks",
            "   • `choose_framework { \"framework\": \"SwiftUI\" }` - Select a framework",
            "   • `search_apple_docs { \"query\": \"Button\" }` - Search all frameworks"
        ])

    return {
        "content": [{"type": "text", "text": "\n".join(output)}]
    }


def get_version(args):
    """Get server version and status information."""
    try:
        framework_counts = get_framework_counts()
        total_frameworks = len(framework_counts)
        total_docs = sum(framework_counts.values())

        output = [
            f"🍎 **Apple Docs MCP Server** v{SERVER_VERSION}",
            "",
            "**Status:**",
            f"   • Meilisearch: Connected",
            f"   • Frameworks indexed: {total_frameworks}",
            f"   • Documents indexed: {total_docs:,}",
            ""
        ]

        if active_framework:
            output.append(f"   • Active framework: {active_framework}")
        else:
            output.append("   • Active framework: None (searching all)")

        output.extend([
            "",
            "**Available tools:**",
            "   • `search_apple_docs` - Search documentation",
            "   • `expand_result` - Get full content for a result",
            "   • `list_frameworks` - Browse frameworks",
            "   • `choose_framework` - Select active framework",
            "   • `current_framework` - Show current selection",
            "   • `get_version` - This information"
        ])

        return {
            "content": [{"type": "text", "text": "\n".join(output)}]
        }

    except Exception as e:
        return {
            "content": [{"type": "text", "text": f"🍎 **Apple Docs MCP Server** v{SERVER_VERSION}\n\nStatus: Error - {str(e)}"}]
        }

def send_response(request_id, result):
    """Send JSON-RPC response."""
    response = {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": result
    }
    print(json.dumps(response))
    sys.stdout.flush()

def send_error(request_id, error_code, error_message):
    """Send JSON-RPC error response."""
    response = {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {
            "code": error_code,
            "message": error_message
        }
    }
    print(json.dumps(response))
    sys.stdout.flush()

def main():
    """Main stdio loop."""
    # Initialize Meilisearch
    if not init_meilisearch():
        sys.exit(1)
    
    logger.info("Apple Docs MCP Server ready (stdio mode)")
    
    # Process stdin messages
    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            
            try:
                message = json.loads(line)
                
                method = message.get("method")
                params = message.get("params", {})
                request_id = message.get("id")
                
                if method == "initialize":
                    result = handle_initialize(params)
                    send_response(request_id, result)
                elif method == "notifications/initialized":
                    # No response needed for notifications
                    pass
                elif method == "tools/list":
                    result = handle_list_tools(params)
                    send_response(request_id, result)
                elif method == "tools/call":
                    result = handle_call_tool(params)
                    send_response(request_id, result)
                else:
                    send_error(request_id, -32601, f"Method not found: {method}")
                    
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON: {e}")
            except Exception as e:
                logger.error(f"Error processing message: {e}")
                if 'request_id' in locals():
                    send_error(request_id, -32603, str(e))
                    
    except KeyboardInterrupt:
        logger.info("Server shutting down")
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()