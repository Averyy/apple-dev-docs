#!/usr/bin/env python3
"""Test the real scraper to get framework and URL counts."""

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
Config.ensure_directories()
setup_logging(log_level="WARNING")  # Reduce noise


async def test_real_counts():
    """Test with real scraper to get accurate counts."""
    print("=" * 80)
    print("APPLE DOCUMENTATION SCRAPER - FRAMEWORK & URL COUNT TEST")
    print("=" * 80)
    
    # Use MCP Puppeteer to get frameworks from rendered page
    print("\nNOTE: Using httpx for initial test. For accurate counts, the scraper")
    print("would use Puppeteer/pyppeteer to handle JavaScript-rendered content.")
    
    # For this test, let's use known frameworks
    test_frameworks = [
        {"id": "swiftui", "name": "SwiftUI"},
        {"id": "uikit", "name": "UIKit"},
        {"id": "metal", "name": "Metal"},
        {"id": "coreml", "name": "Core ML"},
        {"id": "arkit", "name": "ARKit"}
    ]
    
    all_urls = []
    framework_stats = []
    
    print(f"\nTesting {len(test_frameworks)} frameworks:")
    
    for fw in test_frameworks:
        print(f"\n{'='*60}")
        print(f"Framework: {fw['name']} ({fw['id']})")
        print(f"{'='*60}")
        
        async with AppleDocumentationScraper(fw['id'], fw['name']) as scraper:
            try:
                # Discover URLs (with timeout to avoid hanging)
                urls = await asyncio.wait_for(
                    scraper.discover_urls(), 
                    timeout=30.0
                )
                
                print(f"URLs discovered: {len(urls)}")
                
                # Show first 5 URLs
                print("\nSample URLs:")
                for url in urls[:5]:
                    print(f"  - {url}")
                
                if len(urls) > 5:
                    print(f"  ... and {len(urls) - 5} more")
                
                all_urls.extend(urls)
                framework_stats.append({
                    "name": fw['name'],
                    "id": fw['id'],
                    "url_count": len(urls)
                })
                
            except asyncio.TimeoutError:
                print(f"Timeout discovering URLs for {fw['name']}")
            except Exception as e:
                print(f"Error discovering URLs for {fw['name']}: {e}")
    
    # Show random 5 URLs from all discovered
    print("\n" + "=" * 80)
    print("RANDOM 5 SUBPAGE URLs FROM ALL DISCOVERED")
    print("=" * 80)
    
    if all_urls:
        # Remove duplicates
        unique_urls = list(set(all_urls))
        random_urls = random.sample(unique_urls, min(5, len(unique_urls)))
        for i, url in enumerate(random_urls, 1):
            print(f"\n{i}. {url}")
    
    # Summary statistics
    print("\n" + "=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)
    
    print(f"\nFrameworks tested: {len(test_frameworks)}")
    print(f"Total URLs discovered: {len(set(all_urls))}")
    
    if framework_stats:
        avg_urls = sum(f['url_count'] for f in framework_stats) / len(framework_stats)
        print(f"Average URLs per framework: {avg_urls:.0f}")
        
        # Based on Apple having ~150+ frameworks
        estimated_total_frameworks = 150
        estimated_total_urls = int(avg_urls * estimated_total_frameworks)
        print(f"\nEstimated total frameworks: ~{estimated_total_frameworks}")
        print(f"Estimated total subpages: ~{estimated_total_urls:,}")
    
    print("\n" + "=" * 80)
    print("PER-FRAMEWORK BREAKDOWN")
    print("=" * 80)
    
    for stat in framework_stats:
        print(f"{stat['name']:20s}: {stat['url_count']:5d} URLs")


if __name__ == "__main__":
    asyncio.run(test_real_counts())