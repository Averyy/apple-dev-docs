#!/usr/bin/env python3
"""
Automated framework discovery that validates against the manual gold standard.
This helps us catch when Apple adds/removes/changes frameworks.
"""

import asyncio
import json
import re
from typing import Dict, List, Set, Tuple
import httpx
from urllib.parse import urljoin, urlparse
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

# Gold standard manual list (non-deprecated frameworks)
GOLD_STANDARD_FRAMEWORKS = """Accelerate
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

class FrameworkDiscoveryValidator:
    """Discovers frameworks and validates against gold standard."""
    
    def __init__(self):
        self.gold_standard = set(f.strip() for f in GOLD_STANDARD_FRAMEWORKS.split('\n') if f.strip())
        self.discovered_frameworks = set()
        self.client = None
        
    async def __aenter__(self):
        self.client = httpx.AsyncClient(timeout=30.0)
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            await self.client.aclose()
    
    def title_to_framework_id(self, title: str) -> str:
        """Convert framework title to URL identifier."""
        # Handle known mappings first
        mappings = {
            "Core Animation": "quartzcore",
            "Core Audio": "coreaudio", 
            "Core Bluetooth": "corebluetooth",
            "Core Data": "coredata",
            "Core Foundation": "corefoundation",
            "Core Graphics": "coregraphics",
            "Core Image": "coreimage",
            "Core Location": "corelocation",
            "Core ML": "coreml",
            "Core Motion": "coremotion",
            "Core NFC": "corenfc",
            "Game Controller": "gamecontroller",
            "Image I/O": "imageio",
            "Natural Language": "naturallanguage",
            "User Notifications": "usernotifications",
            "External Accessory": "externalaccessory",
            "Local Authentication": "localauthentication",
            "PassKit (Apple Pay and Wallet)": "passkit",
            "Quick Look": "quicklook",
            "App Tracking Transparency": "apptrackingtransparency",
            "Authentication Services": "authenticationservices",
            "Sign in with Apple": "signinwithapple",
            "Metal Performance Shaders": "metalperformanceshaders",
            "Apple CryptoKit": "cryptokit",
            "Address Book": "addressbook",
            "Address Book UI": "addressbookui",
        }
        
        if title in mappings:
            return mappings[title]
        
        # Convert to lowercase, remove special chars, spaces
        identifier = re.sub(r'[^\w\s]', '', title.lower())
        identifier = re.sub(r'\s+', '', identifier)
        return identifier
    
    async def discover_from_technologies_page(self) -> Set[str]:
        """Discover frameworks from main technologies page."""
        discovered = set()
        
        try:
            url = "https://developer.apple.com/tutorials/data/documentation/technologies.json"
            response = await self.client.get(url)
            response.raise_for_status()
            data = json.loads(response.text)
            
            # Extract from sections
            for section in data.get('sections', []):
                for item in section.get('items', []):
                    title = item.get('title', '')
                    if title:
                        discovered.add(title)
            
            # Extract from topicSections 
            for section in data.get('topicSections', []):
                for identifier in section.get('identifiers', []):
                    if 'documentation/' in identifier:
                        # Try to extract title from identifier
                        parts = identifier.split('/')
                        if len(parts) > 0:
                            framework_part = parts[-1]
                            # Convert to title case
                            title = framework_part.replace('-', ' ').title()
                            discovered.add(title)
            
            logger.info(f"Discovered {len(discovered)} frameworks from technologies page")
            
        except Exception as e:
            logger.error(f"Failed to discover from technologies page: {e}")
        
        return discovered
    
    async def discover_from_documentation_index(self) -> Set[str]:
        """Try to discover frameworks from documentation index pages."""
        discovered = set()
        
        # Common documentation index patterns
        index_urls = [
            "https://developer.apple.com/documentation/",
            "https://developer.apple.com/documentation/technologies",
        ]
        
        for url in index_urls:
            try:
                response = await self.client.get(url)
                if response.status_code == 200:
                    # Look for framework links in HTML
                    content = response.text
                    # Extract links to /documentation/framework_name
                    framework_links = re.findall(r'/documentation/([a-zA-Z0-9_-]+)(?:/|"|\s)', content)
                    
                    for framework_id in framework_links:
                        # Convert ID back to likely title
                        title = framework_id.replace('-', ' ').title()
                        discovered.add(title)
                
                logger.info(f"Discovered {len(framework_links)} frameworks from {url}")
                
            except Exception as e:
                logger.error(f"Failed to discover from {url}: {e}")
        
        return discovered
    
    async def discover_from_sitemap(self) -> Set[str]:
        """Try to discover frameworks from Apple's sitemap."""
        discovered = set()
        
        try:
            # Apple may have sitemaps
            sitemap_urls = [
                "https://developer.apple.com/sitemap.xml",
                "https://developer.apple.com/documentation/sitemap.xml"
            ]
            
            for url in sitemap_urls:
                try:
                    response = await self.client.get(url)
                    if response.status_code == 200:
                        content = response.text
                        # Extract documentation URLs
                        doc_urls = re.findall(r'https://developer\.apple\.com/documentation/([a-zA-Z0-9_-]+)', content)
                        
                        for framework_id in doc_urls:
                            title = framework_id.replace('-', ' ').title()
                            discovered.add(title)
                
                except Exception as e:
                    logger.debug(f"Sitemap {url} not accessible: {e}")
        
        except Exception as e:
            logger.error(f"Failed sitemap discovery: {e}")
        
        return discovered
    
    async def verify_framework_exists(self, framework_title: str) -> bool:
        """Verify if a framework documentation page exists."""
        framework_id = self.title_to_framework_id(framework_title)
        url = f"https://developer.apple.com/documentation/{framework_id}"
        
        try:
            response = await self.client.head(url)
            return response.status_code == 200
        except:
            return False
    
    async def discover_all_frameworks(self) -> Set[str]:
        """Comprehensive framework discovery using multiple methods."""
        logger.info("Starting comprehensive framework discovery...")
        
        all_discovered = set()
        
        # Method 1: Technologies page
        tech_frameworks = await self.discover_from_technologies_page()
        all_discovered.update(tech_frameworks)
        logger.info(f"Method 1 (Technologies): {len(tech_frameworks)} frameworks")
        
        # Method 2: Documentation index
        index_frameworks = await self.discover_from_documentation_index()
        all_discovered.update(index_frameworks)
        logger.info(f"Method 2 (Doc Index): {len(index_frameworks)} frameworks")
        
        # Method 3: Sitemap
        sitemap_frameworks = await self.discover_from_sitemap()
        all_discovered.update(sitemap_frameworks)
        logger.info(f"Method 3 (Sitemap): {len(sitemap_frameworks)} frameworks")
        
        # Method 4: Validate gold standard exists
        logger.info("Validating gold standard frameworks...")
        verified_count = 0
        for framework in list(self.gold_standard)[:10]:  # Test first 10 to avoid too many requests
            if await self.verify_framework_exists(framework):
                verified_count += 1
                all_discovered.add(framework)
        
        logger.info(f"Method 4 (Gold Standard): {verified_count}/10 verified")
        
        self.discovered_frameworks = all_discovered
        return all_discovered
    
    def analyze_discovery_results(self) -> Dict:
        """Analyze discovery results against gold standard."""
        
        # Normalize for comparison (case-insensitive, strip spaces)
        gold_normalized = {fw.strip().lower() for fw in self.gold_standard}
        discovered_normalized = {fw.strip().lower() for fw in self.discovered_frameworks}
        
        # Find matches, missing, and extra
        matches = gold_normalized.intersection(discovered_normalized)
        missing_from_discovery = gold_normalized - discovered_normalized
        extra_in_discovery = discovered_normalized - gold_normalized
        
        coverage_percentage = (len(matches) / len(gold_normalized)) * 100 if gold_normalized else 0
        
        return {
            "gold_standard_count": len(self.gold_standard),
            "discovered_count": len(self.discovered_frameworks),
            "matches_count": len(matches),
            "missing_count": len(missing_from_discovery),
            "extra_count": len(extra_in_discovery),
            "coverage_percentage": coverage_percentage,
            "matches": sorted(matches),
            "missing_from_discovery": sorted(missing_from_discovery),
            "extra_in_discovery": sorted(extra_in_discovery)
        }

