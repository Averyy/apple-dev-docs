#!/usr/bin/env python3
"""Process Apple Developer documentation for Meilisearch indexing."""

import os
import re
import hashlib
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import json
from datetime import datetime
from metadata_extractor import MetadataExtractor

class DocumentProcessor:
    """Process and chunk documentation for optimal indexing."""
    
    def __init__(self, chunk_size: int = 50000):  # 50KB default
        """Initialize processor.
        
        Args:
            chunk_size: Maximum size for a single document chunk in bytes
        """
        self.chunk_size = chunk_size
        self.metadata_extractor = MetadataExtractor()
        
    def process_document(self, file_path: str) -> List[Dict[str, Any]]:
        """Process a single documentation file.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            List of document chunks ready for indexing
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata
        metadata = self.metadata_extractor.extract_metadata(content, file_path)
        
        # Check if chunking is needed
        content_size = len(content.encode('utf-8'))
        if content_size <= self.chunk_size:
            # Single document
            return [self._create_document(content, metadata, chunk_index=0, total_chunks=1)]
        else:
            # Need to chunk
            chunks = self._chunk_content(content, metadata)
            return chunks
    
    def _create_document(self, content: str, metadata: Dict[str, Any], 
                        chunk_index: int = 0, total_chunks: int = 1) -> Dict[str, Any]:
        """Create a document ready for Meilisearch.
        
        Args:
            content: The document content
            metadata: Extracted metadata
            chunk_index: Index of this chunk (0-based)
            total_chunks: Total number of chunks for this document
        """
        # Generate document ID
        base_id = metadata.get('id', 'unknown')
        if total_chunks > 1:
            doc_id = f"{base_id}_chunk_{chunk_index}"
        else:
            doc_id = base_id
        
        # Build document starting with metadata
        doc = {**metadata}  # Start with metadata
        
        # Override with our specific values
        doc.update({
            "id": doc_id,
            "content": content,
            "chunk_index": chunk_index,
            "total_chunks": total_chunks,
            "content_hash": self._hash_content(content),
        })
        
        # Clean content for better search
        doc["content_cleaned"] = self._clean_content(content)
        
        # Add chunk relationship if chunked
        if total_chunks > 1:
            doc["parent_id"] = base_id
            doc["is_chunk"] = True
        else:
            doc["is_chunk"] = False
        
        return doc
    
    def _chunk_content(self, content: str, metadata: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Intelligently chunk large content.
        
        Args:
            content: The full document content
            metadata: Document metadata
            
        Returns:
            List of document chunks
        """
        chunks = []
        
        # Try to split by major sections first
        sections = self._split_by_sections(content)
        
        if len(sections) > 1:
            # Process each section
            for i, section in enumerate(sections):
                if len(section.encode('utf-8')) <= self.chunk_size:
                    chunks.append(self._create_document(
                        section, metadata, 
                        chunk_index=i, 
                        total_chunks=len(sections)
                    ))
                else:
                    # Section is still too large, split further
                    sub_chunks = self._split_by_size(section, preserve_blocks=True)
                    for j, sub_chunk in enumerate(sub_chunks):
                        chunks.append(self._create_document(
                            sub_chunk, metadata,
                            chunk_index=len(chunks),
                            total_chunks=-1  # Will update later
                        ))
        else:
            # No clear sections, split by size
            size_chunks = self._split_by_size(content, preserve_blocks=True)
            for i, chunk_content in enumerate(size_chunks):
                chunks.append(self._create_document(
                    chunk_content, metadata,
                    chunk_index=i,
                    total_chunks=len(size_chunks)
                ))
        
        # Update total chunks count
        total = len(chunks)
        for chunk in chunks:
            if chunk["total_chunks"] == -1:
                chunk["total_chunks"] = total
                # Also update is_chunk since we now know total > 1
                if total > 1:
                    chunk["is_chunk"] = True
                    chunk["parent_id"] = metadata.get('id', 'unknown')
        
        return chunks
    
    def _split_by_sections(self, content: str) -> List[str]:
        """Split content by major sections (## headers)."""
        # Split by second-level headers
        pattern = r'^##\s+(.+)$'
        
        sections = []
        current_section = []
        lines = content.split('\n')
        found_first_h2 = False
        
        for line in lines:
            if re.match(pattern, line, re.MULTILINE):
                if found_first_h2 and current_section:
                    # Save previous section
                    sections.append('\n'.join(current_section))
                    current_section = [line]
                else:
                    # First H2 found
                    found_first_h2 = True
                    current_section.append(line)
            else:
                current_section.append(line)
        
        # Add last section
        if current_section and found_first_h2:
            sections.append('\n'.join(current_section))
        
        # If no H2 sections found, return original
        if not sections:
            return [content]
        
        return sections
    
    def _split_by_size(self, content: str, preserve_blocks: bool = True) -> List[str]:
        """Split content by size, trying to preserve code blocks and paragraphs."""
        chunks = []
        current_chunk = []
        current_size = 0
        
        if preserve_blocks:
            # Split by paragraphs and code blocks
            blocks = self._extract_blocks(content)
            
            for block in blocks:
                block_size = len(block.encode('utf-8'))
                
                if current_size + block_size > self.chunk_size and current_chunk:
                    # Start new chunk
                    chunks.append('\n\n'.join(current_chunk))
                    current_chunk = [block]
                    current_size = block_size
                elif block_size > self.chunk_size:
                    # Block itself is too large, split it
                    if current_chunk:
                        chunks.append('\n\n'.join(current_chunk))
                        current_chunk = []
                        current_size = 0
                    
                    # Split large block by lines
                    sub_blocks = self._split_large_block(block)
                    for sub_block in sub_blocks:
                        chunks.append(sub_block)
                else:
                    current_chunk.append(block)
                    current_size += block_size
            
            # Add remaining
            if current_chunk:
                chunks.append('\n\n'.join(current_chunk))
        else:
            # Simple line-based splitting
            lines = content.split('\n')
            for line in lines:
                line_size = len(line.encode('utf-8'))
                
                if current_size + line_size > self.chunk_size and current_chunk:
                    chunks.append('\n'.join(current_chunk))
                    current_chunk = [line]
                    current_size = line_size
                else:
                    current_chunk.append(line)
                    current_size += line_size
            
            if current_chunk:
                chunks.append('\n'.join(current_chunk))
        
        return chunks
    
    def _extract_blocks(self, content: str) -> List[str]:
        """Extract logical blocks (paragraphs, code blocks, etc.)."""
        blocks = []
        current_block = []
        in_code_block = False
        
        lines = content.split('\n')
        
        for line in lines:
            # Check for code block markers
            if line.strip().startswith('```'):
                if in_code_block:
                    # End of code block
                    current_block.append(line)
                    blocks.append('\n'.join(current_block))
                    current_block = []
                    in_code_block = False
                else:
                    # Start of code block
                    if current_block:
                        blocks.append('\n'.join(current_block))
                    current_block = [line]
                    in_code_block = True
            elif in_code_block:
                # Inside code block
                current_block.append(line)
            elif line.strip() == '':
                # Empty line - end of paragraph
                if current_block:
                    blocks.append('\n'.join(current_block))
                    current_block = []
            else:
                # Regular content
                current_block.append(line)
        
        # Add remaining
        if current_block:
            blocks.append('\n'.join(current_block))
        
        return [b for b in blocks if b.strip()]
    
    def _split_large_block(self, block: str) -> List[str]:
        """Split a large block that exceeds chunk size."""
        # This is a fallback for very large blocks
        chunks = []
        lines = block.split('\n')
        current_chunk = []
        current_size = 0
        
        for line in lines:
            line_size = len(line.encode('utf-8'))
            
            if current_size + line_size > self.chunk_size and current_chunk:
                chunks.append('\n'.join(current_chunk))
                current_chunk = [line]
                current_size = line_size
            else:
                current_chunk.append(line)
                current_size += line_size
        
        if current_chunk:
            chunks.append('\n'.join(current_chunk))
        
        return chunks
    
    def _clean_content(self, content: str) -> str:
        """Clean content for better search quality."""
        # Remove multiple spaces
        content = re.sub(r'\s+', ' ', content)
        
        # Remove markdown image syntax but keep alt text
        content = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', content)
        
        # Remove markdown link syntax but keep text
        content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
        
        # Remove HTML comments
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        
        # Remove excess whitespace
        content = ' '.join(content.split())
        
        return content
    
    def _hash_content(self, content: str) -> str:
        """Generate hash of content for change detection."""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    
    def process_directory(self, directory: str, 
                         file_pattern: str = "*.md") -> List[Dict[str, Any]]:
        """Process all matching files in a directory.
        
        Args:
            directory: Directory to process
            file_pattern: Glob pattern for files
            
        Returns:
            List of all processed documents
        """
        from glob import glob
        
        documents = []
        pattern = os.path.join(directory, "**", file_pattern)
        files = glob(pattern, recursive=True)
        
        for file_path in files:
            try:
                docs = self.process_document(file_path)
                documents.extend(docs)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
        
        return documents

def main():
    """CLI for testing document processing."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Process documentation for indexing")
    parser.add_argument("path", help="File or directory to process")
    parser.add_argument("--chunk-size", type=int, default=50000,
                       help="Maximum chunk size in bytes")
    parser.add_argument("--json", action="store_true",
                       help="Output as JSON")
    parser.add_argument("--test", action="store_true",
                       help="Test mode - process but don't save")
    
    args = parser.parse_args()
    
    processor = DocumentProcessor(chunk_size=args.chunk_size)
    
    try:
        if os.path.isfile(args.path):
            documents = processor.process_document(args.path)
        else:
            documents = processor.process_directory(args.path)
        
        if args.json:
            print(json.dumps(documents, indent=2))
        else:
            print(f"Processed {len(documents)} documents")
            for doc in documents[:3]:  # Show first 3
                print(f"\nDocument: {doc['id']}")
                print(f"  Framework: {doc.get('framework', 'N/A')}")
                print(f"  Platforms: {', '.join(doc.get('platforms', []))}")
                print(f"  Chunk: {doc['chunk_index']+1}/{doc['total_chunks']}")
                print(f"  Size: {len(doc['content'])} chars")
        
        if len(documents) > 3:
            print(f"\n... and {len(documents) - 3} more documents")
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())