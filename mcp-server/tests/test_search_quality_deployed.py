#!/usr/bin/env python3
"""
Comprehensive search quality test for deployed MCP server

Tests various search patterns to ensure high-quality results.
"""

import asyncio
import aiohttp
import json
import re
import os
from pathlib import Path
import sys
from typing import Tuple, Optional, Dict, Any, List
from dataclasses import dataclass
import time

# Load environment variables
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from dotenv import load_dotenv
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)

# Configuration
API_KEY = os.getenv("MCP_API_KEY")
DEPLOYED_SERVER_URL = os.getenv("MCP_SERVER_URL", "https://mcp.xdocs.dev/mcp/")


@dataclass
class SearchTest:
    """Test case for search quality"""
    query: str
    expected_terms: List[str]  # Terms that should appear in top results
    expected_framework: Optional[str] = None
    platform: str = "ios"
    description: str = ""


class SearchQualityTester:
    """Test search quality on deployed server"""
    
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
    
    async def initialize_session(self, session: aiohttp.ClientSession) -> Optional[Dict[str, str]]:
        """Initialize MCP session and return headers with session ID"""
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/event-stream'
        }
        
        # Initialize
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "clientInfo": {
                    "name": "search-quality-test",
                    "version": "1.0.0"
                }
            }
        }
        
        result, session_id = await self.send_request(session, init_request, headers)
        if not result or "result" not in result:
            print(f"❌ Initialize failed: {result}")
            return None
            
        self.session_id = session_id
        headers['MCP-Session-Id'] = self.session_id
        
        # Send initialized notification
        init_notif = {
            "jsonrpc": "2.0",
            "method": "notifications/initialized"
        }
        await session.post(self.server_url, json=init_notif, headers=headers)
        
        return headers
    
    async def search(self, session: aiohttp.ClientSession, headers: Dict[str, str], 
                     query: str, platform: str = "ios", limit: int = 5) -> Optional[List[Dict[str, Any]]]:
        """Perform search and return results"""
        search_request = {
            "jsonrpc": "2.0",
            "id": f"search-{query[:20]}",
            "method": "tools/call",
            "params": {
                "name": "search_apple_docs",
                "arguments": {
                    "query": query,
                    "platform": platform,
                    "summary_mode": True,  # Use summary mode for quality test
                    "limit": limit
                }
            }
        }
        
        start_time = time.time()
        result, _ = await self.send_request(session, search_request, headers)
        search_time = (time.time() - start_time) * 1000  # Convert to ms
        
        if result and "result" in result:
            content = result.get("result", {}).get("content", [])
            
            # Parse results from MCP response
            if isinstance(content, list) and len(content) > 0:
                text_content = content[0].get("text", "") if isinstance(content[0], dict) else str(content[0])
                
                
                # Extract individual results using simple parsing
                results = []
                
                # Split by result number pattern "1. **", "2. **", etc.
                parts = re.split(r'\n\d+\.\s+\*\*', text_content)
                
                for i, part in enumerate(parts[1:], 1):  # Skip first part (header)
                    if not part.strip():
                        continue
                    
                    lines = part.split('\n')
                    
                    # Extract title (first line up to **)
                    title_match = re.match(r'([^*]+)\*\*', lines[0])
                    title = title_match.group(1).strip() if title_match else f"Result {i}"
                    
                    # Extract framework from title line
                    framework_match = re.search(r'\(([^)]+)\)', lines[0])
                    framework = framework_match.group(1) if framework_match else ""
                    
                    # Extract relevance
                    relevance = 0
                    for line in lines:
                        if '📊 Relevance:' in line:
                            try:
                                relevance = int(re.search(r'(\d+)%', line).group(1))
                            except:
                                pass
                            break
                    
                    # Extract content (everything after the dashes)
                    content = ""
                    dash_found = False
                    for line in lines:
                        if '---' in line:
                            dash_found = True
                            continue
                        if dash_found:
                            content += line + '\n'
                    
                    results.append({
                        'title': title,
                        'framework': framework,
                        'relevance': relevance,
                        'content': content.strip()
                    })
                
                return {
                    'results': results,
                    'search_time_ms': search_time,
                    'total_found': len(results)
                }
        
        return None
    
    async def test_search_quality(self):
        """Run comprehensive search quality tests"""
        
        # Define test cases
        test_cases = [
            # Basic API searches
            SearchTest(
                query="Button SwiftUI",
                expected_terms=["Button", "SwiftUI", "struct"],
                expected_framework="SwiftUI",
                description="Basic SwiftUI component search"
            ),
            
            SearchTest(
                query="URLSession",
                expected_terms=["URLSession", "class", "network"],
                expected_framework="Foundation",
                description="Foundation networking class"
            ),
            
            # Specific method/property searches
            SearchTest(
                query="NavigationView navigationBarTitle",
                expected_terms=["navigationBarTitle", "NavigationView", "modifier"],
                expected_framework="SwiftUI",
                description="SwiftUI modifier search"
            ),
            
            # Cross-framework searches
            SearchTest(
                query="async await Swift",
                expected_terms=["async", "await", "concurrency"],
                description="Modern Swift concurrency"
            ),
            
            # Framework-specific searches
            SearchTest(
                query="CPTemplateApplicationScene CarPlay",
                expected_terms=["CPTemplateApplicationScene", "CarPlay", "class"],
                expected_framework="CarPlay",
                description="CarPlay specific API"
            ),
            
            # Entitlements search
            SearchTest(
                query="carplay entitlements",
                expected_terms=["entitlement", "carplay", "com.apple.developer"],
                description="CarPlay entitlements"
            ),
            
            # Error/edge case handling
            SearchTest(
                query="AsyncImagePhase failure",
                expected_terms=["AsyncImagePhase", "Failure", "enum"],
                expected_framework="SwiftUI",
                description="Specific enum case search"
            ),
            
            # Common patterns
            SearchTest(
                query="@State property wrapper",
                expected_terms=["State", "property wrapper", "SwiftUI"],
                expected_framework="SwiftUI",
                description="SwiftUI property wrapper"
            ),
            
            # Platform-specific
            SearchTest(
                query="WKWebView",
                expected_terms=["WKWebView", "WebKit", "class"],
                expected_framework="WebKit",
                platform="ios",
                description="WebKit view class"
            ),
            
            # Ambiguous queries
            SearchTest(
                query="frame",
                expected_terms=["frame"],
                description="Ambiguous term that could match many APIs"
            )
        ]
        
        print("🔍 Testing Search Quality on Deployed Server")
        print("=" * 80)
        
        timeout = aiohttp.ClientTimeout(total=60)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            # Initialize session
            headers = await self.initialize_session(session)
            if not headers:
                print("❌ Failed to initialize session")
                return
            
            print("✅ Session initialized\n")
            
            # Run test cases
            total_tests = len(test_cases)
            passed_tests = 0
            total_search_time = 0
            relevance_scores = []
            
            for i, test in enumerate(test_cases, 1):
                print(f"\n{'='*60}")
                print(f"Test {i}/{total_tests}: {test.description}")
                print(f"Query: '{test.query}'")
                print(f"Platform: {test.platform}")
                
                # Perform search
                search_result = await self.search(session, headers, test.query, test.platform)
                
                if not search_result:
                    print("❌ Search failed - no results returned")
                    continue
                
                results = search_result['results']
                search_time = search_result['search_time_ms']
                total_search_time += search_time
                
                print(f"\n📊 Results: {len(results)} found in {search_time:.0f}ms")
                
                # Analyze results
                test_passed = True
                found_terms = set()
                
                # Check top 3 results
                for j, result in enumerate(results[:3]):
                    print(f"\n  {j+1}. {result['title']}")
                    if result['framework']:
                        print(f"     Framework: {result['framework']}")
                    print(f"     Relevance: {result['relevance']}%")
                    
                    relevance_scores.append(result['relevance'])
                    
                    # Check for expected terms
                    content_lower = (result['title'] + ' ' + result['content']).lower()
                    for term in test.expected_terms:
                        if term.lower() in content_lower:
                            found_terms.add(term)
                    
                    # First result should be highly relevant
                    if j == 0 and result['relevance'] < 20:
                        print(f"     ⚠️  Low relevance for top result")
                        test_passed = False
                
                # Check if expected terms were found
                missing_terms = set(test.expected_terms) - found_terms
                if missing_terms:
                    print(f"\n  ⚠️  Missing expected terms: {missing_terms}")
                    test_passed = False
                
                # Check framework if specified
                if test.expected_framework and results:
                    if results[0]['framework'] != test.expected_framework:
                        print(f"  ⚠️  Expected framework '{test.expected_framework}' but got '{results[0]['framework']}'")
                        test_passed = False
                
                if test_passed:
                    print("\n  ✅ Test PASSED")
                    passed_tests += 1
                else:
                    print("\n  ❌ Test FAILED")
            
            # Summary
            print(f"\n{'='*80}")
            print("📊 Search Quality Summary")
            print("=" * 80)
            print(f"Tests passed: {passed_tests}/{total_tests} ({passed_tests/total_tests*100:.1f}%)")
            print(f"Average search time: {total_search_time/total_tests:.0f}ms")
            
            if relevance_scores:
                avg_relevance = sum(relevance_scores) / len(relevance_scores)
                print(f"Average relevance score: {avg_relevance:.1f}%")
                print(f"Relevance range: {min(relevance_scores)}% - {max(relevance_scores)}%")
            
            # Quality assessment
            print(f"\n🎯 Quality Assessment:")
            if passed_tests == total_tests:
                print("✅ EXCELLENT - All search tests passed!")
            elif passed_tests >= total_tests * 0.8:
                print("✅ GOOD - Most searches return relevant results")
            elif passed_tests >= total_tests * 0.6:
                print("⚠️  FAIR - Some search quality issues detected")
            else:
                print("❌ POOR - Significant search quality problems")
            
            if total_search_time/total_tests > 1000:
                print("⚠️  Search performance is slow (>1s average)")
            else:
                print("✅ Search performance is good")


async def main():
    """Run search quality tests"""
    tester = SearchQualityTester()
    await tester.test_search_quality()


if __name__ == "__main__":
    asyncio.run(main())