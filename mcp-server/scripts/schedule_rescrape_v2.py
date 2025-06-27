#!/usr/bin/env python3
"""
Weekly rescrape scheduler for Apple Docs V2 with Meilisearch

This scheduler:
1. Runs the scraper to update markdown files
2. Runs the Meilisearch indexer to update the search index

Default schedule: Every Sunday at 1:00 AM
"""

import os
import sys
import time
import subprocess
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('/data/logs/scheduler.log' if Path('/data/logs').exists() else 'scheduler.log')
    ]
)
logger = logging.getLogger(__name__)

# Configuration
SCHEDULE_DAY = 6  # Sunday (0=Monday, 6=Sunday)
SCHEDULE_HOUR = 1  # 1 AM
CHECK_INTERVAL = 3600  # Check every hour


def get_next_scheduled_time() -> datetime:
    """Calculate the next scheduled run time"""
    now = datetime.now()
    
    # Find next Sunday at 1 AM
    days_ahead = SCHEDULE_DAY - now.weekday()
    if days_ahead < 0:  # Target day already passed this week
        days_ahead += 7
    elif days_ahead == 0 and now.hour >= SCHEDULE_HOUR:  # Today but past scheduled hour
        days_ahead += 7
    
    next_run = now.replace(hour=SCHEDULE_HOUR, minute=0, second=0, microsecond=0)
    next_run += timedelta(days=days_ahead)
    
    return next_run


def should_run_now(last_run_file: Path) -> bool:
    """Check if we should run the rescrape now"""
    now = datetime.now()
    
    # Check if it's the scheduled time
    if now.weekday() != SCHEDULE_DAY or now.hour != SCHEDULE_HOUR:
        return False
    
    # Check if we already ran today
    if last_run_file.exists():
        last_run_str = last_run_file.read_text().strip()
        try:
            last_run = datetime.fromisoformat(last_run_str)
            if (now - last_run).total_seconds() < 86400:  # Less than 24 hours
                return False
        except:
            pass
    
    return True


def run_weekly_rescrape() -> bool:
    """Run the weekly rescrape, cleanup orphans, and full reindex process"""
    logger.info("🔄 Starting weekly rescrape process (with orphan cleanup and full reindex)...")
    start_time = datetime.now()
    
    # Use meilisearch directory for state files
    state_path = Path("/data/meilisearch")
    state_path.mkdir(parents=True, exist_ok=True)
    
    try:
        # Step 1: Run the scraper
        logger.info("📥 Step 1: Running scraper to update documentation...")
        
        # Find scraper location
        if Path("/app/scrape.py").exists():
            # Docker environment - scrape.py is at /app/
            scraper_path = Path("/app")
        else:
            # Local development - go up to project root
            scraper_path = Path(__file__).parent.parent.parent
            
        scrape_script = scraper_path / "scrape.py"
        if not scrape_script.exists():
            logger.error(f"Scraper script not found: {scrape_script}")
            return False
        
        os.chdir(scraper_path)
        
        # Run scraper with orphan cleanup
        env = os.environ.copy()
        cmd = [sys.executable, "scrape.py", "--all", "--yes", "--cleanup-orphans", "--auto-cleanup"]
        
        result = subprocess.run(cmd, env=env, capture_output=True, text=True)
        
        if result.returncode != 0:
            logger.error(f"❌ Scraper failed with return code {result.returncode}")
            if result.stderr:
                logger.error(f"Error output: {result.stderr}")
            return False
            
        logger.info("✅ Scraping completed successfully")
        
        # Log scraper output
        if result.stdout:
            for line in result.stdout.split('\n')[-20:]:  # Last 20 lines
                if line.strip():
                    logger.info(f"Scraper: {line}")
        
        # Step 2: Run Meilisearch indexing (full delete and rebuild)
        logger.info("📥 Step 2: Full re-indexing to Meilisearch (delete and rebuild)...")
        
        # Find scripts directory
        if Path("/app/scripts").exists():
            # Docker environment
            scripts_path = Path("/app/scripts")
        else:
            # Local development
            scripts_path = Path(__file__).parent
            
        os.chdir(scripts_path)
        
        # Force full rebuild to ensure orphaned documents are removed from search index
        docs_path = "/data/documentation" if Path("/data/documentation").exists() else "../documentation"
        cmd = [sys.executable, "index_to_meilisearch.py", "--docs-path", docs_path, "--force"]
        
        result = subprocess.run(cmd, env=env, capture_output=True, text=True)
        
        if result.returncode != 0:
            logger.error(f"❌ Indexing failed with return code {result.returncode}")
            if result.stderr:
                logger.error(f"Error output: {result.stderr}")
            return False
            
        logger.info("✅ Full re-indexing completed successfully")
        
        # Log indexer output
        if result.stdout:
            for line in result.stdout.split('\n')[-10:]:  # Last 10 lines
                if line.strip():
                    logger.info(f"Indexer: {line}")
        
        # Record successful update
        (state_path / "last_weekly_update.txt").write_text(start_time.isoformat())
        (state_path / "last_update.txt").write_text(start_time.strftime("%Y-%m-%d %H:%M:%S"))
        
        elapsed = datetime.now() - start_time
        logger.info(f"✅ Weekly rescrape and reindex completed in {elapsed}")
        
        # Log final document count if possible
        try:
            import httpx
            meili_key = os.getenv("MEILI_MASTER_KEY")
            if meili_key:
                response = httpx.get(
                    "http://localhost:7700/indexes/apple-docs/stats",
                    headers={"Authorization": f"Bearer {meili_key}"}
                )
                if response.status_code == 200:
                    stats = response.json()
                    doc_count = stats.get('numberOfDocuments', 0)
                    logger.info(f"📊 Total documents indexed: {doc_count:,}")
        except:
            pass  # Stats logging is optional
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Weekly rescrape failed with exception: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


def main():
    """Main scheduler loop"""
    logger.info("🕐 Apple Docs V2 Weekly Rescrape Scheduler Started")
    logger.info(f"📅 Schedule: Every Sunday at {SCHEDULE_HOUR}:00 AM")
    logger.info(f"⏱️  Check interval: Every {CHECK_INTERVAL} seconds")
    
    # Ensure we're using the correct timezone
    tz = os.getenv('TZ', 'America/New_York')
    logger.info(f"🌍 Timezone: {tz}")
    
    # Get last run file path
    state_path = Path("/data/meilisearch")
    last_run_file = state_path / "last_weekly_update.txt"
    
    # Show next scheduled run
    next_run = get_next_scheduled_time()
    logger.info(f"⏭️  Next scheduled run: {next_run}")
    
    while True:
        try:
            if should_run_now(last_run_file):
                logger.info("🎯 It's time for the weekly rescrape!")
                
                if run_weekly_rescrape():
                    logger.info("✅ Weekly rescrape completed successfully")
                else:
                    logger.error("❌ Weekly rescrape failed")
                
                # Update next run time
                next_run = get_next_scheduled_time()
                logger.info(f"⏭️  Next scheduled run: {next_run}")
            
            # Sleep until next check
            time.sleep(CHECK_INTERVAL)
            
        except KeyboardInterrupt:
            logger.info("⏹️  Scheduler stopped by user")
            break
        except Exception as e:
            logger.error(f"❌ Scheduler error: {e}")
            time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()