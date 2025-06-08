#!/usr/bin/env python3
"""
Build vector index for Apple documentation using Voyage AI embeddings.

This script:
1. Scans all markdown files in the documentation directory
2. Tracks file hashes to detect changes
3. Only re-embeds changed or new files
4. Uses Voyage AI API for embeddings (voyage-3-lite)
5. Stores in ChromaDB for fast retrieval
"""

import hashlib
import json
import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

import chromadb
import voyageai
from tqdm import tqdm

from server.config import (
    COLLECTION_NAME,
    DOCS_PATH,
    EMBEDDING_BATCH_SIZE,
    EMBEDDING_MODEL,
    VECTORSTORE_PATH,
    VOYAGE_API_KEY,
)
from server.logger import get_logger

logger = get_logger(__name__)


class VectorIndexBuilder:
    """Builds and maintains vector index with incremental updates"""
    
    def __init__(self, docs_path: Optional[Path] = None):
        self.docs_path = Path(docs_path) if docs_path else DOCS_PATH
        self.hash_file = VECTORSTORE_PATH / "file_hashes.json"
        self.client = chromadb.PersistentClient(path=str(VECTORSTORE_PATH))
        self.collection = None
        self.file_hashes = self._load_hashes()
        
        # Initialize Voyage AI client
        if not VOYAGE_API_KEY:
            raise ValueError("VOYAGE_API_KEY not found in environment. Please add it to your .env file.")
        
        self.voyage = voyageai.Client(api_key=VOYAGE_API_KEY)
        logger.info(f"Using Voyage AI model: {EMBEDDING_MODEL}")
        
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
        
        # Try to extract title from content
        title = api_name
        lines = content.split('\n')
        for line in lines[:10]:  # Check first 10 lines
            if line.startswith('# '):
                title = line[2:].strip()
                break
        
        # Build URL (approximate - adjust based on actual URL structure)
        url_parts = [p.lower() for p in parts[:-1]] + [file_path.stem]
        url = f"https://developer.apple.com/documentation/{'/'.join(url_parts)}"
        
        return {
            "framework": framework,
            "api_name": api_name,
            "title": title,
            "file_path": str(file_path),
            "relative_path": str(relative_path),
            "url": url
        }
    
    def _embed_texts(self, texts: List[str]) -> List[List[float]]:
        """Embed texts using Voyage AI"""
        embeddings = []
        
        # Process in batches
        for i in range(0, len(texts), EMBEDDING_BATCH_SIZE):
            batch = texts[i:i + EMBEDDING_BATCH_SIZE]
            
            try:
                # Voyage AI embedding call
                result = self.voyage.embed(
                    batch, 
                    model=EMBEDDING_MODEL,
                    input_type="document"  # Optimized for document retrieval
                )
                
                # Extract embeddings from response
                batch_embeddings = [emb for emb in result.embeddings]
                embeddings.extend(batch_embeddings)
                
                # Small delay to avoid rate limits
                if i + EMBEDDING_BATCH_SIZE < len(texts):
                    time.sleep(0.1)  # 100ms between batches
                
            except Exception as e:
                logger.error(f"Embedding error: {e}")
                # Return zero embeddings for failed batch
                embeddings.extend([[0.0] * 512 for _ in batch])  # voyage-3-lite has 512 dims
        
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
        logger.info("Starting vector index build with Voyage AI...")
        logger.info(f"Model: {EMBEDDING_MODEL} (512 dimensions)")
        logger.info(f"Batch size: {EMBEDDING_BATCH_SIZE}")
        
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
                    "embedding_dimensions": 512
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
        logger.info(f"Estimated cost: ${len(changed_files) * 1050 * 0.02 / 1_000_000:.2f}")
        
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
            else:
                logger.warning("⚠️  No results found in index")
                
        except Exception as e:
            logger.error(f"❌ Index verification failed: {e}")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Build vector index for Apple docs using Voyage AI")
    parser.add_argument("--force", action="store_true", help="Force rebuild entire index")
    parser.add_argument("--verify", action="store_true", help="Verify index after building")
    args = parser.parse_args()
    
    # Build index
    builder = VectorIndexBuilder()
    builder.build_index(force_rebuild=args.force)
    
    # Optionally verify
    if args.verify:
        builder.verify_index()


if __name__ == "__main__":
    main()