#!/usr/bin/env python3
"""Fix incomplete frameworks by updating their progress files"""

from pathlib import Path

def fix_incomplete_frameworks():
    """Update progress files for frameworks that completed but show as incomplete"""
    
    incomplete_frameworks = [
        ("ActivityKit", 222, 1, 0),
        ("AddressBook", 51, 1, 0),
        ("AddressBookUI", 8, 0, 0)
    ]
    
    print("🔧 Fixing incomplete framework progress files")
    print()
    
    for framework, scraped, skipped, failed in incomplete_frameworks:
        progress_file = Path(f"documentation/{framework}/scraping_progress.txt")
        
        if progress_file.exists():
            # Read current content
            current_content = progress_file.read_text()
            
            if "Completed scraping" not in current_content:
                # Update with completion status
                new_content = f"""Completed scraping {framework}!
Total pages scraped: {scraped}
Pages skipped (unchanged): {skipped}
Pages failed: {failed}
"""
                progress_file.write_text(new_content)
                print(f"✓ Fixed {framework} - marked as completed with {scraped} pages")
            else:
                print(f"✓ {framework} - already marked as completed")
        else:
            print(f"⚠️  {framework} - no progress file found")
    
    print("\n✅ Done! Run check_scraping_status.py to verify the fix.")

if __name__ == "__main__":
    fix_incomplete_frameworks()