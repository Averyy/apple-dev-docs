#!/usr/bin/env python3
"""
Scrape Apple's documentation menu using different approaches.
This will help us get the complete framework list automatically.
"""

import asyncio
import json
import re
from typing import Dict, List, Set
from playwright.async_api import async_playwright
import httpx
from bs4 import BeautifulSoup
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

class AppleMenuScraper:
    """Scrape Apple's documentation menu to get complete framework list."""
    
    def __init__(self):
        self.frameworks = set()
        
    async def scrape_with_playwright(self) -> Set[str]:
        """Use Playwright to scrape JavaScript-rendered menu."""
        frameworks = set()
        
        try:
            async with async_playwright() as p:
                # Launch browser
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                
                # Navigate to Apple documentation
                await page.goto("https://developer.apple.com/documentation/")
                
                # Wait for the page to load completely
                await page.wait_for_load_state("networkidle")
                
                # Look for framework links in the navigation/menu
                # Try different selectors that might contain framework links
                selectors_to_try = [
                    'a[href*="/documentation/"]',
                    '.nav-menu a[href*="/documentation/"]',
                    '.technology-grid a[href*="/documentation/"]',
                    '.category-links a[href*="/documentation/"]',
                    'nav a[href*="/documentation/"]',
                    '.frameworks-list a[href*="/documentation/"]'
                ]
                
                for selector in selectors_to_try:
                    try:
                        elements = await page.query_selector_all(selector)
                        logger.info(f"Found {len(elements)} elements with selector: {selector}")
                        
                        for element in elements:
                            href = await element.get_attribute('href')
                            text = await element.text_content()
                            
                            if href and '/documentation/' in href:
                                # Extract framework name from URL
                                framework_id = href.split('/documentation/')[-1].split('/')[0]
                                if framework_id and framework_id not in ['', 'technologies']:
                                    frameworks.add(framework_id)
                                
                                # Also try to get the display text
                                if text and text.strip():
                                    frameworks.add(text.strip())
                    
                    except Exception as e:
                        logger.debug(f"Selector {selector} failed: {e}")
                
                # Try to find any technology/framework menus that might be loaded dynamically
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await page.wait_for_timeout(2000)  # Wait for any lazy loading
                
                # Look for any dropdown menus or expanded sections
                dropdown_selectors = [
                    'button[aria-expanded="false"]',
                    '.dropdown-toggle',
                    '.menu-trigger'
                ]
                
                for selector in dropdown_selectors:
                    try:
                        buttons = await page.query_selector_all(selector)
                        for button in buttons[:5]:  # Limit to avoid too many clicks
                            await button.click()
                            await page.wait_for_timeout(1000)
                            
                            # Look for newly visible framework links
                            new_links = await page.query_selector_all('a[href*="/documentation/"]')
                            for link in new_links:
                                href = await link.get_attribute('href')
                                text = await link.text_content()
                                
                                if href and '/documentation/' in href:
                                    framework_id = href.split('/documentation/')[-1].split('/')[0]
                                    if framework_id and framework_id not in ['', 'technologies']:
                                        frameworks.add(framework_id)
                                    
                                    if text and text.strip():
                                        frameworks.add(text.strip())
                    
                    except Exception as e:
                        logger.debug(f"Dropdown interaction failed: {e}")
                
                # Get the final page content for additional parsing
                content = await page.content()
                
                # Parse with BeautifulSoup for additional extraction
                soup = BeautifulSoup(content, 'html.parser')
                
                # Look for any data attributes or JSON that might contain framework lists
                script_tags = soup.find_all('script')
                for script in script_tags:
                    if script.string:
                        # Look for JSON data containing documentation links
                        json_matches = re.findall(r'\{[^}]*"documentation"[^}]*\}', script.string)
                        for match in json_matches:
                            try:
                                data = json.loads(match)
                                # Extract any documentation-related URLs
                                if isinstance(data, dict):
                                    for value in data.values():
                                        if isinstance(value, str) and '/documentation/' in value:
                                            framework_id = value.split('/documentation/')[-1].split('/')[0]
                                            if framework_id:
                                                frameworks.add(framework_id)
                            except:
                                continue
                
                await browser.close()
                
        except Exception as e:
            logger.error(f"Playwright scraping failed: {e}")
            
        logger.info(f"Playwright discovered {len(frameworks)} frameworks")
        return frameworks
    
    async def scrape_technologies_page_deep(self) -> Set[str]:
        """Deep scrape of the technologies page with better parsing."""
        frameworks = set()
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                # Try the main technologies page
                response = await client.get("https://developer.apple.com/documentation/technologies")
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Look for framework links
                    for link in soup.find_all('a', href=True):
                        href = link['href']
                        if '/documentation/' in href and href != '/documentation/':
                            framework_id = href.split('/documentation/')[-1].split('/')[0]
                            if framework_id and not framework_id.startswith('_'):
                                frameworks.add(framework_id)
                                
                                # Also get the link text
                                text = link.get_text(strip=True)
                                if text:
                                    frameworks.add(text)
                
                # Try to find any AJAX endpoints that load framework data
                # Look for network requests in the page
                ajax_patterns = [
                    "/api/documentation",
                    "/data/documentation", 
                    "/tutorials/data",
                    "technologies.json",
                    "frameworks.json"
                ]
                
                for pattern in ajax_patterns:
                    try:
                        ajax_url = f"https://developer.apple.com{pattern}"
                        ajax_response = await client.get(ajax_url)
                        
                        if ajax_response.status_code == 200:
                            data = ajax_response.json()
                            # Extract framework info from JSON
                            frameworks.update(self._extract_frameworks_from_json(data))
                            
                    except:
                        continue
                        
        except Exception as e:
            logger.error(f"Deep technologies scraping failed: {e}")
            
        logger.info(f"Deep technologies scraping discovered {len(frameworks)} frameworks")
        return frameworks
    
    def _extract_frameworks_from_json(self, data) -> Set[str]:
        """Extract framework names from JSON data recursively."""
        frameworks = set()
        
        if isinstance(data, dict):
            for key, value in data.items():
                if key in ['title', 'name', 'identifier'] and isinstance(value, str):
                    if value and not value.startswith('_'):
                        frameworks.add(value)
                
                if key == 'identifier' and isinstance(value, str) and '/documentation/' in value:
                    framework_id = value.split('/documentation/')[-1].split('/')[0]
                    if framework_id:
                        frameworks.add(framework_id)
                
                frameworks.update(self._extract_frameworks_from_json(value))
                
        elif isinstance(data, list):
            for item in data:
                frameworks.update(self._extract_frameworks_from_json(item))
        
        return frameworks
    
    async def scrape_sitemap_comprehensive(self) -> Set[str]:
        """Comprehensive sitemap scraping."""
        frameworks = set()
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                # Try multiple sitemap locations
                sitemap_urls = [
                    "https://developer.apple.com/sitemap.xml",
                    "https://developer.apple.com/documentation/sitemap.xml",
                    "https://developer.apple.com/robots.txt"  # Might contain sitemap references
                ]
                
                for url in sitemap_urls:
                    try:
                        response = await client.get(url)
                        if response.status_code == 200:
                            content = response.text
                            
                            # Extract documentation URLs
                            doc_matches = re.findall(r'https://developer\.apple\.com/documentation/([a-zA-Z0-9_-]+)', content)
                            
                            for match in doc_matches:
                                if match and not match.startswith('_'):
                                    frameworks.add(match)
                                    
                                    # Convert to title format too
                                    title = match.replace('-', ' ').title()
                                    frameworks.add(title)
                    
                    except Exception as e:
                        logger.debug(f"Sitemap {url} failed: {e}")
                        
        except Exception as e:
            logger.error(f"Sitemap scraping failed: {e}")
            
        logger.info(f"Sitemap scraping discovered {len(frameworks)} frameworks")
        return frameworks

