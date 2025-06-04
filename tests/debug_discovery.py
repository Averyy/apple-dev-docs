#!/usr/bin/env python3
"""Debug framework discovery."""

import asyncio
import httpx
from bs4 import BeautifulSoup


async def debug_technologies_page():
    """Debug the technologies page structure."""
    url = "https://developer.apple.com/documentation/technologies"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(f"Status: {response.status_code}")
        print(f"URL: {response.url}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Check title
            title = soup.find('title')
            print(f"\nPage title: {title.text if title else 'No title'}")
            
            # Look for different potential containers
            print("\nLooking for framework links...")
            
            # Method 1: All links to /documentation/
            doc_links = soup.find_all('a', href=lambda x: x and '/documentation/' in x)
            print(f"\nTotal documentation links: {len(doc_links)}")
            
            # Show first 10 unique framework-looking links
            frameworks = set()
            for link in doc_links:
                href = link['href']
                if href.count('/') >= 2 and not any(x in href for x in ['technologies', 'sample', 'release-notes', '?']):
                    text = link.get_text().strip()
                    if text:
                        frameworks.add((text, href))
            
            print(f"\nUnique framework links found: {len(frameworks)}")
            print("\nFirst 20 frameworks:")
            for i, (name, href) in enumerate(sorted(frameworks)[:20], 1):
                print(f"{i:2d}. {name:30s} -> {href}")
            
            # Save HTML for inspection
            with open('technologies_page.html', 'w') as f:
                f.write(response.text)
            print("\nSaved HTML to technologies_page.html for inspection")


if __name__ == "__main__":
    asyncio.run(debug_technologies_page())