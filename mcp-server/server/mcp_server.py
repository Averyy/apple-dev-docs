#!/usr/bin/env python3
"""
MCP (Model Context Protocol) Server for Apple Documentation
Using the official MCP Python SDK with FastMCP framework
"""

import os
import sys
from typing import Optional, List, Dict, Any, Annotated
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from pydantic import Field
from starlette.requests import Request
from starlette.responses import JSONResponse

# Import config and RAG engine
try:
    from .config import MCP_PORT, MAX_SEARCH_LIMIT, DEFAULT_SEARCH_LIMIT
    from .rag import SimpleRAG
    from .logger import get_logger
except ImportError:
    from config import MCP_PORT, MAX_SEARCH_LIMIT, DEFAULT_SEARCH_LIMIT
    from rag import SimpleRAG
    from logger import get_logger

# Setup logging
logger = get_logger(__name__)

# Initialize FastMCP server
mcp = FastMCP("apple-docs-mcp")

# Initialize RAG engine globally
rag_engine: Optional[SimpleRAG] = None

# Add custom routes without auth
@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> JSONResponse:
    """Health check endpoint without auth"""
    try:
        rag = get_rag_engine()
        stats = rag.get_stats()
        return JSONResponse({
            "status": "healthy",
            "service": "apple-docs-mcp",
            "transport": "streamable-http",
            "vectorstore": {
                "documents": stats.get("total_documents", 0),
                "frameworks": stats.get("frameworks_loaded", 0)
            }
        })
    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={"status": "unhealthy", "error": str(e)}
        )

@mcp.custom_route("/", methods=["GET"])
async def root(request: Request) -> JSONResponse:
    """Root endpoint"""
    return JSONResponse({
        "service": "apple-docs-mcp",
        "version": "2.0.0",
        "transport": "streamable-http",
        "endpoint": "/mcp"
    })

def get_rag_engine() -> SimpleRAG:
    """Get or create RAG engine instance"""
    global rag_engine
    if rag_engine is None:
        try:
            rag_engine = SimpleRAG()
            logger.info("RAG engine initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize RAG engine: {e}")
            raise
    return rag_engine

@mcp.tool()
async def search_apple_docs(
    query: Annotated[str, Field(description="Search query (e.g., 'SwiftUI Button', 'async await')")],
    framework: Annotated[Optional[str], Field(description="Optional framework filter (e.g., 'SwiftUI', 'UIKit')")] = None,
    platform: Annotated[str, Field(
        description="Platform filter - use 'all' for cross-platform results",
        json_schema_extra={"enum": ["ios", "ipados", "macos", "tvos", "watchos", "visionos", "catalyst", "all"]}
    )] = "all",
    limit: Annotated[int, Field(
        description=f"Number of results (1-{MAX_SEARCH_LIMIT}, default: {DEFAULT_SEARCH_LIMIT})",
        ge=1,
        le=MAX_SEARCH_LIMIT
    )] = DEFAULT_SEARCH_LIMIT,
    include_full_content: Annotated[bool, Field(description="Return full document content (default: false)")] = False
) -> str:
    """Search Apple developer documentation across 341+ frameworks"""
    
    logger.info(f"Search request: query='{query}', framework={framework}, platform={platform}, limit={limit}")
    
    rag = get_rag_engine()
    
    try:
        results = await rag.search(
            query=query,
            framework=framework,
            platform=platform,
            limit=limit,
            expand_query=True
        )
        
        if include_full_content:
            return format_full_results(results)
        else:
            return format_concise_results(results)
            
    except Exception as e:
        logger.error(f"Search failed: {e}")
        raise

@mcp.tool()
async def list_frameworks(
    platform: Annotated[Optional[str], Field(
        description="Optional platform filter",
        json_schema_extra={"enum": ["ios", "ipados", "macos", "tvos", "watchos", "visionos", "catalyst", "all", None]}
    )] = None
) -> str:
    """List Apple frameworks with optional platform filter"""
    
    logger.info(f"list_frameworks called with platform={repr(platform)}")
    
    rag = get_rag_engine()
    
    try:
        framework_data = rag.list_frameworks(platform)
        
        lines = []
        
        if framework_data.get('platform'):
            # Platform-specific response
            platform_display = framework_data['platform'].upper()
            if platform_display == "IOS":
                platform_display = "iOS"
            elif platform_display == "IPADOS":
                platform_display = "iPadOS"
            elif platform_display == "MACOS":
                platform_display = "macOS"
            elif platform_display == "TVOS":
                platform_display = "tvOS"
            elif platform_display == "WATCHOS":
                platform_display = "watchOS"
            elif platform_display == "VISIONOS":
                platform_display = "visionOS"
            lines.append(f"# {platform_display} Frameworks")
            lines.append(f"\nTotal frameworks: **{framework_data['total_frameworks']}**\n")
            
            for fw_name in framework_data['frameworks']:
                fw_info = framework_data['framework_details'].get(fw_name, {})
                summary = fw_info.get('summary', '')
                if summary:
                    lines.append(f"- **{fw_name}**: {summary}")
                else:
                    lines.append(f"- **{fw_name}**")
                    
        else:
            # All frameworks
            lines.append(f"# Available Apple Frameworks")
            lines.append(f"\nTotal frameworks indexed: **{framework_data['total_frameworks']}**\n")
            
            for fw_name in framework_data['frameworks']:
                fw_info = framework_data['framework_details'].get(fw_name, {})
                summary = fw_info.get('summary', '')
                platforms = fw_info.get('platforms', [])
                
                platform_str = f" [{', '.join(platforms)}]" if platforms else ""
                
                if summary:
                    lines.append(f"- **{fw_name}**{platform_str}: {summary}")
                else:
                    lines.append(f"- **{fw_name}**{platform_str}")
        
        lines.append("\n---")
        lines.append("💡 **Usage Tip**: Use any framework name with the `framework` parameter in search_apple_docs.")
        
        return '\n'.join(lines)
        
    except Exception as e:
        logger.error(f"Failed to list frameworks: {e}")
        return f"Error listing frameworks: {str(e)}"

