#!/usr/bin/env python3
"""
Resume scraping for incomplete frameworks
"""

import asyncio
import sys
import json
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / "scripts" / "utilities"))

from scrape_all_frameworks import scrape_frameworks
from framework_list_scraper import AppleFrameworkListScraper

async def main():
    """Resume scraping incomplete frameworks."""
    print("🍎 RESUMING APPLE DOCUMENTATION SCRAPER")
    print("=" * 60)
    
    # Check what's already been scraped
    doc_dir = Path("documentation")
    scraped_frameworks = set()
    if doc_dir.exists():
        for item in doc_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                md_count = len(list(item.rglob("*.md")))
                if md_count > 0:
                    scraped_frameworks.add(item.name.lower())
    
    print(f"📁 Found {len(scraped_frameworks)} frameworks already scraped")
    
    # Get complete framework list
    async with AppleFrameworkListScraper() as framework_scraper:
        all_frameworks = await framework_scraper.fetch_all_frameworks()
    
    # Find frameworks to scrape (those not already done)
    frameworks_to_scrape = []
    for fw in all_frameworks:
        if fw['id'].lower() not in scraped_frameworks:
            frameworks_to_scrape.append(fw)
    
    print(f"📋 Found {len(frameworks_to_scrape)} frameworks to scrape:")
    for fw in frameworks_to_scrape[:10]:  # Show first 10
        print(f"   - {fw['title']} (id: {fw['id']})")
    if len(frameworks_to_scrape) > 10:
        print(f"   ... and {len(frameworks_to_scrape) - 10} more")
    print()
    
    if not frameworks_to_scrape:
        print("✅ All frameworks are already scraped!")
        return
    
    # Confirm before starting
    response = input(f"\n🚀 Ready to scrape {len(frameworks_to_scrape)} remaining frameworks? Continue? (y/N): ")
    if response.lower() not in ['y', 'yes']:
        print("❌ Aborted by user")
        return
    
    try:
        print("\n🚀 Starting to scrape remaining frameworks...")
        print("💡 Press Ctrl+C to stop gracefully")
        print()
        
        await scrape_frameworks(
            framework_list=frameworks_to_scrape,
            max_concurrent=3
        )
        
        print("\n🎉 ALL REMAINING FRAMEWORKS SCRAPED SUCCESSFULLY!")
        
    except KeyboardInterrupt:
        print("\n⏹️  Scraping interrupted by user")
        print("💡 Run this script again to resume")
    except Exception as e:
        print(f"\n❌ Error during scraping: {e}")
        import traceback
        traceback.print_exc()
        print("\n💡 Run this script again to resume")

if __name__ == "__main__":
    asyncio.run(main())