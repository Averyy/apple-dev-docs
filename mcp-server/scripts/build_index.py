#!/usr/bin/env python3
"""
Build vector index for Apple documentation with incremental update support.
Uses OpenAI text-embedding-3-small model for consistency with RAG engine.

This script:
1. Scans all markdown files in the documentation directory
2. Tracks file hashes to detect changes
3. Only re-embeds changed or new files
4. Uses OpenAI API for embeddings (text-embedding-3-small)
5. Stores in ChromaDB for fast retrieval
"""

import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

import chromadb
import openai
from tqdm import tqdm

from server.config import (
    COLLECTION_NAME,
    DOCS_PATH,
    EMBEDDING_BATCH_SIZE,
    EMBEDDING_MODEL,
    EMBEDDING_DIMENSIONS,
    OPENAI_API_KEY,
    VECTORSTORE_PATH,
)
from server.logger import get_logger

logger = get_logger(__name__)


class VectorIndexBuilder:
    """Builds and maintains vector index with incremental updates"""
    
    def __init__(self, docs_path: Optional[Path] = None):
        self.docs_path = Path(docs_path) if docs_path else DOCS_PATH
        self.hash_file = VECTORSTORE_PATH / "file_hashes.json"
        
        # Initialize OpenAI client
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY environment variable must be set")
        
        self.openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)
        logger.info(f"OpenAI client initialized with model: {EMBEDDING_MODEL}")
        
        # Initialize ChromaDB
        self.client = chromadb.PersistentClient(path=str(VECTORSTORE_PATH))
        self.collection = None
        self.file_hashes = self._load_hashes()
        
    def _load_hashes(self) -> Dict[str, str]:
        """Load existing file hashes"""
        if self.hash_file.exists():
            try:
                with open(self.hash_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load hashes: {e}")
        return {}
    
    def _save_hashes(self):
        """Save file hashes to disk"""
        self.hash_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.hash_file, 'w') as f:
            json.dump(self.file_hashes, f, indent=2)
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash of file content"""
        content = file_path.read_text(encoding='utf-8')
        return hashlib.sha256(content.encode()).hexdigest()
    
    def _extract_metadata(self, file_path: Path, content: str) -> Dict[str, str]:
        """Extract metadata from markdown file"""
        relative_path = file_path.relative_to(self.docs_path)
        parts = relative_path.parts
        
        # Extract framework name
        framework = parts[0] if parts else "unknown"
        
        # Extract API name from filename
        api_name = file_path.stem
        
        # Check if this is the framework's main page
        is_framework_main = len(parts) == 2 and api_name.lower() == framework.lower()
        
        # Try to extract title from content
        title = api_name
        lines = content.split('\n')
        for line in lines[:10]:  # Check first 10 lines
            if line.startswith('# '):
                title = line[2:].strip()
                break
        
        # Extract platforms
        platforms = self._extract_platforms(content)
        
        # Extract summary (try for all pages, not just main framework pages)
        summary = None
        if is_framework_main:
            summary = self._extract_summary(content)
            # If no overview, try to get first meaningful sentence
            if not summary:
                summary = self._extract_first_sentence(content)
        
        # Build URL (approximate - adjust based on actual URL structure)
        url_parts = [p.lower() for p in parts[:-1]] + [file_path.stem]
        url = f"https://developer.apple.com/documentation/{'/'.join(url_parts)}"
        
        return {
            "framework": framework,
            "api_name": api_name,
            "title": title,
            "file_path": str(file_path),
            "relative_path": str(relative_path),
            "url": url,
            "platforms": platforms,
            "summary": summary,
            "is_framework_main": is_framework_main
        }
    
    def _extract_platforms(self, content: str) -> List[str]:
        """Extract platform availability from markdown content"""
        platforms = []
        
        # Common platform patterns in Apple docs
        # Updated to handle both "13.0+" and "13.0-17.4 Deprecated" formats
        platform_patterns = [
            (r'iOS \d+\.\d+[\+\-–]', 'ios'),
            (r'iPadOS \d+\.\d+[\+\-–]', 'ipados'),
            (r'macOS \d+\.\d+[\+\-–]', 'macos'),
            (r'Mac Catalyst \d+\.\d+[\+\-–]', 'catalyst'),
            (r'tvOS \d+\.\d+[\+\-–]', 'tvos'),
            (r'watchOS \d+\.\d+[\+\-–]', 'watchos'),
            (r'visionOS \d+\.\d+[\+\-–]', 'visionos')
        ]
        
        # Look for availability section (usually in first 30 lines)
        lines = content.split('\n')[:30]
        
        for line in lines:
            for pattern, platform_name in platform_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    if platform_name not in platforms:
                        platforms.append(platform_name)
        
        return platforms
    
    def _extract_summary(self, content: str) -> Optional[str]:
        """Extract first sentence after Overview heading"""
        
        # Find the Overview section
        overview_match = re.search(r'^#+\s*Overview\s*$', content, re.MULTILINE | re.IGNORECASE)
        if not overview_match:
            return None
        
        # Get text after Overview
        overview_start = overview_match.end()
        remaining_content = content[overview_start:].strip()
        
        # Skip empty lines and find first paragraph
        lines = remaining_content.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('-'):
                # Extract first sentence
                # Handle common abbreviations that contain periods
                line = re.sub(r'\be\.g\.\s*', 'eg ', line)
                line = re.sub(r'\bi\.e\.\s*', 'ie ', line)
                line = re.sub(r'\betc\.\s*', 'etc ', line)
                
                # Split on sentence endings
                sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', line)
                if sentences:
                    return sentences[0].strip()
        
        return None
    
    def _extract_first_sentence(self, content: str) -> Optional[str]:
        """Extract first meaningful sentence from content"""
        
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines, headers, and code blocks
            if not line or line.startswith('#') or line.startswith('```') or line.startswith('---'):
                continue
            
            # Skip lines that are just links or metadata
            if line.startswith('[') or line.startswith('**Framework**:') or line.startswith('**Availability**:'):
                continue
            
            # Skip import statements
            if line.startswith('import ') or line.startswith('`import '):
                continue
            
            # Found a potential sentence
            if len(line) > 20:  # Minimum length for a meaningful sentence
                # Clean up the line
                line = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line)  # Remove markdown links
                line = re.sub(r'`([^`]+)`', r'\1', line)  # Remove inline code marks
                
                # Extract first sentence
                sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', line)
                if sentences and len(sentences[0]) > 20:
                    return sentences[0].strip()
        
        return None
    
    def _embed_texts(self, texts: List[str]) -> List[List[float]]:
        """Embed texts using OpenAI API"""
        embeddings = []
        
        # Process in batches
        for i in range(0, len(texts), EMBEDDING_BATCH_SIZE):
            batch = texts[i:i + EMBEDDING_BATCH_SIZE]
            
            try:
                response = self.openai_client.embeddings.create(
                    input=batch,
                    model=EMBEDDING_MODEL
                )
                
                batch_embeddings = [item.embedding for item in response.data]
                embeddings.extend(batch_embeddings)
                
                # Rate limiting (OpenAI has generous limits, but be respectful)
                if i + EMBEDDING_BATCH_SIZE < len(texts):
                    time.sleep(0.1)  # Small delay between batches
                
            except Exception as e:
                logger.error(f"Embedding error: {e}")
                # Return empty embeddings for failed batch
                embeddings.extend([[0.0] * EMBEDDING_DIMENSIONS for _ in batch])
        
        return embeddings
    
    def _find_changed_files(self) -> Tuple[List[Path], List[str]]:
        """Find new or changed markdown files"""
        all_files = []
        changed_files = []
        deleted_ids = []
        
        # Scan all markdown files
        for md_file in self.docs_path.rglob("*.md"):
            all_files.append(md_file)
            
            # Calculate hash
            try:
                current_hash = self._calculate_file_hash(md_file)
                file_key = str(md_file.relative_to(self.docs_path))
                
                # Check if file is new or changed
                if file_key not in self.file_hashes or self.file_hashes[file_key] != current_hash:
                    changed_files.append(md_file)
                    self.file_hashes[file_key] = current_hash
                    
            except Exception as e:
                logger.warning(f"Error processing {md_file}: {e}")
        
        # Find deleted files
        current_files = {str(f.relative_to(self.docs_path)) for f in all_files}
        for file_key in list(self.file_hashes.keys()):
            if file_key not in current_files:
                deleted_ids.append(f"doc_{file_key}")
                del self.file_hashes[file_key]
        
        return changed_files, deleted_ids
    
    def build_index(self, force_rebuild: bool = False):
        """Build or update the vector index"""
        logger.info("Starting vector index build...")
        logger.info(f"Using OpenAI {EMBEDDING_MODEL} with {EMBEDDING_DIMENSIONS} dimensions")
        
        # Get or create collection
        try:
            if force_rebuild:
                logger.info("Force rebuild requested, deleting existing collection...")
                try:
                    self.client.delete_collection(COLLECTION_NAME)
                except:
                    pass
                self.file_hashes = {}
            
            self.collection = self.client.get_or_create_collection(
                name=COLLECTION_NAME,
                metadata={
                    "description": "Apple Developer Documentation",
                    "embedding_model": EMBEDDING_MODEL,
                    "embedding_dimensions": str(EMBEDDING_DIMENSIONS)
                }
            )
            
        except Exception as e:
            logger.error(f"Failed to create collection: {e}")
            return
        
        # Find changed files
        logger.info("Scanning for changes...")
        changed_files, deleted_ids = self._find_changed_files()
        
        # Delete removed documents
        if deleted_ids:
            logger.info(f"Deleting {len(deleted_ids)} removed documents...")
            try:
                self.collection.delete(ids=deleted_ids)
            except Exception as e:
                logger.warning(f"Error deleting documents: {e}")
        
        # Process changed files
        if not changed_files:
            logger.info("No changes detected. Index is up to date!")
            return
        
        logger.info(f"Processing {len(changed_files)} changed/new files...")
        
        # Process in chunks to manage memory
        chunk_size = 100
        total_processed = 0
        
        with tqdm(total=len(changed_files), desc="Indexing files") as pbar:
            for chunk_start in range(0, len(changed_files), chunk_size):
                chunk_files = changed_files[chunk_start:chunk_start + chunk_size]
                
                # Prepare batch data
                contents = []
                metadatas = []
                ids = []
                
                for file_path in chunk_files:
                    try:
                        content = file_path.read_text(encoding='utf-8')
                        metadata = self._extract_metadata(file_path, content)
                        
                        # Use relative path as ID for easy updates
                        doc_id = f"doc_{metadata['relative_path']}"
                        
                        contents.append(content)
                        metadatas.append(metadata)
                        ids.append(doc_id)
                        
                    except Exception as e:
                        logger.warning(f"Error reading {file_path}: {e}")
                        continue
                
                # Embed batch
                if contents:
                    embeddings = self._embed_texts(contents)
                    
                    # Add to collection
                    try:
                        self.collection.upsert(
                            embeddings=embeddings,
                            documents=contents,
                            metadatas=metadatas,
                            ids=ids
                        )
                        total_processed += len(contents)
                        
                    except Exception as e:
                        logger.error(f"Error adding to collection: {e}")
                
                pbar.update(len(chunk_files))
        
        # Save updated hashes
        self._save_hashes()
        
        # Print summary
        logger.info("=" * 60)
        logger.info(f"✅ Indexing complete!")
        logger.info(f"   Total documents: {self.collection.count()}")
        logger.info(f"   Processed this run: {total_processed}")
        logger.info(f"   Deleted: {len(deleted_ids)}")
        logger.info(f"   Embedding model: {EMBEDDING_MODEL}")
        logger.info(f"   Embedding dimensions: {EMBEDDING_DIMENSIONS}")
        
        # Show sample frameworks
        if metadatas:
            frameworks = list(set(m['framework'] for m in metadatas[:100]))
            logger.info(f"   Sample frameworks: {', '.join(frameworks[:5])}")
    
    def verify_index(self):
        """Verify the index with a test query"""
        logger.info("\nVerifying index with test query...")
        
        try:
            # Test embedding
            test_query = "SwiftUI Button view"
            embeddings = self._embed_texts([test_query])
            
            # Query collection
            results = self.collection.query(
                query_embeddings=embeddings,
                n_results=3
            )
            
            if results['documents'][0]:
                logger.info("✅ Index verification successful!")
                logger.info(f"   Test query: '{test_query}'")
                logger.info(f"   Top result: {results['metadatas'][0][0]['title']}")
                logger.info(f"   Framework: {results['metadatas'][0][0]['framework']}")
                logger.info(f"   Platforms: {results['metadatas'][0][0].get('platforms', [])}")
            else:
                logger.warning("⚠️  No results found in index")
                
        except Exception as e:
            logger.error(f"❌ Index verification failed: {e}")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Build vector index for Apple docs using OpenAI embeddings")
    parser.add_argument("--force", action="store_true", help="Force rebuild entire index")
    parser.add_argument("--verify", action="store_true", help="Verify index after building")
    args = parser.parse_args()
    
    # Verify API key
    if not OPENAI_API_KEY:
        print("❌ Error: OPENAI_API_KEY environment variable must be set")
        sys.exit(1)
    
    # Build index
    builder = VectorIndexBuilder()
    builder.build_index(force_rebuild=args.force)
    
    # Optionally verify
    if args.verify:
        builder.verify_index()


if __name__ == "__main__":
    main()