# Add resources
@mcp.resource("resource://frameworks")
async def get_frameworks_resource() -> str:
    """Get a summary of all available frameworks"""
    rag = get_rag_engine()
    framework_data = rag.list_frameworks(None)
    
    lines = [
        f"# Apple Developer Frameworks",
        f"Total frameworks: {framework_data['total_frameworks']}",
        "",
        "## Frameworks by Platform:",
        ""
    ]
    
    # Group frameworks by platform
    platform_frameworks = {}
    for fw_name in framework_data['frameworks']:
        fw_info = framework_data['framework_details'].get(fw_name, {})
        platforms = fw_info.get('platforms', [])
        for platform in platforms:
            if platform not in platform_frameworks:
                platform_frameworks[platform] = []
            platform_frameworks[platform].append(fw_name)
    
    for platform, frameworks in sorted(platform_frameworks.items()):
        lines.append(f"### {platform.upper()}")
        lines.append(f"{len(frameworks)} frameworks")
        lines.append("")
    
    return '\n'.join(lines)

@mcp.resource("resource://stats")
async def get_stats_resource() -> str:
    """Get statistics about the documentation index"""
    rag = get_rag_engine()
    stats = rag.get_stats()
    
    lines = [
        f"# Apple Documentation Index Statistics",
        f"",
        f"- Total documents: **{stats.get('total_documents', 0):,}**",
        f"- Collection name: **{stats.get('collection_name', 'Unknown')}**",
        f"- Frameworks loaded: **{stats.get('frameworks_loaded', 0)}**",
        f"- Index status: **{'Ready' if stats.get('total_documents', 0) > 0 else 'Empty'}**"
    ]
    
    return '\n'.join(lines)

# Add prompts
@mcp.prompt()
async def analyze_api(
    api_name: Annotated[str, Field(description="Name of the API to analyze")],
    framework: Annotated[Optional[str], Field(description="Optional framework to narrow the search")] = None
) -> List[Dict[str, Any]]:
    """Generate a prompt to analyze a specific Apple API"""
    
    # Search for the API
    rag = get_rag_engine()
    results = await rag.search(
        query=api_name,
        framework=framework,
        platform="all",
        limit=5,
        expand_query=False
    )
    
    if not results:
        return [{
            "role": "user",
            "content": f"I couldn't find documentation for '{api_name}'. Please check the API name and try again."
        }]
    
    # Format the documentation
    docs_content = format_full_results(results[:3])  # Top 3 results
    
    return [{
        "role": "user",
        "content": f"""Please analyze the following Apple API documentation for '{api_name}':

{docs_content}

Provide:
1. A brief summary of what this API does
2. Key methods and properties
3. Common use cases
4. Any important notes or best practices"""
    }]

@mcp.prompt()
async def compare_frameworks(
    framework1: Annotated[str, Field(description="First framework to compare")],
    framework2: Annotated[str, Field(description="Second framework to compare")]
) -> List[Dict[str, Any]]:
    """Generate a prompt to compare two Apple frameworks"""
    
    rag = get_rag_engine()
    
    # Get info about both frameworks
    framework_data = rag.list_frameworks(None)
    fw1_info = framework_data['framework_details'].get(framework1, {})
    fw2_info = framework_data['framework_details'].get(framework2, {})
    
    if not fw1_info or not fw2_info:
        missing = []
        if not fw1_info:
            missing.append(framework1)
        if not fw2_info:
            missing.append(framework2)
        return [{
            "role": "user",
            "content": f"I couldn't find information for: {', '.join(missing)}. Please check the framework names."
        }]
    
    return [{
        "role": "user",
        "content": f"""Please compare these two Apple frameworks:

## {framework1}
- Summary: {fw1_info.get('summary', 'No summary available')}
- Platforms: {', '.join(fw1_info.get('platforms', []))}

## {framework2}
- Summary: {fw2_info.get('summary', 'No summary available')}
- Platforms: {', '.join(fw2_info.get('platforms', []))}

Compare:
1. Primary use cases for each
2. Key differences in approach
3. When to use one over the other
4. Platform availability differences"""
    }]

