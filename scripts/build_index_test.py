#!/usr/bin/env python3
"""
Test version of build_index_openai.py that allows filtering by framework
"""

import os
import sys
import chromadb
import openai
from pathlib import Path
from typing import List, Dict, Any, Optional
from tqdm import tqdm
import logging
from dotenv import load_dotenv
import tiktoken

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

def configure_openai():
    """Configure OpenAI API using environment variable"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable must be set")
    
    # Return configured client (v1.0+ API)
    client = openai.OpenAI(api_key=api_key)
    logger.info("OpenAI API configured")
    return client

def count_tokens(text: str) -> int:
    """Count tokens using tiktoken"""
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def load_documents(docs_path: Path, framework_filter: Optional[str] = None) -> List[Dict[str, Any]]:
    """Load documents, optionally filtering by framework"""
    documents = []
    
    pattern = f"{framework_filter}/**/*.md" if framework_filter else "**/*.md"
    
    for md_file in docs_path.glob(pattern):
        try:
            content = md_file.read_text(encoding='utf-8')
            documents.append({
                "content": content,
                "path": str(md_file),
                "metadata": extract_metadata(md_file, docs_path),
                "tokens": count_tokens(content)
            })
        except Exception as e:
            logger.warning(f"Failed to read {md_file}: {e}")
            continue
    
    return documents

def extract_metadata(file_path: Path, docs_path: Path) -> Dict[str, Any]:
    """Extract metadata from file path"""
    try:
        parts = file_path.relative_to(docs_path).parts
        framework = parts[0] if parts else "unknown"
        api_name = file_path.stem
        
        return {
            "framework": framework,
            "api_name": api_name,
            "file_path": str(file_path),
            "file_size": file_path.stat().st_size
        }
    except Exception as e:
        return {
            "framework": "unknown",
            "api_name": file_path.stem,
            "file_path": str(file_path),
            "file_size": 0
        }

def embed_batch(client: openai.OpenAI, texts: List[str], batch_size: int = 100) -> List[List[float]]:
    """Generate embeddings using OpenAI text-embedding-3-small"""
    embeddings = []
    
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        
        try:
            response = client.embeddings.create(
                input=batch,
                model="text-embedding-3-small"
            )
            batch_embeddings = [r.embedding for r in response.data]
            embeddings.extend(batch_embeddings)
            
        except openai.RateLimitError as e:
            logger.error(f"Rate limit/quota exceeded: {e}")
            logger.error("Please check your OpenAI billing at: https://platform.openai.com/usage")
            raise  # Stop processing on quota errors
        except Exception as e:
            logger.error(f"Failed to embed batch {i//batch_size}: {e}")
            # Add empty embeddings for failed batch
            embeddings.extend([[0.0] * 1536 for _ in batch])
    
    return embeddings

def build_index(docs_path: Path, 
                vectorstore_path: Path,
                framework_filter: Optional[str] = None,
                dry_run: bool = False):
    """Build vector index with optional framework filter and dry run"""
    
    # Configure OpenAI
    client = configure_openai()
    
    # Load documents
    logger.info(f"Loading documents{f' from {framework_filter}' if framework_filter else ''}...")
    documents = load_documents(docs_path, framework_filter)
    
    if not documents:
        logger.error("No documents found")
        return
    
    # Calculate costs
    total_tokens = sum(doc["tokens"] for doc in documents)
    estimated_cost = (total_tokens / 1_000_000) * 0.02
    
    logger.info(f"Found {len(documents)} documents")
    logger.info(f"Total tokens: {total_tokens:,}")
    logger.info(f"Estimated cost: ${estimated_cost:.4f}")
    
    if dry_run:
        logger.info("DRY RUN - Not creating embeddings")
        print("\nSample documents:")
        for doc in documents[:5]:
            print(f"  - {doc['metadata']['framework']}/{doc['metadata']['api_name']}: {doc['tokens']} tokens")
        return
    
    # Confirm with user for costs over $0.10
    if estimated_cost > 0.10:
        response = input(f"\n⚠️  This will cost ${estimated_cost:.4f}. Continue? (y/N): ")
        if response.lower() != 'y':
            logger.info("Cancelled by user")
            return
    
    # Setup ChromaDB
    collection_name = f"apple_docs_{framework_filter}" if framework_filter else "apple_docs"
    chroma = chromadb.PersistentClient(path=str(vectorstore_path))
    
    try:
        collection = chroma.get_collection(collection_name)
        logger.info(f"Using existing collection: {collection_name}")
    except:
        collection = chroma.create_collection(collection_name)
        logger.info(f"Created new collection: {collection_name}")
    
    # Process documents
    all_texts = [doc["content"] for doc in documents]
    all_metadata = [doc["metadata"] for doc in documents]
    
    # Batch embed and store
    batch_size = 100
    for i in tqdm(range(0, len(all_texts), batch_size), desc="Creating embeddings"):
        batch_texts = all_texts[i:i+batch_size]
        batch_metadata = all_metadata[i:i+batch_size]
        
        # Generate embeddings
        embeddings = embed_batch(client, batch_texts, batch_size=batch_size)
        
        # Store in ChromaDB
        try:
            collection.add(
                embeddings=embeddings,
                documents=batch_texts,
                metadatas=batch_metadata,
                ids=[f"{framework_filter or 'doc'}_{j}" for j in range(i, i+len(batch_texts))]
            )
        except Exception as e:
            logger.error(f"Failed to store batch {i//batch_size}: {e}")
            continue
    
    logger.info(f"✅ Indexing complete! Collection '{collection_name}' has {collection.count()} documents")

def main():
    """Main entry point with CLI arguments"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Build vector index for Apple documentation")
    parser.add_argument("--framework", help="Filter to specific framework (e.g., AdSupport, SwiftUI)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be indexed without doing it")
    parser.add_argument("--docs-path", default="documentation", help="Path to documentation directory")
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
    
    print("🚀 Apple Documentation Vector Indexer")
    print(f"📁 Documentation: {docs_path}")
    print(f"💾 Vector store: {vectorstore_path}")
    
    if args.framework:
        print(f"🎯 Framework filter: {args.framework}")
    
    if args.dry_run:
        print("🔍 DRY RUN MODE - No embeddings will be created")
    
    print()
    
    try:
        build_index(docs_path, vectorstore_path, args.framework, args.dry_run)
    except KeyboardInterrupt:
        print("\n⏹️ Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()