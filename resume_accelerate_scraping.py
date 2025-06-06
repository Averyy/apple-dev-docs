#!/usr/bin/env python3
"""
Resume Accelerate scraping with better progress tracking
"""

import asyncio
import sys
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).parent / "scripts" / "utilities"))

from comprehensive_scraper import ComprehensiveAppleScraper

async def resume_accelerate():
    """Resume scraping Accelerate framework"""
    
    print("🚀 Resuming Accelerate framework scraping...")
    print("=" * 60)
    
    # Count existing files
    doc_dir = Path("documentation/Accelerate")
    if doc_dir.exists():
        existing_files = list(doc_dir.rglob("*.md"))
        print(f"📊 Found {len(existing_files)} existing files")
    else:
        existing_files = []
    
    # Create scraper for single framework
    from scraper.json_scraper import AppleJSONDocumentationScraper
    scraper = AppleJSONDocumentationScraper("accelerate", "Accelerate")
    
    start_time = time.time()
    last_update_time = start_time
    last_file_count = len(existing_files)
    
    async def monitor_progress():
        """Monitor progress in the background"""
        nonlocal last_update_time, last_file_count
        
        while True:
            await asyncio.sleep(30)  # Update every 30 seconds
            
            current_files = list(doc_dir.rglob("*.md"))
            current_count = len(current_files)
            
            # Calculate rate
            time_elapsed = time.time() - last_update_time
            files_scraped = current_count - last_file_count
            rate = files_scraped / (time_elapsed / 60) if time_elapsed > 0 else 0
            
            print(f"\n📈 Progress Update:")
            print(f"  - Total files: {current_count}")
            print(f"  - New files: {files_scraped}")
            print(f"  - Rate: {rate:.1f} files/minute")
            print(f"  - Total elapsed: {(time.time() - start_time) / 60:.1f} minutes")
            
            last_update_time = time.time()
            last_file_count = current_count
    
    # Start monitoring task
    monitor_task = asyncio.create_task(monitor_progress())
    
    try:
        # Run the scraper
        async with scraper:
            await scraper.discover_and_scrape_streaming()
        
        print("\n✅ Scraping completed successfully!")
        
    except KeyboardInterrupt:
        print("\n⏹️  Stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # Cancel monitoring
        monitor_task.cancel()
        try:
            await monitor_task
        except asyncio.CancelledError:
            pass
    
    # Final stats
    final_files = list(doc_dir.rglob("*.md"))
    print(f"\n📊 Final Statistics:")
    print(f"  - Total files: {len(final_files)}")
    print(f"  - Files added: {len(final_files) - len(existing_files)}")
    print(f"  - Total time: {(time.time() - start_time) / 60:.1f} minutes")

if __name__ == "__main__":
    print("🍎 ACCELERATE FRAMEWORK SCRAPER")
    print("This will continue scraping the Accelerate framework")
    print("Press Ctrl+C to stop at any time")
    print()
    
    asyncio.run(resume_accelerate())