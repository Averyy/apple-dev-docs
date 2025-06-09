#!/usr/bin/env python3
"""
Security-hardened version of build_index_openai.py
Includes cost caps, input validation, and rate limiting
"""

import os
import sys
import re
import time
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional
import chromadb
import openai
from tqdm import tqdm
import logging
from dotenv import load_dotenv
import tiktoken

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Security Configuration
MAX_COST_LIMIT = float(os.getenv("MAX_EMBEDDING_COST", "10.00"))
MAX_FILES_TO_PROCESS = int(os.getenv("MAX_FILES_TO_EMBED", "300000"))
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE_MB", "10")) * 1024 * 1024
MAX_TOKENS_PER_DOC = int(os.getenv("MAX_TOKENS_PER_DOC", "8000"))
REQUESTS_PER_MINUTE = int(os.getenv("OPENAI_RPM", "3000"))
MIN_REQUEST_INTERVAL = 60.0 / REQUESTS_PER_MINUTE

# Load environment variables
env_paths = [
    Path(__file__).parent.parent / "mcp-server" / ".env",
    Path(__file__).parent.parent / ".env"
]

for env_path in env_paths:
    if env_path.exists():
        load_dotenv(env_path)
        logger.info(f"Loaded environment from {env_path}")
        break

def validate_framework_name(name: str) -> bool:
    """Validate framework name to prevent path traversal"""
    if not name:
        return True  # Empty is ok (means all frameworks)
    
    # Only allow alphanumeric, dash, underscore
    if not re.match(r'^[a-zA-Z0-9_-]+$', name):
        raise ValueError(f"Invalid framework name: {name}. Only alphanumeric, dash, and underscore allowed.")
    
    # Prevent path traversal
    if ".." in name or "/" in name or "\\" in name:
        raise ValueError(f"Invalid framework name: {name}. Path traversal not allowed.")
    
    return True

def validate_collection_name(name: str) -> str:
    """Validate and sanitize ChromaDB collection name"""
    # ChromaDB requirements: 3-63 chars, start/end with alphanumeric
    sanitized = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    sanitized = sanitized[:63]  # Max length
    
    # Ensure starts/ends with alphanumeric
    sanitized = re.sub(r'^[^a-zA-Z0-9]+', '', sanitized)
    sanitized = re.sub(r'[^a-zA-Z0-9]+$', '', sanitized)
    
    if len(sanitized) < 3:
        sanitized = f"col_{sanitized}"
    
    return sanitized

