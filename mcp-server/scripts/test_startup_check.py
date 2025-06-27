#!/usr/bin/env python3
"""
Test the startup check script to ensure all fixes are working correctly.
"""

import os
import sys
import meilisearch
from pathlib import Path

# Add startup_check to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from startup_check import check_index_status, needs_reindexing, get_last_index_time, get_most_recent_hash_update

def test_startup_check():
    """Test the startup check functions."""
    print("🧪 Testing startup check functions...")
    
    # Test with local Meilisearch
    meilisearch_url = os.getenv("MEILI_HTTP_ADDR", "http://localhost:7700")
    meilisearch_key = os.getenv("MEILI_MASTER_KEY", "")
    
    if not meilisearch_key:
        print("❌ MEILI_MASTER_KEY not set")
        return
    
    print(f"📍 Connecting to Meilisearch at {meilisearch_url}")
    
    try:
        client = meilisearch.Client(meilisearch_url, meilisearch_key)
        
        # Test 1: Check index status
        print("\n1️⃣ Testing check_index_status()...")
        index_exists, doc_count = check_index_status(client)
        print(f"   Index exists: {index_exists}")
        print(f"   Document count: {doc_count:,}")
        
        # Test 2: Check hash timestamps
        print("\n2️⃣ Testing timestamp functions...")
        last_index = get_last_index_time()
        print(f"   Last index time: {last_index}")
        
        last_hash = get_most_recent_hash_update()
        print(f"   Most recent hash update: {last_hash}")
        
        # Test 3: Check if reindexing needed
        print("\n3️⃣ Testing needs_reindexing()...")
        needs_index, reason = needs_reindexing()
        print(f"   Needs reindexing: {needs_index}")
        print(f"   Reason: {reason}")
        
        # Test 4: Try to get stats directly
        print("\n4️⃣ Testing direct stats access...")
        if index_exists:
            index = client.index("apple-docs")
            stats = index.get_stats()
            print(f"   Stats type: {type(stats)}")
            print(f"   Stats content: {stats}")
            
            # Test different access methods
            if isinstance(stats, dict):
                print(f"   numberOfDocuments (dict): {stats.get('numberOfDocuments', 'NOT FOUND')}")
            else:
                print(f"   numberOfDocuments (attr): {getattr(stats, 'numberOfDocuments', 'NOT FOUND')}")
        
        print("\n✅ All tests completed!")
        
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_startup_check()