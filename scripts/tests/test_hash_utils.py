#!/usr/bin/env python3
"""Unit tests for hash utilities module."""

import errno
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from utilities.hash_utils import (
    HashFileError,
    compute_hash,
    compute_file_hash,
    has_content_changed,
    load_hashes,
    load_metadata,
    read_hash_file,
    save_hashes,
    write_text_atomic,
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
    # metadata= / load_metadata / read_hash_file tests
    # ==========================================================================

    def test_metadata_keys_are_preserved_as_given(self):
        """Every metadata= key is written as given and read back by load_metadata."""
        hash_file = Path(self.temp_dir) / "hashes.json"
        extra = {
            "sources": {"MLX": "MLX", "coremltools": "coremltools"},
            "failure_counts": {"MLX:https://x/a.html": {"fail": 2}},
            "pending_orphans": ["MLX/a.md"],
            "render": {"version": 3},
        }
        self.assertTrue(save_hashes(hash_file, {"k": "h"}, source="s.py", metadata=extra))
        metadata = load_metadata(hash_file)
        for key, value in extra.items():
            self.assertEqual(metadata[key], value)
        self.assertEqual(metadata["source"], "s.py")
        self.assertEqual(metadata["total_files"], 1)
        self.assertEqual(load_hashes(hash_file), {"k": "h"})

    def test_run_metadata_keys_cannot_be_overridden(self):
        hash_file = Path(self.temp_dir) / "hashes.json"
        save_hashes(hash_file, {"k": "h"}, source="s.py", metadata={"total_files": 99, "source": "other"})
        metadata = load_metadata(hash_file)
        self.assertEqual(metadata["total_files"], 1)
        self.assertEqual(metadata["source"], "s.py")

    def test_a_key_left_out_is_dropped(self):
        hash_file = Path(self.temp_dir) / "hashes.json"
        save_hashes(hash_file, {}, metadata={"pending_orphans": ["a.md"]})
        save_hashes(hash_file, {}, metadata={})
        self.assertNotIn("pending_orphans", load_metadata(hash_file))

    def test_load_metadata_of_flat_missing_and_corrupt_files(self):
        hash_file = Path(self.temp_dir) / "hashes.json"
        self.assertEqual(load_metadata(hash_file), {})
        hash_file.write_text(json.dumps({"a": {"hash": "x"}}))
        self.assertEqual(load_metadata(hash_file), {})
        hash_file.write_text("{{{")
        self.assertEqual(load_metadata(hash_file), {})

    def test_read_hash_file_raises_on_unreadable_files(self):
        """Invalid JSON, invalid UTF-8 and the wrong shape raise; load_hashes logs and returns {}."""
        hash_file = Path(self.temp_dir) / "hashes.json"
        for content in (b"{{{", b"\xff\xfe\x00 not utf-8", b"[1, 2]", b'{"hashes": [1], "metadata": {}}'):
            hash_file.write_bytes(content)
            with self.assertRaises(HashFileError):
                read_hash_file(hash_file)
            self.assertEqual(load_hashes(hash_file), {})
        self.assertEqual(read_hash_file(Path(self.temp_dir) / "missing.json"), ({}, {}))

    def test_save_is_atomic_and_reports_failure(self):
        """A failed save leaves the old file intact (no temp file left) and returns False."""
        hash_file = Path(self.temp_dir) / "hashes.json"
        save_hashes(hash_file, {"k": "old"})
        before = hash_file.read_text()
        self.assertFalse(save_hashes(hash_file, {"k": object()}))  # not JSON-serializable
        self.assertEqual(hash_file.read_text(), before)
        self.assertEqual(sorted(p.name for p in Path(self.temp_dir).iterdir()), ["hashes.json"])
        blocked = Path(self.temp_dir) / "file-not-dir"
        blocked.write_text("x")
        self.assertFalse(save_hashes(blocked / "hashes.json", {"k": "h"}))

    def test_write_text_atomic(self):
        """Whole or not at all: a write that fails part way keeps the old file, with no temp file left."""
        doc = Path(self.temp_dir) / "page.md"
        write_text_atomic(doc, "# old\n")
        write_text_atomic(doc, "# new ü\n")
        self.assertEqual(doc.read_text(encoding="utf-8"), "# new ü\n")
        write_text = Path.write_text

        def disk_full(path, data, *args, **kwargs):
            write_text(path, data[:3], *args, **kwargs)
            raise OSError(errno.ENOSPC, "No space left on device")

        with mock.patch.object(Path, "write_text", disk_full):
            with self.assertRaises(OSError):
                write_text_atomic(doc, "# newer\n")
        self.assertEqual(doc.read_text(encoding="utf-8"), "# new ü\n")
        self.assertEqual(sorted(p.name for p in Path(self.temp_dir).iterdir()), ["page.md"])
        # A name with no room for the ".tmp" suffix gets a short temp name
        long_doc = Path(self.temp_dir) / ("a" * 250 + ".md")
        write_text_atomic(long_doc, "# long\n")
        self.assertEqual(long_doc.read_text(), "# long\n")
        self.assertEqual(sorted(p.name for p in Path(self.temp_dir).iterdir()), sorted([long_doc.name, "page.md"]))

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