async def main():
    print("Apple Framework Discovery Validator")
    print("=" * 60)
    print("Discovering frameworks and validating against gold standard...")
    print()
    
    async with FrameworkDiscoveryValidator() as validator:
        # Discover frameworks
        discovered = await validator.discover_all_frameworks()
        
        # Analyze results
        analysis = validator.analyze_discovery_results()
        
        print("DISCOVERY RESULTS:")
        print("=" * 60)
        print(f"Gold Standard Count: {analysis['gold_standard_count']}")
        print(f"Discovered Count: {analysis['discovered_count']}")
        print(f"Matches: {analysis['matches_count']}")
        print(f"Missing from Discovery: {analysis['missing_count']}")
        print(f"Extra in Discovery: {analysis['extra_count']}")
        print(f"Coverage: {analysis['coverage_percentage']:.1f}%")
        print()
        
        if analysis['missing_count'] > 0:
            print("MISSING FROM DISCOVERY (first 20):")
            print("-" * 40)
            for framework in list(analysis['missing_from_discovery'])[:20]:
                print(f"  - {framework}")
            if len(analysis['missing_from_discovery']) > 20:
                print(f"  ... and {len(analysis['missing_from_discovery']) - 20} more")
            print()
        
        if analysis['extra_count'] > 0:
            print("EXTRA IN DISCOVERY (first 20):")
            print("-" * 40)
            for framework in list(analysis['extra_in_discovery'])[:20]:
                print(f"  + {framework}")
            if len(analysis['extra_in_discovery']) > 20:
                print(f"  ... and {len(analysis['extra_in_discovery']) - 20} more")
            print()
        
        # Create comprehensive framework list using gold standard as base
        print("CREATING COMPREHENSIVE FRAMEWORK LIST:")
        print("-" * 40)
        
        # Use gold standard as primary source, add any new discoveries
        comprehensive_frameworks = []
        gold_list = [fw.strip() for fw in GOLD_STANDARD_FRAMEWORKS.split('\n') if fw.strip()]
        
        for framework in gold_list:
            framework_id = validator.title_to_framework_id(framework)
            comprehensive_frameworks.append({
                "id": framework_id,
                "title": framework,
                "url": f"https://developer.apple.com/documentation/{framework_id}",
                "source": "gold_standard",
                "priority": "medium"  # Default, can be refined
            })
        
        # Add any new discoveries not in gold standard
        for framework in analysis['extra_in_discovery']:
            framework_title = framework.title()  # Convert back to title case
            framework_id = validator.title_to_framework_id(framework_title)
            comprehensive_frameworks.append({
                "id": framework_id,
                "title": framework_title,
                "url": f"https://developer.apple.com/documentation/{framework_id}",
                "source": "discovered",
                "priority": "low"  # New discoveries get lower priority initially
            })
        
        print(f"Total frameworks in comprehensive list: {len(comprehensive_frameworks)}")
        
        # Save results
        output = {
            "discovery_analysis": analysis,
            "comprehensive_frameworks": comprehensive_frameworks,
            "discovery_methods_used": [
                "technologies_page",
                "documentation_index", 
                "sitemap",
                "gold_standard_validation"
            ],
            "timestamp": "2025-06-04",
            "total_frameworks": len(comprehensive_frameworks)
        }
        
        with open("framework_discovery_results.json", "w") as f:
            json.dump(output, f, indent=2)
        
        print(f"\nResults saved to: framework_discovery_results.json")
        
        # Recommendations
        print("\nRECOMMENDATIONS:")
        print("=" * 60)
        
        if analysis['coverage_percentage'] < 50:
            print("⚠️  LOW COVERAGE: Discovery methods need improvement")
            print("   Consider adding more discovery endpoints or manual verification")
        elif analysis['coverage_percentage'] < 80:
            print("📍 MEDIUM COVERAGE: Discovery is working but has gaps")
            print("   Review missing frameworks to improve discovery methods")
        else:
            print("✅ GOOD COVERAGE: Discovery methods are working well")
        
        print(f"\n📋 Use comprehensive list of {len(comprehensive_frameworks)} frameworks for scraping")
        print("🔄 Re-run this validator periodically to catch Apple's updates")

if __name__ == "__main__":
    asyncio.run(main())