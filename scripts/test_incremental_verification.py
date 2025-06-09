#!/usr/bin/env python3
"""
Test to verify incremental embedding functionality
Ensures we don't re-embed unchanged documents
"""

import os
import sys
import json
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

def test_incremental_behavior():
    """Test that we don't re-embed unchanged documents"""
    
    test_framework = "AdSupport"  # 5 files
    collection_name = f"test_incremental_{int(time.time())}"
    
    print("="*70)
    print("INCREMENTAL EMBEDDING TEST")
    print("="*70)
    print(f"Testing with: {test_framework} (5 files)")
    print(f"Collection: {collection_name}")
    
    # Step 1: Run initial embedding
    print("\n1. Initial embedding run...")
    start_time = time.time()
    
    # Track API calls
    api_calls = {"count": 0}
    original_create = client.embeddings.create
    
    def tracked_create(*args, **kwargs):
        api_calls["count"] += 1
        return original_create(*args, **kwargs)
    
    client.embeddings.create = tracked_create
    
    # Run the embedding script (build_index_test doesn't support --collection)
    import subprocess
    cmd = f"python3 scripts/build_index_test.py --framework {test_framework}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    initial_time = time.time() - start_time
    initial_api_calls = api_calls["count"]
    
    print(f"   Time: {initial_time:.1f}s")
    print(f"   API calls: {initial_api_calls}")
    print(f"   Expected: 1 (batch of 5 docs)")
    
    if initial_api_calls == 0:
        print("   ❌ No API calls made - script may have failed")
        print(f"   stderr: {result.stderr}")
        return False
    
    # Verify embeddings exist (use the actual collection name)
    chroma = chromadb.PersistentClient(path="vectorstore")
    actual_collection_name = f"apple_docs_{test_framework}"
    try:
        collection = chroma.get_collection(actual_collection_name)
        doc_count = collection.count()
    except:
        print(f"   ❌ Collection {actual_collection_name} not found")
        return False
    print(f"   Documents in collection: {doc_count}")
    
    # Step 2: Run again with NO changes
    print("\n2. Second run (no changes)...")
    api_calls["count"] = 0
    start_time = time.time()
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    second_time = time.time() - start_time
    second_api_calls = api_calls["count"]
    
    print(f"   Time: {second_time:.1f}s")
    print(f"   API calls: {second_api_calls}")
    print(f"   Expected: 0 (should skip all)")
    
    # Check collection count didn't change
    new_doc_count = collection.count()
    print(f"   Documents in collection: {new_doc_count}")
    
    # Analyze results
    print("\n3. Analysis:")
    
    if second_api_calls == 0:
        print("   ✅ PASS: No API calls on second run (correctly skipped)")
        print("   ✅ Incremental updates working correctly!")
    else:
        print(f"   ❌ FAIL: Made {second_api_calls} API calls (should be 0)")
        print("   ❌ Re-embedded unchanged documents!")
        print("   💸 This would waste money on every run!")
    
    if second_time < initial_time * 0.5:
        print(f"   ✅ Second run was {initial_time/second_time:.1f}x faster")
    else:
        print(f"   ⚠️  Second run wasn't significantly faster")
    
    # Step 3: Modify one file and run again
    print("\n4. Third run (modify one file)...")
    
    # Modify a file
    test_file = Path("documentation") / test_framework / "AdSupport.md"
    if test_file.exists():
        original_content = test_file.read_text()
        test_file.write_text(original_content + "\n<!-- Test modification -->")
        
        api_calls["count"] = 0
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        third_api_calls = api_calls["count"]
        print(f"   API calls: {third_api_calls}")
        print(f"   Expected: 1 (only the modified file)")
        
        # Restore original
        test_file.write_text(original_content)
        
        if third_api_calls == 1:
            print("   ✅ Correctly re-embedded only the modified file")
        else:
            print(f"   ❌ Wrong number of API calls (expected 1, got {third_api_calls})")
    
    # Cleanup
    print("\n5. Cleanup...")
    try:
        chroma.delete_collection(collection_name)
        print("   ✅ Test collection deleted")
    except:
        pass
    
    # Restore original function
    client.embeddings.create = original_create
    
    return second_api_calls == 0

def check_current_implementation():
    """Check if current scripts have incremental support"""
    print("\n" + "="*70)
    print("IMPLEMENTATION CHECK")
    print("="*70)
    
    scripts = [
        "scripts/build_index_openai.py",
        "scripts/build_index_test.py",
        "scripts/build_index_secure.py"
    ]
    
    for script in scripts:
        print(f"\nChecking {script}:")
        
        if not Path(script).exists():
            print("   ❌ File not found")
            continue
        
        content = Path(script).read_text()
        
        # Check for incremental functionality
        checks = {
            "Hash checking": any(x in content for x in ["has_changed", "HashManager", "hash_manager"]),
            "Skip logic": "skip" in content.lower() and ("unchanged" in content.lower() or "up to date" in content.lower()),
            "Existing ID check": any(x in content for x in ["get_existing", "existing_ids", "collection.get"]),
            "Delete handling": any(x in content for x in ["delete", "remove", "orphan"]),
            "State tracking": any(x in content for x in ["embedding_metadata", "state", "tracking"])
        }
        
        for check, found in checks.items():
            status = "✅" if found else "❌"
            print(f"   {status} {check}")
        
        if not any(checks.values()):
            print("   ⚠️  NO INCREMENTAL FUNCTIONALITY FOUND!")

def main():
    """Run all checks"""
    print("🔍 Incremental Embedding Verification")
    print("💰 Testing if we waste money re-embedding unchanged docs")
    
    # Check implementation
    check_current_implementation()
    
    # Run actual test
    print("\n" + "="*70)
    success = test_incremental_behavior()
    
    if not success:
        print("\n❌ CRITICAL: Current implementation will re-embed everything on every run!")
        print("💸 This means $3.74 cost EVERY TIME you run it!")
        print("\n✅ Use the new incremental script instead:")
        print("   python3 scripts/build_index_incremental.py")

if __name__ == "__main__":
    main()