#!/usr/bin/env python3
"""Comprehensive list of Apple frameworks to scrape."""

import json
from typing import Dict, List

def get_all_apple_frameworks() -> Dict[str, List[Dict[str, str]]]:
    """Get comprehensive list of Apple frameworks organized by category."""
    
    frameworks = {
        "User Interface": [
            {"id": "swiftui", "title": "SwiftUI", "priority": "high"},
            {"id": "uikit", "title": "UIKit", "priority": "high"},
            {"id": "appkit", "title": "AppKit", "priority": "high"},
            {"id": "watchkit", "title": "WatchKit", "priority": "high"},
            {"id": "widgetkit", "title": "WidgetKit", "priority": "medium"},
            {"id": "tvuikit", "title": "TVUIKit", "priority": "medium"},
            {"id": "pencilkit", "title": "PencilKit", "priority": "medium"},
            {"id": "accessibility", "title": "Accessibility", "priority": "medium"},
        ],
        
        "Graphics and Games": [
            {"id": "metal", "title": "Metal", "priority": "high"},
            {"id": "metalkit", "title": "MetalKit", "priority": "high"},
            {"id": "metalperformanceshaders", "title": "Metal Performance Shaders", "priority": "high"},
            {"id": "scenekit", "title": "SceneKit", "priority": "high"},
            {"id": "spritekit", "title": "SpriteKit", "priority": "high"},
            {"id": "gamekit", "title": "GameKit", "priority": "medium"},
            {"id": "gamecontroller", "title": "Game Controller", "priority": "medium"},
            {"id": "gameplaykit", "title": "GameplayKit", "priority": "medium"},
            {"id": "realitykit", "title": "RealityKit", "priority": "high"},
            {"id": "coregraphics", "title": "Core Graphics", "priority": "high"},
            {"id": "coreanimation", "title": "Core Animation", "priority": "high"},
            {"id": "coreimage", "title": "Core Image", "priority": "high"},
            {"id": "quartzcore", "title": "Quartz Core", "priority": "medium"},
            {"id": "accelerate", "title": "Accelerate", "priority": "medium"},
        ],
        
        "App Frameworks": [
            {"id": "foundation", "title": "Foundation", "priority": "high"},
            {"id": "combine", "title": "Combine", "priority": "high"},
            {"id": "swift", "title": "Swift", "priority": "high"},
            {"id": "swiftdata", "title": "SwiftData", "priority": "high"},
            {"id": "observation", "title": "Observation", "priority": "medium"},
            {"id": "concurrency", "title": "Swift Concurrency", "priority": "high"},
        ],
        
        "App Services": [
            {"id": "cloudkit", "title": "CloudKit", "priority": "high"},
            {"id": "coredata", "title": "Core Data", "priority": "high"},
            {"id": "storekit", "title": "StoreKit", "priority": "high"},
            {"id": "callkit", "title": "CallKit", "priority": "medium"},
            {"id": "pushkit", "title": "PushKit", "priority": "medium"},
            {"id": "sirikit", "title": "SiriKit", "priority": "high"},
            {"id": "notificationcenter", "title": "Notification Center", "priority": "medium"},
            {"id": "usernotifications", "title": "User Notifications", "priority": "high"},
            {"id": "backgroundtasks", "title": "Background Tasks", "priority": "medium"},
            {"id": "eventkit", "title": "EventKit", "priority": "medium"},
            {"id": "contacts", "title": "Contacts", "priority": "medium"},
            {"id": "contactsui", "title": "ContactsUI", "priority": "low"},
            {"id": "mapkit", "title": "MapKit", "priority": "high"},
            {"id": "passkit", "title": "PassKit", "priority": "medium"},
            {"id": "messageui", "title": "MessageUI", "priority": "low"},
        ],
        
        "Media": [
            {"id": "avfoundation", "title": "AVFoundation", "priority": "high"},
            {"id": "avkit", "title": "AVKit", "priority": "high"},
            {"id": "photokit", "title": "PhotoKit", "priority": "high"},
            {"id": "photos", "title": "Photos", "priority": "medium"},
            {"id": "photosui", "title": "PhotosUI", "priority": "medium"},
            {"id": "imageio", "title": "Image I/O", "priority": "medium"},
            {"id": "coreaudio", "title": "Core Audio", "priority": "high"},
            {"id": "coremedia", "title": "Core Media", "priority": "high"},
            {"id": "corevideo", "title": "Core Video", "priority": "medium"},
            {"id": "videotoolbox", "title": "VideoToolbox", "priority": "medium"},
            {"id": "audiotoolbox", "title": "AudioToolbox", "priority": "medium"},
            {"id": "audiounits", "title": "AudioUnit", "priority": "medium"},
            {"id": "mediaplayer", "title": "Media Player", "priority": "medium"},
            {"id": "soundanalysis", "title": "Sound Analysis", "priority": "medium"},
            {"id": "musickit", "title": "MusicKit", "priority": "medium"},
            {"id": "shazamkit", "title": "ShazamKit", "priority": "low"},
        ],
        
        "Web": [
            {"id": "webkit", "title": "WebKit", "priority": "high"},
            {"id": "javascriptcore", "title": "JavaScriptCore", "priority": "medium"},
            {"id": "safariservices", "title": "Safari Services", "priority": "medium"},
            {"id": "authenticationservices", "title": "Authentication Services", "priority": "medium"},
        ],
        
        "Machine Learning and AI": [
            {"id": "coreml", "title": "Core ML", "priority": "high"},
            {"id": "createml", "title": "Create ML", "priority": "high"},
            {"id": "naturallanguage", "title": "Natural Language", "priority": "high"},
            {"id": "speech", "title": "Speech", "priority": "high"},
            {"id": "vision", "title": "Vision", "priority": "high"},
            {"id": "visionkit", "title": "VisionKit", "priority": "medium"},
            {"id": "translation", "title": "Translation", "priority": "medium"},
        ],
        
        "Augmented Reality": [
            {"id": "arkit", "title": "ARKit", "priority": "high"},
            {"id": "roomplan", "title": "RoomPlan", "priority": "medium"},
            {"id": "quicklook", "title": "Quick Look", "priority": "medium"},
        ],
        
        "Health and Fitness": [
            {"id": "healthkit", "title": "HealthKit", "priority": "high"},
            {"id": "carekit", "title": "CareKit", "priority": "medium"},
            {"id": "researchkit", "title": "ResearchKit", "priority": "medium"},
            {"id": "workoutkit", "title": "WorkoutKit", "priority": "medium"},
        ],
        
        "System": [
            {"id": "security", "title": "Security", "priority": "high"},
            {"id": "network", "title": "Network", "priority": "high"},
            {"id": "corelocation", "title": "Core Location", "priority": "high"},
            {"id": "corebluetooth", "title": "Core Bluetooth", "priority": "high"},
            {"id": "corenfc", "title": "Core NFC", "priority": "medium"},
            {"id": "coremotion", "title": "Core Motion", "priority": "high"},
            {"id": "devicemanagement", "title": "Device Management", "priority": "low"},
            {"id": "os", "title": "OS", "priority": "high"},
            {"id": "dispatch", "title": "Dispatch", "priority": "high"},
            {"id": "compression", "title": "Compression", "priority": "low"},
            {"id": "cryptokit", "title": "CryptoKit", "priority": "medium"},
            {"id": "localauthentication", "title": "Local Authentication", "priority": "medium"},
            {"id": "externalaccessory", "title": "External Accessory", "priority": "low"},
            {"id": "multipeerconnectivity", "title": "Multipeer Connectivity", "priority": "low"},
            {"id": "networkextension", "title": "Network Extension", "priority": "low"},
        ],
        
        "Developer Tools": [
            {"id": "xctest", "title": "XCTest", "priority": "high"},
            {"id": "xcode", "title": "Xcode", "priority": "medium"},
            {"id": "packagedescription", "title": "Package Description", "priority": "medium"},
            {"id": "docc", "title": "DocC", "priority": "medium"},
            {"id": "oslog", "title": "OSLog", "priority": "medium"},
            {"id": "metrickit", "title": "MetricKit", "priority": "low"},
        ],
        
        "visionOS (Spatial Computing)": [
            {"id": "realitykit", "title": "RealityKit", "priority": "high"},  # Shared with Graphics
            {"id": "immersivespace", "title": "ImmersiveSpace", "priority": "high"},
            {"id": "spacialaudio", "title": "Spatial Audio", "priority": "medium"},
        ],
        
        "Business and Enterprise": [
            {"id": "businesschat", "title": "Business Chat", "priority": "low"},
            {"id": "devicecheck", "title": "DeviceCheck", "priority": "low"},
            {"id": "appstoreconnectapi", "title": "App Store Connect API", "priority": "low"},
        ],
        
        "Interoperability": [
            {"id": "objectivec", "title": "Objective-C Runtime", "priority": "medium"},
            {"id": "c", "title": "C", "priority": "low"},
            {"id": "darwin", "title": "Darwin", "priority": "low"},
        ],
        
        "Legacy/Deprecated": [
            {"id": "newsstandkit", "title": "Newsstand Kit", "priority": "very_low"},
            {"id": "glkit", "title": "GLKit", "priority": "very_low"},
            {"id": "opengles", "title": "OpenGL ES", "priority": "very_low"},
            {"id": "addressbook", "title": "Address Book", "priority": "very_low"},
            {"id": "addressbookui", "title": "Address Book UI", "priority": "very_low"},
        ]
    }
    
    return frameworks

