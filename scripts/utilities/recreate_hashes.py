#!/usr/bin/env python3
"""
Recreate hash files for frameworks that were scraped but are missing hash files.
This ensures incremental updates work properly.
"""

import json
import hashlib
from pathlib import Path
from datetime import datetime

def create_hash_file_for_framework(framework_id: str):
    """Create a hash file for a framework based on existing markdown files."""
    
    framework_dir = Path(f"documentation/{framework_id}")
    if not framework_dir.exists():
        print(f"❌ Framework directory not found: {framework_dir}")
        return
    
    # Get all markdown files
    md_files = list(framework_dir.rglob("*.md"))
    if not md_files:
        print(f"❌ No markdown files found in {framework_dir}")
        return
    
    print(f"📁 Found {len(md_files)} markdown files for {framework_id}")
    
    # Create hash entries for each file
    hashes = {}
    for md_file in md_files:
        # Convert file path back to URL
        relative_path = md_file.relative_to(framework_dir)
        url_path = str(relative_path).replace('.md', '').replace('/', '/')
        
        # Construct the documentation URL
        doc_url = f"https://developer.apple.com/documentation/{framework_id}/{url_path}"
        
        # Read file content and compute hash
        content = md_file.read_text()
        content_hash = hashlib.sha256(content.encode()).hexdigest()
        
        # Store in hash dict
        hashes[doc_url] = {
            "hash": content_hash,
            "last_modified": datetime.utcnow().isoformat()
        }
    
    # Create hash file
    hash_dir = Path(".hashes")
    hash_dir.mkdir(exist_ok=True)
    
    hash_file = hash_dir / f"{framework_id}_hashes.json"
    
    data = {
        "metadata": {
            "last_updated": datetime.utcnow().isoformat(),
            "total_pages": len(hashes)
        },
        "hashes": hashes
    }
    
    with open(hash_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Created {hash_file} with {len(hashes)} entries")

def main():
    """Recreate hash files for all scraped frameworks."""
    
    print("🔄 RECREATING HASH FILES FOR SCRAPED FRAMEWORKS")
    print("=" * 50)
    
    # Check which frameworks have been scraped
    documentation_dir = Path("documentation")
    if not documentation_dir.exists():
        print("❌ No documentation directory found")
        return
    
    # Get all framework directories
    frameworks = []
    for item in documentation_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            frameworks.append(item.name)
    
    print(f"📊 Found {len(frameworks)} framework directories")
    
    # Check which ones are missing hash files
    hash_dir = Path(".hashes")
    missing_hashes = []
    
    for framework in frameworks:
        hash_file = hash_dir / f"{framework}_hashes.json"
        if not hash_file.exists():
            missing_hashes.append(framework)
            print(f"  ❌ Missing hash file: {framework}")
        else:
            print(f"  ✅ Has hash file: {framework}")
    
    if not missing_hashes:
        print("\n✅ All frameworks have hash files!")
        return
    
    print(f"\n🔧 Need to create hash files for {len(missing_hashes)} frameworks:")
    for fw in missing_hashes:
        print(f"  - {fw}")
    
    # Create hash files
    print("\n🚀 Creating hash files...")
    for framework in missing_hashes:
        create_hash_file_for_framework(framework)
    
    print("\n✅ Done! All hash files have been created.")
    print("💡 The scraper will now properly track changes for incremental updates.")

if __name__ == "__main__":
    main()