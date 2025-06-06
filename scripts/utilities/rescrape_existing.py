#!/usr/bin/env python3
"""
Re-scrape existing frameworks to apply cross-framework link fixes
"""

import asyncio
import sys
from pathlib import Path
import shutil

async def rescrape_existing_frameworks():
    """Re-scrape existing frameworks by clearing hash caches"""
    
    print("🔄 RE-SCRAPING EXISTING FRAMEWORKS")
    print("=" * 50)
    print("This will re-scrape frameworks that already exist to apply cross-framework link fixes")
    print()
    
    # Find existing framework directories
    documentation_dir = Path("documentation")
    if not documentation_dir.exists():
        print("❌ No documentation directory found")
        return
    
    existing_frameworks = []
    for framework_dir in documentation_dir.iterdir():
        if framework_dir.is_dir() and framework_dir.name != ".DS_Store":
            md_files = list(framework_dir.rglob("*.md"))
            if md_files:
                existing_frameworks.append({
                    'name': framework_dir.name,
                    'path': framework_dir,
                    'file_count': len(md_files)
                })
    
    if not existing_frameworks:
        print("❌ No existing framework documentation found")
        return
    
    print(f"📁 Found {len(existing_frameworks)} existing frameworks:")
    for fw in existing_frameworks:
        print(f"  - {fw['name']}: {fw['file_count']} files")
    
    # Check which option to use
    if '--clear-hashes' in sys.argv:
        print("\\n🗑️  Clearing hash caches to force re-scraping...")
        
        hash_dir = Path(".hashes")
        if hash_dir.exists():
            # Clear all hash files
            for hash_file in hash_dir.glob("*_hashes.json"):
                print(f"   Removing {hash_file}")
                hash_file.unlink()
        
        print("✅ Hash caches cleared - all frameworks will be re-scraped on next run")
        print("💡 Now run: python3 scrape_all_frameworks.py --yes")
        return
    
    elif '--clear-specific' in sys.argv:
        # Clear hash for specific frameworks
        frameworks_to_clear = []
        for i, arg in enumerate(sys.argv):
            if arg == '--clear-specific' and i + 1 < len(sys.argv):
                frameworks_to_clear = sys.argv[i + 1:] 
                break
        
        if not frameworks_to_clear:
            print("❌ No frameworks specified. Usage: --clear-specific Accelerate Accessibility")
            return
        
        print(f"\\n🎯 Clearing hashes for specific frameworks: {frameworks_to_clear}")
        hash_dir = Path(".hashes")
        
        for fw_name in frameworks_to_clear:
            hash_file = hash_dir / f"{fw_name}_hashes.json"
            if hash_file.exists():
                print(f"   Removing {hash_file}")
                hash_file.unlink()
            else:
                print(f"   No hash file found for {fw_name}")
        
        print("✅ Specific hash caches cleared")
        print("💡 Now run: python3 scrape_all_frameworks.py --yes")
        return
    
    elif '--delete-and-rescrape' in sys.argv:
        print("\\n⚠️  WARNING: This will delete ALL existing documentation!")
        if '--yes' not in sys.argv:
            response = input("Are you sure you want to delete everything and start over? (y/N): ")
            if response.lower() not in ['y', 'yes']:
                print("❌ Aborted")
                return
        
        print("🗑️  Deleting all existing documentation...")
        
        # Delete documentation directory
        if documentation_dir.exists():
            shutil.rmtree(documentation_dir)
            print("   Removed documentation/")
        
        # Delete hash directory  
        hash_dir = Path(".hashes")
        if hash_dir.exists():
            shutil.rmtree(hash_dir)
            print("   Removed .hashes/")
        
        print("✅ All existing documentation deleted")
        print("💡 Now run: python3 scrape_all_frameworks.py --yes")
        return
    
    else:
        print("\\n📋 AVAILABLE OPTIONS:")
        print()
        print("1. 🔄 Clear all hash caches (recommended):")
        print(f"   python3 {sys.argv[0]} --clear-hashes")
        print("   • Keeps existing files, forces re-scraping to apply fixes")
        print("   • Fast and safe approach")
        print()
        print("2. 🎯 Clear specific framework hashes:")
        print(f"   python3 {sys.argv[0]} --clear-specific Accelerate Accessibility")
        print("   • Only re-scrapes specified frameworks")
        print()
        print("3. 🗑️  Delete everything and start over:")
        print(f"   python3 {sys.argv[0]} --delete-and-rescrape --yes")
        print("   • Nuclear option - deletes all existing docs")
        print("   • Use only if you want a completely fresh start")
        print()
        print("💡 After clearing hashes, run: python3 scrape_all_frameworks.py --yes")

if __name__ == "__main__":
    asyncio.run(rescrape_existing_frameworks())