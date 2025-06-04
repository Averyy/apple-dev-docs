"""Tests for hash manager."""

import json
import tempfile
from pathlib import Path

import pytest

from scraper.utils.hash_manager import HashManager


@pytest.fixture
def temp_hash_file():
    """Create a temporary hash file."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = Path(f.name)
    yield temp_path
    temp_path.unlink(missing_ok=True)


def test_hash_manager_init(temp_hash_file):
    """Test HashManager initialization."""
    manager = HashManager(temp_hash_file)
    assert manager.cache_file == temp_hash_file
    assert manager.hashes == {}
    assert not manager._modified


def test_get_content_hash():
    """Test content hashing."""
    manager = HashManager(Path("test.json"))
    
    # Same content should produce same hash
    hash1 = manager.get_content_hash("Hello, World!")
    hash2 = manager.get_content_hash("Hello, World!")
    assert hash1 == hash2
    
    # Different content should produce different hash
    hash3 = manager.get_content_hash("Hello, Universe!")
    assert hash1 != hash3
    
    # Hash should be 64 characters (SHA-256)
    assert len(hash1) == 64


def test_has_changed(temp_hash_file):
    """Test change detection."""
    manager = HashManager(temp_hash_file)
    
    url = "https://example.com/page1"
    content = "Test content"
    
    # First time should always be changed
    assert manager.has_changed(url, content)
    
    # Update the hash
    manager.update_hash(url, content)
    
    # Same content should not be changed
    assert not manager.has_changed(url, content)
    
    # Different content should be changed
    assert manager.has_changed(url, "Different content")


def test_update_hash(temp_hash_file):
    """Test hash updates."""
    manager = HashManager(temp_hash_file)
    
    url = "https://example.com/page1"
    content = "Test content"
    
    manager.update_hash(url, content)
    
    assert url in manager.hashes
    assert manager.hashes[url]['hash'] == manager.get_content_hash(content)
    assert 'last_checked' in manager.hashes[url]
    assert manager.hashes[url]['status'] == 'new'
    assert manager._modified


def test_mark_error(temp_hash_file):
    """Test error marking."""
    manager = HashManager(temp_hash_file)
    
    url = "https://example.com/page1"
    error_msg = "404 Not Found"
    
    manager.mark_error(url, error_msg)
    
    assert url in manager.hashes
    assert manager.hashes[url]['status'] == 'error'
    assert manager.hashes[url]['error'] == error_msg
    assert manager._modified


def test_save_and_load(temp_hash_file):
    """Test saving and loading hashes."""
    # Create and populate manager
    manager1 = HashManager(temp_hash_file)
    manager1.update_hash("https://example.com/page1", "Content 1")
    manager1.update_hash("https://example.com/page2", "Content 2")
    manager1.mark_error("https://example.com/page3", "Error")
    
    # Save
    manager1.save()
    
    # Load in new manager
    manager2 = HashManager(temp_hash_file)
    
    assert len(manager2.hashes) == 3
    assert "https://example.com/page1" in manager2.hashes
    assert "https://example.com/page2" in manager2.hashes
    assert "https://example.com/page3" in manager2.hashes
    
    # Verify error status preserved
    assert manager2.hashes["https://example.com/page3"]['status'] == 'error'


def test_get_statistics(temp_hash_file):
    """Test statistics generation."""
    manager = HashManager(temp_hash_file)
    
    # Add various statuses
    manager.update_hash("https://example.com/page1", "Content 1")
    manager.update_hash("https://example.com/page2", "Content 2")
    manager.mark_error("https://example.com/page3", "Error 1")
    manager.mark_error("https://example.com/page4", "Error 2")
    
    # Mark one as unchanged
    manager.hashes["https://example.com/page1"]['status'] = 'unchanged'
    
    stats = manager.get_statistics()
    
    assert stats['total'] == 4
    assert stats['new'] == 1
    assert stats['unchanged'] == 1
    assert stats['error'] == 2


def test_get_unchanged_urls(temp_hash_file):
    """Test getting unchanged URLs."""
    manager = HashManager(temp_hash_file)
    
    # Add URLs with different statuses
    manager.update_hash("https://example.com/page1", "Content 1")
    manager.update_hash("https://example.com/page2", "Content 2")
    manager.mark_error("https://example.com/page3", "Error")
    
    # Mark some as unchanged
    manager.hashes["https://example.com/page1"]['status'] = 'unchanged'
    manager.hashes["https://example.com/page2"]['status'] = 'unchanged'
    
    unchanged = manager.get_unchanged_urls()
    
    assert len(unchanged) == 2
    assert "https://example.com/page1" in unchanged
    assert "https://example.com/page2" in unchanged
    assert "https://example.com/page3" not in unchanged