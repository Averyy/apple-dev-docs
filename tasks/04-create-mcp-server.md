# Task 4: Create MCP Server ✅ COMPLETE & ENHANCED

## Objective
Build the Model Context Protocol (MCP) server that exposes Apple documentation search capabilities to Claude via STDIO communication.

## Prerequisites
- Task 3 completed (RAG engine implemented at `mcp-server/server/rag.py`)
- Understanding of MCP protocol basics
- Python async programming knowledge

## MCP Server Architecture

### 1. Server Setup
The MCP server acts as a bridge between:
- **Client**: Any MCP-compatible client (Claude Desktop, Cursor, Claude Code, VS Code, etc.)
- **RAG Engine**: Your Apple docs search system
- **Communication**: JSON-RPC over STDIO (standard input/output)

### 2. Core MCP Components

#### a. Single Tool Design
Define one powerful search tool:

**Tool: search_apple_docs**
- Purpose: Comprehensive search across Apple documentation
- Inputs:
  - `query`: Search terms (required)
  - `framework`: Optional filter (SwiftUI, UIKit, etc.)
  - `platform`: Platform filter (required, default: "all") - ios, macos, tvos, watchos, visionos, catalyst
  - `limit`: Number of results (default: 5, max: 20)
  - `include_full_content`: Boolean for complete documents (default: false)

**Tool: list_frameworks** (NEW)
- Purpose: List all available frameworks with metadata
- Inputs: None
- Returns: Frameworks grouped by platform with summaries

The search tool intelligently adapts output based on parameters:
- Default: Returns concise chunks (500-1000 chars) for the specified platform
- With `include_full_content=true`: Returns complete markdown files
- With higher `limit`: Returns more results for comprehensive coverage

This single tool lets Claude control token usage - it can request:
- Quick summaries (default)
- Deep dives (full content)
- Broad searches (higher limit)
- Focused searches (with framework filter)

### 3. Single HTTP Implementation

```python
# mcp_server.py (HTTP only - works everywhere)
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
import uvicorn
from typing import Optional
from server.rag import SimpleRAG

app = FastAPI(title="Apple Docs MCP Server")
security = HTTPBearer()  # API key required everywhere
rag_engine = SimpleRAG()

def verify_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """API key authentication - always required"""
    expected_key = os.getenv("MCP_API_KEY")
    
    if not expected_key:
        raise HTTPException(status_code=500, detail="MCP_API_KEY environment variable required")
        
    if not credentials or credentials.credentials != expected_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return True

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "apple-docs-mcp"}

@app.post("/mcp/tools/call")
async def call_tool(request: dict, authorized: bool = Depends(verify_api_key)):
    """MCP tool endpoint"""
    tool_name = request.get("name")
    arguments = request.get("arguments", {})
    
    if tool_name == "search_apple_docs":
        try:
            result = await search_apple_docs(**arguments)
            return {"result": result}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=404, detail="Tool not found")

@app.get("/mcp/tools/list")
async def list_tools(authorized: bool = Depends(verify_api_key)):
    """List available tools"""
    return {
        "tools": [{
            "name": "search_apple_docs",
            "description": "Search Apple developer documentation",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "framework": {"type": "string"},
                    "limit": {"type": "integer", "default": 5},
                    "include_full_content": {"type": "boolean", "default": False}
                },
                "required": ["query"]
            }
        }]
    }

async def search_apple_docs(
    query: str,
    framework: Optional[str] = None,
    limit: int = 5,
    include_full_content: bool = False
) -> str:
    """Search implementation"""
    limit = min(max(limit, 1), 20)
    results = await rag_engine.search(query=query, framework=framework, limit=limit)
    
    if include_full_content:
        return format_full_results(results)
    else:
        return format_concise_results(results)

if __name__ == "__main__":
    # Verify API key is set before starting
    if not os.getenv("MCP_API_KEY"):
        print("❌ Error: MCP_API_KEY environment variable required")
        print("Generate one with: openssl rand -hex 32")
        exit(1)
    
    port = int(os.getenv("MCP_PORT", 8080))
    print(f"🔒 Starting MCP server on port {port} with API key authentication")
    
    uvicorn.run(app, host="0.0.0.0", port=port)
```

### 4. Alternative: Using Official MCP SDK

