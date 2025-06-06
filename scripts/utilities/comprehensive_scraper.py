#!/usr/bin/env python3
"""
COMPREHENSIVE Apple Documentation Scraper
Uses framework_list_scraper.py to get all frameworks, then scrapes each one with full content
Handles incremental updates and avoids double scraping
"""

import asyncio
import json
import time
from pathlib import Path
from typing import List, Dict, Set, Optional
from dataclasses import dataclass

from scraper.json_scraper import AppleJSONDocumentationScraper

@dataclass
class ScrapingStats:
    total_frameworks: int = 0
    completed_frameworks: int = 0
    skipped_frameworks: int = 0
    failed_frameworks: int = 0
    total_pages_scraped: int = 0
    total_pages_skipped: int = 0
    total_pages_failed: int = 0
    start_time: Optional[float] = None
    end_time: Optional[float] = None

class ComprehensiveAppleScraper:
    """Comprehensive scraper that gets framework list dynamically and scrapes all content"""
    
    def __init__(self, max_concurrent: int = 3, resume_from: Optional[str] = None):
        """
        Initialize comprehensive scraper
        
        Args:
            max_concurrent: Maximum concurrent framework scrapers (default: 3 to be nice to Apple)
            resume_from: Framework ID to resume from (useful if scraping was interrupted)
        """
        self.max_concurrent = max_concurrent
        self.resume_from = resume_from
        self.stats = ScrapingStats()
        self.progress_file = Path("scraping_master_progress.txt")
        self.completed_frameworks: Set[str] = set()
        
    async def get_all_frameworks(self) -> List[Dict[str, str]]:
        """Get the complete framework list from the fixed JSON file"""
        print("🍎 Loading framework list...")
        
        # Use the fixed framework list
        framework_file = Path("data/fixed_frameworks_list.json")
        if not framework_file.exists():
            print("❌ Fixed framework list not found. Run fix_framework_list.py first!")
            raise Exception("Missing fixed_frameworks_list.json")
            
        with open(framework_file, 'r') as f:
            data = json.load(f)
            frameworks = data.get('frameworks', [])
            
        if not frameworks:
            raise Exception("No frameworks found in fixed list")
            
        print(f"✅ Loaded {len(frameworks)} frameworks from fixed list")
        return frameworks
    
    def should_skip_framework(self, framework: Dict[str, str]) -> tuple:
        """Check if we should skip this framework based on existing content and resume point"""
        framework_id = framework['id']
        
        # Check resume point
        if self.resume_from:
            if framework_id != self.resume_from and framework_id not in self.completed_frameworks:
                return True, f"Before resume point ({self.resume_from})"
        
        # Check if framework folder exists and has substantial content
        framework_dir = Path(f"documentation/{framework_id}")
        if framework_dir.exists():
            md_files = list(framework_dir.rglob("*.md"))
            if len(md_files) > 10:  # Has substantial content already
                # Check if scraping_progress.txt shows completion
                progress_file = framework_dir / "scraping_progress.txt"
                if progress_file.exists():
                    content = progress_file.read_text()
                    if "Completed scraping" in content and "failed: 0" in content:
                        return True, f"Already completed ({len(md_files)} files)"
        
        return False, ""
    
    async def scrape_single_framework(self, framework: Dict[str, str]) -> Dict:
        """Scrape a single framework completely"""
        framework_id = framework['id']
        framework_name = framework['title']
        
        start_time = time.time()
        
        try:
            print(f"\n🚀 Starting {framework_name} ({framework_id})...")
            
            async with AppleJSONDocumentationScraper(framework_id, framework_name) as scraper:
                # Use streaming discovery and scrape
                await scraper.discover_and_scrape_streaming()
                
                stats = scraper.stats
                duration = time.time() - start_time
                
                result = {
                    'framework_id': framework_id,
                    'framework_name': framework_name,
                    'status': 'completed',
                    'pages_scraped': stats.get('pages_scraped', 0),
                    'pages_skipped': stats.get('pages_skipped', 0),
                    'pages_failed': stats.get('pages_failed', 0),
                    'duration': duration
                }
                
                print(f"✅ {framework_name}: {result['pages_scraped']} scraped, {result['pages_skipped']} skipped, {result['pages_failed']} failed ({duration:.1f}s)")
                return result
                
        except Exception as e:
            duration = time.time() - start_time
            result = {
                'framework_id': framework_id,
                'framework_name': framework_name,
                'status': 'failed',
                'error': str(e),
                'duration': duration
            }
            print(f"❌ {framework_name} failed: {e}")
            return result
    
    def update_master_progress(self, current_framework: str, stats: ScrapingStats):
        """Update master progress file with current status"""
        content = f"""Apple Documentation Comprehensive Scraping Progress

Current Framework: {current_framework}
Progress: {stats.completed_frameworks}/{stats.total_frameworks} frameworks
Completed: {stats.completed_frameworks}
Skipped: {stats.skipped_frameworks} 
Failed: {stats.failed_frameworks}

Total Pages:
- Scraped: {stats.total_pages_scraped}
- Skipped: {stats.total_pages_skipped}
- Failed: {stats.total_pages_failed}

Started: {time.ctime(stats.start_time) if stats.start_time else 'Not started'}
Duration: {(time.time() - stats.start_time) / 3600:.1f} hours
"""
        self.progress_file.write_text(content)
    
    async def scrape_batch_concurrent(self, frameworks: List[Dict[str, str]]) -> List[Dict]:
        """Scrape a batch of frameworks concurrently"""
        tasks = []
        for framework in frameworks:
            task = self.scrape_single_framework(framework)
            tasks.append(task)
        
        # Run batch concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Handle exceptions
        processed_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                framework = frameworks[i]
                processed_results.append({
                    'framework_id': framework['id'],
                    'framework_name': framework['title'],
                    'status': 'failed',
                    'error': str(result),
                    'duration': 0
                })
            else:
                processed_results.append(result)
        
        return processed_results
    
    async def scrape_all_frameworks(self):
        """Main method to scrape all Apple frameworks comprehensively"""
        self.stats.start_time = time.time()
        
        print("🍎 COMPREHENSIVE APPLE DOCUMENTATION SCRAPER")
        print("=" * 60)
        print(f"Max concurrent scrapers: {self.max_concurrent}")
        if self.resume_from:
            print(f"Resuming from: {self.resume_from}")
        print()
        
        # Get all frameworks dynamically
        frameworks = await self.get_all_frameworks()
        self.stats.total_frameworks = len(frameworks)
        
        # Filter frameworks if resuming
        if self.resume_from:
            resume_index = next((i for i, fw in enumerate(frameworks) if fw['id'] == self.resume_from), 0)
            frameworks = frameworks[resume_index:]
            print(f"📍 Resuming from framework {resume_index + 1}/{self.stats.total_frameworks}")
        
        # Process frameworks in batches
        all_results = []
        
        for i in range(0, len(frameworks), self.max_concurrent):
            batch_frameworks = frameworks[i:i + self.max_concurrent]
            
            # Check which frameworks to skip
            frameworks_to_scrape = []
            for framework in batch_frameworks:
                should_skip, reason = self.should_skip_framework(framework)
                if should_skip:
                    print(f"⏭️  Skipping {framework['title']}: {reason}")
                    self.stats.skipped_frameworks += 1
                else:
                    frameworks_to_scrape.append(framework)
            
            if not frameworks_to_scrape:
                continue
            
            # Update progress
            current_fw_names = [fw['title'] for fw in frameworks_to_scrape]
            print(f"\n📦 Batch {i//self.max_concurrent + 1}: {', '.join(current_fw_names)}")
            self.update_master_progress(', '.join(current_fw_names), self.stats)
            
            # Scrape the batch concurrently
            batch_results = await self.scrape_batch_concurrent(frameworks_to_scrape)
            
            # Update stats for all results in batch
            for result in batch_results:
                if result['status'] == 'completed':
                    self.stats.completed_frameworks += 1
                    self.stats.total_pages_scraped += result.get('pages_scraped', 0)
                    self.stats.total_pages_skipped += result.get('pages_skipped', 0)
                    self.stats.total_pages_failed += result.get('pages_failed', 0)
                else:
                    self.stats.failed_frameworks += 1
            
            # Update progress after batch completes
            self.update_master_progress(', '.join([fw['title'] for fw in frameworks_to_scrape]), self.stats)
            
            all_results.extend(batch_results)
            
            print(f"📊 Progress: {self.stats.completed_frameworks + self.stats.skipped_frameworks + self.stats.failed_frameworks}/{self.stats.total_frameworks} frameworks processed")
        
        self.stats.end_time = time.time()
        
        # Save final results
        await self.save_final_results(all_results)
        
        # Print final summary
        self.print_final_summary()
    
    async def save_final_results(self, results: List[Dict]):
        """Save comprehensive scraping results"""
        output = {
            "metadata": {
                "scraping_method": "Comprehensive Apple Documentation Scraper",
                "start_time": self.stats.start_time,
                "end_time": self.stats.end_time,
                "duration_hours": (self.stats.end_time - self.stats.start_time) / 3600,
                "total_frameworks": self.stats.total_frameworks,
                "completed_frameworks": self.stats.completed_frameworks,
                "skipped_frameworks": self.stats.skipped_frameworks,
                "failed_frameworks": self.stats.failed_frameworks,
                "total_pages_scraped": self.stats.total_pages_scraped,
                "total_pages_skipped": self.stats.total_pages_skipped,
                "total_pages_failed": self.stats.total_pages_failed
            },
            "results": results
        }
        
        results_file = Path("comprehensive_scraping_results.json")
        with open(results_file, 'w') as f:
            json.dump(output, f, indent=2)
        
        print(f"💾 Final results saved to: {results_file}")
    
    def print_final_summary(self):
        """Print final scraping summary"""
        duration = self.stats.end_time - self.stats.start_time
        
        print("\n" + "=" * 60)
        print("🎉 COMPREHENSIVE SCRAPING COMPLETE!")
        print("=" * 60)
        print(f"Duration: {duration / 3600:.1f} hours")
        print(f"Total Frameworks: {self.stats.total_frameworks}")
        print(f"✅ Completed: {self.stats.completed_frameworks}")
        print(f"⏭️  Skipped: {self.stats.skipped_frameworks}")
        print(f"❌ Failed: {self.stats.failed_frameworks}")
        print()
        print(f"📄 Total Pages:")
        print(f"   Scraped: {self.stats.total_pages_scraped:,}")
        print(f"   Skipped: {self.stats.total_pages_skipped:,}")
        print(f"   Failed: {self.stats.total_pages_failed:,}")
        print()
        
        if self.stats.completed_frameworks > 0:
            avg_pages = self.stats.total_pages_scraped / self.stats.completed_frameworks
            print(f"📊 Average pages per framework: {avg_pages:.1f}")
        
        print(f"🍎 Apple's entire documentation ecosystem now available locally!")

async def main():
    """Main entry point"""
    import sys
    
    # Parse command line arguments
    resume_from = None
    max_concurrent = 3
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--resume':
            resume_from = sys.argv[2] if len(sys.argv) > 2 else None
        elif sys.argv[1] == '--concurrent':
            max_concurrent = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    
    scraper = ComprehensiveAppleScraper(max_concurrent=max_concurrent, resume_from=resume_from)
    await scraper.scrape_all_frameworks()

if __name__ == "__main__":
    # Usage examples:
    # python3 comprehensive_scraper.py                    # Scrape everything
    # python3 comprehensive_scraper.py --resume SwiftUI  # Resume from SwiftUI
    # python3 comprehensive_scraper.py --concurrent 5    # Use 5 concurrent scrapers
    asyncio.run(main())