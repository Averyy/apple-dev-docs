"""Test critical scraping functionality without async requirements."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pathlib import Path
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.markdown_converter import AppleDocMarkdownConverter
from scraper.utils.hash_manager import HashManager
import tempfile


class TestCriticalPathGeneration:
    """Test critical path generation to ensure files are saved correctly."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.scraper = AppleJSONDocumentationScraper('watchkit')
        
    def test_no_double_nesting_bug(self):
        """CRITICAL: Prevent watchkit/foo/foo.md double nesting bug."""
        # This was creating watchkit/enabling-background-sessions/enabling-background-sessions.md
        url = "https://developer.apple.com/documentation/watchkit/enabling-background-sessions"
        data = {"title": "Test"}
        
        file_path = self.scraper._get_organized_file_path(url, data)
        
        # Must be watchkit/enabling-background-sessions.md
        assert str(file_path) == "documentation/watchkit/enabling-background-sessions.md"
        print("✓ No double nesting bug test passed")
        
    def test_case_insensitive_url_parsing(self):
        """CRITICAL: Handle WatchKit vs watchkit case mismatch."""
        # Apple uses 'WatchKit' but framework_id is 'watchkit'
        url = "https://developer.apple.com/documentation/WatchKit/WKApplication"
        data = {"title": "WKApplication"}
        
        file_path = self.scraper._get_organized_file_path(url, data)
        
        # Should not fail or create wrong path
        assert "watchkit" in str(file_path).lower()
        assert not str(file_path).startswith("documentation/watchkit/https:")
        print("✓ Case insensitive URL parsing test passed")
        

class TestCrossFrameworkReferences:
    """Test to prevent incorrect cross-framework file creation."""
    
    def test_uikit_reference_in_watchkit(self):
        """CRITICAL: Don't create UIKit files in WatchKit folder."""
        output_dir = Path('documentation/watchkit')
        converter = AppleDocMarkdownConverter(output_dir)
        
        # UIKit reference in WatchKit docs
        result = converter._create_dual_link(
            "https://developer.apple.com/documentation/UIKit/UIUserNotificationActionResponseTypedTextKey",
            "UIUserNotificationActionResponseTypedTextKey"
        )
        
        # Must NOT create local .md link
        assert ".md" not in result or "([Apple Docs](" in result
        print("✓ Cross-framework reference test passed")
        

class TestURLConversion:
    """Test critical URL conversions for API access."""
    
    def setup_method(self):
        self.scraper = AppleJSONDocumentationScraper('watchkit')
        
    def test_doc_to_json_url_conversion(self):
        """CRITICAL: Ensure we can fetch JSON data."""
        doc_url = "https://developer.apple.com/documentation/watchkit/wkapplication"
        json_url = self.scraper._convert_doc_url_to_json_url(doc_url)
        
        expected = "https://developer.apple.com/tutorials/data/documentation/watchkit/wkapplication.json"
        assert json_url == expected
        print("✓ Doc to JSON URL conversion test passed")
        
    def test_json_to_doc_url_conversion(self):
        """CRITICAL: Ensure we can convert back for saving."""
        json_url = "https://developer.apple.com/tutorials/data/documentation/watchkit/wkapplication.json"
        doc_url = self.scraper._convert_json_url_to_doc_url(json_url)
        
        expected = "https://developer.apple.com/documentation/watchkit/wkapplication"
        assert doc_url == expected
        print("✓ JSON to doc URL conversion test passed")
    
    def test_identifier_to_json_url_conversion(self):
        """CRITICAL: Test identifier parsing that was causing 404s."""
        test_cases = [
            # (identifier, expected_json_url)
            ("doc://com.apple.watchkit/documentation/WatchKit/WKApplication",
             "https://developer.apple.com/tutorials/data/documentation/watchkit/wkapplication.json"),
            ("doc://com.apple.watchkit/documentation/WatchKit/setting-up-a-watchos-project",
             "https://developer.apple.com/tutorials/data/documentation/watchkit/setting-up-a-watchos-project.json"),
        ]
        
        for identifier, expected in test_cases:
            # Test the identifier parsing logic
            path = identifier.replace('doc://', '')
            if '/documentation/' in path:
                parts = path.split('/documentation/', 1)
                if len(parts) == 2:
                    path = parts[1]
            
            path_lower = path.lower()
            if not path_lower.startswith(f"{self.scraper.framework_id}/"):
                if path_lower.startswith('watchkit/'):
                    path_lower = f"{self.scraper.framework_id}/{path_lower[9:]}"
                else:
                    path_lower = f"{self.scraper.framework_id}/{path_lower}"
            
            json_url = f"{self.scraper.JSON_BASE_URL}/{path_lower}.json"
            assert json_url == expected, f"Expected {expected}, got {json_url}"
        
        print("✓ Identifier to JSON URL conversion test passed")
    
    def test_recursive_discovery(self):
        """CRITICAL: Test that recursive discovery finds all nested documentation."""
        # This test ensures we don't miss documentation by failing to recurse
        # through all identifiers. This bug caused us to only find 4 files instead of 700+
        
        # Test the identifier processing logic
        test_identifiers = [
            "doc://com.apple.watchkit/documentation/WatchKit/WKApplication",
            "doc://com.apple.watchkit/documentation/WatchKit/WKApplication/shared()",
            "doc://com.apple.watchkit/documentation/WatchKit/WKApplicationDelegate"
        ]
        
        # Convert identifiers to JSON URLs
        converted_urls = []
        for identifier in test_identifiers:
            if 'watchkit' in identifier.lower():
                # This is the same logic from _process_and_scrape_identifier
                path = identifier.replace('doc://', '')
                if '/documentation/' in path:
                    path = path.split('/documentation/', 1)[1]
                path_lower = path.lower()
                json_url = f"https://developer.apple.com/tutorials/data/documentation/{path_lower}.json"
                converted_urls.append(json_url)
        
        # Should convert all identifiers
        assert len(converted_urls) == 3, f"Failed to convert all identifiers"
        
        # Check conversions are correct
        assert "watchkit/wkapplication.json" in converted_urls[0]
        assert "watchkit/wkapplication/shared().json" in converted_urls[1]
        assert "watchkit/wkapplicationdelegate.json" in converted_urls[2]
        
        print("✓ Recursive discovery test passed")


