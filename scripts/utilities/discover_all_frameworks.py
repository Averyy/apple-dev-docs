#!/usr/bin/env python3
"""Discover all available Apple frameworks from the documentation site."""

import asyncio
import json
from typing import Dict, List, Set
import httpx
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

async def discover_frameworks() -> Dict[str, List[Dict[str, str]]]:
    """Discover all frameworks from Apple's documentation."""
    
    # Main technologies/frameworks page
    base_url = "https://developer.apple.com/tutorials/data/documentation/technologies.json"
    
    frameworks_by_category = {}
    all_frameworks = []
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            # Fetch the main technologies list
            response = await client.get(base_url)
            response.raise_for_status()
            data = json.loads(response.text)
            
            # Extract sections
            for section in data.get('sections', []):
                category_title = section.get('title', 'Other')
                frameworks_in_category = []
                
                for item in section.get('items', []):
                    identifier = item.get('identifier', '')
                    if identifier.startswith('doc://'):
                        # Extract framework ID from identifier
                        # Format: doc://com.apple.documentation/documentation/framework_name
                        parts = identifier.split('/')
                        if len(parts) >= 4 and parts[3] == 'documentation':
                            framework_id = parts[4] if len(parts) > 4 else ''
                            if framework_id and not framework_id.startswith('_'):  # Skip private frameworks
                                framework_info = {
                                    'id': framework_id,
                                    'title': item.get('title', framework_id),
                                    'category': category_title,
                                    'url': f"https://developer.apple.com/documentation/{framework_id}"
                                }
                                frameworks_in_category.append(framework_info)
                                all_frameworks.append(framework_info)
                
                if frameworks_in_category:
                    frameworks_by_category[category_title] = frameworks_in_category
            
            # Also check for frameworks in topicSections
            for section in data.get('topicSections', []):
                category_title = section.get('title', 'Other')
                frameworks_in_category = []
                
                for identifier in section.get('identifiers', []):
                    if identifier.startswith('doc://'):
                        parts = identifier.split('/documentation/')
                        if len(parts) == 2:
                            framework_id = parts[1].split('/')[0]
                            if framework_id and not framework_id.startswith('_'):
                                # Check if we already have this framework
                                if not any(f['id'] == framework_id for f in all_frameworks):
                                    framework_info = {
                                        'id': framework_id,
                                        'title': framework_id.replace('-', ' ').title(),
                                        'category': category_title,
                                        'url': f"https://developer.apple.com/documentation/{framework_id}"
                                    }
                                    frameworks_in_category.append(framework_info)
                                    all_frameworks.append(framework_info)
                
                if frameworks_in_category:
                    if category_title in frameworks_by_category:
                        frameworks_by_category[category_title].extend(frameworks_in_category)
                    else:
                        frameworks_by_category[category_title] = frameworks_in_category
            
        except Exception as e:
            logger.error(f"Failed to fetch technologies list: {e}")
            
            # Fallback: Use known frameworks
            frameworks_by_category = get_known_frameworks()
            for frameworks in frameworks_by_category.values():
                all_frameworks.extend(frameworks)
    
    return frameworks_by_category, all_frameworks

