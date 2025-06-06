#!/usr/bin/env python3
"""
Scrape ALL remaining frameworks without the broken resume logic
"""

import asyncio
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper

async def scrape_remaining_frameworks():
    """Scrape all remaining frameworks"""
    print("🍎 SCRAPING ALL REMAINING APPLE FRAMEWORKS")
    print("=" * 60)
    
    # Get already scraped frameworks
    scraped = set()
    for item in os.listdir('documentation'):
        if os.path.isdir(f'documentation/{item}') and not item.startswith('.'):
            # Add both the exact name and lowercase version
            scraped.add(item)
            scraped.add(item.lower())
    
    # Load framework list
    with open('data/fixed_frameworks_list.json', 'r') as f:
        data = json.load(f)
        frameworks = data['frameworks']
    
    # Find missing frameworks
    missing = []
    for fw in frameworks:
        fw_id = fw['id']
        # Check if this framework is already scraped
        if fw_id not in scraped and fw_id.lower() not in scraped:
            missing.append(fw)
    
    print(f"📁 Already scraped: {len(scraped)} frameworks")
    print(f"📋 Remaining to scrape: {len(missing)} frameworks")
    
    if not missing:
        print("✅ All frameworks already scraped!")
        return
    
    print("\nFrameworks to scrape:")
    for fw in missing:
        print(f"- {fw['title']} (id: {fw['id']})")
    print()
    
    # Scrape each missing framework
    for i, fw in enumerate(missing, 1):
        framework_id = fw['id']
        framework_name = fw['title']
        
        print(f"\n{'='*60}")
        print(f"📦 [{i}/{len(missing)}] Scraping {framework_name} (id: {framework_id})")
        print(f"{'='*60}\n")
        
        try:
            async with AppleJSONDocumentationScraper(framework_id) as scraper:
                # Call the streaming discovery and scrape method
                await scraper.discover_and_scrape_streaming()
                
                stats = scraper.stats
                print(f"\n✅ {framework_name} completed successfully")
                print(f"   - Pages scraped: {stats.get('pages_scraped', 0)}")
                print(f"   - Pages skipped: {stats.get('pages_skipped', 0)}")
                print(f"   - Pages failed: {stats.get('pages_failed', 0)}")
            
        except Exception as e:
            print(f"\n❌ {framework_name} failed: {e}")
            import traceback
            traceback.print_exc()
            continue
    
    print("\n" + "="*60)
    print("🎉 ALL FRAMEWORKS SCRAPING COMPLETE!")
    
    # Final count
    final_scraped = set()
    for item in os.listdir('documentation'):
        if os.path.isdir(f'documentation/{item}') and not item.startswith('.'):
            final_scraped.add(item.lower())
    
    print(f"\n📊 Final statistics:")
    print(f"- Total frameworks scraped: {len(final_scraped)}")
    print(f"- Newly scraped: {len(final_scraped) - len(scraped)}")

if __name__ == "__main__":
    asyncio.run(scrape_remaining_frameworks())