def configure_openai():
    """Configure OpenAI API with security checks"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable must be set")
    
    # Validate API key format (basic check)
    if not api_key.startswith("sk-") or len(api_key) < 20:
        raise ValueError("Invalid OpenAI API key format")
    
    client = openai.OpenAI(api_key=api_key)
    logger.info("OpenAI API configured securely")
    return client

def count_tokens_safe(text: str) -> int:
    """Count tokens with error handling"""
    try:
        encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(text[:MAX_TOKENS_PER_DOC]))  # Limit input size
    except Exception as e:
        logger.warning(f"Token counting failed: {e}, estimating")
        return len(text) // 4  # Rough estimate

def load_documents_secure(docs_path: Path, framework_filter: Optional[str] = None, 
                         max_files: int = MAX_FILES_TO_PROCESS) -> List[Dict[str, Any]]:
    """Load documents with security limits"""
    documents = []
    file_count = 0
    total_size = 0
    skipped_files = {"too_large": 0, "errors": 0}
    
    # Validate framework filter
    if framework_filter:
        validate_framework_name(framework_filter)
    
    pattern = f"{framework_filter}/**/*.md" if framework_filter else "**/*.md"
    
    logger.info(f"Scanning for documents (max: {max_files}, max size: {MAX_FILE_SIZE/1024/1024}MB each)")
    
    for md_file in docs_path.glob(pattern):
        # Security check: max files
        if file_count >= max_files:
            logger.warning(f"Reached maximum file limit: {max_files}")
            break
        
        try:
            # Security check: file size
            file_size = md_file.stat().st_size
            if file_size > MAX_FILE_SIZE:
                logger.warning(f"Skipping large file: {md_file} ({file_size/1024/1024:.1f}MB)")
                skipped_files["too_large"] += 1
                continue
            
            # Security check: total size
            total_size += file_size
            if total_size > MAX_FILE_SIZE * 100:  # 1GB total max
                logger.warning("Reached total size limit (1GB)")
                break
            
            content = md_file.read_text(encoding='utf-8')
            
            # Security check: token limit
            tokens = count_tokens_safe(content)
            if tokens > MAX_TOKENS_PER_DOC:
                logger.warning(f"Truncating document {md_file}: {tokens} tokens > {MAX_TOKENS_PER_DOC}")
                # Truncate to max tokens (rough)
                content = content[:MAX_TOKENS_PER_DOC * 4]
                tokens = MAX_TOKENS_PER_DOC
            
            documents.append({
                "content": content,
                "path": str(md_file),
                "metadata": extract_metadata_safe(md_file, docs_path),
                "tokens": tokens,
                "file_size": file_size
            })
            file_count += 1
            
        except Exception as e:
            logger.warning(f"Failed to read {md_file}: {e}")
            skipped_files["errors"] += 1
            continue
    
    logger.info(f"Loaded {len(documents)} documents, skipped {sum(skipped_files.values())} files")
    logger.info(f"Skipped details: {skipped_files}")
    
    return documents

def extract_metadata_safe(file_path: Path, docs_path: Path) -> Dict[str, Any]:
    """Extract metadata with sanitization"""
    try:
        parts = file_path.relative_to(docs_path).parts
        framework = parts[0] if parts else "unknown"
        api_name = file_path.stem
        
        # Sanitize metadata values
        framework = re.sub(r'[^\w\s-]', '', framework)[:50]
        api_name = re.sub(r'[^\w\s-]', '', api_name)[:50]
        
        return {
            "framework": framework,
            "api_name": api_name,
            "file_path": str(file_path)[:200],  # Limit path length
            "file_size": min(file_path.stat().st_size, 2**31-1)  # Prevent integer overflow
        }
    except Exception as e:
        logger.warning(f"Metadata extraction failed for {file_path}: {e}")
        return {
            "framework": "unknown",
            "api_name": "unknown",
            "file_path": "unknown",
            "file_size": 0
        }

def embed_batch_secure(client: openai.OpenAI, texts: List[str], 
                      batch_size: int = 100, rate_limiter: Dict[str, float] = None) -> List[List[float]]:
    """Generate embeddings with rate limiting and error handling"""
    embeddings = []
    
    # Rate limiting state
    if rate_limiter is None:
        rate_limiter = {"last_request": 0}
    
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        
        # Rate limiting
        elapsed = time.time() - rate_limiter["last_request"]
        if elapsed < MIN_REQUEST_INTERVAL:
            sleep_time = MIN_REQUEST_INTERVAL - elapsed
            logger.debug(f"Rate limiting: sleeping {sleep_time:.2f}s")
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
            # Exponential backoff
            sleep_time = min(60, 2 ** (i // batch_size))
            logger.info(f"Sleeping {sleep_time}s before retry")
            time.sleep(sleep_time)
            # Retry once
            try:
                response = client.embeddings.create(
                    input=batch,
                    model="text-embedding-3-small"
                )
                batch_embeddings = [r.embedding for r in response.data]
                embeddings.extend(batch_embeddings)
            except Exception as e2:
                logger.error(f"Retry failed: {e2}")
                raise
                
        except Exception as e:
            logger.error(f"Failed to embed batch {i//batch_size}: {e}")
            raise
    
    return embeddings

def estimate_and_confirm_cost(documents: List[Dict[str, Any]], force: bool = False) -> bool:
    """Estimate cost and get confirmation with strict limits"""
    total_tokens = sum(doc["tokens"] for doc in documents)
    estimated_cost = (total_tokens / 1_000_000) * 0.02
    
    logger.info(f"Total tokens: {total_tokens:,}")
    logger.info(f"Estimated cost: ${estimated_cost:.4f}")
    
    # Hard cost limit
    if estimated_cost > MAX_COST_LIMIT:
        logger.error(f"ABORTED: Cost ${estimated_cost:.2f} exceeds hard limit ${MAX_COST_LIMIT}")
        logger.error(f"Set MAX_EMBEDDING_COST environment variable to increase limit")
        return False
    
    # Require confirmation for any cost
    if not force and estimated_cost > 0.01:
        print(f"\n⚠️  This will cost approximately ${estimated_cost:.4f}")
        print(f"   Maximum allowed: ${MAX_COST_LIMIT}")
        print(f"   Documents: {len(documents)}")
        print(f"   Total tokens: {total_tokens:,}")
        
        response = input("\nProceed? (yes/N): ")
        if response.lower() != 'yes':  # Require full "yes"
            logger.info("Cancelled by user")
            return False
    
    return True

def build_index_secure(docs_path: Path, vectorstore_path: Path, 
                      framework_filter: Optional[str] = None,
                      collection_name: Optional[str] = None,
                      force: bool = False):
    """Build vector index with security measures"""
    
    # Configure OpenAI
    client = configure_openai()
    
    # Load documents with limits
    logger.info("Loading documents with security limits...")
    documents = load_documents_secure(docs_path, framework_filter)
    
    if not documents:
        raise ValueError(f"No documents found in {docs_path}")
    
    # Cost check
    if not estimate_and_confirm_cost(documents, force):
        return
    
    # Setup ChromaDB with validated collection name
    if not collection_name:
        collection_name = f"apple_docs_{framework_filter}" if framework_filter else "apple_docs"
    
    collection_name = validate_collection_name(collection_name)
    logger.info(f"Using collection name: {collection_name}")
    
    chroma = chromadb.PersistentClient(path=str(vectorstore_path))
    
    # Create or get collection
    try:
        collection = chroma.get_collection(collection_name)
        logger.info(f"Using existing collection: {collection_name}")
    except:
        collection = chroma.create_collection(collection_name)
        logger.info(f"Created new collection: {collection_name}")
    
    # Process documents
    all_texts = [doc["content"] for doc in documents]
    all_metadata = [doc["metadata"] for doc in documents]
    
    # Generate unique IDs based on content
    all_ids = []
    for i, (text, metadata) in enumerate(zip(all_texts, all_metadata)):
        # Content-based ID to prevent duplicates
        content_hash = hashlib.md5(text.encode()).hexdigest()[:8]
        doc_id = f"{metadata['framework']}_{metadata['api_name']}_{content_hash}"
        all_ids.append(doc_id)
    
    # Batch embed and store with rate limiting
    batch_size = min(100, int(os.getenv("EMBEDDING_BATCH_SIZE", "100")))
    rate_limiter = {"last_request": 0}
    
    # Track progress and cost
    total_batches = (len(all_texts) + batch_size - 1) // batch_size
    actual_cost = 0
    
    for i in tqdm(range(0, len(all_texts), batch_size), desc="Creating embeddings", total=total_batches):
        batch_texts = all_texts[i:i+batch_size]
        batch_metadata = all_metadata[i:i+batch_size]
        batch_ids = all_ids[i:i+batch_size]
        
        # Calculate batch cost
        batch_tokens = sum(count_tokens_safe(text) for text in batch_texts)
        batch_cost = (batch_tokens / 1_000_000) * 0.02
        
        # Check if we're about to exceed limit
        if actual_cost + batch_cost > MAX_COST_LIMIT:
            logger.error(f"Stopping: Next batch would exceed cost limit (${actual_cost:.4f} + ${batch_cost:.4f} > ${MAX_COST_LIMIT})")
            break
        
        # Generate embeddings with rate limiting
        embeddings = embed_batch_secure(client, batch_texts, batch_size=len(batch_texts), rate_limiter=rate_limiter)
        
        actual_cost += batch_cost
        
        # Store in ChromaDB
        try:
            collection.add(
                embeddings=embeddings,
                documents=batch_texts,
                metadatas=batch_metadata,
                ids=batch_ids
            )
        except Exception as e:
            logger.error(f"Failed to store batch {i//batch_size}: {e}")
            # Don't raise - continue with other batches
            continue
        
        # Progress checkpoint
        if (i + batch_size) % 1000 == 0:
            logger.info(f"Checkpoint: {i + batch_size} embeddings, cost so far: ${actual_cost:.4f}")
    
    logger.info(f"✅ Indexing complete!")
    logger.info(f"   Collection: {collection_name}")
    logger.info(f"   Documents: {collection.count()}")
    logger.info(f"   Actual cost: ${actual_cost:.4f}")

def main():
    """Main entry point with argument parsing"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Build vector index with security measures")
    parser.add_argument("--framework", help="Filter to specific framework")
    parser.add_argument("--collection", help="Custom collection name")
    parser.add_argument("--force", action="store_true", help="Skip cost confirmation")
    parser.add_argument("--max-files", type=int, help="Override max files limit")
    parser.add_argument("--max-cost", type=float, help="Override max cost limit")
    parser.add_argument("--docs-path", default="documentation", help="Path to documentation")
    parser.add_argument("--vectorstore-path", default="vectorstore", help="Path to vector store")
    
    args = parser.parse_args()
    
    # Override limits if specified
    if args.max_files:
        global MAX_FILES_TO_PROCESS
        MAX_FILES_TO_PROCESS = args.max_files
    
    if args.max_cost:
        global MAX_COST_LIMIT
        MAX_COST_LIMIT = args.max_cost
    
    # Convert to Path objects
    docs_path = Path(args.docs_path)
    vectorstore_path = Path(args.vectorstore_path)
    
    # Validation
    if not docs_path.exists():
        print(f"❌ Documentation directory not found: {docs_path}")
        sys.exit(1)
    
    # Ensure vectorstore directory exists
    vectorstore_path.mkdir(exist_ok=True)
    
    print("🔒 Secure Vector Index Builder")
    print(f"📁 Documentation: {docs_path}")
    print(f"💾 Vector store: {vectorstore_path}")
    print(f"💰 Max cost limit: ${MAX_COST_LIMIT}")
    print(f"📄 Max files: {MAX_FILES_TO_PROCESS:,}")
    print(f"📏 Max file size: {MAX_FILE_SIZE/1024/1024}MB")
    
    if args.framework:
        print(f"🎯 Framework filter: {args.framework}")
    
    print()
    
    try:
        build_index_secure(docs_path, vectorstore_path, args.framework, args.collection, args.force)
    except KeyboardInterrupt:
        print("\n⏹️ Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        logger.exception("Build failed")
        sys.exit(1)

if __name__ == "__main__":
    main()