```python
# mcp_server_official.py
import asyncio
from mcp.server import Server
import mcp.server.stdio
from mcp.types import Tool
from server.rag import SimpleRAG

# Create server instance
server = Server("apple-docs")
rag_engine = SimpleRAG()

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search_apple_docs",
            description="Search Apple developer documentation",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"},
                    "framework": {"type": "string", "description": "Optional framework filter"},
                    "limit": {"type": "integer", "description": "Number of results (1-20)", "default": 5},
                    "include_full_content": {"type": "boolean", "description": "Return full documents", "default": False}
                },
                "required": ["query"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> str:
    if name == "search_apple_docs":
        return await search_apple_docs(**arguments)
    raise ValueError(f"Unknown tool: {name}")

# Run the server
async def main():
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, InitializationOptions())

if __name__ == "__main__":
    asyncio.run(main())
```

### 4. Configuration for MCP Clients

**API key is always required** - generate one with `openssl rand -hex 32`

#### A. Local Development
For testing on your laptop:
```json
{
  "mcpServers": {
    "apple-docs": {
      "type": "sse",
      "url": "http://localhost:8080/mcp",
      "headers": {
        "Authorization": "Bearer your-mcp-api-key-here"
      }
    }
  }
}
```

#### B. Remote Server
For accessing Docker server at 192.168.2.99:
```json
{
  "mcpServers": {
    "apple-docs": {
      "type": "sse",
      "url": "http://192.168.2.99:8080/mcp",
      "headers": {
        "Authorization": "Bearer your-mcp-api-key-here"
      }
    }
  }
}
```

#### C. HTTPS (with reverse proxy)
For production with SSL:
```json
{
  "mcpServers": {
    "apple-docs": {
      "type": "sse", 
      "url": "https://your-domain.com/mcp",
      "headers": {
        "Authorization": "Bearer your-mcp-api-key-here"
      }
    }
  }
}
```

### 5. Environment Variables

**Required (both local and remote):**
- `OPENAI_API_KEY` - For embeddings
- `MCP_API_KEY` - For authentication (generate with `openssl rand -hex 32`)

**Optional:**
- `MCP_PORT` - HTTP server port (default: 8080)  
- `KEEP_MARKDOWN_FILES` - Retain docs (default: true)

### 6. Security Notes

**Minimal security features:**
- ✅ API key authentication (Bearer token)
- ✅ HTTPS ready (add reverse proxy)
- ✅ Input validation
- ✅ Error handling

**For production, consider adding:**
- Rate limiting
- Request logging
- IP allowlisting

### 6. Error Handling
```python
try:
    results = await rag_engine.search(query, framework, limit)
except Exception as e:
    return f"Error searching documentation: {str(e)}"
```

### 7. Testing the MCP Server

#### Local Testing
```bash
# Test server directly
python mcp_server.py

# In another terminal, send test JSON-RPC messages
echo '{"jsonrpc": "2.0", "method": "tools/list", "id": 1}' | python mcp_server.py
```

#### With Any MCP Client
1. Update client config file with absolute path
2. Restart your MCP client (Claude Desktop, Cursor, etc.)
3. In the client, ask: "Search Apple docs for SwiftUI Button"
4. The client should automatically use the tool

## Important Links
- [MCP Specification](https://modelcontextprotocol.io/docs/specification)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Server Examples](https://github.com/modelcontextprotocol/servers)

## Success Criteria
- [x] Server runs via HTTP with API authentication ✅
- [x] Tool appears in MCP client's available tools ✅
- [x] Search queries return relevant results ✅
- [x] Full content mode works for detailed queries ✅
- [x] Error handling works gracefully ✅
- [x] Response time < 1000ms for searches (323K doc search index) ✅

## Implementation Summary

The MCP server was successfully implemented using the HTTP approach with FastAPI:

- **Location**: `/mcp-server/server/mcp_server.py`
- **Endpoints**:
  - `/health` - Health check (no auth)
  - `/mcp/tools/list` - Lists available tools
  - `/mcp/tools/call` - Executes tool calls
- **Authentication**: Bearer token via `MCP_API_KEY`
- **Search Performance**: Sub-500ms for 323,096 documents
- **Test Coverage**: Comprehensive test at `/mcp-server/tests/test_mcp_server.py`

The server correctly resolves paths relative to the project root, making it portable for deployment.

## Time Estimate
3-4 hours for implementation (much simpler with FastMCP!)