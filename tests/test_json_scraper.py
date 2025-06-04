#!/usr/bin/env python3
"""Test the JSON-based scraper."""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.config import Config
from scraper.utils.logger import setup_logging

Config.ensure_directories()
setup_logging(log_level="INFO")


async def test_json_scraper():
    """Test scraping with JSON endpoints."""
    print("=" * 80)
    print("TESTING JSON-BASED SCRAPER")
    print("=" * 80)
    
    # Test with SwiftUI Text
    test_urls = [
        "https://developer.apple.com/documentation/swiftui/text",
        "https://developer.apple.com/documentation/swiftui/button",
        "https://developer.apple.com/documentation/swiftui/view/frame(width:height:alignment:)"
    ]
    
    async with AppleJSONDocumentationScraper("swiftui", "SwiftUI") as scraper:
        for url in test_urls:
            print(f"\n{'='*60}")
            print(f"Testing: {url}")
            print('='*60)
            
            try:
                # Extract data (we pass None for soup since we don't use it)
                data = await scraper.extract_page_data(None, url)
                
                if data:
                    print(f"\nExtracted data:")
                    print(f"  Title: {data.get('title')}")
                    print(f"  Brief: {data.get('brief_description', '')[:100]}...")
                    print(f"  Platforms: {len(data.get('availability', []))} platforms")
                    print(f"  Declaration: {'swift' in data.get('declaration', {})}")
                    print(f"  Overview: {len(data.get('overview', ''))} chars")
                    print(f"  Parameters: {len(data.get('parameters', []))} params")
                    print(f"  Code examples: {len(data.get('code_examples', []))} examples")
                    print(f"  Topics: {len(data.get('topics', []))} topic groups")
                    
                    # Save the data
                    await scraper.save_page_data(url, data)
                    output_file = scraper.output_dir / scraper.get_relative_path(url)
                    print(f"\nSaved to: {output_file}")
                    
                else:
                    print("No data extracted")
                    
            except Exception as e:
                print(f"Error: {e}")
                import traceback
                traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_json_scraper())