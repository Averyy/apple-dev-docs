#!/usr/bin/env python3
"""
Incremental embedding generation with hash-based change detection
Only processes new or modified files, saving significant costs
"""

import os
import sys
import re
import time
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional, Set, Tuple
import chromadb
import openai
from tqdm import tqdm
import logging
from dotenv import load_dotenv
import tiktoken

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from scraper.utils.hash_manager import HashManager

# Disable ChromaDB telemetry
os.environ["ANONYMIZED_TELEMETRY"] = "False"

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Security Configuration (same as secure version)
MAX_COST_LIMIT = float(os.getenv("MAX_EMBEDDING_COST", "10.00"))
MAX_FILES_TO_PROCESS = int(os.getenv("MAX_FILES_TO_EMBED", "350000"))
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE_MB", "10")) * 1024 * 1024
MAX_TOKENS_PER_DOC = int(os.getenv("MAX_TOKENS_PER_DOC", "8000"))
# Reduce request rate to avoid 429 errors
REQUESTS_PER_MINUTE = int(os.getenv("OPENAI_RPM", "1000"))  # More conservative: 1000 RPM instead of 3000
MIN_REQUEST_INTERVAL = 60.0 / REQUESTS_PER_MINUTE  # 0.06 seconds between requests

# Load environment variables
env_paths = [
    Path(__file__).parent.parent / ".env"
]

for env_path in env_paths:
    if env_path.exists():
        load_dotenv(env_path)
        logger.info(f"Loaded environment from {env_path}")
        break

