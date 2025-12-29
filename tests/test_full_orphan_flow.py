#!/usr/bin/env python3
"""Test the complete scraping and orphan detection flow."""

import asyncio
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.hash_manager import HashManager
from scraper.utils.logger import get_logger

logger = get_logger(__name__)


async def test_full_flow():
    """Test complete flow: initial scrape, re-scrape with orphan detection."""
    
    # Use a tiny test framework
    test_framework = "AutomaticAssessmentConfiguration"  # Very small framework (~10 pages)
    
    logger.info("="*60)
    logger.info(f"TESTING FULL SCRAPING + ORPHAN FLOW WITH {test_framework}")
    logger.info("="*60)
    
    # Paths
    output_dir = Config.get_framework_output_dir(test_framework)
    hash_file = Config.get_hash_file(test_framework)
    
    # Create backups
    backup_dir = Path(f"test_backup_{test_framework}")
    backup_hash = Path(f"test_backup_{test_framework}_hashes.json")
    
    if output_dir.exists():
        logger.info(f"Backing up existing {test_framework} documentation...")
        if backup_dir.exists():
            shutil.rmtree(backup_dir)
        shutil.copytree(output_dir, backup_dir)
        
    if hash_file.exists():
        logger.info(f"Backing up existing hash file...")
        shutil.copy2(hash_file, backup_hash)
    
    try:
        # Clean slate - remove existing files
        if output_dir.exists():
            shutil.rmtree(output_dir)
        if hash_file.exists():
            hash_file.unlink()
            
        logger.info("\n" + "="*40)
        logger.info("PHASE 1: INITIAL SCRAPE")
        logger.info("="*40)
        
        # Phase 1: Initial full scrape
        async with AppleJSONDocumentationScraper(test_framework) as scraper:
            stats = await scraper.scrape_framework()
            
        logger.info(f"\nInitial scrape complete:")
        logger.info(f"  Pages scraped: {stats['pages_scraped']}")
        logger.info(f"  Pages skipped: {stats['pages_skipped']}")
        logger.info(f"  Pages failed: {stats['pages_failed']}")
        logger.info(f"  Orphans deleted: {stats.get('orphaned_files_deleted', 0)}")
        
        # Check what was created
        md_files_phase1 = list(output_dir.rglob("*.md"))
        logger.info(f"  Files created: {len(md_files_phase1)}")
        
        # Examine hash file
        hash_manager1 = HashManager(hash_file)
        entries_with_path1 = sum(1 for d in hash_manager1.hashes.values() if "file_path" in d)
        entries_with_session1 = sum(1 for d in hash_manager1.hashes.values() if "session_id" in d)
        logger.info(f"\nHash file after initial scrape:")
        logger.info(f"  Total entries: {len(hash_manager1.hashes)}")
        logger.info(f"  Entries with file_path: {entries_with_path1}")
        logger.info(f"  Entries with session_id: {entries_with_session1}")
        
        # Show sample entries
        logger.info("\nSample hash entries:")
        for i, (url, data) in enumerate(hash_manager1.hashes.items()):
            if i >= 3:
                break
            logger.info(f"  {url}:")
            logger.info(f"    has file_path: {'file_path' in data}")
            logger.info(f"    has session_id: {'session_id' in data}")
            if 'file_path' in data:
                logger.info(f"    file_path: {data['file_path']}")
        
        # Phase 2: Create some files that will become orphans
        logger.info("\n" + "="*40)
        logger.info("PHASE 2: CREATE FUTURE ORPHANS")
        logger.info("="*40)
        
        orphan_files = [
            output_dir / "will_be_orphaned_1.md",
            output_dir / "subfolder" / "will_be_orphaned_2.md"
        ]
        
        for orphan in orphan_files:
            orphan.parent.mkdir(parents=True, exist_ok=True)
            orphan.write_text(f"# File that will become orphaned\n\nThis should be deleted.")
            logger.info(f"Created future orphan: {orphan.relative_to(output_dir)}")
        
        # Wait a moment to ensure time difference
        await asyncio.sleep(2)
        
        # Phase 3: Re-scrape (should detect and remove orphans)
        logger.info("\n" + "="*40)
        logger.info("PHASE 3: RE-SCRAPE WITH ORPHAN DETECTION")
        logger.info("="*40)
        
        async with AppleJSONDocumentationScraper(test_framework) as scraper:
            stats2 = await scraper.scrape_framework()
            
        logger.info(f"\nRe-scrape complete:")
        logger.info(f"  Pages scraped: {stats2['pages_scraped']}")
        logger.info(f"  Pages skipped: {stats2['pages_skipped']}")
        logger.info(f"  Pages failed: {stats2['pages_failed']}")
        logger.info(f"  Orphans deleted: {stats2.get('orphaned_files_deleted', 0)}")
        
        # Check orphan detection manually before cleanup
        logger.info(f"\nChecking orphan detection before cleanup...")
        hash_manager_before_cleanup = HashManager(hash_file)
        orphaned_before = hash_manager_before_cleanup.get_orphaned_files(output_dir)
        logger.info(f"Orphaned files detected: {len(orphaned_before)}")
        
        if len(orphaned_before) > 0:
            logger.info(f"Orphaned files:")
            for orphan in orphaned_before:
                logger.info(f"  - {orphan.relative_to(output_dir)}")
        
        # Manually run orphan cleanup (as scraper doesn't do it automatically)
        logger.info(f"\nRunning manual orphan cleanup...")
        from scripts.analysis.check_orphans import cleanup_framework_orphans
        orphan_count = cleanup_framework_orphans(test_framework)
        logger.info(f"Orphan cleanup deleted: {orphan_count} files")
        
        # Update stats to reflect orphan cleanup
        stats2['orphaned_files_deleted'] = orphan_count
        
        # Check final state
        md_files_phase3 = list(output_dir.rglob("*.md"))
        logger.info(f"  Files after re-scrape: {len(md_files_phase3)}")
        
        # Check if orphans were deleted
        orphans_exist = []
        orphans_deleted = []
        for orphan in orphan_files:
            if orphan.exists():
                orphans_exist.append(orphan)
                logger.error(f"❌ Orphan NOT deleted: {orphan.relative_to(output_dir)}")
            else:
                orphans_deleted.append(orphan)
                logger.info(f"✅ Orphan deleted: {orphan.relative_to(output_dir)}")
        
        # Final hash file check
        hash_manager3 = HashManager(hash_file)
        entries_with_path3 = sum(1 for d in hash_manager3.hashes.values() if "file_path" in d)
        entries_with_session3 = sum(1 for d in hash_manager3.hashes.values() if "session_id" in d)
        logger.info(f"\nHash file after re-scrape:")
        logger.info(f"  Total entries: {len(hash_manager3.hashes)}")
        logger.info(f"  Entries with file_path: {entries_with_path3}")
        logger.info(f"  Entries with session_id: {entries_with_session3}")
        
        # Summary
        logger.info("\n" + "="*60)
        logger.info("TEST SUMMARY")
        logger.info("="*60)
        logger.info(f"Framework: {test_framework}")
        logger.info(f"Initial scrape files: {len(md_files_phase1)}")
        logger.info(f"Orphans created: {len(orphan_files)}")
        logger.info(f"Orphans deleted: {len(orphans_deleted)}")
        logger.info(f"Final file count: {len(md_files_phase3)}")
        logger.info(f"Hash entries with file paths: {entries_with_path3}")
        
        # Pass/Fail
        if (len(orphans_deleted) == len(orphan_files) and 
            entries_with_path3 > 0 and 
            entries_with_session3 > 0):
            logger.info("\n✅ FULL FLOW TEST PASSED!")
            return True
        else:
            logger.error("\n❌ FULL FLOW TEST FAILED!")
            if entries_with_path3 == 0:
                logger.error("  - No hash entries have file_path")
            if entries_with_session3 == 0:
                logger.error("  - No hash entries have session_id")
            if len(orphans_deleted) < len(orphan_files):
                logger.error("  - Not all orphans were deleted")
            return False
            
    finally:
        # Restore backups
        logger.info("\n--- Restoring backups ---")
        if backup_dir.exists():
            if output_dir.exists():
                shutil.rmtree(output_dir)
            shutil.copytree(backup_dir, output_dir)
            shutil.rmtree(backup_dir)
            logger.info("Restored documentation backup")
            
        if backup_hash.exists():
            shutil.copy2(backup_hash, hash_file)
            backup_hash.unlink()
            logger.info("Restored hash file backup")


if __name__ == "__main__":
    success = asyncio.run(test_full_flow())
    sys.exit(0 if success else 1)