#!/usr/bin/env python3
"""
Collect and cleanup orphaned files at the end of scraping.
This collects all orphans across all frameworks and presents them once for approval.
"""

import sys
import os
from pathlib import Path
from typing import Dict, List, Tuple

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from analysis.check_orphans import HashManager
from scraper.utils.logger import get_logger

logger = get_logger(__name__)


def collect_all_orphans() -> Dict[str, List[Path]]:
    """Collect orphaned files from all frameworks."""
    hash_dir = Path(".hashes")
    doc_dir = Path("documentation")
    
    if not hash_dir.exists() or not doc_dir.exists():
        return {}
    
    orphans_by_framework = {}
    
    # Get all hash files
    hash_files = list(hash_dir.glob("*_hashes.json"))
    
    for hash_file in hash_files:
        framework_name = hash_file.stem.replace("_hashes", "")
        
        # Load hash manager
        hash_manager = HashManager(hash_file)
        
        # Get framework directory
        framework_dir = doc_dir / framework_name
        
        # Handle case sensitivity
        if not framework_dir.exists():
            possible_dirs = [d for d in doc_dir.iterdir() if d.is_dir() and d.name.lower() == framework_name.lower()]
            if possible_dirs:
                framework_dir = possible_dirs[0]
            else:
                continue
        
        # Find orphaned files
        orphaned_files = hash_manager.get_orphaned_files(framework_dir)
        
        if orphaned_files:
            # Safety check
            all_files = list(framework_dir.rglob("*.md"))
            if all_files and len(orphaned_files) > len(all_files) * 0.5:
                logger.warning(f"Skipping {framework_name}: too many orphans ({len(orphaned_files)}/{len(all_files)})")
                continue
            
            orphans_by_framework[framework_name] = orphaned_files
    
    return orphans_by_framework


def cleanup_orphans_with_approval(orphans_by_framework: Dict[str, List[Path]]) -> int:
    """Present all orphans and get approval once."""
    if not orphans_by_framework:
        return 0
    
    # Count total orphans
    total_orphans = sum(len(files) for files in orphans_by_framework.values())
    
    print("\n" + "=" * 70)
    print(f"🗑️  Detected that Apple has removed {total_orphans} pages across {len(orphans_by_framework)} frameworks:")
    print("=" * 70)
    
    # Group by framework for display
    for framework, files in sorted(orphans_by_framework.items()):
        print(f"\n📁 {framework} ({len(files)} files):")
        for orphan in files[:5]:  # Show first 5 per framework
            print(f"   • {orphan.name}")
        if len(files) > 5:
            print(f"   ... and {len(files) - 5} more files")
    
    print("\n" + "=" * 70)
    response = input("\n⚠️  These markdown files will be removed if you approve. Continue? (y/N): ")
    
    if response.lower() not in ['y', 'yes']:
        print("❌ Deletion cancelled by user")
        return 0
    
    # Perform deletion
    deleted_count = 0
    for framework, files in orphans_by_framework.items():
        print(f"\n🧹 Cleaning {framework}...")
        for orphan in files:
            try:
                orphan.unlink()
                deleted_count += 1
                
                # Remove empty directories
                parent = orphan.parent
                doc_dir = Path("documentation")
                framework_dir = doc_dir / framework
                while parent != framework_dir and parent != doc_dir:
                    try:
                        if not any(parent.iterdir()):
                            parent.rmdir()
                        parent = parent.parent
                    except OSError:
                        break
                        
            except Exception as e:
                logger.error(f"Failed to delete {orphan}: {e}")
    
    print(f"\n✅ Deleted {deleted_count} orphaned files")
    return deleted_count


def main():
    """Main entry point."""
    print("🔍 Collecting orphaned files across all frameworks...")
    
    orphans = collect_all_orphans()
    
    if not orphans:
        print("✅ No orphaned files found!")
        return
    
    cleanup_orphans_with_approval(orphans)


if __name__ == "__main__":
    main()