#!/usr/bin/env python3
"""Extract comprehensive framework list matching the manual list provided."""

import asyncio
import json
import re
from typing import Dict, List, Set, Tuple
import httpx
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

# Your manually provided list
MANUAL_FRAMEWORKS = """Accelerate
Accessibility
AccessorySetupKit
Account & Organizational Data Sharing
Account Data Transfer
Accounts
ActivityKit
AdAttributionKit
Address Book
Address Book UI
AdServices
AdSupport
Advanced Commerce API
AGL
Analytics Reports
App Clips
App Data Transfer
App Intents
App License Delivery SDK
App Store Connect API
App Store Receipts
App Store Server API
App Store Server Notifications
App Tracking Transparency
AppKit
Apple Archive
Apple CryptoKit
Apple Maps Server API
Apple Music API
Apple Music Feed
Apple News
Apple Pay Merchant Token Management API
Apple Pay Web Merchant Registration API
Apple Pencil
Apple Search Ads
Apple silicon
Application Services
ARKit
Assets Library
Assignables
Audio Toolbox
Audio Unit
AudioDriverKit
Authentication Services
Automated Device Enrollment
Automatic Assessment Configuration
Automator
AVFAudio
AVFoundation
AVKit
AVRouting
Background Assets
Background Tasks
BlockStorageDeviceDriverKit
BrowserEngineCore
BrowserEngineKit
BrowserKit
Bundle Resources
CallKit
CareKit
CarKey
CarPlay
CFNetwork
Cinematic
CKTool JS
ClassKit
ClassKit Catalog API
ClockKit
CloudKit
CloudKit JS
Collaboration
ColorSync
Combine
Compositor Services
Compression
ContactProvider
Contacts
Contacts UI
Core Animation
Core Audio
Core Audio Types
Core Bluetooth
Core Data
Core Foundation
Core Graphics
Core Haptics
Core HID
Core Image
Core Location
Core Location UI
Core Media
Core Media I/O
Core MIDI
Core ML
Core Motion
Core NFC
Core Services
Core Spotlight
Core Telephony
Core Text
Core Transferable
Core Video
Core WLAN
CoreAudioKit
Create ML
Create ML Components
CryptoTokenKit
Darwin Notify
DataDetection
Developer Tools Support
Device Activity
Device Management
DeviceCheck
DeviceDiscoveryExtension
DeviceDiscoveryUI
Disk Arbitration
Dispatch
Distributed
dnssd
DocC
DockKit
DriverKit
Endpoint Security
Enterprise Program API
EventKit
EventKit UI
Exception Handling
Execution Policy
Exposure Notification
ExtensionFoundation
ExtensionKit
External Accessory
External Purchase Server API
Family Controls
File Provider
File Provider UI
FinanceKit
FinanceKitUI
Finder Sync
Force Feedback
Foundation
FSKit
Game Controller
GameKit
GameplayKit
GLKit
Group Activities
GSS
HealthKit
HIDDriverKit
HomeKit
HTTP Live Streaming
Human Interface Guidelines
hvf
Hypervisor
iAd
Image I/O
Image Playground
ImageCaptureCore
InputMethodKit
Installer JS
IOBluetooth
IOBluetooth UI
IOKit
iOS & iPadOS Release Notes
IOSurface
IOUSBHost
iTunes Library
iWork Document Exporting API
JavaScriptCore
Journaling Suggestions
Kernel
Kernel Management
Latent Semantic Mapping
LightweightCodeRequirements
Link Presentation
LiveCommunicationKit
LivePhotosKit JS
Local Authentication
Local Authentication Embedded UI
LockedCameraCapture
Mac Catalyst
macOS Release Notes
MailKit
Managed App Distribution
Managed Settings
Managed Settings UI
ManagedApp
MapKit
MapKit JS
Maps Web Snapshots
MarketplaceKit
Matter
MatterSupport
Media Accessibility
Media Library
Media Player
Media Setup
Media Toolbox
MediaExtension
Message UI
Messages
Metal
Metal Performance Shaders
Metal Performance Shaders Graph
MetalFX
MetalKit
MetricKit
MIDIDriverKit
ML Compute
Model I/O
Multipeer Connectivity
MusicKit
MusicKitJS
Natural Language
Nearby Interaction
Network
Network Extension
NetworkingDriverKit
Notary API
Notification Center
Objective-C Runtime
Observation
Open Directory
os
OSLog
PackageDescription
Paravirtualized Graphics
PassKit (Apple Pay and Wallet)
PCIDriverKit
PDFKit
PencilKit
PHASE
PhotoKit
Playground Bluetooth
Playground Support
Preference Panes
Professional Video Applications
ProximityReader
Push to Talk
PushKit
Quartz
Quick Look
Quick Look Thumbnailing
QuickLook UI
QuickTime File Format
RealityKit
RegexBuilder
ReplayKit
ResearchKit
RoomPlan
Roster API
Safari app extensions
Safari Developer Features
Safari Release Notes
Safari Services
SafetyKit
SceneKit
Screen Saver
Screen Time
ScreenCaptureKit
Scripting Bridge
SCSIControllerDriverKit
SCSIPeripheralsDriverKit
SecureElementCredential
Security
Security Foundation
Security Interface
SensitiveContentAnalysis
SensorKit
SerialDriverKit
Service Management
ShaderGraph
Shared With You
ShazamKit
Sign in with Apple
simd
Siri Event Suggestions Markup
SiriKit
SiriKit Cloud Media
SKAdNetwork for Web Ads
SMS and Call Reporting
Social
Sound Analysis
Spatial
Speech
SpriteKit
StoreKit
StoreKit Test
Swift
Swift Charts
Swift packages
Swift Playgrounds
Swift Testing
SwiftData
SwiftUI
Symbols
Synchronization
System
System Configuration
System Extensions
TabletopKit
Tabular Data
Technology Updates
Technotes
Thread Network
TipKit
Translation
TV Services
TVML
tvOS Release Notes
TVUIKit
UIKit
Uniform Type Identifiers
USBDriverKit
USBSerialDriverKit
User Notifications
User Notifications UI
Video Subscriber Account
Video Toolbox
Virtualization
Vision
VisionKit
visionOS
visionOS Release Notes
vmnet
Wallet Orders
Wallet Passes
Watch Connectivity
WatchKit
watchOS apps
watchOS Release Notes
WeatherKit
WeatherKit REST API
WebKit
WebKit JS
WidgetKit
WorkoutKit
Xcode
Xcode Cloud
Xcode Release Notes
XcodeKit
xcselect
XCTest
XCUIAutomation
XPC""".strip()

