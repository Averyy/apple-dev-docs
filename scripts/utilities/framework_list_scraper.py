#!/usr/bin/env python3
"""
DEDICATED Framework List Scraper
Hits Apple's technologies.json endpoint directly to get ALL 340+ frameworks
SEPARATE from content scraping - this is ONLY for framework discovery
"""

import asyncio
import json
import httpx
from typing import List, Dict, Set
from pathlib import Path

class AppleFrameworkListScraper:
    """Dedicated scraper ONLY for getting the complete framework list from Apple's API"""
    
    # Apple's official framework list endpoint
    TECHNOLOGIES_URL = "https://developer.apple.com/tutorials/data/documentation/technologies.json"
    
    def __init__(self):
        self.client = httpx.AsyncClient(
            timeout=30.0,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
        )
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()
    
    async def fetch_all_frameworks(self) -> List[Dict[str, str]]:
        """
        Fetch ALL frameworks directly from Apple's technologies.json endpoint
        This gives us the complete authoritative list of 340+ frameworks
        """
        print(f"🚀 Fetching complete framework list from: {self.TECHNOLOGIES_URL}")
        
        try:
            response = await self.client.get(self.TECHNOLOGIES_URL)
            response.raise_for_status()
            
            data = response.json()
            print(f"✅ Successfully fetched JSON data: {len(response.text)} chars")
            
            # Extract frameworks from the JSON structure
            frameworks = self._extract_frameworks_from_json(data)
            
            print(f"🎯 Extracted {len(frameworks)} frameworks from technologies.json")
            return frameworks
            
        except Exception as e:
            print(f"❌ Error fetching framework list: {e}")
            return []
    
    def _extract_frameworks_from_json(self, data: Dict) -> List[Dict[str, str]]:
        """Extract framework information from technologies.json structure"""
        frameworks = []
        
        # The JSON structure contains references to all technologies
        references = data.get('references', {})
        
        for ref_id, ref_data in references.items():
            # Skip non-technology references
            url = ref_data.get('url', '')
            if not url.startswith('/documentation/'):
                continue
            
            # Extract path after /documentation/
            path = url.replace('/documentation/', '')
            
            # IMPORTANT: Only include top-level frameworks (no sub-paths)
            # This filters out entries like /documentation/accelerate/simd
            if '/' in path:
                # Skip sub-modules
                continue
            
            # Extract framework info
            title = ref_data.get('title', '')
            
            if title and path:
                # Use the exact casing from the URL path as the framework ID
                framework_id = path
                
                frameworks.append({
                    'id': framework_id,
                    'title': title,
                    'url': url,
                    'href': url,  # For compatibility
                    'type': ref_data.get('type', 'topic')
                })
        
        # Remove duplicates by lowercase ID (but preserve original casing)
        seen_lowercase = {}
        unique_frameworks = []
        
        for fw in frameworks:
            # Use lowercase for deduplication check
            lowercase_id = fw['id'].lower()
            
            if lowercase_id not in seen_lowercase:
                seen_lowercase[lowercase_id] = True
                unique_frameworks.append(fw)
            else:
                # Skip duplicate with different casing
                pass
        
        # Sort alphabetically by title (not ID, since IDs have inconsistent casing)
        unique_frameworks.sort(key=lambda x: x['title'].lower())
        
        print(f"📊 Extracted {len(unique_frameworks)} top-level frameworks (filtered {len(frameworks) - len(unique_frameworks)} sub-modules/duplicates)")
        
        return unique_frameworks
    
    async def save_framework_list(self, frameworks: List[Dict[str, str]], filename: str = "complete_apple_frameworks.json"):
        """Save the complete framework list to JSON file"""
        
        output = {
            "metadata": {
                "source": "Apple technologies.json API",
                "url": self.TECHNOLOGIES_URL, 
                "total_frameworks": len(frameworks),
                "description": "Complete list of Apple frameworks from official API"
            },
            "frameworks": frameworks,
            "framework_ids": [fw['id'] for fw in frameworks],
            "framework_titles": [fw['title'] for fw in frameworks]
        }
        
        output_path = Path(filename)
        with open(output_path, 'w') as f:
            json.dump(output, f, indent=2)
        
        print(f"💾 Saved {len(frameworks)} frameworks to: {filename}")
        return filename
    
    def compare_with_existing_lists(self, frameworks: List[Dict[str, str]]) -> Dict:
        """Compare with existing framework lists to see coverage"""
        
        # Load existing comprehensive list if it exists
        try:
            with open('comprehensive_nav_frameworks.json', 'r') as f:
                nav_data = json.load(f)
                nav_frameworks = nav_data.get('framework_ids', [])
        except FileNotFoundError:
            nav_frameworks = []
        
        # Load manual README list
        manual_list = [
            "Accelerate", "Accessibility", "AccessorySetupKit", "Account & Organizational Data Sharing",
            "Account Data Transfer", "Accounts", "ActivityKit", "AdAttributionKit", "Address Book",
            "Address Book UI", "AdServices", "AdSupport", "Advanced Commerce API", "AGL",
            "Analytics Reports", "App Clips", "App Data Transfer", "App Intents",
            "App License Delivery SDK", "App Store Connect API", "App Store Receipts",
            "App Store Server API", "App Store Server Notifications", "App Tracking Transparency",
            "AppKit", "Apple Archive", "Apple CryptoKit", "Apple Maps Server API",
            "Apple Music API", "Apple Music Feed", "Apple News", "Apple Pay Merchant Token Management API",
            "Apple Pay Web Merchant Registration API", "Apple Pencil", "Apple Search Ads", "Apple silicon",
            "Application Services", "ARKit", "Assets Library", "Assignables", "Audio Toolbox",
            "Audio Unit", "AudioDriverKit", "Authentication Services", "Automated Device Enrollment",
            "Automatic Assessment Configuration", "Automator", "AVFAudio", "AVFoundation", "AVKit",
            "AVRouting", "Background Assets", "Background Tasks", "BlockStorageDeviceDriverKit",
            "BrowserEngineCore", "BrowserEngineKit", "BrowserKit", "Bundle Resources", "CallKit",
            "CareKit", "CarKey", "CarPlay", "CFNetwork", "Cinematic", "CKTool JS", "ClassKit",
            "ClassKit Catalog API", "ClockKit", "CloudKit", "CloudKit JS", "Collaboration",
            "ColorSync", "Combine", "Compositor Services", "Compression", "ContactProvider",
            "Contacts", "Contacts UI", "Core Animation", "Core Audio", "Core Audio Types",
            "Core Bluetooth", "Core Data", "Core Foundation", "Core Graphics", "Core Haptics",
            "Core HID", "Core Image", "Core Location", "Core Location UI", "Core Media",
            "Core Media I/O", "Core MIDI", "Core ML", "Core Motion", "Core NFC", "Core Services",
            "Core Spotlight", "Core Telephony", "Core Text", "Core Transferable", "Core Video",
            "Core WLAN", "CoreAudioKit", "Create ML", "Create ML Components", "CryptoTokenKit",
            "SwiftUI", "UIKit", "Metal", "Foundation", "Swift"  # Major frameworks
        ]
        
        api_titles = [fw['title'] for fw in frameworks]
        api_ids = [fw['id'] for fw in frameworks]
        
        # Find matches
        found_in_api = []
        missing_from_api = []
        
        for manual_name in manual_list:
            # Check both title and ID matches
            title_match = manual_name in api_titles
            id_match = any(manual_name.lower().replace(" ", "").replace("-", "") 
                          in fw_id.lower().replace("-", "") for fw_id in api_ids)
            
            if title_match or id_match:
                found_in_api.append(manual_name)
            else:
                missing_from_api.append(manual_name)
        
        return {
            "api_total": len(frameworks),
            "nav_total": len(nav_frameworks),
            "manual_total": len(manual_list),
            "found_in_api": len(found_in_api),
            "missing_from_api": len(missing_from_api),
            "api_coverage_percent": round((len(found_in_api) / len(manual_list)) * 100, 1),
            "missing_frameworks": missing_from_api[:20],  # Show first 20
            "sample_api_frameworks": api_titles[:10]
        }

