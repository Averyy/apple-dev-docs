#!/usr/bin/env python3
"""
Test network resilience and HTTP error handling
Critical for production reliability with Apple's APIs
"""

import os
import sys
import time
import json
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock, Mock
import httpx
import pytest

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.hash_manager import HashManager

class TestNetworkErrorHandling:
    """Test network error handling and resilience"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = Path(tempfile.mkdtemp())
        hash_file = self.temp_dir / "test_hashes.json"
        self.hash_manager = HashManager(hash_file)
        
        # Create test scraper instance
        self.scraper = AppleJSONDocumentationScraper("testframework")
        self.scraper.hash_manager = self.hash_manager
    
    def teardown_method(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_http_429_rate_limit_handling(self):
        """Test handling of HTTP 429 rate limit responses"""
        url = "https://developer.apple.com/tutorials/data/documentation/test.json"
        
        # Mock rate limit response
        mock_response = Mock()
        mock_response.status_code = 429
        mock_response.headers = {'Retry-After': '2'}
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "Rate limited", request=Mock(), response=mock_response
        )
        
        with patch('httpx.get', return_value=mock_response) as mock_get:
            # Should handle rate limit gracefully
            result = self.scraper.fetch_page_with_etag(url)
            
            # Should return None and not crash
            assert result is None
            # Should have attempted the request
            assert mock_get.called
        
        print("✓ HTTP 429 rate limit handling test passed")
    
    def test_http_503_server_error_retry(self):
        """Test retry logic for HTTP 503 server errors"""
        url = "https://developer.apple.com/tutorials/data/documentation/test.json"
        
        # Mock server error response
        mock_response = Mock()
        mock_response.status_code = 503
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "Server error", request=Mock(), response=mock_response
        )
        
        with patch('httpx.get', return_value=mock_response) as mock_get:
            with patch('time.sleep') as mock_sleep:  # Skip actual sleep
                result = self.scraper.fetch_page_with_etag(url)
                
                # Should return None after retries
                assert result is None
                # Should have called sleep for backoff
                mock_sleep.assert_called()
        
        print("✓ HTTP 503 server error retry test passed")
    
    def test_network_timeout_handling(self):
        """Test handling of network timeouts"""
        url = "https://developer.apple.com/tutorials/data/documentation/test.json"
        
        # Mock timeout exception
        with patch('httpx.get', side_effect=httpx.TimeoutException("Request timeout")) as mock_get:
            result = self.scraper.fetch_page_with_etag(url)
            
            # Should handle timeout gracefully
            assert result is None
            assert mock_get.called
        
        print("✓ Network timeout handling test passed")
    
    def test_ssl_error_handling(self):
        """Test handling of SSL certificate errors"""
        url = "https://developer.apple.com/tutorials/data/documentation/test.json"
        
        # Mock SSL error
        with patch('httpx.get', side_effect=httpx.SSLError("SSL certificate verification failed")) as mock_get:
            result = self.scraper.fetch_page_with_etag(url)
            
            # Should handle SSL error gracefully
            assert result is None
            assert mock_get.called
        
        print("✓ SSL error handling test passed")
    
    def test_malformed_json_response(self):
        """Test handling of malformed JSON responses"""
        url = "https://developer.apple.com/tutorials/data/documentation/test.json"
        
        # Mock response with invalid JSON
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<!DOCTYPE html><html>Error page</html>"  # HTML instead of JSON
        mock_response.headers = {}
        
        with patch('httpx.get', return_value=mock_response) as mock_get:
            result = self.scraper.fetch_page_with_etag(url)
            
            # Should handle malformed JSON gracefully
            assert result is None
            assert mock_get.called
        
        print("✓ Malformed JSON response test passed")

class TestETagIntegration:
    """Test ETag integration edge cases"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = Path(tempfile.mkdtemp())
        hash_file = self.temp_dir / "test_hashes.json"
        self.hash_manager = HashManager(hash_file)
        
        self.scraper = AppleJSONDocumentationScraper("testframework")
        self.scraper.hash_manager = self.hash_manager
    
    def teardown_method(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_malformed_etag_header(self):
        """Test handling of malformed ETag headers"""
        url = "https://developer.apple.com/tutorials/data/documentation/test.json"
        
        # Mock response with malformed ETag
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'ETag': 'invalid-etag-format'}  # Missing quotes
        mock_response.text = '{"valid": "json"}'
        
        with patch('httpx.get', return_value=mock_response) as mock_get:
            result = self.scraper.fetch_page_with_etag(url)
            
            # Should still work, just treat ETag as-is
            assert result is not None
            assert result["valid"] == "json"
        
        print("✓ Malformed ETag header test passed")
    
    def test_missing_etag_header(self):
        """Test handling when ETag header is missing"""
        url = "https://developer.apple.com/tutorials/data/documentation/test.json"
        
        # Mock response without ETag header
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {}  # No ETag
        mock_response.text = '{"valid": "json"}'
        
        with patch('httpx.get', return_value=mock_response) as mock_get:
            result = self.scraper.fetch_page_with_etag(url)
            
            # Should still work without ETag
            assert result is not None
            assert result["valid"] == "json"
        
        print("✓ Missing ETag header test passed")
    
    def test_etag_storage_corruption(self):
        """Test handling of corrupted ETag storage"""
        # Corrupt the hash file
        with open(self.hash_manager.cache_file, 'w') as f:
            f.write("invalid json content {")
        
        url = "test_url"
        content = "test content"
        
        # Should handle corrupted storage gracefully
        result = self.hash_manager.has_changed(url, content)
        assert result is True  # Should treat as new content
        
        # Should be able to update despite corruption
        self.hash_manager.update_hash(url, content, "test-etag")
        
        print("✓ ETag storage corruption test passed")
    
    def test_concurrent_hash_access(self):
        """Test concurrent access to hash files"""
        import threading
        import queue
        
        results = queue.Queue()
        
        def worker(worker_id):
            try:
                url = f"test_url_{worker_id}"
                content = f"test content {worker_id}"
                etag = f"test-etag-{worker_id}"
                
                # Each worker updates hash
                self.hash_manager.update_hash(url, content, etag)
                
                # Then checks for changes
                changed = self.hash_manager.has_changed(url, content, etag)
                results.put((worker_id, changed))
            except Exception as e:
                results.put((worker_id, f"ERROR: {e}"))
        
        # Start multiple concurrent workers
        threads = []
        for i in range(5):
            t = threading.Thread(target=worker, args=(i,))
            threads.append(t)
            t.start()
        
        # Wait for all to complete
        for t in threads:
            t.join()
        
        # Check results
        while not results.empty():
            worker_id, result = results.get()
            if isinstance(result, str) and result.startswith("ERROR"):
                assert False, f"Worker {worker_id} failed: {result}"
            else:
                assert result is False, f"Worker {worker_id} should see no changes"
        
        print("✓ Concurrent hash access test passed")