def title_to_framework_id(title: str) -> str:
    """Convert framework title to likely URL identifier."""
    # Common mappings
    mappings = {
        "Address Book": "addressbook",
        "Address Book UI": "addressbookui",
        "Core Animation": "quartzcore",  # Core Animation is in QuartzCore
        "Core Audio": "coreaudio",
        "Core Audio Types": "coreaudiotypes",
        "Core Bluetooth": "corebluetooth",
        "Core Data": "coredata",
        "Core Foundation": "corefoundation",
        "Core Graphics": "coregraphics",
        "Core Haptics": "corehaptics",
        "Core HID": "corehid",
        "Core Image": "coreimage",
        "Core Location": "corelocation",
        "Core Location UI": "corelocationui",
        "Core Media": "coremedia",
        "Core Media I/O": "coremediaio",
        "Core MIDI": "coremidi",
        "Core ML": "coreml",
        "Core Motion": "coremotion",
        "Core NFC": "corenfc",
        "Core Services": "coreservices",
        "Core Spotlight": "corespotlight",
        "Core Telephony": "coretelephony",
        "Core Text": "coretext",
        "Core Transferable": "coretransferable",
        "Core Video": "corevideo",
        "Core WLAN": "corewlan",
        "Create ML": "createml",
        "Create ML Components": "createmlcomponents",
        "Audio Toolbox": "audiotoolbox",
        "Audio Unit": "audiounit",
        "Game Controller": "gamecontroller",
        "Image I/O": "imageio",
        "Metal Performance Shaders": "metalperformanceshaders",
        "Metal Performance Shaders Graph": "metalperformanceshadersgraph",
        "Natural Language": "naturallanguage",
        "Nearby Interaction": "nearbyinteraction",
        "Network Extension": "networkextension",
        "User Notifications": "usernotifications",
        "User Notifications UI": "usernotificationsui",
        "External Accessory": "externalaccessory",
        "Local Authentication": "localauthentication",
        "PassKit (Apple Pay and Wallet)": "passkit",
        "Quick Look": "quicklook",
        "Quick Look Thumbnailing": "quicklookthumbnailing",
        "Watch Connectivity": "watchconnectivity",
        "Video Toolbox": "videotoolbox",
        "Media Player": "mediaplayer",
        "Message UI": "messageui",
        "Contacts UI": "contactsui",
        "EventKit UI": "eventkitui",
        "Multipeer Connectivity": "multipeerconnectivity",
        "Social": "social",
        "Sound Analysis": "soundanalysis",
        "Push to Talk": "pushtotalk",
        "Shared With You": "sharedwithyou",
        "Background Tasks": "backgroundtasks",
        "App Tracking Transparency": "apptrackingtransparency",
        "Authentication Services": "authenticationservices",
        "Safari Services": "safariservices",
        "App Store Connect API": "appstoreconnectapi",
        "Sign in with Apple": "signinwithapple",
        "Objective-C Runtime": "objectivec",
        "System Configuration": "systemconfiguration",
        "System Extensions": "systemextensions",
        "Uniform Type Identifiers": "uniformtypeidentifiers",
        "Bundle Resources": "bundleresources",
        "Swift Charts": "charts",
        "Apple CryptoKit": "cryptokit",
        "File Provider": "fileprovider",
        "File Provider UI": "fileproviderui",
        "Link Presentation": "linkpresentation",
        "Screen Time": "screentime",
        "Device Management": "devicemanagement",
        "Professional Video Applications": "professionalvideoapplications",
        "Sensitive Content Analysis": "sensitivecontentanalysis",
        "Thread Network": "threadnetwork",
        "TV Services": "tvservices",
        "Video Subscriber Account": "videosubscriberaccount",
        "WeatherKit REST API": "weatherkitrestapi",
        "Wallet Orders": "walletorders",
        "Wallet Passes": "walletpasses",
        "App Intents": "appintents",
    }
    
    if title in mappings:
        return mappings[title]
    
    # Convert title to lowercase identifier
    # Remove special characters and spaces
    identifier = re.sub(r'[^\w\s]', '', title.lower())
    identifier = re.sub(r'\s+', '', identifier)
    
    # Handle special cases
    identifier = identifier.replace('&', '').replace('api', '').replace('js', '').replace('ui', '')
    
    return identifier

