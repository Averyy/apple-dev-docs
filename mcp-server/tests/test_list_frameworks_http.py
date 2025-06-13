#!/usr/bin/env python3
"""
Test list_frameworks via direct HTTP calls to understand the behavior
"""

import os
import httpx
import asyncio
import json
from pathlib import Path

# Load environment
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")

# Get config
MCP_API_KEY = os.getenv("MCP_API_KEY")
MCP_PORT = int(os.getenv("MCP_PORT", "8451"))

async def test_list_frameworks_http():
    """Test list_frameworks with different HTTP payloads"""
    
    base_url = f"http://localhost:{MCP_PORT}"
    headers = {"Authorization": f"Bearer {MCP_API_KEY}"}
    
    async with httpx.AsyncClient() as client:
        # Check if server is running
        try:
            health = await client.get(f"{base_url}/health")
            print(f"✅ Server is running: {health.json()['status']}")
        except Exception as e:
            print(f"❌ Server not running: {e}")
            print("Please start the server with: cd mcp-server && make server")
            return
        
        print("\n" + "="*60)
        print("Testing different list_frameworks payloads")
        print("="*60)
        
        # Test cases
        test_cases = [
            ("No arguments", {"name": "list_frameworks", "arguments": {}}),
            ("Empty platform", {"name": "list_frameworks", "arguments": {"platform": ""}}),
            ("Platform=None (JSON null)", {"name": "list_frameworks", "arguments": {"platform": None}}),
            ("Platform='all'", {"name": "list_frameworks", "arguments": {"platform": "all"}}),
            ("Platform='ios'", {"name": "list_frameworks", "arguments": {"platform": "ios"}}),
            ("Platform='ipados'", {"name": "list_frameworks", "arguments": {"platform": "ipados"}}),
            ("No arguments key", {"name": "list_frameworks"}),
        ]
        
        for test_name, payload in test_cases:
            print(f"\n🧪 Test: {test_name}")
            print(f"Payload: {json.dumps(payload, indent=2)}")
            
            try:
                response = await client.post(
                    f"{base_url}/mcp/tools/call",
                    headers=headers,
                    json=payload
                )
                
                if response.status_code == 200:
                    data = response.json()
                    result = data["result"]
                    
                    # Extract key info
                    lines = result.split('\n')
                    
                    # Find header
                    header = next((l for l in lines if l.startswith('#')), "No header")
                    print(f"Header: {header}")
                    
                    # Count frameworks
                    framework_lines = [l for l in lines if l.strip().startswith('- **')]
                    print(f"Frameworks count: {len(framework_lines)}")
                    
                    # Check for platform-specific content
                    if "IOS Frameworks" in result or "IPADOS Frameworks" in result:
                        print("➡️  Platform-specific response detected")
                    else:
                        print("➡️  All frameworks response")
                    
                    # Show first few frameworks
                    if framework_lines:
                        print("First 3 frameworks:")
                        for fw in framework_lines[:3]:
                            print(f"  {fw.strip()}")
                else:
                    print(f"❌ Error {response.status_code}: {response.text}")
                    
            except Exception as e:
                print(f"❌ Request failed: {e}")
        
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        print("If 'No arguments' shows platform-specific results, the issue is confirmed.")
        print("Check the server logs for platform parameter values.")


if __name__ == "__main__":
    asyncio.run(test_list_frameworks_http())