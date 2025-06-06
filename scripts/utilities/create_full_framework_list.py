#!/usr/bin/env python3
"""
Create a comprehensive list of all Apple frameworks (excluding only deprecated ones).
No priority ranking - we want to scrape them all.
"""

import json
import re
from typing import Dict, List, Set

def clean_framework_id(framework_id: str) -> str:
    """Clean and normalize framework ID."""
    # Convert to lowercase for consistency
    clean_id = framework_id.lower()
    
    # Remove special characters except hyphens and underscores
    clean_id = re.sub(r'[^a-z0-9_-]', '', clean_id)
    
    # Handle some known mappings
    mappings = {
        'quartzcore': 'coreanimation',  # Core Animation is in QuartzCore
    }
    
    return mappings.get(clean_id, clean_id)

def is_deprecated_or_excluded(framework_id: str, title: str) -> bool:
    """Check if framework is deprecated or should be excluded."""
    framework_lower = framework_id.lower()
    title_lower = title.lower()
    
    # Deprecated frameworks
    deprecated = [
        'addressbook', 'addressbookui', 'glkit', 'opengl', 'opengles',
        'iad', 'social', 'assetslibrary', 'newsstand'
    ]
    
    # Non-framework items to exclude
    exclude_patterns = [
        'welcome', 'samplecode', 'updates', 'technotes',
        'release-notes', 'release_notes', '-notes', '_notes'
    ]
    
    # Check deprecated
    if framework_lower in deprecated:
        return True
    
    # Check exclude patterns
    for pattern in exclude_patterns:
        if pattern in framework_lower or pattern in title_lower:
            return True
    
    # Exclude obvious documentation pages
    if 'release notes' in title_lower or 'documentation' in title_lower:
        return True
    
    return False

def categorize_framework(framework_id: str, title: str) -> str:
    """Categorize framework based on ID and title."""
    framework_lower = framework_id.lower()
    title_lower = title.lower()
    
    # Define category keywords
    categories = {
        "User Interface": ['ui', 'kit', 'swiftui', 'uikit', 'appkit', 'widget', 'pencil', 'accessibility', 'contacts'],
        "Graphics & Media": ['metal', 'sprite', 'scene', 'game', 'av', 'animation', 'graphics', 'image', 'video', 'cinematic', 'phase', 'quartz', 'audio', 'media', 'photo'],
        "System & Foundation": ['core', 'foundation', 'dispatch', 'os', 'kernel', 'driver', 'io', 'system', 'disk', 'hypervisor', 'virtualization', 'security', 'network', 'swift'],
        "Web & JavaScript": ['js', 'javascript', 'webkit', 'safari', 'web', 'browser'],
        "Machine Learning": ['ml', 'coreml', 'create', 'natural', 'speech', 'vision', 'translation'],
        "Health & Fitness": ['health', 'care', 'research', 'workout'],
        "AR & Spatial": ['ar', 'reality', 'room', 'spatial', 'visionos'],
        "Business & Commerce": ['store', 'pay', 'commerce', 'enterprise', 'business', 'account', 'receipt', 'purchase', 'wallet'],
        "Developer Tools": ['xcode', 'test', 'docc', 'package', 'metric'],
        "APIs & Services": ['api', 'rest', 'server', 'reports', 'notification'],
        "Hardware & Drivers": ['usb', 'hid', 'scsi', 'pci', 'midi', 'serial', 'block', 'bluetooth', 'nfc', 'accessory', 'driver'],
        "Communication": ['call', 'message', 'multipeer', 'push', 'live', 'mail', 'siri']
    }
    
    # Check against each category
    for category, keywords in categories.items():
        if any(keyword in framework_lower or keyword in title_lower for keyword in keywords):
            return category
    
    return "Other"

