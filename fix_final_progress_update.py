#!/usr/bin/env python3
"""
Fix for the final progress update issue in json_scraper.py
This ensures the completion status is always written
"""

import sys
from pathlib import Path

def apply_fix():
    """Apply the fix to json_scraper.py"""
    
    scraper_file = Path("scraper/json_scraper.py")
    if not scraper_file.exists():
        print("❌ scraper/json_scraper.py not found!")
        return False
    
    content = scraper_file.read_text()
    
    # Find the discover_and_scrape_streaming method
    method_start = content.find("async def discover_and_scrape_streaming(self):")
    if method_start == -1:
        print("❌ Could not find discover_and_scrape_streaming method!")
        return False
    
    # Find where we need to add the fix
    # Look for the line after "await self._discover_and_scrape_from_json(framework_json_url, progress_file)"
    search_line = "await self._discover_and_scrape_from_json(framework_json_url, progress_file)"
    insert_pos = content.find(search_line, method_start)
    if insert_pos == -1:
        print("❌ Could not find the target line!")
        return False
    
    # Find the end of this line
    line_end = content.find('\n', insert_pos)
    
    # Check if the fix is already applied
    if "Final progress update" in content[line_end:line_end + 200]:
        print("✓ Fix already applied!")
        return True
    
    # Insert the fix
    fix_code = """
        
        # Final progress update - ensure completion status is written
        logger.info(
            "scraping_complete",
            framework=self.framework_name,
            pages_scraped=self.stats['pages_scraped'],
            pages_skipped=self.stats['pages_skipped'],
            pages_failed=self.stats['pages_failed']
        )"""
    
    # Apply the fix
    new_content = content[:line_end] + fix_code + content[line_end:]
    
    # Backup the original
    backup_file = scraper_file.with_suffix('.py.backup')
    scraper_file.rename(backup_file)
    print(f"✓ Created backup: {backup_file}")
    
    # Write the fixed version
    scraper_file.write_text(new_content)
    print(f"✓ Applied fix to: {scraper_file}")
    
    return True

def create_fixed_version():
    """Create a complete fixed version of the discover_and_scrape_streaming method"""
    
    fixed_method = '''
    async def discover_and_scrape_streaming(self):
        """Discover URLs and scrape them immediately for real-time feedback."""
        logger.info("starting_streaming_discovery_and_scrape", framework=self.framework_name)
        
        # Create progress file immediately
        progress_file = self.output_dir / "scraping_progress.txt" 
        progress_file.parent.mkdir(parents=True, exist_ok=True)
        progress_file.write_text(f"Starting {self.framework_name} streaming scrape...\\n")
        
        # Start with the framework's main JSON file
        framework_json_url = f"{self.JSON_BASE_URL}/{self.framework_id}.json"
        
        # Extract topic hierarchy from main framework page
        await self._extract_topic_hierarchy(framework_json_url)
        
        # Scrape the main framework page first
        main_doc_url = f"https://developer.apple.com/documentation/{self.framework_id}"
        progress_file.write_text(f"Scraping main page: {main_doc_url}\\n")
        await self._scrape_and_save_url(main_doc_url)
        
        # Start discovery and scrape as we go
        # Force processing of main framework JSON even if already seen
        if framework_json_url in self.processed_urls:
            self.processed_urls.remove(framework_json_url)
        
        try:
            await self._discover_and_scrape_from_json(framework_json_url, progress_file)
        finally:
            # CRITICAL FIX: Always update progress file with final status
            self._update_progress_file(progress_file, "COMPLETED", final=True)
            logger.info(
                "scraping_complete",
                framework=self.framework_name,
                pages_scraped=self.stats['pages_scraped'],
                pages_skipped=self.stats['pages_skipped'],
                pages_failed=self.stats['pages_failed']
            )
'''
    
    print("\nFixed discover_and_scrape_streaming method:")
    print("=" * 60)
    print(fixed_method)
    print("=" * 60)
    
    # Save the fixed method to a file
    with open("fixed_discover_and_scrape_streaming.txt", "w") as f:
        f.write(fixed_method)
    print("\n✓ Fixed method saved to: fixed_discover_and_scrape_streaming.txt")

if __name__ == "__main__":
    print("🔧 Applying fix for final progress update issue")
    print()
    
    # Create the fixed version for reference
    create_fixed_version()
    
    # Option to apply the fix
    response = input("\nApply this fix to scraper/json_scraper.py? (y/N): ")
    if response.lower() == 'y':
        if apply_fix():
            print("\n✅ Fix applied successfully!")
            print("\nYou can now re-run the scraper and it should properly complete.")
        else:
            print("\n❌ Failed to apply fix automatically.")
            print("Please apply the fix manually using the code in fixed_discover_and_scrape_streaming.txt")
    else:
        print("\n📄 Fix not applied. You can apply it manually using fixed_discover_and_scrape_streaming.txt")