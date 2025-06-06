#!/usr/bin/env python3
"""Test scraping a single framework to verify the fix"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper

async def test_framework(framework_id: str, framework_name: str = None):
    """Test scraping a single framework"""
    
    if not framework_name:
        framework_name = framework_id.title()
    
    print(f"🧪 Testing {framework_name} ({framework_id}) scraping")
    print()
    
    # Clear any old progress file
    progress_file = Path(f"documentation/{framework_id}/scraping_progress.txt")
    if progress_file.exists():
        progress_file.unlink()
        print("✓ Cleared old progress file")
    
    try:
        async with AppleJSONDocumentationScraper(framework_id, framework_name) as scraper:
            await scraper.discover_and_scrape_streaming()
            
            print(f"\n✅ Completed successfully!")
            print(f"Pages scraped: {scraper.stats.get('pages_scraped', 0)}")
            print(f"Pages skipped: {scraper.stats.get('pages_skipped', 0)}")
            print(f"Pages failed: {scraper.stats.get('pages_failed', 0)}")
            
            # Check the progress file
            if progress_file.exists():
                content = progress_file.read_text()
                if "Completed scraping" in content:
                    print("\n✓ Progress file shows completion")
                else:
                    print("\n⚠️ Progress file doesn't show completion")
                    print(f"Content: {content}")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

async def main():
    if len(sys.argv) < 2:
        print("Usage: python test_single_framework.py <framework_id> [framework_name]")
        print("Example: python test_single_framework.py swiftui SwiftUI")
        sys.exit(1)
    
    framework_id = sys.argv[1]
    framework_name = sys.argv[2] if len(sys.argv) > 2 else None
    
    await test_framework(framework_id, framework_name)

if __name__ == "__main__":
    asyncio.run(main())