def main():
    print("Creating Full Apple Frameworks List (All Non-Deprecated)")
    print("=" * 60)
    
    # Load the discovered frameworks
    with open("simple_scraper_frameworks.json", "r") as f:
        data = json.load(f)
    
    raw_frameworks = data["extraction_summary"]["detailed_links"]
    print(f"Starting with {len(raw_frameworks)} discovered frameworks")
    
    # Clean and filter
    clean_frameworks = {}
    excluded_count = 0
    
    for fw in raw_frameworks:
        original_id = fw['framework_id']
        clean_id = clean_framework_id(original_id)
        title = fw['title']
        
        # Skip deprecated/excluded frameworks
        if is_deprecated_or_excluded(clean_id, title):
            excluded_count += 1
            continue
            
        # For duplicates, keep the better one
        if clean_id in clean_frameworks:
            existing = clean_frameworks[clean_id]
            # Keep the one with the more descriptive title
            if len(title) > len(existing['title']) and 'http' not in title:
                clean_frameworks[clean_id] = {
                    'id': clean_id,
                    'title': title,
                    'url': f"https://developer.apple.com/documentation/{clean_id}",
                    'original_ids': existing['original_ids'] + [original_id]
                }
            else:
                clean_frameworks[clean_id]['original_ids'].append(original_id)
        else:
            clean_frameworks[clean_id] = {
                'id': clean_id,
                'title': title,
                'url': f"https://developer.apple.com/documentation/{clean_id}",
                'original_ids': [original_id]
            }
    
    print(f"After filtering deprecated/excluded: {len(clean_frameworks)} frameworks")
    print(f"Excluded {excluded_count} deprecated or non-framework items")
    
    # Categorize frameworks
    final_frameworks = []
    categories = {}
    
    for fw_id, fw_data in clean_frameworks.items():
        category = categorize_framework(fw_id, fw_data['title'])
        
        framework_info = {
            'id': fw_id,
            'title': fw_data['title'],
            'url': fw_data['url'],
            'category': category,
            'original_ids': fw_data['original_ids']
        }
        
        final_frameworks.append(framework_info)
        
        # Track categories
        if category not in categories:
            categories[category] = []
        categories[category].append(framework_info)
    
    # Sort frameworks alphabetically
    final_frameworks.sort(key=lambda x: x['id'])
    
    print(f"\nFinal count: {len(final_frameworks)} frameworks to scrape")
    print("\nBy category:")
    for category, frameworks in sorted(categories.items()):
        print(f"  {category}: {len(frameworks)} frameworks")
    
    # Create output
    output = {
        'total_frameworks': len(final_frameworks),
        'by_category': categories,
        'all_frameworks': final_frameworks,
        'scraping_plan': {
            'description': 'Scrape all frameworks in alphabetical order',
            'total_frameworks': len(final_frameworks),
            'estimated_total_pages': len(final_frameworks) * 200,  # Rough estimate
            'approach': 'systematic_alphabetical'
        },
        'metadata': {
            'source': 'Apple Documentation JSON APIs',
            'discovery_method': 'HTTP scraping + JSON API extraction',
            'timestamp': '2025-06-04',
            'excluded_deprecated': excluded_count,
            'inclusion_criteria': 'All non-deprecated Apple frameworks'
        }
    }
    
    # Save final list
    with open("apple_frameworks_complete_list.json", "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nComplete framework list saved to: apple_frameworks_complete_list.json")
    
    # Show first 20 frameworks
    print(f"\nFirst 20 frameworks to scrape:")
    print("-" * 50)
    for i, fw in enumerate(final_frameworks[:20], 1):
        print(f"{i:2d}. {fw['id']:25} - {fw['title']}")
    
    if len(final_frameworks) > 20:
        print(f"    ... and {len(final_frameworks) - 20} more")
    
    print(f"\n✅ Ready for systematic scraping of ALL {len(final_frameworks)} frameworks!")
    print(f"📊 Estimated total pages: ~{len(final_frameworks) * 200:,}")
    print(f"🎯 No priority ranking - scrape them all!")

if __name__ == "__main__":
    main()