def main():
    frameworks_by_category = get_all_apple_frameworks()
    
    # Flatten all frameworks
    all_frameworks = []
    for category, frameworks in frameworks_by_category.items():
        for fw in frameworks:
            fw['category'] = category
            fw['url'] = f"https://developer.apple.com/documentation/{fw['id']}"
            all_frameworks.append(fw)
    
    # Count by priority
    priority_counts = {}
    for fw in all_frameworks:
        priority = fw['priority']
        priority_counts[priority] = priority_counts.get(priority, 0) + 1
    
    print("Apple Frameworks Comprehensive List")
    print("=" * 60)
    print(f"Total frameworks: {len(all_frameworks)}")
    print()
    
    # Print by priority
    priorities = ["high", "medium", "low", "very_low"]
    for priority in priorities:
        frameworks = [fw for fw in all_frameworks if fw['priority'] == priority]
        if frameworks:
            print(f"{priority.upper()} PRIORITY ({len(frameworks)} frameworks):")
            print("-" * 40)
            
            # Group by category
            by_category = {}
            for fw in frameworks:
                cat = fw['category']
                if cat not in by_category:
                    by_category[cat] = []
                by_category[cat].append(fw)
            
            for category, cat_frameworks in sorted(by_category.items()):
                print(f"  {category}:")
                for fw in sorted(cat_frameworks, key=lambda x: x['title']):
                    print(f"    - {fw['title']:25} ({fw['id']})")
            print()
    
    # Recommendations for scraping order
    print("RECOMMENDED SCRAPING ORDER:")
    print("=" * 60)
    print("1. Start with HIGH priority frameworks (most commonly used)")
    print("2. Then MEDIUM priority frameworks")
    print("3. LOW and VERY_LOW can be done later")
    print()
    
    print("Suggested pilot frameworks to test after WatchKit:")
    pilot_frameworks = [fw for fw in all_frameworks if fw['id'] in 
                       ['foundation', 'swiftui', 'uikit', 'coredata', 'combine']]
    
    for i, fw in enumerate(pilot_frameworks, 1):
        print(f"{i}. {fw['title']} ({fw['id']}) - {fw['category']}")
    
    # Save to file
    output = {
        "total_count": len(all_frameworks),
        "by_priority": {priority: [fw for fw in all_frameworks if fw['priority'] == priority] 
                       for priority in priorities},
        "by_category": frameworks_by_category,
        "all_frameworks": all_frameworks
    }
    
    with open("apple_frameworks_comprehensive.json", "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nComplete list saved to: apple_frameworks_comprehensive.json")

if __name__ == "__main__":
    main()