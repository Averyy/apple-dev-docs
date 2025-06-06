#!/usr/bin/env python3
"""
Run comprehensive scraper with better error handling and resume capability
"""

import asyncio
import sys
import traceback
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent / "scripts" / "utilities"))

from comprehensive_scraper import ComprehensiveAppleScraper

async def main():
    """Run the comprehensive scraper with resume capability."""
    print("🍎 COMPREHENSIVE APPLE DOCUMENTATION SCRAPER")
    print("=" * 60)
    
    # Check what's already been scraped
    doc_dir = Path("documentation")
    existing = []
    if doc_dir.exists():
        for item in doc_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                md_count = len(list(item.rglob("*.md")))
                if md_count > 0:
                    existing.append(f"{item.name}: {md_count} files")
    
    if existing:
        print(f"📁 Found {len(existing)} existing frameworks:")
        for fw in existing:
            print(f"   - {fw}")
        print()
    
    # Create scraper with resume capability
    scraper = ComprehensiveAppleScraper(
        max_concurrent=5,
        resume_from="UIKit"  # Resume from UIKit
    )
    
    try:
        print("🚀 Starting comprehensive scraping...")
        print("💡 This will skip already completed frameworks")
        print("💡 Press Ctrl+C to stop gracefully")
        print()
        
        await scraper.scrape_all_frameworks()
        
        print("\n🎉 ALL FRAMEWORKS SCRAPED SUCCESSFULLY!")
        
    except KeyboardInterrupt:
        print("\n⏹️  Scraping interrupted by user")
        print("💡 Run this script again to resume")
    except Exception as e:
        print(f"\n❌ Error during scraping: {e}")
        traceback.print_exc()
        print("\n💡 Run this script again to resume")

if __name__ == "__main__":
    asyncio.run(main())