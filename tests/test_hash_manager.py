#!/usr/bin/env python3
"""Tests for HashManager content change detection."""

import sys
import tempfile
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scraper.utils.hash_manager import HashManager


def test_new_url_is_changed():
    """New URLs should always be detected as changed."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        hm = HashManager(Path(f.name))

    assert hm.has_changed("https://example.com/new", "content") is True
    print("PASS: new_url_is_changed")


def test_same_etag_unchanged():
    """Same ETag should be detected as unchanged."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        hm = HashManager(Path(f.name))

    url = "https://example.com/page"
    hm.update_hash(url, "content", etag="W/\"abc123\"")

    assert hm.has_changed(url, "content", etag="W/\"abc123\"") is False
    print("PASS: same_etag_unchanged")


def test_different_etag_different_content_is_changed():
    """Different ETag AND different content should be detected as changed."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        hm = HashManager(Path(f.name))

    url = "https://example.com/page"
    hm.update_hash(url, "old content", etag="W/\"old_etag\"")

    assert hm.has_changed(url, "new content", etag="W/\"new_etag\"") is True
    print("PASS: different_etag_different_content_is_changed")


def test_different_etag_same_content_is_unchanged():
    """Different ETag but same content should be detected as UNCHANGED.

    This is the critical fix: Apple can regenerate ETags during CDN redeployments
    without changing any actual content. The scraper must fall through to hash
    comparison instead of trusting ETag changes blindly.
    """
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        hm = HashManager(Path(f.name))

    url = "https://example.com/page"
    content = '{"identifier":{"url":"/documentation/swiftui/text"}}'

    hm.update_hash(url, content, etag="W/\"old_etag\"")

    # Same content, different ETag (CDN regenerated ETags)
    assert hm.has_changed(url, content, etag="W/\"new_etag\"") is False
    print("PASS: different_etag_same_content_is_unchanged")


def test_no_etag_uses_hash():
    """When no ETag is available, hash comparison should work."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        hm = HashManager(Path(f.name))

    url = "https://example.com/page"
    hm.update_hash(url, "content", etag=None)

    assert hm.has_changed(url, "content", etag=None) is False
    assert hm.has_changed(url, "different content", etag=None) is True
    print("PASS: no_etag_uses_hash")


def test_etag_updated_after_regeneration():
    """After ETag regeneration, the new ETag should be stored via update_hash.

    Simulates the full flow: ETag changes, hash says unchanged, code calls
    update_hash with new ETag. Next check with new ETag should be fast (ETag match).
    """
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        hm = HashManager(Path(f.name))

    url = "https://example.com/page"
    content = "same content throughout"

    # Initial scrape
    hm.update_hash(url, content, etag="W/\"etag_v1\"")

    # Apple regenerates ETags — has_changed falls through to hash, returns False
    assert hm.has_changed(url, content, etag="W/\"etag_v2\"") is False

    # Simulate what json_scraper does on the unchanged path: update_hash with new ETag
    hm.update_hash(url, content, etag="W/\"etag_v2\"")

    # Next run: ETag matches, fast path
    assert hm.has_changed(url, content, etag="W/\"etag_v2\"") is False
    print("PASS: etag_updated_after_regeneration")


def main():
    tests = [
        test_new_url_is_changed,
        test_same_etag_unchanged,
        test_different_etag_different_content_is_changed,
        test_different_etag_same_content_is_unchanged,
        test_no_etag_uses_hash,
        test_etag_updated_after_regeneration,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"FAIL: {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"ERROR: {test.__name__}: {e}")
            failed += 1

    print(f"\n{passed}/{passed + failed} tests passed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
