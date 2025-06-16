#!/usr/bin/env python3
"""
Comprehensive test for MCP server functionality.
Tests all endpoints, authentication, search functionality, and error handling.
Updated to use proper MCP JSON-RPC protocol.
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
            headers=self.headers,
            json=payload
        )
        return response
    
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
        response = await client.post(f"{self.base_url}/mcp", json={"jsonrpc": "2.0", "method": "tools/list", "id": 1})
        assert response.status_code == 403  # Forbidden without auth
        
        # Test with wrong auth
        wrong_headers = {"Authorization": "Bearer wrong_key"}
        response = await client.post(
            f"{self.base_url}/mcp",
            headers=wrong_headers,
            json={"jsonrpc": "2.0", "method": "tools/list", "id": 1}
        )
        assert response.status_code == 401  # Unauthorized with wrong key
    
    async def test_sse_endpoint(self, client):
        """Test SSE endpoint completes properly without hanging"""
        # Test that SSE connection completes within reasonable time
        response = await client.get(
            f"{self.base_url}/mcp",
            headers={**self.headers, "Accept": "text/event-stream"},
            timeout=3.0  # Should complete within 3 seconds
        )
        assert response.status_code == 200
        content = response.text
        
        # Should contain session event
        assert "event: session" in content
        assert "sessionId" in content
        
        # Should contain initialization message
        assert "event: message" in content
        assert "protocolVersion" in content
        assert "serverInfo" in content
        
        # Connection should have closed cleanly (not timed out)
        assert len(content) < 1000  # Should not have endless ping messages
    
    async def test_tools_list(self, client):
        """Test tools list endpoint"""
        response = await self.mcp_request(client, "tools/list")
        assert response.status_code == 200
        data = response.json()
        
        # Check JSON-RPC response structure
        assert data["jsonrpc"] == "2.0"
        assert "result" in data
        assert data["id"] == 1
        
        result = data["result"]
        # Check structure
        assert "tools" in result
        assert len(result["tools"]) == 2  # Should have 2 tools now
        
        # Check search_apple_docs tool
        search_tool = next(t for t in result["tools"] if t["name"] == "search_apple_docs")
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
        list_tool = next(t for t in result["tools"] if t["name"] == "list_frameworks")
        assert "description" in list_tool
        assert "inputSchema" in list_tool
    
    async def test_search_basic(self, client):
        """Test basic search functionality"""
        params = {
            "name": "search_apple_docs",
            "arguments": {
                "query": "SwiftUI Button"
            }
        }
        
        response = await self.mcp_request(client, "tools/call", params)
        
        assert response.status_code == 200
        data = response.json()
        assert data["jsonrpc"] == "2.0"
        assert "result" in data
        
        # Check result content
        result = data["result"]["content"]
        assert isinstance(result, str)
        assert "Found" in result  # Should say "Found X relevant documentation pages"
        assert "Button" in result or "button" in result.lower()
    
    async def test_search_with_framework(self, client):
        """Test search with framework filter"""
        params = {
            "name": "search_apple_docs",
            "arguments": {
                "query": "View",
                "framework": "SwiftUI",
                "limit": 5
            }
        }
        
        response = await self.mcp_request(client, "tools/call", params, request_id=2)
        
        assert response.status_code == 200
        data = response.json()
        result = data["result"]["content"]
        # Should find results for View in SwiftUI
        assert len(result) > 100, "Should have found results for View in SwiftUI"
        assert "swiftui" in result.lower(), "Results should mention SwiftUI framework"
    
    async def test_search_with_limit(self, client):
        """Test search with custom limit"""
        params = {
            "name": "search_apple_docs",
            "arguments": {
                "query": "URLSession",
                "limit": 2
            }
        }
        
        response = await self.mcp_request(client, "tools/call", params, request_id=3)
        
        assert response.status_code == 200
        data = response.json()
        result = data["result"]["content"]
        
        # Should have at most 2 results
        assert result.count("## Result") <= 2 or result.count("1.") <= 2
    
    async def test_search_full_content(self, client):
        """Test search with full content mode"""
        params = {
            "name": "search_apple_docs",
            "arguments": {
                "query": "array",
                "framework": "Foundation",
                "limit": 1,
                "include_full_content": True
            }
        }
        
        response = await self.mcp_request(client, "tools/call", params, request_id=4)
        
        assert response.status_code == 200
        data = response.json()
        result = data["result"]["content"]
        
        # Full content should be much longer
        assert len(result) > 1000, f"Full content should be >1000 chars, got {len(result)}"
        assert "## Result 1:" in result or "# Apple Documentation" in result, "Should have result header"
        assert "### Metadata" in result or "foundation" in result.lower(), "Should have metadata or framework info"
        assert "### Content" in result or len(result) > 2000, "Should have content section or be long"
    
    async def test_invalid_tool(self, client):
        """Test calling non-existent tool"""
        params = {
            "name": "invalid_tool",
            "arguments": {}
        }
        
        response = await self.mcp_request(client, "tools/call", params, request_id=5)
        
        assert response.status_code == 200  # JSON-RPC returns 200 with error in response
        data = response.json()
        assert "error" in data
        assert data["error"]["code"] == -32603  # Internal error
        assert "Unknown tool" in data["error"]["data"]
    
    async def test_missing_query(self, client):
        """Test search without required query parameter"""
        params = {
            "name": "search_apple_docs",
            "arguments": {
                "framework": "SwiftUI"  # Missing required 'query'
            }
        }
        
        response = await self.mcp_request(client, "tools/call", params, request_id=6)
        
        assert response.status_code == 200  # JSON-RPC returns 200 with error
        data = response.json()
        assert "error" in data
        # Should have error about missing query
    
    async def test_edge_cases(self, client):
        """Test various edge cases"""
        # Empty query
        params = {
            "name": "search_apple_docs",
            "arguments": {"query": ""}
        }
        response = await self.mcp_request(client, "tools/call", params, request_id=7)
        # Should handle empty query gracefully
        assert response.status_code == 200
        
        # Very long query
        params = {
            "name": "search_apple_docs",
            "arguments": {"query": "a" * 1000}
        }
        response = await self.mcp_request(client, "tools/call", params, request_id=8)
        assert response.status_code == 200
        
        # Invalid limit
        params = {
            "name": "search_apple_docs",
            "arguments": {"query": "test", "limit": 100}
        }
        response = await self.mcp_request(client, "tools/call", params, request_id=9)
        assert response.status_code == 200
        # Should clamp to MAX_SEARCH_LIMIT (20)
    
    async def test_search_with_platform(self, client):
        """Test search with platform filter"""
        params = {
            "name": "search_apple_docs",
            "arguments": {
                "query": "Button",
                "platform": "ios"
            }
        }
        
        response = await self.mcp_request(client, "tools/call", params, request_id=10)
        
        assert response.status_code == 200
        data = response.json()
        result = data["result"]["content"]
        assert "Found" in result
        # Should have platform info in results
        assert "[" in result and "]" in result  # Platform indicators
    
    async def test_list_frameworks(self, client):
        """Test list frameworks tool"""
        # Test 1: No arguments (should show all frameworks)
        params = {
            "name": "list_frameworks",
            "arguments": {}
        }
        
        response = await self.mcp_request(client, "tools/call", params, request_id=11)
        
        assert response.status_code == 200
        data = response.json()
        result = data["result"]["content"]
        
        # Check result structure for all frameworks
        assert "Available Apple Frameworks" in result or "# Available Apple Frameworks" in result
        assert "Total frameworks" in result
        
        # Extract the actual count from the result
        lines = result.split('\n')
        total_line = [l for l in lines if "Total frameworks" in l][0]
        # Extract number from format like "Total frameworks indexed: **360**"
        import re
        match = re.search(r'\*\*(\d+)\*\*', total_line)
        assert match, f"Could not find framework count in: {total_line}"
        total_count = int(match.group(1))
        
        # Count actual framework lines
        framework_lines = [l for l in lines if l.strip().startswith('- **')]
        assert len(framework_lines) == total_count, f"Expected {total_count} frameworks (from header), got {len(framework_lines)}"
        
        # Verify we have a reasonable number of frameworks
        assert total_count > 300, f"Expected 300+ frameworks, got {total_count}"
        
        # Check for known popular frameworks
        result_lower = result.lower()
        assert "swiftui" in result_lower, "Should include SwiftUI"
        assert "foundation" in result_lower, "Should include Foundation"
        assert "uikit" in result_lower, "Should include UIKit"
        
        # Should have usage tips
        assert "Usage Tip" in result
        
        # Test 2: Platform = "ios" (should show only iOS frameworks)
        params_ios = {
            "name": "list_frameworks",
            "arguments": {"platform": "ios"}
        }
        
        response_ios = await self.mcp_request(client, "tools/call", params_ios, request_id=12)
        
        assert response_ios.status_code == 200
        data_ios = response_ios.json()
        result_ios = data_ios["result"]["content"]
        
        # Should have iOS-specific header
        assert "IOS Frameworks" in result_ios or "iOS Frameworks" in result_ios
        # Should have fewer frameworks than all
        framework_lines_ios = [l for l in result_ios.split('\n') if l.strip().startswith('- **')]
        assert len(framework_lines_ios) < len(framework_lines), f"iOS frameworks ({len(framework_lines_ios)}) should be fewer than all ({len(framework_lines)})"
        assert len(framework_lines_ios) > 50, f"Expected 50+ iOS frameworks, got {len(framework_lines_ios)}"


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
    # Use longer timeout for list_frameworks which can be slow
    async with httpx.AsyncClient(timeout=httpx.Timeout(60.0)) as client:
        tests = [
            ("Health Check", test.test_health_endpoint),
            ("Authentication", test.test_auth_required),
            ("SSE Endpoint (Fixed!)", test.test_sse_endpoint),
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