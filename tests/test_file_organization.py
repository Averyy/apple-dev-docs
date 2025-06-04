"""Test file organization and path generation."""

import pytest
from pathlib import Path
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.markdown_converter import AppleDocMarkdownConverter


class TestFileOrganization:
    """Test that file paths mirror Apple's URL structure correctly."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.scraper = AppleJSONDocumentationScraper('watchkit')
        self.output_dir = Path('documentation/watchkit')
        
    def test_single_level_path(self):
        """Test single-level paths like /documentation/watchkit/enabling-background-sessions."""
        url = "https://developer.apple.com/documentation/watchkit/enabling-background-sessions"
        data = {"title": "Enabling Background Sessions"}
        
        file_path = self.scraper._get_organized_file_path(url, data)
        
        # Should be watchkit/enabling-background-sessions.md, NOT watchkit/enabling-background-sessions/enabling-background-sessions.md
        assert str(file_path) == "documentation/watchkit/enabling-background-sessions.md"
        assert file_path.parts[-2] == "watchkit"  # Parent should be framework
        assert file_path.parts[-1] == "enabling-background-sessions.md"
        
    def test_two_level_path(self):
        """Test two-level paths like /documentation/watchkit/wkapplication/shared."""
        url = "https://developer.apple.com/documentation/watchkit/wkapplication/shared"
        data = {"title": "shared()"}
        
        file_path = self.scraper._get_organized_file_path(url, data)
        
        # Should be watchkit/wkapplication/shared.md
        assert str(file_path) == "documentation/watchkit/wkapplication/shared.md"
        assert file_path.parts[-3] == "watchkit"
        assert file_path.parts[-2] == "wkapplication"
        assert file_path.parts[-1] == "shared.md"
        
    def test_method_with_parameters(self):
        """Test method names with parameters are cleaned properly."""
        url = "https://developer.apple.com/documentation/watchkit/wkalertactionstyle/init(rawValue:)"
        data = {"title": "init(rawValue:)"}
        
        file_path = self.scraper._get_organized_file_path(url, data)
        
        # Should be watchkit/wkalertactionstyle/init-rawvalue.md
        assert str(file_path) == "documentation/watchkit/wkalertactionstyle/init-rawvalue.md"
        assert "?" not in str(file_path)  # No special characters
        assert ":" not in str(file_path)
        assert "(" not in str(file_path)
        
    def test_case_insensitive_framework_matching(self):
        """Test that WatchKit URLs are handled correctly despite case differences."""
        # Apple uses 'WatchKit' but framework_id is 'watchkit'
        url = "https://developer.apple.com/documentation/WatchKit/WKApplication"
        data = {"title": "WKApplication"}
        
        file_path = self.scraper._get_organized_file_path(url, data)
        
        # Should handle case mismatch and create proper path
        assert str(file_path) == "documentation/watchkit/wkapplication.md"
        
    def test_framework_root_page(self):
        """Test the main framework page."""
        url = "https://developer.apple.com/documentation/watchkit"
        data = {"title": "WatchKit"}
        
        file_path = self.scraper._get_organized_file_path(url, data)
        
        # Should be watchkit/watchkit.md
        assert str(file_path) == "documentation/watchkit/watchkit.md"
        
    def test_no_double_nesting(self):
        """Ensure we don't create paths like foo/foo/foo.md."""
        test_cases = [
            ("https://developer.apple.com/documentation/watchkit/background-execution", 
             "documentation/watchkit/background-execution.md"),
            ("https://developer.apple.com/documentation/watchkit/wkinterfacecontroller", 
             "documentation/watchkit/wkinterfacecontroller.md"),
            ("https://developer.apple.com/documentation/watchkit/life-cycles", 
             "documentation/watchkit/life-cycles.md"),
        ]
        
        for url, expected_path in test_cases:
            data = {"title": "Test"}
            file_path = self.scraper._get_organized_file_path(url, data)
            assert str(file_path) == expected_path
            
            # Ensure no segment is repeated
            parts = file_path.parts
            for i in range(len(parts)-1):
                assert parts[i] != parts[i+1].replace('.md', ''), \
                    f"Double nesting detected: {parts[i]} repeated in {file_path}"


