#!/usr/bin/env python3
"""
Scrape remaining frameworks that were missed
"""

import asyncio
import json
import sys
from pathlib import Path
import os

# Add scraper to path
sys.path.insert(0, str(Path(__file__).parent))

from scraper.apple_scraper import AppleDocumentationScraper

# Frameworks that need to be scraped (based on analysis)
REMAINING_FRAMEWORKS = [
    ("vmnet", "vmnet"),
    ("watchconnectivity", "Watch Connectivity"),
    ("xcselect", "xcselect"),
    ("xpc", "XPC"),
    ("usbdriverkit", "USBDriverKit"),
    ("usbserialdriverkit", "USBSerialDriverKit"),
    ("usernotificationsui", "User Notifications UI"),
    ("visionkit", "VisionKit"),
    ("watchkit", "WatchKit"),
    ("weatherkit", "WeatherKit"),
    ("weatherkit_rest_api", "WeatherKit REST API"),
    ("widgetkit", "WidgetKit"),
    ("walletorders", "Wallet Orders"),
    ("walletpasses", "Wallet Passes"),
    ("videotoolbox", "Video Toolbox"),
    ("videosubscriberaccount", "Video Subscriber Account"),
    ("virtualization", "Virtualization"),
    ("webkit", "WebKit"),
    ("webkit_js", "WebKit JS"),
    ("workoutkit", "WorkoutKit"),
    ("xcode", "Xcode"),
    ("xcode_release_notes", "Xcode Release Notes"),
    ("xcodekit", "XcodeKit"),
    ("xctest", "XCTest"),
    ("xcuiautomation", "XCUIAutomation")
]

async def scrape_framework(framework_id: str, framework_name: str):
    """Scrape a single framework"""
    print(f"\n{'='*60}")
    print(f"📦 Scraping {framework_name} (id: {framework_id})")
    print(f"{'='*60}\n")
    
    # Check if already scraped
    doc_dir = Path(f"documentation/{framework_id}")
    if doc_dir.exists():
        md_count = len(list(doc_dir.rglob("*.md")))
        if md_count > 10:
            print(f"⏭️  Skipping {framework_name} - already has {md_count} files")
            return
    
    try:
        scraper = AppleDocumentationScraper(framework_id)
        await scraper.discover_and_scrape_streaming()
        
        stats = scraper.stats
        print(f"\n✅ {framework_name} completed:")
        print(f"   - Pages scraped: {stats.get('pages_scraped', 0)}")
        print(f"   - Pages skipped: {stats.get('pages_skipped', 0)}")
        print(f"   - Pages failed: {stats.get('pages_failed', 0)}")
        
    except Exception as e:
        print(f"\n❌ {framework_name} failed: {e}")
        import traceback
        traceback.print_exc()

async def main():
    """Scrape all remaining frameworks"""
    print("🍎 SCRAPING REMAINING APPLE FRAMEWORKS")
    print("=" * 60)
    
    # Check what's already been scraped
    doc_dir = Path("documentation")
    scraped_count = 0
    if doc_dir.exists():
        for item in doc_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                md_count = len(list(item.rglob("*.md")))
                if md_count > 0:
                    scraped_count += 1
    
    print(f"📁 Already scraped: {scraped_count} frameworks")
    print(f"📋 Remaining to scrape: {len(REMAINING_FRAMEWORKS)} frameworks")
    
    # Scrape frameworks one at a time to avoid issues
    for framework_id, framework_name in REMAINING_FRAMEWORKS:
        try:
            await scrape_framework(framework_id, framework_name)
        except KeyboardInterrupt:
            print("\n⏹️  Scraping interrupted by user")
            break
        except Exception as e:
            print(f"\n❌ Error scraping {framework_name}: {e}")
            continue
    
    print("\n🎉 SCRAPING COMPLETE!")
    
    # Count final results
    final_count = 0
    if doc_dir.exists():
        for item in doc_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                md_count = len(list(item.rglob("*.md")))
                if md_count > 0:
                    final_count += 1
    
    print(f"📊 Total frameworks scraped: {final_count}")

if __name__ == "__main__":
    asyncio.run(main())