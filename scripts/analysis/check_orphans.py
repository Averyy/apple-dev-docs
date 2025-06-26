#!/usr/bin/env python3
"""Simple orphan detection script using hash files."""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scraper.utils.hash_manager import HashManager
from scraper.utils.logger import get_logger

logger = get_logger(__name__)


def check_orphans(framework: str = None, clean: bool = False, dry_run: bool = True) -> int:
    """Check for orphaned markdown files.
    
    Args:
        framework: Specific framework to check (None for all)
        clean: Whether to delete orphaned files
        dry_run: If True, only report what would be deleted
        
    Returns:
        Total number of orphaned files found
    """
    hash_dir = Path(".hashes")
    doc_dir = Path("documentation")
    
    if not hash_dir.exists():
        logger.error("No .hashes directory found")
        return
        
    if not doc_dir.exists():
        logger.error("No documentation directory found")
        return
    
    # Get list of frameworks to check
    if framework:
        frameworks = [framework]
        hash_files = [hash_dir / f"{framework}_hashes.json"]
    else:
        # Get all hash files
        hash_files = list(hash_dir.glob("*_hashes.json"))
        frameworks = [f.stem.replace("_hashes", "") for f in hash_files]
    
    total_orphans = 0
    
    for framework_name, hash_file in zip(frameworks, hash_files):
        if not hash_file.exists():
            logger.warning(f"Hash file not found: {hash_file}")
            continue
            
        # Load hash manager for this framework
        hash_manager = HashManager(hash_file)
        
        # Get framework directory - handle case sensitivity
        framework_dir = doc_dir / framework_name
        
        # If exact case doesn't exist, try case-insensitive search
        if not framework_dir.exists():
            # Find matching directory case-insensitively
            possible_dirs = [d for d in doc_dir.iterdir() if d.is_dir() and d.name.lower() == framework_name.lower()]
            if possible_dirs:
                framework_dir = possible_dirs[0]
                logger.info(f"Using case-corrected directory: {framework_dir.name} for framework {framework_name}")
            else:
                logger.warning(f"Framework directory not found: {framework_dir}")
                continue
        
        # Find orphaned files
        orphaned_files = hash_manager.get_orphaned_files(framework_dir)
        
        # Safety check: if more than 50% of files would be deleted, something is wrong
        all_files = list(framework_dir.rglob("*.md"))
        if all_files and len(orphaned_files) > len(all_files) * 0.5:
            logger.error(
                "excessive_orphans_detected",
                framework=framework_name,
                orphaned=len(orphaned_files),
                total=len(all_files),
                percentage=f"{(len(orphaned_files)/len(all_files)*100):.1f}%"
            )
            print(f"\n⚠️  WARNING: {framework_name} has {len(orphaned_files)}/{len(all_files)} files marked as orphaned!")
            print("This seems excessive and may indicate a session tracking issue.")
            print("Skipping deletion for safety. Please investigate manually.")
            continue
        
        if orphaned_files:
            total_orphans += len(orphaned_files)
            if not framework:  # Only print details for interactive use
                print(f"\n{framework_name}: Found {len(orphaned_files)} orphaned files")
            
            for orphan in orphaned_files:
                if not framework:  # Only print details for interactive use
                    print(f"  - {orphan.relative_to(doc_dir)}")
                
                if clean and not dry_run:
                    try:
                        orphan.unlink()
                        logger.info(f"Deleted orphaned file: {orphan}")
                        
                        # Remove empty parent directories
                        parent = orphan.parent
                        while parent != framework_dir and parent != doc_dir:
                            try:
                                if not any(parent.iterdir()):
                                    parent.rmdir()
                                    logger.info(f"Removed empty directory: {parent}")
                                parent = parent.parent
                            except OSError:
                                break
                                
                    except Exception as e:
                        logger.error(f"Failed to delete {orphan}: {e}")
        else:
            if not framework:  # Only print status for interactive use
                print(f"{framework_name}: No orphaned files found")
    
    # Summary
    if not framework:  # Only print summary for full runs, not single framework calls
        print(f"\nTotal orphaned files: {total_orphans}")
        
        if clean and dry_run:
            print("\nThis was a dry run. Use --no-dry-run to actually delete files.")
        elif clean and not dry_run:
            print(f"\nDeleted {total_orphans} orphaned files.")
    
    return total_orphans


