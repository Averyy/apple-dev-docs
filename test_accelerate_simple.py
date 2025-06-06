#!/usr/bin/env python3
"""
Simple test to run Accelerate scraper with detailed logging
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper

async def test_accelerate():
    """Test scraping Accelerate with detailed logging"""
    
    print("🚀 Starting Accelerate scraper test...")
    print("=" * 60)
    
    scraper = AppleJSONDocumentationScraper("accelerate", "Accelerate")
    
    # Override some settings for testing
    scraper._discovery_batch_size = 100  # Process fewer URLs at a time
    
    async with scraper:
        try:
            # Start the streaming scrape
            await scraper.discover_and_scrape_streaming()
            
            print("\n✅ Scraping completed successfully!")
            print(f"📊 Final stats:")
            print(f"  - Pages scraped: {scraper.stats['pages_scraped']}")
            print(f"  - Pages skipped: {scraper.stats['pages_skipped']}")
            print(f"  - Pages failed: {scraper.stats['pages_failed']}")
            
        except asyncio.TimeoutError:
            print("\n⏱️  Scraper timed out")
        except KeyboardInterrupt:
            print("\n⏹️  Stopped by user")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    # Check what was in the processed URLs
    print(f"\n📝 Processed URLs count: {len(scraper.processed_urls)}")
    
    # Check the last few processed URLs
    if scraper.processed_urls:
        processed_list = list(scraper.processed_urls)
        print("\nLast 5 processed URLs:")
        for url in processed_list[-5:]:
            print(f"  - {url}")

async def main():
    """Run with timeout"""
    try:
        # Run with a 5 minute timeout
        await asyncio.wait_for(test_accelerate(), timeout=300)
    except asyncio.TimeoutError:
        print("\n⏱️  Test timed out after 5 minutes")

if __name__ == "__main__":
    asyncio.run(main())