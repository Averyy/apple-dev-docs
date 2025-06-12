#!/usr/bin/env python3
"""
Comprehensive test for MCP server functionality.
Tests all endpoints, authentication, search functionality, and error handling.
"""

import os
import sys
import json
import asyncio
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import httpx
from server.config import MCP_API_KEY, MCP_PORT


class TestMCPServer:
    """Comprehensive test suite for MCP server"""
    
    base_url = f"http://localhost:{MCP_PORT}"
    headers = {"Authorization": f"Bearer {MCP_API_KEY}"}
    
    
    async def test_health_endpoint(self, client):
        """Test health check endpoint (no auth required)"""
        response = await client.get(f"{self.base_url}/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "apple-docs-mcp"
        assert "vectorstore" in data
        assert data["vectorstore"]["documents"] > 300000  # Should have 323K+ docs
    
    
    async def test_auth_required(self, client):
        """Test that auth is required for MCP endpoints"""
        # Test without auth
        response = await client.get(f"{self.base_url}/mcp/tools/list")
        assert response.status_code == 403  # Forbidden without auth
        
        # Test with wrong auth
        wrong_headers = {"Authorization": "Bearer wrong_key"}
        response = await client.get(f"{self.base_url}/mcp/tools/list", headers=wrong_headers)
        assert response.status_code == 401  # Unauthorized with wrong key
    
    async def test_tools_list(self, client):
        """Test tools list endpoint"""
        response = await client.get(f"{self.base_url}/mcp/tools/list", headers=self.headers)
        assert response.status_code == 200
        data = response.json()
        
        # Check structure
        assert "tools" in data
        assert len(data["tools"]) == 2  # Should have 2 tools now
        
        # Check search_apple_docs tool
        search_tool = next(t for t in data["tools"] if t["name"] == "search_apple_docs")
        assert "description" in search_tool
        assert "inputSchema" in search_tool
        
        # Check search tool input schema
        schema = search_tool["inputSchema"]
        assert schema["type"] == "object"
        assert "query" in schema["properties"]
        assert "platform" in schema["properties"]  # New platform parameter
        assert schema["required"] == ["query"]
        
        # Check platform enum values
        platform_schema = schema["properties"]["platform"]
        assert "enum" in platform_schema
        assert "all" in platform_schema["enum"]
        assert "ios" in platform_schema["enum"]
        
        # Check list_frameworks tool
        list_tool = next(t for t in data["tools"] if t["name"] == "list_frameworks")
        assert "description" in list_tool
        assert "inputSchema" in list_tool
    
    async def test_search_basic(self, client):
        """Test basic search functionality"""
        payload = {
            "name": "search_apple_docs",
            "arguments": {
                "query": "SwiftUI Button"
            }
        }
        
        response = await client.post(
            f"{self.base_url}/mcp/tools/call",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "result" in data
        
        # Check result content
        result = data["result"]
        assert isinstance(result, str)
        assert "Found" in result  # Should say "Found X relevant documentation pages"
        assert "Button" in result or "button" in result.lower()
    
    async def test_search_with_framework(self, client):
        """Test search with framework filter"""
        payload = {
            "name": "search_apple_docs",
            "arguments": {
                "query": "async await",
                "framework": "Swift"
            }
        }
        
        response = await client.post(
            f"{self.base_url}/mcp/tools/call",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        result = data["result"]
        assert "Swift" in result or "async" in result.lower()
    
    async def test_search_with_limit(self, client):
        """Test search with custom limit"""
        payload = {
            "name": "search_apple_docs",
            "arguments": {
                "query": "URLSession",
                "limit": 2
            }
        }
        
        response = await client.post(
            f"{self.base_url}/mcp/tools/call",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        result = data["result"]
        
        # Should have at most 2 results
        assert result.count("## Result") <= 2 or result.count("1.") <= 2
    
    async def test_search_full_content(self, client):
        """Test search with full content mode"""
        payload = {
            "name": "search_apple_docs",
            "arguments": {
                "query": "NavigationView",
                "framework": "SwiftUI",
                "limit": 1,
                "include_full_content": True
            }
        }
        
        response = await client.post(
            f"{self.base_url}/mcp/tools/call",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        result = data["result"]
        
        # Full content should be much longer
        assert len(result) > 1000
        assert "## Result 1:" in result
        assert "### Metadata" in result
        assert "### Content" in result
    
    async def test_invalid_tool(self, client):
        """Test calling non-existent tool"""
        payload = {
            "name": "invalid_tool",
            "arguments": {}
        }
        
        response = await client.post(
            f"{self.base_url}/mcp/tools/call",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 404
        data = response.json()
        assert "not found" in data["detail"]
    
    async def test_missing_query(self, client):
        """Test search without required query parameter"""
        payload = {
            "name": "search_apple_docs",
            "arguments": {
                "framework": "SwiftUI"  # Missing required 'query'
            }
        }
        
        response = await client.post(
            f"{self.base_url}/mcp/tools/call",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 400
        data = response.json()
        assert "Invalid arguments" in data["detail"]
    
    async def test_edge_cases(self, client):
        """Test various edge cases"""
        # Empty query
        payload = {
            "name": "search_apple_docs",
            "arguments": {"query": ""}
        }
        response = await client.post(
            f"{self.base_url}/mcp/tools/call",
            headers=self.headers,
            json=payload
        )
        # Should handle empty query gracefully
        assert response.status_code in [200, 400]
        
        # Very long query
        payload = {
            "name": "search_apple_docs",
            "arguments": {"query": "a" * 1000}
        }
        response = await client.post(
            f"{self.base_url}/mcp/tools/call",
            headers=self.headers,
            json=payload
        )
        assert response.status_code == 200
        
        # Invalid limit
        payload = {
            "name": "search_apple_docs",
            "arguments": {"query": "test", "limit": 100}
        }
        response = await client.post(
            f"{self.base_url}/mcp/tools/call",
            headers=self.headers,
            json=payload
        )
        assert response.status_code == 200
        # Should clamp to MAX_SEARCH_LIMIT (20)
    
    async def test_search_with_platform(self, client):
        """Test search with platform filter"""
        payload = {
            "name": "search_apple_docs",
            "arguments": {
                "query": "Button",
                "platform": "ios"  # Filter to iOS only
            }
        }
        
        response = await client.post(
            f"{self.base_url}/mcp/tools/call",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        result = data["result"]
        assert "Found" in result
        # Should have platform info in results
        assert "[" in result and "]" in result  # Platform indicators
    
    async def test_list_frameworks(self, client):
        """Test list frameworks tool"""
        payload = {
            "name": "list_frameworks",
            "arguments": {}
        }
        
        response = await client.post(
            f"{self.base_url}/mcp/tools/call",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        result = data["result"]
        
        # Check result structure
        assert "Available Apple Frameworks" in result
        assert "Total frameworks indexed:" in result
        assert "Frameworks by Platform" in result or "Popular Frameworks" in result
        
        # Should have usage tips
        assert "Usage Tip" in result


async def run_all_tests():
    """Run all tests and report results"""
    print("🧪 Running comprehensive MCP server tests...\n")
    
    # Check if server is running
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://localhost:{MCP_PORT}/health", timeout=2)
            if response.status_code != 200:
                print("❌ MCP server is not healthy!")
                return False
    except Exception as e:
        print(f"❌ MCP server is not running! Start it with: make server")
        print(f"   Error: {e}")
        return False
    
    # Run tests
    test = TestMCPServer()
    async with httpx.AsyncClient() as client:
        tests = [
            ("Health Check", test.test_health_endpoint),
            ("Authentication", test.test_auth_required),
            ("Tools List", test.test_tools_list),
            ("Basic Search", test.test_search_basic),
            ("Search with Framework", test.test_search_with_framework),
            ("Search with Limit", test.test_search_with_limit),
            ("Search Full Content", test.test_search_full_content),
            ("Invalid Tool", test.test_invalid_tool),
            ("Missing Query", test.test_missing_query),
            ("Edge Cases", test.test_edge_cases),
            ("Search with Platform", test.test_search_with_platform),
            ("List Frameworks", test.test_list_frameworks),
        ]
        
        passed = 0
        failed = 0
        
        for test_name, test_func in tests:
            try:
                await test_func(client)
                print(f"✅ {test_name}")
                passed += 1
            except Exception as e:
                print(f"❌ {test_name}: {str(e)}")
                failed += 1
        
        print(f"\n📊 Results: {passed} passed, {failed} failed")
        return failed == 0


if __name__ == "__main__":
    # Run the tests
    success = asyncio.run(run_all_tests())
    sys.exit(0 if success else 1)