def categorize_frameworks() -> Dict[str, List[Dict[str, str]]]:
    """Categorize the manual framework list."""
    
    frameworks_by_category = {
        "User Interface & App Frameworks": [],
        "Graphics, Games & Media": [],
        "System & Low-Level": [],
        "Web & JavaScript": [],
        "Machine Learning & AI": [],
        "Health & Fitness": [],
        "Augmented Reality & Spatial": [],
        "Business & Enterprise": [],
        "Developer Tools & Testing": [],
        "APIs & Web Services": [],
        "Hardware & Drivers": [],
        "Security & Authentication": [],
        "Networking & Communication": [],
        "Legacy & Deprecated": []
    }
    
    # Parse manual list
    manual_frameworks = [f.strip() for f in MANUAL_FRAMEWORKS.split('\n') if f.strip()]
    
    # Categorization rules
    ui_keywords = ['ui', 'kit', 'swiftui', 'uikit', 'appkit', 'widget', 'pencil', 'accessibility', 'contacts ui', 'eventkit ui']
    graphics_keywords = ['metal', 'sprite', 'scene', 'game', 'av', 'core animation', 'core graphics', 'core image', 'core video', 'audio', 'media', 'photo', 'image', 'video', 'cinematic', 'phase']
    system_keywords = ['core', 'foundation', 'dispatch', 'os', 'kernel', 'driver', 'io', 'system', 'disk', 'hypervisor', 'virtualization']
    web_keywords = ['js', 'javascript', 'webkit', 'safari', 'web', 'browser']
    ml_keywords = ['ml', 'coreml', 'create ml', 'natural language', 'speech', 'vision', 'translation']
    health_keywords = ['health', 'care', 'research', 'workout']
    ar_keywords = ['ar', 'reality', 'room', 'spatial', 'visionos']
    business_keywords = ['store', 'pay', 'commerce', 'enterprise', 'business', 'account', 'receipt', 'purchase']
    dev_keywords = ['xcode', 'test', 'docc', 'package', 'swift testing', 'xcui', 'metric']
    api_keywords = ['api', 'rest', 'server', 'reports', 'notification']
    hardware_keywords = ['usb', 'hid', 'scsi', 'pci', 'midi', 'serial', 'block', 'bluetooth', 'nfc', 'accessory']
    security_keywords = ['security', 'crypto', 'authentication', 'local auth', 'endpoint']
    network_keywords = ['network', 'call', 'message', 'multipeer', 'push', 'live']
    legacy_keywords = ['address book', 'glkit', 'iad', 'newsstand', 'social', 'assets library']
    
    for framework_title in manual_frameworks:
        framework_id = title_to_framework_id(framework_title)
        framework_lower = framework_title.lower()
        
        framework_info = {
            "id": framework_id,
            "title": framework_title,
            "url": f"https://developer.apple.com/documentation/{framework_id}",
            "priority": "medium"  # Default priority
        }
        
        # Categorize based on keywords
        if any(keyword in framework_lower for keyword in legacy_keywords):
            frameworks_by_category["Legacy & Deprecated"].append(framework_info)
            framework_info["priority"] = "very_low"
        elif any(keyword in framework_lower for keyword in ui_keywords):
            frameworks_by_category["User Interface & App Frameworks"].append(framework_info)
            framework_info["priority"] = "high" if framework_title in ['SwiftUI', 'UIKit', 'AppKit', 'WidgetKit'] else "medium"
        elif any(keyword in framework_lower for keyword in graphics_keywords):
            frameworks_by_category["Graphics, Games & Media"].append(framework_info)
            framework_info["priority"] = "high" if framework_title in ['Metal', 'AVFoundation', 'Core Graphics'] else "medium"
        elif any(keyword in framework_lower for keyword in web_keywords):
            frameworks_by_category["Web & JavaScript"].append(framework_info)
            framework_info["priority"] = "high" if framework_title == 'WebKit' else "medium"
        elif any(keyword in framework_lower for keyword in ml_keywords):
            frameworks_by_category["Machine Learning & AI"].append(framework_info)
            framework_info["priority"] = "high" if framework_title in ['Core ML', 'Vision'] else "medium"
        elif any(keyword in framework_lower for keyword in health_keywords):
            frameworks_by_category["Health & Fitness"].append(framework_info)
            framework_info["priority"] = "high" if framework_title == 'HealthKit' else "medium"
        elif any(keyword in framework_lower for keyword in ar_keywords):
            frameworks_by_category["Augmented Reality & Spatial"].append(framework_info)
            framework_info["priority"] = "high" if framework_title in ['ARKit', 'RealityKit'] else "medium"
        elif any(keyword in framework_lower for keyword in business_keywords):
            frameworks_by_category["Business & Enterprise"].append(framework_info)
            framework_info["priority"] = "medium" if framework_title in ['StoreKit', 'PassKit'] else "low"
        elif any(keyword in framework_lower for keyword in dev_keywords):
            frameworks_by_category["Developer Tools & Testing"].append(framework_info)
            framework_info["priority"] = "high" if framework_title == 'XCTest' else "medium"
        elif any(keyword in framework_lower for keyword in api_keywords):
            frameworks_by_category["APIs & Web Services"].append(framework_info)
            framework_info["priority"] = "low"
        elif any(keyword in framework_lower for keyword in hardware_keywords):
            frameworks_by_category["Hardware & Drivers"].append(framework_info)
            framework_info["priority"] = "low"
        elif any(keyword in framework_lower for keyword in security_keywords):
            frameworks_by_category["Security & Authentication"].append(framework_info)
            framework_info["priority"] = "medium"
        elif any(keyword in framework_lower for keyword in network_keywords):
            frameworks_by_category["Networking & Communication"].append(framework_info)
            framework_info["priority"] = "medium"
        elif any(keyword in framework_lower for keyword in system_keywords):
            frameworks_by_category["System & Low-Level"].append(framework_info)
            framework_info["priority"] = "high" if framework_title in ['Foundation', 'Combine', 'Swift'] else "medium"
        else:
            frameworks_by_category["System & Low-Level"].append(framework_info)  # Default category
    
    return frameworks_by_category

