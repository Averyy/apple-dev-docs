#!/usr/bin/env python3
"""
MCP (Model Context Protocol) Server for Apple Documentation
HTTP-based implementation for maximum compatibility with all MCP clients
"""

import os
import sys
import logging
from typing import Optional, Dict, Any, List
from pathlib import Path

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
import uvicorn

# Import config and RAG engine
try:
    # Try relative imports first (when running as module)
    from .config import MCP_API_KEY, MCP_PORT, MAX_SEARCH_LIMIT, DEFAULT_SEARCH_LIMIT
    from .rag import SimpleRAG
    from .logger import get_logger
except ImportError:
    # Fall back to absolute imports (when running as script)
    from config import MCP_API_KEY, MCP_PORT, MAX_SEARCH_LIMIT, DEFAULT_SEARCH_LIMIT
    from rag import SimpleRAG
    from logger import get_logger

# Setup logging
logger = get_logger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Apple Docs MCP Server",
    description="Model Context Protocol server for searching Apple developer documentation",
    version="1.0.0"
)

# Security setup
security = HTTPBearer()

# Initialize RAG engine (singleton)
rag_engine = None

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


def verify_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)) -> bool:
    """
    Verify API key for authentication.
    API key is always required for security.
    """
    expected_key = MCP_API_KEY
    
    if not expected_key:
        logger.error("MCP_API_KEY environment variable not set")
        raise HTTPException(
            status_code=500, 
            detail="Server configuration error: MCP_API_KEY not configured"
        )
    
    if not credentials or credentials.credentials != expected_key:
        logger.warning(f"Invalid API key attempt")
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )
    
    return True


