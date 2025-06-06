#!/usr/bin/env python3
"""
COMPREHENSIVE Apple Documentation Scraper (Fixed Version)
Improved error handling and timeout management
"""

import asyncio
import json
import time
from pathlib import Path
from typing import List, Dict, Set, Optional
from dataclasses import dataclass

from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

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

class ComprehensiveAppleScraperFixed:
    """Fixed comprehensive scraper with improved error handling"""
    
    def __init__(self, max_concurrent: int = 3, resume_from: Optional[str] = None):
        self.max_concurrent = max_concurrent
        self.resume_from = resume_from
        self.stats = ScrapingStats()
        self.progress_file = Path("scraping_master_progress.txt")
        self.completed_frameworks: Set[str] = set()
        self.framework_timeout = 3600  # 1 hour timeout per framework
        
    async def get_all_frameworks(self) -> List[Dict[str, str]]:
        """Get the complete framework list from the fixed JSON file"""
        logger.info("Loading framework list...")
        
        framework_file = Path("data/fixed_frameworks_list.json")
        if not framework_file.exists():
            raise Exception("Fixed framework list not found. Run fix_framework_list.py first!")
            
        with open(framework_file, 'r') as f:
            data = json.load(f)
            frameworks = data.get('frameworks', [])
            
        if not frameworks:
            raise Exception("No frameworks found in fixed list")
            
        logger.info(f"Loaded {len(frameworks)} frameworks from fixed list")
        return frameworks
    
    def should_skip_framework(self, framework: Dict[str, str]) -> tuple:
        """Check if we should skip this framework"""
        framework_id = framework['id']
        
        # Check resume point
        if self.resume_from:
            if framework_id != self.resume_from and framework_id not in self.completed_frameworks:
                return True, f"Before resume point ({self.resume_from})"
        
        # Check if framework folder exists and has substantial content
        framework_dir = Path(f"documentation/{framework_id}")
        if framework_dir.exists():
            md_files = list(framework_dir.rglob("*.md"))
            if len(md_files) > 10:
                progress_file = framework_dir / "scraping_progress.txt"
                if progress_file.exists():
                    content = progress_file.read_text()
                    if "Completed scraping" in content and "failed: 0" in content:
                        return True, f"Already completed ({len(md_files)} files)"
        
        return False, ""
    
    async def scrape_single_framework_with_timeout(self, framework: Dict[str, str]) -> Dict:
        """Scrape a single framework with timeout"""
        try:
            # Create task with timeout
            task = asyncio.create_task(self.scrape_single_framework(framework))
            result = await asyncio.wait_for(task, timeout=self.framework_timeout)
            return result
        except asyncio.TimeoutError:
            framework_id = framework['id']
            framework_name = framework['title']
            logger.error(f"Framework {framework_name} timed out after {self.framework_timeout}s")
            return {
                'framework_id': framework_id,
                'framework_name': framework_name,
                'status': 'timeout',
                'error': f'Timeout after {self.framework_timeout} seconds',
                'duration': self.framework_timeout
            }
    
    async def scrape_single_framework(self, framework: Dict[str, str]) -> Dict:
        """Scrape a single framework completely"""
        framework_id = framework['id']
        framework_name = framework['title']
        
        start_time = time.time()
        
        try:
            logger.info(f"Starting {framework_name} ({framework_id})...")
            
            # Clear any stale progress files
            progress_file = Path(f"documentation/{framework_id}/scraping_progress.txt")
            if progress_file.exists():
                # Check if it's a stale incomplete file
                content = progress_file.read_text()
                if "in progress..." in content and "Completed scraping" not in content:
                    logger.warning(f"Clearing stale progress file for {framework_id}")
                    progress_file.unlink()
            
            async with AppleJSONDocumentationScraper(framework_id, framework_name) as scraper:
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
                
                logger.info(
                    f"Completed {framework_name}: "
                    f"{result['pages_scraped']} scraped, "
                    f"{result['pages_skipped']} skipped, "
                    f"{result['pages_failed']} failed "
                    f"({duration:.1f}s)"
                )
                return result
                
        except Exception as e:
            duration = time.time() - start_time
            logger.error(f"Framework {framework_name} failed: {e}")
            return {
                'framework_id': framework_id,
                'framework_name': framework_name,
                'status': 'failed',
                'error': str(e),
                'duration': duration
            }
    
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
        """Scrape a batch of frameworks concurrently with timeout"""
        tasks = []
        for framework in frameworks:
            task = self.scrape_single_framework_with_timeout(framework)
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
        """Main method to scrape all Apple frameworks"""
        self.stats.start_time = time.time()
        
        logger.info("COMPREHENSIVE APPLE DOCUMENTATION SCRAPER (Fixed)")
        logger.info("=" * 60)
        logger.info(f"Max concurrent scrapers: {self.max_concurrent}")
        logger.info(f"Framework timeout: {self.framework_timeout}s")
        if self.resume_from:
            logger.info(f"Resuming from: {self.resume_from}")
        
        # Get all frameworks
        frameworks = await self.get_all_frameworks()
        self.stats.total_frameworks = len(frameworks)
        
        # Filter frameworks if resuming
        if self.resume_from:
            resume_index = next((i for i, fw in enumerate(frameworks) if fw['id'] == self.resume_from), 0)
            frameworks = frameworks[resume_index:]
            logger.info(f"Resuming from framework {resume_index + 1}/{self.stats.total_frameworks}")
        
        # Process frameworks in batches
        all_results = []
        
        for i in range(0, len(frameworks), self.max_concurrent):
            batch_frameworks = frameworks[i:i + self.max_concurrent]
            
            # Check which frameworks to skip
            frameworks_to_scrape = []
            for framework in batch_frameworks:
                should_skip, reason = self.should_skip_framework(framework)
                if should_skip:
                    logger.info(f"Skipping {framework['title']}: {reason}")
                    self.stats.skipped_frameworks += 1
                    self.stats.completed_frameworks += 1
                else:
                    frameworks_to_scrape.append(framework)
            
            if not frameworks_to_scrape:
                continue
            
            # Update progress
            current_fw_names = [fw['title'] for fw in frameworks_to_scrape]
            logger.info(f"\nBatch {i//self.max_concurrent + 1}: {', '.join(current_fw_names)}")
            self.update_master_progress(', '.join(current_fw_names), self.stats)
            
            # Scrape the batch
            batch_results = await self.scrape_batch_concurrent(frameworks_to_scrape)
            
            # Update stats
            for result in batch_results:
                if result['status'] == 'completed':
                    self.stats.completed_frameworks += 1
                    self.stats.total_pages_scraped += result.get('pages_scraped', 0)
                    self.stats.total_pages_skipped += result.get('pages_skipped', 0)
                    self.stats.total_pages_failed += result.get('pages_failed', 0)
                elif result['status'] in ['failed', 'timeout']:
                    self.stats.failed_frameworks += 1
                    self.stats.completed_frameworks += 1
            
            # Update progress after batch
            self.update_master_progress('Batch complete', self.stats)
            
            all_results.extend(batch_results)
            
            logger.info(
                f"Progress: {self.stats.completed_frameworks}/{self.stats.total_frameworks} "
                f"frameworks processed"
            )
        
        self.stats.end_time = time.time()
        
        # Save final results
        await self.save_final_results(all_results)
        
        # Print final summary
        self.print_final_summary()
    
    async def save_final_results(self, results: List[Dict]):
        """Save comprehensive scraping results"""
        output = {
            "metadata": {
                "scraping_method": "Comprehensive Apple Documentation Scraper (Fixed)",
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
        
        results_file = Path("comprehensive_scraping_results_fixed.json")
        with open(results_file, 'w') as f:
            json.dump(output, f, indent=2)
        
        logger.info(f"Final results saved to: {results_file}")
    
    def print_final_summary(self):
        """Print final scraping summary"""
        duration = self.stats.end_time - self.stats.start_time
        
        print("\n" + "=" * 60)
        print("🎉 COMPREHENSIVE SCRAPING COMPLETE!")
        print("=" * 60)
        print(f"Duration: {duration / 3600:.1f} hours")
        print(f"Total Frameworks: {self.stats.total_frameworks}")
        print(f"✅ Completed: {self.stats.completed_frameworks - self.stats.skipped_frameworks - self.stats.failed_frameworks}")
        print(f"⏭️  Skipped: {self.stats.skipped_frameworks}")
        print(f"❌ Failed: {self.stats.failed_frameworks}")
        print()
        print(f"📄 Total Pages:")
        print(f"   Scraped: {self.stats.total_pages_scraped:,}")
        print(f"   Skipped: {self.stats.total_pages_skipped:,}")
        print(f"   Failed: {self.stats.total_pages_failed:,}")
        print()
        
        if self.stats.completed_frameworks > 0:
            avg_pages = self.stats.total_pages_scraped / (self.stats.completed_frameworks - self.stats.skipped_frameworks)
            print(f"📊 Average pages per framework: {avg_pages:.1f}")
        
        print(f"🍎 Apple's documentation ecosystem scraping complete!")

async def main():
    """Main entry point"""
    import sys
    
    # Parse command line arguments
    resume_from = None
    max_concurrent = 3
    
    if '--resume' in sys.argv:
        idx = sys.argv.index('--resume')
        if idx + 1 < len(sys.argv):
            resume_from = sys.argv[idx + 1]
    
    if '--concurrent' in sys.argv:
        idx = sys.argv.index('--concurrent')
        if idx + 1 < len(sys.argv):
            max_concurrent = int(sys.argv[idx + 1])
    
    scraper = ComprehensiveAppleScraperFixed(max_concurrent=max_concurrent, resume_from=resume_from)
    await scraper.scrape_all_frameworks()

if __name__ == "__main__":
    asyncio.run(main())