class IncrementalEmbeddingBuilder:
    """Manages incremental embedding generation with change detection"""
    
    def __init__(self, docs_path: Path, vectorstore_path: Path):
        self.docs_path = docs_path
        self.vectorstore_path = vectorstore_path
        self.hash_file = Path(__file__).parent.parent / ".hashes" / "embedding_hashes.json"
        self.checkpoint_file = Path(__file__).parent.parent / ".hashes" / "embedding_checkpoint.json"
        self.hash_manager = HashManager(self.hash_file)
        self.processed_ids = set()
        
    def save_checkpoint(self, batch_index: int, total_batches: int, processed_files: List[str]):
        """Save checkpoint for resume capability"""
        checkpoint_data = {
            "timestamp": time.time(),
            "batch_index": batch_index,
            "total_batches": total_batches,
            "processed_files": processed_files,
            "last_hash_save": self.hash_manager.cache_file.stat().st_mtime if self.hash_manager.cache_file.exists() else 0
        }
        
        try:
            self.checkpoint_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.checkpoint_file, 'w') as f:
                json.dump(checkpoint_data, f, indent=2)
            logger.debug(f"Checkpoint saved: batch {batch_index}/{total_batches}")
        except Exception as e:
            logger.warning(f"Failed to save checkpoint: {e}")
    
    def load_checkpoint(self) -> Optional[Dict[str, Any]]:
        """Load checkpoint if it exists and is recent"""
        if not self.checkpoint_file.exists():
            return None
        
        try:
            with open(self.checkpoint_file, 'r') as f:
                checkpoint = json.load(f)
            
            # Check if checkpoint is recent (within last hour)
            age = time.time() - checkpoint.get("timestamp", 0)
            if age > 3600:  # 1 hour
                logger.info("Checkpoint is too old, starting fresh")
                return None
            
            logger.info(f"Found checkpoint: batch {checkpoint['batch_index']}/{checkpoint['total_batches']}")
            return checkpoint
        except Exception as e:
            logger.warning(f"Failed to load checkpoint: {e}")
            return None
    
    def clear_checkpoint(self):
        """Clear checkpoint file after successful completion"""
        try:
            if self.checkpoint_file.exists():
                self.checkpoint_file.unlink()
                logger.debug("Checkpoint cleared")
        except Exception as e:
            logger.warning(f"Failed to clear checkpoint: {e}")
    
    def verify_embedding(self, collection, doc_id: str, original_content: str) -> bool:
        """Verify that an embedding was stored correctly"""
        try:
            # Get the embedding we just stored
            result = collection.get(ids=[doc_id], include=["documents"])
            
            if not result["ids"]:
                logger.warning(f"Embedding not found for ID: {doc_id}")
                return False
            
            stored_content = result["documents"][0]
            
            # Check if content matches
            if stored_content != original_content:
                logger.warning(f"Content mismatch for ID: {doc_id}")
                return False
            
            logger.debug(f"Embedding verified: {doc_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to verify embedding {doc_id}: {e}")
            return False
    
    def verify_embeddings_batch(self, collection, batch_ids: List[str], batch_contents: List[str]) -> Tuple[int, int]:
        """Verify a batch of embeddings"""
        verified = 0
        failed = 0
        
        for doc_id, content in zip(batch_ids, batch_contents):
            if self.verify_embedding(collection, doc_id, content):
                verified += 1
            else:
                failed += 1
        
        return verified, failed
        
    def configure_openai(self):
        """Configure OpenAI API with security checks"""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable must be set")
        
        if not api_key.startswith("sk-") or len(api_key) < 20:
            raise ValueError("Invalid OpenAI API key format")
        
        client = openai.OpenAI(api_key=api_key)
        logger.info("OpenAI API configured")
        return client
    
    def get_existing_ids(self, collection) -> Set[str]:
        """Get all document IDs currently in the collection"""
        try:
            # Get all IDs from collection
            result = collection.get(include=[])  # Just get IDs, no data
            return set(result['ids'])
        except Exception as e:
            logger.warning(f"Failed to get existing IDs: {e}")
            return set()
    
    def validate_framework_name(self, name: str) -> bool:
        """Validate framework name to prevent path traversal"""
        if not name:
            return True
        
        if not re.match(r'^[a-zA-Z0-9_-]+$', name):
            raise ValueError(f"Invalid framework name: {name}")
        
        if ".." in name or "/" in name or "\\" in name:
            raise ValueError(f"Path traversal not allowed: {name}")
        
        return True
    
    def validate_collection_name(self, name: str) -> str:
        """Validate and sanitize ChromaDB collection name"""
        sanitized = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
        sanitized = sanitized[:63]
        sanitized = re.sub(r'^[^a-zA-Z0-9]+', '', sanitized)
        sanitized = re.sub(r'[^a-zA-Z0-9]+$', '', sanitized)
        
        if len(sanitized) < 3:
            sanitized = f"col_{sanitized}"
        
        return sanitized
    
    def generate_doc_id(self, file_path: Path, content: str) -> str:
        """Generate consistent document ID based on file path and content"""
        # Use file path for consistency across runs
        path_hash = hashlib.md5(str(file_path).encode()).hexdigest()[:8]
        # Include content hash to detect changes
        content_hash = hashlib.md5(content.encode()).hexdigest()[:8]
        return f"{file_path.stem}_{path_hash}_{content_hash}"
    
    def count_tokens_safe(self, text: str) -> int:
        """Count tokens with error handling"""
        try:
            encoding = tiktoken.get_encoding("cl100k_base")
            # Count all tokens, don't truncate for counting
            return len(encoding.encode(text))
        except Exception as e:
            logger.warning(f"Token counting failed: {e}, estimating")
            return len(text) // 4
    
    def split_by_headers(self, content: str, max_tokens: int = 7000) -> List[str]:
        """Split large markdown documents by headers to fit token limits
        
        Args:
            content: Markdown content to split
            max_tokens: Maximum tokens per chunk (default 7000)
            
        Returns:
            List of content chunks, each with title context preserved
        """
        # If content is small enough, return as-is
        if self.count_tokens_safe(content) <= max_tokens:
            return [content]
        
        # Try different header levels in order
        for header_level in ['## ', '### ', '#### ', '##### ']:
            if f'\n{header_level}' in content:
                parts = content.split(f'\n{header_level}', 1)
                if len(parts) == 2:
                    title_section = parts[0]
                    remaining = header_level + parts[1]
                    sections = re.split(rf'\n(?={re.escape(header_level)})', remaining)
                    
                    # If we got reasonable sections, use them
                    if len(sections) > 1:
                        break
        else:
            # No headers found, split by size
            logger.warning(f"Large document with no headers, splitting by size")
            return self._split_by_size(content, max_tokens)
        
        chunks = []
        current_chunk = title_section
        current_tokens = self.count_tokens_safe(current_chunk)
        
        for section in sections:
            section_tokens = self.count_tokens_safe(section)
            
            # If adding section would exceed limit, save current chunk
            if current_tokens + section_tokens > max_tokens and current_chunk != title_section:
                chunks.append(current_chunk)
                # Start new chunk with title for context
                current_chunk = title_section + '\n' + section
                current_tokens = self.count_tokens_safe(current_chunk)
            else:
                current_chunk += '\n' + section
                current_tokens += section_tokens
        
        # Add final chunk
        if current_chunk and current_chunk != title_section:
            chunks.append(current_chunk)
        
        # Check if any chunks are still too big and split them further
        final_chunks = []
        for chunk in chunks:
            if self.count_tokens_safe(chunk) > max_tokens:
                logger.warning(f"Chunk still too large ({self.count_tokens_safe(chunk)} tokens), splitting by size")
                final_chunks.extend(self._split_by_size(chunk, max_tokens))
            else:
                final_chunks.append(chunk)
        
        return final_chunks
    
    def _split_by_size(self, content: str, max_tokens: int) -> List[str]:
        """Split content by size when no headers are available"""
        chunks = []
        lines = content.split('\n')
        current_chunk = []
        current_tokens = 0
        
        for line in lines:
            line_tokens = self.count_tokens_safe(line)
            if current_tokens + line_tokens > max_tokens and current_chunk:
                # Save current chunk
                chunks.append('\n'.join(current_chunk))
                current_chunk = [line]
                current_tokens = line_tokens
            else:
                current_chunk.append(line)
                current_tokens += line_tokens
        
        # Add final chunk
        if current_chunk:
            chunks.append('\n'.join(current_chunk))
        
        return chunks
    
    def scan_for_changes(self, framework_filter: Optional[str] = None) -> Dict[str, Any]:
        """Scan documents and identify which need embedding"""
        stats = {
            "total": 0,
            "unchanged": 0,
            "changed": 0,
            "new": 0,
            "deleted": 0,
            "files_to_process": []
        }
        
        if framework_filter:
            self.validate_framework_name(framework_filter)
        
        pattern = f"{framework_filter}/**/*.md" if framework_filter else "**/*.md"
        
        logger.info("Scanning for changes...")
        
        # Track all current files
        current_files = set()
        
        for md_file in self.docs_path.glob(pattern):
            if stats["total"] >= MAX_FILES_TO_PROCESS:
                logger.warning(f"Reached maximum file limit: {MAX_FILES_TO_PROCESS}")
                break
            
            stats["total"] += 1
            current_files.add(str(md_file))
            
            try:
                # Check file size
                if md_file.stat().st_size > MAX_FILE_SIZE:
                    logger.warning(f"Skipping large file: {md_file}")
                    continue
                
                # Read content
                content = md_file.read_text(encoding='utf-8')
                
                # Check if content has changed
                file_key = str(md_file.relative_to(self.docs_path))
                
                if self.hash_manager.has_changed(file_key, content):
                    if file_key in self.hash_manager.hashes:
                        stats["changed"] += 1
                        logger.debug(f"Changed: {file_key}")
                    else:
                        stats["new"] += 1
                        logger.debug(f"New: {file_key}")
                    
                    stats["files_to_process"].append({
                        "path": md_file,
                        "content": content,
                        "key": file_key,
                        "tokens": self.count_tokens_safe(content)
                    })
                else:
                    stats["unchanged"] += 1
                    
            except Exception as e:
                logger.warning(f"Error processing {md_file}: {e}")
        
        # Check for deleted files
        stored_files = set(self.hash_manager.hashes.keys())
        if framework_filter:
            # Only check files in the filtered framework
            stored_files = {f for f in stored_files if f.startswith(framework_filter + "/")}
        
        deleted_files = stored_files - {str(Path(f["path"]).relative_to(self.docs_path)) 
                                       for f in stats["files_to_process"]}
        deleted_files = deleted_files - {str(Path(p).relative_to(self.docs_path)) 
                                        for p in current_files}
        stats["deleted"] = len(deleted_files)
        
        return stats, list(deleted_files)
    
    def estimate_cost(self, files_to_process: List[Dict[str, Any]]) -> float:
        """Estimate embedding cost accounting for document splitting"""
        total_tokens = 0
        
        for f in files_to_process:
            content_length = len(f["content"])
            
            # Account for splitting
            if content_length > 30000:
                # Estimate chunks (conservative: assume 3-4 chunks for large files)
                estimated_chunks = max(2, content_length // 25000)
                # Each chunk will have ~7000 tokens max
                total_tokens += estimated_chunks * 7000
            else:
                # Use actual token count for normal files
                total_tokens += f["tokens"]
        
        return (total_tokens / 1_000_000) * 0.02
    
    def embed_batch_secure(self, client: openai.OpenAI, texts: List[str], 
                          batch_size: int = 100, rate_limiter: Dict[str, float] = None) -> List[List[float]]:
        """Generate embeddings with rate limiting"""
        embeddings = []
        
        if rate_limiter is None:
            rate_limiter = {"last_request": 0}
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            
            # Rate limiting
            elapsed = time.time() - rate_limiter["last_request"]
            if elapsed < MIN_REQUEST_INTERVAL:
                sleep_time = MIN_REQUEST_INTERVAL - elapsed
                time.sleep(sleep_time)
            
            try:
                response = client.embeddings.create(
                    input=batch,
                    model="text-embedding-3-small"
                )
                batch_embeddings = [r.embedding for r in response.data]
                embeddings.extend(batch_embeddings)
                
                rate_limiter["last_request"] = time.time()
                
            except openai.RateLimitError as e:
                logger.error(f"Rate limit hit: {e}")
                time.sleep(min(60, 2 ** (i // batch_size)))
                # Retry once
                response = client.embeddings.create(
                    input=batch,
                    model="text-embedding-3-small"
                )
                batch_embeddings = [r.embedding for r in response.data]
                embeddings.extend(batch_embeddings)
                
            except Exception as e:
                logger.error(f"Failed to embed batch: {e}")
                raise
        
        return embeddings
    
    def process_incremental(self, framework_filter: Optional[str] = None, 
                          collection_name: Optional[str] = None,
                          force: bool = False):
        """Process only new or changed documents"""
        
        # Scan for changes
        stats, deleted_files = self.scan_for_changes(framework_filter)
        
        logger.info(f"\nScan complete:")
        logger.info(f"  Total files: {stats['total']}")
        logger.info(f"  Unchanged: {stats['unchanged']} (will skip)")
        logger.info(f"  Changed: {stats['changed']} (will re-embed)")
        logger.info(f"  New: {stats['new']} (will embed)")
        logger.info(f"  Deleted: {stats['deleted']} (will remove from index)")
        
        files_to_process = stats["files_to_process"]
        
        if not files_to_process and not deleted_files:
            logger.info("\n✅ Everything is up to date! No embeddings needed.")
            return
        
        # Estimate cost
        if files_to_process:
            estimated_cost = self.estimate_cost(files_to_process)
            logger.info(f"\nEstimated cost for {len(files_to_process)} files: ${estimated_cost:.4f}")
            
            # Check cost limit
            if estimated_cost > MAX_COST_LIMIT:
                logger.error(f"ABORTED: Cost ${estimated_cost:.2f} exceeds limit ${MAX_COST_LIMIT}")
                return
            
            # Confirm with user
            if not force and estimated_cost > 0.01:
                print(f"\n⚠️  This will cost approximately ${estimated_cost:.4f}")
                print(f"   Files to process: {len(files_to_process)}")
                response = input("\nProceed? (yes/N): ")
                if response.lower() != 'yes':
                    logger.info("Cancelled by user")
                    return
        
        # Configure OpenAI
        client = self.configure_openai()
        
        # Setup ChromaDB with OpenAI embeddings
        if not collection_name:
            collection_name = f"apple_docs_{framework_filter}" if framework_filter else "apple_docs"
        
        collection_name = self.validate_collection_name(collection_name)
        chroma = chromadb.PersistentClient(path=str(self.vectorstore_path))
        
        # Configure OpenAI embedding function
        from chromadb.utils import embedding_functions
        embedding_function = embedding_functions.OpenAIEmbeddingFunction(
            api_key=os.getenv("OPENAI_API_KEY"),
            model_name="text-embedding-3-small",
            dimensions=1536
        )
        
        try:
            collection = chroma.get_collection(
                collection_name,
                embedding_function=embedding_function
            )
            logger.info(f"Using existing collection: {collection_name}")
            
            # Get existing IDs for deletion check
            existing_ids = self.get_existing_ids(collection)
            
        except:
            collection = chroma.create_collection(
                collection_name,
                embedding_function=embedding_function
            )
            logger.info(f"Created new collection: {collection_name}")
            existing_ids = set()
        
        # Process deletions first
        if deleted_files:
            logger.info(f"\nRemoving {len(deleted_files)} deleted files from index...")
            for file_key in deleted_files:
                # Find and delete all IDs for this file
                ids_to_delete = [id for id in existing_ids if file_key.replace("/", "_") in id]
                if ids_to_delete:
                    try:
                        collection.delete(ids=ids_to_delete)
                        logger.debug(f"Deleted {len(ids_to_delete)} embeddings for {file_key}")
                    except Exception as e:
                        logger.warning(f"Failed to delete {file_key}: {e}")
                
                # Remove from hash manager
                if file_key in self.hash_manager.hashes:
                    del self.hash_manager.hashes[file_key]
        
        # Process new/changed files
        if files_to_process:
            logger.info(f"\nProcessing {len(files_to_process)} files...")
            
            # Check for checkpoint
            checkpoint = self.load_checkpoint()
            start_batch = 0
            processed_files_from_checkpoint = []
            
            if checkpoint:
                start_batch = checkpoint.get("batch_index", 0)
                processed_files_from_checkpoint = checkpoint.get("processed_files", [])
                logger.info(f"Resuming from batch {start_batch}")
            
            rate_limiter = {"last_request": 0}
            actual_cost = 0
            verification_stats = {"verified": 0, "failed": 0}
            
            # Process in batches with token awareness
            MAX_TOKENS_PER_REQUEST = 250000  # Conservative limit (OpenAI's is 300k)
            batch_size = min(100, int(os.getenv("EMBEDDING_BATCH_SIZE", "100")))
            
            # Create token-aware batches
            token_aware_batches = []
            current_batch = []
            current_batch_tokens = 0
            
            for idx in range(start_batch * batch_size, len(files_to_process)):
                file_data = files_to_process[idx]
                file_tokens = file_data["tokens"]
                
                # Check if adding this file would exceed token limit
                if current_batch_tokens + file_tokens > MAX_TOKENS_PER_REQUEST and current_batch:
                    token_aware_batches.append(current_batch)
                    current_batch = [file_data]
                    current_batch_tokens = file_tokens
                elif len(current_batch) >= batch_size:
                    # Also respect the file count batch size
                    token_aware_batches.append(current_batch)
                    current_batch = [file_data]
                    current_batch_tokens = file_tokens
                else:
                    current_batch.append(file_data)
                    current_batch_tokens += file_tokens
            
            # Add final batch
            if current_batch:
                token_aware_batches.append(current_batch)
            
            total_batches = len(token_aware_batches)
            
            for batch_idx, batch_files in enumerate(tqdm(token_aware_batches, 
                                                        desc="Creating embeddings", 
                                                        initial=start_batch)):
                
                # Prepare batch data
                batch_texts = []
                batch_metadata = []
                batch_ids = []
                
                # Calculate actual tokens for this batch (accounting for splits)
                batch_total_tokens = 0
                
                for file_data in batch_files:
                    md_file = file_data["path"]
                    content = file_data["content"]
                    file_key = file_data["key"]
                    
                    # Check if document needs splitting based on actual token count
                    token_count = self.count_tokens_safe(content)
                    if token_count > 7000:
                        chunks = self.split_by_headers(content, max_tokens=6000)
                        logger.info(f"Split large file {md_file.name} into {len(chunks)} chunks")
                        
                        for chunk_idx, chunk in enumerate(chunks):
                            # Generate ID with chunk suffix
                            chunk_hash = hashlib.md5(chunk.encode()).hexdigest()[:8]
                            doc_id = self.generate_doc_id(md_file, content) + f"_part{chunk_idx}"
                            
                            # Extract metadata with chunk info
                            metadata = {
                                "framework": md_file.parts[0] if len(md_file.parts) > 0 else "unknown",
                                "api_name": md_file.stem,
                                "file_path": str(md_file),
                                "file_size": md_file.stat().st_size,
                                "chunk_index": chunk_idx,
                                "total_chunks": len(chunks),
                                "chunk_hash": chunk_hash
                            }
                            
                            batch_texts.append(chunk)
                            batch_metadata.append(metadata)
                            batch_ids.append(doc_id)
                            batch_total_tokens += self.count_tokens_safe(chunk)
                    else:
                        # Normal processing for smaller files
                        doc_id = self.generate_doc_id(md_file, content)
                        
                        metadata = {
                            "framework": md_file.parts[0] if len(md_file.parts) > 0 else "unknown",
                            "api_name": md_file.stem,
                            "file_path": str(md_file),
                            "file_size": md_file.stat().st_size
                        }
                        
                        batch_texts.append(content)
                        batch_metadata.append(metadata)
                        batch_ids.append(doc_id)
                        batch_total_tokens += token_count
                
                # Safety check - verify batch won't exceed token limit
                if batch_total_tokens > MAX_TOKENS_PER_REQUEST:
                    logger.error(f"Batch exceeds token limit: {batch_total_tokens} > {MAX_TOKENS_PER_REQUEST}")
                    logger.error(f"Batch had {len(batch_texts)} documents")
                    # Skip this batch to avoid API error
                    continue
                
                # Calculate batch cost
                batch_tokens = sum(self.count_tokens_safe(text) for text in batch_texts)
                batch_cost = (batch_tokens / 1_000_000) * 0.02
                
                # Check if we're about to exceed limit
                if actual_cost + batch_cost > MAX_COST_LIMIT:
                    logger.error(f"Stopping: Next batch would exceed cost limit")
                    break
                
                # Generate embeddings
                embeddings = self.embed_batch_secure(client, batch_texts, 
                                                   batch_size=len(batch_texts), 
                                                   rate_limiter=rate_limiter)
                
                actual_cost += batch_cost
                
                # Delete old versions if they exist
                old_ids_to_delete = []
                for file_data in batch_files:
                    md_file = file_data["path"]
                    # Create base pattern for this file (without content hash)
                    path_hash = hashlib.md5(str(md_file).encode()).hexdigest()[:8]
                    base_pattern = f"{md_file.stem}_{path_hash}_"
                    
                    # Find all IDs that start with this pattern (includes all chunks)
                    # but exclude the ones we're about to add
                    old_ids = [id for id in existing_ids 
                              if id.startswith(base_pattern) and id not in batch_ids]
                    old_ids_to_delete.extend(old_ids)
                
                if old_ids_to_delete:
                    try:
                        collection.delete(ids=old_ids_to_delete)
                        logger.debug(f"Deleted {len(old_ids_to_delete)} old embeddings")
                    except Exception as e:
                        logger.warning(f"Failed to delete old embeddings: {e}")
                
                # Store new embeddings
                try:
                    collection.add(
                        embeddings=embeddings,
                        documents=batch_texts,
                        metadatas=batch_metadata,
                        ids=batch_ids
                    )
                    
                    # Verify embeddings were stored correctly
                    batch_verified, batch_failed = self.verify_embeddings_batch(
                        collection, batch_ids, batch_texts
                    )
                    verification_stats["verified"] += batch_verified
                    verification_stats["failed"] += batch_failed
                    
                    if batch_failed > 0:
                        logger.warning(f"Failed to verify {batch_failed}/{len(batch_ids)} embeddings in batch")
                    
                    # Update hash manager only for successfully verified embeddings
                    for j, file_data in enumerate(batch_files):
                        if j < batch_verified:  # Only update hash for verified embeddings
                            self.hash_manager.update_hash(file_data["key"], file_data["content"])
                    
                    # Save checkpoint
                    processed_files = [fd["key"] for fd in batch_files]
                    self.save_checkpoint(batch_idx + 1, total_batches, 
                                       processed_files_from_checkpoint + processed_files)
                    
                    # Periodically save hash data
                    if batch_idx % 10 == 0:  # Every 10 batches
                        self.hash_manager.save()
                    
                except Exception as e:
                    logger.error(f"Failed to store batch: {e}")
                    # Save checkpoint even on failure to avoid redoing successful work
                    self.save_checkpoint(batch_idx, total_batches, processed_files_from_checkpoint)
                    continue
            
            logger.info(f"\n✅ Incremental update complete!")
            logger.info(f"   Processed: {len(files_to_process)} files")
            logger.info(f"   Actual cost: ${actual_cost:.4f}")
            logger.info(f"   Verified: {verification_stats['verified']} embeddings")
            if verification_stats['failed'] > 0:
                logger.warning(f"   Failed verification: {verification_stats['failed']} embeddings")
            
            # Clear checkpoint on successful completion
            self.clear_checkpoint()
        
        # Save hash data
        self.hash_manager.save()
        logger.info(f"   Hash data saved: {self.hash_file}")
        
        # Final stats
        total_docs = collection.count()
        logger.info(f"   Total documents in collection: {total_docs}")

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Incremental embedding builder with change detection")
    parser.add_argument("--framework", help="Filter to specific framework")
    parser.add_argument("--collection", help="Custom collection name")
    parser.add_argument("--force", action="store_true", help="Skip cost confirmation")
    parser.add_argument("--docs-path", default="documentation", help="Path to documentation")
    parser.add_argument("--vectorstore-path", default="vectorstore", help="Path to vector store")
    
    args = parser.parse_args()
    
    # Convert to Path objects
    docs_path = Path(args.docs_path)
    vectorstore_path = Path(args.vectorstore_path)
    
    # Validation
    if not docs_path.exists():
        print(f"❌ Documentation directory not found: {docs_path}")
        sys.exit(1)
    
    # Ensure vectorstore directory exists
    vectorstore_path.mkdir(exist_ok=True)
    
    print("🚀 Incremental Embedding Builder")
    print(f"📁 Documentation: {docs_path}")
    print(f"💾 Vector store: {vectorstore_path}")
    print(f"🔐 Hash storage: .hashes/embedding_hashes.json")
    print(f"💰 Max cost limit: ${MAX_COST_LIMIT}")
    
    if args.framework:
        print(f"🎯 Framework filter: {args.framework}")
    
    print()
    
    try:
        builder = IncrementalEmbeddingBuilder(docs_path, vectorstore_path)
        builder.process_incremental(args.framework, args.collection, args.force)
    except KeyboardInterrupt:
        print("\n⏹️ Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        logger.exception("Build failed")
        sys.exit(1)

if __name__ == "__main__":
    main()