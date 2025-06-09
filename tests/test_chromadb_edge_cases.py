#!/usr/bin/env python3
"""
Test ChromaDB edge cases and validate our handling
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

import chromadb
from scripts.chromadb_utils import *
import tempfile
import shutil
import numpy as np

def test_collection_name_validation():
    """Test collection name validation and sanitization"""
    print("\n1. Testing collection name validation...")
    
    test_cases = [
        # (input, expected_valid, description)
        ("valid_collection_123", True, "Valid name"),
        ("a", False, "Too short"),
        ("ab", False, "Too short"),
        ("abc", True, "Minimum length"),
        ("a" * 64, False, "Too long"),
        ("a" * 63, True, "Maximum length"),
        ("_invalid_start", False, "Starts with underscore"),
        ("invalid_end_", False, "Ends with underscore"),
        ("invalid-end-", False, "Ends with hyphen"),
        ("-invalid-start", False, "Starts with hyphen"),
        ("valid-with_mixed-123", True, "Valid with mixed characters"),
        ("invalid name!", False, "Contains space and special char"),
        ("SwiftUI.Button", False, "Contains period"),
    ]
    
    for name, expected, desc in test_cases:
        result = validate_collection_name(name)
        status = "✅" if result == expected else "❌"
        print(f"  {status} {desc}: '{name}' -> {result}")
    
    # Test sanitization
    print("\n  Testing sanitization:")
    sanitize_tests = [
        "Invalid Name!",
        "UIKit.UIViewController",
        "_starts_with_underscore_",
        "a",
        "a" * 100,
        "Core Data Framework"
    ]
    
    for name in sanitize_tests:
        sanitized = sanitize_collection_name(name)
        valid = validate_collection_name(sanitized)
        print(f"  '{name}' -> '{sanitized}' (valid: {valid})")

def test_document_size_limits():
    """Test document size validation and truncation"""
    print("\n2. Testing document size limits...")
    
    # Test various document sizes
    small_doc = "Small document"
    large_doc = "x" * 10000  # 10KB
    
    print(f"  Small doc ({len(small_doc)} bytes): {validate_document_size(small_doc)}")
    print(f"  Large doc ({len(large_doc)} bytes): {validate_document_size(large_doc)}")
    
    # Test truncation
    truncated = truncate_document(large_doc)
    print(f"  Truncated doc size: {len(truncated.encode('utf-8'))} bytes")
    print(f"  Truncated valid: {validate_document_size(truncated)}")
    
    # Test UTF-8 edge case
    utf8_doc = "Test " + "🔥" * 2000  # Emojis are multi-byte
    print(f"  UTF-8 doc chars: {len(utf8_doc)}, bytes: {len(utf8_doc.encode('utf-8'))}")
    truncated_utf8 = truncate_document(utf8_doc)
    print(f"  Truncated UTF-8 valid: {validate_document_size(truncated_utf8)}")

def test_metadata_limits():
    """Test metadata validation and sanitization"""
    print("\n3. Testing metadata limits...")
    
    # Small metadata
    small_meta = {
        "framework": "SwiftUI",
        "api_name": "Button",
        "url": "https://developer.apple.com/documentation/swiftui/button"
    }
    
    # Large metadata
    large_meta = {
        "framework": "UIKit",
        "api_name": "UIViewController" * 100,
        "description": "x" * 50000,
        "extra_field": "y" * 10000
    }
    
    print(f"  Small metadata valid: {validate_metadata(small_meta)}")
    print(f"  Large metadata valid: {validate_metadata(large_meta)}")
    
    # Test sanitization
    sanitized = sanitize_metadata(large_meta)
    print(f"  Sanitized metadata valid: {validate_metadata(sanitized)}")
    print(f"  Sanitized keys: {list(sanitized.keys())}")

def test_id_generation():
    """Test document ID generation"""
    print("\n4. Testing ID generation...")
    
    test_sources = [
        "simple_doc",
        "very_long_document_path_that_exceeds_normal_limits" * 5,
        "doc_with_special_chars!@#$%",
        "unicode_doc_🔥_test"
    ]
    
    for source in test_sources:
        doc_id = generate_document_id(source, 0)
        print(f"  Source: {source[:50]}... -> ID: {doc_id} (len: {len(doc_id)})")

def test_batch_chunking():
    """Test batch chunking for ChromaDB limits"""
    print("\n5. Testing batch chunking...")
    
    # Create test data
    items = list(range(2500))
    
    batches = chunk_for_chromadb(items)
    print(f"  Total items: {len(items)}")
    print(f"  Number of batches: {len(batches)}")
    print(f"  Batch sizes: {[len(b) for b in batches]}")

def test_embedding_validation():
    """Test embedding validation"""
    print("\n6. Testing embedding validation...")
    
    # Valid embeddings
    valid_embeddings = [[0.1] * 1536 for _ in range(3)]
    print(f"  Valid embeddings (1536d): {validate_embeddings(valid_embeddings)}")
    
    # Invalid: wrong dimension
    invalid_dim = [[0.1] * 1024 for _ in range(3)]
    print(f"  Wrong dimension (1024d): {validate_embeddings(invalid_dim, 1536)}")
    
    # Invalid: mixed dimensions
    mixed_dim = [[0.1] * 1536, [0.1] * 1024]
    print(f"  Mixed dimensions: {validate_embeddings(mixed_dim, 1536)}")
    
    # Invalid: non-numeric
    invalid_type = [[0.1] * 1535 + ["invalid"]]
    print(f"  Non-numeric values: {validate_embeddings(invalid_type, 1536)}")

def test_error_handling():
    """Test error message handling"""
    print("\n7. Testing error handling...")
    
    test_errors = [
        Exception("database is locked"),
        Exception("UNIQUE constraint failed: document.id"),
        Exception("Embedding dimension 1024 does not match collection dimension 1536"),
        Exception("Collection my_collection not found"),
        Exception("Batch size exceeds maximum limit"),
    ]
    
    for error in test_errors:
        advice = handle_chromadb_error(error, "test context")
        print(f"  Error: {str(error)[:50]}...")
        print(f"  Advice: {advice}")

def test_safe_operations():
    """Test safe ChromaDB operations"""
    print("\n8. Testing safe ChromaDB operations...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create client
        client = chromadb.PersistentClient(path=temp_dir)
        
        # Test safe collection creation
        collection = create_collection_safely(client, "Test Collection With Spaces!")
        print(f"  Created collection: {collection.name}")
        
        # Test safe document upsertion
        documents = [
            "Short doc",
            "x" * 10000,  # Large doc
            "Doc with 🔥 emojis"
        ]
        
        embeddings = [[0.1] * 1536 for _ in documents]
        
        metadatas = [
            {"type": "small"},
            {"type": "large", "extra": "x" * 50000},  # Large metadata
            {"type": "emoji", "special": "🔥"}
        ]
        
        ids = [generate_document_id(doc, i) for i, doc in enumerate(documents)]
        
        results = upsert_documents_safely(
            collection, documents, embeddings, metadatas, ids
        )
        
        print(f"  Upsert results: {results}")
        print(f"  Collection count: {collection.count()}")

def test_hnsw_config_validation():
    """Test HNSW configuration validation"""
    print("\n9. Testing HNSW config validation...")
    
    test_configs = [
        {"space": "cosine", "ef_search": 100},
        {"space": "invalid", "ef_search": 10000},  # Invalid values
        {"M": 32, "num_threads": 8},
        {"ef_construction": -1, "M": 100},  # Out of range
    ]
    
    for config in test_configs:
        validated = validate_hnsw_config(config)
        print(f"  Input: {config}")
        print(f"  Valid: {validated}")

def run_all_tests():
    """Run all edge case tests"""
    print("ChromaDB Edge Case Tests")
    print("=" * 50)
    
    tests = [
        test_collection_name_validation,
        test_document_size_limits,
        test_metadata_limits,
        test_id_generation,
        test_batch_chunking,
        test_embedding_validation,
        test_error_handling,
        test_safe_operations,
        test_hnsw_config_validation
    ]
    
    for test in tests:
        try:
            test()
        except Exception as e:
            print(f"\n❌ Test failed: {test.__name__}")
            print(f"   Error: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 50)
    print("✅ All edge case tests completed!")

if __name__ == "__main__":
    run_all_tests()