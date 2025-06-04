#!/usr/bin/env python3
"""Test if Apple serves different content to bots."""

import asyncio
import httpx

async def test_bot_user_agents():
    """Test different user agents to see if we get pre-rendered content."""
    
    url = "https://developer.apple.com/documentation/swiftui/text"
    
    user_agents = {
        "Googlebot": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Bingbot": "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "curl": "curl/7.64.1",
        "Python": "Python/3.9 aiohttp/3.8.1",
        "No JS Bot": "Mozilla/5.0 (compatible; NoJSBot/1.0)",
    }
    
    async with httpx.AsyncClient() as client:
        for name, ua in user_agents.items():
            print(f"\n{'='*60}")
            print(f"Testing: {name}")
            print(f"User-Agent: {ua}")
            
            headers = {"User-Agent": ua}
            
            try:
                response = await client.get(url, headers=headers, follow_redirects=True)
                print(f"Status: {response.status_code}")
                
                # Check if we get actual content or just the JS app
                content = response.text
                
                # Look for signs of pre-rendered content
                has_title = "<title>Text" in content
                has_js_only = "This page requires JavaScript" in content
                has_content = "struct Text" in content or "A view that displays" in content
                has_meta_desc = '<meta name="description" content="A view that displays' in content
                
                print(f"Has title tag: {has_title}")
                print(f"Has JS warning: {has_js_only}")
                print(f"Has actual content: {has_content}")
                
                if has_content:
                    print("✅ This UA gets pre-rendered content!")
                    with open(f"bot_response_{name}.html", "w") as f:
                        f.write(content)
                    print(f"Saved to bot_response_{name}.html")
                
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_bot_user_agents())