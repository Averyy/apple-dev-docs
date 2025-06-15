#!/usr/bin/env python3
"""
MCP Streamable HTTP Protocol Test Suite
Tests the new streamable HTTP implementation
"""

import asyncio
import httpx
import json
import os
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)

class StreamableHTTPTester:
    def __init__(self):
        self.api_key = os.getenv("MCP_API_KEY")
        if not self.api_key:
            raise ValueError("MCP_API_KEY not set in .env")
        
        self.base_url = "http://localhost:8080"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.test_results = []
        self.session_id = None
    
    def add_result(self, test_name: str, passed: bool, details: str):
        """Add a test result"""
        self.test_results.append({
            "test": test_name,
            "passed": passed,
            "details": details
        })
        print(f"{'✅' if passed else '❌'} {test_name}: {details}")
    
    async def test_health_endpoint(self):
        """Test 1: Health endpoint"""
        print("\n🧪 Test 1: Health Endpoint")
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.base_url}/health")
                passed = response.status_code == 200
                data = response.json() if passed else None
                
                if passed and data:
                    self.add_result(
                        "Health endpoint",
                        True,
                        f"Documents: {data['vectorstore']['documents']:,}, Transport: {data.get('transport', 'unknown')}"
                    )
                else:
                    self.add_result("Health endpoint", False, f"Status: {response.status_code}")
            except Exception as e:
                self.add_result("Health endpoint", False, str(e))
    
    async def test_initialize_handshake(self):
        """Test 2: Initialize/Initialized handshake"""
        print("\n🧪 Test 2: Initialize Handshake")
        async with httpx.AsyncClient() as client:
            try:
                # Send initialize request
                init_request = {
                    "jsonrpc": "2.0",
                    "id": "init-1",
                    "method": "initialize",
                    "params": {
                        "protocolVersion": "1.0.0",
                        "clientInfo": {
                            "name": "test-client",
                            "version": "1.0.0"
                        },
                        "capabilities": {}
                    }
                }
                
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers=self.headers,
                    json=init_request
                )
                
                if response.status_code != 200:
                    self.add_result("Initialize request", False, f"Status: {response.status_code}")
                    return
                
                data = response.json()
                
                # Check response
                if "error" in data:
                    self.add_result("Initialize request", False, f"Error: {data['error']['message']}")
                    return
                
                result = data.get("result", {})
                
                # Validate response structure
                checks = [
                    ("protocolVersion" in result, "Protocol version present"),
                    ("serverInfo" in result, "Server info present"),
                    ("capabilities" in result, "Capabilities present"),
                    (result.get("capabilities", {}).get("tools"), "Tools capability"),
                    (result.get("capabilities", {}).get("resources"), "Resources capability"),
                    (result.get("capabilities", {}).get("prompts"), "Prompts capability"),
                ]
                
                all_passed = True
                for check, desc in checks:
                    if not check:
                        self.add_result(f"Initialize - {desc}", False, "Missing")
                        all_passed = False
                
                if all_passed:
                    # Store session ID if provided
                    self.session_id = result.get("sessionId")
                    if response.headers.get("x-session-id"):
                        self.session_id = response.headers["x-session-id"]
                    
                    self.add_result(
                        "Initialize handshake",
                        True,
                        f"Server: {result['serverInfo']['name']} v{result['serverInfo']['version']}"
                    )
                    
                    # Send initialized notification
                    init_notif = {
                        "jsonrpc": "2.0",
                        "method": "initialized",
                        "params": {}
                    }
                    
                    headers = self.headers.copy()
                    if self.session_id:
                        headers["x-session-id"] = self.session_id
                    
                    notif_response = await client.post(
                        f"{self.base_url}/mcp",
                        headers=headers,
                        json=init_notif
                    )
                    
                    self.add_result(
                        "Initialized notification",
                        notif_response.status_code == 202,
                        f"Status: {notif_response.status_code}"
                    )
                        
            except Exception as e:
                self.add_result("Initialize handshake", False, f"Error: {type(e).__name__}: {e}")
    
    async def test_tools_list(self):
        """Test 3: tools/list"""
        print("\n🧪 Test 3: Tools List")
        async with httpx.AsyncClient() as client:
            try:
                request = {
                    "jsonrpc": "2.0",
                    "id": "tools-list",
                    "method": "tools/list"
                }
                
                headers = self.headers.copy()
                if self.session_id:
                    headers["x-session-id"] = self.session_id
                
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers=headers,
                    json=request
                )
                
                if response.status_code != 200:
                    self.add_result("tools/list", False, f"Status: {response.status_code}")
                    return
                
                data = response.json()
                
                if "error" in data:
                    self.add_result("tools/list", False, f"Error: {data['error']['message']}")
                    return
                
                tools = data.get("result", {}).get("tools", [])
                tool_names = [t["name"] for t in tools]
                
                self.add_result(
                    "tools/list",
                    len(tools) > 0,
                    f"Found {len(tools)} tools: {', '.join(tool_names)}"
                )
                
            except Exception as e:
                self.add_result("tools/list", False, f"Error: {e}")
    
    async def test_tools_call(self):
        """Test 4: tools/call - search_apple_docs"""
        print("\n🧪 Test 4: Tools Call (search)")
        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                request = {
                    "jsonrpc": "2.0",
                    "id": "search-1",
                    "method": "tools/call",
                    "params": {
                        "name": "search_apple_docs",
                        "arguments": {
                            "query": "SwiftUI Button",
                            "platform": "ios",
                            "limit": 2
                        }
                    }
                }
                
                headers = self.headers.copy()
                if self.session_id:
                    headers["x-session-id"] = self.session_id
                
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers=headers,
                    json=request
                )
                
                if response.status_code != 200:
                    self.add_result("tools/call search", False, f"Status: {response.status_code}")
                    return
                
                data = response.json()
                
                if "error" in data:
                    self.add_result("tools/call search", False, f"Error: {data['error']['message']}")
                    return
                
                content = data.get("result", {}).get("content", "")
                self.add_result(
                    "tools/call search",
                    len(content) > 0,
                    f"Got {len(content)} chars of results"
                )
                
            except Exception as e:
                self.add_result("tools/call search", False, f"Error: {e}")
    
    async def test_resources_list(self):
        """Test 5: resources/list"""
        print("\n🧪 Test 5: Resources List")
        async with httpx.AsyncClient() as client:
            try:
                request = {
                    "jsonrpc": "2.0",
                    "id": "res-list",
                    "method": "resources/list"
                }
                
                headers = self.headers.copy()
                if self.session_id:
                    headers["x-session-id"] = self.session_id
                
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers=headers,
                    json=request
                )
                
                if response.status_code != 200:
                    self.add_result("resources/list", False, f"Status: {response.status_code}")
                    return
                
                data = response.json()
                
                if "error" in data:
                    self.add_result("resources/list", False, f"Error: {data['error']['message']}")
                    return
                
                result = data.get("result", {})
                resources = result.get("resources", [])
                templates = result.get("resourceTemplates", [])
                
                self.add_result(
                    "resources/list",
                    True,
                    f"Found {len(resources)} resources, {len(templates)} templates"
                )
                
                # Test reading a resource if available
                if resources:
                    await self.test_resources_read(resources[0]["uri"])
                
            except Exception as e:
                self.add_result("resources/list", False, f"Error: {e}")
    
    async def test_resources_read(self, uri: str):
        """Test 6: resources/read"""
        print("\n🧪 Test 6: Resources Read")
        async with httpx.AsyncClient() as client:
            try:
                request = {
                    "jsonrpc": "2.0",
                    "id": "res-read",
                    "method": "resources/read",
                    "params": {
                        "uri": uri
                    }
                }
                
                headers = self.headers.copy()
                if self.session_id:
                    headers["x-session-id"] = self.session_id
                
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers=headers,
                    json=request
                )
                
                if response.status_code != 200:
                    self.add_result("resources/read", False, f"Status: {response.status_code}")
                    return
                
                data = response.json()
                
                if "error" in data:
                    self.add_result("resources/read", False, f"Error: {data['error']['message']}")
                    return
                
                result = data.get("result", {})
                self.add_result(
                    "resources/read",
                    "text" in result,
                    f"Read {uri}: {len(result.get('text', ''))} chars"
                )
                
            except Exception as e:
                self.add_result("resources/read", False, f"Error: {e}")
    
    async def test_prompts_list(self):
        """Test 7: prompts/list"""
        print("\n🧪 Test 7: Prompts List")
        async with httpx.AsyncClient() as client:
            try:
                request = {
                    "jsonrpc": "2.0",
                    "id": "prompts-list",
                    "method": "prompts/list"
                }
                
                headers = self.headers.copy()
                if self.session_id:
                    headers["x-session-id"] = self.session_id
                
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers=headers,
                    json=request
                )
                
                if response.status_code != 200:
                    self.add_result("prompts/list", False, f"Status: {response.status_code}")
                    return
                
                data = response.json()
                
                if "error" in data:
                    self.add_result("prompts/list", False, f"Error: {data['error']['message']}")
                    return
                
                prompts = data.get("result", {}).get("prompts", [])
                prompt_names = [p["name"] for p in prompts]
                
                self.add_result(
                    "prompts/list",
                    len(prompts) > 0,
                    f"Found {len(prompts)} prompts: {', '.join(prompt_names[:3])}..."
                )
                
                # Test getting a prompt
                if prompts:
                    await self.test_prompts_get(prompts[0]["name"])
                
            except Exception as e:
                self.add_result("prompts/list", False, f"Error: {e}")
    
    async def test_prompts_get(self, prompt_name: str):
        """Test 8: prompts/get"""
        print("\n🧪 Test 8: Prompts Get")
        async with httpx.AsyncClient() as client:
            try:
                # Use appropriate arguments based on prompt name
                args = {}
                if prompt_name == "explain_api":
                    args = {"api_name": "Button"}
                elif prompt_name == "compare_apis":
                    args = {"api1": "UIButton", "api2": "Button"}
                elif prompt_name == "migration_guide":
                    args = {"from_framework": "UIKit", "to_framework": "SwiftUI", "component": "Button"}
                elif prompt_name == "platform_availability":
                    args = {"api_name": "Button"}
                elif prompt_name == "code_example":
                    args = {"topic": "Button"}
                
                request = {
                    "jsonrpc": "2.0",
                    "id": "prompt-get",
                    "method": "prompts/get",
                    "params": {
                        "name": prompt_name,
                        "arguments": args
                    }
                }
                
                headers = self.headers.copy()
                if self.session_id:
                    headers["x-session-id"] = self.session_id
                
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers=headers,
                    json=request
                )
                
                if response.status_code != 200:
                    self.add_result("prompts/get", False, f"Status: {response.status_code}")
                    return
                
                data = response.json()
                
                if "error" in data:
                    self.add_result("prompts/get", False, f"Error: {data['error']['message']}")
                    return
                
                result = data.get("result", {})
                self.add_result(
                    "prompts/get",
                    "messages" in result,
                    f"Got prompt '{prompt_name}' with {len(result.get('messages', []))} messages"
                )
                
            except Exception as e:
                self.add_result("prompts/get", False, f"Error: {e}")
    
    async def test_batch_request(self):
        """Test 9: Batch requests"""
        print("\n🧪 Test 9: Batch Requests")
        async with httpx.AsyncClient() as client:
            try:
                batch = [
                    {
                        "jsonrpc": "2.0",
                        "id": "batch-1",
                        "method": "tools/list"
                    },
                    {
                        "jsonrpc": "2.0",
                        "id": "batch-2", 
                        "method": "resources/list"
                    }
                ]
                
                headers = self.headers.copy()
                if self.session_id:
                    headers["x-session-id"] = self.session_id
                
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers=headers,
                    json=batch
                )
                
                if response.status_code != 200:
                    self.add_result("Batch request", False, f"Status: {response.status_code}")
                    return
                
                data = response.json()
                
                self.add_result(
                    "Batch request",
                    isinstance(data, list) and len(data) == 2,
                    f"Got {len(data) if isinstance(data, list) else 0} responses"
                )
                
            except Exception as e:
                self.add_result("Batch request", False, f"Error: {e}")
    
    async def test_sse_stream(self):
        """Test 10: SSE Stream (GET /mcp)"""
        print("\n🧪 Test 10: SSE Stream")
        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                headers = self.headers.copy()
                headers["Accept"] = "text/event-stream"
                if self.session_id:
                    headers["x-session-id"] = self.session_id
                
                async with client.stream(
                    "GET",
                    f"{self.base_url}/mcp",
                    headers=headers
                ) as response:
                    
                    if response.status_code != 200:
                        self.add_result("SSE stream", False, f"Status: {response.status_code}")
                        return
                    
                    # Read first event
                    event_count = 0
                    async for line in response.aiter_lines():
                        if line.startswith("event:"):
                            event_type = line[6:].strip()
                        elif line.startswith("data:"):
                            try:
                                data = json.loads(line[5:])
                                event_count += 1
                                if event_count == 1:
                                    self.add_result(
                                        "SSE stream",
                                        True,
                                        f"Connected, first event: {event_type if 'event_type' in locals() else 'unknown'}"
                                    )
                                    return
                            except json.JSONDecodeError:
                                pass
                    
                    self.add_result("SSE stream", False, "No events received")
                    
            except Exception as e:
                self.add_result("SSE stream", False, f"Error: {e}")
    
    async def run_all_tests(self):
        """Run all streamable HTTP tests"""
        print("🚀 MCP Streamable HTTP Test Suite")
        print(f"🔑 Using API key: {self.api_key[:8]}...")
        print(f"🌐 Testing server at: {self.base_url}")
        print("=" * 60)
        
        # Run tests in order
        await self.test_health_endpoint()
        await self.test_initialize_handshake()
        await self.test_tools_list()
        await self.test_tools_call()
        await self.test_resources_list()
        await self.test_prompts_list()
        await self.test_batch_request()
        await self.test_sse_stream()
        
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
            print("\n✅ All tests passed! Streamable HTTP implementation is working.")
        
        return passed == total

async def main():
    """Run streamable HTTP tests"""
    tester = StreamableHTTPTester()
    success = await tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)