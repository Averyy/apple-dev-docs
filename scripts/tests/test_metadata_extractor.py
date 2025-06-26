#!/usr/bin/env python3
"""Unit tests for metadata extractor."""

import unittest
import tempfile
import os
from pathlib import Path
from metadata_extractor import MetadataExtractor

class TestMetadataExtractor(unittest.TestCase):
    """Test metadata extraction functionality."""
    
    def setUp(self):
        self.extractor = MetadataExtractor()
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_dir)
    
    def create_test_file(self, content: str, path: str = "test.md") -> str:
        """Create a test markdown file."""
        file_path = os.path.join(self.test_dir, path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
        return file_path
    
    def test_extract_api_name(self):
        """Test API name extraction."""
        test_cases = [
            ("# UIView\n\nA view class", "UIView"),
            ("# class MyCustomView\n\nCustom view", "MyCustomView"),
            ("struct ContentView {\n}", "ContentView"),
            ("protocol Drawable {\n}", "Drawable"),
            ("enum State {\n}", "State"),
        ]
        
        for content, expected in test_cases:
            with self.subTest(content=content):
                result = self.extractor.extract_api_name(content, "test.md")
                self.assertEqual(result, expected)
    
    def test_extract_framework(self):
        """Test framework extraction."""
        # Test path-based extraction
        path = "documentation/SwiftUI/View.md"
        result = self.extractor.extract_framework("", path)
        self.assertEqual(result, "SwiftUI")
        
        # Test content-based extraction
        content = "Framework: UIKit\n\nSome content"
        result = self.extractor.extract_framework(content, "test.md")
        self.assertEqual(result, "UIKit")
        
        # Test import-based extraction
        content = "import Foundation\n\nclass MyClass {}"
        result = self.extractor.extract_framework(content, "test.md")
        self.assertEqual(result, "Foundation")
    
    def test_extract_platforms(self):
        """Test platform extraction."""
        test_cases = [
            ("Available on: iOS 15+, macOS 12+", ["iOS", "macOS"]),
            ("Platforms: iOS, tvOS, watchOS", ["iOS", "tvOS", "watchOS"]),
            ("@available(iOS 14, macOS 11, *)", ["iOS", "macOS"]),
            ("![iOS](badge-ios.png) ![macOS](badge-macos.png)", ["iOS", "macOS"]),
            ("`iOS 15.0+` `macOS 12.0+` `Mac Catalyst 15.0+`", ["Mac Catalyst", "iOS", "macOS"]),
        ]
        
        for content, expected in test_cases:
            with self.subTest(content=content):
                result = self.extractor.extract_platforms(content)
                self.assertEqual(sorted(result), sorted(expected))
    
    def test_extract_kind(self):
        """Test API kind extraction."""
        test_cases = [
            ("class MyView: UIView {", "class"),
            ("struct Point {", "struct"),
            ("protocol Drawable {", "protocol"),
            ("enum State {", "enum"),
            ("actor DataManager {", "actor"),
            ("func calculate() -> Int", "function"),
            ("var name: String", "property"),
        ]
        
        for content, expected in test_cases:
            with self.subTest(content=content):
                result = self.extractor.extract_kind(content)
                self.assertEqual(result, expected)
    
    def test_extract_overview(self):
        """Test overview extraction."""
        content = """
# MyClass

## Overview

This is a comprehensive overview that explains what MyClass does.
It can span multiple lines and provides detailed information.

## Usage

Here's how to use it.
"""
        result = self.extractor.extract_overview(content)
        self.assertIn("comprehensive overview", result)
        self.assertIn("MyClass", result)
        self.assertNotIn("Usage", result)
    
    def test_framework_normalization(self):
        """Test framework name normalization."""
        test_cases = [
            ("swiftui", "SwiftUI"),
            ("swift ui", "SwiftUI"),
            ("uikit", "UIKit"),
            ("coredata", "CoreData"),
            ("core data", "CoreData"),
            ("CustomFramework", "CustomFramework"),  # Unknown framework
        ]
        
        for input_name, expected in test_cases:
            with self.subTest(input=input_name):
                result = self.extractor.normalize_framework_name(input_name)
                self.assertEqual(result, expected)
    
    def test_document_id_generation(self):
        """Test document ID generation."""
        test_cases = [
            ("documentation/SwiftUI/View.md", "swiftui_view"),
            ("documentation/UIKit/UIViewController.md", "uikit_uiviewcontroller"),
            ("documentation/Core-Data/NSManagedObject.md", "core_data_nsmanagedobject"),
        ]
        
        for path, expected in test_cases:
            with self.subTest(path=path):
                result = self.extractor.generate_document_id(path)
                self.assertEqual(result, expected)
    
    def test_is_framework_main_page(self):
        """Test framework main page detection."""
        # Test index file
        self.assertTrue(self.extractor.is_framework_main_page("", "documentation/SwiftUI/index.md"))
        self.assertTrue(self.extractor.is_framework_main_page("", "documentation/UIKit/README.md"))
        
        # Test content-based detection
        content = "# SwiftUI Framework\n\nOverview of SwiftUI"
        self.assertTrue(self.extractor.is_framework_main_page(content, "test.md"))
        
        # Test non-main page
        self.assertFalse(self.extractor.is_framework_main_page("class View {}", "View.md"))
    
    def test_complete_metadata_extraction(self):
        """Test complete metadata extraction."""
        content = """# View

A type that represents part of your app's user interface.

## Overview

You create custom views by declaring types that conform to the View protocol.

Platforms: iOS 13+, macOS 10.15+, tvOS 13+, watchOS 6+

Framework: SwiftUI

protocol View {
    associatedtype Body : View
    var body: Self.Body { get }
}
"""
        
        file_path = self.create_test_file(content, "documentation/SwiftUI/View.md")
        metadata = self.extractor.extract_metadata(content, file_path)
        
        # Verify all expected fields
        self.assertEqual(metadata["api_name"], "View")
        self.assertEqual(metadata["framework"], "SwiftUI")
        self.assertEqual(metadata["title"], "View")
        self.assertEqual(metadata["kind"], "protocol")
        self.assertIn("iOS", metadata["platforms"])
        self.assertIn("macOS", metadata["platforms"])
        # Overview should come from the Overview section, not the first paragraph
        self.assertIn("You create custom views", metadata["overview"])
        self.assertFalse(metadata["is_framework_main"])
        self.assertTrue(metadata["url"].endswith("swiftui/view"))

if __name__ == "__main__":
    unittest.main()