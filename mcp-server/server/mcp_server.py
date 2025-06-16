#!/usr/bin/env python3
"""
MCP (Model Context Protocol) Server for Apple Documentation
Streamable HTTP transport implementation following MCP specification
"""

import os
import sys
import logging
import json
import uuid
import asyncio
from typing import Optional, Dict, Any, List
from pathlib import Path
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException, Depends, Request, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse, StreamingResponse
from sse_starlette.sse import EventSourceResponse
import uvicorn

# Import config and RAG engine
try:
    from .config import MCP_API_KEY, MCP_PORT, MAX_SEARCH_LIMIT, DEFAULT_SEARCH_LIMIT
    from .rag import SimpleRAG
    from .logger import get_logger
    from .resources_handler import ResourcesHandler
    from .prompts_handler import PromptsHandler
except ImportError:
    from config import MCP_API_KEY, MCP_PORT, MAX_SEARCH_LIMIT, DEFAULT_SEARCH_LIMIT
    from rag import SimpleRAG
    from logger import get_logger
    from resources_handler import ResourcesHandler
    from prompts_handler import PromptsHandler

# Setup logging
logger = get_logger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Apple Docs MCP Server",
    description="Model Context Protocol server for searching Apple developer documentation",
    version="2.0.0"  # Version 2.0 with Streamable HTTP
)

# Security setup
security = HTTPBearer()

# Initialize components
rag_engine = None
resources_handler = None
prompts_handler = None

# Session management
sessions: Dict[str, Dict[str, Any]] = {}

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

def get_resources_handler() -> ResourcesHandler:
    """Get or create resources handler"""
    global resources_handler
    if resources_handler is None:
        resources_handler = ResourcesHandler()
    return resources_handler

def get_prompts_handler() -> PromptsHandler:
    """Get or create prompts handler"""
    global prompts_handler
    if prompts_handler is None:
        prompts_handler = PromptsHandler(get_rag_engine())
    return prompts_handler

def verify_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)) -> bool:
    """Verify API key for authentication"""
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

def create_session() -> str:
    """Create a new session"""
    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "id": session_id,
        "created": datetime.now(timezone.utc).isoformat(),
        "initialized": False,
        "client_info": {},
        "capabilities": {}
    }
    return session_id

def get_session(session_id: Optional[str]) -> Optional[Dict[str, Any]]:
    """Get session by ID"""
    if session_id:
        return sessions.get(session_id)
    return None

