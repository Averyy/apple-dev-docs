#!/usr/bin/env python3
"""Test extracting a single page using the JSON scraper."""

import asyncio
import json
from scraper.json_scraper import AppleJSONDocumentationScraper

async def test_single_page():
    # Initialize scraper for SwiftUI
    scraper = AppleJSONDocumentationScraper("swiftui", "SwiftUI")
    
    # The page URL you want to scrape
    doc_url = "https://developer.apple.com/documentation/swiftui/declaring-a-custom-view"
    
    # Extract page data (passing None for soup since we don't use it)
    print(f"Extracting data from: {doc_url}")
    data = await scraper.extract_page_data(None, doc_url)
    
    if data:
        print("\n=== EXTRACTED DATA ===")
        print(json.dumps(data, indent=2))
        
        # Save as markdown
        await scraper.save_page_data(doc_url, data)
        print(f"\n=== MARKDOWN SAVED ===")
        
        # Read and display the markdown
        from pathlib import Path
        md_path = Path("docs/swiftui/declaring-a-custom-view.md")
        if md_path.exists():
            print(f"\n=== MARKDOWN CONTENT ===")
            print(md_path.read_text())
    else:
        print("Failed to extract data")

if __name__ == "__main__":
    asyncio.run(test_single_page())