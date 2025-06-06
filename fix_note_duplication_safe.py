#!/usr/bin/env python3
"""
SAFE version: Fix Note duplication by reading actual URLs from markdown files.
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
    """Check a single file for duplication and extract its URL."""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Quick check: if no blockquote notes, skip
        if '> **Note**:' not in content and '> **Warning**:' not in content and '> **Important**:' not in content and '> **Tip**:' not in content:
            return None
        
        # Check for actual duplication
        lines = content.split('\n')
        has_duplication = False
        
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
                            has_duplication = True
                            break
                        break
        
        if not has_duplication:
            return None
        
        # Extract the actual URL from the bottom of the file
        # Look for the last occurrence of the Apple Developer URL pattern
        # This handles URLs with parentheses like requestreview()
        lines = content.split('\n')
        for line in reversed(lines):
            if '*[View on Apple Developer](' in line and line.endswith(')*'):
                # Extract URL between ]( and )*
                start = line.find('](') + 2
                end = line.rfind(')*')
                if start > 1 and end > start:
                    url = line[start:end]
                    if url.startswith('https://developer.apple.com/documentation/'):
                        return {
                            'file': str(file_path),
                            'url': url
                        }
        
        print(f"WARNING: No URL found in {file_path}")
        return None
        
    except Exception as e:
        print(f"Error checking {file_path}: {e}")
        return None

async def rescrape_files_safe(affected_files_data):
    """Re-scrape files using their actual URLs."""
    # Group files by framework
    framework_files = {}
    for file_data in affected_files_data:
        file_path = Path(file_data['file'])
        url = file_data['url']
        
        # Extract framework from URL
        url_parts = url.replace('https://developer.apple.com/documentation/', '').split('/')
        if url_parts:
            framework_id = url_parts[0]
            if framework_id not in framework_files:
                framework_files[framework_id] = []
            framework_files[framework_id].append(file_data)
    
    success_count = 0
    failed_count = 0
    
    # Process each framework
    for framework_id, files_data in framework_files.items():
        print(f"\n📦 Processing {framework_id} ({len(files_data)} files)...")
        
        try:
            async with AppleJSONDocumentationScraper(framework_id) as scraper:
                for file_data in files_data:
                    file_path = Path(file_data['file'])
                    doc_url = file_data['url']
                    
                    try:
                        print(f"  Re-scraping: {file_path.name} -> {doc_url}")
                        
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
                            print(f"    ✅ Fixed: {file_path.name}")
                        else:
                            failed_count += 1
                            print(f"    ❌ Failed: {file_path.name}")
                            
                    except Exception as e:
                        failed_count += 1
                        print(f"    ❌ Error: {file_path.name} - {e}")
                    
                    # Small delay between files
                    await asyncio.sleep(0.2)
                    
        except Exception as e:
            print(f"  ❌ Framework error for {framework_id}: {e}")
            failed_count += len(files_data)
    
    return success_count, failed_count

async def main():
    """Main function to find and fix duplications."""
    print("🔍 SAFE scan for Note duplication (reads URLs from files)...")
    print("=" * 80)
    
    # Find all markdown files
    documentation_dir = Path('documentation')
    all_md_files = list(documentation_dir.rglob('*.md'))
    print(f"Total markdown files: {len(all_md_files)}")
    
    # Use multiprocessing to check files in parallel
    print("\n⚡ Scanning files and extracting URLs...")
    cpu_count = multiprocessing.cpu_count()
    affected_files_data = []
    
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
                affected_files_data.append(result)
    
    print(f"\n📊 Found {len(affected_files_data)} files with Note duplication")
    
    if not affected_files_data:
        print("✅ No files need fixing!")
        return
    
    # Show some examples
    print("\nExample affected files with their URLs:")
    for i, file_data in enumerate(affected_files_data[:5]):
        file_path = Path(file_data['file']).relative_to(documentation_dir)
        url = file_data['url']
        print(f"  - {file_path}")
        print(f"    URL: {url}")
    if len(affected_files_data) > 5:
        print(f"  ... and {len(affected_files_data) - 5} more")
    
    # Save the list for safety
    backup_file = Path('note_duplication_files_backup.json')
    backup_file.write_text(json.dumps(affected_files_data, indent=2))
    print(f"\n💾 Backup saved to: {backup_file}")
    
    # Confirm
    print(f"\n⚠️  This will re-scrape {len(affected_files_data)} files to fix the duplication.")
    print("URLs will be read directly from each file to ensure accuracy.")
    response = input("Continue? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        return
    
    # Re-scrape affected files
    print(f"\n♻️  Re-scraping {len(affected_files_data)} files...")
    print("=" * 80)
    
    success_count, failed_count = await rescrape_files_safe(affected_files_data)
    
    # Final report
    print("\n" + "=" * 80)
    print("🎉 DUPLICATION FIX COMPLETE!")
    print(f"✅ Successfully fixed: {success_count} files")
    if failed_count > 0:
        print(f"❌ Failed: {failed_count} files")
    
    # Save results
    results = {
        'total_affected': len(affected_files_data),
        'success_count': success_count,
        'failed_count': failed_count,
        'affected_files': affected_files_data
    }
    results_file = Path('note_duplication_fix_results.json')
    results_file.write_text(json.dumps(results, indent=2))
    print(f"\n📄 Results saved to: {results_file}")

if __name__ == "__main__":
    asyncio.run(main())