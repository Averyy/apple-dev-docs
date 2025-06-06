#!/usr/bin/env python3
"""
PRODUCTION: Scrape ALL Apple Frameworks
Comprehensive scraper for all 342+ Apple frameworks using dynamic framework discovery
"""

import asyncio
import sys
from comprehensive_scraper_fixed import ComprehensiveAppleScraperFixed as ComprehensiveAppleScraper

async def scrape_everything():
    """Production script to scrape all Apple frameworks"""
    
    print("🍎 APPLE DOCUMENTATION COMPREHENSIVE SCRAPER - PRODUCTION")
    print("=" * 70)
    print("This will scrape ALL 342+ Apple frameworks from technologies.json")
    print("Estimated time: 6-12 hours (depends on content and rate limits)")
    print("Uses incremental scraping - won't re-scrape unchanged content")
    print()
    
    # Parse command line arguments
    resume_from = None
    max_concurrent = 3  # Conservative to be nice to Apple's servers
    
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
    
    if '--dry-run' in sys.argv:
        print("🧪 DRY RUN MODE - Will show what would be scraped")
        
        # Just show the framework list
        from framework_list_scraper import AppleFrameworkListScraper
        async with AppleFrameworkListScraper() as framework_scraper:
            frameworks = await framework_scraper.fetch_all_frameworks()
        
        print(f"\\n📋 Would scrape {len(frameworks)} frameworks:")
        for i, fw in enumerate(frameworks[:20], 1):
            print(f"{i:3d}. {fw['title']} ({fw['id']})")
        
        if len(frameworks) > 20:
            print(f"    ... and {len(frameworks) - 20} more frameworks")
        
        print(f"\\n💡 To start scraping: python3 {sys.argv[0]}")
        print(f"💡 To resume from framework: python3 {sys.argv[0]} --resume SwiftUI")
        return
    
    # Confirm before starting
    if '--yes' not in sys.argv:
        response = input("\\n🚀 Ready to scrape all Apple frameworks? This will take several hours. Continue? (y/N): ")
        if response.lower() not in ['y', 'yes']:
            print("❌ Aborted by user")
            return
    
    print("\\n🚀 Starting comprehensive Apple framework scraping...")
    
    # Create and run the comprehensive scraper
    scraper = ComprehensiveAppleScraper(
        max_concurrent=max_concurrent,
        resume_from=resume_from
    )
    
    try:
        await scraper.scrape_all_frameworks()
        print("\\n🎉 ALL APPLE FRAMEWORKS SCRAPED SUCCESSFULLY!")
        
    except KeyboardInterrupt:
        print("\\n⏹️  Scraping interrupted by user")
        print(f"💡 To resume, run: python3 {sys.argv[0]} --resume [last_framework]")
        
    except Exception as e:
        print(f"\\n❌ Scraping failed: {e}")
        print(f"💡 To resume, run: python3 {sys.argv[0]} --resume [last_framework]")

if __name__ == "__main__":
    # Usage examples:
    print("Usage examples:")
    print(f"  python3 {sys.argv[0]} --dry-run                    # Show what would be scraped")
    print(f"  python3 {sys.argv[0]} --yes                        # Start scraping without confirmation")
    print(f"  python3 {sys.argv[0]} --resume SwiftUI             # Resume from SwiftUI")
    print(f"  python3 {sys.argv[0]} --concurrent 5               # Use 5 concurrent scrapers")
    print(f"  python3 {sys.argv[0]} --resume SwiftUI --yes       # Resume without confirmation")
    print()
    
    asyncio.run(scrape_everything())