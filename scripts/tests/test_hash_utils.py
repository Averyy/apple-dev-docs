#!/usr/bin/env python3
"""Unit tests for hash utilities module."""

import json
import tempfile
import unittest
from pathlib import Path

from utilities.hash_utils import (
    compute_hash,
    compute_file_hash,
    has_content_changed,
    load_hashes,
    save_hashes,
)


class TestHashUtils(unittest.TestCase):
    """Test hash utility functions."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)

    # ==========================================================================
    # compute_hash tests
    # ==========================================================================

    def test_compute_hash_basic(self):
        """Test basic string hashing."""
        result = compute_hash("test content")
        self.assertEqual(len(result), 64)  # SHA-256 hex = 64 chars
        self.assertTrue(all(c in "0123456789abcdef" for c in result))

    def test_compute_hash_deterministic(self):
        """Test that same input produces same hash."""
        content = "hello world"
        hash1 = compute_hash(content)
        hash2 = compute_hash(content)
        self.assertEqual(hash1, hash2)

    def test_compute_hash_different_inputs(self):
        """Test that different inputs produce different hashes."""
        hash1 = compute_hash("content A")
        hash2 = compute_hash("content B")
        self.assertNotEqual(hash1, hash2)

    def test_compute_hash_empty_string(self):
        """Test hashing empty string."""
        result = compute_hash("")
        self.assertEqual(len(result), 64)

    def test_compute_hash_unicode(self):
        """Test hashing unicode content."""
        result = compute_hash("日本語テスト 🎉")
        self.assertEqual(len(result), 64)

    # ==========================================================================
    # compute_file_hash tests
    # ==========================================================================

    def test_compute_file_hash_basic(self):
        """Test file hashing."""
        file_path = Path(self.temp_dir) / "test.txt"
        file_path.write_text("test file content")

        result = compute_file_hash(file_path)
        self.assertEqual(len(result), 64)

    def test_compute_file_hash_deterministic(self):
        """Test that same file produces same hash."""
        file_path = Path(self.temp_dir) / "test.txt"
        file_path.write_text("consistent content")

        hash1 = compute_file_hash(file_path)
        hash2 = compute_file_hash(file_path)
        self.assertEqual(hash1, hash2)

    def test_compute_file_hash_large_file(self):
        """Test hashing a file larger than chunk size (4KB)."""
        file_path = Path(self.temp_dir) / "large.txt"
        # Create 10KB file
        file_path.write_text("x" * 10240)

        result = compute_file_hash(file_path)
        self.assertEqual(len(result), 64)

    # ==========================================================================
    # load_hashes tests
    # ==========================================================================

    def test_load_hashes_nonexistent_file(self):
        """Test loading from non-existent file returns empty dict."""
        result = load_hashes(Path("/nonexistent/path/hashes.json"))
        self.assertEqual(result, {})

    def test_load_hashes_flat_format(self):
        """Test loading old flat format (just a dict of hashes)."""
        hash_file = Path(self.temp_dir) / "hashes.json"
        data = {"file1.md": "abc123", "file2.md": "def456"}
        hash_file.write_text(json.dumps(data))

        result = load_hashes(hash_file)
        self.assertEqual(result, data)

    def test_load_hashes_metadata_format(self):
        """Test loading new format with metadata wrapper."""
        hash_file = Path(self.temp_dir) / "hashes.json"
        data = {
            "metadata": {"last_updated": "2024-01-01", "total_files": 2},
            "hashes": {"file1.md": "abc123", "file2.md": "def456"},
        }
        hash_file.write_text(json.dumps(data))

        result = load_hashes(hash_file)
        self.assertEqual(result, {"file1.md": "abc123", "file2.md": "def456"})

    def test_load_hashes_corrupted_file(self):
        """Test loading corrupted JSON returns empty dict."""
        hash_file = Path(self.temp_dir) / "hashes.json"
        hash_file.write_text("not valid json {{{")

        result = load_hashes(hash_file)
        self.assertEqual(result, {})

    # ==========================================================================
    # save_hashes tests
    # ==========================================================================

    def test_save_hashes_with_metadata(self):
        """Test saving hashes with metadata."""
        hash_file = Path(self.temp_dir) / "subdir" / "hashes.json"
        hashes = {"file1.md": "abc123"}

        save_hashes(hash_file, hashes, source="test_script.py")

        # Verify file was created (including parent directory)
        self.assertTrue(hash_file.exists())

        # Verify content
        data = json.loads(hash_file.read_text())
        self.assertIn("metadata", data)
        self.assertIn("hashes", data)
        self.assertEqual(data["hashes"], hashes)
        self.assertEqual(data["metadata"]["source"], "test_script.py")
        self.assertEqual(data["metadata"]["total_files"], 1)

    def test_save_hashes_without_metadata(self):
        """Test saving hashes without metadata wrapper."""
        hash_file = Path(self.temp_dir) / "hashes.json"
        hashes = {"file1.md": "abc123"}

        save_hashes(hash_file, hashes, include_metadata=False)

        data = json.loads(hash_file.read_text())
        self.assertEqual(data, hashes)
        self.assertNotIn("metadata", data)

    def test_save_hashes_creates_parent_dirs(self):
        """Test that save_hashes creates parent directories."""
        hash_file = Path(self.temp_dir) / "deep" / "nested" / "dir" / "hashes.json"
        save_hashes(hash_file, {"test": "hash"})
        self.assertTrue(hash_file.exists())

    # ==========================================================================
    # has_content_changed tests
    # ==========================================================================

    def test_has_content_changed_new_content(self):
        """Test detecting new content (not in hashes)."""
        hashes = {}
        result = has_content_changed(hashes, "new_file.md", "new content")
        self.assertTrue(result)

    def test_has_content_changed_unchanged(self):
        """Test detecting unchanged content."""
        content = "test content"
        content_hash = compute_hash(content)
        hashes = {"file.md": content_hash}

        result = has_content_changed(hashes, "file.md", content)
        self.assertFalse(result)

    def test_has_content_changed_modified(self):
        """Test detecting modified content."""
        hashes = {"file.md": "old_hash_value"}
        result = has_content_changed(hashes, "file.md", "new content")
        self.assertTrue(result)

    def test_has_content_changed_nested_format(self):
        """Test handling nested hash format (dict with 'hash' key)."""
        content = "test content"
        content_hash = compute_hash(content)
        hashes = {"file.md": {"hash": content_hash, "timestamp": "2024-01-01"}}

        result = has_content_changed(hashes, "file.md", content)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
