#!/usr/bin/env python3
"""
Test script to verify platform extraction and summary features work correctly
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from scripts.build_index import VectorIndexBuilder

def test_platform_extraction():
    """Test platform extraction from markdown content"""
    builder = VectorIndexBuilder()
    
    # Test content with multiple platforms
    test_content = """
# Button

**Framework**: SwiftUI  
**Availability**: iOS 13.0+, macOS 10.15+, tvOS 13.0+, watchOS 6.0+, visionOS 1.0+

A control that initiates an action.
"""
    
    platforms = builder._extract_platforms(test_content)
    print(f"✅ Platform extraction test:")
    print(f"   Found platforms: {platforms}")
    print(f"   Expected: ['ios', 'macos', 'tvos', 'watchos', 'visionos']")
    
    expected = {'ios', 'macos', 'tvos', 'watchos', 'visionos'}
    found = set(platforms)
    assert expected == found, f"Platform mismatch: expected {expected}, got {found}"
    print("   ✅ Platform extraction working correctly!\n")

def test_summary_extraction():
    """Test summary extraction from overview section"""
    builder = VectorIndexBuilder()
    
    # Test content with overview
    test_content = """
# SwiftUI

**Framework**: SwiftUI

## Overview

SwiftUI is a modern way to declare user interfaces for any Apple platform. Create beautiful, dynamic apps faster than ever before.

## Topics

### Essentials
"""
    
    summary = builder._extract_summary(test_content)
    print(f"✅ Summary extraction test (with Overview):")
    print(f"   Found summary: {summary}")
    assert summary == "SwiftUI is a modern way to declare user interfaces for any Apple platform.", \
        f"Summary mismatch: {summary}"
    print("   ✅ Summary extraction working correctly!\n")

def test_summary_fallback():
    """Test summary extraction fallback when no overview"""
    builder = VectorIndexBuilder()
    
    # Test content without overview
    test_content = """
# Foundation

The Foundation framework provides a base layer of functionality for apps and frameworks, including data storage and persistence, text processing, date and time calculations, sorting and filtering, and networking.

## Topics

### Numbers, Data, and Basic Values
"""
    
    summary = builder._extract_first_sentence(test_content)
    print(f"✅ Summary extraction test (fallback):")
    print(f"   Found summary: {summary}")
    assert summary and len(summary) > 20, f"Summary too short or missing: {summary}"
    print("   ✅ Summary fallback working correctly!\n")

def test_metadata_extraction():
    """Test complete metadata extraction"""
    builder = VectorIndexBuilder()
    
    # Create a mock file path
    from unittest.mock import Mock
    mock_path = Mock()
    mock_path.relative_to.return_value = Path("SwiftUI/Button.md")
    mock_path.parts = ["SwiftUI", "Button.md"]
    mock_path.stem = "Button"
    
    test_content = """
# Button

**Framework**: SwiftUI  
**Availability**: iOS 13.0+, macOS 10.15+

A control that initiates an action.

## Overview

Use buttons to allow users to initiate actions. You create a button with a label and an action.
"""
    
    metadata = builder._extract_metadata(mock_path, test_content)
    
    print(f"✅ Full metadata extraction test:")
    print(f"   Framework: {metadata['framework']} (expected: SwiftUI)")
    print(f"   API name: {metadata['api_name']} (expected: Button)")
    print(f"   Platforms: {metadata['platforms']} (expected: ['ios', 'macos'])")
    print(f"   Is framework main: {metadata['is_framework_main']} (expected: False)")
    
    assert metadata['framework'] == 'SwiftUI', f"Framework mismatch: {metadata['framework']}"
    assert metadata['api_name'] == 'Button', f"API name mismatch: {metadata['api_name']}"
    assert set(metadata['platforms']) == {'ios', 'macos'}, f"Platform mismatch: {metadata['platforms']}"
    assert metadata['is_framework_main'] == False, f"Is framework main mismatch: {metadata['is_framework_main']}"
    
    print("   ✅ All metadata extraction working correctly!\n")

def main():
    """Run all tests"""
    print("🧪 Testing embedding feature enhancements...\n")
    
    try:
        test_platform_extraction()
        test_summary_extraction()
        test_summary_fallback()
        test_metadata_extraction()
        
        print("✅ All tests passed! The embedding features are working correctly.")
        print("\n📝 Next steps:")
        print("1. Run the build script with --force to rebuild the vectorstore:")
        print("   cd mcp-server && python scripts/build_index.py --force")
        print("2. This will embed all documents with the new metadata")
        print("3. The MCP server will then have platform filtering and framework summaries")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()