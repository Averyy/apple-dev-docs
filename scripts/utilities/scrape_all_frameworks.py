#!/usr/bin/env python3
"""
PRODUCTION: Scrape ALL Apple Frameworks
Comprehensive scraper for all 342+ Apple frameworks using JSON API
"""

import asyncio
import sys
import os
import json
from pathlib import Path

# Add parent directories to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from scraper.json_scraper import AppleJSONDocumentationScraper
from framework_list_scraper import AppleFrameworkListScraper

async def scrape_frameworks(framework_list=None, resume_from=None, max_concurrent=3):
    """Scrape specified frameworks or all frameworks"""
    
    # Get list of frameworks to scrape
    if framework_list:
        # Use provided list
        frameworks = framework_list
    else:
        # Fetch all frameworks
        print("📋 Fetching complete framework list from Apple...")
        async with AppleFrameworkListScraper() as framework_scraper:
            frameworks = await framework_scraper.fetch_all_frameworks()
    
    # Filter if resuming
    if resume_from:
        found = False
        filtered = []
        for fw in frameworks:
            if fw['id'] == resume_from or fw['title'] == resume_from:
                found = True
            if found:
                filtered.append(fw)
        frameworks = filtered
        if not frameworks:
            print(f"❌ Could not find framework '{resume_from}' to resume from")
            return
    
    print(f"\n📊 Will scrape {len(frameworks)} frameworks")
    
    # Track progress
    total = len(frameworks)
    completed = 0
    failed = []
    
    # Process in batches
    batch_size = max_concurrent
    for i in range(0, len(frameworks), batch_size):
        batch = frameworks[i:i+batch_size]
        tasks = []
        
        for fw in batch:
            print(f"\n[{completed+1}/{total}] 🚀 Starting: {fw['title']} ({fw['id']})")
            scraper = AppleJSONDocumentationScraper(
                framework_id=fw['id'],
                framework_name=fw['title']
            )
            tasks.append(scrape_single_framework(scraper, fw, completed+1, total))
            completed += 1
        
        # Run batch concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Check for failures
        for fw, result in zip(batch, results):
            if isinstance(result, Exception):
                failed.append((fw, str(result)))
                print(f"❌ Failed: {fw['title']} - {result}")
    
    # Summary
    print("\n" + "="*70)
    print("📊 SCRAPING COMPLETE")
    print(f"✅ Successful: {total - len(failed)}")
    print(f"❌ Failed: {len(failed)}")
    
    if failed:
        print("\nFailed frameworks:")
        for fw, error in failed:
            print(f"  - {fw['title']} ({fw['id']}): {error}")

async def scrape_single_framework(scraper, framework, current, total):
    """Scrape a single framework"""
    try:
        async with scraper:
            print(f"[{current}/{total}] 📝 Starting scrape for {framework['title']}...")
            
            # Use the streaming scrape_framework method
            stats = await scraper.scrape_framework()
            print(f"[{current}/{total}] ✅ Completed: {framework['title']} - {stats['pages_scraped']} scraped, {stats['pages_skipped']} skipped")
                
    except Exception as e:
        print(f"[{current}/{total}] ❌ Error scraping {framework['title']}: {e}")
        raise

