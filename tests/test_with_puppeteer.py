#!/usr/bin/env python3
"""Test framework and URL discovery using Puppeteer for accurate counts."""

import asyncio
import random
from pyppeteer import launch


async def test_discovery_with_puppeteer():
    """Test framework discovery and URL counting with Puppeteer."""
    print("=" * 80)
    print("TESTING WITH PUPPETEER")
    print("=" * 80)
    
    # Launch browser
    browser = await launch(headless=True)
    page = await browser.newPage()
    
    try:
        # Step 1: Get all frameworks
        print("\n1. Discovering frameworks...")
        await page.goto('https://developer.apple.com/documentation/technologies')
        await page.waitForSelector('a[href*="/documentation/"]', {'timeout': 5000})
        
        # Extract frameworks
        frameworks = await page.evaluate('''() => {
            const frameworks = [];
            const links = document.querySelectorAll('a[href*="/documentation/"]');
            
            links.forEach(link => {
                const href = link.href;
                const text = link.textContent.trim();
                
                if (href && text && href.includes('/documentation/')) {
                    const url = new URL(href);
                    const path = url.pathname;
                    const parts = path.split('/').filter(p => p);
                    
                    if (parts.length >= 2 && parts[0] === 'documentation' && 
                        parts[1] !== 'technologies' && 
                        !parts[1].includes('sample') &&
                        !parts[1].includes('release') &&
                        !parts[1].includes('?')) {
                        
                        frameworks.push({
                            name: text,
                            id: parts[1],
                            url: href
                        });
                    }
                }
            });
            
            // Remove duplicates
            const seen = new Set();
            return frameworks.filter(f => {
                if (seen.has(f.id)) return false;
                seen.add(f.id);
                return true;
            });
        }''')
        
        print(f"Total frameworks found: {len(frameworks)}")
        
        # Step 2: Test 3 random frameworks for URL counts
        test_frameworks = random.sample(frameworks, min(3, len(frameworks)))
        total_urls = 0
        all_discovered_urls = []
        
        for fw in test_frameworks:
            print(f"\n2. Testing {fw['name']} ({fw['id']})...")
            
            # Navigate to framework page
            await page.goto(fw['url'])
            await asyncio.sleep(2)  # Wait for content to load
            
            # Get all URLs on the main page
            fw_urls = await page.evaluate(f'''() => {{
                const urls = new Set();
                const links = document.querySelectorAll('a[href*="/documentation/{fw['id']}/"]');
                
                links.forEach(link => {{
                    const href = link.href;
                    if (href && !href.includes('?') && !href.includes('#') && !href.includes('changes')) {{
                        urls.add(href);
                    }}
                }});
                
                return Array.from(urls);
            }}''')
            
            print(f"   URLs on main page: {len(fw_urls)}")
            
            # Visit a few sub-pages to estimate total
            sub_pages_to_check = min(3, len(fw_urls))
            additional_urls = set(fw_urls)
            
            for i in range(sub_pages_to_check):
                if i < len(fw_urls):
                    try:
                        await page.goto(fw_urls[i])
                        await asyncio.sleep(1)
                        
                        sub_urls = await page.evaluate(f'''() => {{
                            const urls = new Set();
                            const links = document.querySelectorAll('a[href*="/documentation/{fw['id']}/"]');
                            
                            links.forEach(link => {{
                                const href = link.href;
                                if (href && !href.includes('?') && !href.includes('#') && !href.includes('changes')) {{
                                    urls.add(href);
                                }}
                            }});
                            
                            return Array.from(urls);
                        }}''')
                        
                        additional_urls.update(sub_urls)
                        print(f"   Sub-page {i+1} added {len(sub_urls)} URLs")
                    except:
                        pass
            
            fw_total = len(additional_urls)
            total_urls += fw_total
            all_discovered_urls.extend(list(additional_urls))
            print(f"   Estimated total URLs for {fw['name']}: {fw_total}")
        
        # Step 3: Show random URLs
        print("\n" + "=" * 80)
        print("RANDOM 5 SUBPAGE URLs")
        print("=" * 80)
        
        if all_discovered_urls:
            random_urls = random.sample(all_discovered_urls, min(5, len(all_discovered_urls)))
            for i, url in enumerate(random_urls, 1):
                print(f"{i}. {url}")
        
        # Step 4: Estimate total
        avg_urls_per_framework = total_urls / len(test_frameworks) if test_frameworks else 0
        estimated_total = int(avg_urls_per_framework * len(frameworks))
        
        print(f"\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"Total frameworks: {len(frameworks)}")
        print(f"Frameworks tested: {len(test_frameworks)}")
        print(f"Total URLs discovered: {total_urls}")
        print(f"Average URLs per framework: {avg_urls_per_framework:.0f}")
        print(f"Estimated total subpages across all frameworks: ~{estimated_total:,}")
        
    finally:
        await browser.close()


if __name__ == "__main__":
    asyncio.run(test_discovery_with_puppeteer())