async def main():
    """Main function to fetch and save the complete Apple framework list"""
    
    print("🍎 Apple Framework List Scraper - DEDICATED FRAMEWORK DISCOVERY")
    print("=" * 70)
    print("This scraper ONLY gets the framework list from technologies.json")
    print("Separate from content scraping!")
    print()
    
    async with AppleFrameworkListScraper() as scraper:
        # Fetch complete framework list from Apple's API
        frameworks = await scraper.fetch_all_frameworks()
        
        if not frameworks:
            print("❌ Failed to fetch frameworks")
            return
        
        # Save to file
        filename = await scraper.save_framework_list(frameworks)
        
        # Compare with existing lists
        comparison = scraper.compare_with_existing_lists(frameworks)
        
        # Display results
        print(f"\n📊 FRAMEWORK LIST COMPARISON:")
        print(f"API (technologies.json): {comparison['api_total']} frameworks")
        print(f"Navigation scraper: {comparison['nav_total']} frameworks")
        print(f"Manual README list: {comparison['manual_total']} frameworks")
        print(f"API covers {comparison['api_coverage_percent']}% of manual list")
        
        if comparison['missing_frameworks']:
            print(f"\n❌ Missing from API (first 10):")
            for missing in comparison['missing_frameworks'][:10]:
                print(f"  - {missing}")
        
        print(f"\n✅ COMPLETE: Use {filename} as the authoritative framework list!")
        print("Now use the separate JSON content scraper for individual framework pages.")

if __name__ == "__main__":
    asyncio.run(main())