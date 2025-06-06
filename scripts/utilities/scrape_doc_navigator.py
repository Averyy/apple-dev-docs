#!/usr/bin/env python3
"""
Scrape Apple's Documentation Navigator to extract all framework links.
Specifically targets aria-label="Documentation Navigator" and finds all href="/documentation/*" links.
"""

import asyncio
import json
import re
from typing import Set, Dict, List
from playwright.async_api import async_playwright
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

class DocumentationNavigatorScraper:
    """Scrape Apple's Documentation Navigator for all framework links."""
    
    def __init__(self):
        self.framework_links = []
        
    async def scrape_navigation_links(self) -> List[Dict[str, str]]:
        """Extract all documentation links from the Documentation Navigator."""
        links = []
        
        try:
            async with async_playwright() as p:
                # Launch browser
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                
                # Navigate to Apple documentation
                print("Loading Apple documentation page...")
                await page.goto("https://developer.apple.com/documentation/")
                
                # Wait for the page to load completely
                await page.wait_for_load_state("networkidle")
                print("Page loaded successfully")
                
                # Find the Documentation Navigator
                nav_selector = '[aria-label="Documentation Navigator"]'
                
                try:
                    navigator = await page.wait_for_selector(nav_selector, timeout=15000)
                    if navigator:
                        print("✅ Found Documentation Navigator")
                        
                        # First, expand any collapsed sections
                        expandable_buttons = await navigator.query_selector_all('button[aria-expanded="false"]')
                        print(f"Found {len(expandable_buttons)} collapsed sections to expand")
                        
                        for i, button in enumerate(expandable_buttons):
                            try:
                                print(f"Expanding section {i+1}/{len(expandable_buttons)}")
                                await button.click()
                                await page.wait_for_timeout(500)  # Wait for expansion
                            except Exception as e:
                                logger.debug(f"Could not expand section {i+1}: {e}")
                        
                        # Wait a bit more for all expansions to complete
                        await page.wait_for_timeout(2000)
                        
                        # Now get ALL links with documentation hrefs
                        all_doc_links = await navigator.query_selector_all('a[href*="/documentation/"]')
                        print(f"Found {len(all_doc_links)} documentation links total")
                        
                        for link in all_doc_links:
                            try:
                                href = await link.get_attribute('href')
                                text = await link.text_content()
                                
                                if href and '/documentation/' in href:
                                    # Clean up the href
                                    if href.startswith('/'):
                                        href = f"https://developer.apple.com{href}"
                                    
                                    # Extract framework ID from URL
                                    url_parts = href.split('/documentation/')
                                    if len(url_parts) > 1:
                                        framework_path = url_parts[1].split('/')[0].split('?')[0]
                                        
                                        if framework_path and framework_path != 'technologies':
                                            link_info = {
                                                'framework_id': framework_path,
                                                'title': text.strip() if text else framework_path,
                                                'url': href,
                                                'href_path': href.split('developer.apple.com')[-1] if 'developer.apple.com' in href else href
                                            }
                                            links.append(link_info)
                                            
                            except Exception as e:
                                logger.debug(f"Error processing link: {e}")
                        
                        print(f"✅ Extracted {len(links)} unique documentation links")
                        
                    else:
                        print("❌ Documentation Navigator not found")
                        
                except Exception as e:
                    print(f"❌ Error finding Documentation Navigator: {e}")
                
                await browser.close()
                
        except Exception as e:
            print(f"❌ Browser scraping failed: {e}")
            print("Make sure to install Playwright browsers: playwright install chromium")
            
        return links
    
    def analyze_links(self, links: List[Dict[str, str]]) -> Dict:
        """Analyze the extracted links and organize them."""
        
        # Remove duplicates by framework_id
        unique_frameworks = {}
        for link in links:
            framework_id = link['framework_id']
            if framework_id not in unique_frameworks:
                unique_frameworks[framework_id] = link
            # Keep the one with the cleanest title (shortest, most descriptive)
            elif len(link['title']) < len(unique_frameworks[framework_id]['title']):
                unique_frameworks[framework_id] = link
        
        unique_links = list(unique_frameworks.values())
        
        # Sort by framework_id for easier reading
        unique_links.sort(key=lambda x: x['framework_id'].lower())
        
        # Extract just the framework IDs and titles
        framework_ids = [link['framework_id'] for link in unique_links]
        framework_titles = [link['title'] for link in unique_links]
        
        analysis = {
            'total_unique_frameworks': len(unique_links),
            'framework_ids': framework_ids,
            'framework_titles': framework_titles,
            'detailed_links': unique_links,
            'sample_links': unique_links[:10]  # First 10 for display
        }
        
        return analysis

async def main():
    print("Apple Documentation Navigator Scraper")
    print("=" * 60)
    print("Extracting all href='/documentation/*' links from Documentation Navigator...")
    print()
    
    scraper = DocumentationNavigatorScraper()
    
    # Scrape the navigation links
    links = await scraper.scrape_navigation_links()
    
    if links:
        # Analyze the results
        analysis = scraper.analyze_links(links)
        
        print("RESULTS:")
        print("=" * 60)
        print(f"Total unique frameworks: {analysis['total_unique_frameworks']}")
        print()
        
        print("Sample frameworks found:")
        print("-" * 30)
        for link in analysis['sample_links']:
            print(f"  {link['framework_id']:20} - {link['title']}")
        
        if len(analysis['detailed_links']) > 10:
            print(f"  ... and {len(analysis['detailed_links']) - 10} more")
        
        print()
        print("All framework IDs:")
        print("-" * 30)
        # Print in columns for better readability
        ids = analysis['framework_ids']
        for i in range(0, len(ids), 4):
            row = ids[i:i+4]
            print("  " + "  ".join(f"{fw:20}" for fw in row))
        
        # Save detailed results
        output_file = "documentation_navigator_frameworks.json"
        with open(output_file, "w") as f:
            json.dump({
                "extraction_summary": analysis,
                "timestamp": "2025-06-04",
                "source": "Apple Documentation Navigator (aria-label='Documentation Navigator')",
                "method": "Playwright browser automation"
            }, f, indent=2)
        
        print(f"\nDetailed results saved to: {output_file}")
        
        # Compare with known frameworks
        known_frameworks = [
            'foundation', 'swiftui', 'uikit', 'watchkit', 'metal', 'coredata', 
            'arkit', 'coreml', 'vision', 'webkit', 'combine', 'swift'
        ]
        
        found_known = []
        for known in known_frameworks:
            if known in analysis['framework_ids']:
                found_known.append(known)
        
        print(f"\nKnown frameworks found: {len(found_known)}/{len(known_frameworks)}")
        print(f"Found: {', '.join(found_known)}")
        
        missing = [fw for fw in known_frameworks if fw not in analysis['framework_ids']]
        if missing:
            print(f"Missing: {', '.join(missing)}")
        
    else:
        print("❌ No links found. This could mean:")
        print("1. Playwright browsers not installed: playwright install chromium")
        print("2. Apple changed their documentation structure")
        print("3. Network/loading issues")

if __name__ == "__main__":
    asyncio.run(main())