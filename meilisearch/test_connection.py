#!/usr/bin/env python3
"""Test Meilisearch connection and basic operations."""

import os
import sys
import time
from typing import Dict, Any
import requests
from datetime import datetime

# Load environment variables
MEILISEARCH_URL = os.getenv('MEILISEARCH_URL', 'http://localhost:7700')
MEILI_MASTER_KEY = os.getenv('MEILI_MASTER_KEY', 'local_test_key')

def test_connection() -> bool:
    """Test basic connection to Meilisearch."""
    try:
        response = requests.get(f"{MEILISEARCH_URL}/health")
        if response.status_code == 200:
            print("✅ Meilisearch is healthy")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def test_version() -> bool:
    """Get Meilisearch version info."""
    try:
        response = requests.get(
            f"{MEILISEARCH_URL}/version",
            headers={"Authorization": f"Bearer {MEILI_MASTER_KEY}"}
        )
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Meilisearch version: {data.get('pkgVersion', 'unknown')}")
            return True
        else:
            print(f"❌ Version check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Version check failed: {e}")
        return False

def create_test_index() -> bool:
    """Create a test index."""
    try:
        # Create index
        response = requests.post(
            f"{MEILISEARCH_URL}/indexes",
            headers={
                "Authorization": f"Bearer {MEILI_MASTER_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "uid": "test-apple-docs",
                "primaryKey": "id"
            }
        )
        
        if response.status_code in [201, 202]:
            print("✅ Created test index 'test-apple-docs'")
            # Wait for task to complete
            time.sleep(1)
            return True
        elif response.status_code == 409:
            print("ℹ️  Test index already exists")
            return True
        else:
            print(f"❌ Failed to create index: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Index creation failed: {e}")
        return False

def test_document_operations() -> bool:
    """Test adding and searching documents."""
    try:
        # Add test documents
        test_docs = [
            {
                "id": "1",
                "title": "SwiftUI View",
                "framework": "SwiftUI",
                "content": "A type that represents part of your app's user interface.",
                "platforms": ["iOS", "macOS", "tvOS", "watchOS"],
                "url": "https://developer.apple.com/documentation/swiftui/view"
            },
            {
                "id": "2",
                "title": "UIView",
                "framework": "UIKit",
                "content": "An object that manages the content for a rectangular area on the screen.",
                "platforms": ["iOS", "tvOS"],
                "url": "https://developer.apple.com/documentation/uikit/uiview"
            }
        ]
        
        response = requests.post(
            f"{MEILISEARCH_URL}/indexes/test-apple-docs/documents",
            headers={
                "Authorization": f"Bearer {MEILI_MASTER_KEY}",
                "Content-Type": "application/json"
            },
            json=test_docs
        )
        
        if response.status_code == 202:
            print("✅ Added test documents")
            # Wait for indexing
            time.sleep(2)
            
            # Test search
            search_response = requests.post(
                f"{MEILISEARCH_URL}/indexes/test-apple-docs/search",
                headers={
                    "Authorization": f"Bearer {MEILI_MASTER_KEY}",
                    "Content-Type": "application/json"
                },
                json={"q": "View"}
            )
            
            if search_response.status_code == 200:
                results = search_response.json()
                hit_count = len(results.get('hits', []))
                print(f"✅ Search test passed: found {hit_count} results for 'View'")
                return True
            else:
                print(f"❌ Search failed: {search_response.status_code}")
                return False
        else:
            print(f"❌ Failed to add documents: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Document operations failed: {e}")
        return False

def cleanup_test_index() -> bool:
    """Clean up test index."""
    try:
        response = requests.delete(
            f"{MEILISEARCH_URL}/indexes/test-apple-docs",
            headers={"Authorization": f"Bearer {MEILI_MASTER_KEY}"}
        )
        if response.status_code in [202, 404]:
            print("✅ Cleaned up test index")
            return True
        else:
            print(f"⚠️  Cleanup failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"⚠️  Cleanup failed: {e}")
        return False

def main():
    """Run all tests."""
    print(f"\n🔍 Testing Meilisearch at {MEILISEARCH_URL}")
    print(f"   Using key: {'*' * 10}{MEILI_MASTER_KEY[-4:]}\n")
    
    tests = [
        ("Connection", test_connection),
        ("Version", test_version),
        ("Create Index", create_test_index),
        ("Document Operations", test_document_operations),
        ("Cleanup", cleanup_test_index)
    ]
    
    passed = 0
    for name, test_func in tests:
        print(f"\nTesting {name}...")
        if test_func():
            passed += 1
        time.sleep(0.5)
    
    print(f"\n{'='*50}")
    print(f"Tests passed: {passed}/{len(tests)}")
    
    if passed == len(tests):
        print("✅ All tests passed! Meilisearch is ready for use.")
        return 0
    else:
        print("❌ Some tests failed. Please check your configuration.")
        return 1

if __name__ == "__main__":
    sys.exit(main())