#!/usr/bin/env python3
"""
Test deployed MCP server functionality

IMPORTANT: This test is for the DEPLOYED server, not localhost.
The deployed server requires:
1. Initialize with protocol version "2024-11-05"
2. Session management via MCP-Session-Id header
3. SSE (Server-Sent Events) response parsing
4. include_full_content: True to get link transformations
"""

import asyncio
import aiohttp
import json
import re
import os
from pathlib import Path
import sys
from typing import Tuple, Optional, Dict, Any

# Load environment variables
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from dotenv import load_dotenv
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)

# Configuration
API_KEY = os.getenv("MCP_API_KEY")
DEPLOYED_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://192.168.2.5:8080/mcp/")


class DeployedServerTest:
    """Test suite for deployed MCP server"""
    
    def __init__(self):
        self.api_key = API_KEY
        self.server_url = DEPLOYED_SERVER_URL
        self.session_id: Optional[str] = None
        
        if not self.api_key:
            raise ValueError("MCP_API_KEY not set in .env")
    
    async def send_request(self, session: aiohttp.ClientSession, payload: Dict[str, Any], 
                          headers: Dict[str, str]) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
        """Send request and parse SSE response"""
        async with session.post(self.server_url, json=payload, headers=headers) as response:
            if response.status != 200:
                return {"error": f"HTTP {response.status}"}, None
            
            # Get session ID if present
            session_id = response.headers.get('mcp-session-id')
            
            # Parse SSE response
            text = await response.text()
            for line in text.split('\n'):
                if line.startswith('data: '):
                    try:
                        return json.loads(line[6:]), session_id
                    except:
                        pass
            return None, session_id
    
    async def test_server_health(self):
        """Test 1: Check server health"""
        print("\n🧪 Test 1: Server Health Check")
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f"http://192.168.2.5:8080/health") as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"✅ Server healthy: {data['vectorstore']['documents']:,} documents")
                        return True
                    else:
                        print(f"❌ Health check failed: HTTP {response.status}")
                        return False
            except Exception as e:
                print(f"❌ Connection failed: {e}")
                return False
    
    async def test_complete_flow(self):
        """Test 2: Complete MCP flow with link transformation check"""
        print("\n🧪 Test 2: Complete MCP Flow")
        
        timeout = aiohttp.ClientTimeout(total=30)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json',
                'Accept': 'application/json, text/event-stream'
            }
            
            # Step 1: Initialize
            print("\n  1️⃣ Initializing...")
            init_request = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "clientInfo": {
                        "name": "test-client",
                        "version": "1.0.0"
                    }
                }
            }
            
            result, session_id = await self.send_request(session, init_request, headers)
            if not result or "result" not in result:
                print(f"  ❌ Initialize failed: {result}")
                return False
                
            self.session_id = session_id
            headers['MCP-Session-Id'] = self.session_id
            server_info = result['result']['serverInfo']
            print(f"  ✅ Initialized: {server_info['name']} v{server_info['version']}")
            
            # Step 2: Send initialized notification (required by some servers)
            init_notif = {
                "jsonrpc": "2.0",
                "method": "notifications/initialized"
            }
            
            # Send notification (no response expected)
            async with session.post(self.server_url, json=init_notif, headers=headers) as response:
                if response.status not in [200, 202]:
                    print(f"  ⚠️  Initialized notification failed: HTTP {response.status}")
            
            # Step 3: List tools
            print("\n  2️⃣ Listing tools...")
            list_request = {
                "jsonrpc": "2.0",
                "id": "list-1",
                "method": "tools/list",
                "params": {}  # Some servers require empty params object
            }
            
            result, _ = await self.send_request(session, list_request, headers)
            if result and "result" in result:
                tools = result.get("result", {}).get("tools", [])
                print(f"  ✅ Found {len(tools)} tools: {', '.join([t['name'] for t in tools])}")
            else:
                print(f"  ❌ Tools list failed: {result}")
                return False
            
            # Step 4: Test search with link transformation
            print("\n  3️⃣ Testing search with link transformation...")
            test_passed = await self.test_link_transformation(session, headers)
            
            return test_passed
    
    async def test_link_transformation(self, session: aiohttp.ClientSession, headers: Dict[str, str]) -> bool:
        """Test link transformation in search results"""
        
        # Test queries that should have links
        test_queries = [
            ("NavigationView", "SwiftUI navigation"),
            ("carplay entitlements", "CarPlay entitlements"),
            ("AsyncImagePhase", "SwiftUI async image")
        ]
        
        total_transformed = 0
        total_untransformed = 0
        tests_with_links = 0
        
        for query, description in test_queries:
            print(f"\n  📍 Testing: {description}")
            print(f"     Query: '{query}'")
            
            search_request = {
                "jsonrpc": "2.0",
                "id": f"search-{query[:10]}",
                "method": "tools/call",
                "params": {
                    "name": "search_apple_docs",
                    "arguments": {
                        "query": query,
                        "platform": "ios",
                        "include_full_content": True,  # CRITICAL: Must be True to get links
                        "limit": 2
                    }
                }
            }
            
            result, _ = await self.send_request(session, search_request, headers)
            
            if result and "result" in result:
                content = result.get("result", {}).get("content", [])
                
                # Handle content as list (MCP format)
                if isinstance(content, list) and len(content) > 0:
                    text_content = content[0].get("text", "") if isinstance(content[0], dict) else str(content[0])
                    
                    # Check for transformed and untransformed links
                    transformed = re.findall(r'\[([^\]]+)\]\(💡 Search: `([^`]+)`\)', text_content)
                    untransformed = re.findall(r'\[([^\]]+)\]\(([^)]+\.md)\)', text_content)
                    
                    if transformed or untransformed:
                        tests_with_links += 1
                        total_transformed += len(transformed)
                        total_untransformed += len(untransformed)
                        
                        print(f"     ✅ Found {len(transformed)} transformed links")
                        if untransformed:
                            print(f"     ❌ Found {len(untransformed)} untransformed links")
                        
                        # Show examples
                        if transformed and len(transformed) <= 3:
                            for text, search in transformed:
                                print(f"        • [{text}] → 💡 '{search}'")
                    else:
                        print(f"     ℹ️  No links found in results")
                else:
                    print(f"     ❌ Unexpected content format")
            else:
                print(f"     ❌ Search failed: {result}")
        
        # Summary
        print(f"\n  📊 Link Transformation Summary:")
        print(f"     Tests with links: {tests_with_links}/{len(test_queries)}")
        print(f"     Total transformed: {total_transformed}")
        print(f"     Total untransformed: {total_untransformed}")
        
        if total_untransformed == 0 and total_transformed > 0:
            print("\n  ✅ SUCCESS: All links are properly transformed!")
            return True
        elif total_transformed > 0:
            success_rate = (total_transformed / (total_transformed + total_untransformed)) * 100
            print(f"\n  ⚠️  PARTIAL: {success_rate:.1f}% of links are transformed")
            return False
        else:
            print("\n  ❌ FAILURE: No transformed links found")
            return False


async def main():
    """Run all tests"""
    print("🚀 Testing Deployed MCP Server")
    print(f"📍 Server: {DEPLOYED_SERVER_URL}")
    print("=" * 60)
    
    tester = DeployedServerTest()
    
    # Run tests
    tests_passed = 0
    total_tests = 2
    
    # Test 1: Health check
    if await tester.test_server_health():
        tests_passed += 1
    
    # Test 2: Complete flow with link transformation
    if await tester.test_complete_flow():
        tests_passed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"📊 Test Summary: {tests_passed}/{total_tests} passed")
    
    if tests_passed == total_tests:
        print("✅ All tests passed!")
        return 0
    else:
        print("❌ Some tests failed")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)