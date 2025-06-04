"""Test critical scraping functionality to prevent data loss or incorrect scraping."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pathlib import Path
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.markdown_converter import AppleDocMarkdownConverter


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
        
    def test_case_insensitive_url_parsing(self):
        """CRITICAL: Handle WatchKit vs watchkit case mismatch."""
        # Apple uses 'WatchKit' but framework_id is 'watchkit'
        url = "https://developer.apple.com/documentation/WatchKit/WKApplication"
        data = {"title": "WKApplication"}
        
        file_path = self.scraper._get_organized_file_path(url, data)
        
        # Should not fail or create wrong path
        assert "watchkit" in str(file_path).lower()
        assert not str(file_path).startswith("documentation/watchkit/https:")
        

class TestCrossFrameworkReferences:
    """Test to prevent incorrect cross-framework file creation."""
    
    def test_uikit_reference_in_watchkit(self):
        """CRITICAL: Don't create UIKit files in WatchKit folder."""
        output_dir = Path('documentation/watchkit')
        converter = AppleDocMarkdownConverter(output_dir)
        
        # UIKit reference in WatchKit docs
        result = converter._convert_reference_link(
            "UIUserNotificationActionResponseTypedTextKey",
            "https://developer.apple.com/documentation/UIKit/UIUserNotificationActionResponseTypedTextKey"
        )
        
        # Must NOT create local .md link
        assert ".md" not in result
        assert "([Apple Docs](" in result
        

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
        
    def test_json_to_doc_url_conversion(self):
        """CRITICAL: Ensure we can convert back for saving."""
        json_url = "https://developer.apple.com/tutorials/data/documentation/watchkit/wkapplication.json"
        doc_url = self.scraper._convert_json_url_to_doc_url(json_url)
        
        expected = "https://developer.apple.com/documentation/watchkit/wkapplication"
        assert doc_url == expected


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
            

if __name__ == "__main__":
    pytest.main([__file__, "-v"])