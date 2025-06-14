#!/usr/bin/env python3
"""
Scheduler for automatic weekly rescraping of Apple documentation.
Runs every Sunday at 1:00 AM to check for updates and rescrape if needed.
"""

import os
import sys
import time
import logging
from datetime import datetime, timedelta
import subprocess
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from server.logger import get_logger

# Setup logging
logger = get_logger(__name__)

# Configuration
RESCRAPE_DAY = 6  # Sunday (0=Monday, 6=Sunday)
RESCRAPE_HOUR = 1  # 1:00 AM
CHECK_INTERVAL = 3600  # Check every hour


def get_next_sunday_1am():
    """Calculate the next Sunday at 1:00 AM"""
    now = datetime.now()
    
    # Find next Sunday
    days_until_sunday = (RESCRAPE_DAY - now.weekday()) % 7
    if days_until_sunday == 0 and now.hour >= RESCRAPE_HOUR:
        # It's Sunday but past 1 AM, so next week
        days_until_sunday = 7
    
    next_sunday = now + timedelta(days=days_until_sunday)
    next_sunday = next_sunday.replace(hour=RESCRAPE_HOUR, minute=0, second=0, microsecond=0)
    
    return next_sunday


def should_run_now():
    """Check if we should run the rescrape now"""
    now = datetime.now()
    
    # Check if it's Sunday at 1 AM (within the current hour)
    if now.weekday() == RESCRAPE_DAY and now.hour == RESCRAPE_HOUR:
        # Check if we've already run this week
        last_update_file = Path("/data/hashes/last_weekly_update.txt")
        if last_update_file.exists():
            try:
                last_update = datetime.fromisoformat(last_update_file.read_text().strip())
                # If we ran less than 6 days ago, skip
                if (now - last_update).days < 6:
                    return False
            except Exception as e:
                logger.warning(f"Could not read last update time: {e}")
        
        return True
    
    return False


def run_rescrape():
    """Run the rescraping and embedding process"""
    logger.info("🔄 Starting weekly rescrape process...")
    
    # Record start time
    start_time = datetime.now()
    hashes_path = Path("/data/hashes")
    hashes_path.mkdir(parents=True, exist_ok=True)
    
    try:
        # Change to the scraper directory
        scraper_path = Path(__file__).parent.parent.parent / "scraper"
        if not scraper_path.exists():
            logger.error(f"Scraper directory not found: {scraper_path}")
            return False
        
        os.chdir(scraper_path)
        
        # Run the combined scrape and embed script
        logger.info("📥 Running scraper with automatic embedding...")
        
        # Build command with environment variables
        env = os.environ.copy()
        env["PYTHONPATH"] = str(Path(__file__).parent.parent.parent)
        
        # Determine if we should keep markdown files
        keep_markdown = os.getenv("KEEP_MARKDOWN_FILES", "true").lower() == "true"
        
        cmd = [
            sys.executable,
            "auto_scrape_and_embed.py",
            "--embed",  # Enable automatic embedding
            "--yes"     # Skip confirmation prompts
        ]
        
        if not keep_markdown:
            logger.info("🗑️  Markdown files will be deleted after embedding (KEEP_MARKDOWN_FILES=false)")
        
        # Run the scraper
        result = subprocess.run(
            cmd,
            env=env,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            logger.error(f"❌ Scraper failed with return code {result.returncode}")
            logger.error(f"Error output: {result.stderr}")
            return False
        
        # Log output
        if result.stdout:
            for line in result.stdout.split('\n'):
                if line.strip():
                    logger.info(f"Scraper: {line}")
        
        # Record successful update
        (hashes_path / "last_weekly_update.txt").write_text(start_time.isoformat())
        (hashes_path / "last_update.txt").write_text(start_time.strftime("%Y-%m-%d %H:%M:%S"))
        
        elapsed = datetime.now() - start_time
        logger.info(f"✅ Weekly rescrape completed in {elapsed}")
        
        # Clean up if needed
        if not keep_markdown:
            documentation_path = Path("/data/documentation")
            if documentation_path.exists():
                logger.info("🧹 Cleaning up markdown files...")
                # The scraper should have already cleaned up, but double-check
                md_files = list(documentation_path.rglob("*.md"))
                if md_files:
                    logger.info(f"Found {len(md_files)} markdown files to clean")
                    for f in md_files:
                        try:
                            f.unlink()
                        except Exception as e:
                            logger.warning(f"Could not delete {f}: {e}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Rescrape failed with error: {e}", exc_info=True)
        return False


def main():
    """Main scheduler loop"""
    logger.info("🕐 Apple Docs Weekly Rescrape Scheduler Started")
    logger.info(f"📅 Schedule: Every Sunday at 1:00 AM")
    logger.info(f"⏱️  Check interval: Every {CHECK_INTERVAL} seconds")
    
    # Show next scheduled run
    next_run = get_next_sunday_1am()
    logger.info(f"⏭️  Next scheduled run: {next_run}")
    
    while True:
        try:
            # Check if we should run now
            if should_run_now():
                logger.info("🎯 It's time for the weekly rescrape!")
                
                # Run the rescrape
                success = run_rescrape()
                
                if success:
                    logger.info("✅ Weekly rescrape completed successfully")
                else:
                    logger.error("❌ Weekly rescrape failed")
                
                # Calculate next run time
                next_run = get_next_sunday_1am()
                logger.info(f"⏭️  Next scheduled run: {next_run}")
            
            # Sleep until next check
            time.sleep(CHECK_INTERVAL)
            
        except KeyboardInterrupt:
            logger.info("🛑 Scheduler stopped by user")
            break
        except Exception as e:
            logger.error(f"❌ Scheduler error: {e}", exc_info=True)
            # Continue running even if there's an error
            time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()