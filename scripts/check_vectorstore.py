#!/usr/bin/env python3
"""
Script to check what's already embedded in the ChromaDB vectorstore
"""

import chromadb
import os
import json
from collections import defaultdict

def check_vectorstore():
    """Examine the contents of the ChromaDB vectorstore"""
    
    # Connect to ChromaDB
    persist_directory = "/Users/avery/Code/apple-developer-docs/vectorstore"
    client = chromadb.PersistentClient(path=persist_directory)
    
    print("=" * 80)
    print("ChromaDB Vectorstore Analysis")
    print("=" * 80)
    
    # Get all collections
    collections = client.list_collections()
    print(f"\nFound {len(collections)} collection(s):\n")
    
    total_documents = 0
    framework_counts = defaultdict(int)
    
    for collection in collections:
        print(f"\nCollection: '{collection.name}'")
        print("-" * 40)
        
        # Get collection info
        count = collection.count()
        total_documents += count
        print(f"Document count: {count}")
        
        if count > 0:
            # Sample a few documents to understand the structure
            try:
                # Get first 5 documents
                results = collection.get(limit=5, include=['documents', 'metadatas'])
                
                print("\nSample documents:")
                for i, (doc_id, doc, metadata) in enumerate(zip(
                    results['ids'], 
                    results['documents'], 
                    results['metadatas']
                )):
                    print(f"\n  Document {i+1}:")
                    print(f"    ID: {doc_id}")
                    print(f"    Content preview: {doc[:100]}..." if doc else "    Content: None")
                    print(f"    Metadata: {json.dumps(metadata, indent=6)}")
                    
                    # Track frameworks
                    if metadata and 'framework' in metadata:
                        framework_counts[metadata['framework']] += 1
                
                # Get all metadata to analyze what's embedded
                print("\nAnalyzing all documents for framework coverage...")
                all_results = collection.get(include=['metadatas'])
                
                # Reset framework counts for accurate total
                framework_counts.clear()
                for metadata in all_results['metadatas']:
                    if metadata and 'framework' in metadata:
                        framework_counts[metadata['framework']] += 1
                
            except Exception as e:
                print(f"Error retrieving documents: {e}")
    
    print("\n" + "=" * 80)
    print("Summary Statistics")
    print("=" * 80)
    print(f"\nTotal documents across all collections: {total_documents}")
    
    if framework_counts:
        print(f"\nFrameworks embedded ({len(framework_counts)} total):")
        # Sort by count descending
        for framework, count in sorted(framework_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {framework}: {count} documents")
    
    # Check for hash tracking files
    print("\n" + "=" * 80)
    print("Hash Tracking Files")
    print("=" * 80)
    
    hashes_dir = "/Users/avery/Code/apple-developer-docs/.hashes"
    if os.path.exists(hashes_dir):
        hash_files = [f for f in os.listdir(hashes_dir) if f.endswith('_hashes.json')]
        print(f"\nFound {len(hash_files)} hash tracking files:")
        
        total_tracked = 0
        for hash_file in sorted(hash_files):
            try:
                with open(os.path.join(hashes_dir, hash_file), 'r') as f:
                    hashes = json.load(f)
                    count = len(hashes)
                    total_tracked += count
                    print(f"  - {hash_file}: {count} documents tracked")
            except Exception as e:
                print(f"  - {hash_file}: Error reading - {e}")
        
        print(f"\nTotal documents tracked by hashes: {total_tracked}")
    else:
        print("\nNo .hashes directory found")

if __name__ == "__main__":
    check_vectorstore()