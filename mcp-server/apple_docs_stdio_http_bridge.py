#!/usr/bin/env python3
"""
STDIO-to-HTTP Bridge for Apple Docs MCP Server

This script acts as a local STDIO server that forwards requests to a remote HTTP MCP server.
It allows Claude Code (which only supports STDIO) to communicate with a deployed MCP server.

Usage:
    python apple_docs_stdio_http_bridge.py --server-url http://192.168.2.5:8080/mcp --api-key YOUR_API_KEY
"""

import asyncio
import json
import logging
import os
import sys
from typing import Any, Dict, Optional
import argparse

import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('stdio_http_bridge.log'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


class StdioHttpBridge:
    """Bridge between STDIO protocol and HTTP MCP server"""
    
    def __init__(self, server_url: str, api_key: str):
        self.server_url = server_url.rstrip('/')
        self.api_key = api_key
        self.client = httpx.AsyncClient(
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            timeout=30.0
        )
        logger.info(f"Initialized bridge to {self.server_url}")
    
    async def forward_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Forward a JSON-RPC request to the HTTP server"""
        try:
            response = await self.client.post(self.server_url, json=request)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"HTTP error: {e}")
            return {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": f"HTTP error: {str(e)}"
                },
                "id": request.get("id")
            }
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": f"Internal error: {str(e)}"
                },
                "id": request.get("id")
            }
    
    async def run(self):
        """Main loop - read from stdin, forward to HTTP, write to stdout"""
        logger.info("Starting STDIO-HTTP bridge...")
        
        try:
            reader = asyncio.StreamReader()
            protocol = asyncio.StreamReaderProtocol(reader)
            await asyncio.get_event_loop().connect_read_pipe(lambda: protocol, sys.stdin)
            
            while True:
                try:
                    # Read line from stdin
                    line = await reader.readline()
                    if not line:
                        break
                    
                    # Parse JSON-RPC request
                    request = json.loads(line.decode().strip())
                    logger.debug(f"Received request: {request}")
                    
                    # Forward to HTTP server
                    response = await self.forward_request(request)
                    logger.debug(f"Got response: {response}")
                    
                    # Write response to stdout
                    print(json.dumps(response), flush=True)
                    
                except json.JSONDecodeError as e:
                    logger.error(f"Invalid JSON: {e}")
                    error_response = {
                        "jsonrpc": "2.0",
                        "error": {
                            "code": -32700,
                            "message": "Parse error"
                        },
                        "id": None
                    }
                    print(json.dumps(error_response), flush=True)
                except Exception as e:
                    logger.error(f"Error processing request: {e}")
                    
        except KeyboardInterrupt:
            logger.info("Shutting down bridge...")
        finally:
            await self.client.aclose()


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="STDIO-to-HTTP bridge for Apple Docs MCP Server"
    )
    parser.add_argument(
        "--server-url",
        default=os.getenv("MCP_SERVER_URL", "http://192.168.2.5:8080/mcp"),
        help="URL of the remote MCP server (default: http://192.168.2.5:8080/mcp)"
    )
    parser.add_argument(
        "--api-key",
        default=os.getenv("MCP_API_KEY"),
        help="API key for authentication"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging"
    )
    
    args = parser.parse_args()
    
    if not args.api_key:
        print("Error: API key is required. Set MCP_API_KEY environment variable or use --api-key", file=sys.stderr)
        sys.exit(1)
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Create and run bridge
    bridge = StdioHttpBridge(args.server_url, args.api_key)
    
    try:
        asyncio.run(bridge.run())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()