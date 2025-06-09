#!/usr/bin/env python3
"""
Test new checkpointing and verification features
"""

import os
import sys
import json
import time
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock
import chromadb

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from scripts.build_index_incremental import IncrementalEmbeddingBuilder

class TestCheckpointing:
    """Test checkpoint functionality"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.docs_path = self.temp_dir / "docs"
        self.vectorstore_path = self.temp_dir / "vectorstore"
        self.docs_path.mkdir()
        self.vectorstore_path.mkdir()
        
        # Create test builder
        self.builder = IncrementalEmbeddingBuilder(self.docs_path, self.vectorstore_path)
        
        # Override checkpoint file to use temp location
        self.builder.checkpoint_file = self.temp_dir / "checkpoint.json"
        
    def teardown_method(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_checkpoint_save_and_load(self):
        """Test checkpoint save and load functionality"""
        # Test data
        batch_index = 5
        total_batches = 20
        processed_files = ["file1.md", "file2.md", "file3.md"]
        
        # Save checkpoint
        self.builder.save_checkpoint(batch_index, total_batches, processed_files)
        
        # Verify file was created
        assert self.builder.checkpoint_file.exists()
        
        # Load checkpoint
        checkpoint = self.builder.load_checkpoint()
        
        # Verify data
        assert checkpoint is not None
        assert checkpoint["batch_index"] == batch_index
        assert checkpoint["total_batches"] == total_batches
        assert checkpoint["processed_files"] == processed_files
        assert "timestamp" in checkpoint
        
        print("✓ Checkpoint save/load test passed")
    
    def test_checkpoint_expiry(self):
        """Test that old checkpoints are ignored"""
        # Create old checkpoint (simulate)
        old_checkpoint = {
            "timestamp": time.time() - 7200,  # 2 hours ago
            "batch_index": 5,
            "total_batches": 20,
            "processed_files": ["file1.md"]
        }
        
        with open(self.builder.checkpoint_file, 'w') as f:
            json.dump(old_checkpoint, f)
        
        # Try to load - should return None due to age
        checkpoint = self.builder.load_checkpoint()
        assert checkpoint is None
        
        print("✓ Checkpoint expiry test passed")
    
    def test_checkpoint_clear(self):
        """Test checkpoint clearing"""
        # Create checkpoint
        self.builder.save_checkpoint(1, 10, ["file1.md"])
        assert self.builder.checkpoint_file.exists()
        
        # Clear checkpoint
        self.builder.clear_checkpoint()
        assert not self.builder.checkpoint_file.exists()
        
        print("✓ Checkpoint clear test passed")

class TestVerification:
    """Test embedding verification functionality"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.docs_path = self.temp_dir / "docs"
        self.vectorstore_path = self.temp_dir / "vectorstore"
        self.docs_path.mkdir()
        self.vectorstore_path.mkdir()
        
        # Create test builder
        self.builder = IncrementalEmbeddingBuilder(self.docs_path, self.vectorstore_path)
        
        # Create test ChromaDB collection
        self.chroma = chromadb.PersistentClient(path=str(self.vectorstore_path))
        self.collection = self.chroma.create_collection("test_collection")
        
    def teardown_method(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_embedding_verification_success(self):
        """Test successful embedding verification"""
        # Add test embedding
        test_content = "Test document content"
        test_id = "test_doc_1"
        test_embedding = [0.1] * 1536  # Mock embedding
        
        self.collection.add(
            ids=[test_id],
            documents=[test_content],
            embeddings=[test_embedding]
        )
        
        # Verify embedding
        result = self.builder.verify_embedding(self.collection, test_id, test_content)
        assert result is True
        
        print("✓ Embedding verification success test passed")
    
    def test_embedding_verification_failure(self):
        """Test embedding verification failure (content mismatch)"""
        # Add test embedding
        stored_content = "Original content"
        test_id = "test_doc_2"
        test_embedding = [0.1] * 1536
        
        self.collection.add(
            ids=[test_id],
            documents=[stored_content],
            embeddings=[test_embedding]
        )
        
        # Try to verify with different content
        different_content = "Different content"
        result = self.builder.verify_embedding(self.collection, test_id, different_content)
        assert result is False
        
        print("✓ Embedding verification failure test passed")
    
    def test_batch_verification(self):
        """Test batch verification functionality"""
        # Add multiple test embeddings
        test_contents = ["Content 1", "Content 2", "Content 3"]
        test_ids = ["doc_1", "doc_2", "doc_3"]
        test_embeddings = [[0.1] * 1536, [0.2] * 1536, [0.3] * 1536]
        
        self.collection.add(
            ids=test_ids,
            documents=test_contents,
            embeddings=test_embeddings
        )
        
        # Verify batch
        verified, failed = self.builder.verify_embeddings_batch(
            self.collection, test_ids, test_contents
        )
        
        assert verified == 3
        assert failed == 0
        
        print("✓ Batch verification test passed")
    
    def test_batch_verification_with_failures(self):
        """Test batch verification with some failures"""
        # Add test embeddings with one mismatch
        stored_contents = ["Content 1", "Content 2", "Content 3"]
        verification_contents = ["Content 1", "Different Content", "Content 3"]
        test_ids = ["doc_1", "doc_2", "doc_3"]
        test_embeddings = [[0.1] * 1536, [0.2] * 1536, [0.3] * 1536]
        
        self.collection.add(
            ids=test_ids,
            documents=stored_contents,
            embeddings=test_embeddings
        )
        
        # Verify batch (should have 1 failure)
        verified, failed = self.builder.verify_embeddings_batch(
            self.collection, test_ids, verification_contents
        )
        
        assert verified == 2
        assert failed == 1
        
        print("✓ Batch verification with failures test passed")

class TestHealthCheck:
    """Test health check functionality"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.docs_path = self.temp_dir / "docs"
        self.vectorstore_path = self.temp_dir / "vectorstore"
        self.docs_path.mkdir()
        self.vectorstore_path.mkdir()
        
        # Create some test markdown files
        (self.docs_path / "test1.md").write_text("Test content 1")
        (self.docs_path / "test2.md").write_text("Test content 2")
        
        # Import health checker
        from scripts.vectorstore_health_check import VectorstoreHealthChecker
        self.checker = VectorstoreHealthChecker(self.docs_path, self.vectorstore_path)
        
        # Create test collection
        self.chroma = chromadb.PersistentClient(path=str(self.vectorstore_path))
        self.collection = self.chroma.create_collection("test_health")
        
    def teardown_method(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_orphaned_embeddings_detection(self):
        """Test detection of orphaned embeddings"""
        # Add embedding for non-existent file
        self.collection.add(
            ids=["orphan_1"],
            documents=["Orphaned content"],
            embeddings=[[0.1] * 1536],
            metadatas=[{"file_path": str(self.docs_path / "nonexistent.md")}]
        )
        
        # Check for orphaned embeddings
        result = self.checker.check_orphaned_embeddings(self.collection)
        
        assert result["orphaned_count"] == 1
        assert result["status"] == "FAIL"
        
        print("✓ Orphaned embeddings detection test passed")
    
    def test_missing_embeddings_detection(self):
        """Test detection of missing embeddings"""
        # Files exist but no embeddings for them
        result = self.checker.check_missing_embeddings(self.collection)
        
        # Should find missing embeddings for our test files
        assert result["missing_count"] > 0
        assert result["status"] == "INFO"
        
        print("✓ Missing embeddings detection test passed")
    
    def test_duplicate_detection(self):
        """Test detection of duplicate embeddings"""
        file_path = str(self.docs_path / "test1.md")
        
        # Add multiple embeddings for same file
        self.collection.add(
            ids=["dup_1", "dup_2"],
            documents=["Content", "Content"],
            embeddings=[[0.1] * 1536, [0.2] * 1536],
            metadatas=[
                {"file_path": file_path},
                {"file_path": file_path}
            ]
        )
        
        # Check for duplicates
        result = self.checker.check_duplicates(self.collection)
        
        assert result["duplicates_found"] == 1
        assert result["status"] == "WARNING"
        
        print("✓ Duplicate detection test passed")

def run_all_tests():
    """Run all new feature tests"""
    print("🧪 Testing New Embedding Features\n")
    
    test_classes = [TestCheckpointing, TestVerification, TestHealthCheck]
    total_passed = 0
    total_failed = 0
    
    for test_class in test_classes:
        print(f"\n📋 Running {test_class.__name__} tests:")
        print("-" * 50)
        
        # Get all test methods
        test_methods = [method for method in dir(test_class) if method.startswith('test_')]
        
        for test_method_name in test_methods:
            try:
                # Create instance and run test
                test_instance = test_class()
                test_instance.setup_method()
                
                test_method = getattr(test_instance, test_method_name)
                test_method()
                
                test_instance.teardown_method()
                total_passed += 1
                
            except Exception as e:
                print(f"❌ {test_method_name} failed: {e}")
                total_failed += 1
                import traceback
                traceback.print_exc()
    
    print(f"\n{'='*60}")
    print(f"NEW FEATURES TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Tests passed: {total_passed}")
    print(f"Tests failed: {total_failed}")
    print(f"Success rate: {(total_passed/(total_passed+total_failed)*100):.1f}%")
    
    if total_failed == 0:
        print("\n✅ All new feature tests passed!")
        return True
    else:
        print(f"\n❌ {total_failed} tests failed")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)