#!/usr/bin/env python3
"""Unit tests for MCP server functions."""

import sys
import time
import unittest
from pathlib import Path
from unittest.mock import MagicMock

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from apple_docs_mcp import escape_filter_value, RateLimitMiddleware


class TestEscapeFilterValue(unittest.TestCase):
    """Test filter value escaping and sanitization."""

    def test_escape_quotes(self):
        """Test escaping double quotes."""
        result = escape_filter_value('test"value')
        self.assertEqual(result, 'test\\"value')

    def test_escape_backslashes(self):
        """Test escaping backslashes."""
        result = escape_filter_value("test\\value")
        self.assertEqual(result, "test\\\\value")

    def test_escape_both(self):
        """Test escaping both quotes and backslashes."""
        result = escape_filter_value('test\\"value')
        self.assertEqual(result, 'test\\\\\\"value')

    def test_max_length_truncation(self):
        """Test that values are truncated to max_length."""
        long_value = "a" * 200
        result = escape_filter_value(long_value, max_length=100)
        self.assertEqual(len(result), 100)

    def test_max_length_default(self):
        """Test default max_length of 100."""
        long_value = "a" * 150
        result = escape_filter_value(long_value)
        self.assertEqual(len(result), 100)

    def test_control_char_removal(self):
        """Test that control characters are removed."""
        result = escape_filter_value("test\x00\x01\x02value")
        self.assertEqual(result, "testvalue")

    def test_control_char_null_byte(self):
        """Test null byte removal."""
        result = escape_filter_value("before\x00after")
        self.assertEqual(result, "beforeafter")

    def test_newline_removal(self):
        """Test newline removal (control char)."""
        result = escape_filter_value("line1\nline2")
        self.assertNotIn("\n", result)

    def test_tab_removal(self):
        """Test tab removal (control char)."""
        result = escape_filter_value("col1\tcol2")
        self.assertNotIn("\t", result)

    def test_empty_string(self):
        """Test empty string handling."""
        result = escape_filter_value("")
        self.assertEqual(result, "")

    def test_none_handling(self):
        """Test None handling (returns as-is)."""
        result = escape_filter_value(None)
        self.assertIsNone(result)

    def test_normal_framework_name(self):
        """Test normal framework names pass through."""
        result = escape_filter_value("SwiftUI")
        self.assertEqual(result, "SwiftUI")

    def test_framework_with_hyphen(self):
        """Test framework names with hyphens."""
        result = escape_filter_value("Core-Data")
        self.assertEqual(result, "Core-Data")

    def test_unicode_preserved(self):
        """Test that unicode is preserved (printable chars)."""
        result = escape_filter_value("日本語")
        self.assertEqual(result, "日本語")


class TestRateLimitMiddleware(unittest.TestCase):
    """Test rate limiter functionality."""

    def setUp(self):
        """Set up test middleware."""
        self.app = MagicMock()
        self.middleware = RateLimitMiddleware(
            self.app, requests_per_minute=60, api_key="test_key"
        )

    def test_cleanup_stale_entries_removes_old(self):
        """Test that stale entries are removed."""
        now = time.time()
        old_time = now - 120  # 2 minutes ago (outside 60s window)

        # Add some old entries
        self.middleware.request_counts["192.168.1.1"] = [old_time, old_time]
        self.middleware.request_counts["192.168.1.2"] = [old_time]

        # Add a recent entry
        self.middleware.request_counts["192.168.1.3"] = [now - 30]  # 30s ago

        # Run cleanup
        window_start = now - 60
        self.middleware._cleanup_stale_entries(now, window_start)

        # Old IPs should be removed entirely
        self.assertNotIn("192.168.1.1", self.middleware.request_counts)
        self.assertNotIn("192.168.1.2", self.middleware.request_counts)

        # Recent IP should remain
        self.assertIn("192.168.1.3", self.middleware.request_counts)

    def test_cleanup_stale_entries_updates_timestamp(self):
        """Test that cleanup updates last_cleanup timestamp."""
        now = time.time()
        old_cleanup_time = self.middleware._last_cleanup

        self.middleware._cleanup_stale_entries(now, now - 60)

        self.assertEqual(self.middleware._last_cleanup, now)
        self.assertNotEqual(self.middleware._last_cleanup, old_cleanup_time)

    def test_cleanup_interval_default(self):
        """Test default cleanup interval is 5 minutes."""
        self.assertEqual(self.middleware._cleanup_interval, 300)

    def test_check_rate_limit_allows_under_limit(self):
        """Test that requests under limit are allowed.

        _check_rate_limit returns False when request is allowed (not rate limited).
        """
        # First request should always be allowed
        result = self.middleware._check_rate_limit("192.168.1.1")
        self.assertFalse(result)  # False = allowed

    def test_check_rate_limit_blocks_over_limit(self):
        """Test that requests over limit are blocked.

        _check_rate_limit returns True when rate limit is exceeded (should block).
        """
        client_ip = "192.168.1.1"

        # Fill up the rate limit
        now = time.time()
        self.middleware.request_counts[client_ip] = [now] * 60

        # Next request should be blocked
        result = self.middleware._check_rate_limit(client_ip)
        self.assertTrue(result)  # True = blocked

    def test_check_rate_limit_cleans_old_entries(self):
        """Test that old entries are cleaned for current IP."""
        client_ip = "192.168.1.1"
        now = time.time()

        # Add old entries (outside window)
        self.middleware.request_counts[client_ip] = [now - 120, now - 90]

        # Make a new request
        result = self.middleware._check_rate_limit(client_ip)

        # Old entries should be cleaned, new one added
        self.assertEqual(len(self.middleware.request_counts[client_ip]), 1)
        self.assertFalse(result)  # False = allowed (under limit after cleanup)

    def test_is_authenticated_valid(self):
        """Test valid API key is accepted."""
        request = MagicMock()
        request.headers = {"authorization": "Bearer test_key"}

        result = self.middleware._is_authenticated(request)
        self.assertTrue(result)

    def test_is_authenticated_invalid(self):
        """Test invalid API key is rejected."""
        request = MagicMock()
        request.headers = {"authorization": "Bearer wrong_key"}

        result = self.middleware._is_authenticated(request)
        self.assertFalse(result)

    def test_is_authenticated_missing(self):
        """Test missing API key is rejected."""
        request = MagicMock()
        request.headers = {}

        result = self.middleware._is_authenticated(request)
        self.assertFalse(result)

    def test_is_authenticated_wrong_scheme(self):
        """Test wrong auth scheme is rejected."""
        request = MagicMock()
        request.headers = {"authorization": "Basic test_key"}

        result = self.middleware._is_authenticated(request)
        self.assertFalse(result)

    def test_get_client_ip_direct(self):
        """Test getting client IP from direct connection."""
        request = MagicMock()
        request.headers = {}
        request.client.host = "192.168.1.1"

        result = self.middleware._get_client_ip(request)
        self.assertEqual(result, "192.168.1.1")

    def test_get_client_ip_forwarded(self):
        """Test getting client IP from X-Forwarded-For header."""
        request = MagicMock()
        request.headers = {"x-forwarded-for": "10.0.0.1, 192.168.1.1"}

        result = self.middleware._get_client_ip(request)
        self.assertEqual(result, "10.0.0.1")


if __name__ == "__main__":
    unittest.main()
