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
from dotenv import load_dotenv
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

# Configuration
MCP_API_KEY = os.getenv("MCP_API_KEY", "")
HTTP_PORT = int(os.getenv("HTTP_PORT", "8080"))
MCP_STDIO_PATH = Path(__file__).parent / "apple_docs_stdio_mcp.py"

# Security
security = HTTPBearer()

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

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """Verify the Bearer token"""
    if not MCP_API_KEY:
        raise HTTPException(status_code=500, detail="MCP_API_KEY not configured")
    
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
    print(f"🚀 Starting Apple Docs MCP HTTP Wrapper on port {HTTP_PORT}")
    print(f"📍 Remote clients can connect to http://your-server-ip:{HTTP_PORT}/mcp")
    print(f"🔐 Authentication required: Bearer {MCP_API_KEY[:8]}...")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=HTTP_PORT,
        log_level="info"
    )