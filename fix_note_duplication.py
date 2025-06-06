#!/usr/bin/env python3
"""
Fix Note duplication in existing markdown files by re-scraping only affected files.
"""

import asyncio
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper

def has_note_duplication(file_path: Path) -> bool:
    """Check if a markdown file has the Note duplication issue."""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Look for blockquote notes followed by duplicated content
        # Pattern: > **Note**: <content> followed by the same <content> without blockquote
        
        # Find all blockquote notes/warnings/tips/important
        blockquote_pattern = r'> \*\*(?:Note|Warning|Important|Tip)\*\*:\s*(.+?)(?=\n\n|\n[>#]|\Z)'
        matches = list(re.finditer(blockquote_pattern, content, re.DOTALL))
        
        for match in matches:
            # Get the content after the Note:
            note_content = match.group(1).strip()
            
            # Check if this exact content appears again after the blockquote
            # (within the next few lines, not counting other blockquotes)
            end_pos = match.end()
            next_section = content[end_pos:end_pos + len(note_content) + 50]
            
            # Remove any leading whitespace/newlines
            next_section = next_section.lstrip()
            
            # Check if it starts with the same content (not as a blockquote)
            if next_section.startswith(note_content) and not next_section.startswith('>'):
                return True
        
        return False
        
    except Exception as e:
        print(f"Error checking {file_path}: {e}")
        return False

async def rescrape_file(file_path: Path) -> bool:
    """Re-scrape a single file based on its path."""
    try:
        # Extract framework and URL from file path
        # Path structure: documentation/<framework>/<path>/<file>.md
        parts = file_path.relative_to(Path('documentation')).parts
        if not parts:
            return False
        
        framework_id = parts[0]
        
        # Reconstruct the documentation URL
        # Remove .md extension and construct URL
        url_parts = list(parts)
        url_parts[-1] = url_parts[-1].replace('.md', '')
        doc_url = f"https://developer.apple.com/documentation/{'/'.join(url_parts)}"
        
        print(f"  Re-scraping: {doc_url}")
        
        # Create scraper for this framework
        async with AppleJSONDocumentationScraper(framework_id) as scraper:
            # Force re-scrape by clearing hash
            json_url = scraper._convert_doc_url_to_json_url(doc_url)
            if doc_url in scraper.hash_manager.hashes:
                del scraper.hash_manager.hashes[doc_url]
            if json_url in scraper.hash_manager.hashes:
                del scraper.hash_manager.hashes[json_url]
            
            # Scrape the page
            data = await scraper.scrape_page(doc_url)
            
            if data:
                # Save the fixed content
                await scraper.save_page_data(doc_url, data)
                return True
            else:
                print(f"  ❌ Failed to scrape: {doc_url}")
                return False
                
    except Exception as e:
        print(f"  ❌ Error re-scraping {file_path}: {e}")
        return False

async def fix_note_duplications():
    """Find and fix all files with Note duplication."""
    print("🔍 Scanning for files with Note duplication...")
    print("=" * 80)
    
    # Find all markdown files
    documentation_dir = Path('documentation')
    all_md_files = list(documentation_dir.rglob('*.md'))
    print(f"Total markdown files: {len(all_md_files)}")
    
    # Check each file for duplication
    affected_files = []
    
    # Process in batches to show progress
    batch_size = 1000
    for i in range(0, len(all_md_files), batch_size):
        batch = all_md_files[i:i + batch_size]
        for file_path in batch:
            if has_note_duplication(file_path):
                affected_files.append(file_path)
        print(f"  Checked {min(i + batch_size, len(all_md_files))}/{len(all_md_files)} files... Found {len(affected_files)} affected")
    
    print(f"\n📊 Found {len(affected_files)} files with Note duplication")
    
    if not affected_files:
        print("✅ No files need fixing!")
        return
    
    # Confirm before proceeding
    print("\nAffected files will be re-scraped to fix the duplication.")
    response = input("Continue? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        return
    
    # Process files
    print(f"\n♻️  Re-scraping {len(affected_files)} files...")
    print("=" * 80)
    
    # Process in smaller batches to avoid overwhelming the API
    success_count = 0
    failed_count = 0
    batch_size = 10  # Smaller batches for API calls
    
    for i in range(0, len(affected_files), batch_size):
        batch = affected_files[i:i + batch_size]
        print(f"\nProcessing batch {i//batch_size + 1}/{(len(affected_files) + batch_size - 1)//batch_size}")
        
        # Process files in batch concurrently
        tasks = [rescrape_file(file_path) for file_path in batch]
        results = await asyncio.gather(*tasks)
        
        # Count results
        for success in results:
            if success:
                success_count += 1
            else:
                failed_count += 1
        
        # Small delay between batches
        if i + batch_size < len(affected_files):
            await asyncio.sleep(1)
    
    # Final report
    print("\n" + "=" * 80)
    print("🎉 DUPLICATION FIX COMPLETE!")
    print(f"✅ Successfully fixed: {success_count} files")
    if failed_count > 0:
        print(f"❌ Failed: {failed_count} files")
    
    # Verify a sample
    if affected_files and success_count > 0:
        print("\n🔍 Verifying a sample file...")
        sample_file = affected_files[0]
        if has_note_duplication(sample_file):
            print(f"  ❌ {sample_file.name} still has duplication")
        else:
            print(f"  ✅ {sample_file.name} is fixed!")

if __name__ == "__main__":
    asyncio.run(fix_note_duplications())