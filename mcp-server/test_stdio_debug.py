#!/usr/bin/env python3
"""Debug MCP stdio server"""

import json
import subprocess
import sys

def test_mcp_server():
    # Start the MCP server
    proc = subprocess.Popen(
        [sys.executable, "apple_docs_stdio_mcp.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Send initialize request
    initialize_request = {
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
    }
    
    proc.stdin.write(json.dumps(initialize_request) + "\n")
    proc.stdin.flush()
    
    # Read response
    response_line = proc.stdout.readline()
    if response_line:
        response = json.loads(response_line)
        print("Initialize Response:")
        print(json.dumps(response, indent=2))
    
    # Send initialized notification
    initialized_notif = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    }
    proc.stdin.write(json.dumps(initialized_notif) + "\n")
    proc.stdin.flush()
    
    # Send tools/list request
    list_request = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {}
    }
    
    proc.stdin.write(json.dumps(list_request) + "\n")
    proc.stdin.flush()
    
    # Read response
    response_line = proc.stdout.readline()
    if response_line:
        response = json.loads(response_line)
        print("\nTools List Response:")
        print(json.dumps(response, indent=2))
    
    # Check stderr for any errors
    proc.stdin.close()
    stderr = proc.stderr.read()
    if stderr:
        print("\nServer stderr:")
        print(stderr)
    
    proc.terminate()
    proc.wait()

if __name__ == "__main__":
    test_mcp_server()