class TestCrossFrameworkReferences:
    """Test handling of cross-framework references."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.output_dir = Path('documentation/watchkit')
        self.converter = AppleDocMarkdownConverter(self.output_dir)
        
    def test_cross_framework_reference_no_local_link(self):
        """Test that UIKit references in WatchKit docs don't create local links."""
        link_text = "UIUserNotificationActionResponseTypedTextKey"
        apple_url = "https://developer.apple.com/documentation/UIKit/UIUserNotificationActionResponseTypedTextKey"
        
        result = self.converter._convert_reference_link(link_text, apple_url)
        
        # Should NOT create a local .md link for cross-framework reference
        assert ".md" not in result
        assert "([Apple Docs](" in result
        assert link_text in result
        
    def test_same_framework_reference_creates_local_link(self):
        """Test that same-framework references create local links."""
        link_text = "WKApplication"
        apple_url = "https://developer.apple.com/documentation/watchkit/WKApplication"
        
        result = self.converter._convert_reference_link(link_text, apple_url)
        
        # Should create a local .md link for same-framework reference
        assert "WKApplication.md" in result.lower()
        assert "([Apple Docs](" in result
        
    def test_various_framework_references(self):
        """Test various cross-framework scenarios."""
        test_cases = [
            # (current_framework, url, should_have_local_link)
            ("watchkit", "https://developer.apple.com/documentation/UIKit/UIColor", False),
            ("watchkit", "https://developer.apple.com/documentation/Foundation/NSObject", False),
            ("watchkit", "https://developer.apple.com/documentation/watchkit/WKInterfaceObject", True),
            ("swiftui", "https://developer.apple.com/documentation/SwiftUI/View", True),
            ("swiftui", "https://developer.apple.com/documentation/UIKit/UIView", False),
        ]
        
        for current_framework, url, should_have_local in test_cases:
            converter = AppleDocMarkdownConverter(Path(f'documentation/{current_framework}'))
            result = converter._convert_reference_link("TestLink", url)
            
            if should_have_local:
                assert ".md" in result, f"Expected local link for {url} in {current_framework}"
            else:
                assert ".md" not in result, f"Expected no local link for {url} in {current_framework}"


class TestCleanFilenameGeneration:
    """Test filename cleaning for special characters."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.scraper = AppleJSONDocumentationScraper('watchkit')
        
    def test_method_names_cleaned(self):
        """Test that method names are cleaned properly."""
        test_cases = [
            ("init?(rawValue: Int)", "init-rawvalue-int"),
            ("shared()", "shared"),
            ("applicationDidFinishLaunching()", "applicationdidfinishlaunching"),
            ("addMenuItem(with:title:action:)", "addmenuitem-with-title-action"),
            ("setValue(_:forKey:)", "setvalue-forkey"),
        ]
        
        for input_name, expected_output in test_cases:
            result = self.scraper._create_clean_filename(input_name, {})
            assert result == expected_output, f"Expected {expected_output}, got {result}"
            
    def test_special_characters_removed(self):
        """Test that special characters are removed."""
        test_cases = [
            ("test@property", "testproperty"),
            ("test#method", "testmethod"),
            ("test$var", "testvar"),
            ("test&param", "testparam"),
        ]
        
        for input_name, expected_output in test_cases:
            result = self.scraper._create_clean_filename(input_name, {})
            assert result == expected_output
            
    def test_no_empty_filenames(self):
        """Test that we never get empty filenames."""
        test_cases = ["", "()", "???", "@#$%"]
        
        for input_name in test_cases:
            result = self.scraper._create_clean_filename(input_name, {})
            assert result == "unknown"  # Fallback for empty results


if __name__ == "__main__":
    pytest.main([__file__, "-v"])