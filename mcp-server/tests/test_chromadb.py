#!/usr/bin/env python3
"""
Test ChromaDB functionality
"""
import os
import sys
import shutil
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

import chromadb
from server.config import VECTORSTORE_PATH, COLLECTION_NAME


def test_chromadb_connection():
    """Test basic ChromaDB connection"""
    print("\n1. Testing ChromaDB connection...")
    
    try:
        # Create a test client with a temporary path
        test_path = VECTORSTORE_PATH / "test"
        client = chromadb.PersistentClient(path=str(test_path))
        
        # List collections (should be empty)
        collections = client.list_collections()
        
        print(f"✓ ChromaDB connection successful")
        print(f"  Path: {test_path}")
        print(f"  Collections: {len(collections)}")
        
        # Clean up
        shutil.rmtree(test_path, ignore_errors=True)
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_collection_operations():
    """Test creating and managing collections"""
    print("\n2. Testing collection operations...")
    
    try:
        # Create test client
        test_path = VECTORSTORE_PATH / "test"
        client = chromadb.PersistentClient(path=str(test_path))
        
        # Create collection
        collection = client.create_collection(
            name="test_collection",
            metadata={"description": "Test collection for Apple docs"}
        )
        
        print(f"✓ Collection created successfully")
        print(f"  Name: {collection.name}")
        print(f"  Count: {collection.count()}")
        
        # Delete collection
        client.delete_collection("test_collection")
        print(f"✓ Collection deleted successfully")
        
        # Clean up
        shutil.rmtree(test_path, ignore_errors=True)
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_document_operations():
    """Test adding and querying documents"""
    print("\n3. Testing document operations...")
    
    try:
        # Create test client and collection
        test_path = VECTORSTORE_PATH / "test"
        client = chromadb.PersistentClient(path=str(test_path))
        collection = client.create_collection(name="test_docs")
        
        # Add test documents
        test_embeddings = [
            [0.1] * 1024,  # BGE-M3 dimensions
            [0.2] * 1024,
            [0.3] * 1024
        ]
        
        test_documents = [
            "SwiftUI Button is a view that triggers an action",
            "UIKit UIViewController manages a view hierarchy",
            "Core Data provides persistent storage"
        ]
        
        test_metadatas = [
            {"framework": "SwiftUI", "api_name": "Button"},
            {"framework": "UIKit", "api_name": "UIViewController"},
            {"framework": "CoreData", "api_name": "NSManagedObject"}
        ]
        
        collection.add(
            embeddings=test_embeddings,
            documents=test_documents,
            metadatas=test_metadatas,
            ids=["doc1", "doc2", "doc3"]
        )
        
        print(f"✓ Documents added successfully")
        print(f"  Count: {collection.count()}")
        
        # Query documents
        results = collection.query(
            query_embeddings=[[0.15] * 1024],
            n_results=2
        )
        
        print(f"✓ Query successful")
        print(f"  Results: {len(results['documents'][0])}")
        print(f"  Top result: {results['metadatas'][0][0]['api_name']}")
        
        # Clean up
        shutil.rmtree(test_path, ignore_errors=True)
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_persistence():
    """Test that data persists across sessions"""
    print("\n4. Testing persistence...")
    
    try:
        test_path = VECTORSTORE_PATH / "test_persist"
        
        # First session: create and add data
        client1 = chromadb.PersistentClient(path=str(test_path))
        collection1 = client1.create_collection(name="persist_test")
        
        collection1.add(
            embeddings=[[0.5] * 1024],
            documents=["Test document"],
            metadatas=[{"test": True}],
            ids=["test1"]
        )
        
        count1 = collection1.count()
        print(f"✓ First session: added {count1} documents")
        
        # Second session: verify data exists
        client2 = chromadb.PersistentClient(path=str(test_path))
        collection2 = client2.get_collection(name="persist_test")
        
        count2 = collection2.count()
        print(f"✓ Second session: found {count2} documents")
        
        success = count1 == count2 == 1
        
        # Clean up
        shutil.rmtree(test_path, ignore_errors=True)
        
        return success
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


if __name__ == "__main__":
    print("ChromaDB Tests")
    print("==============")
    print(f"Vectorstore path: {VECTORSTORE_PATH}")
    
    tests = [
        test_chromadb_connection(),
        test_collection_operations(),
        test_document_operations(),
        test_persistence()
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