@app.get("/")
async def root():
    """Root endpoint with server info"""
    return {
        "service": "apple-docs-mcp",
        "version": "2.0.0",
        "transport": "streamable-http",
        "description": "Model Context Protocol server for Apple developer documentation",
        "endpoint": "/mcp"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint (no auth required for monitoring)"""
    try:
        rag = get_rag_engine()
        stats = rag.get_stats()
        
        return {
            "status": "healthy",
            "service": "apple-docs-mcp",
            "transport": "streamable-http",
            "vectorstore": {
                "status": "connected",
                "documents": stats.get("total_documents", 0),
                "collection": stats.get("collection_name"),
                "frameworks_available": stats.get("frameworks_loaded", 0)
            },
            "sessions": len(sessions)
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

@app.post("/mcp")
async def mcp_post(request: Request, response: Response, authorized: bool = Depends(verify_api_key)):
    """
    Handle MCP requests via POST.
    Can return either JSON response or SSE stream based on Accept header.
    """
    # Check Accept header
    accept_header = request.headers.get("accept", "")
    wants_sse = "text/event-stream" in accept_header
    
    # Get session ID if provided
    session_id = request.headers.get("x-session-id")
    session = get_session(session_id)
    
    # Parse request
    try:
        body = await request.json()
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={
                "jsonrpc": "2.0",
                "error": {
                    "code": -32700,
                    "message": "Parse error",
                    "data": str(e)
                },
                "id": None
            }
        )
    
    # Handle request based on whether it's a batch
    if isinstance(body, list):
        # Batch request
        responses = []
        for req in body:
            resp = await handle_single_request(req, session)
            if resp:
                responses.append(resp)
        
        if wants_sse:
            return create_sse_response(responses)
        else:
            return JSONResponse(content=responses)
    else:
        # Single request
        response_data = await handle_single_request(body, session)
        
        # For notifications (no ID), return 202 Accepted
        if "id" not in body:
            return Response(status_code=202)
        
        if wants_sse:
            return create_sse_response([response_data])
        else:
            # Set session header if new session created
            if not session_id and session:
                response.headers["x-session-id"] = session["id"]
            return JSONResponse(content=response_data)

@app.get("/mcp")
async def mcp_get(request: Request, authorized: bool = Depends(verify_api_key)):
    """
    SSE endpoint for MCP protocol - handles streaming responses
    """
    # Get or create session
    session_id = request.headers.get("x-session-id")
    if not session_id:
        session_id = create_session()
    
    session = sessions.get(session_id)
    if not session:
        session_id = create_session()
        session = sessions[session_id]
    
    async def event_generator():
        """Generate SSE events for MCP protocol"""
        try:
            # Send session establishment
            yield {
                "event": "session",
                "data": json.dumps({
                    "sessionId": session_id,
                    "created": session["created"]
                })
            }
            
            # Send server capabilities (initialize response)
            if not session.get("initialized"):
                init_response = {
                    "jsonrpc": "2.0",
                    "result": {
                        "protocolVersion": "1.0.0",
                        "serverInfo": {
                            "name": "apple-docs-mcp",
                            "version": "2.0.0"
                        },
                        "capabilities": {
                            "tools": {
                                "list": True,
                                "call": True
                            },
                            "resources": {
                                "list": True,
                                "read": True,
                                "templates": True
                            },
                            "prompts": {
                                "list": True,
                                "get": True
                            }
                        },
                        "sessionId": session_id
                    },
                    "id": "server-init"
                }
                
                yield {
                    "event": "message",
                    "data": json.dumps(init_response)
                }
                
                session["initialized"] = True
            
            # Connection established - close after initialization
            logger.info(f"MCP initialization complete for session {session_id}")
            return
                
        except asyncio.CancelledError:
            logger.info(f"SSE connection closed for session {session_id}")
            raise
    
    return EventSourceResponse(event_generator())

async def handle_single_request(request: Dict[str, Any], session: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """Handle a single JSON-RPC request"""
    method = request.get("method")
    params = request.get("params", {})
    request_id = request.get("id")
    
    # Create session if needed
    if not session and method == "initialize":
        session_id = create_session()
        session = sessions[session_id]
    
    try:
        # Route to appropriate handler
        if method == "initialize":
            result = await handle_initialize(params, session)
        elif method == "initialized":
            result = await handle_initialized(session)
        elif method == "tools/list":
            result = await handle_tools_list()
        elif method == "tools/call":
            result = await handle_tools_call(params)
        elif method == "resources/list":
            result = await handle_resources_list()
        elif method == "resources/read":
            result = await handle_resources_read(params)
        elif method == "prompts/list":
            result = await handle_prompts_list()
        elif method == "prompts/get":
            result = await handle_prompts_get(params)
        else:
            # Unknown method
            if request_id:
                return {
                    "jsonrpc": "2.0",
                    "error": {
                        "code": -32601,
                        "message": f"Method not found: {method}"
                    },
                    "id": request_id
                }
            return None
        
        # Return response if request had an ID
        if request_id:
            response = {
                "jsonrpc": "2.0",
                "result": result,
                "id": request_id
            }
            
            # Add session ID to initialize response
            if method == "initialize" and session:
                response["result"]["sessionId"] = session["id"]
            
            return response
        
        # No response for notifications
        return None
        
    except Exception as e:
        logger.error(f"Error handling {method}: {e}")
        if request_id:
            return {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": "Internal error",
                    "data": str(e)
                },
                "id": request_id
            }
        return None

async def handle_initialize(params: Dict[str, Any], session: Dict[str, Any]) -> Dict[str, Any]:
    """Handle initialize request"""
    # Store client info
    session["client_info"] = params.get("clientInfo", {})
    session["capabilities"] = params.get("capabilities", {})
    session["initialized"] = True
    
    # Return server capabilities
    return {
        "protocolVersion": "1.0.0",
        "serverInfo": {
            "name": "apple-docs-mcp",
            "version": "2.0.0"
        },
        "capabilities": {
            "tools": {
                "list": True,
                "call": True
            },
            "resources": {
                "list": True,
                "read": True,
                "templates": True
            },
            "prompts": {
                "list": True,
                "get": True
            }
        }
    }

async def handle_initialized(session: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Handle initialized notification"""
    if session:
        session["initialized"] = True
    return {}

async def handle_tools_list() -> Dict[str, Any]:
    """Handle tools/list request"""
    tools = [
        {
            "name": "search_apple_docs",
            "description": "Search Apple developer documentation across 341+ frameworks",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query (e.g., 'SwiftUI Button', 'async await')"
                    },
                    "framework": {
                        "type": "string", 
                        "description": "Optional framework filter (e.g., 'SwiftUI', 'UIKit')"
                    },
                    "platform": {
                        "type": "string",
                        "description": "Platform filter - use 'all' for cross-platform results",
                        "enum": ["ios", "ipados", "macos", "tvos", "watchos", "visionos", "catalyst", "all"],
                        "default": "all"
                    },
                    "limit": {
                        "type": "integer",
                        "description": f"Number of results (1-{MAX_SEARCH_LIMIT}, default: {DEFAULT_SEARCH_LIMIT})",
                        "default": DEFAULT_SEARCH_LIMIT,
                        "minimum": 1,
                        "maximum": MAX_SEARCH_LIMIT
                    },
                    "include_full_content": {
                        "type": "boolean",
                        "description": "Return full document content (default: false)",
                        "default": False
                    }
                },
                "required": ["query"]
            }
        },
        {
            "name": "list_frameworks",
            "description": "List Apple frameworks with optional platform filter",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "platform": {
                        "type": "string",
                        "description": "Optional platform filter",
                        "enum": ["ios", "ipados", "macos", "tvos", "watchos", "visionos", "catalyst", "all"]
                    }
                },
                "required": []
            }
        }
    ]
    
    return {"tools": tools}

