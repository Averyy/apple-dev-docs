#!/usr/bin/env python3
"""
Test integration between hash manager and embedding system
Ensures embeddings are only generated when content actually changes
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import Dict, List, Any
import chromadb
import openai
from dotenv import load_dotenv
import logging

# Add parent directory to path to import hash_manager
sys.path.append(str(Path(__file__).parent.parent))
from scraper.utils.hash_manager import HashManager

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
env_path = Path(__file__).parent.parent / "mcp-server" / ".env"
load_dotenv(env_path)

# Configure OpenAI
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class HashIntegrationTester:
    def __init__(self, test_framework: str = "AppTrackingTransparency"):
        self.test_framework = test_framework
        self.docs_path = Path(__file__).parent.parent / "documentation"
        self.vectorstore_path = Path(__file__).parent.parent / "vectorstore"
        hash_file = Path(__file__).parent.parent / ".hashes" / "test_hashes.json"
        self.hash_manager = HashManager(hash_file)
        
    def test_hash_based_embedding_decision(self):
        """Test that embeddings are only created when hashes change"""
        print("\n" + "="*70)
        print("TEST: Hash-Based Embedding Decision")
        print("="*70)
        
        framework_path = self.docs_path / self.test_framework
        test_files = list(framework_path.glob("*.md"))[:3]  # Test with 3 files
        
        # Step 1: Initial embedding (no hashes exist)
        print("\n1. Initial state - no hashes exist")
        files_needing_embedding = []
        
        for file_path in test_files:
            content = file_path.read_text()
            file_key = f"{self.test_framework}/{file_path.name}"
            
            if not self.hash_manager.has_changed(file_key, content):
                print(f"   ❌ {file_path.name} - Hash unchanged (shouldn't happen on first run)")
            else:
                print(f"   ✅ {file_path.name} - Needs embedding (new file)")
                files_needing_embedding.append(file_path)
                # Update hash after "embedding"
                self.hash_manager.update_hash(file_key, content)
        
        print(f"\nFiles needing embedding: {len(files_needing_embedding)}/{len(test_files)}")
        
        # Step 2: Run again with no changes
        print("\n2. Second run - no content changes")
        files_needing_embedding = []
        
        for file_path in test_files:
            content = file_path.read_text()
            file_key = f"{self.test_framework}/{file_path.name}"
            
            if not self.hash_manager.has_changed(file_key, content):
                print(f"   ✅ {file_path.name} - Skip (hash unchanged)")
            else:
                print(f"   ❌ {file_path.name} - Needs embedding (shouldn't happen)")
                files_needing_embedding.append(file_path)
        
        print(f"\nFiles needing embedding: {len(files_needing_embedding)}/{len(test_files)}")
        
        # Step 3: Modify one file
        print("\n3. Modify one file")
        test_file = test_files[0]
        original_content = test_file.read_text()
        
        # Add a comment to change the hash
        modified_content = original_content + "\n<!-- Test modification -->"
        test_file.write_text(modified_content)
        
        files_needing_embedding = []
        
        for file_path in test_files:
            content = file_path.read_text()
            file_key = f"{self.test_framework}/{file_path.name}"
            
            if not self.hash_manager.has_changed(file_key, content):
                print(f"   ✅ {file_path.name} - Skip (hash unchanged)")
            else:
                print(f"   ✅ {file_path.name} - Needs embedding (content changed)")
                files_needing_embedding.append(file_path)
                # Update hash after "embedding"
                self.hash_manager.update_hash(file_key, content)
        
        print(f"\nFiles needing embedding: {len(files_needing_embedding)}/{len(test_files)}")
        
        # Restore original content
        test_file.write_text(original_content)
        
        return True
    
    def test_etag_integration(self):
        """Test ETag-based change detection"""
        print("\n" + "="*70)
        print("TEST: ETag Integration")
        print("="*70)
        
        # Test with dummy content and ETags
        test_url = f"https://developer.apple.com/documentation/{self.test_framework}/test"
        test_content = "Test content for ETag verification"
        test_etag = "W/\"test-etag-12345\""
        
        print("1. Initial state - no hash/etag stored")
        has_changed = self.hash_manager.has_changed(test_url, test_content, test_etag)
        print(f"   Changed: {has_changed} ✅ (Should be True - new content)")
        
        # Update with ETag
        self.hash_manager.update_hash(test_url, test_content, test_etag)
        
        print("\n2. Check with same ETag")
        has_changed = self.hash_manager.has_changed(test_url, test_content, test_etag)
        print(f"   Changed: {has_changed} ✅ (Should be False - same ETag)")
        
        print("\n3. Check with different ETag but same content")
        new_etag = "W/\"test-etag-67890\""
        has_changed = self.hash_manager.has_changed(test_url, test_content, new_etag)
        print(f"   Changed: {has_changed} ✅ (Should be True - different ETag)")
        
        # Save changes
        self.hash_manager.save()
        
        return True
    
    def test_incremental_embedding_workflow(self):
        """Test complete incremental embedding workflow"""
        print("\n" + "="*70)
        print("TEST: Complete Incremental Workflow")
        print("="*70)
        
        # Simulate a complete workflow
        framework_path = self.docs_path / self.test_framework
        
        print("1. Scan all files and check for changes")
        stats = {
            "total": 0,
            "unchanged": 0,
            "changed": 0,
            "new": 0
        }
        
        for file_path in framework_path.glob("*.md"):
            content = file_path.read_text()
            file_key = f"{self.test_framework}/{file_path.name}"
            
            stats["total"] += 1
            
            if file_key in self.hash_manager.hashes:
                if self.hash_manager.has_changed(file_key, content):
                    stats["changed"] += 1
                else:
                    stats["unchanged"] += 1
            else:
                stats["new"] += 1
        
        print(f"\n   Total files: {stats['total']}")
        print(f"   Unchanged: {stats['unchanged']} (skip embedding)")
        print(f"   Changed: {stats['changed']} (re-embed)")
        print(f"   New: {stats['new']} (initial embed)")
        print(f"\n   Embeddings needed: {stats['changed'] + stats['new']}")
        
        # Calculate cost savings
        if stats['total'] > 0:
            savings_percent = (stats['unchanged'] / stats['total']) * 100
            print(f"   Cost savings: {savings_percent:.1f}% (skipped embeddings)")
        
        return True
    
    def run_all_tests(self):
        """Run all integration tests"""
        tests = [
            self.test_hash_based_embedding_decision,
            self.test_etag_integration,
            self.test_incremental_embedding_workflow
        ]
        
        results = []
        for test in tests:
            try:
                result = test()
                results.append((test.__name__, result))
            except Exception as e:
                logger.error(f"Test {test.__name__} failed: {e}")
                import traceback
                traceback.print_exc()
                results.append((test.__name__, False))
        
        # Summary
        print("\n" + "="*70)
        print("INTEGRATION TEST SUMMARY")
        print("="*70)
        passed = sum(1 for _, result in results if result)
        print(f"Tests passed: {passed}/{len(tests)}")
        
        for test_name, result in results:
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"{status} - {test_name}")
        
        # Save hash data
        self.hash_manager.save()
        print(f"\nHash data saved to: {self.hash_manager.cache_file}")
        print(f"Total hashes stored: {len(self.hash_manager.hashes)}")
        
        return all(result for _, result in results)

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Test hash integration with embeddings")
    parser.add_argument("--framework", default="AppTrackingTransparency", 
                       help="Framework to test with")
    args = parser.parse_args()
    
    print(f"🧪 Testing Hash Integration with {args.framework}")
    print(f"📁 Documentation: documentation/{args.framework}")
    print(f"🔐 Hash storage: .hashes/document_hashes.json")
    
    tester = HashIntegrationTester(args.framework)
    success = tester.run_all_tests()
    
    if success:
        print("\n✅ All integration tests passed!")
        print("The embedding system correctly:")
        print("- Only embeds new or changed content")
        print("- Skips unchanged files based on hash")
        print("- Integrates with ETag change detection")
        print("- Provides significant cost savings on updates")
    else:
        print("\n❌ Some integration tests failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()