def format_concise_results(results: List[Dict[str, Any]]) -> str:
    """Format search results concisely"""
    if not results:
        return "No results found for your query."
    
    formatted = []
    formatted.append(f"Found {len(results)} relevant documentation pages:\n")
    
    for i, result in enumerate(results, 1):
        meta = result['metadata']
        content = result['content']
        
        lines = []
        
        # Title line
        title = f"{i}. **{meta.get('api_name', 'Unknown API')}**"
        if 'framework' in meta:
            title += f" ({meta['framework']})"
        if 'platforms' in meta and meta['platforms']:
            platforms_str = meta['platforms']
            if isinstance(platforms_str, str):
                platforms_list = [p.strip() for p in platforms_str.split(',') if p.strip()]
            else:
                platforms_list = platforms_str if isinstance(platforms_str, list) else []
            if platforms_list:
                title += f" [{', '.join(platforms_list)}]"
        lines.append(title)
        
        # File path
        if 'file_path' in meta:
            lines.append(f"   📁 `{meta['file_path']}`")
        
        # Relevance score
        if 'relevance_score' in result and result['relevance_score'] is not None:
            lines.append(f"   📊 Relevance: {result['relevance_score']:.0%}")
        
        # Content preview
        content_preview = content.strip()
        if len(content_preview) > 800:
            break_point = content_preview.rfind(' ', 500, 800)
            if break_point == -1:
                break_point = 800
            content_preview = content_preview[:break_point] + "..."
        
        # Indent content
        content_lines = content_preview.split('\n')
        content_preview = '\n'.join(f"   {line}" for line in content_lines[:10])
        
        lines.append("   " + "-" * 50)
        lines.append(content_preview)
        lines.append("")
        
        formatted.append('\n'.join(lines))
    
    return '\n'.join(formatted)

def format_full_results(results: List[Dict[str, Any]]) -> str:
    """Format search results with full content"""
    if not results:
        return "No results found for your query."
    
    formatted = []
    formatted.append(f"# Apple Documentation Search Results\n")
    formatted.append(f"Found {len(results)} relevant documentation pages:\n")
    formatted.append("---\n")
    
    for i, result in enumerate(results, 1):
        meta = result['metadata']
        content = result['content']
        
        lines = []
        
        # Header
        lines.append(f"## Result {i}: {meta.get('api_name', 'Unknown API')}")
        
        # Metadata
        lines.append("\n### Metadata")
        if 'framework' in meta:
            lines.append(f"- **Framework**: {meta['framework']}")
        if 'platforms' in meta and meta['platforms']:
            platforms_str = meta['platforms']
            if isinstance(platforms_str, str):
                platforms_list = [p.strip() for p in platforms_str.split(',') if p.strip()]
            else:
                platforms_list = platforms_str if isinstance(platforms_str, list) else []
            if platforms_list:
                lines.append(f"- **Platforms**: {', '.join(platforms_list)}")
        if 'file_path' in meta:
            lines.append(f"- **File Path**: `{meta['file_path']}`")
        if 'relevance_score' in result and result['relevance_score'] is not None:
            lines.append(f"- **Relevance Score**: {result['relevance_score']:.0%}")
        
        # Content
        lines.append("\n### Content")
        lines.append(content)
        lines.append("\n---\n")
        
        formatted.append('\n'.join(lines))
    
    return '\n'.join(formatted)

if __name__ == "__main__":
    # Verify OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable required")
        sys.exit(1)
    
    # Initialize components
    try:
        rag = get_rag_engine()
        stats = rag.get_stats()
        print(f"✅ RAG engine initialized: {stats['total_documents']:,} documents available")
        
        framework_count = len(rag._framework_names)
        print(f"📊 Frameworks indexed: {framework_count}")
    except Exception as e:
        print(f"❌ Failed to initialize RAG engine: {e}")
        sys.exit(1)
    
    # Run server
    print(f"\n🚀 Starting Apple Docs MCP Server (HTTP)")
    print(f"📚 Documentation available: {stats['total_documents']:,} pages")
    print(f"📍 Server URL: http://0.0.0.0:{MCP_PORT}/mcp/")
    print(f"🔓 No authentication required")
    print(f"\n💡 Use stdio proxy: python3 mcp_stdio_proxy.py")
    
    # Run with HTTP transport for remote access
    import uvicorn
    uvicorn.run(
        mcp.streamable_http_app(),
        host="0.0.0.0",
        port=MCP_PORT
    )