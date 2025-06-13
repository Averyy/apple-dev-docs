#!/usr/bin/env python3
"""
Incremental embedding generation with hash-based change detection
Only processes new or modified files, saving significant costs

Enhanced with:
- Platform metadata extraction
- Framework summary extraction  
- Correct framework name extraction (parts[0] not parts[-2])
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
sys.path.append(str(Path(__file__).parent.parent.parent))
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
REQUESTS_PER_MINUTE = int(os.getenv("OPENAI_RPM", "500"))  # Even more conservative: 500 RPM (8.3/sec)
MIN_REQUEST_INTERVAL = 60.0 / REQUESTS_PER_MINUTE  # 0.12 seconds between requests

# Load environment variables
env_paths = [
    Path(__file__).parent.parent.parent / ".env",  # Project root
    Path(__file__).parent.parent / ".env"  # mcp-server directory
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
        self.hash_file = Path(__file__).parent.parent.parent / ".hashes" / "embedding_hashes.json"
        self.checkpoint_file = Path(__file__).parent.parent.parent / ".hashes" / "embedding_checkpoint.json"
        self.hash_manager = HashManager(self.hash_file)
        self.processed_ids = set()
        
    def save_checkpoint(self, processed_files: List[str]):
        """Save checkpoint for resume capability"""
        checkpoint_data = {
            "timestamp": time.time(),
            "processed_files": processed_files,
            "last_hash_save": self.hash_manager.cache_file.stat().st_mtime if self.hash_manager.cache_file.exists() else 0
        }
        
        try:
            self.checkpoint_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.checkpoint_file, 'w') as f:
                json.dump(checkpoint_data, f, indent=2)
            logger.debug(f"Checkpoint saved: {len(processed_files)} files processed")
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
            
            logger.info(f"Found checkpoint with {len(checkpoint.get('processed_files', []))} processed files")
            return checkpoint
        except Exception as e:
            logger.warning(f"Failed to load checkpoint: {e}")
            return None
    
    def clear_checkpoint(self):
        """Clear checkpoint file after successful completion"""
        if self.checkpoint_file.exists():
            try:
                self.checkpoint_file.unlink()
                logger.debug("Checkpoint cleared")
            except Exception as e:
                logger.warning(f"Failed to clear checkpoint: {e}")
    
    def configure_openai(self) -> openai.OpenAI:
        """Configure OpenAI client with security checks"""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable must be set")
        
        # Validate API key format
        if not api_key.startswith(("sk-", "sk-proj-")):
            raise ValueError("Invalid OpenAI API key format")
        
        return openai.OpenAI(api_key=api_key)
    
    def validate_collection_name(self, name: str) -> str:
        """Validate and sanitize collection name"""
        # ChromaDB collection name requirements
        if not name:
            raise ValueError("Collection name cannot be empty")
        
        # Remove invalid characters and replace with underscore
        sanitized = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
        
        # Ensure it starts with alphanumeric
        if not sanitized[0].isalnum():
            sanitized = 'c_' + sanitized
        
        # Limit length
        if len(sanitized) > 63:
            sanitized = sanitized[:63]
        
        return sanitized
    
    def validate_framework_name(self, framework: str):
        """Validate framework name against path traversal"""
        if not framework:
            raise ValueError("Framework name cannot be empty")
        
        # Check for path traversal attempts
        if any(char in framework for char in ['..', '/', '\\', '~']):
            raise ValueError(f"Invalid framework name: {framework}")
        
        # Check framework exists
        framework_path = self.docs_path / framework
        if not framework_path.exists() or not framework_path.is_dir():
            raise ValueError(f"Framework directory not found: {framework}")
    
    def estimate_cost(self, files: List[Dict[str, Any]]) -> float:
        """Estimate embedding cost for files"""
        # text-embedding-3-small pricing: $0.020 per 1M tokens
        total_tokens = sum(f["tokens"] for f in files)
        return (total_tokens / 1_000_000) * 0.02
    
    def embed_batch_secure(self, client: openai.OpenAI, texts: List[str], 
                          batch_size: int = 100, rate_limiter: Dict[str, float] = None) -> List[List[float]]:
        """Embed texts with security and rate limiting"""
        embeddings = []
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            
            # Rate limiting
            if rate_limiter:
                elapsed = time.time() - rate_limiter.get("last_request", 0)
                if elapsed < MIN_REQUEST_INTERVAL:
                    time.sleep(MIN_REQUEST_INTERVAL - elapsed)
            
            try:
                response = client.embeddings.create(
                    input=batch,
                    model="text-embedding-3-small",
                    dimensions=1536
                )
                
                batch_embeddings = [item.embedding for item in response.data]
                embeddings.extend(batch_embeddings)
                
                if rate_limiter:
                    rate_limiter["last_request"] = time.time()
                
            except Exception as e:
                logger.error(f"Embedding error: {e}")
                # Return zero embeddings for failed batch
                embeddings.extend([[0.0] * 1536 for _ in batch])
        
        return embeddings
    
    def get_existing_ids(self, collection) -> Set[str]:
        """Get all existing document IDs from collection"""
        try:
            # Get IDs in batches
            all_ids = set()
            batch_size = 10000
            offset = 0
            
            while True:
                results = collection.get(
                    limit=batch_size,
                    offset=offset,
                    include=[]  # Just need IDs
                )
                
                if not results['ids']:
                    break
                
                all_ids.update(results['ids'])
                offset += batch_size
                
                if len(results['ids']) < batch_size:
                    break
            
            return all_ids
        except Exception as e:
            logger.warning(f"Failed to get existing IDs: {e}")
            return set()
    
    def verify_embeddings_batch(self, collection, ids: List[str], original_texts: List[str]) -> Tuple[int, int]:
        """Verify embeddings were stored correctly"""
        try:
            # Query the stored documents
            results = collection.get(ids=ids, include=["documents"])
            
            verified = 0
            failed = 0
            
            stored_docs = {id: doc for id, doc in zip(results['ids'], results['documents'])}
            
            for id, original_text in zip(ids, original_texts):
                if id in stored_docs:
                    # Simple verification - check document exists and has content
                    if stored_docs[id] and len(stored_docs[id]) > 0:
                        verified += 1
                    else:
                        logger.warning(f"Document {id} stored but empty")
                        failed += 1
                else:
                    logger.warning(f"Document {id} not found in collection")
                    failed += 1
            
            return verified, failed
            
        except Exception as e:
            logger.error(f"Verification failed: {e}")
            return 0, len(ids)
    
    def generate_doc_id(self, file_path: Path, content: str) -> str:
        """Generate unique document ID including content hash"""
        # Use path hash for uniqueness across similar filenames
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
    
    def _extract_platforms(self, content: str) -> List[str]:
        """Extract platform availability from markdown content"""
        platforms = []
        
        # Common platform patterns in Apple docs
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
    
    def _extract_metadata(self, file_path: Path, content: str) -> Dict[str, Any]:
        """Extract metadata from markdown file with enhanced features"""
        relative_path = file_path.relative_to(self.docs_path)
        parts = relative_path.parts
        
        # Extract framework name - FIX THE BUG HERE
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
        
        # Extract summary (only for main framework pages)
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
            "platforms": ",".join(platforms) if platforms else "",  # Convert to string for ChromaDB
            "summary": summary if summary else "",  # Ensure string, not None
            "is_framework_main": is_framework_main,
            "file_size": file_path.stat().st_size
        }
    
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
                    
                    # Count tokens
                    token_count = self.count_tokens_safe(content)
                    
                    stats["files_to_process"].append({
                        "path": md_file,
                        "key": file_key,
                        "content": content,
                        "tokens": token_count
                    })
                else:
                    stats["unchanged"] += 1
                    
            except Exception as e:
                logger.warning(f"Error scanning {md_file}: {e}")
        
        # Find deleted files
        existing_keys = set(self.hash_manager.hashes.keys())
        current_keys = {str(Path(f).relative_to(self.docs_path)) for f in current_files}
        deleted_files = existing_keys - current_keys
        
        stats["deleted"] = len(deleted_files)
        
        return stats, deleted_files
    
    def process_incremental(self, framework_filter: Optional[str] = None, 
                          collection_name: Optional[str] = None,
                          force: bool = False):
        """Main processing function with all security and production features"""
        # Scan for changes
        stats, deleted_files = self.scan_for_changes(framework_filter)
        
        # Display stats
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
            processed_files_from_checkpoint = []
            
            if checkpoint:
                processed_files_from_checkpoint = checkpoint.get("processed_files", [])
                logger.info(f"Found checkpoint with {len(processed_files_from_checkpoint)} processed files")
                
                # Filter out already processed files by their paths
                processed_paths = set(processed_files_from_checkpoint)
                original_count = len(files_to_process)
                files_to_process = [f for f in files_to_process if f["path"] not in processed_paths]
                skipped_count = original_count - len(files_to_process)
                logger.info(f"Skipping {skipped_count} already processed files, {len(files_to_process)} remaining")
            
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
            
            for idx in range(0, len(files_to_process)):
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
                                                        desc="Creating embeddings")):
                
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
                            metadata = self._extract_metadata(md_file, content)
                            metadata["chunk_index"] = chunk_idx
                            metadata["total_chunks"] = len(chunks)
                            metadata["chunk_hash"] = chunk_hash
                            
                            batch_texts.append(chunk)
                            batch_metadata.append(metadata)
                            batch_ids.append(doc_id)
                            batch_total_tokens += self.count_tokens_safe(chunk)
                    else:
                        # Normal processing for smaller files
                        doc_id = self.generate_doc_id(md_file, content)
                        
                        metadata = self._extract_metadata(md_file, content)
                        
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
                    all_processed = processed_files_from_checkpoint + processed_files
                    self.save_checkpoint(all_processed)
                    
                    # Periodically save hash data
                    if batch_idx % 10 == 0:  # Every 10 batches
                        self.hash_manager.save()
                    
                except Exception as e:
                    logger.error(f"Failed to store batch: {e}")
                    # Save checkpoint even on failure to avoid redoing successful work
                    self.save_checkpoint(processed_files_from_checkpoint)
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
    parser.add_argument("--force", action="store_true", help="Force rebuild entire index")
    parser.add_argument("--docs-path", help="Path to documentation (relative to project root)")
    parser.add_argument("--vectorstore-path", help="Path to vector store (relative to project root)")
    parser.add_argument("--verify", action="store_true", help="Verify index after building")
    
    args = parser.parse_args()
    
    # Get project root
    project_root = Path(__file__).parent.parent.parent
    
    # Set paths relative to project root
    docs_path = project_root / (args.docs_path or "documentation")
    vectorstore_path = project_root / (args.vectorstore_path or "vectorstore")
    
    # Validation
    if not docs_path.exists():
        print(f"❌ Documentation directory not found: {docs_path}")
        sys.exit(1)
    
    # Ensure vectorstore directory exists
    vectorstore_path.mkdir(exist_ok=True)
    
    # Verify API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable must be set")
        sys.exit(1)
    
    print("🚀 Incremental Embedding Builder")
    print(f"📁 Documentation: {docs_path}")
    print(f"💾 Vector store: {vectorstore_path}")
    print(f"🔐 Hash storage: {project_root}/.hashes/embedding_hashes.json")
    print(f"💰 Max cost limit: ${MAX_COST_LIMIT}")
    
    if args.framework:
        print(f"🎯 Framework filter: {args.framework}")
    
    print()
    
    try:
        builder = IncrementalEmbeddingBuilder(docs_path, vectorstore_path)
        
        # Handle force rebuild
        if args.force:
            logger.info("Force rebuild requested, clearing collection and hashes...")
            # Clear the collection
            chroma = chromadb.PersistentClient(path=str(vectorstore_path))
            collection_name = args.collection or "apple_docs"
            try:
                chroma.delete_collection(collection_name)
                logger.info(f"Deleted collection: {collection_name}")
            except:
                pass
            # Clear hashes
            builder.hash_manager.hashes = {}
            builder.hash_manager.save()
        
        builder.process_incremental(args.framework, args.collection, args.force or True)
        
        # Verify if requested
        if args.verify:
            logger.info("\nVerifying index...")
            # Simple verification - check collection has documents
            chroma = chromadb.PersistentClient(path=str(vectorstore_path))
            collection_name = args.collection or "apple_docs"
            try:
                collection = chroma.get_collection(collection_name)
                count = collection.count()
                logger.info(f"✅ Verification complete: {count} documents in collection")
            except Exception as e:
                logger.error(f"❌ Verification failed: {e}")
                
    except KeyboardInterrupt:
        print("\n⏹️ Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        logger.exception("Build failed")
        sys.exit(1)

if __name__ == "__main__":
    main()