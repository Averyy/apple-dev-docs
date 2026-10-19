#!/usr/bin/env python3
"""Unit tests for document processor."""

import unittest
import tempfile
import os
import hashlib
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
        # NOTE: content_cleaned was removed to reduce document size by ~50%
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
        parent_id = hashlib.sha1(b"documentation/TestKit/LargeClass.md").hexdigest()
        for i, doc in enumerate(docs):
            self.assertEqual(doc["chunk_index"], i)
            self.assertEqual(doc["total_chunks"], len(docs))
            self.assertEqual(doc["id"], f"{parent_id}_chunk_{i}")
            if len(docs) > 1:
                # Debug print
                if not doc.get("is_chunk"):
                    print(f"Doc {i}: is_chunk={doc.get('is_chunk')}, total_chunks={doc['total_chunks']}")
                self.assertTrue(doc["is_chunk"])
                self.assertEqual(doc["parent_id"], parent_id)
        self.assertEqual("\n".join(doc["content"] for doc in docs), content)

    def test_split_sections_give_every_chunk_its_own_id(self) -> None:
        """A section split by size among whole ones: unique ids, sequential indexes, one total."""
        content = ("# Mixed\n\nIntro.\n\n## Small\n\nShort section.\n\n## Big\n\n"
                   + "\n\n".join(f"Paragraph {n}. " + "word " * 60 for n in range(12))
                   + "\n\n## Tail\n\nLast section.\n")
        file_path = self.create_test_file(content, "documentation/TestKit/Mixed.md")
        docs = self.processor.process_document(file_path)
        
        self.assertGreater(len(docs), 4)
        ids = [doc["id"] for doc in docs]
        self.assertEqual(len(set(ids)), len(ids))
        self.assertEqual([doc["chunk_index"] for doc in docs], list(range(len(docs))))
        self.assertTrue(all(doc["total_chunks"] == len(docs) and doc["is_chunk"] for doc in docs))
        self.assertTrue(all(len(doc["content"].encode("utf-8")) <= 1000 for doc in docs))
        # Joined in order, the chunks are the file exactly
        self.assertEqual("\n".join(doc["content"] for doc in docs), content)
        # The same file gives the same documents
        self.assertEqual(self.processor.process_document(file_path), docs)

    def test_oversized_block_after_another_block_is_split(self) -> None:
        """A block larger than a chunk is split even when it doesn't come first."""
        table = "\n".join(f"| row {n} | " + "cell " * 20 + "|" for n in range(40))  # one ~4.5 KB block
        content = "# Table\n\nA short paragraph first.\n\n" + table + "\n\nAfter the table.\n"
        file_path = self.create_test_file(content, "documentation/TestKit/Table.md")
        docs = self.processor.process_document(file_path)
        
        self.assertGreater(len(docs), 4)
        # At most a chunk's size plus the line breaks between its lines (not counted)
        self.assertTrue(all(len(doc["content"].encode("utf-8")) <= 1000 + 10 for doc in docs))
        self.assertEqual("\n".join(doc["content"] for doc in docs), content)
    
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
        """Test content cleaning functionality.

        NOTE: content_cleaned field was removed to reduce document size by ~50%.
        This test now verifies that the raw content is preserved correctly.
        """
        content = """# Test

![Image Alt Text](image.png)
[Link Text](https://example.com)
<!-- HTML comment -->

Multiple     spaces     here.
"""

        file_path = self.create_test_file(content)
        docs = self.processor.process_document(file_path)
        doc = docs[0]

        # Verify content is preserved (cleaning removed for size optimization)
        self.assertIn("content", doc)
        self.assertIn("# Test", doc["content"])
    
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
        # Blank lines stay with their blocks: joined, the blocks are the content
        self.assertEqual("\n".join(blocks), content)

    def test_block_extraction_keeps_every_line(self) -> None:
        """Leading, repeated and whitespace-only blank lines, and a fence right after text."""
        content = "\n\nIntro line\n```swift\nlet x = 1\n\nlet y = 2\n```\n  \n\n\nNext\nparagraph\n\n"
        blocks = self.processor._extract_blocks(content)
        
        self.assertEqual(len(blocks), 3)
        self.assertTrue(blocks[0].endswith("Intro line"))
        self.assertTrue(blocks[1].startswith("```swift") and "let y = 2" in blocks[1])
        self.assertTrue(blocks[2].startswith("Next"))
        self.assertEqual("\n".join(blocks), content)
    
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
        # Create test files: two of the same name, outside a documentation dir
        paths = [self.create_test_file("# File 1", "file1.md"),
                 self.create_test_file("# File 1", "subdir/file1.md"),
                 self.create_test_file("# File 2", "subdir/file2.md")]
        self.create_test_file("Not markdown", "file.txt")
        
        docs = self.processor.process_directory(self.test_dir)
        
        # Should process only .md files
        self.assertEqual(len(docs), 3)
        
        # Check that every file was processed, each with its own file_path (the whole
        # path, without a documentation dir) and id
        self.assertEqual(sorted(doc["file_path"] for doc in docs), sorted(Path(p).as_posix() for p in paths))
        self.assertEqual(len({doc["id"] for doc in docs}), 3)

if __name__ == "__main__":
    unittest.main()