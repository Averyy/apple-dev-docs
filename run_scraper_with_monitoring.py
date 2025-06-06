#!/usr/bin/env python3
"""
Run scraper with better monitoring and restart capability
"""

import asyncio
import sys
import time
import traceback
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent / "scripts" / "utilities"))

from comprehensive_scraper import ComprehensiveAppleScraper

async def run_with_monitoring():
    """Run scraper with monitoring and automatic restart on failure."""
    
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            print(f"\n🚀 Starting scraper (attempt {retry_count + 1}/{max_retries})...")
            
            # Create scraper
            scraper = ComprehensiveAppleScraper(
                max_concurrent=2,  # Reduce concurrency to be gentler
                resume_from=None
            )
            
            # Run with a timeout to prevent hanging
            await asyncio.wait_for(
                scraper.scrape_all_frameworks(),
                timeout=3600  # 1 hour timeout per attempt
            )
            
            print("\n✅ Scraping completed successfully!")
            break
            
        except asyncio.TimeoutError:
            print(f"\n⏱️  Scraper timed out after 1 hour")
            retry_count += 1
            
            # Check progress
            doc_dir = Path("documentation")
            if doc_dir.exists():
                total_files = len(list(doc_dir.rglob("*.md")))
                print(f"📊 Progress: {total_files} files scraped so far")
            
            if retry_count < max_retries:
                print(f"🔄 Retrying in 30 seconds...")
                await asyncio.sleep(30)
            
        except KeyboardInterrupt:
            print("\n⏹️  Stopped by user")
            break
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            traceback.print_exc()
            retry_count += 1
            
            if retry_count < max_retries:
                print(f"🔄 Retrying in 30 seconds...")
                await asyncio.sleep(30)
    
    if retry_count >= max_retries:
        print(f"\n❌ Failed after {max_retries} attempts")
        print("💡 Check logs for details")

if __name__ == "__main__":
    print("🍎 APPLE DOCUMENTATION SCRAPER WITH MONITORING")
    print("=" * 60)
    print("This will automatically restart if the scraper gets stuck")
    print("Press Ctrl+C to stop")
    print()
    
    asyncio.run(run_with_monitoring())