def main():
    print("Apple Frameworks - Comprehensive List (Based on Manual Collection)")
    print("=" * 80)
    
    frameworks_by_category = categorize_frameworks()
    
    # Count totals
    total_frameworks = sum(len(frameworks) for frameworks in frameworks_by_category.values())
    manual_count = len([f.strip() for f in MANUAL_FRAMEWORKS.split('\n') if f.strip()])
    
    print(f"Manual list count: {manual_count}")
    print(f"Processed frameworks: {total_frameworks}")
    print()
    
    # Print by category
    for category, frameworks in frameworks_by_category.items():
        if frameworks:  # Only show categories with frameworks
            print(f"{category} ({len(frameworks)} frameworks):")
            print("-" * 50)
            
            # Group by priority within category
            by_priority = {}
            for fw in frameworks:
                priority = fw['priority']
                if priority not in by_priority:
                    by_priority[priority] = []
                by_priority[priority].append(fw)
            
            for priority in ['high', 'medium', 'low', 'very_low']:
                if priority in by_priority:
                    print(f"  {priority.upper()}:")
                    for fw in sorted(by_priority[priority], key=lambda x: x['title']):
                        print(f"    - {fw['title']:35} ({fw['id']})")
            print()
    
    # Flatten for priority analysis
    all_frameworks = []
    for frameworks in frameworks_by_category.values():
        all_frameworks.extend(frameworks)
    
    # Priority summary
    print("PRIORITY SUMMARY:")
    print("=" * 50)
    priorities = {}
    for fw in all_frameworks:
        priority = fw['priority']
        priorities[priority] = priorities.get(priority, 0) + 1
    
    for priority in ['high', 'medium', 'low', 'very_low']:
        if priority in priorities:
            print(f"{priority.upper()}: {priorities[priority]} frameworks")
    
    print("\nRECOMMENDED SCRAPING ORDER:")
    print("=" * 50)
    print("1. HIGH priority: Core frameworks (Foundation, SwiftUI, UIKit, etc.)")
    print("2. MEDIUM priority: Commonly used frameworks")
    print("3. LOW priority: Specialized/less common frameworks")
    print("4. VERY_LOW priority: Legacy/deprecated frameworks")
    
    # Pilot recommendations
    pilot_candidates = [fw for fw in all_frameworks if fw['priority'] == 'high' and 
                       fw['id'] in ['foundation', 'swiftui', 'uikit', 'coredata', 'combine', 'metal']]
    
    print(f"\nPILOT FRAMEWORKS (after WatchKit success):")
    print("-" * 50)
    for i, fw in enumerate(pilot_candidates[:5], 1):
        print(f"{i}. {fw['title']} ({fw['id']})")
    
    # Save comprehensive data
    output = {
        "total_count": len(all_frameworks),
        "manual_list_count": manual_count,
        "by_category": frameworks_by_category,
        "by_priority": {
            priority: [fw for fw in all_frameworks if fw['priority'] == priority]
            for priority in ['high', 'medium', 'low', 'very_low']
        },
        "all_frameworks": all_frameworks,
        "pilot_candidates": pilot_candidates
    }
    
    with open("apple_frameworks_complete.json", "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nComplete framework data saved to: apple_frameworks_complete.json")
    print(f"Ready for systematic scraping of {len(all_frameworks)} frameworks!")

if __name__ == "__main__":
    main()