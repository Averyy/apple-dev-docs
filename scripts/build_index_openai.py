#!/usr/bin/env python3
"""
Build vector index using OpenAI text-embedding-3-small
Uses environment variable OPENAI_API_KEY for secure authentication
"""

import os
import sys
import asyncio
import chromadb
import openai
from pathlib import Path
from typing import List, Dict, Any
from tqdm import tqdm
import json
import logging
import hashlib
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
# First try mcp-server/.env, then root .env
env_paths = [
    Path(__file__).parent.parent / "mcp-server" / ".env",
    Path(__file__).parent.parent / ".env"
]

for env_path in env_paths:
    if env_path.exists():
        load_dotenv(env_path)
        logger.info(f"Loaded environment from {env_path}")
        break

# Security: Only use environment variable for API key
def configure_openai():
    """Configure OpenAI API using environment variable"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable must be set. "
            "Add it to your .env file (which is not checked into git)."
        )
    
    # Return configured client
    client = openai.OpenAI(api_key=api_key)
    logger.info("OpenAI API configured from environment variable")
    return client

def load_documents(docs_path: Path) -> List[Dict[str, Any]]:
    """Load all markdown documents from documentation directory"""
    documents = []
    
    for md_file in docs_path.rglob("*.md"):
        try:
            content = md_file.read_text(encoding='utf-8')
            documents.append({
                "content": content,
                "path": str(md_file),
                "metadata": extract_metadata(md_file, docs_path)
            })
        except Exception as e:
            logger.warning(f"Failed to read {md_file}: {e}")
            continue
    
    logger.info(f"Loaded {len(documents)} documents")
    return documents

def extract_metadata(file_path: Path, docs_path: Path) -> Dict[str, Any]:
    """Extract metadata from file path"""
    try:
        parts = file_path.relative_to(docs_path).parts
        framework = parts[0] if parts else "unknown"
        api_name = file_path.stem
        
        # Construct Apple developer URL
        url_parts = "/".join(parts[:-1]) if len(parts) > 1 else framework
        url = f"https://developer.apple.com/documentation/{url_parts}/{api_name}"
        
        # Keep metadata concise - ChromaDB has limits
        # Avoid very long strings that could exceed limits
        metadata = {
            "framework": framework[:100],  # Limit length
            "api_name": api_name[:200],    # Limit length
            "url": url[:500],              # URLs can be long
            "file_path": str(file_path)[-500:],  # Keep last 500 chars if too long
            "file_size": min(file_path.stat().st_size, 2147483647)  # Ensure within int32 range
        }
        
        # Validate total metadata size (ChromaDB has limits)
        metadata_str = json.dumps(metadata)
        if len(metadata_str) > 40000:  # Conservative limit
            logger.warning(f"Metadata too large for {file_path}, truncating")
            # Remove file_path if metadata is too large
            del metadata["file_path"]
        
        return metadata
    except Exception as e:
        logger.warning(f"Failed to extract metadata from {file_path}: {e}")
        return {
            "framework": "unknown",
            "api_name": file_path.stem[:200],
            "url": "",
            "file_path": "",
            "file_size": 0
        }

def process_document(content: str, max_length: int = 5000) -> List[Dict[str, Any]]:
    """
    Process document content into chunks if needed
    Most Apple docs are single-API focused, so minimal chunking
    
    Note: ChromaDB performs better with smaller chunks (5000 chars)
    and this aligns with best practices from Context7 documentation
    """
    # Calculate size in bytes for more accurate chunking
    content_bytes = content.encode('utf-8')
    
    # Most files: one embedding per file
    if len(content_bytes) <= max_length:
        return [{
            "content": content,
            "chunk_index": 0,
            "total_chunks": 1
        }]
    
    # Only for very large files: split by headers
    sections = content.split('\n## ')
    chunks = []
    
    for i, section in enumerate(sections):
        if i > 0:
            section = "## " + section  # Re-add header marker
        
        # Ensure chunk doesn't exceed byte limit
        section_bytes = section.encode('utf-8')
        if len(section_bytes) > max_length:
            # Truncate at character boundary
            truncated = section_bytes[:max_length].decode('utf-8', errors='ignore')
            section = truncated
        
        chunks.append({
            "content": section,
            "chunk_index": i,
            "total_chunks": len(sections)
        })
    
    return chunks

def embed_batch(client: openai.OpenAI, texts: List[str], batch_size: int = 100) -> List[List[float]]:
    """
    Generate embeddings using OpenAI text-embedding-3-small
    SECURITY: Only this model is allowed for the provided API key
    """
    embeddings = []
    
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        
        try:
            response = client.embeddings.create(
                input=batch,
                model="text-embedding-3-small"  # ONLY allowed model
            )
            batch_embeddings = [r.embedding for r in response.data]
            embeddings.extend(batch_embeddings)
            
        except openai.RateLimitError as e:
            logger.error(f"Rate limit/quota exceeded: {e}")
            logger.error("Please check your OpenAI billing at: https://platform.openai.com/usage")
            raise  # Stop processing on quota errors
        except Exception as e:
            logger.error(f"Failed to embed batch {i//batch_size}: {e}")
            # Add empty embeddings for failed batch to maintain alignment
            embeddings.extend([[0.0] * 1536 for _ in batch])
    
    return embeddings

def build_index(docs_path: Path, vectorstore_path: Path, collection_name: str = "apple_docs"):
    """Build the complete vector index"""
    
    # Validate collection name
    import re
    if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9_-]{1,61}[a-zA-Z0-9]$', collection_name):
        raise ValueError(
            f"Invalid collection name: {collection_name}. "
            "Must be 3-63 characters, start/end with alphanumeric, "
            "and contain only alphanumeric, underscore, or hyphen."
        )
    
    # Configure OpenAI API
    client = configure_openai()
    
    # Load documents
    documents = load_documents(docs_path)
    if not documents:
        raise ValueError(f"No documents found in {docs_path}")
    
    # Setup ChromaDB
    chroma = chromadb.PersistentClient(path=str(vectorstore_path))
    
    # Create or get collection
    try:
        collection = chroma.get_collection(collection_name)
        logger.info(f"Using existing collection: {collection_name}")
    except:
        collection = chroma.create_collection(collection_name)
        logger.info(f"Created new collection: {collection_name}")
    
    # Process documents into chunks
    all_chunks = []
    all_metadata = []
    all_ids = []
    
    logger.info("Processing documents into chunks...")
    for doc in tqdm(documents, desc="Processing documents"):
        chunks = process_document(doc["content"])
        
        for chunk_data in chunks:
            all_chunks.append(chunk_data["content"])
            
            # Add chunk info to metadata
            metadata = doc["metadata"].copy()
            metadata["chunk_index"] = chunk_data["chunk_index"]
            metadata["total_chunks"] = chunk_data["total_chunks"]
            all_metadata.append(metadata)
            
            # Generate unique ID based on file path and chunk index
            # This ensures consistent IDs across runs
            id_source = f"{metadata['file_path']}:chunk_{chunk_data['chunk_index']}"
            doc_id = hashlib.sha256(id_source.encode()).hexdigest()[:16]
            all_ids.append(doc_id)
    
    logger.info(f"Total embeddings to create: {len(all_chunks)}")
    logger.info(f"Estimated cost: ${len(all_chunks) * 1000 * 0.02 / 1_000_000:.2f}")
    
    # Batch embed and store
    # ChromaDB has internal batch limits, typically around 5000 documents
    # But we'll use smaller batches for stability and OpenAI rate limits
    batch_size = 100
    max_chromadb_batch = 1000  # Conservative limit for ChromaDB
    
    for i in tqdm(range(0, len(all_chunks), batch_size), desc="Creating embeddings"):
        batch_chunks = all_chunks[i:i+batch_size]
        batch_metadata = all_metadata[i:i+batch_size]
        batch_ids = all_ids[i:i+batch_size]
        
        # Generate embeddings
        embeddings = embed_batch(client, batch_chunks, batch_size=batch_size)
        
        # Store in ChromaDB with additional batch size check
        try:
            # If batch is still too large, split it further
            if len(batch_chunks) > max_chromadb_batch:
                for sub_i in range(0, len(batch_chunks), max_chromadb_batch):
                    sub_end = min(sub_i + max_chromadb_batch, len(batch_chunks))
                    collection.add(
                        embeddings=embeddings[sub_i:sub_end],
                        documents=batch_chunks[sub_i:sub_end],
                        metadatas=batch_metadata[sub_i:sub_end],
                        ids=batch_ids[sub_i:sub_end]
                    )
            else:
                collection.add(
                    embeddings=embeddings,
                    documents=batch_chunks,
                    metadatas=batch_metadata,
                    ids=batch_ids
                )
        except Exception as e:
            logger.error(f"Failed to store batch {i//batch_size}: {e}")
            # Log more details for debugging
            logger.error(f"Batch size: {len(batch_chunks)}, Error type: {type(e).__name__}")
            
            # Retry logic for database locked errors
            if "database is locked" in str(e).lower():
                logger.info("Database locked, retrying after delay...")
                import time
                time.sleep(2)  # Wait 2 seconds
                try:
                    collection.add(
                        embeddings=embeddings,
                        documents=batch_chunks,
                        metadatas=batch_metadata,
                        ids=batch_ids
                    )
                    logger.info("Retry successful")
                except Exception as retry_e:
                    logger.error(f"Retry failed: {retry_e}")
                    continue
            else:
                continue
        
        # Progress checkpoint every 1000 embeddings
        if (i + batch_size) % 1000 == 0:
            logger.info(f"Checkpoint: {i + batch_size} embeddings processed")
    
    logger.info("✅ Vector index build complete!")
    
    # Verify persistence
    final_count = collection.count()
    logger.info(f"Collection stats: {final_count} documents indexed")
    
    # Validate the count matches expectations
    expected_count = len(all_chunks)
    if final_count != expected_count:
        logger.warning(
            f"⚠️  Count mismatch! Expected {expected_count}, but got {final_count}. "
            f"Missing: {expected_count - final_count} documents"
        )
    
    # Force persistence by recreating client
    del chroma
    
    # Verify data persists after client recreation
    verify_client = chromadb.PersistentClient(path=str(vectorstore_path))
    verify_collection = verify_client.get_collection(collection_name)
    verify_count = verify_collection.count()
    
    if verify_count == final_count:
        logger.info(f"✅ Persistence verified: {verify_count} documents")
    else:
        logger.error(f"❌ Persistence issue: Expected {final_count}, got {verify_count}")

def main():
    """Main entry point"""
    
    # Configuration
    project_root = Path(__file__).parent.parent
    docs_path = project_root / "documentation"
    vectorstore_path = project_root / "vectorstore"
    
    # Validation
    if not docs_path.exists():
        print(f"❌ Documentation directory not found: {docs_path}")
        print("Run the scraper first to generate documentation")
        sys.exit(1)
    
    # Ensure vectorstore directory exists
    vectorstore_path.mkdir(exist_ok=True)
    
    print("🚀 Building vector index with OpenAI text-embedding-3-small")
    print(f"📁 Documentation: {docs_path}")
    print(f"💾 Vector store: {vectorstore_path}")
    print(f"🔑 API key: Using OPENAI_API_KEY environment variable")
    print()
    
    try:
        build_index(docs_path, vectorstore_path)
    except KeyboardInterrupt:
        print("\n⏹️ Build interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Build failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()