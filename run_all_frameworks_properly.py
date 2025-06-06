#!/usr/bin/env python3
"""
Run all frameworks properly - don't get stuck on large frameworks
"""

import asyncio
import json
import sys
import time
from pathlib import Path
from typing import List, Dict, Set

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper

class FrameworkManager:
    """Manages multiple framework scrapers running concurrently"""
    
    def __init__(self, max_concurrent: int = 3):
        self.max_concurrent = max_concurrent
        self.active_scrapers: Dict[str, asyncio.Task] = {}
        self.completed_frameworks: Set[str] = set()
        self.failed_frameworks: Set[str] = set()
        self.framework_stats: Dict[str, Dict] = {}
        
    async def scrape_framework_with_timeout(self, framework: Dict[str, str], timeout: int = 1800):
        """Scrape a single framework with timeout (default 30 minutes)"""
        framework_id = framework['id']
        framework_name = framework['title']
        
        print(f"\n🚀 Starting {framework_name} ({framework_id})...")
        
        scraper = AppleJSONDocumentationScraper(framework_id, framework_name)
        
        start_time = time.time()
        
        try:
            async with scraper:
                # Run with timeout
                await asyncio.wait_for(
                    scraper.discover_and_scrape_streaming(),
                    timeout=timeout
                )
                
            duration = time.time() - start_time
            stats = scraper.stats
            
            print(f"✅ {framework_name} completed: {stats['pages_scraped']} pages in {duration/60:.1f} minutes")
            
            self.framework_stats[framework_id] = {
                'status': 'completed',
                'pages_scraped': stats['pages_scraped'],
                'pages_skipped': stats['pages_skipped'],
                'pages_failed': stats['pages_failed'],
                'duration': duration
            }
            
            self.completed_frameworks.add(framework_id)
            
        except asyncio.TimeoutError:
            duration = time.time() - start_time
            stats = scraper.stats if hasattr(scraper, 'stats') else {'pages_scraped': 0}
            
            print(f"⏱️  {framework_name} timed out after {timeout/60:.0f} minutes ({stats.get('pages_scraped', 0)} pages scraped)")
            
            self.framework_stats[framework_id] = {
                'status': 'timeout',
                'pages_scraped': stats.get('pages_scraped', 0),
                'duration': duration
            }
            
        except Exception as e:
            print(f"❌ {framework_name} failed: {e}")
            self.failed_frameworks.add(framework_id)
            
            self.framework_stats[framework_id] = {
                'status': 'failed',
                'error': str(e),
                'duration': time.time() - start_time
            }
    
    async def scrape_all_frameworks(self, frameworks: List[Dict[str, str]]):
        """Scrape all frameworks with proper concurrency management"""
        
        print(f"📦 Starting scraping of {len(frameworks)} frameworks")
        print(f"Max concurrent scrapers: {self.max_concurrent}")
        print()
        
        # Skip already completed frameworks
        existing_dirs = [d.name for d in Path("documentation").iterdir() if d.is_dir()]
        frameworks_to_scrape = []
        
        for fw in frameworks:
            # Check multiple variations of the framework name
            fw_variations = [
                fw['id'],
                fw['id'].lower(),
                fw['id'].capitalize(),
                fw['title'].replace(' ', ''),
                fw['title'].replace(' ', '').lower()
            ]
            
            if any(var in existing_dirs for var in fw_variations):
                print(f"⏭️  Skipping {fw['title']}: Already exists")
                self.completed_frameworks.add(fw['id'])
            else:
                frameworks_to_scrape.append(fw)
        
        print(f"\n📋 {len(frameworks_to_scrape)} frameworks to scrape")
        
        # Process frameworks
        framework_index = 0
        
        while framework_index < len(frameworks_to_scrape) or self.active_scrapers:
            # Start new scrapers if we have capacity
            while len(self.active_scrapers) < self.max_concurrent and framework_index < len(frameworks_to_scrape):
                framework = frameworks_to_scrape[framework_index]
                framework_id = framework['id']
                
                # Create task with appropriate timeout
                # Large frameworks get more time
                timeout = 3600 if framework_id.lower() in ['accelerate', 'foundation', 'uikit', 'swiftui'] else 1800
                
                task = asyncio.create_task(
                    self.scrape_framework_with_timeout(framework, timeout)
                )
                
                self.active_scrapers[framework_id] = task
                framework_index += 1
            
            # Wait for at least one to complete
            if self.active_scrapers:
                done, pending = await asyncio.wait(
                    self.active_scrapers.values(),
                    return_when=asyncio.FIRST_COMPLETED
                )
                
                # Remove completed tasks
                for task in done:
                    # Find which framework this was
                    for fw_id, t in list(self.active_scrapers.items()):
                        if t == task:
                            del self.active_scrapers[fw_id]
                            break
                
                # Print progress
                total_processed = len(self.completed_frameworks) + len(self.failed_frameworks) + len([s for s in self.framework_stats.values() if s.get('status') == 'timeout'])
                print(f"\n📊 Progress: {total_processed}/{len(frameworks)} frameworks")
                print(f"   Active: {len(self.active_scrapers)}, Completed: {len(self.completed_frameworks)}, Failed: {len(self.failed_frameworks)}")
        
        # Final summary
        self.print_summary(frameworks)
    
    def print_summary(self, all_frameworks: List[Dict[str, str]]):
        """Print final summary"""
        print("\n" + "=" * 60)
        print("📊 FINAL SUMMARY")
        print("=" * 60)
        
        total_pages = sum(s.get('pages_scraped', 0) for s in self.framework_stats.values())
        
        print(f"\nFrameworks processed: {len(self.framework_stats)}/{len(all_frameworks)}")
        print(f"Total pages scraped: {total_pages}")
        
        # Breakdown by status
        completed = [fw for fw, stats in self.framework_stats.items() if stats.get('status') == 'completed']
        timeout = [fw for fw, stats in self.framework_stats.items() if stats.get('status') == 'timeout']
        failed = [fw for fw, stats in self.framework_stats.items() if stats.get('status') == 'failed']
        
        print(f"\n✅ Completed: {len(completed)}")
        print(f"⏱️  Timed out: {len(timeout)}")
        print(f"❌ Failed: {len(failed)}")
        
        # Show timeout frameworks
        if timeout:
            print("\n⏱️  Frameworks that timed out (may need re-run):")
            for fw_id in timeout:
                stats = self.framework_stats[fw_id]
                print(f"   - {fw_id}: {stats.get('pages_scraped', 0)} pages scraped")
        
        # Save results
        results_file = Path("scraping_results.json")
        with open(results_file, 'w') as f:
            json.dump({
                'summary': {
                    'total_frameworks': len(all_frameworks),
                    'processed': len(self.framework_stats),
                    'completed': len(completed),
                    'timeout': len(timeout),
                    'failed': len(failed),
                    'total_pages': total_pages
                },
                'frameworks': self.framework_stats
            }, f, indent=2)
        
        print(f"\n📄 Results saved to {results_file}")

async def main():
    """Main entry point"""
    print("🍎 APPLE DOCUMENTATION SCRAPER - ALL FRAMEWORKS")
    print("=" * 60)
    
    # Load framework list
    framework_file = Path("data/fixed_frameworks_list.json")
    if not framework_file.exists():
        print("❌ Framework list not found. Run framework_list_scraper.py first.")
        return
    
    with open(framework_file) as f:
        data = json.load(f)
        frameworks = data['frameworks']
    
    print(f"📋 Loaded {len(frameworks)} frameworks")
    
    # Create manager and run
    manager = FrameworkManager(max_concurrent=3)
    
    try:
        await manager.scrape_all_frameworks(frameworks)
    except KeyboardInterrupt:
        print("\n⏹️  Stopped by user")
        manager.print_summary(frameworks)

if __name__ == "__main__":
    asyncio.run(main())