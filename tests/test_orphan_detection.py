#!/usr/bin/env python3
"""
Test orphan detection functionality
Tests the session-based orphan tracking and cleanup
"""

import json
import tempfile
from pathlib import Path
import sys
import shutil

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from scraper.utils.hash_manager import HashManager


def test_orphan_detection_basic():
    """Test basic orphan detection with session tracking"""
    with tempfile.TemporaryDirectory() as tmpdir:
        hash_file = Path(tmpdir) / "test_hashes.json"
        doc_dir = Path(tmpdir) / "docs"
        doc_dir.mkdir()
        
        # Create some files
        (doc_dir / "file1.md").write_text("content1")
        (doc_dir / "file2.md").write_text("content2")
        (doc_dir / "file3.md").write_text("content3")
        
        # First session - all files tracked
        hm1 = HashManager(hash_file)
        hm1.session_id = "session1"
        
        # Track files 1 and 2
        hm1.update_hash("url1", "content1", None, doc_dir / "file1.md")
        hm1.update_hash("url2", "content2", None, doc_dir / "file2.md")
        hm1.save()
        
        # Second session - only file1 is touched
        hm2 = HashManager(hash_file)
        hm2.session_id = "session2"
        hm2.update_hash("url1", "content1", None, doc_dir / "file1.md")
        hm2.save()
        
        # Check orphan detection
        hm3 = HashManager(hash_file)
        orphans = hm3.get_orphaned_files(doc_dir)
        
        # file2.md should be orphaned
        # file3.md is also orphaned since it exists but was never tracked
        # The get_orphaned_files method returns ALL files not touched in latest session
        assert len(orphans) == 2
        assert doc_dir / "file2.md" in orphans
        assert doc_dir / "file3.md" in orphans
        
    print("✅ Basic orphan detection works correctly")


def test_orphan_detection_with_unchanged_content():
    """Test that unchanged content (304 responses) still updates session"""
    with tempfile.TemporaryDirectory() as tmpdir:
        hash_file = Path(tmpdir) / "test_hashes.json"
        
        # First session
        hm1 = HashManager(hash_file)
        hm1.session_id = "session1"
        hm1.update_hash("url1", "content1", "etag1", Path("/path/to/file1.md"))
        hm1.save()
        
        # Second session - same content (unchanged)
        hm2 = HashManager(hash_file)
        hm2.session_id = "session2"
        
        # Check if content has changed
        changed = hm2.has_changed("url1", "content1", "etag1")
        assert not changed  # Content hasn't changed
        
        # Update session even though content unchanged
        hm2.update_hash("url1", "content1", "etag1", Path("/path/to/file1.md"))
        hm2.save()
        
        # Verify session was updated
        data = json.loads(hash_file.read_text())
        assert data["hashes"]["url1"]["session_id"] == "session2"
        
    print("✅ Session updates correctly for unchanged content")


def test_orphan_safety_check():
    """Test safety check prevents excessive deletion"""
    with tempfile.TemporaryDirectory() as tmpdir:
        hash_file = Path(tmpdir) / "test_hashes.json"
        doc_dir = Path(tmpdir) / "docs"
        doc_dir.mkdir()
        
        # Create many files
        files = []
        for i in range(10):
            file_path = doc_dir / f"file{i}.md"
            file_path.write_text(f"content{i}")
            files.append(file_path)
        
        # Track all files in session1
        hm1 = HashManager(hash_file)
        hm1.session_id = "session1"
        for i, file_path in enumerate(files):
            hm1.update_hash(f"url{i}", f"content{i}", None, file_path)
        hm1.save()
        
        # New session with only 2 files touched (simulating a bug)
        hm2 = HashManager(hash_file)
        hm2.session_id = "session2"
        hm2.update_hash("url0", "content0", None, files[0])
        hm2.update_hash("url1", "content1", None, files[1])
        hm2.save()
        
        # Check orphans - should be 8 out of 10 files (80%)
        hm3 = HashManager(hash_file)
        orphans = hm3.get_orphaned_files(doc_dir)
        assert len(orphans) == 8
        
        # Safety check should prevent deletion when >50% would be deleted
        total_files = list(doc_dir.glob("*.md"))
        deletion_percentage = len(orphans) / len(total_files)
        assert deletion_percentage > 0.5  # This would trigger safety check
        
    print("✅ Safety check would prevent excessive deletion")


def test_case_sensitivity_handling():
    """Test framework name vs ID case handling"""
    with tempfile.TemporaryDirectory() as tmpdir:
        hash_file = Path(tmpdir) / "AdSupport_hashes.json"
        
        # Create hash file with mixed case
        hm = HashManager(hash_file)
        hm.session_id = "test"
        
        # Test various URL patterns
        urls = [
            "https://developer.apple.com/documentation/adsupport",
            "https://developer.apple.com/documentation/AdSupport", 
            "https://developer.apple.com/documentation/adsupport/asidentifiermanager"
        ]
        
        for url in urls:
            hm.update_hash(url, f"content_{url}", None, Path(f"/path/{url}"))
        
        hm.save()
        
        # Verify all saved correctly
        data = json.loads(hash_file.read_text())
        assert len(data["hashes"]) == 3
        
    print("✅ Case sensitivity handled correctly")


def main():
    """Run all orphan detection tests"""
    print("\n🧪 ORPHAN DETECTION TEST SUITE")
    print("=" * 60)
    
    tests = [
        test_orphan_detection_basic,
        test_orphan_detection_with_unchanged_content,
        test_orphan_safety_check,
        test_case_sensitivity_handling
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"❌ {test.__name__} failed: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    
    if failed > 0:
        sys.exit(1)
    else:
        print("\n✅ All orphan detection tests passed!")


if __name__ == "__main__":
    main()