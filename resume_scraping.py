#!/usr/bin/env python3
"""
Resume scraping from USBDriverKit onwards
"""

import asyncio
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "scripts" / "utilities"))

from comprehensive_scraper import ComprehensiveAppleScraper

async def main():
    """Run the comprehensive scraper starting from USBDriverKit."""
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
    
    # Load framework list
    with open("data/apple_frameworks_complete_list.json", 'r') as f:
        data = json.load(f)
    
    # Collect all frameworks
    all_frameworks = []
    for category, frameworks in data['by_category'].items():
        all_frameworks.extend(frameworks)
    
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
    
    # Create scraper WITHOUT resume_from since we'll handle it differently
    scraper = ComprehensiveAppleScraper(
        max_concurrent=5,
        resume_from=None  # Don't use built-in resume logic
    )
    
    # Override the framework loading to only include our missing frameworks
    original_load_frameworks = scraper.load_frameworks
    
    async def custom_load_frameworks():
        # Return only the frameworks we want to scrape
        return frameworks_to_scrape
    
    scraper.load_frameworks = custom_load_frameworks
    
    try:
        print("🚀 Starting to scrape remaining frameworks...")
        print("💡 Press Ctrl+C to stop gracefully")
        print()
        
        await scraper.scrape_all_frameworks()
        
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