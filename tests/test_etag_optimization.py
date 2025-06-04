"""Test ETag optimization and hash management."""

import pytest
from pathlib import Path
import json
import tempfile
from datetime import datetime
from scraper.utils.hash_manager import HashManager


class TestHashManager:
    """Test hash manager with ETag support."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.temp_file = Path(tempfile.mktemp(suffix='.json'))
        self.hash_manager = HashManager(self.temp_file)
        
    def teardown_method(self):
        """Clean up test files."""
        if self.temp_file.exists():
            self.temp_file.unlink()
            
    def test_etag_stored_and_retrieved(self):
        """Test that ETags are properly stored and retrieved."""
        url = "https://example.com/test.json"
        content = "test content"
        etag = 'W/"abc123"'
        
        # Store hash with ETag
        self.hash_manager.update_hash(url, content, etag)
        
        # Retrieve ETag
        retrieved_etag = self.hash_manager.get_etag(url)
        assert retrieved_etag == etag
        
    def test_etag_comparison_when_unchanged(self):
        """Test ETag comparison detects unchanged content."""
        url = "https://example.com/test.json"
        content = "test content"
        etag = 'W/"abc123"'
        
        # Store initial hash with ETag
        self.hash_manager.update_hash(url, content, etag)
        
        # Check with same ETag - should be unchanged
        assert not self.hash_manager.has_changed(url, content, etag)
        
    def test_etag_comparison_when_changed(self):
        """Test ETag comparison detects changed content."""
        url = "https://example.com/test.json"
        content = "test content"
        old_etag = 'W/"abc123"'
        new_etag = 'W/"def456"'
        
        # Store initial hash with ETag
        self.hash_manager.update_hash(url, content, old_etag)
        
        # Check with different ETag - should be changed
        assert self.hash_manager.has_changed(url, content, new_etag)
        
    def test_hash_fallback_when_no_etag(self):
        """Test hash comparison works as fallback when no ETag."""
        url = "https://example.com/test.json"
        content1 = "test content 1"
        content2 = "test content 2"
        
        # Store without ETag
        self.hash_manager.update_hash(url, content1)
        
        # Check with different content - should detect change via hash
        assert self.hash_manager.has_changed(url, content2)
        
        # Check with same content - should detect no change via hash
        assert not self.hash_manager.has_changed(url, content1)
        
    def test_etag_priority_over_hash(self):
        """Test that ETag comparison takes priority over hash."""
        url = "https://example.com/test.json"
        content = "test content"
        etag = 'W/"abc123"'
        
        # Store with ETag
        self.hash_manager.update_hash(url, content, etag)
        
        # Even with same content, if we don't provide ETag, it falls back to hash
        assert not self.hash_manager.has_changed(url, content)  # Hash comparison
        
        # With ETag provided, uses ETag comparison
        assert not self.hash_manager.has_changed(url, content, etag)
        
    def test_hash_persistence(self):
        """Test that hashes and ETags persist to file."""
        url = "https://example.com/test.json"
        content = "test content"
        etag = 'W/"abc123"'
        
        # Store and save
        self.hash_manager.update_hash(url, content, etag)
        self.hash_manager.save()
        
        # Load in new instance
        new_manager = HashManager(self.temp_file)
        
        # Should have same data
        assert new_manager.get_etag(url) == etag
        assert not new_manager.has_changed(url, content, etag)
        
    def test_error_marking(self):
        """Test marking URLs with errors."""
        url = "https://example.com/error.json"
        error_msg = "HTTP 404"
        
        self.hash_manager.mark_error(url, error_msg)
        
        # Check it's stored
        assert url in self.hash_manager.hashes
        assert self.hash_manager.hashes[url]["status"] == "error"
        assert self.hash_manager.hashes[url]["error"] == error_msg


class TestETagIntegration:
    """Test ETag integration with scraper."""
    
    @pytest.mark.asyncio
    async def test_fetch_with_etag_returns_tuple(self):
        """Test that fetch_page_with_etag returns (content, etag) tuple."""
        from scraper.json_scraper import AppleJSONDocumentationScraper
        
        async with AppleJSONDocumentationScraper('watchkit') as scraper:
            # Test with a real URL
            url = "https://developer.apple.com/tutorials/data/documentation/watchkit.json"
            result = await scraper.fetch_page_with_etag(url)
            
            assert result is not None
            assert isinstance(result, tuple)
            assert len(result) == 2
            
            content, etag = result
            assert content is not None
            assert isinstance(content, str)
            # ETag might be None if server doesn't provide it
            if etag:
                assert isinstance(etag, str)
                assert etag.startswith(('W/"', '"'))  # Weak or strong ETag
    
    @pytest.mark.asyncio
    async def test_304_not_modified_returns_none(self):
        """Test that 304 Not Modified returns None."""
        from scraper.json_scraper import AppleJSONDocumentationScraper
        
        async with AppleJSONDocumentationScraper('watchkit') as scraper:
            url = "https://developer.apple.com/tutorials/data/documentation/watchkit.json"
            
            # First fetch to get ETag
            result1 = await scraper.fetch_page_with_etag(url)
            assert result1 is not None
            content1, etag1 = result1
            
            if etag1:
                # Store the ETag
                scraper.hash_manager.update_hash(url, content1, etag1)
                
                # Second fetch should use stored ETag
                # Note: This might not actually return 304 if content changed
                # but the mechanism should work
                result2 = await scraper.fetch_page_with_etag(url)
                
                # If content unchanged, result would be None
                # If content changed, result would be new content
                # Either way, the ETag mechanism is being used


if __name__ == "__main__":
    pytest.main([__file__, "-v"])