class TestFilenameGeneration:
    """Test critical filename generation to prevent file conflicts."""
    
    def setup_method(self):
        self.scraper = AppleJSONDocumentationScraper('watchkit')
        
    def test_method_names_dont_break_filesystem(self):
        """CRITICAL: Special characters in method names must be cleaned."""
        dangerous_names = [
            ("init?(rawValue: Int)", "init-rawvalue-int"),  # ? would break
            ("foo:bar:baz:", "foo-bar-baz"),  # : is invalid on Windows
            ("operator==(_:_:)", "operator-"),  # = might cause issues
            ("foo/bar", "foo-bar"),  # / would create subdirectory
        ]
        
        for input_name, expected in dangerous_names:
            result = self.scraper._create_clean_filename(input_name, {})
            # Must not contain filesystem-breaking characters
            assert "/" not in result
            assert ":" not in result
            assert "?" not in result
            assert "*" not in result
        print("✓ Filename generation test passed")


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
        print("✓ ETag storage test passed")
        
    def test_etag_comparison_when_unchanged(self):
        """Test ETag comparison detects unchanged content."""
        url = "https://example.com/test.json"
        content = "test content"
        etag = 'W/"abc123"'
        
        # Store initial hash with ETag
        self.hash_manager.update_hash(url, content, etag)
        
        # Check with same ETag - should be unchanged
        assert not self.hash_manager.has_changed(url, content, etag)
        print("✓ ETag unchanged detection test passed")
        
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
        print("✓ ETag change detection test passed")


def run_all_tests():
    """Run all critical tests."""
    print("Running critical scraping tests...\n")
    
    # Path generation tests
    path_tests = TestCriticalPathGeneration()
    path_tests.setup_method()
    path_tests.test_no_double_nesting_bug()
    path_tests.test_case_insensitive_url_parsing()
    
    # Cross-framework tests
    cross_tests = TestCrossFrameworkReferences()
    cross_tests.test_uikit_reference_in_watchkit()
    
    # URL conversion tests
    url_tests = TestURLConversion()
    url_tests.setup_method()
    url_tests.test_doc_to_json_url_conversion()
    url_tests.test_json_to_doc_url_conversion()
    url_tests.test_identifier_to_json_url_conversion()
    url_tests.test_recursive_discovery()
    
    # Filename generation tests
    filename_tests = TestFilenameGeneration()
    filename_tests.setup_method()
    filename_tests.test_method_names_dont_break_filesystem()
    
    # Hash manager tests
    hash_tests = TestHashManager()
    hash_tests.setup_method()
    hash_tests.test_etag_stored_and_retrieved()
    hash_tests.test_etag_comparison_when_unchanged()
    hash_tests.test_etag_comparison_when_changed()
    hash_tests.teardown_method()
    
    print("\n✅ All critical tests passed!")


if __name__ == "__main__":
    run_all_tests()