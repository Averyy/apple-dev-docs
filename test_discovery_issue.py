#!/usr/bin/env python3
"""
Test discovery issue - why scraper stops
"""

import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper

class DebugScraper(AppleJSONDocumentationScraper):
    """Scraper with extra debugging"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url_processing_count = 0
        self.last_processed_urls = []
    
    async def _discover_and_scrape_from_json(self, json_url: str, progress_file) -> None:
        """Override to add debugging"""
        self.url_processing_count += 1
        self.last_processed_urls.append(json_url)
        
        # Keep only last 10 URLs
        if len(self.last_processed_urls) > 10:
            self.last_processed_urls.pop(0)
        
        print(f"\n🔄 Processing URL #{self.url_processing_count}: {json_url}")
        
        # Check if we're in a loop
        if self.url_processing_count > 1600:
            print("⚠️  Processed over 1600 URLs, checking for issues...")
            
            # Count occurrences of each URL
            url_counts = {}
            for url in self.last_processed_urls:
                url_counts[url] = url_counts.get(url, 0) + 1
            
            # Check for repeats
            repeats = [(url, count) for url, count in url_counts.items() if count > 1]
            if repeats:
                print("🔴 Found repeated URLs in last 10:")
                for url, count in repeats:
                    print(f"  - {url} (×{count})")
            
            if self.url_processing_count > 1700:
                print("🛑 Stopping at 1700 to prevent infinite loop")
                return
        
        # Call parent implementation
        await super()._discover_and_scrape_from_json(json_url, progress_file)

async def test_with_debug_scraper():
    """Test using debug scraper"""
    
    print("🐛 Testing Accelerate scraper with debugging...")
    
    scraper = DebugScraper("accelerate", "Accelerate")
    
    async with scraper:
        try:
            # Start from the problematic URL
            start_url = "https://developer.apple.com/tutorials/data/documentation/accelerate/sharing-texture-data-between-the-model-io-framework-and-the-vimage-library.json"
            
            print(f"Starting from: {start_url}")
            
            # Create a dummy progress file
            progress_file = Path("test_progress.txt")
            progress_file.write_text("Testing...")
            
            # Process just this URL and see what happens
            await scraper._discover_and_scrape_from_json(start_url, progress_file)
            
            print(f"\n📊 Stats after processing:")
            print(f"  - URLs processed: {scraper.url_processing_count}")
            print(f"  - Pages scraped: {scraper.stats['pages_scraped']}")
            print(f"  - Processed URLs set size: {len(scraper.processed_urls)}")
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()
        finally:
            # Clean up
            if progress_file.exists():
                progress_file.unlink()

if __name__ == "__main__":
    asyncio.run(test_with_debug_scraper())