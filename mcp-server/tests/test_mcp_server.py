#!/usr/bin/env python3
"""
Test for MCP server functionality using streamable HTTP transport.
"""

import os
import sys
import json
import asyncio
import time
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import httpx
from server.config import MCP_PORT

class TestMCPServer:
    """Test suite for MCP server with HTTP transport"""
    
    # FastMCP uses port 8000 by default, not MCP_PORT
    base_url = "http://localhost:8000"
    
    async def mcp_request(self, client, method, params=None, request_id=1):
        """Make a JSON-RPC request to the MCP server"""
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "id": request_id
        }
        if params:
            payload["params"] = params
            
        response = await client.post(
            f"{self.base_url}/mcp",
            json=payload
        )
        return response
    
    async def test_server_running(self, client):
        """Test if server is running"""
        try:
            response = await client.get(f"{self.base_url}/", timeout=2)
            print(f"✅ Server is running at {self.base_url}")
            return True
        except:
            print(f"❌ Server is not running at {self.base_url}")
            return False
    
    async def test_initialize(self, client):
        """Test initialize endpoint"""
        params = {
            "protocolVersion": "1.0.0",
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
        
        response = await self.mcp_request(client, "initialize", params)
        assert response.status_code == 200
        data = response.json()
        
        # Check JSON-RPC response structure
        assert data["jsonrpc"] == "2.0"
        assert "result" in data
        assert data["id"] == 1
        
        result = data["result"]
        assert "protocolVersion" in result
        assert "serverInfo" in result
        assert result["serverInfo"]["name"] == "apple-docs-mcp"
        
        print("✅ Initialize test passed")
        return True
    
    async def test_tools_list(self, client):
        """Test tools list endpoint"""
        response = await self.mcp_request(client, "tools/list")
        assert response.status_code == 200
        data = response.json()
        
        # Check JSON-RPC response structure
        assert data["jsonrpc"] == "2.0"
        assert "result" in data
        
        result = data["result"]
        assert "tools" in result
        assert len(result["tools"]) == 2  # search_apple_docs and list_frameworks
        
        # Check search_apple_docs tool
        search_tool = next(t for t in result["tools"] if t["name"] == "search_apple_docs")
        assert "description" in search_tool
        assert "inputSchema" in search_tool
        
        print(f"✅ Tools list test passed - found {len(result['tools'])} tools")
        return True
    
    async def test_search_basic(self, client):
        """Test basic search functionality"""
        params = {
            "name": "search_apple_docs",
            "arguments": {
                "query": "SwiftUI Button",
                "limit": 2
            }
        }
        
        response = await self.mcp_request(client, "tools/call", params, request_id=2)
        
        assert response.status_code == 200
        data = response.json()
        assert data["jsonrpc"] == "2.0"
        assert "result" in data
        
        # Check result content
        result = data["result"]["content"]
        assert isinstance(result, str)
        assert "Found" in result
        assert len(result) > 100  # Should have some content
        
        print("✅ Search test passed")
        return True
    
    async def test_list_frameworks(self, client):
        """Test list frameworks tool"""
        params = {
            "name": "list_frameworks",
            "arguments": {}
        }
        
        response = await self.mcp_request(client, "tools/call", params, request_id=3)
        
        assert response.status_code == 200
        data = response.json()
        result = data["result"]["content"]
        
        assert "Available Apple Frameworks" in result
        assert "Total frameworks" in result
        
        print("✅ List frameworks test passed")
        return True
    
    async def test_resources(self, client):
        """Test resources endpoints"""
        # List resources
        response = await self.mcp_request(client, "resources/list", request_id=4)
        assert response.status_code == 200
        data = response.json()
        
        resources = data["result"]["resources"]
        assert len(resources) == 2  # frameworks and stats
        
        # Read a resource
        params = {"uri": "resource://stats"}
        response = await self.mcp_request(client, "resources/read", params, request_id=5)
        assert response.status_code == 200
        data = response.json()
        
        content = data["result"]["contents"][0]["text"]
        assert "Apple Documentation Index Statistics" in content
        assert "Total documents" in content
        
        print("✅ Resources test passed")
        return True
    
    async def test_prompts(self, client):
        """Test prompts endpoints"""
        # List prompts
        response = await self.mcp_request(client, "prompts/list", request_id=6)
        assert response.status_code == 200
        data = response.json()
        
        prompts = data["result"]["prompts"]
        assert len(prompts) == 2  # analyze_api and compare_frameworks
        
        print("✅ Prompts test passed")
        return True

async def run_all_tests():
    """Run all tests and report results"""
    print("🧪 Running MCP server tests (HTTP transport)...\n")
    
    # Check if server is running
    test = TestMCPServer()
    async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
        # First check if server is up
        if not await test.test_server_running(client):
            print("\n⚠️  Start the server first with: make server")
            return False
        
        tests = [
            ("Initialize", test.test_initialize),
            ("Tools List", test.test_tools_list),
            ("Search", test.test_search_basic),
            ("List Frameworks", test.test_list_frameworks),
            ("Resources", test.test_resources),
            ("Prompts", test.test_prompts),
        ]
        
        passed = 0
        failed = 0
        
        for test_name, test_func in tests:
            try:
                await test_func(client)
                passed += 1
            except Exception as e:
                print(f"❌ {test_name}: {str(e)}")
                failed += 1
        
        print(f"\n📊 Results: {passed} passed, {failed} failed")
        return failed == 0

if __name__ == "__main__":
    success = asyncio.run(run_all_tests())
    sys.exit(0 if success else 1)