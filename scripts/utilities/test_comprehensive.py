#!/usr/bin/env python3
"""
Test script for comprehensive scraper - runs on just a few frameworks
"""

import asyncio
from comprehensive_scraper import ComprehensiveAppleScraper

async def test_run():
    """Test with just 2-3 frameworks to verify everything works"""
    
    print("🧪 TESTING COMPREHENSIVE SCRAPER")
    print("=" * 50)
    
    # Create scraper with limited concurrency for testing
    scraper = ComprehensiveAppleScraper(max_concurrent=1)
    
    # Override to test with just a few frameworks
    original_method = scraper.get_all_frameworks
    
    async def get_test_frameworks():
        all_frameworks = await original_method()
        # Return just a few frameworks for testing
        test_frameworks = [
            fw for fw in all_frameworks 
            if fw['id'] in ['simd', 'Accessibility', 'AdServices']  # Pick some small ones
        ]
        print(f"🎯 Testing with {len(test_frameworks)} frameworks: {[fw['title'] for fw in test_frameworks]}")
        return test_frameworks
    
    scraper.get_all_frameworks = get_test_frameworks
    
    # Run the comprehensive scraper
    await scraper.scrape_all_frameworks()

if __name__ == "__main__":
    asyncio.run(test_run())