def cleanup_framework_orphans(framework_name: str, manual_approval: bool = False) -> int:
    """Clean up orphaned files for a specific framework.
    
    This is designed to be called from the main scraping workflow.
    
    Args:
        framework_name: Name of the framework to clean up
        manual_approval: If True, prompt user for approval before deleting
        
    Returns:
        Number of orphaned files that were deleted
    """
    try:
        # First, get the list of orphaned files
        hash_dir = Path(".hashes")
        doc_dir = Path("documentation")
        hash_file = hash_dir / f"{framework_name}_hashes.json"
        
        if not hash_file.exists():
            return 0
            
        hash_manager = HashManager(hash_file)
        framework_dir = doc_dir / framework_name
        
        # Handle case sensitivity
        if not framework_dir.exists():
            possible_dirs = [d for d in doc_dir.iterdir() if d.is_dir() and d.name.lower() == framework_name.lower()]
            if possible_dirs:
                framework_dir = possible_dirs[0]
            else:
                return 0
        
        orphaned_files = hash_manager.get_orphaned_files(framework_dir)
        
        if not orphaned_files:
            return 0
        
        # Safety check
        all_files = list(framework_dir.rglob("*.md"))
        if all_files and len(orphaned_files) > len(all_files) * 0.5:
            print(f"\n⚠️  WARNING: {framework_name} has {len(orphaned_files)}/{len(all_files)} files marked as orphaned!")
            print("This seems excessive and may indicate a session tracking issue.")
            print("Skipping deletion for safety.")
            return 0
        
        if manual_approval:
            print(f"\n🗑️  Detected that Apple has removed {len(orphaned_files)} pages from {framework_name}:")
            print("─" * 70)
            for orphan in orphaned_files[:20]:  # Show first 20
                print(f"  • {orphan.relative_to(doc_dir)}")
            if len(orphaned_files) > 20:
                print(f"  ... and {len(orphaned_files) - 20} more files")
            print("─" * 70)
            
            response = input("\n⚠️  These markdown files will be removed if you approve. Continue? (y/N): ")
            if response.lower() not in ['y', 'yes']:
                print("❌ Deletion cancelled by user")
                return 0
        
        # Perform deletion
        deleted_count = 0
        for orphan in orphaned_files:
            try:
                orphan.unlink()
                logger.info(f"Deleted orphaned file: {orphan}")
                deleted_count += 1
                
                # Remove empty parent directories
                parent = orphan.parent
                while parent != framework_dir and parent != doc_dir:
                    try:
                        if not any(parent.iterdir()):
                            parent.rmdir()
                            logger.info(f"Removed empty directory: {parent}")
                        parent = parent.parent
                    except OSError:
                        break
                        
            except Exception as e:
                logger.error(f"Failed to delete {orphan}: {e}")
        
        if deleted_count > 0:
            if manual_approval:
                print(f"✅ Deleted {deleted_count} orphaned files from {framework_name}")
            else:
                logger.info(f"Auto-cleaned {deleted_count} orphaned files from {framework_name}")
        
        return deleted_count
        
    except Exception as e:
        logger.error(f"Failed to clean orphans for {framework_name}: {e}")
        return 0


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Check for orphaned documentation files")
    parser.add_argument(
        "--framework",
        help="Check specific framework only"
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Delete orphaned files"
    )
    parser.add_argument(
        "--no-dry-run",
        action="store_true",
        help="Actually delete files (default is dry run)"
    )
    
    args = parser.parse_args()
    
    check_orphans(
        framework=args.framework,
        clean=args.clean,
        dry_run=not args.no_dry_run
    )


if __name__ == "__main__":
    main()