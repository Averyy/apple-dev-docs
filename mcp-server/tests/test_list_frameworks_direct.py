#!/usr/bin/env python3
"""
Direct test of list_frameworks functionality
"""

import os
import sys
from pathlib import Path

# Add parent and server directories to path
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))
sys.path.insert(0, str(parent_dir / "server"))

# Load environment
from dotenv import load_dotenv
load_dotenv(parent_dir / ".env")

# Now we can import
from rag import SimpleRAG


def test_list_frameworks():
    """Test the RAG engine's list_frameworks method directly"""
    
    print("Initializing RAG engine...")
    rag = SimpleRAG()
    stats = rag.get_stats()
    print(f"✅ RAG engine ready: {stats['total_documents']:,} documents")
    print()
    
    # Test 1: No platform (should show ALL frameworks)
    print("=" * 60)
    print("Test 1: rag.list_frameworks() - No platform specified")
    print("Expected: All frameworks")
    print("=" * 60)
    result = rag.list_frameworks()
    print(f"Total frameworks: {result['total_frameworks']}")
    print(f"Framework list length: {len(result['frameworks'])}")
    print(f"First 10 frameworks: {result['frameworks'][:10]}")
    
    # Check if platform grouping exists
    if 'frameworks_by_platform' in result:
        print("\nFrameworks by platform:")
        for platform, frameworks in result['frameworks_by_platform'].items():
            print(f"  {platform}: {len(frameworks)} frameworks")
    print()
    
    # Test 2: Platform = None (should be same as no args)
    print("=" * 60)
    print("Test 2: rag.list_frameworks(platform=None)")
    print("Expected: Same as Test 1")
    print("=" * 60)
    result_none = rag.list_frameworks(platform=None)
    if result['total_frameworks'] == result_none['total_frameworks']:
        print("✅ Results match Test 1 (as expected)")
    else:
        print("❌ Results differ from Test 1!")
    print()
    
    # Test 3: Platform = "all" (should be same as no platform)
    print("=" * 60)
    print('Test 3: rag.list_frameworks(platform="all")')
    print("Expected: Same as Test 1")
    print("=" * 60)
    result_all = rag.list_frameworks(platform="all")
    if result['total_frameworks'] == result_all['total_frameworks']:
        print("✅ Results match Test 1 (as expected)")
    else:
        print("❌ Results differ from Test 1!")
    print()
    
    # Test 4: Platform = "ios" (should show only iOS frameworks)
    print("=" * 60)
    print('Test 4: rag.list_frameworks(platform="ios")')
    print("Expected: Only iOS frameworks")
    print("=" * 60)
    result_ios = rag.list_frameworks(platform="ios")
    print(f"Total frameworks: {result_ios['total_frameworks']}")
    print(f"Platform: {result_ios.get('platform', 'Not specified')}")
    print(f"First 10 iOS frameworks: {result_ios['frameworks'][:10] if result_ios['frameworks'] else 'None'}")
    
    # Test 5: Platform = "ipados" 
    print("\n" + "=" * 60)
    print('Test 5: rag.list_frameworks(platform="ipados")')
    print("Expected: Only iPadOS frameworks")
    print("=" * 60)
    result_ipados = rag.list_frameworks(platform="ipados")
    print(f"Total frameworks: {result_ipados['total_frameworks']}")
    print(f"Platform: {result_ipados.get('platform', 'Not specified')}")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"No platform: {result['total_frameworks']} frameworks")
    print(f"platform=None: {result_none['total_frameworks']} frameworks")
    print(f"platform='all': {result_all['total_frameworks']} frameworks")
    print(f"platform='ios': {result_ios['total_frameworks']} frameworks")
    print(f"platform='ipados': {result_ipados['total_frameworks']} frameworks")
    
    # Debug: Check what happens with empty string
    print("\n" + "=" * 60)
    print("DEBUG: Testing edge cases")
    print("=" * 60)
    result_empty = rag.list_frameworks(platform="")
    print(f"platform='': {result_empty['total_frameworks']} frameworks")


if __name__ == "__main__":
    test_list_frameworks()