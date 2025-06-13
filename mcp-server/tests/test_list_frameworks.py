#!/usr/bin/env python3
"""
Test the list_frameworks functionality
"""

import asyncio
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Set up environment if needed
if not os.getenv("OPENAI_API_KEY"):
    print("Loading .env file...")
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")

# Import after environment is set up
from server.mcp_server import list_frameworks_handler, get_rag_engine


async def test_list_frameworks():
    """Test list_frameworks with different parameters"""
    
    # Initialize RAG engine first
    print("Initializing RAG engine...")
    rag = get_rag_engine()
    stats = rag.get_stats()
    print(f"✅ RAG engine ready: {stats['total_documents']:,} documents")
    print()
    
    # Test 1: No platform (should show ALL frameworks)
    print("=" * 60)
    print("Test 1: list_frameworks() - No platform specified")
    print("Expected: All 360+ frameworks with platform indicators")
    print("=" * 60)
    result = await list_frameworks_handler()
    lines = result.split('\n')
    print(f"First 20 lines of output:")
    for line in lines[:20]:
        print(line)
    print("...")
    print(f"Total lines: {len(lines)}")
    
    # Count frameworks
    framework_count = sum(1 for line in lines if line.strip().startswith('- **'))
    print(f"Total frameworks listed: {framework_count}")
    print()
    
    # Test 2: Platform = "all" (should be same as no platform)
    print("=" * 60)
    print('Test 2: list_frameworks(platform="all")')
    print("Expected: Same as Test 1")
    print("=" * 60)
    result_all = await list_frameworks_handler("all")
    if result == result_all:
        print("✅ Results match Test 1 (as expected)")
    else:
        print("❌ Results differ from Test 1!")
        print(f"Length difference: {len(result)} vs {len(result_all)}")
    print()
    
    # Test 3: Platform = "ios" (should show only iOS frameworks)
    print("=" * 60)
    print('Test 3: list_frameworks(platform="ios")')
    print("Expected: Only iOS frameworks with descriptions")
    print("=" * 60)
    result_ios = await list_frameworks_handler("ios")
    lines_ios = result_ios.split('\n')
    print(f"First 20 lines of output:")
    for line in lines_ios[:20]:
        print(line)
    print("...")
    
    # Check that it's iOS-specific
    if "# IOS Frameworks" in result_ios:
        print("✅ iOS-specific header found")
    else:
        print("❌ Missing iOS-specific header")
    
    ios_framework_count = sum(1 for line in lines_ios if line.strip().startswith('- **'))
    print(f"Total iOS frameworks: {ios_framework_count}")
    print()
    
    # Test 4: Invalid platform (should still work)
    print("=" * 60)
    print('Test 4: list_frameworks(platform="invalid")')
    print("Expected: Empty or error-like response")
    print("=" * 60)
    result_invalid = await list_frameworks_handler("invalid")
    lines_invalid = result_invalid.split('\n')
    print(f"First 10 lines of output:")
    for line in lines_invalid[:10]:
        print(line)
    invalid_framework_count = sum(1 for line in lines_invalid if line.strip().startswith('- **'))
    print(f"Total frameworks: {invalid_framework_count}")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"No platform specified: {framework_count} frameworks")
    print(f"Platform='all': {'Same as no platform' if result == result_all else 'Different!'}")
    print(f"Platform='ios': {ios_framework_count} frameworks")
    print(f"Platform='invalid': {invalid_framework_count} frameworks")
    
    # Check for the specific bug
    if "IPADOS" in result and "ipados" not in result.lower():
        print("\n⚠️  WARNING: Found 'IPADOS' in output when no platform specified!")
        print("This suggests the default platform is being set incorrectly.")


if __name__ == "__main__":
    asyncio.run(test_list_frameworks())