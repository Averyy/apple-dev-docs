#!/usr/bin/env python3
"""
Test the STDIO-to-HTTP bridge for remote MCP server access
"""

import json
import subprocess
import sys
import os
from pathlib import Path

def test_bridge():
    """Test the STDIO-to-HTTP bridge."""
    print("Testing STDIO-to-HTTP Bridge...")
    
    # Check for required environment variables
    server_url = os.getenv("MCP_SERVER_URL", "https://mcp.xdocs.dev/mcp")
    api_key = os.getenv("MCP_API_KEY")
    
    if not api_key:
        print("❌ Error: MCP_API_KEY environment variable is required")
        print("   Set it in .env or export MCP_API_KEY=your-key")
        return False
    
    # Start the bridge
    bridge_path = Path(__file__).parent / "apple_docs_stdio_http_bridge.py"
    process = subprocess.Popen(
        ["python3", str(bridge_path), "--server-url", server_url],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env={**os.environ, "MCP_API_KEY": api_key}
    )
    
    try:
        # Test 1: List tools
        print("\n1. Testing tools/list...")
        request = {
            "jsonrpc": "2.0",
            "method": "tools/list",
            "id": 1
        }
        
        process.stdin.write(json.dumps(request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if not response_line:
            print("❌ No response received")
            return False
            
        response = json.loads(response_line)
        if "result" in response and "tools" in response["result"]:
            tools = response["result"]["tools"]
            print(f"✅ Found {len(tools)} tools:")
            for tool in tools:
                print(f"   - {tool['name']}")
        else:
            print(f"❌ Unexpected response: {response}")
            return False
        
        # Test 2: Search
        print("\n2. Testing search_apple_docs...")
        request = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": "search_apple_docs",
                "arguments": {
                    "query": "SwiftUI Button",
                    "limit": 3
                }
            },
            "id": 2
        }
        
        process.stdin.write(json.dumps(request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if not response_line:
            print("❌ No response received")
            return False
            
        response = json.loads(response_line)
        if "result" in response:
            print("✅ Search completed successfully")
            # Don't print full results as they can be large
            if "content" in response["result"]:
                print(f"   Response length: {len(str(response['result']['content']))} chars")
        else:
            print(f"❌ Search failed: {response}")
            return False
        
        print("\n✅ All tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        # Print stderr for debugging
        stderr = process.stderr.read()
        if stderr:
            print(f"Bridge stderr: {stderr}")
        return False
    finally:
        process.terminate()
        process.wait()

if __name__ == "__main__":
    print("=" * 60)
    print("STDIO-to-HTTP Bridge Test")
    print("=" * 60)
    print(f"Server URL: {os.getenv('MCP_SERVER_URL', 'https://mcp.xdocs.dev/mcp')}")
    print(f"API Key: {'Set' if os.getenv('MCP_API_KEY') else 'Not set'}")
    print()
    
    success = test_bridge()
    sys.exit(0 if success else 1)