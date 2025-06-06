#!/usr/bin/env python3
"""
Verify scraping results after completion:
1. Check that all frameworks have been scraped
2. Verify hash files exist for all frameworks
3. Randomly sample markdown files to check quality
"""

import asyncio
import json
import random
import sys
from pathlib import Path
from typing import List, Dict, Tuple

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / "scripts" / "utilities"))

from framework_list_scraper import AppleFrameworkListScraper

async def load_framework_list() -> List[Dict[str, str]]:
    """Load the framework list dynamically from Apple's API."""
    try:
        async with AppleFrameworkListScraper() as scraper:
            frameworks = await scraper.fetch_all_frameworks()
            return frameworks
    except Exception as e:
        print(f"❌ Error fetching framework list: {e}")
        return []

async def check_all_frameworks_scraped() -> Tuple[List[str], List[str]]:
    """Check which frameworks have been scraped."""
    documentation_dir = Path("documentation")
    scraped_frameworks = []
    missing_frameworks = []
    
    # Get expected frameworks
    frameworks = await load_framework_list()
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

def sample_markdown_files(num_samples: int = 5) -> List[Path]:
    """Randomly sample markdown files for quality check."""
    documentation_dir = Path("documentation")
    all_md_files = list(documentation_dir.rglob("*.md"))
    
    if not all_md_files:
        return []
    
    num_samples = min(num_samples, len(all_md_files))
    return random.sample(all_md_files, num_samples)

def check_markdown_quality(md_file: Path) -> Dict[str, bool]:
    """Basic quality checks for a markdown file."""
    try:
        content = md_file.read_text(encoding='utf-8')
        
        checks = {
            'has_title': content.startswith('# '),
            'has_framework': '**Framework**:' in content,
            'has_availability': '**Availability**:' in content or '**Platform**:' in content,
            'has_content': len(content) > 200,
            'has_source_link': 'developer.apple.com' in content,
            'has_code_block': '```' in content,
        }
        
        return checks
    except Exception as e:
        print(f"❌ Error reading {md_file}: {e}")
        return {}

async def main():
    print("🔍 VERIFYING APPLE DOCUMENTATION SCRAPING RESULTS")
    print("=" * 60)
    
    # Check all frameworks
    scraped, missing = await check_all_frameworks_scraped()
    
    print(f"\n✅ Scraped Frameworks: {len(scraped)}")
    if scraped:
        for i, fw in enumerate(scraped[:10]):
            print(f"   - {fw}")
        if len(scraped) > 10:
            print(f"   ... and {len(scraped) - 10} more")
    
    if missing:
        print(f"\n❌ Missing Frameworks: {len(missing)}")
        for fw in missing[:10]:
            print(f"   - {fw}")
        if len(missing) > 10:
            print(f"   ... and {len(missing) - 10} more")
    
    # Check hash files
    total_hashes, valid_hashes = check_hash_files()
    print(f"\n📁 Hash Files: {valid_hashes}/{total_hashes} valid")
    
    # Count total markdown files
    documentation_dir = Path("documentation")
    total_md_files = len(list(documentation_dir.rglob("*.md")))
    print(f"\n📄 Total Markdown Files: {total_md_files:,}")
    
    # Sample quality check
    print("\n🔬 Sample Quality Check:")
    samples = sample_markdown_files(5)
    
    for sample in samples:
        rel_path = sample.relative_to(documentation_dir)
        checks = check_markdown_quality(sample)
        
        if all(checks.values()):
            print(f"   ✅ {rel_path}")
        else:
            print(f"   ⚠️  {rel_path}")
            for check, passed in checks.items():
                if not passed:
                    print(f"      - Missing: {check}")
    
    # Summary
    print("\n" + "=" * 60)
    success_rate = len(scraped) / (len(scraped) + len(missing)) * 100 if (scraped or missing) else 0
    print(f"📊 SUMMARY: {success_rate:.1f}% frameworks scraped ({len(scraped)}/{len(scraped) + len(missing)})")
    
    if missing:
        print("\n💡 To scrape missing frameworks, run:")
        print("   python3 scrape.py --yes")

if __name__ == "__main__":
    asyncio.run(main())