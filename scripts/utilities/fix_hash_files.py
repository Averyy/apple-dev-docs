#!/usr/bin/env python3
"""
Fix hash files to match the correct format with ETags and proper field names.
This ensures incremental updates work efficiently with HTTP 304 responses.
"""

import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

def fix_hash_file(framework_id: str):
    """Fix a hash file to match the correct format."""
    
    hash_file = Path(f".hashes/{framework_id}_hashes.json")
    if not hash_file.exists():
        print(f"❌ Hash file not found: {hash_file}")
        return
    
    # Load existing hash file
    with open(hash_file, 'r') as f:
        data = json.load(f)
    
    hashes = data.get("hashes", {})
    original_count = len(hashes)
    
    # Check if it needs fixing
    needs_fixing = False
    for url, entry in hashes.items():
        if "last_modified" in entry or "etag" not in entry:
            needs_fixing = True
            break
    
    if not needs_fixing:
        print(f"✅ {framework_id} hash file is already in correct format")
        return
    
    print(f"🔧 Fixing {framework_id} hash file ({original_count} entries)...")
    
    # Fix each entry
    fixed_hashes = {}
    for url, entry in hashes.items():
        # Convert to correct format
        fixed_entry = {
            "hash": entry.get("hash"),
            "last_checked": entry.get("last_checked") or entry.get("last_modified") or datetime.now(timezone.utc).isoformat(),
            "status": entry.get("status", "unchanged")  # Mark as unchanged since we have the content
        }
        
        # We don't have ETags for recreated entries, but that's OK
        # The scraper will get them on the next run
        if "etag" in entry:
            fixed_entry["etag"] = entry["etag"]
        
        # Convert documentation URLs to JSON URLs for proper tracking
        if "/documentation/" in url and not url.endswith(".json"):
            # This is a doc URL, we also need the JSON URL entry
            json_url = url.replace("https://developer.apple.com/documentation/", 
                                 "https://developer.apple.com/tutorials/data/documentation/")
            json_url = json_url.replace(framework_id, framework_id.lower())
            if not json_url.endswith(".json"):
                json_url += ".json"
            
            # Add both URLs
            fixed_hashes[url] = fixed_entry
            fixed_hashes[json_url] = fixed_entry.copy()  # Same hash for JSON endpoint
        else:
            fixed_hashes[url] = fixed_entry
    
    # Update the data
    data["hashes"] = fixed_hashes
    data["metadata"]["total_pages"] = len(fixed_hashes)
    data["metadata"]["last_updated"] = datetime.now(timezone.utc).isoformat()
    
    # Save the fixed file
    with open(hash_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Fixed {framework_id}: {original_count} → {len(fixed_hashes)} entries")

def main():
    """Fix all hash files to match the correct format."""
    
    print("🔧 FIXING HASH FILES TO CORRECT FORMAT")
    print("=" * 50)
    
    # Get all hash files
    hash_dir = Path(".hashes")
    if not hash_dir.exists():
        print("❌ No .hashes directory found")
        return
    
    hash_files = list(hash_dir.glob("*_hashes.json"))
    print(f"📊 Found {len(hash_files)} hash files to check")
    
    # Fix each one
    for hash_file in hash_files:
        framework_id = hash_file.stem.replace("_hashes", "")
        fix_hash_file(framework_id)
    
    print("\n✅ Done! All hash files have been checked and fixed.")
    print("💡 Note: ETags will be populated on the next scraper run for entries that don't have them.")

if __name__ == "__main__":
    main()