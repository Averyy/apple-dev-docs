#!/usr/bin/env python3
"""Test framework discovery and URL counting."""

import asyncio
import random
import sys
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

from scraper.framework_discovery import FrameworkDiscovery
from scraper.apple_scraper import AppleDocumentationScraper
from scraper.config import Config
from scraper.utils.logger import setup_logging

# Setup logging
setup_logging(log_level="INFO")


async def test_discovery():
    """Test framework discovery and get URL counts."""
    print("=" * 80)
    print("TESTING FRAMEWORK DISCOVERY")
    print("=" * 80)
    
    # Discover all frameworks
    async with FrameworkDiscovery() as discovery:
        frameworks = await discovery.discover_all_frameworks()
        
        print(f"\nTotal frameworks discovered: {len(frameworks)}")
        print("\nFramework categories:")
        
        # Group by category
        by_category = {}
        for fw in frameworks:
            category = fw.get('category', 'other')
            by_category.setdefault(category, []).append(fw)
        
        for category, items in sorted(by_category.items()):
            print(f"  {category}: {len(items)} frameworks")
        
        # Show some examples
        print("\nSample frameworks:")
        for fw in frameworks[:10]:
            print(f"  - {fw['name']} ({fw['id']})")
        
        # Test URL discovery for a few frameworks
        print("\n" + "=" * 80)
        print("TESTING URL DISCOVERY FOR SAMPLE FRAMEWORKS")
        print("=" * 80)
        
        # Pick 3 random frameworks to test
        test_frameworks = random.sample(frameworks, min(3, len(frameworks)))
        
        all_urls = []
        
        for fw in test_frameworks:
            print(f"\nDiscovering URLs for {fw['name']} ({fw['id']})...")
            
            async with AppleDocumentationScraper(fw['id'], fw['name']) as scraper:
                try:
                    urls = await scraper.discover_urls()
                    print(f"  Found {len(urls)} URLs")
                    
                    # Show first 5 URLs
                    print(f"  Sample URLs:")
                    for url in urls[:5]:
                        print(f"    - {url}")
                    
                    all_urls.extend(urls)
                    
                except Exception as e:
                    print(f"  Error: {e}")
        
        # Show random 5 URLs from all discovered
        print("\n" + "=" * 80)
        print("RANDOM 5 SUBPAGE URLs FROM ALL DISCOVERED")
        print("=" * 80)
        
        if all_urls:
            random_urls = random.sample(all_urls, min(5, len(all_urls)))
            for i, url in enumerate(random_urls, 1):
                print(f"{i}. {url}")
        
        print(f"\nTotal URLs discovered across {len(test_frameworks)} frameworks: {len(all_urls)}")
        
        # Estimate total subpages if we scraped all frameworks
        if test_frameworks:
            avg_urls_per_framework = len(all_urls) / len(test_frameworks)
            estimated_total = int(avg_urls_per_framework * len(frameworks))
            print(f"\nEstimated total subpages across all {len(frameworks)} frameworks: ~{estimated_total:,}")
        
        return frameworks, all_urls


if __name__ == "__main__":
    # Run the test
    asyncio.run(test_discovery())