#!/usr/bin/env python3
"""
Test TEI embedding functionality
"""
import os
import sys
import time
import requests
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from server.config import TEI_URL, EMBEDDING_BATCH_SIZE


def test_single_embedding():
    """Test single text embedding"""
    print("\n1. Testing single embedding...")
    
    test_text = "SwiftUI is a modern UI framework for iOS development"
    
    try:
        response = requests.post(
            TEI_URL,
            json={"inputs": [test_text]},
            timeout=5
        )
        
        if response.status_code == 200:
            embeddings = response.json()
            print(f"✓ Single embedding successful")
            print(f"  Shape: {len(embeddings)} x {len(embeddings[0])}")
            print(f"  First 5 values: {embeddings[0][:5]}")
            return True
        else:
            print(f"✗ Failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_batch_embedding():
    """Test batch embedding with multiple texts"""
    print("\n2. Testing batch embedding...")
    
    test_texts = [
        "SwiftUI Button view",
        "UIKit UIViewController lifecycle",
        "Core Data persistent storage",
        "Metal shader programming"
    ]
    
    try:
        response = requests.post(
            TEI_URL,
            json={"inputs": test_texts[:EMBEDDING_BATCH_SIZE]},
            timeout=10
        )
        
        if response.status_code == 200:
            embeddings = response.json()
            print(f"✓ Batch embedding successful")
            print(f"  Batch size: {len(embeddings)}")
            print(f"  Embedding dimensions: {len(embeddings[0])}")
            return True
        else:
            print(f"✗ Failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_embedding_speed():
    """Test embedding speed for performance baseline"""
    print("\n3. Testing embedding speed...")
    
    test_texts = [
        f"Test document {i}: This is a sample Apple documentation text about SwiftUI and iOS development"
        for i in range(10)
    ]
    
    start_time = time.time()
    successful = 0
    
    try:
        # Process in batches
        for i in range(0, len(test_texts), EMBEDDING_BATCH_SIZE):
            batch = test_texts[i:i + EMBEDDING_BATCH_SIZE]
            response = requests.post(
                TEI_URL,
                json={"inputs": batch},
                timeout=10
            )
            if response.status_code == 200:
                successful += len(batch)
        
        elapsed = time.time() - start_time
        
        print(f"✓ Speed test complete")
        print(f"  Documents embedded: {successful}")
        print(f"  Time taken: {elapsed:.2f}s")
        print(f"  Rate: {successful/elapsed:.1f} docs/second")
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_large_document():
    """Test embedding a large document"""
    print("\n4. Testing large document embedding...")
    
    # Create a document similar in size to Apple docs
    large_text = """
    # SwiftUI Text View
    
    A view that displays one or more lines of read-only text.
    
    ## Overview
    
    Use Text to display one or more lines of read-only text. You can display text 
    using the standard system fonts, or you can customize the appearance of your 
    text using modifiers.
    
    """ * 10  # Multiply to simulate larger docs
    
    try:
        response = requests.post(
            TEI_URL,
            json={"inputs": [large_text]},
            timeout=10
        )
        
        if response.status_code == 200:
            print(f"✓ Large document embedding successful")
            print(f"  Document size: {len(large_text)} characters")
            return True
        else:
            print(f"✗ Failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


if __name__ == "__main__":
    print("TEI Embedding Tests")
    print("==================")
    print(f"TEI URL: {TEI_URL}")
    print(f"Batch size: {EMBEDDING_BATCH_SIZE}")
    
    tests = [
        test_single_embedding(),
        test_batch_embedding(),
        test_embedding_speed(),
        test_large_document()
    ]
    
    passed = sum(tests)
    total = len(tests)
    
    print(f"\n{'='*40}")
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed!")
    else:
        print("⚠ Some tests failed")
        sys.exit(1)