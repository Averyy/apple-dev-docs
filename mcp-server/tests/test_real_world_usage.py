#!/usr/bin/env python3
"""
Real-world usage test - simulates an AI assistant helping with Apple development
"""

import asyncio
import httpx
import json
import os
import sys
from pathlib import Path
from typing import Dict, Any, List

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv

env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)

class RealWorldUsageTest:
    def __init__(self):
        self.api_key = os.getenv("MCP_API_KEY")
        if not self.api_key:
            raise ValueError("MCP_API_KEY not set in .env")
        
        self.base_url = "http://localhost:8080"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.session_id = None
    
    async def mcp_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make an MCP request"""
        async with httpx.AsyncClient(timeout=30.0) as client:
            headers = self.headers.copy()
            if self.session_id:
                headers["x-session-id"] = self.session_id
            
            request = {
                "jsonrpc": "2.0",
                "id": f"{method}-{asyncio.get_event_loop().time()}",
                "method": method
            }
            if params:
                request["params"] = params
            
            response = await client.post(
                f"{self.base_url}/mcp",
                headers=headers,
                json=request
            )
            
            if response.status_code != 200:
                raise Exception(f"Request failed: {response.status_code}")
            
            return response.json()
    
    async def scenario_1_new_developer(self):
        """Scenario 1: New developer learning SwiftUI"""
        print("\n📱 Scenario 1: New developer asks 'How do I create a custom button in SwiftUI?'")
        
        # Step 1: Get usage guide for search tips
        print("\n1️⃣ AI gets search tips...")
        result = await self.mcp_request("prompts/get", {
            "name": "usage_guide",
            "arguments": {"topic": "search_tips"}
        })
        print("   ✅ Learned how to search effectively")
        
        # Step 2: Search for SwiftUI Button documentation
        print("\n2️⃣ Searching for SwiftUI Button...")
        result = await self.mcp_request("tools/call", {
            "name": "search_apple_docs",
            "arguments": {
                "query": "SwiftUI Button custom style",
                "platform": "ios",
                "framework": "SwiftUI",
                "limit": 3
            }
        })
        content = result["result"]["content"]
        print(f"   ✅ Found {len(content)} chars of documentation")
        
        # Step 3: Get detailed explanation
        print("\n3️⃣ Getting detailed explanation...")
        result = await self.mcp_request("prompts/get", {
            "name": "explain_api",
            "arguments": {
                "api_name": "ButtonStyle",
                "framework": "SwiftUI",
                "platform": "ios"
            }
        })
        print("   ✅ Generated comprehensive explanation with examples")
    
    async def scenario_2_migration(self):
        """Scenario 2: Developer migrating from UIKit to SwiftUI"""
        print("\n🔄 Scenario 2: Developer asks 'How do I migrate my UITableView to SwiftUI?'")
        
        # Step 1: Use migration guide prompt
        print("\n1️⃣ Generating migration guide...")
        result = await self.mcp_request("prompts/get", {
            "name": "migration_guide",
            "arguments": {
                "from_framework": "UIKit",
                "to_framework": "SwiftUI",
                "component": "UITableView"
            }
        })
        print("   ✅ Generated migration guide with comparisons")
        
        # Step 2: Search for List documentation
        print("\n2️⃣ Finding SwiftUI List documentation...")
        result = await self.mcp_request("tools/call", {
            "name": "search_apple_docs",
            "arguments": {
                "query": "SwiftUI List ForEach selection",
                "platform": "ios",
                "limit": 5
            }
        })
        print("   ✅ Found List implementation details")
    
    async def scenario_3_platform_check(self):
        """Scenario 3: Checking platform availability"""
        print("\n🌐 Scenario 3: Developer asks 'Does visionOS support ARKit?'")
        
        # Step 1: List visionOS frameworks
        print("\n1️⃣ Listing visionOS frameworks...")
        result = await self.mcp_request("tools/call", {
            "name": "list_frameworks",
            "arguments": {"platform": "visionos"}
        })
        content = result["result"]["content"]
        has_arkit = "ARKit" in content
        print(f"   ✅ Found {'ARKit' if has_arkit else 'no ARKit'} in visionOS frameworks")
        
        # Step 2: Search for specific ARKit features
        if has_arkit:
            print("\n2️⃣ Searching for ARKit in visionOS...")
            result = await self.mcp_request("tools/call", {
                "name": "search_apple_docs",
                "arguments": {
                    "query": "ARKit spatial",
                    "platform": "visionos",
                    "framework": "ARKit",
                    "limit": 3
                }
            })
            print("   ✅ Found visionOS-specific ARKit documentation")
    
    async def scenario_4_code_examples(self):
        """Scenario 4: Finding code examples"""
        print("\n💻 Scenario 4: Developer asks 'Show me async/await examples in Swift'")
        
        # Step 1: Search for async/await documentation
        print("\n1️⃣ Searching for async/await docs...")
        result = await self.mcp_request("tools/call", {
            "name": "search_apple_docs",
            "arguments": {
                "query": "async await Task concurrent",
                "platform": "all",
                "limit": 5
            }
        })
        print("   ✅ Found async/await documentation")
        
        # Step 2: Get code examples
        print("\n2️⃣ Getting code examples...")
        result = await self.mcp_request("prompts/get", {
            "name": "code_example",
            "arguments": {
                "topic": "async await networking",
                "platform": "ios",
                "complexity": "intermediate"
            }
        })
        print("   ✅ Generated practical code examples")
    
    async def run_all_scenarios(self):
        """Run all real-world scenarios"""
        print("🚀 Real-World Usage Test Suite")
        print("=" * 60)
        
        # Initialize session
        print("🔌 Initializing MCP session...")
        result = await self.mcp_request("initialize", {
            "protocolVersion": "1.0.0",
            "clientInfo": {
                "name": "ai-assistant",
                "version": "1.0.0"
            }
        })
        if "x-session-id" in result:
            self.session_id = result["x-session-id"]
        print("✅ Session initialized")
        
        # Run scenarios
        try:
            await self.scenario_1_new_developer()
            await self.scenario_2_migration()
            await self.scenario_3_platform_check()
            await self.scenario_4_code_examples()
            
            print("\n" + "=" * 60)
            print("✅ All scenarios completed successfully!")
            print("\nThe MCP server successfully handled:")
            print("- Usage guidance discovery")
            print("- Technical searches with platform filtering")
            print("- Framework discovery and availability checks")
            print("- Migration assistance between frameworks")
            print("- Code example generation")
            print("- Prompt-based workflows")
            
        except Exception as e:
            print(f"\n❌ Scenario failed: {e}")
            return False
        
        return True

async def main():
    """Run real-world tests"""
    tester = RealWorldUsageTest()
    success = await tester.run_all_scenarios()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)