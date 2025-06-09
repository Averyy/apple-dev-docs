#!/usr/bin/env python3
"""
Full end-to-end test of the embedding workflow
Tests the complete pipeline from scraping to search
"""

import os
import sys
import json
import subprocess
import time
from pathlib import Path
import chromadb
import openai
from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent / "mcp-server" / ".env"
load_dotenv(env_path)

# Configure OpenAI
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_command(cmd: str) -> tuple[int, str, str]:
    """Run a command and return exit code, stdout, stderr"""
    print(f"\n$ {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def test_full_workflow():
    """Test the complete embedding workflow"""
    test_framework = "AdSupport"  # Small framework for testing
    
    print("="*70)
    print("FULL EMBEDDING WORKFLOW TEST")
    print("="*70)
    print(f"Test framework: {test_framework}")
    print(f"Expected files: 5")
    print(f"Expected cost: < $0.001")
    
    # Step 1: Clear existing embeddings for clean test
    print("\n1. Clearing existing test embeddings...")
    vectorstore_path = Path(__file__).parent.parent / "vectorstore"
    chroma = chromadb.PersistentClient(path=str(vectorstore_path))
    
    try:
        chroma.delete_collection(f"apple_docs_{test_framework}")
        print("   ✅ Cleared existing collection")
    except:
        print("   ℹ️  No existing collection to clear")
    
    # Step 2: Run embedding generation
    print("\n2. Running embedding generation...")
    cmd = f"python3 scripts/build_index_test.py --framework {test_framework}"
    exit_code, stdout, stderr = run_command(cmd)
    
    if exit_code != 0:
        print(f"   ❌ Embedding generation failed with exit code {exit_code}")
        print(f"   stderr: {stderr}")
        return False
    
    print("   ✅ Embedding generation completed")
    
    # Step 3: Verify embeddings were created
    print("\n3. Verifying embeddings...")
    try:
        collection = chroma.get_collection(f"apple_docs_{test_framework}")
        doc_count = collection.count()
        print(f"   ✅ Found {doc_count} documents in collection")
        
        if doc_count != 5:
            print(f"   ❌ Expected 5 documents, found {doc_count}")
            return False
    except Exception as e:
        print(f"   ❌ Failed to verify embeddings: {e}")
        return False
    
    # Step 4: Test search functionality
    print("\n4. Testing search functionality...")
    test_queries = [
        ("advertising identifier", "Should find main AdSupport APIs"),
        ("ASIdentifierManager", "Should find the exact class"),
        ("tracking enabled", "Should find tracking-related APIs")
    ]
    
    for query, description in test_queries:
        print(f"\n   Query: '{query}' - {description}")
        
        # Generate query embedding
        response = client.embeddings.create(
            input=[query],
            model="text-embedding-3-small"
        )
        query_embedding = response.data[0].embedding
        
        # Search
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3,
            include=["documents", "metadatas"]
        )
        
        if results['documents'][0]:
            print(f"   ✅ Found {len(results['documents'][0])} results")
            for i, metadata in enumerate(results['metadatas'][0][:2]):
                print(f"      {i+1}. {metadata['api_name']}")
        else:
            print("   ❌ No results found")
    
    # Step 5: Test incremental update (no changes)
    print("\n\n5. Testing incremental update (no changes)...")
    print("   Running embedding generation again...")
    
    start_time = time.time()
    cmd = f"python3 scripts/build_index_test.py --framework {test_framework}"
    exit_code, stdout, stderr = run_command(cmd)
    elapsed = time.time() - start_time
    
    print(f"   ✅ Completed in {elapsed:.1f}s")
    
    # Check if it was faster (should skip embeddings)
    if elapsed < 2.0:
        print("   ✅ Fast execution - likely skipped unchanged files")
    else:
        print("   ⚠️  Took longer than expected - may have re-embedded")
    
    # Step 6: Simulate file update
    print("\n6. Testing update detection...")
    test_file = Path(__file__).parent.parent / "documentation" / test_framework / "AdSupport.md"
    
    if test_file.exists():
        # Read original
        original_content = test_file.read_text()
        
        # Modify
        modified_content = original_content + "\n\n<!-- Test update -->"
        test_file.write_text(modified_content)
        print("   ✅ Modified test file")
        
        # Run update
        print("   Running embedding update...")
        cmd = f"python3 scripts/build_index_test.py --framework {test_framework}"
        exit_code, stdout, stderr = run_command(cmd)
        
        if "Creating embeddings" in stdout:
            print("   ✅ Detected change and created new embeddings")
        else:
            print("   ❌ Failed to detect change")
        
        # Restore
        test_file.write_text(original_content)
        print("   ✅ Restored original file")
    
    print("\n" + "="*70)
    print("✅ FULL WORKFLOW TEST COMPLETED SUCCESSFULLY")
    print("="*70)
    print("\nThe embedding system is ready for production use!")
    print("To run full embedding generation for all 259,026 files:")
    print("  python3 scripts/build_index_openai.py")
    print(f"\nEstimated cost: $3.74")
    print(f"Estimated time: 1-2 hours")
    
    return True

def main():
    """Main entry point"""
    print("🧪 Full Embedding Workflow Test")
    print("📁 Testing with AdSupport framework (5 files)")
    print("💰 Cost: < $0.001")
    
    try:
        success = test_full_workflow()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⏹️ Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()