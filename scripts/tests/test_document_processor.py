#!/usr/bin/env python3
"""Unit tests for document processor."""

import unittest
import tempfile
import os
from pathlib import Path
from document_processor import DocumentProcessor

class TestDocumentProcessor(unittest.TestCase):
    """Test document processing functionality."""
    
    def setUp(self):
        self.processor = DocumentProcessor(chunk_size=1000)  # Small chunk size for testing
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_dir)
    
    def create_test_file(self, content: str, filename: str = "test.md") -> str:
        """Create a test markdown file."""
        file_path = os.path.join(self.test_dir, filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
        return file_path
    
    def test_small_document(self):
        """Test processing a small document that doesn't need chunking."""
        content = """# MyClass

A simple class for testing.

## Overview

This is a test class.

Framework: TestKit
Platforms: iOS, macOS
"""
        file_path = self.create_test_file(content)
        docs = self.processor.process_document(file_path)
        
        self.assertEqual(len(docs), 1)
        doc = docs[0]
        
        # Check basic fields
        self.assertEqual(doc["total_chunks"], 1)
        self.assertEqual(doc["chunk_index"], 0)
        self.assertFalse(doc["is_chunk"])
        self.assertIn("content", doc)
        self.assertIn("content_cleaned", doc)
        self.assertIn("content_hash", doc)
    
    def test_large_document_chunking(self):
        """Test chunking of large documents."""
        # Create content larger than chunk size
        section1 = "# Large Document\n\n" + "This is section 1. " * 100
        section2 = "\n\n## Section 2\n\n" + "This is section 2. " * 100
        section3 = "\n\n## Section 3\n\n" + "This is section 3. " * 100
        
        content = section1 + section2 + section3
        file_path = self.create_test_file(content, "documentation/TestKit/LargeClass.md")
        
        docs = self.processor.process_document(file_path)
        
        # Should be split into multiple chunks
        self.assertGreater(len(docs), 1)
        
        # Check chunk relationships
        for i, doc in enumerate(docs):
            self.assertEqual(doc["chunk_index"], i)
            self.assertEqual(doc["total_chunks"], len(docs))
            if len(docs) > 1:
                # Debug print
                if not doc.get("is_chunk"):
                    print(f"Doc {i}: is_chunk={doc.get('is_chunk')}, total_chunks={doc['total_chunks']}")
                self.assertTrue(doc["is_chunk"])
                self.assertEqual(doc["parent_id"], "testkit_largeclass")
    
    def test_code_block_preservation(self):
        """Test that code blocks are preserved during chunking."""
        content = """# Code Example

Some introduction text.

```swift
class MyViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        // This is a long code block
        // with multiple lines
        // that should stay together
        print("Hello, World!")
    }
}
```

More text after the code block.
"""
        
        file_path = self.create_test_file(content)
        docs = self.processor.process_document(file_path)
        
        # Check that code block markers are preserved
        full_content = ' '.join(doc["content"] for doc in docs)
        self.assertIn("```swift", full_content)
        self.assertIn("```", full_content)
    
    def test_content_cleaning(self):
        """Test content cleaning functionality."""
        content = """# Test

![Image Alt Text](image.png)
[Link Text](https://example.com)
<!-- HTML comment -->

Multiple     spaces     here.
"""
        
        file_path = self.create_test_file(content)
        docs = self.processor.process_document(file_path)
        doc = docs[0]
        
        cleaned = doc["content_cleaned"]
        
        # Check cleaning
        self.assertIn("Image Alt Text", cleaned)
        self.assertNotIn("![", cleaned)
        self.assertIn("Link Text", cleaned)
        self.assertNotIn("](", cleaned)
        self.assertNotIn("<!--", cleaned)
        self.assertNotIn("Multiple     spaces", cleaned)
        self.assertIn("Multiple spaces", cleaned)
    
    def test_section_splitting(self):
        """Test splitting by sections."""
        sections = self.processor._split_by_sections("""# Title

## Section 1
Content for section 1.

## Section 2
Content for section 2.

### Subsection
Should be included with Section 2.

## Section 3
Final section.
""")
        
        self.assertEqual(len(sections), 3)
        self.assertIn("Section 1", sections[0])
        self.assertIn("Section 2", sections[1])
        self.assertIn("Subsection", sections[1])
        self.assertIn("Section 3", sections[2])
    
    def test_block_extraction(self):
        """Test block extraction."""
        content = """First paragraph.

Second paragraph with
multiple lines.

```python
def hello():
    print("Hello")
```

Final paragraph."""
        
        blocks = self.processor._extract_blocks(content)
        
        self.assertEqual(len(blocks), 4)
        self.assertIn("First paragraph", blocks[0])
        self.assertIn("multiple lines", blocks[1])
        self.assertIn("```python", blocks[2])
        self.assertIn("Final paragraph", blocks[3])
    
    def test_hash_generation(self):
        """Test content hash generation."""
        content = "Test content"
        hash1 = self.processor._hash_content(content)
        hash2 = self.processor._hash_content(content)
        hash3 = self.processor._hash_content("Different content")
        
        # Same content should produce same hash
        self.assertEqual(hash1, hash2)
        # Different content should produce different hash
        self.assertNotEqual(hash1, hash3)
        # Should be SHA-256 (64 hex chars)
        self.assertEqual(len(hash1), 64)
    
    def test_process_directory(self):
        """Test processing multiple files in a directory."""
        # Create test files
        self.create_test_file("# File 1", "file1.md")
        self.create_test_file("# File 2", "subdir/file2.md")
        self.create_test_file("Not markdown", "file.txt")
        
        docs = self.processor.process_directory(self.test_dir)
        
        # Should process only .md files
        self.assertEqual(len(docs), 2)
        
        # Check that both files were processed
        ids = [doc["id"] for doc in docs]
        self.assertIn("file1", ids[0])
        self.assertIn("file2", ids[1])

if __name__ == "__main__":
    unittest.main()