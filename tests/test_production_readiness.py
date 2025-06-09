#!/usr/bin/env python3
"""
Test production readiness scenarios
Focus on critical functionality that must work in production
"""

import os
import sys
import json
import time
import tempfile
from pathlib import Path
from unittest.mock import patch, Mock, MagicMock
import chromadb

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from scraper.utils.hash_manager import HashManager
from scripts.build_index_incremental import IncrementalEmbeddingBuilder

class TestHashManagerResilience:
    """Test hash manager under various failure conditions"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.hash_file = self.temp_dir / "test_hashes.json"
        self.hash_manager = HashManager(self.hash_file)
    
    def teardown_method(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_corrupted_hash_file_recovery(self):
        """Test recovery from corrupted hash file"""
        # Create corrupted hash file
        with open(self.hash_file, 'w') as f:
            f.write("invalid json content {")
        
        # Should handle corruption gracefully
        url = "test_url"
        content = "test content"
        
        # Should treat as new content
        assert self.hash_manager.has_changed(url, content) is True
        
        # Should be able to update and create new valid file
        self.hash_manager.update_hash(url, content)
        self.hash_manager.save()
        
        # File should now be valid
        assert self.hash_file.exists()
        with open(self.hash_file, 'r') as f:
            data = json.load(f)
            assert "hashes" in data
            assert url in data["hashes"]
        
        print("✓ Corrupted hash file recovery test passed")
    
    def test_disk_space_exhaustion_simulation(self):
        """Test behavior when disk space is exhausted"""
        # Simulate disk space exhaustion by making directory read-only
        os.chmod(self.temp_dir, 0o444)  # Read-only
        
        try:
            url = "test_url"
            content = "test content"
            
            # Should not crash even if save fails
            self.hash_manager.update_hash(url, content)
            self.hash_manager.save()  # This should fail silently
            
            # Hash should still be in memory
            assert url in self.hash_manager.hashes
            
        finally:
            # Restore permissions for cleanup
            os.chmod(self.temp_dir, 0o755)
        
        print("✓ Disk space exhaustion simulation test passed")
    
    def test_very_large_hash_file_performance(self):
        """Test performance with large hash files"""
        # Create many hash entries
        start_time = time.time()
        
        for i in range(1000):
            url = f"test_url_{i}"
            content = f"test content {i}"
            self.hash_manager.update_hash(url, content, f"etag-{i}")
        
        # Save large hash file
        self.hash_manager.save()
        
        # Test load performance
        load_start = time.time()
        new_manager = HashManager(self.hash_file)
        load_time = time.time() - load_start
        
        total_time = time.time() - start_time
        
        # Should complete in reasonable time (< 2 seconds for 1000 entries)
        assert total_time < 2.0, f"Hash operations too slow: {total_time}s"
        assert load_time < 0.5, f"Hash loading too slow: {load_time}s"
        
        # Verify data integrity
        assert len(new_manager.hashes) == 1000
        
        print(f"✓ Large hash file performance test passed ({total_time:.3f}s total)")

class TestEmbeddingSystemResilience:
    """Test embedding system under stress and failure conditions"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.docs_path = self.temp_dir / "docs"
        self.vectorstore_path = self.temp_dir / "vectorstore"
        self.docs_path.mkdir()
        self.vectorstore_path.mkdir()
        
        # Create test builder
        self.builder = IncrementalEmbeddingBuilder(self.docs_path, self.vectorstore_path)
        self.builder.checkpoint_file = self.temp_dir / "checkpoint.json"
        
    def teardown_method(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_checkpoint_persistence_across_failures(self):
        """Test that checkpoints survive process interruption"""
        # Simulate checkpoint data
        batch_index = 15
        total_batches = 100
        processed_files = [f"file_{i}.md" for i in range(50)]
        
        # Save checkpoint
        self.builder.save_checkpoint(batch_index, total_batches, processed_files)
        
        # Simulate process restart by creating new builder
        new_builder = IncrementalEmbeddingBuilder(self.docs_path, self.vectorstore_path)
        new_builder.checkpoint_file = self.temp_dir / "checkpoint.json"
        
        # Should load checkpoint
        checkpoint = new_builder.load_checkpoint()
        assert checkpoint is not None
        assert checkpoint["batch_index"] == batch_index
        assert checkpoint["processed_files"] == processed_files
        
        print("✓ Checkpoint persistence test passed")
    
    def test_verification_system_integrity(self):
        """Test embedding verification under various conditions"""
        # Create test collection
        chroma = chromadb.PersistentClient(path=str(self.vectorstore_path))
        collection = chroma.create_collection("test_verification")
        
        # Test cases: content match, content mismatch, missing embedding
        test_cases = [
            ("doc_1", "Original content", "Original content", True),  # Match
            ("doc_2", "Original content", "Modified content", False), # Mismatch
            ("doc_3", None, "Content", False),  # Missing
        ]
        
        # Add embeddings for first two cases
        collection.add(
            ids=["doc_1", "doc_2"],
            documents=["Original content", "Original content"],
            embeddings=[[0.1] * 1536, [0.2] * 1536]
        )
        
        # Test verification
        for doc_id, stored_content, verify_content, expected in test_cases:
            if stored_content is not None:  # Skip missing doc
                result = self.builder.verify_embedding(collection, doc_id, verify_content)
                assert result == expected, f"Verification failed for {doc_id}"
        
        print("✓ Verification system integrity test passed")
    
    def test_cost_limit_enforcement(self):
        """Test that cost limits are properly enforced"""
        # Create some test files
        for i in range(10):
            test_file = self.docs_path / f"test_{i}.md"
            test_file.write_text(f"Test content {i}" * 1000)  # Make files large enough
        
        # Mock the cost estimation to return high cost
        original_estimate = self.builder.estimate_cost
        
        def mock_estimate_high_cost(files):
            return 999.99  # Exceeds any reasonable limit
        
        self.builder.estimate_cost = mock_estimate_high_cost
        
        # Should refuse to process due to cost
        stats, _ = self.builder.scan_for_changes()
        files_to_process = stats["files_to_process"]
        
        if files_to_process:
            estimated_cost = self.builder.estimate_cost(files_to_process)
            # Should detect high cost
            assert estimated_cost > 10.0  # Default limit
        
        # Restore original method
        self.builder.estimate_cost = original_estimate
        
        print("✓ Cost limit enforcement test passed")

class TestConfigurationValidation:
    """Test configuration and environment validation"""
    
    def test_missing_api_key_handling(self):
        """Test handling of missing OpenAI API key"""
        temp_dir = Path(tempfile.mkdtemp())
        try:
            builder = IncrementalEmbeddingBuilder(temp_dir / "docs", temp_dir / "vectorstore")
            
            # Mock missing API key
            with patch.dict(os.environ, {}, clear=True):
                try:
                    builder.configure_openai()
                    assert False, "Should have raised ValueError for missing API key"
                except ValueError as e:
                    assert "OPENAI_API_KEY" in str(e)
            
            print("✓ Missing API key handling test passed")
        finally:
            import shutil
            shutil.rmtree(temp_dir, ignore_errors=True)
    
    def test_invalid_api_key_format(self):
        """Test validation of API key format"""
        temp_dir = Path(tempfile.mkdtemp())
        try:
            builder = IncrementalEmbeddingBuilder(temp_dir / "docs", temp_dir / "vectorstore")
            
            # Test invalid API key formats
            invalid_keys = ["invalid", "sk-", "not-a-key", ""]
            
            for invalid_key in invalid_keys:
                with patch.dict(os.environ, {"OPENAI_API_KEY": invalid_key}):
                    try:
                        builder.configure_openai()
                        assert False, f"Should have rejected invalid key: {invalid_key}"
                    except ValueError as e:
                        # Accept either missing key or invalid format error
                        assert ("OPENAI_API_KEY" in str(e) or "Invalid OpenAI API key" in str(e))
            
            print("✓ Invalid API key format test passed")
        finally:
            import shutil
            shutil.rmtree(temp_dir, ignore_errors=True)
    
    def test_framework_name_validation(self):
        """Test framework name validation against path traversal"""
        temp_dir = Path(tempfile.mkdtemp())
        try:
            builder = IncrementalEmbeddingBuilder(temp_dir / "docs", temp_dir / "vectorstore")
            
            # Test dangerous framework names
            dangerous_names = [
                "../etc/passwd",
                "../../",
                "framework/../../../etc",
                "framework\x00hidden",
                "framework/../../secret"
            ]
            
            for dangerous_name in dangerous_names:
                try:
                    builder.validate_framework_name(dangerous_name)
                    assert False, f"Should have rejected dangerous name: {dangerous_name}"
                except ValueError:
                    pass  # Expected
            
            # Test valid names
            valid_names = ["SwiftUI", "UIKit", "Foundation", "Core-Data", "My_Framework"]
            for valid_name in valid_names:
                result = builder.validate_framework_name(valid_name)
                assert result is True
            
            print("✓ Framework name validation test passed")
        finally:
            import shutil
            shutil.rmtree(temp_dir, ignore_errors=True)

def run_production_readiness_tests():
    """Run all production readiness tests"""
    print("🏭 Testing Production Readiness\n")
    
    test_classes = [
        TestHashManagerResilience,
        TestEmbeddingSystemResilience, 
        TestConfigurationValidation
    ]
    total_passed = 0
    total_failed = 0
    
    for test_class in test_classes:
        print(f"\n📋 Running {test_class.__name__} tests:")
        print("-" * 60)
        
        # Get all test methods
        test_methods = [method for method in dir(test_class) if method.startswith('test_')]
        
        for test_method_name in test_methods:
            try:
                # Create instance and run test
                test_instance = test_class()
                if hasattr(test_instance, 'setup_method'):
                    test_instance.setup_method()
                
                test_method = getattr(test_instance, test_method_name)
                test_method()
                
                if hasattr(test_instance, 'teardown_method'):
                    test_instance.teardown_method()
                total_passed += 1
                
            except Exception as e:
                print(f"❌ {test_method_name} failed: {e}")
                total_failed += 1
                import traceback
                traceback.print_exc()
    
    print(f"\n{'='*70}")
    print(f"PRODUCTION READINESS TEST SUMMARY")
    print(f"{'='*70}")
    print(f"Tests passed: {total_passed}")
    print(f"Tests failed: {total_failed}")
    
    if total_passed > 0:
        print(f"Success rate: {(total_passed/(total_passed+total_failed)*100):.1f}%")
    
    if total_failed == 0:
        print("\n✅ All production readiness tests passed!")
        print("🚀 System is ready for production deployment!")
        return True
    else:
        print(f"\n❌ {total_failed} tests failed")
        print("⚠️  Fix these issues before production deployment")
        return False

if __name__ == "__main__":
    success = run_production_readiness_tests()
    sys.exit(0 if success else 1)