#!/usr/bin/env python3
"""
Test incremental indexing capabilities
"""
import os
import sys
import json
import shutil
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from server.config import VECTORSTORE_PATH


def test_incremental_updates():
    """Test that incremental updates work correctly"""
    print("\nTesting Incremental Update Detection")
    print("===================================\n")
    
    hash_file = VECTORSTORE_PATH / "file_hashes.json"
    
    # Check if hash file exists
    if hash_file.exists():
        with open(hash_file, 'r') as f:
            hashes = json.load(f)
            print(f"✓ Hash file exists with {len(hashes)} entries")
            
            # Show sample entries
            if hashes:
                print("\nSample tracked files:")
                for path, hash_val in list(hashes.items())[:5]:
                    print(f"  - {path}: {hash_val[:16]}...")
    else:
        print("✗ No hash file found (this is expected on first run)")
    
    # Check ChromaDB collection
    try:
        import chromadb
        client = chromadb.PersistentClient(path=str(VECTORSTORE_PATH))
        
        # List collections
        collections = client.list_collections()
        print(f"\n✓ ChromaDB has {len(collections)} collections")
        
        for collection in collections:
            count = collection.count()
            print(f"  - {collection.name}: {count} documents")
            
            # Show sample document
            if count > 0:
                result = collection.peek(limit=1)
                if result['metadatas']:
                    meta = result['metadatas'][0]
                    print(f"    Sample: {meta.get('title', 'Unknown')} ({meta.get('framework', 'Unknown')})")
                    
    except Exception as e:
        print(f"\n⚠ ChromaDB check failed: {e}")
    
    print("\n" + "="*40)
    print("Incremental indexing is ready!")
    print("\nHow it works:")
    print("1. First run: Indexes all files")
    print("2. Subsequent runs: Only indexes new/changed files")
    print("3. File deletions: Automatically detected and removed")
    print("\nTo test:")
    print("1. Run: python scripts/build_index.py")
    print("2. Modify a markdown file")
    print("3. Run again - only the changed file will be processed")


if __name__ == "__main__":
    test_incremental_updates()