@app.get("/")
async def root():
    """Root endpoint with server info"""
    return {
        "service": "apple-docs-mcp",
        "version": "1.0.0",
        "description": "Model Context Protocol server for Apple developer documentation",
        "endpoints": {
            "health": "/health",
            "tools_list": "/mcp/tools/list",
            "tools_call": "/mcp/tools/call"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint (no auth required for monitoring)"""
    try:
        # Try to get RAG engine stats
        rag = get_rag_engine()
        stats = rag.get_stats()
        
        return {
            "status": "healthy",
            "service": "apple-docs-mcp",
            "vectorstore": {
                "status": "connected",
                "documents": stats.get("total_documents", 0),
                "collection": stats.get("collection_name"),
                "frameworks_available": stats.get("frameworks_loaded", 0)
            }
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "service": "apple-docs-mcp",
                "error": str(e)
            }
        )


@app.get("/mcp/tools/list")
async def list_tools(authorized: bool = Depends(verify_api_key)):
    """
    List available MCP tools.
    Returns the search_apple_docs tool definition.
    """
    return {
        "tools": [
            {
                "name": "search_apple_docs",
                "description": "Search Apple developer documentation across 340+ frameworks and 278K+ pages",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query (e.g., 'SwiftUI Button', 'async await', 'Metal shader')"
                        },
                        "framework": {
                            "type": "string",
                            "description": "Optional framework filter (e.g., 'SwiftUI', 'UIKit', 'Metal', 'Foundation')"
                        },
                        "platform": {
                            "type": "string",
                            "description": "Platform filter - use 'all' for cross-platform results (e.g., 'ios', 'macos', 'tvos', 'watchos', 'visionos')",
                            "enum": ["ios", "ipados", "macos", "tvos", "watchos", "visionos", "catalyst", "all"],
                            "default": "all"
                        },
                        "limit": {
                            "type": "integer",
                            "description": f"Number of results to return (1-{MAX_SEARCH_LIMIT}, default: {DEFAULT_SEARCH_LIMIT})",
                            "default": DEFAULT_SEARCH_LIMIT,
                            "minimum": 1,
                            "maximum": MAX_SEARCH_LIMIT
                        },
                        "include_full_content": {
                            "type": "boolean",
                            "description": "Return full document content instead of concise summaries (default: false)",
                            "default": False
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "list_frameworks",
                "description": "List all available Apple frameworks in the documentation database",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        ]
    }


@app.post("/mcp/tools/call")
async def call_tool(request: Dict[str, Any], authorized: bool = Depends(verify_api_key)):
    """
    Call an MCP tool.
    Currently only supports search_apple_docs.
    """
    tool_name = request.get("name")
    arguments = request.get("arguments", {})
    
    if not tool_name:
        raise HTTPException(status_code=400, detail="Tool name is required")
    
    if tool_name == "search_apple_docs":
        try:
            # Call the search function
            result = await search_apple_docs(**arguments)
            return {"result": result}
        except TypeError as e:
            # Handle invalid arguments
            logger.error(f"Invalid arguments for search_apple_docs: {e}")
            raise HTTPException(
                status_code=400,
                detail=f"Invalid arguments: {str(e)}"
            )
        except Exception as e:
            # Handle other errors
            logger.error(f"Error calling search_apple_docs: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Error executing search: {str(e)}"
            )
    elif tool_name == "list_frameworks":
        try:
            # Call the list frameworks function
            result = await list_frameworks(**arguments)
            return {"result": result}
        except Exception as e:
            # Handle errors
            logger.error(f"Error calling list_frameworks: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Error listing frameworks: {str(e)}"
            )
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Tool '{tool_name}' not found. Available tools: search_apple_docs, list_frameworks"
        )


async def search_apple_docs(
    query: str,
    framework: Optional[str] = None,
    platform: str = "all",
    limit: int = DEFAULT_SEARCH_LIMIT,
    include_full_content: bool = False
) -> str:
    """
    Search Apple documentation and return formatted results.
    
    Args:
        query: Search query
        framework: Optional framework filter
        platform: Optional platform filter
        limit: Number of results (clamped to MAX_SEARCH_LIMIT)
        include_full_content: Whether to return full content or summaries
        
    Returns:
        Formatted search results as a string
    """
    # Validate and clamp limit
    limit = min(max(limit, 1), MAX_SEARCH_LIMIT)
    
    # Log the search request
    logger.info(f"Search request: query='{query}', framework={framework}, platform={platform}, limit={limit}, full_content={include_full_content}")
    
    # Get RAG engine
    rag = get_rag_engine()
    
    # Perform search
    try:
        results = await rag.search(
            query=query,
            framework=framework,
            platform=platform,
            limit=limit,
            expand_query=True  # Use query expansion for better results
        )
        
        # Format results based on include_full_content flag
        if include_full_content:
            return format_full_results(results)
        else:
            return format_concise_results(results)
            
    except Exception as e:
        logger.error(f"Search failed: {e}")
        raise


def format_concise_results(results: List[Dict[str, Any]]) -> str:
    """
    Format search results concisely (500-1000 chars per result).
    This is the default format to save tokens.
    """
    if not results:
        return "No results found for your query."
    
    formatted = []
    formatted.append(f"Found {len(results)} relevant documentation pages:\n")
    
    for i, result in enumerate(results, 1):
        meta = result['metadata']
        content = result['content']
        
        # Build concise result
        lines = []
        
        # Title line
        title = f"{i}. **{meta.get('api_name', 'Unknown API')}**"
        if 'framework' in meta:
            title += f" ({meta['framework']})"
        # Add platforms if available
        if 'platforms' in meta and meta['platforms']:
            title += f" [{', '.join(meta['platforms'])}]"
        lines.append(title)
        
        # File path for reference
        if 'file_path' in meta:
            lines.append(f"   📁 `{meta['file_path']}`")
        
        # Relevance score
        if 'relevance_score' in result and result['relevance_score'] is not None:
            lines.append(f"   📊 Relevance: {result['relevance_score']:.0%}")
        
        # Content preview (first 500-800 chars)
        content_preview = content.strip()
        if len(content_preview) > 800:
            # Find a good break point
            break_point = content_preview.rfind(' ', 500, 800)
            if break_point == -1:
                break_point = 800
            content_preview = content_preview[:break_point] + "..."
        
        # Indent content
        content_lines = content_preview.split('\n')
        content_preview = '\n'.join(f"   {line}" for line in content_lines[:10])  # Max 10 lines
        
        lines.append("   " + "-" * 50)
        lines.append(content_preview)
        lines.append("")  # Empty line between results
        
        formatted.append('\n'.join(lines))
    
    return '\n'.join(formatted)


def format_full_results(results: List[Dict[str, Any]]) -> str:
    """
    Format search results with full content.
    Used when include_full_content=true for deep dives.
    """
    if not results:
        return "No results found for your query."
    
    formatted = []
    formatted.append(f"# Apple Documentation Search Results\n")
    formatted.append(f"Found {len(results)} relevant documentation pages:\n")
    formatted.append("---\n")
    
    for i, result in enumerate(results, 1):
        meta = result['metadata']
        content = result['content']
        
        # Build detailed result
        lines = []
        
        # Header
        lines.append(f"## Result {i}: {meta.get('api_name', 'Unknown API')}")
        
        # Metadata section
        lines.append("\n### Metadata")
        if 'framework' in meta:
            lines.append(f"- **Framework**: {meta['framework']}")
        if 'platforms' in meta and meta['platforms']:
            lines.append(f"- **Platforms**: {', '.join(meta['platforms'])}")
        if 'file_path' in meta:
            lines.append(f"- **File Path**: `{meta['file_path']}`")
        if 'relevance_score' in result and result['relevance_score'] is not None:
            lines.append(f"- **Relevance Score**: {result['relevance_score']:.0%}")
        if meta.get('chunk_index') is not None:
            lines.append(f"- **Document Part**: {meta['chunk_index'] + 1} of {meta.get('total_chunks', '?')}")
        
        # Full content
        lines.append("\n### Content")
        lines.append(content)
        
        # Separator
        lines.append("\n---\n")
        
        formatted.append('\n'.join(lines))
    
    return '\n'.join(formatted)


async def list_frameworks() -> str:
    """
    List all available Apple frameworks in the documentation database.
    
    Returns:
        Formatted list of frameworks grouped alphabetically
    """
    # Get RAG engine
    rag = get_rag_engine()
    
    # Get framework list
    try:
        framework_data = rag.list_frameworks()
        
        # Format the response
        lines = []
        lines.append(f"# Available Apple Frameworks")
        lines.append(f"\nTotal frameworks indexed: **{framework_data['total_frameworks']}**\n")
        
        # Add frameworks by platform if available
        if framework_data.get('frameworks_by_platform'):
            lines.append("## Frameworks by Platform")
            for platform, fw_list in sorted(framework_data['frameworks_by_platform'].items()):
                lines.append(f"\n### {platform.upper()}")
                lines.append(f"{len(fw_list)} frameworks available:")
                # Show first 10 as examples
                for fw in fw_list[:10]:
                    fw_info = framework_data.get('framework_details', {}).get(fw, {})
                    summary = fw_info.get('summary', '')
                    if summary:
                        # Truncate long summaries
                        summary = summary[:80] + "..." if len(summary) > 80 else summary
                        lines.append(f"- **{fw}**: {summary}")
                    else:
                        lines.append(f"- {fw}")
                if len(fw_list) > 10:
                    lines.append(f"- ...and {len(fw_list) - 10} more")
            lines.append("")
        
        # Add popular frameworks section
        if framework_data.get('popular_frameworks'):
            lines.append("## Popular Frameworks")
            lines.append("The most commonly used frameworks:")
            for fw in framework_data['popular_frameworks']:
                fw_info = framework_data.get('framework_details', {}).get(fw, {})
                summary = fw_info.get('summary', '')
                platforms = fw_info.get('platforms', [])
                
                if summary or platforms:
                    platform_str = f" [{', '.join(platforms)}]" if platforms else ""
                    summary_str = f": {summary[:60]}..." if summary and len(summary) > 60 else f": {summary}" if summary else ""
                    lines.append(f"- **{fw}**{platform_str}{summary_str}")
                else:
                    lines.append(f"- {fw}")
            lines.append("")
        
        # Add alphabetically grouped frameworks (simplified)
        lines.append("## All Frameworks (Alphabetically)")
        lines.append(f"Total: {framework_data['total_frameworks']} frameworks")
        lines.append("\nUse the platform filter in search_apple_docs to find frameworks for your target platform.")
        
        # Add usage hint
        lines.append("\n---")
        lines.append("💡 **Usage Tip**: Use any of these framework names with the `framework` parameter in search_apple_docs to filter results to a specific framework.")
        lines.append("\nExample: `search_apple_docs(query='Button', framework='swiftui')`")
        
        return '\n'.join(lines)
        
    except Exception as e:
        logger.error(f"Failed to list frameworks: {e}")
        return f"Error listing frameworks: {str(e)}"


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions"""
    logger.error(f"Unexpected error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc) if os.getenv("DEBUG") else "An unexpected error occurred"
        }
    )


def main():
    """Main entry point"""
    # Verify API key is set
    if not MCP_API_KEY:
        print("❌ Error: MCP_API_KEY environment variable required")
        print("Generate one with: openssl rand -hex 32")
        print("Then set it: export MCP_API_KEY=<your-key>")
        sys.exit(1)
    
    # Verify OpenAI API key is set (needed for RAG)
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable required")
        print("This is needed for generating embeddings during search")
        sys.exit(1)
    
    # Initialize RAG engine early to catch any issues
    try:
        rag = get_rag_engine()
        stats = rag.get_stats()
        print(f"✅ RAG engine initialized: {stats['total_documents']:,} documents available")
        
        # Verify framework coverage
        coverage = rag.verify_frameworks()
        print(f"📊 Framework coverage: {coverage['coverage_percentage']:.1f}% ({coverage['matched']}/{coverage['documentation_folders']} folders)")
    except Exception as e:
        print(f"❌ Failed to initialize RAG engine: {e}")
        sys.exit(1)
    
    # Start server
    port = MCP_PORT
    print(f"\n🚀 Starting Apple Docs MCP Server")
    print(f"🔒 API Key authentication enabled")
    print(f"📍 Server URL: http://0.0.0.0:{port}")
    print(f"📚 Documentation available: {stats['total_documents']:,} pages")
    print(f"\n📡 Endpoints:")
    print(f"   - Health: http://localhost:{port}/health")
    print(f"   - Tools List: http://localhost:{port}/mcp/tools/list")
    print(f"   - Tools Call: http://localhost:{port}/mcp/tools/call")
    print(f"\n🔑 Include 'Authorization: Bearer <your-api-key>' header in all requests")
    
    # Run the server
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )


if __name__ == "__main__":
    main()