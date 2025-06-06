#!/usr/bin/env python3
"""
Fix the framework list to only include top-level frameworks
and use consistent casing from Apple's URLs
"""

import json
import asyncio
from pathlib import Path

async def fix_framework_list():
    """Load technologies.json and extract only top-level frameworks."""
    
    # Load the raw technologies.json data
    import httpx
    
    url = "https://developer.apple.com/tutorials/data/documentation/technologies.json"
    print(f"🔄 Fetching fresh framework list from {url}")
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    
    print(f"✅ Fetched data successfully")
    
    # Extract frameworks
    frameworks = []
    references = data.get('references', {})
    
    for ref_id, ref_data in references.items():
        url = ref_data.get('url', '')
        
        # Only process documentation URLs
        if not url.startswith('/documentation/'):
            continue
            
        # Extract path after /documentation/
        path = url.replace('/documentation/', '')
        
        # Only include top-level frameworks (no slashes in path)
        if '/' in path:
            continue
            
        title = ref_data.get('title', '')
        if not title:
            continue
            
        # Use the exact casing from the URL
        framework_id = path
        
        frameworks.append({
            'id': framework_id,
            'title': title,
            'href': url,
            'type': ref_data.get('type', 'topic')
        })
    
    # Remove duplicates and sort
    unique_frameworks = {}
    for fw in frameworks:
        # Use lowercase for deduplication but preserve original casing
        key = fw['id'].lower()
        if key not in unique_frameworks:
            unique_frameworks[key] = fw
    
    # Get the list and sort by title
    framework_list = list(unique_frameworks.values())
    framework_list.sort(key=lambda x: x['title'].lower())
    
    print(f"📊 Found {len(framework_list)} top-level frameworks")
    
    # Save the corrected list
    output = {
        "metadata": {
            "source": "https://developer.apple.com/tutorials/data/documentation/technologies.json",
            "method": "JSON API extraction - top-level only",
            "timestamp": "2025-06-04",
            "total_frameworks": len(framework_list),
            "extraction_success": "COMPLETE"
        },
        "frameworks": framework_list
    }
    
    output_file = Path("data/fixed_frameworks_list.json")
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"✅ Saved fixed framework list to {output_file}")
    
    # Show some examples
    print("\n📋 Sample frameworks:")
    for fw in framework_list[:10]:
        print(f"   - {fw['title']} (id: {fw['id']})")
    
    # Check for case inconsistencies
    case_issues = []
    for fw in framework_list:
        if fw['id'] != fw['id'].lower() and fw['id'] != fw['id'].upper():
            case_issues.append(fw)
    
    if case_issues:
        print(f"\n⚠️  Found {len(case_issues)} frameworks with mixed case IDs:")
        for fw in case_issues[:5]:
            print(f"   - {fw['title']} (id: {fw['id']})")

if __name__ == "__main__":
    asyncio.run(fix_framework_list())