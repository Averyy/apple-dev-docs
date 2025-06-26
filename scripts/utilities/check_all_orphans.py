#!/usr/bin/env python3
"""
Check and optionally clean up orphaned files across all frameworks.
This is useful for running after a full scrape to see what Apple has removed.
"""

import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from analysis.check_orphans import check_orphans


def main():
    """Check all frameworks for orphans and prompt for deletion."""
    print("🔍 Checking for orphaned documentation files across all frameworks...")
    print("=" * 70)
    
    # First do a dry run to show what would be deleted
    total_orphans = check_orphans(framework=None, clean=False, dry_run=True)
    
    if total_orphans == 0:
        print("\n✅ No orphaned files found!")
        return
    
    print("\n" + "=" * 70)
    print(f"🗑️  Found {total_orphans} orphaned files across all frameworks")
    print("These are documentation pages that Apple has removed from their site.")
    print("=" * 70)
    
    # Ask if user wants to delete them
    response = input("\n⚠️  Would you like to delete these orphaned files? (y/N): ")
    
    if response.lower() in ['y', 'yes']:
        print("\n🧹 Cleaning up orphaned files...")
        deleted = check_orphans(framework=None, clean=True, dry_run=False)
        print(f"\n✅ Deleted {deleted} orphaned files")
    else:
        print("\n❌ Deletion cancelled. Files remain unchanged.")


if __name__ == "__main__":
    main()