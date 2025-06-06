#!/usr/bin/env python3
"""
Verify scraping results after completion:
1. Check that all frameworks have been scraped
2. Verify hash files exist for all frameworks
3. Randomly sample markdown files to check quality
"""

import json
import random
from pathlib import Path
from typing import List, Dict, Tuple

def load_framework_list() -> List[Dict[str, str]]:
    """Load the complete framework list."""
    framework_file = Path("data/complete_frameworks_list.json")
    if not framework_file.exists():
        # Try other locations
        framework_file = Path("complete_frameworks_list.json")
    
    if framework_file.exists():
        with open(framework_file, 'r') as f:
            data = json.load(f)
            return data.get('frameworks', [])
    else:
        print("❌ Could not find framework list file")
        return []

def check_all_frameworks_scraped() -> Tuple[List[str], List[str]]:
    """Check which frameworks have been scraped."""
    documentation_dir = Path("documentation")
    scraped_frameworks = []
    missing_frameworks = []
    
    # Get expected frameworks
    frameworks = load_framework_list()
    if not frameworks:
        print("❌ No framework list found")
        return [], []
    
    print(f"📊 Checking {len(frameworks)} expected frameworks...")
    
    for fw in frameworks:
        fw_id = fw.get('id', '').lower()
        fw_name = fw.get('title', fw_id)
        
        # Check if documentation directory exists
        fw_dir = documentation_dir / fw_id
        if fw_dir.exists():
            md_files = list(fw_dir.rglob("*.md"))
            if md_files:
                scraped_frameworks.append(f"{fw_name} ({fw_id}): {len(md_files)} files")
            else:
                missing_frameworks.append(f"{fw_name} ({fw_id}): directory exists but empty")
        else:
            missing_frameworks.append(f"{fw_name} ({fw_id})")
    
    return scraped_frameworks, missing_frameworks

def check_hash_files() -> Tuple[int, int]:
    """Check hash files for all frameworks."""
    hash_dir = Path(".hashes")
    if not hash_dir.exists():
        print("❌ No .hashes directory found")
        return 0, 0
    
    hash_files = list(hash_dir.glob("*_hashes.json"))
    valid_hashes = 0
    
    for hash_file in hash_files:
        try:
            with open(hash_file, 'r') as f:
                data = json.load(f)
                if 'hashes' in data and len(data['hashes']) > 0:
                    valid_hashes += 1
        except:
            pass
    
    return len(hash_files), valid_hashes

def sample_markdown_files(count: int = 10) -> List[Tuple[Path, str]]:
    """Randomly sample markdown files and check their content."""
    documentation_dir = Path("documentation")
    all_md_files = list(documentation_dir.rglob("*.md"))
    
    if not all_md_files:
        return []
    
    # Sample random files
    sample_size = min(count, len(all_md_files))
    sampled_files = random.sample(all_md_files, sample_size)
    
    results = []
    for md_file in sampled_files:
        try:
            content = md_file.read_text()
            # Check for key elements
            has_framework = "**Framework**:" in content
            has_declaration = "## Declaration" in content or "```" in content
            has_apple_link = "View on Apple Developer" in content
            has_cross_ref = "../" in content  # Cross-framework references
            
            quality = []
            if has_framework:
                quality.append("✓ Framework")
            if has_declaration:
                quality.append("✓ Code")
            if has_apple_link:
                quality.append("✓ Link")
            if has_cross_ref:
                quality.append("✓ Cross-refs")
            
            try:
                relative_path = md_file.relative_to(documentation_dir.parent)
            except:
                relative_path = md_file
            results.append((relative_path, " | ".join(quality) if quality else "❌ Missing content"))
        except Exception as e:
            results.append((md_file, f"❌ Error: {e}"))
    
    return results

def main():
    """Run all verification checks."""
    print("🔍 VERIFYING APPLE DOCUMENTATION SCRAPING RESULTS")
    print("=" * 60)
    
    # Check frameworks
    scraped, missing = check_all_frameworks_scraped()
    
    print(f"\n✅ Scraped Frameworks: {len(scraped)}")
    if len(scraped) <= 20:
        for fw in scraped:
            print(f"   - {fw}")
    else:
        for fw in scraped[:10]:
            print(f"   - {fw}")
        print(f"   ... and {len(scraped) - 10} more")
    
    if missing:
        print(f"\n❌ Missing Frameworks: {len(missing)}")
        for fw in missing[:10]:
            print(f"   - {fw}")
        if len(missing) > 10:
            print(f"   ... and {len(missing) - 10} more")
    
    # Check hash files
    total_hash, valid_hash = check_hash_files()
    print(f"\n📁 Hash Files: {valid_hash}/{total_hash} valid")
    
    # Calculate total files
    doc_dir = Path("documentation")
    total_md_files = len(list(doc_dir.rglob("*.md"))) if doc_dir.exists() else 0
    print(f"\n📄 Total Markdown Files: {total_md_files:,}")
    
    # Sample random files
    print("\n🎲 Random Sample of Markdown Files:")
    samples = sample_markdown_files(10)
    for file_path, quality in samples:
        print(f"   - {file_path}: {quality}")
    
    # Summary
    print("\n📊 SUMMARY:")
    print(f"   - Frameworks scraped: {len(scraped)}/{len(scraped) + len(missing)}")
    print(f"   - Total files: {total_md_files:,}")
    print(f"   - Hash files: {valid_hash}")
    
    completion_rate = (len(scraped) / (len(scraped) + len(missing)) * 100) if (scraped or missing) else 0
    print(f"   - Completion: {completion_rate:.1f}%")
    
    if completion_rate == 100:
        print("\n🎉 ALL FRAMEWORKS SUCCESSFULLY SCRAPED!")
    else:
        print(f"\n⏳ Scraping in progress... {len(missing)} frameworks remaining")

if __name__ == "__main__":
    main()