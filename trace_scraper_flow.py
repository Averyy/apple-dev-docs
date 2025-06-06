#!/usr/bin/env python3
"""Trace the exact flow of the scraper to find where it hangs"""

import asyncio
import sys
import time
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

# Global tracking
call_stack = []
url_visit_count = defaultdict(int)
start_times = {}

async def trace_scraper_execution(framework_id: str, max_urls: int = 200):
    """Trace scraper execution with detailed logging"""
    
    print(f"🔍 Tracing {framework_id} scraper execution (max {max_urls} URLs)")
    print()
    
    # Monkey patch the key methods to add tracing
    original_discover_and_scrape = AppleJSONDocumentationScraper._discover_and_scrape_from_json
    original_process_identifiers = AppleJSONDocumentationScraper._process_identifiers
    
    async def traced_discover_and_scrape(self, json_url, progress_file):
        # Track entry
        url_visit_count[json_url] += 1
        call_stack.append(json_url)
        start_times[json_url] = time.time()
        
        depth = len(call_stack)
        indent = "  " * (depth - 1)
        print(f"{indent}→ Entering: {json_url} (visit #{url_visit_count[json_url]})")
        
        if url_visit_count[json_url] > 2:
            print(f"{indent}⚠️  URL visited {url_visit_count[json_url]} times! Possible infinite loop")
            call_stack.pop()
            return
        
        if len(self.processed_urls) >= max_urls:
            print(f"{indent}🛑 Reached max URLs limit ({max_urls})")
            call_stack.pop()
            return
        
        try:
            result = await original_discover_and_scrape(self, json_url, progress_file)
            
            # Track exit
            elapsed = time.time() - start_times[json_url]
            print(f"{indent}← Exiting: {json_url} ({elapsed:.2f}s)")
            call_stack.pop()
            
            return result
            
        except Exception as e:
            print(f"{indent}❌ Error in {json_url}: {e}")
            call_stack.pop()
            raise
    
    async def traced_process_identifiers(self, identifiers):
        print(f"    Processing {len(identifiers)} identifiers")
        for i, identifier in enumerate(identifiers[:3]):  # Show first 3
            print(f"      {i+1}. {identifier}")
        if len(identifiers) > 3:
            print(f"      ... and {len(identifiers) - 3} more")
        
        return await original_process_identifiers(self, identifiers)
    
    # Apply patches
    AppleJSONDocumentationScraper._discover_and_scrape_from_json = traced_discover_and_scrape
    AppleJSONDocumentationScraper._process_identifiers = traced_process_identifiers
    
    try:
        async with AppleJSONDocumentationScraper(framework_id) as scraper:
            # Create a custom progress file for testing
            progress_file = Path(f"trace_{framework_id}_progress.txt")
            
            # Start scraping
            print("Starting scrape...")
            await scraper.discover_and_scrape_streaming()
            
            print(f"\n✅ Completed!")
            print(f"Total URLs processed: {len(scraper.processed_urls)}")
            print(f"Pages scraped: {scraper.stats.get('pages_scraped', 0)}")
            
    except Exception as e:
        print(f"\n❌ Exception: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Print statistics
        print(f"\n📊 Statistics:")
        print(f"Total unique URLs visited: {len(url_visit_count)}")
        print(f"Current call stack depth: {len(call_stack)}")
        
        # Find URLs visited multiple times
        multi_visits = [(url, count) for url, count in url_visit_count.items() if count > 1]
        if multi_visits:
            print(f"\n⚠️  URLs visited multiple times:")
            for url, count in sorted(multi_visits, key=lambda x: x[1], reverse=True)[:5]:
                print(f"  {count}x: {url}")
        
        # Show current call stack if still active
        if call_stack:
            print(f"\n📚 Current call stack:")
            for i, url in enumerate(call_stack):
                print(f"  {i}: {url}")

async def main():
    if len(sys.argv) < 2:
        print("Usage: python trace_scraper_flow.py <framework_id> [max_urls]")
        print("Example: python trace_scraper_flow.py accelerate 50")
        sys.exit(1)
    
    framework_id = sys.argv[1]
    max_urls = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    
    await trace_scraper_execution(framework_id, max_urls)

if __name__ == "__main__":
    asyncio.run(main())