class TestRateLimiting:
    """Test rate limiting functionality"""
    
    def setup_method(self):
        """Set up test environment"""
        self.scraper = AppleJSONDocumentationScraper("testframework")
    
    def test_rate_limiter_timing(self):
        """Test rate limiter enforces proper delays"""
        # Set aggressive rate limit for testing
        self.scraper.rate_limiter.min_delay = 0.1
        self.scraper.rate_limiter.max_delay = 0.2
        
        start_time = time.time()
        
        # Make multiple rapid requests
        for i in range(3):
            self.scraper.rate_limiter.wait()
        
        elapsed = time.time() - start_time
        
        # Should have taken at least min_delay * 2 (for the delays between requests)
        expected_min_time = 0.1 * 2  # 2 delays for 3 requests
        assert elapsed >= expected_min_time, f"Rate limiter too fast: {elapsed}s < {expected_min_time}s"
        
        print("✓ Rate limiter timing test passed")
    
    def test_rate_limiter_randomization(self):
        """Test rate limiter adds randomization to avoid thundering herd"""
        self.scraper.rate_limiter.min_delay = 0.1
        self.scraper.rate_limiter.max_delay = 0.2
        self.scraper.rate_limiter.randomize = True
        
        delays = []
        
        # Measure actual delays
        for i in range(5):
            start = time.time()
            self.scraper.rate_limiter.wait()
            delay = time.time() - start
            delays.append(delay)
        
        # Should have some variation in delays
        unique_delays = len(set(f"{d:.3f}" for d in delays))
        assert unique_delays > 1, "Rate limiter should add randomization"
        
        print("✓ Rate limiter randomization test passed")

def run_network_tests():
    """Run all network resilience tests"""
    print("🌐 Testing Network Resilience and Error Handling\n")
    
    test_classes = [TestNetworkErrorHandling, TestETagIntegration, TestRateLimiting]
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
    print(f"NETWORK RESILIENCE TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Tests passed: {total_passed}")
    print(f"Tests failed: {total_failed}")
    print(f"Success rate: {(total_passed/(total_passed+total_failed)*100):.1f}%")
    
    if total_failed == 0:
        print("\n✅ All network resilience tests passed!")
        print("🛡️ Production network reliability verified!")
        return True
    else:
        print(f"\n❌ {total_failed} tests failed")
        return False

if __name__ == "__main__":
    success = run_network_tests()
    sys.exit(0 if success else 1)