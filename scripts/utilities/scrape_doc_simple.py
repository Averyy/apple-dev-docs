#!/usr/bin/env python3
"""
Simple scraper to extract documentation links without Playwright.
Uses httpx and BeautifulSoup to find all href="/documentation/*" patterns.
"""

import asyncio
import json
import re
from typing import Set, Dict, List
import httpx
from bs4 import BeautifulSoup
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

class SimpleDocumentationScraper:
    """Scrape Apple's documentation using simple HTTP requests."""
    
    def __init__(self):
        self.framework_links = []
        
    async def scrape_documentation_page(self) -> List[Dict[str, str]]:
        """Extract all documentation links from Apple's main documentation page."""
        links = []
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                print("Loading Apple documentation page...")
                response = await client.get("https://developer.apple.com/documentation/")
                
                if response.status_code == 200:
                    print("✅ Page loaded successfully")
                    
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Find all links with /documentation/ in href
                    doc_links = soup.find_all('a', href=re.compile(r'/documentation/[^/]+/?$'))
                    print(f"Found {len(doc_links)} primary documentation links")
                    
                    for link in doc_links:
                        href = link.get('href', '')
                        text = link.get_text(strip=True)
                        
                        if href and '/documentation/' in href:
                            # Extract framework ID from URL
                            framework_id = href.split('/documentation/')[-1].rstrip('/')
                            
                            if framework_id and framework_id != 'technologies':
                                link_info = {
                                    'framework_id': framework_id,
                                    'title': text if text else framework_id,
                                    'url': f"https://developer.apple.com{href}",
                                    'href_path': href
                                }
                                links.append(link_info)
                    
                    # Also look for any other documentation patterns in the page
                    all_links = soup.find_all('a', href=True)
                    additional_count = 0
                    
                    for link in all_links:
                        href = link.get('href', '')
                        text = link.get_text(strip=True)
                        
                        # Look for documentation links with deeper paths
                        if '/documentation/' in href and href not in [l['href_path'] for l in links]:
                            # Extract the root framework
                            parts = href.split('/documentation/')
                            if len(parts) > 1:
                                framework_parts = parts[1].split('/')
                                framework_id = framework_parts[0]
                                
                                if framework_id and framework_id != 'technologies':
                                    # Check if we already have this framework
                                    existing = next((l for l in links if l['framework_id'] == framework_id), None)
                                    if not existing:
                                        link_info = {
                                            'framework_id': framework_id,
                                            'title': text if text else framework_id,
                                            'url': f"https://developer.apple.com/documentation/{framework_id}",
                                            'href_path': f"/documentation/{framework_id}"
                                        }
                                        links.append(link_info)
                                        additional_count += 1
                    
                    print(f"✅ Found {additional_count} additional framework references")
                    print(f"✅ Total extracted: {len(links)} unique frameworks")
                    
                else:
                    print(f"❌ Failed to load page: {response.status_code}")
                    
        except Exception as e:
            print(f"❌ HTTP scraping failed: {e}")
            
        return links
    
    async def scrape_technologies_page(self) -> List[Dict[str, str]]:
        """Also scrape the technologies page for more frameworks."""
        links = []
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                print("Loading technologies page...")
                response = await client.get("https://developer.apple.com/documentation/technologies")
                
                if response.status_code == 200:
                    print("✅ Technologies page loaded")
                    
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Find all documentation links
                    doc_links = soup.find_all('a', href=re.compile(r'/documentation/'))
                    print(f"Found {len(doc_links)} links on technologies page")
                    
                    for link in doc_links:
                        href = link.get('href', '')
                        text = link.get_text(strip=True)
                        
                        if href and '/documentation/' in href:
                            # Extract framework ID
                            parts = href.split('/documentation/')
                            if len(parts) > 1:
                                framework_parts = parts[1].split('/')
                                framework_id = framework_parts[0]
                                
                                if framework_id and framework_id != 'technologies':
                                    link_info = {
                                        'framework_id': framework_id,
                                        'title': text if text else framework_id,
                                        'url': f"https://developer.apple.com/documentation/{framework_id}",
                                        'href_path': f"/documentation/{framework_id}"
                                    }
                                    links.append(link_info)
                    
                    print(f"✅ Extracted {len(links)} frameworks from technologies page")
                    
        except Exception as e:
            print(f"❌ Technologies page scraping failed: {e}")
            
        return links
    
    async def try_json_api(self) -> List[Dict[str, str]]:
        """Try to get data from Apple's JSON APIs."""
        links = []
        
        json_urls = [
            "https://developer.apple.com/tutorials/data/documentation/technologies.json",
            "https://developer.apple.com/tutorials/data/documentation.json"
        ]
        
        for url in json_urls:
            try:
                async with httpx.AsyncClient(timeout=30.0) as client:
                    print(f"Trying JSON API: {url}")
                    response = await client.get(url)
                    
                    if response.status_code == 200:
                        data = response.json()
                        print(f"✅ Got JSON data from {url}")
                        
                        # Extract frameworks from JSON structure
                        extracted = self._extract_frameworks_from_json(data)
                        links.extend(extracted)
                        print(f"Extracted {len(extracted)} frameworks from JSON")
                    
            except Exception as e:
                print(f"JSON API {url} failed: {e}")
        
        return links
    
    def _extract_frameworks_from_json(self, data) -> List[Dict[str, str]]:
        """Extract framework info from JSON data recursively."""
        links = []
        
        def extract_recursive(obj, path=""):
            if isinstance(obj, dict):
                # Look for common JSON patterns
                if 'identifier' in obj and isinstance(obj['identifier'], str):
                    if '/documentation/' in obj['identifier']:
                        framework_id = obj['identifier'].split('/documentation/')[-1].split('/')[0]
                        if framework_id and framework_id != 'technologies':
                            title = obj.get('title', framework_id)
                            links.append({
                                'framework_id': framework_id,
                                'title': title,
                                'url': f"https://developer.apple.com/documentation/{framework_id}",
                                'href_path': f"/documentation/{framework_id}",
                                'source': 'json_api'
                            })
                
                # Recurse through all values
                for key, value in obj.items():
                    extract_recursive(value, f"{path}.{key}" if path else key)
                    
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    extract_recursive(item, f"{path}[{i}]" if path else f"[{i}]")
        
        extract_recursive(data)
        return links
    
    def analyze_links(self, links: List[Dict[str, str]]) -> Dict:
        """Analyze and deduplicate the extracted links."""
        
        # Remove duplicates by framework_id
        unique_frameworks = {}
        for link in links:
            framework_id = link['framework_id']
            if framework_id not in unique_frameworks:
                unique_frameworks[framework_id] = link
            # Keep the one with the better title
            elif len(link['title']) > len(unique_frameworks[framework_id]['title']):
                unique_frameworks[framework_id] = link
        
        unique_links = list(unique_frameworks.values())
        unique_links.sort(key=lambda x: x['framework_id'].lower())
        
        framework_ids = [link['framework_id'] for link in unique_links]
        framework_titles = [link['title'] for link in unique_links]
        
        return {
            'total_unique_frameworks': len(unique_links),
            'framework_ids': framework_ids,
            'framework_titles': framework_titles,
            'detailed_links': unique_links
        }

