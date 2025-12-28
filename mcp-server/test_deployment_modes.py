#!/usr/bin/env python3
"""
Test both deployment modes for Apple Docs MCP Server V2

This script verifies:
1. Local STDIO mode (for development)
2. Remote HTTP mode with STDIO bridge (for deployment)
"""

import json
import subprocess
import sys
import os
import time
from pathlib import Path
from typing import Dict, Any, Optional

# Colors for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_header(text: str):
    """Print a formatted header"""
    print(f"\n{BLUE}{'=' * 60}{RESET}")
    print(f"{BLUE}{text}{RESET}")
    print(f"{BLUE}{'=' * 60}{RESET}")

def print_success(text: str):
    """Print success message"""
    print(f"{GREEN}✅ {text}{RESET}")

def print_error(text: str):
    """Print error message"""
    print(f"{RED}❌ {text}{RESET}")

def print_info(text: str):
    """Print info message"""
    print(f"{YELLOW}ℹ️  {text}{RESET}")

def test_local_stdio_mode() -> bool:
    """Test local STDIO deployment (development mode)"""
    print_header("Testing Local STDIO Mode")
    
    # Check if Meilisearch is running
    print_info("Checking Meilisearch...")
    try:
        import httpx
        response = httpx.get("http://localhost:7700/health")
        if response.status_code == 200:
            print_success("Meilisearch is running")
        else:
            print_error("Meilisearch health check failed")
            return False
    except Exception as e:
        print_error(f"Meilisearch not accessible: {e}")
        print_info("Start Meilisearch with: docker run -d -p 7700:7700 -e MEILI_MASTER_KEY=your-key getmeili/meilisearch:v1.9")
        return False
    
    # Test STDIO server
    print_info("Starting STDIO MCP server...")
    server_path = Path(__file__).parent / "apple_docs_stdio_mcp.py"
    
    if not server_path.exists():
        print_error(f"Server script not found: {server_path}")
        return False
    
    proc = subprocess.Popen(
        [sys.executable, str(server_path)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    try:
        # Test initialize
        print_info("Sending initialize request...")
        request = {
            "jsonrpc": "2.0",
            "method": "initialize",
            "params": {
                "protocolVersion": "0.1.0",
                "capabilities": {}
            },
            "id": 1
        }
        
        proc.stdin.write(json.dumps(request) + "\n")
        proc.stdin.flush()
        
        # Read response
        response_line = proc.stdout.readline()
        if not response_line:
            print_error("No response from server")
            return False
        
        response = json.loads(response_line)
        if response.get("result", {}).get("protocolVersion"):
            print_success("Server initialized successfully")
        else:
            print_error(f"Unexpected response: {response}")
            return False
        
        # Test tools/list
        print_info("Testing tools/list...")
        request = {
            "jsonrpc": "2.0",
            "method": "tools/list",
            "id": 2
        }
        
        proc.stdin.write(json.dumps(request) + "\n")
        proc.stdin.flush()
        
        response_line = proc.stdout.readline()
        response = json.loads(response_line)
        
        if "result" in response and "tools" in response["result"]:
            tools = response["result"]["tools"]
            print_success(f"Found {len(tools)} tools:")
            for tool in tools:
                print(f"   - {tool['name']}")
        else:
            print_error("Failed to list tools")
            return False
        
        print_success("Local STDIO mode is working correctly!")
        return True
        
    except Exception as e:
        print_error(f"Error testing STDIO mode: {e}")
        return False
    finally:
        proc.terminate()
        proc.wait()

def test_remote_http_mode() -> bool:
    """Test remote HTTP deployment with STDIO bridge"""
    print_header("Testing Remote HTTP Mode (via STDIO Bridge)")
    
    # Check environment
    server_url = os.getenv("MCP_SERVER_URL", "https://mcp.xdocs.dev/mcp")
    api_key = os.getenv("MCP_API_KEY")
    
    if not api_key:
        print_error("MCP_API_KEY not set in environment")
        print_info("Set it in .env file or export MCP_API_KEY=your-key")
        print_info("Skipping remote test...")
        return True  # Not a failure, just skipped
    
    print_info(f"Testing connection to: {server_url}")
    
    # Test HTTP endpoint directly first
    print_info("Testing HTTP endpoint...")
    try:
        import httpx
        headers = {"Authorization": f"Bearer {api_key}"}
        response = httpx.post(
            server_url,
            json={"jsonrpc": "2.0", "method": "tools/list", "id": 1},
            headers=headers,
            timeout=5.0
        )
        
        if response.status_code == 200:
            print_success("HTTP endpoint is accessible")
        else:
            print_error(f"HTTP endpoint returned {response.status_code}")
            print_info("Make sure ENABLE_HTTP_WRAPPER=true on the server")
            return False
    except Exception as e:
        print_error(f"Cannot reach HTTP endpoint: {e}")
        print_info("Server might not be running or HTTP wrapper not enabled")
        return False
    
    # Test STDIO bridge
    print_info("Testing STDIO-to-HTTP bridge...")
    bridge_path = Path(__file__).parent / "apple_docs_stdio_http_bridge.py"
    
    if not bridge_path.exists():
        print_error(f"Bridge script not found: {bridge_path}")
        return False
    
    proc = subprocess.Popen(
        [sys.executable, str(bridge_path), "--server-url", server_url],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env={**os.environ, "MCP_API_KEY": api_key}
    )
    
    try:
        # Test tools/list via bridge
        request = {
            "jsonrpc": "2.0",
            "method": "tools/list",
            "id": 1
        }
        
        proc.stdin.write(json.dumps(request) + "\n")
        proc.stdin.flush()
        
        response_line = proc.stdout.readline()
        if not response_line:
            print_error("No response from bridge")
            stderr = proc.stderr.read()
            if stderr:
                print_error(f"Bridge error: {stderr}")
            return False
        
        response = json.loads(response_line)
        if "result" in response and "tools" in response["result"]:
            print_success("Bridge successfully forwarded request to remote server")
            print_success("Remote HTTP mode is working correctly!")
            return True
        else:
            print_error(f"Unexpected response: {response}")
            return False
            
    except Exception as e:
        print_error(f"Error testing bridge: {e}")
        return False
    finally:
        proc.terminate()
        proc.wait()

def print_claude_config_examples():
    """Print example configurations for Claude Code"""
    print_header("Claude Code Configuration Examples")
    
    print("\n1. Local Development (Direct STDIO):")
    print("```json")
    config = {
        "mcpServers": {
            "apple-docs": {
                "command": "python3",
                "args": [str(Path(__file__).parent / "apple_docs_stdio_mcp.py")]
            }
        }
    }
    print(json.dumps(config, indent=2))
    print("```")
    
    print("\n2. Remote Server (via STDIO Bridge):")
    print("```json")
    config = {
        "mcpServers": {
            "apple-docs": {
                "command": "python3",
                "args": [
                    str(Path(__file__).parent / "apple_docs_stdio_http_bridge.py"),
                    "--server-url", "https://mcp.xdocs.dev/mcp"
                ],
                "env": {
                    "MCP_API_KEY": "your-api-key"
                }
            }
        }
    }
    print(json.dumps(config, indent=2))
    print("```")

def main():
    """Run all deployment mode tests"""
    print_header("Apple Docs MCP Server V2 - Deployment Test Suite")
    
    # Load environment
    env_path = Path(__file__).parent.parent / '.env'
    if env_path.exists():
        from dotenv import load_dotenv
        load_dotenv(env_path)
        print_success(f"Loaded environment from {env_path}")
    
    # Run tests
    local_ok = test_local_stdio_mode()
    
    # Only test remote if explicitly configured
    if os.getenv("TEST_REMOTE", "").lower() == "true":
        remote_ok = test_remote_http_mode()
    else:
        print_info("\nSkipping remote test (set TEST_REMOTE=true to enable)")
        remote_ok = True
    
    # Summary
    print_header("Test Summary")
    if local_ok:
        print_success("Local STDIO mode: PASSED")
    else:
        print_error("Local STDIO mode: FAILED")
    
    if os.getenv("TEST_REMOTE", "").lower() == "true":
        if remote_ok:
            print_success("Remote HTTP mode: PASSED")
        else:
            print_error("Remote HTTP mode: FAILED")
    
    # Show configuration examples
    print_claude_config_examples()
    
    # Exit code
    return 0 if (local_ok and remote_ok) else 1

if __name__ == "__main__":
    sys.exit(main())