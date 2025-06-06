#!/usr/bin/env python3
"""Test scraping a single framework with debugging"""

import asyncio
import sys
import time
import signal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

# Global to track progress
scraped_count = 0
last_url = None
start_time = None

def progress_handler(signum, frame):
    """Handler for progress check"""
    global scraped_count, last_url, start_time
    print(f"\n⏰ Progress check:")
    print(f"  Pages scraped: {scraped_count}")
    print(f"  Last URL: {last_url}")
    if start_time:
        elapsed = time.time() - start_time
        print(f"  Time elapsed: {elapsed:.1f}s")
        if scraped_count > 0:
            print(f"  Rate: {scraped_count / elapsed:.1f} pages/sec")

async def test_single_framework(framework_id: str, limit: int = None):
    """Test scraping a single framework with progress tracking"""
    global scraped_count, last_url, start_time
    
    print(f"🧪 Testing {framework_id} scraping")
    print(f"Limit: {limit or 'No limit'}")
    print()
    
    # Set up progress check every 30 seconds
    signal.signal(signal.SIGALRM, progress_handler)
    signal.alarm(30)
    
    start_time = time.time()
    
    try:
        # Hook into the scraper to track progress
        original_scrape_and_save = AppleJSONDocumentationScraper._scrape_and_save_url
        
        async def wrapped_scrape_and_save(self, url):
            global scraped_count, last_url
            last_url = url
            result = await original_scrape_and_save(self, url)
            if result:
                scraped_count += 1
                if scraped_count % 10 == 0:
                    print(f"✅ Progress: {scraped_count} pages scraped (last: {url})")
                # Reset alarm
                signal.alarm(30)
            return result
        
        # Monkey patch
        AppleJSONDocumentationScraper._scrape_and_save_url = wrapped_scrape_and_save
        
        # Add limit if requested
        if limit:
            original_discover_and_scrape = AppleJSONDocumentationScraper._discover_and_scrape_from_json
            call_count = 0
            
            async def limited_discover_and_scrape(self, json_url, progress_file):
                nonlocal call_count
                if call_count >= limit:
                    print(f"🛑 Reached limit of {limit} URLs")
                    return
                call_count += 1
                return await original_discover_and_scrape(self, json_url, progress_file)
            
            AppleJSONDocumentationScraper._discover_and_scrape_from_json = limited_discover_and_scrape
        
        # Create and run scraper
        async with AppleJSONDocumentationScraper(framework_id) as scraper:
            await scraper.discover_and_scrape_streaming()
            
            # Cancel alarm
            signal.alarm(0)
            
            print(f"\n📊 Final Statistics:")
            print(f"Pages scraped: {scraper.stats.get('pages_scraped', 0)}")
            print(f"Pages skipped: {scraper.stats.get('pages_skipped', 0)}")
            print(f"Pages failed: {scraper.stats.get('pages_failed', 0)}")
            print(f"Total time: {time.time() - start_time:.1f}s")
            
    except KeyboardInterrupt:
        signal.alarm(0)
        print(f"\n⏹️  Interrupted")
        print(f"Last URL: {last_url}")
        print(f"Pages scraped: {scraped_count}")
    except Exception as e:
        signal.alarm(0)
        print(f"\n❌ Exception: {e}")
        import traceback
        traceback.print_exc()
        print(f"\nLast URL: {last_url}")

async def main():
    if len(sys.argv) < 2:
        print("Usage: python test_accelerate_single_framework.py <framework_id> [limit]")
        print("Example: python test_accelerate_single_framework.py accelerate 200")
        sys.exit(1)
    
    framework_id = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
    
    await test_single_framework(framework_id, limit)

if __name__ == "__main__":
    asyncio.run(main())