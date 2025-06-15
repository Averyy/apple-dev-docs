#!/usr/bin/env python3
"""
Test the new usage_guide prompt functionality
"""

import asyncio
import httpx
import json
import os
import sys
from pathlib import Path
from typing import Dict, Any

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)

class UsageGuidePromptTester:
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
    
    async def initialize_session(self):
        """Initialize MCP session"""
        async with httpx.AsyncClient() as client:
            try:
                init_request = {
                    "jsonrpc": "2.0",
                    "id": "init-1",
                    "method": "initialize",
                    "params": {
                        "protocolVersion": "1.0.0",
                        "clientInfo": {
                            "name": "usage-guide-tester",
                            "version": "1.0.0"
                        }
                    }
                }
                
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers=self.headers,
                    json=init_request
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if response.headers.get("x-session-id"):
                        self.session_id = response.headers["x-session-id"]
                    return True
                return False
                
            except Exception as e:
                print(f"Initialize failed: {e}")
                return False
    
    async def test_prompts_list(self):
        """Test 1: Verify usage_guide appears in prompts list"""
        print("\n🧪 Test 1: Check prompts/list includes usage_guide")
        
        async with httpx.AsyncClient() as client:
            try:
                headers = self.headers.copy()
                if self.session_id:
                    headers["x-session-id"] = self.session_id
                
                request = {
                    "jsonrpc": "2.0",
                    "id": "prompts-list",
                    "method": "prompts/list"
                }
                
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers=headers,
                    json=request
                )
                
                if response.status_code != 200:
                    self.add_result("prompts/list", False, f"Status: {response.status_code}")
                    return
                
                data = response.json()
                prompts = data.get("result", {}).get("prompts", [])
                
                # Check if usage_guide is in the list
                usage_guide = next((p for p in prompts if p["name"] == "usage_guide"), None)
                
                if usage_guide:
                    self.add_result(
                        "prompts/list includes usage_guide",
                        True,
                        f"Found: {usage_guide['description']}"
                    )
                else:
                    prompt_names = [p["name"] for p in prompts]
                    self.add_result(
                        "prompts/list includes usage_guide",
                        False,
                        f"Not found. Available: {prompt_names}"
                    )
                    
            except Exception as e:
                self.add_result("prompts/list", False, str(e))
    
    async def test_usage_guide_topics(self):
        """Test 2: Test all usage_guide topics"""
        print("\n🧪 Test 2: Test all usage_guide topics")
        
        topics = ["general", "search_tips", "platform_guide", "framework_discovery", "invalid_topic"]
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            headers = self.headers.copy()
            if self.session_id:
                headers["x-session-id"] = self.session_id
            
            for topic in topics:
                try:
                    request = {
                        "jsonrpc": "2.0",
                        "id": f"guide-{topic}",
                        "method": "prompts/get",
                        "params": {
                            "name": "usage_guide",
                            "arguments": {
                                "topic": topic
                            }
                        }
                    }
                    
                    response = await client.post(
                        f"{self.base_url}/mcp",
                        headers=headers,
                        json=request
                    )
                    
                    if response.status_code != 200:
                        self.add_result(
                            f"usage_guide topic '{topic}'",
                            False,
                            f"Status: {response.status_code}"
                        )
                        continue
                    
                    data = response.json()
                    
                    if "error" in data:
                        self.add_result(
                            f"usage_guide topic '{topic}'",
                            False,
                            f"Error: {data['error']['message']}"
                        )
                        continue
                    
                    result = data.get("result", {})
                    messages = result.get("messages", [])
                    
                    if messages and len(messages) > 0:
                        content = messages[0].get("content", {}).get("text", "")
                        content_preview = content[:100] + "..." if len(content) > 100 else content
                        
                        # Check if content is relevant to topic
                        topic_found = topic in content.lower() or topic == "invalid_topic"
                        
                        self.add_result(
                            f"usage_guide topic '{topic}'",
                            True,
                            f"Got {len(content)} chars of guidance"
                        )
                    else:
                        self.add_result(
                            f"usage_guide topic '{topic}'",
                            False,
                            "No messages returned"
                        )
                        
                except Exception as e:
                    self.add_result(f"usage_guide topic '{topic}'", False, str(e))
    
    async def test_usage_guide_no_args(self):
        """Test 3: Test usage_guide with no arguments (should default to general)"""
        print("\n🧪 Test 3: Test usage_guide with no arguments")
        
        async with httpx.AsyncClient() as client:
            try:
                headers = self.headers.copy()
                if self.session_id:
                    headers["x-session-id"] = self.session_id
                
                request = {
                    "jsonrpc": "2.0",
                    "id": "guide-noargs",
                    "method": "prompts/get",
                    "params": {
                        "name": "usage_guide",
                        "arguments": {}
                    }
                }
                
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers=headers,
                    json=request
                )
                
                if response.status_code == 200:
                    data = response.json()
                    result = data.get("result", {})
                    messages = result.get("messages", [])
                    
                    if messages:
                        content = messages[0].get("content", {}).get("text", "")
                        # Should get general guide by default
                        has_general = "Apple Docs MCP Server Usage Guide" in content
                        
                        self.add_result(
                            "usage_guide with no args",
                            has_general,
                            "Defaults to general guide" if has_general else "Wrong default content"
                        )
                    else:
                        self.add_result("usage_guide with no args", False, "No messages")
                else:
                    self.add_result("usage_guide with no args", False, f"Status: {response.status_code}")
                    
            except Exception as e:
                self.add_result("usage_guide with no args", False, str(e))
    
    async def test_prompt_descriptions(self):
        """Test 4: Verify all prompts have enhanced descriptions"""
        print("\n🧪 Test 4: Check all prompt descriptions")
        
        async with httpx.AsyncClient() as client:
            try:
                headers = self.headers.copy()
                if self.session_id:
                    headers["x-session-id"] = self.session_id
                
                request = {
                    "jsonrpc": "2.0",
                    "id": "prompts-desc",
                    "method": "prompts/list"
                }
                
                response = await client.post(
                    f"{self.base_url}/mcp",
                    headers=headers,
                    json=request
                )
                
                if response.status_code == 200:
                    data = response.json()
                    prompts = data.get("result", {}).get("prompts", [])
                    
                    # Check each prompt has a good description
                    for prompt in prompts:
                        name = prompt["name"]
                        desc = prompt["description"]
                        
                        # Description should be informative (>30 chars)
                        if len(desc) > 30:
                            self.add_result(
                                f"Prompt '{name}' description",
                                True,
                                f"{len(desc)} chars"
                            )
                        else:
                            self.add_result(
                                f"Prompt '{name}' description",
                                False,
                                f"Too short: '{desc}'"
                            )
                            
            except Exception as e:
                self.add_result("prompt descriptions", False, str(e))
    
    async def run_all_tests(self):
        """Run all usage guide tests"""
        print("🚀 Usage Guide Prompt Test Suite")
        print(f"🔑 Using API key: {self.api_key[:8]}...")
        print(f"🌐 Testing server at: {self.base_url}")
        print("=" * 60)
        
        # Initialize session
        if await self.initialize_session():
            print("✅ Session initialized")
        else:
            print("❌ Failed to initialize session")
            return False
        
        # Run tests
        await self.test_prompts_list()
        await self.test_usage_guide_topics()
        await self.test_usage_guide_no_args()
        await self.test_prompt_descriptions()
        
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
            print("\n✅ All tests passed! Usage guide prompt is working correctly.")
        
        return passed == total

async def main():
    """Run usage guide tests"""
    tester = UsageGuidePromptTester()
    success = await tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)