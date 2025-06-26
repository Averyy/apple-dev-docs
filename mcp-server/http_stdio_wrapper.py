#!/usr/bin/env python3
"""
HTTP-to-STDIO Wrapper for Apple Docs MCP Server

This wrapper provides an HTTP endpoint that forwards requests to the STDIO-based
MCP server, enabling remote access over HTTP (e.g., from 192.168.2.5).

The wrapper handles:
- HTTP POST requests with JSON-RPC payloads
- Forwarding to STDIO MCP server
- Response streaming back to HTTP client
- Authentication via Bearer token
"""

import os
import sys
import json
import asyncio
import subprocess
from typing import Dict, Any, Optional
from pathlib import Path

from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse, StreamingResponse
from starlette.middleware.cors import CORSMiddleware
import uvicorn

# Load environment variables
# In Docker, these come from supervisord environment
# Only try to load .env if it exists (for local development)
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent.parent / '.env'
    if env_path.exists():
        load_dotenv(env_path)
except ImportError:
    pass  # dotenv not required in production

# Configuration
MCP_API_KEY = os.getenv("MCP_API_KEY", "")
HTTP_PORT = int(os.getenv("HTTP_PORT", "8080"))
MCP_STDIO_PATH = Path(__file__).parent / "apple_docs_stdio_mcp.py"

# Security
security = HTTPBearer(auto_error=False)  # Don't auto-error when no auth header

# FastAPI app
app = FastAPI(title="Apple Docs MCP HTTP Wrapper")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def verify_token(credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)) -> Optional[str]:
    """Verify the Bearer token"""
    # If no API key is configured, skip authentication
    if not MCP_API_KEY:
        return None
    
    # If API key is configured but no credentials provided
    if not credentials:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    if credentials.credentials != MCP_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    
    return credentials.credentials

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Apple Docs MCP HTTP Wrapper"}

@app.post("/mcp")
async def handle_mcp_request(
    request: Request,
    token: str = Depends(verify_token)
):
    """
    Handle MCP requests by forwarding to STDIO server
    
    Accepts JSON-RPC requests and forwards them to the STDIO MCP server,
    then returns the response.
    """
    try:
        # Get request body
        body = await request.json()
        
        # Validate it's a proper JSON-RPC request
        if "jsonrpc" not in body or "method" not in body:
            return JSONResponse(
                status_code=400,
                content={
                    "jsonrpc": "2.0",
                    "error": {
                        "code": -32600,
                        "message": "Invalid Request"
                    },
                    "id": body.get("id")
                }
            )
        
        # Start the STDIO MCP server as a subprocess
        process = await asyncio.create_subprocess_exec(
            sys.executable,
            str(MCP_STDIO_PATH),
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        # Send the request to STDIO
        request_str = json.dumps(body) + "\n"
        process.stdin.write(request_str.encode())
        await process.stdin.drain()
        
        # Read response
        response_data = await process.stdout.readline()
        
        # Clean up
        process.stdin.close()
        await process.wait()
        
        if not response_data:
            return JSONResponse(
                status_code=500,
                content={
                    "jsonrpc": "2.0",
                    "error": {
                        "code": -32603,
                        "message": "Internal error: No response from STDIO server"
                    },
                    "id": body.get("id")
                }
            )
        
        # Parse and return response
        try:
            response = json.loads(response_data.decode())
            return JSONResponse(content=response)
        except json.JSONDecodeError:
            # If not JSON, return as plain text error
            return JSONResponse(
                status_code=500,
                content={
                    "jsonrpc": "2.0",
                    "error": {
                        "code": -32603,
                        "message": f"Invalid response from STDIO server: {response_data.decode()}"
                    },
                    "id": body.get("id")
                }
            )
            
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": f"Internal error: {str(e)}"
                },
                "id": body.get("id") if "body" in locals() else None
            }
        )

@app.post("/mcp/sse")
async def handle_mcp_sse(
    request: Request,
    token: str = Depends(verify_token)
):
    """
    Handle MCP requests with Server-Sent Events streaming
    
    This endpoint is for clients that expect SSE responses.
    """
    async def generate():
        try:
            body = await request.json()
            
            # Start STDIO server
            process = await asyncio.create_subprocess_exec(
                sys.executable,
                str(MCP_STDIO_PATH),
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            # Send request
            request_str = json.dumps(body) + "\n"
            process.stdin.write(request_str.encode())
            await process.stdin.drain()
            process.stdin.close()
            
            # Stream response lines
            while True:
                line = await process.stdout.readline()
                if not line:
                    break
                    
                # Format as SSE
                yield f"data: {line.decode()}\n\n"
            
            await process.wait()
            
        except Exception as e:
            error_response = {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": f"Internal error: {str(e)}"
                },
                "id": body.get("id") if "body" in locals() else None
            }
            yield f"data: {json.dumps(error_response)}\n\n"
    
    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive"
        }
    )

if __name__ == "__main__":
    try:
        print(f"🚀 Starting Apple Docs MCP HTTP Wrapper on port {HTTP_PORT}", flush=True)
        print(f"📍 Remote clients can connect to http://your-server-ip:{HTTP_PORT}/mcp", flush=True)
        
        if not MCP_API_KEY:
            print("⚠️  Warning: MCP_API_KEY not set - authentication disabled!", flush=True)
        else:
            print(f"🔐 Authentication required: Bearer {MCP_API_KEY[:8]}...", flush=True)
        
        # Check if STDIO script exists
        if not MCP_STDIO_PATH.exists():
            print(f"❌ Error: STDIO MCP script not found at {MCP_STDIO_PATH}", flush=True)
            sys.exit(1)
        else:
            print(f"✅ STDIO MCP script found at {MCP_STDIO_PATH}", flush=True)
        
        # Verify we can import required modules
        try:
            import mcp
            print("✅ MCP module imported successfully", flush=True)
        except ImportError as e:
            print(f"❌ Error importing MCP module: {e}", flush=True)
            sys.exit(1)
        
        print("🌐 Starting HTTP server...", flush=True)
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=HTTP_PORT,
            log_level="info"
        )
    except Exception as e:
        print(f"❌ Fatal error starting HTTP wrapper: {e}", flush=True)
        import traceback
        traceback.print_exc()
        sys.exit(1)