async def scrape_everything():
    """Production script to scrape all Apple frameworks"""
    
    print("🍎 APPLE DOCUMENTATION COMPREHENSIVE SCRAPER - PRODUCTION")
    print("=" * 70)
    print("This will scrape ALL 342+ Apple frameworks from technologies.json")
    print("Estimated time: 3-6 hours (using JSON API)")
    print("Uses incremental scraping - won't re-scrape unchanged content")
    print()
    
    # Parse command line arguments
    resume_from = None
    max_concurrent = 3  # Conservative to be nice to Apple's servers
    specific_frameworks = []
    
    if '--resume' in sys.argv:
        idx = sys.argv.index('--resume')
        if idx + 1 < len(sys.argv):
            resume_from = sys.argv[idx + 1]
            print(f"📍 Resuming from framework: {resume_from}")
    
    if '--concurrent' in sys.argv:
        idx = sys.argv.index('--concurrent')
        if idx + 1 < len(sys.argv):
            max_concurrent = int(sys.argv[idx + 1])
            print(f"🔧 Using {max_concurrent} concurrent scrapers")
    
    if '--frameworks' in sys.argv:
        idx = sys.argv.index('--frameworks')
        # Collect all arguments until next flag or end
        idx += 1
        while idx < len(sys.argv) and not sys.argv[idx].startswith('--'):
            specific_frameworks.append(sys.argv[idx])
            idx += 1
        print(f"📌 Scraping specific frameworks: {', '.join(specific_frameworks)}")
    
    if '--dry-run' in sys.argv:
        print("🧪 DRY RUN MODE - Will show what would be scraped")
        
        # Just show the framework list
        async with AppleFrameworkListScraper() as framework_scraper:
            frameworks = await framework_scraper.fetch_all_frameworks()
        
        if specific_frameworks:
            frameworks = [fw for fw in frameworks if fw['id'] in specific_frameworks or fw['title'] in specific_frameworks]
        
        print(f"\n📋 Would scrape {len(frameworks)} frameworks:")
        for i, fw in enumerate(frameworks[:20], 1):
            print(f"{i:3d}. {fw['title']} ({fw['id']})")
        
        if len(frameworks) > 20:
            print(f"    ... and {len(frameworks) - 20} more frameworks")
        
        return
    
    # Handle --all flag
    if '--all' in sys.argv:
        specific_frameworks = []  # Clear to scrape all
    
    # Confirm before starting
    if '--yes' not in sys.argv:
        if specific_frameworks:
            response = input(f"\n🚀 Ready to scrape {len(specific_frameworks)} frameworks? Continue? (y/N): ")
        else:
            response = input("\n🚀 Ready to scrape all Apple frameworks? This will take several hours. Continue? (y/N): ")
        
        if response.lower() not in ['y', 'yes']:
            print("❌ Aborted by user")
            return
    
    print("\n🚀 Starting Apple framework scraping...")
    
    try:
        # If specific frameworks requested, fetch their info
        framework_list = None
        if specific_frameworks:
            async with AppleFrameworkListScraper() as framework_scraper:
                all_frameworks = await framework_scraper.fetch_all_frameworks()
                framework_list = [
                    fw for fw in all_frameworks 
                    if fw['id'] in specific_frameworks or fw['title'] in specific_frameworks
                ]
        
        await scrape_frameworks(
            framework_list=framework_list,
            resume_from=resume_from,
            max_concurrent=max_concurrent
        )
        
        print("\n🎉 SCRAPING COMPLETED SUCCESSFULLY!")
        
    except KeyboardInterrupt:
        print("\n⏹️  Scraping interrupted by user")
        print(f"💡 To resume, run: python3 {sys.argv[0]} --resume [last_framework]")
        
    except Exception as e:
        print(f"\n❌ Scraping failed: {e}")
        print(f"💡 To resume, run: python3 {sys.argv[0]} --resume [last_framework]")

if __name__ == "__main__":
    # Usage examples:
    print("Usage examples:")
    print(f"  python3 {sys.argv[0]} --dry-run                    # Show what would be scraped")
    print(f"  python3 {sys.argv[0]} --all --yes                  # Scrape all frameworks")
    print(f"  python3 {sys.argv[0]} --frameworks SwiftUI UIKit   # Scrape specific frameworks")
    print(f"  python3 {sys.argv[0]} --resume SwiftUI             # Resume from SwiftUI")
    print(f"  python3 {sys.argv[0]} --concurrent 5               # Use 5 concurrent scrapers")
    print()
    
    asyncio.run(scrape_everything())