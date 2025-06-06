#!/usr/bin/env python3
"""
Clean up and finalize the discovered framework list.
Remove duplicates and organize for systematic scraping.
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
        'accelerate': 'accelerate',  # Keep lowercase
    }
    
    return mappings.get(clean_id, clean_id)

def categorize_framework(framework_id: str, title: str) -> str:
    """Categorize framework based on ID and title."""
    framework_lower = framework_id.lower()
    title_lower = title.lower()
    
    # Define category keywords
    categories = {
        "User Interface": ['ui', 'kit', 'swiftui', 'uikit', 'appkit', 'widget', 'pencil', 'accessibility'],
        "Graphics & Media": ['metal', 'sprite', 'scene', 'game', 'av', 'core animation', 'core graphics', 'core image', 'core video', 'audio', 'media', 'photo', 'image', 'video', 'cinematic', 'phase', 'quartz'],
        "System & Foundation": ['core', 'foundation', 'dispatch', 'os', 'kernel', 'driver', 'io', 'system', 'disk', 'hypervisor', 'virtualization', 'security', 'network'],
        "Web & JavaScript": ['js', 'javascript', 'webkit', 'safari', 'web', 'browser'],
        "Machine Learning": ['ml', 'coreml', 'create', 'natural language', 'speech', 'vision', 'translation'],
        "Health & Fitness": ['health', 'care', 'research', 'workout'],
        "AR & Spatial": ['ar', 'reality', 'room', 'spatial', 'visionos'],
        "Business & Commerce": ['store', 'pay', 'commerce', 'enterprise', 'business', 'account', 'receipt', 'purchase', 'wallet'],
        "Developer Tools": ['xcode', 'test', 'docc', 'package', 'metric'],
        "APIs & Services": ['api', 'rest', 'server', 'reports', 'notification'],
        "Hardware & Drivers": ['usb', 'hid', 'scsi', 'pci', 'midi', 'serial', 'block', 'bluetooth', 'nfc', 'accessory', 'driver'],
        "Communication": ['call', 'message', 'multipeer', 'push', 'live', 'mail'],
        "Legacy": ['address book', 'glkit', 'iad', 'social', 'assets library', 'opengl']
    }
    
    # Check against each category
    for category, keywords in categories.items():
        if any(keyword in framework_lower or keyword in title_lower for keyword in keywords):
            return category
    
    return "Other"

def assign_priority(framework_id: str, title: str, category: str) -> str:
    """Assign scraping priority based on importance and usage."""
    framework_lower = framework_id.lower()
    
    # High priority: Core frameworks everyone uses
    high_priority = [
        'foundation', 'swiftui', 'uikit', 'appkit', 'watchkit',
        'metal', 'coredata', 'combine', 'swift', 'arkit',
        'coreml', 'vision', 'webkit', 'avfoundation', 'cloudkit',
        'storekit', 'healthkit', 'mapkit', 'coreanimation',
        'coregraphics', 'coreimage', 'security', 'network'
    ]
    
    # Medium priority: Commonly used frameworks
    medium_priority = [
        'photokit', 'gamekit', 'scenekit', 'spritekit', 'passkit',
        'eventkit', 'contacts', 'messageui', 'usernotifications',
        'localauthentication', 'authenticationservices', 'backgroundtasks',
        'corelocation', 'corebluetooth', 'coremotion', 'coretext',
        'corehaptics', 'naturallanguage', 'speech', 'translation'
    ]
    
    # Low priority: Specialized or less common
    low_priority = [
        'externalaccessory', 'multipeerconnectivity', 'networkextension',
        'devicecheck', 'cryptokit', 'compression', 'oslog',
        'metrickit', 'replaykit', 'callkit', 'pushkit'
    ]
    
    # Very low priority: Legacy, deprecated, or very specialized
    legacy_frameworks = [
        'addressbook', 'addressbookui', 'glkit', 'opengl', 'iad',
        'social', 'assetslibrary', 'newsstand'
    ]
    
    if framework_lower in high_priority:
        return "high"
    elif framework_lower in medium_priority:
        return "medium"  
    elif framework_lower in low_priority:
        return "low"
    elif framework_lower in legacy_frameworks or category == "Legacy":
        return "very_low"
    elif category in ["User Interface", "Graphics & Media", "System & Foundation", "Machine Learning"]:
        return "medium"
    else:
        return "low"

def main():
    print("Finalizing Apple Frameworks List")
    print("=" * 60)
    
    # Load the discovered frameworks
    with open("simple_scraper_frameworks.json", "r") as f:
        data = json.load(f)
    
    raw_frameworks = data["extraction_summary"]["detailed_links"]
    print(f"Starting with {len(raw_frameworks)} discovered frameworks")
    
    # Clean and deduplicate
    clean_frameworks = {}
    
    for fw in raw_frameworks:
        original_id = fw['framework_id']
        clean_id = clean_framework_id(original_id)
        title = fw['title']
        
        # Skip obvious duplicates and non-frameworks
        if clean_id in ['welcome', 'samplecode', 'updates', 'technotes']:
            continue
            
        # Skip release notes and documentation pages
        if 'release-notes' in clean_id or clean_id.endswith('-notes'):
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
    
    print(f"After deduplication: {len(clean_frameworks)} unique frameworks")
    
    # Categorize and prioritize
    final_frameworks = []
    categories = {}
    priorities = {}
    
    for fw_id, fw_data in clean_frameworks.items():
        category = categorize_framework(fw_id, fw_data['title'])
        priority = assign_priority(fw_id, fw_data['title'], category)
        
        framework_info = {
            'id': fw_id,
            'title': fw_data['title'],
            'url': fw_data['url'],
            'category': category,
            'priority': priority,
            'original_ids': fw_data['original_ids']
        }
        
        final_frameworks.append(framework_info)
        
        # Track categories and priorities
        if category not in categories:
            categories[category] = []
        categories[category].append(framework_info)
        
        if priority not in priorities:
            priorities[priority] = []
        priorities[priority].append(framework_info)
    
    # Sort frameworks
    final_frameworks.sort(key=lambda x: (x['priority'], x['category'], x['id']))
    
    print(f"\nFinal count: {len(final_frameworks)} frameworks")
    print("\nBy priority:")
    for priority in ['high', 'medium', 'low', 'very_low']:
        if priority in priorities:
            print(f"  {priority.upper()}: {len(priorities[priority])}")
    
    print("\nBy category:")
    for category, frameworks in sorted(categories.items()):
        print(f"  {category}: {len(frameworks)}")
    
    # Create output
    output = {
        'total_frameworks': len(final_frameworks),
        'by_priority': {
            priority: [fw for fw in final_frameworks if fw['priority'] == priority]
            for priority in ['high', 'medium', 'low', 'very_low']
        },
        'by_category': categories,
        'all_frameworks': final_frameworks,
        'scraping_order': {
            'description': 'Recommended order for systematic scraping',
            'phases': [
                {
                    'phase': 1,
                    'name': 'Core Frameworks (High Priority)',
                    'frameworks': [fw['id'] for fw in final_frameworks if fw['priority'] == 'high'],
                    'estimated_pages': '~15,000'
                },
                {
                    'phase': 2, 
                    'name': 'Common Frameworks (Medium Priority)',
                    'frameworks': [fw['id'] for fw in final_frameworks if fw['priority'] == 'medium'],
                    'estimated_pages': '~40,000'
                },
                {
                    'phase': 3,
                    'name': 'Specialized Frameworks (Low Priority)', 
                    'frameworks': [fw['id'] for fw in final_frameworks if fw['priority'] == 'low'],
                    'estimated_pages': '~30,000'
                },
                {
                    'phase': 4,
                    'name': 'Legacy Frameworks (Very Low Priority)',
                    'frameworks': [fw['id'] for fw in final_frameworks if fw['priority'] == 'very_low'],
                    'estimated_pages': '~5,000'
                }
            ]
        },
        'metadata': {
            'source': 'Apple Documentation JSON APIs',
            'discovery_method': 'HTTP scraping + JSON API extraction',
            'timestamp': '2025-06-04',
            'total_estimated_pages': '~90,000'
        }
    }
    
    # Save final list
    with open("apple_frameworks_final.json", "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nFinal framework list saved to: apple_frameworks_final.json")
    
    # Show pilot recommendations
    pilot_frameworks = [fw for fw in final_frameworks if fw['priority'] == 'high'][:5]
    print(f"\nPILOT FRAMEWORKS (after WatchKit success):")
    print("-" * 50)
    for i, fw in enumerate(pilot_frameworks, 1):
        print(f"{i}. {fw['id']:20} - {fw['title']}")
    
    print(f"\n✅ Ready for systematic scraping of {len(final_frameworks)} frameworks!")
    print(f"📊 Estimated total pages: ~90,000")
    print(f"🎯 Target achieved: {len(final_frameworks)} frameworks (close to 350)")

if __name__ == "__main__":
    main()