async def main():
    print("Apple Documentation Menu Scraper")
    print("=" * 60)
    print("Attempting to scrape complete framework list using multiple methods...")
    print()
    
    scraper = AppleMenuScraper()
    all_frameworks = set()
    
    # Method 1: Try Playwright (requires: pip install playwright; playwright install)
    print("Method 1: Playwright (JavaScript rendering)")
    print("-" * 40)
    try:
        playwright_frameworks = await scraper.scrape_with_playwright()
        all_frameworks.update(playwright_frameworks)
        print(f"✅ Playwright: {len(playwright_frameworks)} frameworks discovered")
    except Exception as e:
        print(f"❌ Playwright failed: {e}")
        print("   Install with: pip install playwright && playwright install chromium")
    
    print()
    
    # Method 2: Deep scraping of technologies page
    print("Method 2: Deep Technologies Page Scraping")
    print("-" * 40)
    try:
        deep_frameworks = await scraper.scrape_technologies_page_deep()
        all_frameworks.update(deep_frameworks)
        print(f"✅ Deep scraping: {len(deep_frameworks)} frameworks discovered")
    except Exception as e:
        print(f"❌ Deep scraping failed: {e}")
    
    print()
    
    # Method 3: Comprehensive sitemap
    print("Method 3: Comprehensive Sitemap Scraping")
    print("-" * 40)
    try:
        sitemap_frameworks = await scraper.scrape_sitemap_comprehensive()
        all_frameworks.update(sitemap_frameworks)
        print(f"✅ Sitemap: {len(sitemap_frameworks)} frameworks discovered")
    except Exception as e:
        print(f"❌ Sitemap failed: {e}")
    
    print()
    print("=" * 60)
    print(f"TOTAL DISCOVERED: {len(all_frameworks)} unique frameworks")
    
    # Compare with gold standard
    gold_standard = """Foundation SwiftUI UIKit WatchKit Metal Core Data ARKit""".split()
    
    matches = []
    for gold in gold_standard:
        for discovered in all_frameworks:
            if gold.lower() in discovered.lower() or discovered.lower() in gold.lower():
                matches.append((gold, discovered))
                break
    
    print(f"Matches with known frameworks: {len(matches)}/{len(gold_standard)}")
    
    if len(all_frameworks) > 0:
        print("\nFirst 20 discovered frameworks:")
        for fw in sorted(list(all_frameworks))[:20]:
            print(f"  - {fw}")
        
        # Save results
        results = {
            "total_discovered": len(all_frameworks),
            "frameworks": sorted(list(all_frameworks)),
            "discovery_methods": ["playwright", "deep_scraping", "sitemap"],
            "timestamp": "2025-06-04"
        }
        
        with open("discovered_frameworks.json", "w") as f:
            json.dump(results, f, indent=2)
        
        print(f"\nResults saved to: discovered_frameworks.json")
    
    else:
        print("\n⚠️  No frameworks discovered. Consider:")
        print("1. Installing Playwright: pip install playwright && playwright install")
        print("2. Checking if Apple changed their documentation structure") 
        print("3. Using the manual gold standard list as fallback")

if __name__ == "__main__":
    asyncio.run(main())