#!/usr/bin/env python3
"""
Fast version: Fix Note duplication by identifying affected files more efficiently.
"""

import asyncio
import json
import re
import sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper

def check_file_for_duplication(file_path):
    """Check a single file for duplication (can run in parallel)."""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Quick check: if no blockquote notes, skip
        if '> **Note**:' not in content and '> **Warning**:' not in content and '> **Important**:' not in content and '> **Tip**:' not in content:
            return None
        
        # More detailed check for actual duplication
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('> **Note**:') or line.startswith('> **Warning**:') or line.startswith('> **Important**:') or line.startswith('> **Tip**:'):
                # Extract the note content
                note_content = line[line.index(':') + 1:].strip()
                
                # Check if the next non-empty line has the same content (without blockquote)
                for j in range(i + 1, min(i + 5, len(lines))):
                    next_line = lines[j].strip()
                    if next_line and not next_line.startswith('>'):
                        # Check if this line starts with the note content
                        if next_line.startswith(note_content[:50]):  # Check first 50 chars
                            return str(file_path)
                        break
        
        return None
        
    except Exception as e:
        print(f"Error checking {file_path}: {e}")
        return None

async def rescrape_files(file_paths):
    """Re-scrape a list of files."""
    # Group files by framework
    framework_files = {}
    for file_path in file_paths:
        parts = Path(file_path).relative_to(Path('documentation')).parts
        if parts:
            framework_id = parts[0]
            if framework_id not in framework_files:
                framework_files[framework_id] = []
            framework_files[framework_id].append(file_path)
    
    success_count = 0
    failed_count = 0
    
    # Process each framework
    for framework_id, files in framework_files.items():
        print(f"\n📦 Processing {framework_id} ({len(files)} files)...")
        
        async with AppleJSONDocumentationScraper(framework_id) as scraper:
            for file_path in files:
                try:
                    # Reconstruct URL
                    parts = Path(file_path).relative_to(Path('documentation')).parts
                    url_parts = list(parts)
                    url_parts[-1] = url_parts[-1].replace('.md', '')
                    doc_url = f"https://developer.apple.com/documentation/{'/'.join(url_parts)}"
                    
                    # Clear hash to force re-scrape
                    json_url = scraper._convert_doc_url_to_json_url(doc_url)
                    if doc_url in scraper.hash_manager.hashes:
                        del scraper.hash_manager.hashes[doc_url]
                    if json_url in scraper.hash_manager.hashes:
                        del scraper.hash_manager.hashes[json_url]
                    
                    # Scrape
                    data = await scraper.scrape_page(doc_url)
                    
                    if data:
                        await scraper.save_page_data(doc_url, data)
                        success_count += 1
                        print(f"  ✅ Fixed: {Path(file_path).name}")
                    else:
                        failed_count += 1
                        print(f"  ❌ Failed: {Path(file_path).name}")
                        
                except Exception as e:
                    failed_count += 1
                    print(f"  ❌ Error: {Path(file_path).name} - {e}")
                
                # Small delay between files
                await asyncio.sleep(0.2)
    
    return success_count, failed_count

async def main():
    """Main function to find and fix duplications."""
    print("🔍 Fast scan for Note duplication...")
    print("=" * 80)
    
    # Find all markdown files
    documentation_dir = Path('documentation')
    all_md_files = list(documentation_dir.rglob('*.md'))
    print(f"Total markdown files: {len(all_md_files)}")
    
    # Use multiprocessing to check files in parallel
    print("\n⚡ Scanning files in parallel...")
    cpu_count = multiprocessing.cpu_count()
    affected_files = []
    
    with ProcessPoolExecutor(max_workers=cpu_count) as executor:
        # Submit all files for checking
        future_to_file = {executor.submit(check_file_for_duplication, f): f for f in all_md_files}
        
        # Process results as they complete
        completed = 0
        for future in as_completed(future_to_file):
            completed += 1
            if completed % 1000 == 0:
                print(f"  Scanned {completed}/{len(all_md_files)} files...")
            
            result = future.result()
            if result:
                affected_files.append(result)
    
    print(f"\n📊 Found {len(affected_files)} files with Note duplication")
    
    if not affected_files:
        print("✅ No files need fixing!")
        return
    
    # Show some examples
    print("\nExample affected files:")
    for i, file_path in enumerate(affected_files[:5]):
        print(f"  - {Path(file_path).relative_to(documentation_dir)}")
    if len(affected_files) > 5:
        print(f"  ... and {len(affected_files) - 5} more")
    
    # Confirm
    print(f"\n⚠️  This will re-scrape {len(affected_files)} files to fix the duplication.")
    response = input("Continue? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        return
    
    # Re-scrape affected files
    print(f"\n♻️  Re-scraping {len(affected_files)} files...")
    print("=" * 80)
    
    success_count, failed_count = await rescrape_files(affected_files)
    
    # Final report
    print("\n" + "=" * 80)
    print("🎉 DUPLICATION FIX COMPLETE!")
    print(f"✅ Successfully fixed: {success_count} files")
    if failed_count > 0:
        print(f"❌ Failed: {failed_count} files")
    
    # Save list of affected files for reference
    output_file = Path('note_duplication_fix_results.json')
    results = {
        'total_affected': len(affected_files),
        'success_count': success_count,
        'failed_count': failed_count,
        'affected_files': affected_files
    }
    output_file.write_text(json.dumps(results, indent=2))
    print(f"\n📄 Results saved to: {output_file}")

if __name__ == "__main__":
    asyncio.run(main())