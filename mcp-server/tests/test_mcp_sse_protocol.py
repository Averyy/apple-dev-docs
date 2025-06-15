#!/usr/bin/env python3
"""
MCP SSE Protocol Test Suite
Tests SSE implementation for Claude Code compatibility
"""

import asyncio
import httpx
import json
import os
import time
import sys
from pathlib import Path
from typing import Dict, Any, List

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)

class MCPProtocolTester:
    def __init__(self):
        self.api_key = os.getenv("MCP_API_KEY")
        if not self.api_key:
            raise ValueError("MCP_API_KEY not set in .env")
        
        self.base_url = "http://localhost:8080"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        self.test_results = []
    
    def add_result(self, test_name: str, passed: bool, details: str):
        """Add a test result"""
        self.test_results.append({
            "test": test_name,
            "passed": passed,
            "details": details
        })
        print(f"{'✅' if passed else '❌'} {test_name}: {details}")
    
    async def test_health_endpoint(self):
        """Test 1: Health endpoint (no auth required)"""
        print("\n🧪 Test 1: Health Endpoint")
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.base_url}/health")
                passed = response.status_code == 200
                data = response.json() if passed else None
                
                if passed and data:
                    self.add_result(
                        "Health endpoint accessible",
                        True,
                        f"Documents: {data['vectorstore']['documents']:,}"
                    )
                else:
                    self.add_result("Health endpoint accessible", False, f"Status: {response.status_code}")
            except Exception as e:
                self.add_result("Health endpoint accessible", False, str(e))
    
    async def test_sse_connection(self):
        """Test 2: SSE Connection and Initial Message"""
        print("\n🧪 Test 2: SSE Connection")
        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                async with client.stream(
                    "GET",
                    f"{self.base_url}/mcp",
                    headers={
                        **self.headers,
                        "Accept": "text/event-stream"
                    }
                ) as response:
                    if response.status_code != 200:
                        self.add_result("SSE connection", False, f"Status: {response.status_code}")
                        return
                    
                    # Read first event
                    first_event = None
                    async for line in response.aiter_lines():
                        if line.startswith("data: "):
                            try:
                                first_event = json.loads(line[6:])
                                break
                            except json.JSONDecodeError as e:
                                self.add_result("SSE JSON format", False, f"Invalid JSON: {e}")
                                return
                    
                    if not first_event:
                        self.add_result("SSE initial event", False, "No event received")
                        return
                    
                    # Validate initial connection event
                    if first_event.get("method") == "connection":
                        params = first_event.get("params", {})
                        
                        # Check required fields
                        checks = [
                            ("jsonrpc" in first_event and first_event["jsonrpc"] == "2.0", "JSON-RPC 2.0 format"),
                            ("protocolVersion" in params, "Protocol version present"),
                            ("serverInfo" in params, "Server info present"),
                            ("capabilities" in params, "Capabilities present"),
                            (params.get("capabilities", {}).get("tools", {}).get("list"), "Tools list capability"),
                            (params.get("capabilities", {}).get("tools", {}).get("call"), "Tools call capability"),
                        ]
                        
                        all_passed = True
                        for check, desc in checks:
                            if not check:
                                self.add_result(f"SSE connection - {desc}", False, "Missing or invalid")
                                all_passed = False
                        
                        if all_passed:
                            self.add_result(
                                "SSE connection event",
                                True,
                                f"Server: {params['serverInfo']['name']} v{params['serverInfo']['version']}"
                            )
                    else:
                        self.add_result("SSE connection event", False, f"Wrong method: {first_event.get('method')}")
                        
            except Exception as e:
                self.add_result("SSE connection", False, f"Error: {type(e).__name__}: {e}")
    
    async def test_jsonrpc_tools_list(self):
        """Test 3: JSON-RPC tools/list method"""
        print("\n🧪 Test 3: JSON-RPC tools/list")
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers={**self.headers, "Content-Type": "application/json"},
                    json={
                        "jsonrpc": "2.0",
                        "id": "test-tools-list",
                        "method": "tools/list"
                    }
                )
                
                if response.status_code != 200:
                    self.add_result("JSON-RPC tools/list", False, f"Status: {response.status_code}")
                    return
                
                data = response.json()
                
                # Validate response format
                checks = [
                    ("jsonrpc" in data and data["jsonrpc"] == "2.0", "JSON-RPC 2.0 response"),
                    ("id" in data and data["id"] == "test-tools-list", "Correct request ID"),
                    ("result" in data, "Has result field"),
                    ("tools" in data.get("result", {}), "Has tools array"),
                    (len(data.get("result", {}).get("tools", [])) > 0, "Has at least one tool"),
                ]
                
                all_passed = True
                for check, desc in checks:
                    if not check:
                        self.add_result(f"tools/list - {desc}", False, "Failed validation")
                        all_passed = False
                
                if all_passed:
                    tools = data["result"]["tools"]
                    tool_names = [t["name"] for t in tools]
                    self.add_result(
                        "JSON-RPC tools/list",
                        True,
                        f"Found {len(tools)} tools: {', '.join(tool_names)}"
                    )
                    
                    # Validate tool schema
                    for tool in tools:
                        if "inputSchema" in tool and "properties" in tool["inputSchema"]:
                            self.add_result(
                                f"Tool schema - {tool['name']}",
                                True,
                                f"{len(tool['inputSchema']['properties'])} parameters"
                            )
                        
            except Exception as e:
                self.add_result("JSON-RPC tools/list", False, f"Error: {type(e).__name__}: {e}")
    
    async def test_jsonrpc_tool_call(self):
        """Test 4: JSON-RPC tools/call method"""
        print("\n🧪 Test 4: JSON-RPC tools/call")
        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers={**self.headers, "Content-Type": "application/json"},
                    json={
                        "jsonrpc": "2.0",
                        "id": "test-search",
                        "method": "tools/call",
                        "params": {
                            "name": "search_apple_docs",
                            "arguments": {
                                "query": "SwiftUI Button",
                                "platform": "ios",
                                "limit": 1
                            }
                        }
                    }
                )
                
                if response.status_code != 200:
                    self.add_result("JSON-RPC tools/call", False, f"Status: {response.status_code}")
                    return
                
                data = response.json()
                
                # Validate response
                checks = [
                    ("jsonrpc" in data and data["jsonrpc"] == "2.0", "JSON-RPC 2.0 response"),
                    ("id" in data and data["id"] == "test-search", "Correct request ID"),
                    ("result" in data, "Has result field"),
                    ("content" in data.get("result", {}), "Has content field"),
                ]
                
                all_passed = True
                for check, desc in checks:
                    if not check:
                        self.add_result(f"tools/call - {desc}", False, "Failed validation")
                        all_passed = False
                
                if all_passed:
                    content = data["result"]["content"]
                    self.add_result(
                        "JSON-RPC tools/call",
                        True,
                        f"Got search results ({len(content)} chars)"
                    )
                    
            except Exception as e:
                self.add_result("JSON-RPC tools/call", False, f"Error: {type(e).__name__}: {e}")
    
    async def test_error_handling(self):
        """Test 5: Error Handling"""
        print("\n🧪 Test 5: Error Handling")
        
        # Test invalid method
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers={**self.headers, "Content-Type": "application/json"},
                    json={
                        "jsonrpc": "2.0",
                        "id": "test-error",
                        "method": "invalid/method"
                    }
                )
                
                data = response.json()
                if "error" in data:
                    self.add_result(
                        "Error handling - invalid method",
                        True,
                        f"Error code: {data['error'].get('code')}, message: {data['error'].get('message')}"
                    )
                else:
                    self.add_result("Error handling - invalid method", False, "No error returned")
                    
            except Exception as e:
                self.add_result("Error handling", False, f"Exception: {e}")
    
    async def test_authentication(self):
        """Test 6: Authentication"""
        print("\n🧪 Test 6: Authentication")
        
        # Test without auth header
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.base_url}/mcp")
                self.add_result(
                    "Authentication required",
                    response.status_code == 401,
                    f"Status without auth: {response.status_code}"
                )
                
                # Test with invalid auth
                response = await client.get(
                    f"{self.base_url}/mcp",
                    headers={"Authorization": "Bearer invalid-key"}
                )
                self.add_result(
                    "Invalid auth rejected",
                    response.status_code == 401,
                    f"Status with bad auth: {response.status_code}"
                )
                
            except Exception as e:
                self.add_result("Authentication test", False, f"Exception: {e}")
    
    async def test_keepalive(self, wait_time: int = 5):
        """Test 7: SSE Keep-Alive (configurable wait time)"""
        print(f"\n🧪 Test 7: SSE Keep-Alive (waiting {wait_time}s)")
        
        async with httpx.AsyncClient(timeout=wait_time + 5) as client:
            try:
                async with client.stream(
                    "GET",
                    f"{self.base_url}/mcp",
                    headers={**self.headers, "Accept": "text/event-stream"}
                ) as response:
                    
                    if response.status_code != 200:
                        self.add_result("SSE keepalive", False, f"Connection failed: {response.status_code}")
                        return
                    
                    events_received = []
                    start_time = time.time()
                    
                    async for line in response.aiter_lines():
                        if line.startswith("data: "):
                            try:
                                event = json.loads(line[6:])
                                events_received.append(event)
                                
                                if event.get("method") == "heartbeat":
                                    elapsed = time.time() - start_time
                                    self.add_result(
                                        "SSE heartbeat",
                                        True,
                                        f"Received after {elapsed:.1f}s"
                                    )
                                    return
                                    
                            except json.JSONDecodeError:
                                pass
                        
                        # Timeout
                        if time.time() - start_time > wait_time:
                            self.add_result(
                                "SSE heartbeat",
                                False,
                                f"No heartbeat after {wait_time}s (got {len(events_received)} events)"
                            )
                            return
                            
            except Exception as e:
                self.add_result("SSE keepalive", False, f"Error: {e}")
    
    async def run_all_tests(self, skip_keepalive: bool = False):
        """Run all MCP protocol tests"""
        print("🚀 MCP SSE Protocol Test Suite")
        print(f"🔑 Using API key: {self.api_key[:8]}...")
        print(f"🌐 Testing server at: {self.base_url}")
        print("=" * 60)
        
        # Run tests in order
        await self.test_health_endpoint()
        await self.test_sse_connection()
        await self.test_jsonrpc_tools_list()
        await self.test_jsonrpc_tool_call()
        await self.test_error_handling()
        await self.test_authentication()
        
        if not skip_keepalive:
            await self.test_keepalive(wait_time=5)  # Short wait for automated tests
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 Test Summary")
        passed = sum(1 for r in self.test_results if r["passed"])
        total = len(self.test_results)
        
        print(f"\nTotal: {passed}/{total} tests passed ({passed/total*100:.0f}%)")
        
        if passed < total:
            print("\n❌ Failed tests:")
            for result in self.test_results:
                if not result["passed"]:
                    print(f"  - {result['test']}: {result['details']}")
        else:
            print("\n✅ All tests passed! MCP server is Claude Code compatible.")
        
        return passed == total

async def main():
    """Run MCP SSE protocol tests"""
    tester = MCPProtocolTester()
    success = await tester.run_all_tests(skip_keepalive=True)
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)