async def handle_tools_call(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle tools/call request"""
    tool_name = params.get("name")
    tool_args = params.get("arguments", {})
    
    if tool_name == "search_apple_docs":
        result = await search_apple_docs(**tool_args)
    elif tool_name == "list_frameworks":
        platform = tool_args.get("platform", None)
        if platform == "":
            platform = None
        result = await list_frameworks_handler(platform)
    else:
        raise ValueError(f"Unknown tool: {tool_name}")
    
    return {"content": result}

async def handle_resources_list() -> Dict[str, Any]:
    """Handle resources/list request"""
    handler = get_resources_handler()
    resources_data = await handler.list_resources(limit=50)
    
    # Add resource templates
    resources_data["resourceTemplates"] = handler.get_resource_templates()
    
    return resources_data

async def handle_resources_read(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle resources/read request"""
    uri = params.get("uri")
    if not uri:
        raise ValueError("URI is required")
    
    handler = get_resources_handler()
    return await handler.read_resource(uri)

async def handle_prompts_list() -> Dict[str, Any]:
    """Handle prompts/list request"""
    handler = get_prompts_handler()
    return await handler.list_prompts()

async def handle_prompts_get(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle prompts/get request"""
    name = params.get("name")
    arguments = params.get("arguments", {})
    
    if not name:
        raise ValueError("Prompt name is required")
    
    handler = get_prompts_handler()
    return await handler.get_prompt(name, arguments)

def create_sse_response(messages: List[Dict[str, Any]]) -> EventSourceResponse:
    """Create SSE response from messages"""
    async def generate():
        for msg in messages:
            yield {"data": json.dumps(msg)}
    
    return EventSourceResponse(generate())

# Import search functions from original implementation
async def search_apple_docs(
    query: str,
    framework: Optional[str] = None,
    platform: str = "all",
    limit: int = DEFAULT_SEARCH_LIMIT,
    include_full_content: bool = False
) -> str:
    """Search Apple documentation and return formatted results"""
    limit = min(max(limit, 1), MAX_SEARCH_LIMIT)
    
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

async def list_frameworks_handler(platform: Optional[str] = None) -> str:
    """List all available Apple frameworks"""
    logger.info(f"list_frameworks_handler called with platform={repr(platform)}")
    
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
    # Verify API key
    if not MCP_API_KEY:
        print("❌ Error: MCP_API_KEY environment variable required")
        sys.exit(1)
    
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
    
    # Start server
    port = MCP_PORT
    print(f"\n🚀 Starting Apple Docs MCP Server (Streamable HTTP)")
    print(f"🔒 API Key authentication enabled")
    print(f"📍 Server URL: http://0.0.0.0:{port}")
    print(f"📚 Documentation available: {stats['total_documents']:,} pages")
    print(f"\n📡 Transport: Streamable HTTP (MCP Specification Compliant)")
    print(f"   - Single endpoint: /mcp (GET and POST)")
    print(f"   - Session management supported")
    print(f"   - Resources and Prompts enabled")
    print(f"\n🔑 Include 'Authorization: Bearer <your-api-key>' header in all requests")
    
    # Run server
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )

if __name__ == "__main__":
    main()