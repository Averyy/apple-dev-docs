#!/usr/bin/env python3
"""Test scraping specific SwiftUI pages and review markdown output."""

import asyncio
import sys
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

from scraper.apple_scraper import AppleDocumentationScraper
from scraper.config import Config
from scraper.utils.logger import setup_logging

# Setup
Config.ensure_directories()
setup_logging(log_level="INFO")


async def test_scrape_specific_pages():
    """Test scraping specific SwiftUI pages."""
    # Test pages with different content types
    test_urls = [
        "https://developer.apple.com/documentation/swiftui/text",
        "https://developer.apple.com/documentation/swiftui/view/frame(width:height:alignment:)",
        "https://developer.apple.com/documentation/swiftui/button",
    ]
    
    async with AppleDocumentationScraper("swiftui", "SwiftUI") as scraper:
        for url in test_urls:
            print(f"\n{'='*80}")
            print(f"Scraping: {url}")
            print('='*80)
            
            try:
                # Scrape the page
                data = await scraper.scrape_page(url)
                
                if data:
                    # Save the page
                    await scraper.save_page_data(url, data)
                    
                    # Get the output file path
                    output_file = scraper.output_dir / scraper.get_relative_path(url)
                    
                    print(f"\nSaved to: {output_file}")
                    print(f"Data extracted: {list(data.keys())}")
                else:
                    print("No data extracted")
                    
            except Exception as e:
                print(f"Error: {e}")
    
    print("\n\nDone! Check the docs/swiftui/ directory for output.")


if __name__ == "__main__":
    asyncio.run(test_scrape_specific_pages())