def get_known_frameworks() -> Dict[str, List[Dict[str, str]]]:
    """Get a hardcoded list of known Apple frameworks as fallback."""
    return {
        "User Interface": [
            {"id": "swiftui", "title": "SwiftUI", "category": "User Interface"},
            {"id": "uikit", "title": "UIKit", "category": "User Interface"},
            {"id": "appkit", "title": "AppKit", "category": "User Interface"},
            {"id": "watchkit", "title": "WatchKit", "category": "User Interface"},
            {"id": "widgetkit", "title": "WidgetKit", "category": "User Interface"},
        ],
        "Graphics and Games": [
            {"id": "metal", "title": "Metal", "category": "Graphics and Games"},
            {"id": "metalkit", "title": "MetalKit", "category": "Graphics and Games"},
            {"id": "metalperformanceshaders", "title": "Metal Performance Shaders", "category": "Graphics and Games"},
            {"id": "scenekit", "title": "SceneKit", "category": "Graphics and Games"},
            {"id": "spritekit", "title": "SpriteKit", "category": "Graphics and Games"},
            {"id": "gamekit", "title": "GameKit", "category": "Graphics and Games"},
            {"id": "gamecontroller", "title": "Game Controller", "category": "Graphics and Games"},
            {"id": "realitykit", "title": "RealityKit", "category": "Graphics and Games"},
        ],
        "App Frameworks": [
            {"id": "foundation", "title": "Foundation", "category": "App Frameworks"},
            {"id": "combine", "title": "Combine", "category": "App Frameworks"},
            {"id": "swift", "title": "Swift", "category": "App Frameworks"},
            {"id": "swiftdata", "title": "SwiftData", "category": "App Frameworks"},
            {"id": "observation", "title": "Observation", "category": "App Frameworks"},
        ],
        "App Services": [
            {"id": "cloudkit", "title": "CloudKit", "category": "App Services"},
            {"id": "coredata", "title": "Core Data", "category": "App Services"},
            {"id": "storekit", "title": "StoreKit", "category": "App Services"},
            {"id": "gameplaykit", "title": "GameplayKit", "category": "App Services"},
            {"id": "callkit", "title": "CallKit", "category": "App Services"},
            {"id": "pushkit", "title": "PushKit", "category": "App Services"},
            {"id": "sirikit", "title": "SiriKit", "category": "App Services"},
            {"id": "notificationcenter", "title": "Notification Center", "category": "App Services"},
        ],
        "Media": [
            {"id": "avfoundation", "title": "AVFoundation", "category": "Media"},
            {"id": "avkit", "title": "AVKit", "category": "Media"},
            {"id": "photokit", "title": "PhotoKit", "category": "Media"},
            {"id": "imageio", "title": "Image I/O", "category": "Media"},
            {"id": "coreaudio", "title": "Core Audio", "category": "Media"},
            {"id": "coremedia", "title": "Core Media", "category": "Media"},
            {"id": "corevideo", "title": "Core Video", "category": "Media"},
            {"id": "videotoolbox", "title": "VideoToolbox", "category": "Media"},
            {"id": "audiotoolbox", "title": "AudioToolbox", "category": "Media"},
            {"id": "mediaPlayer", "title": "Media Player", "category": "Media"},
            {"id": "soundanalysis", "title": "Sound Analysis", "category": "Media"},
        ],
        "Web": [
            {"id": "webkit", "title": "WebKit", "category": "Web"},
            {"id": "javascriptcore", "title": "JavaScriptCore", "category": "Web"},
            {"id": "safariservices", "title": "Safari Services", "category": "Web"},
        ],
        "Machine Learning and AI": [
            {"id": "coreml", "title": "Core ML", "category": "Machine Learning and AI"},
            {"id": "createml", "title": "Create ML", "category": "Machine Learning and AI"},
            {"id": "naturallanguage", "title": "Natural Language", "category": "Machine Learning and AI"},
            {"id": "speech", "title": "Speech", "category": "Machine Learning and AI"},
            {"id": "vision", "title": "Vision", "category": "Machine Learning and AI"},
            {"id": "visionkit", "title": "VisionKit", "category": "Machine Learning and AI"},
        ],
        "Augmented Reality": [
            {"id": "arkit", "title": "ARKit", "category": "Augmented Reality"},
            {"id": "roomplan", "title": "RoomPlan", "category": "Augmented Reality"},
        ],
        "Health": [
            {"id": "healthkit", "title": "HealthKit", "category": "Health"},
            {"id": "carekit", "title": "CareKit", "category": "Health"},
            {"id": "researchkit", "title": "ResearchKit", "category": "Health"},
        ],
        "System": [
            {"id": "security", "title": "Security", "category": "System"},
            {"id": "network", "title": "Network", "category": "System"},
            {"id": "corelocation", "title": "Core Location", "category": "System"},
            {"id": "corebluetooth", "title": "Core Bluetooth", "category": "System"},
            {"id": "corenfc", "title": "Core NFC", "category": "System"},
            {"id": "coremotion", "title": "Core Motion", "category": "System"},
            {"id": "usernotifications", "title": "User Notifications", "category": "System"},
            {"id": "backgroundtasks", "title": "Background Tasks", "category": "System"},
            {"id": "os", "title": "OS", "category": "System"},
            {"id": "dispatch", "title": "Dispatch", "category": "System"},
        ],
        "Developer Tools": [
            {"id": "xctest", "title": "XCTest", "category": "Developer Tools"},
            {"id": "xcode", "title": "Xcode", "category": "Developer Tools"},
            {"id": "packagedescription", "title": "Package Description", "category": "Developer Tools"},
            {"id": "docc", "title": "DocC", "category": "Developer Tools"},
        ]
    }

async def main():
    print("Discovering all Apple frameworks...")
    print("-" * 60)
    
    frameworks_by_category, all_frameworks = await discover_frameworks()
    
    # Sort frameworks
    all_frameworks.sort(key=lambda x: x['title'])
    
    # Print summary by category
    print("\nFrameworks by Category:")
    print("=" * 60)
    
    total_count = 0
    for category, frameworks in sorted(frameworks_by_category.items()):
        print(f"\n{category} ({len(frameworks)} frameworks):")
        for fw in sorted(frameworks, key=lambda x: x['title']):
            print(f"  - {fw['title']:30} ({fw['id']})")
        total_count += len(frameworks)
    
    print("\n" + "=" * 60)
    print(f"Total frameworks discovered: {len(all_frameworks)}")
    
    # Save to JSON file
    output = {
        "total_count": len(all_frameworks),
        "by_category": frameworks_by_category,
        "all_frameworks": all_frameworks
    }
    
    with open("frameworks_list.json", "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nFull list saved to frameworks_list.json")
    
    # Print scrapting command examples
    print("\nExample scraping commands:")
    print("-" * 60)
    for fw in all_frameworks[:5]:
        print(f"python3 scrape_framework.py --framework {fw['id']}")

if __name__ == "__main__":
    asyncio.run(main())