async def main():
    print("Apple Documentation Simple Scraper")
    print("=" * 60)
    print("Extracting documentation links using HTTP requests...")
    print()
    
    scraper = SimpleDocumentationScraper()
    all_links = []
    
    # Method 1: Main documentation page
    print("Method 1: Main Documentation Page")
    print("-" * 40)
    main_links = await scraper.scrape_documentation_page()
    all_links.extend(main_links)
    
    print()
    
    # Method 2: Technologies page
    print("Method 2: Technologies Page")
    print("-" * 40)
    tech_links = await scraper.scrape_technologies_page()
    all_links.extend(tech_links)
    
    print()
    
    # Method 3: JSON APIs
    print("Method 3: JSON APIs")
    print("-" * 40)
    json_links = await scraper.try_json_api()
    all_links.extend(json_links)
    
    print()
    
    if all_links:
        # Analyze results
        analysis = scraper.analyze_links(all_links)
        
        print("RESULTS:")
        print("=" * 60)
        print(f"Total unique frameworks: {analysis['total_unique_frameworks']}")
        print()
        
        print("All frameworks found:")
        print("-" * 30)
        for i, link in enumerate(analysis['detailed_links'], 1):
            print(f"{i:3d}. {link['framework_id']:25} - {link['title']}")
        
        # Save results
        output_file = "simple_scraper_frameworks.json"
        with open(output_file, "w") as f:
            json.dump({
                "extraction_summary": analysis,
                "timestamp": "2025-06-04",
                "source": "HTTP scraping of Apple documentation pages",
                "methods": ["main_page", "technologies_page", "json_apis"]
            }, f, indent=2)
        
        print(f"\nResults saved to: {output_file}")
        
        # Check if we're close to 350
        count = analysis['total_unique_frameworks']
        if count < 100:
            print(f"\n⚠️  Only found {count} frameworks - need to try more aggressive discovery")
            print("Consider using Playwright for JavaScript-rendered content")
        elif count < 300:
            print(f"\n📍 Found {count} frameworks - getting closer to target of ~350")
        else:
            print(f"\n✅ Found {count} frameworks - excellent coverage!")
        
    else:
        print("❌ No frameworks found")

if __name__ == "__main__":
    asyncio.run(main())