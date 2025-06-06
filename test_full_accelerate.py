#!/usr/bin/env python3
"""Test full Accelerate framework scraping with monitoring"""

import asyncio
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

async def test_full_framework():
    """Test scraping the full Accelerate framework"""
    
    print("🚀 Testing full Accelerate framework scraping")
    print("This will scrape ALL pages in the Accelerate framework")
    print()
    
    # Clear old progress file to start fresh
    progress_file = Path("documentation/accelerate/scraping_progress.txt")
    if progress_file.exists():
        progress_file.unlink()
        print("✓ Cleared old progress file")
    
    start_time = time.time()
    last_progress_time = start_time
    last_scraped_count = 0
    
    # Hook to monitor progress
    original_update_progress = AppleJSONDocumentationScraper._update_progress_file
    
    def monitored_update_progress(self, progress_file, last_url, final=False):
        nonlocal last_progress_time, last_scraped_count
        
        result = original_update_progress(self, progress_file, last_url, final)
        
        current_time = time.time()
        current_scraped = self.stats['pages_scraped']
        
        # Print progress every 30 seconds or every 50 pages
        if (current_time - last_progress_time > 30 or 
            current_scraped - last_scraped_count >= 50 or 
            final):
            
            elapsed = current_time - start_time
            rate = current_scraped / elapsed if elapsed > 0 else 0
            
            print(f"\n📊 Progress Update:")
            print(f"  Pages scraped: {current_scraped}")
            print(f"  Pages skipped: {self.stats['pages_skipped']}")
            print(f"  Pages failed: {self.stats['pages_failed']}")
            print(f"  Time elapsed: {elapsed:.1f}s")
            print(f"  Rate: {rate:.1f} pages/sec")
            if not final:
                print(f"  Last URL: {last_url}")
            
            last_progress_time = current_time
            last_scraped_count = current_scraped
        
        return result
    
    # Apply monitoring
    AppleJSONDocumentationScraper._update_progress_file = monitored_update_progress
    
    try:
        async with AppleJSONDocumentationScraper("accelerate", "Accelerate") as scraper:
            await scraper.discover_and_scrape_streaming()
            
            elapsed = time.time() - start_time
            
            print("\n✅ COMPLETED SUCCESSFULLY!")
            print(f"\n📊 Final Statistics:")
            print(f"  Total pages scraped: {scraper.stats['pages_scraped']}")
            print(f"  Total pages skipped: {scraper.stats['pages_skipped']}")
            print(f"  Total pages failed: {scraper.stats['pages_failed']}")
            print(f"  Total time: {elapsed:.1f}s ({elapsed/60:.1f} minutes)")
            print(f"  Average rate: {scraper.stats['pages_scraped']/elapsed:.1f} pages/sec")
            
    except KeyboardInterrupt:
        print("\n⏹️  Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

async def main():
    await test_full_framework()

if __name__ == "__main__":
    asyncio.run(main())