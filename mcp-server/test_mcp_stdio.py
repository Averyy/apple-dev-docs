#!/usr/bin/env python3
"""
Test the MCP stdio server
"""

import json
import subprocess
import sys
import time

def test_mcp_server():
    """Test the MCP stdio server."""
    print("Testing Apple Docs MCP Server...")
    
    # Start the server
    server_path = "apple_docs_stdio_mcp.py"
    process = subprocess.Popen(
        ["python3", server_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=0
    )
    
    def send_message(message):
        """Send a message to the server."""
        json_str = json.dumps(message)
        print(f"→ {json_str}")
        process.stdin.write(json_str + "\n")
        process.stdin.flush()
        
        # Read response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            print(f"← {json.dumps(response, indent=2)}")
            return response
        return None
    
    try:
        # Wait a moment for server to start
        time.sleep(1)
        
        # 1. Initialize
        print("\n1. Testing initialize...")
        init_response = send_message({
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            }
        })
        
        if not init_response or "error" in init_response:
            print("❌ Initialize failed")
            return False
        
        # 2. Send initialized notification
        print("\n2. Sending initialized notification...")
        send_message({
            "jsonrpc": "2.0",
            "method": "notifications/initialized"
        })
        
        # 3. List tools
        print("\n3. Testing list tools...")
        tools_response = send_message({
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list"
        })
        
        if not tools_response or "error" in tools_response:
            print("❌ List tools failed")
            return False
        
        tools = tools_response.get("result", {}).get("tools", [])
        print(f"✅ Found {len(tools)} tools")
        
        # 4. Test search
        print("\n4. Testing search...")
        search_response = send_message({
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "search_apple_docs",
                "arguments": {
                    "query": "Button",
                    "limit": 3
                }
            }
        })
        
        if not search_response or "error" in search_response:
            print("❌ Search failed")
            return False
        
        print("✅ Search completed")
        
        # 5. Test list frameworks
        print("\n5. Testing list frameworks...")
        frameworks_response = send_message({
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "list_frameworks",
                "arguments": {}
            }
        })
        
        if not frameworks_response or "error" in frameworks_response:
            print("❌ List frameworks failed")
            return False
        
        print("✅ List frameworks completed")
        
        print("\n✅ All tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False
    
    finally:
        # Clean up
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()

if __name__ == "__main__":
    success = test_mcp_server()
    sys.exit(0 if success else 1)