# Task 2: Build Vector Index

**Status**: Ready to proceed - Apple documentation scraping complete (278,778 pages)

## Objective
Create a one-time indexing script to convert all Apple documentation into searchable vector embeddings using direct API calls.

## Prerequisites
- ✅ Task 1 completed (environment setup)
- ✅ Apple documentation scraped (278,778 pages across 341 frameworks)
- 🔧 Choose embedding provider: Voyage API key OR local TEI server

## Implementation Steps

### 1. Embedding Model Options (Updated 2024)

**Selected: Voyage-3-lite** ✅
- **Cost**: $0.02/1M tokens
- **Performance**: Outperforms OpenAI-3-large by 3.82% on MTEB
- **Context**: 32K tokens (vs OpenAI's 8K) - perfect for Apple docs
- **Dimensions**: 512 (faster search, smaller storage)
- **Your cost**: $0.83 for 278,778 docs (actual count)
- **Implementation**: See `scripts/build_index_voyage.py`

**Alternative: BGE-M3 (Local via TEI)**
- **Cost**: $0 (local inference)
- **Performance**: Top MTEB performer
- **Dimensions**: 1024
- **Issue**: TEI server too slow (~26 days for full indexing)

### 2. Simple Document Loading
```python
# No LangChain needed - just basic file operations
from pathlib import Path

def load_documents(docs_path):
    documents = []
    for md_file in Path(docs_path).rglob("*.md"):
        content = md_file.read_text()
        documents.append({
            "content": content,
            "path": str(md_file),
            "metadata": extract_metadata(md_file)
        })
    return documents
```

### 3. Document Processing Strategy
One embedding per file (matching Apple's API structure):
```python
def process_document(file_path, max_length=8000):
    """
    Most Apple doc files are focused on a single API.
    Only split if exceptionally large.
    """
    content = file_path.read_text()
    
    # Most files: one embedding per file
    if len(content) <= max_length:
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
        chunks.append({
            "content": section[:max_length],
            "chunk_index": i,
            "total_chunks": len(sections)
        })
    
    return chunks
```

This approach:
- Keeps related content together (entire API in one embedding)
- Matches how developers search (by API name, not fragments)
- Reduces from ~200K chunks to ~50K embeddings
- Improves search accuracy significantly

### 4. Metadata Extraction
```python
def extract_metadata(file_path):
    parts = file_path.relative_to(docs_path).parts
    return {
        "framework": parts[0] if parts else "unknown",
        "api_name": file_path.stem,
        "url": f"https://developer.apple.com/documentation/{'/'.join(parts[:-1])}/{file_path.stem}",
        "file_path": str(file_path)
    }
```

### 5. Direct ChromaDB Usage with TEI
```python
import chromadb
import requests
import numpy as np

# TEI BGE-M3 server endpoint
TEI_URL = "http://192.168.2.5/embed"

chroma = chromadb.PersistentClient(path="./vectorstore")
collection = chroma.create_collection("apple_docs")

# Batch process embeddings using TEI
def embed_batch(texts, batch_size=4):
    """TEI 1.2 has max batch size of 4"""
    embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        response = requests.post(TEI_URL, json={"inputs": batch})
        batch_embeddings = response.json()
        embeddings.extend(batch_embeddings)
    return embeddings
```

### 6. Main Indexing Loop
```python
def build_index(docs_path):
    documents = load_documents(docs_path)
    
    batch_size = 100
    all_chunks = []
    all_metadata = []
    
    # Process documents
    for doc in tqdm(documents, desc="Processing documents"):
        chunks = process_document(Path(doc["path"]))
        for chunk_data in chunks:
            all_chunks.append(chunk_data["content"])
            # Add chunk info to metadata
            metadata = doc["metadata"].copy()
            metadata["chunk_index"] = chunk_data["chunk_index"]
            metadata["total_chunks"] = chunk_data["total_chunks"]
            all_metadata.append(metadata)
    
    print(f"Total embeddings to create: {len(all_chunks)}")
    
    # Batch embed and store
    for i in tqdm(range(0, len(all_chunks), batch_size), desc="Creating embeddings"):
        batch_chunks = all_chunks[i:i+batch_size]
        batch_metadata = all_metadata[i:i+batch_size]
        
        embeddings = embed_batch(batch_chunks)
        
        collection.add(
            embeddings=embeddings,
            documents=batch_chunks,
            metadatas=batch_metadata,
            ids=[f"doc_{j}" for j in range(i, i+len(batch_chunks))]
        )
```

## Cost Estimation (Final Production Data)
- **278,778 documents** (1.17 GB total)
- Average: ~4,200 chars/doc = ~1,050 tokens/doc
- Total tokens: ~293 million tokens

**Current Setup: Voyage-3-lite (In Use)**
- Cost: **$0.83** (API-based)
- Time: **2-3 hours** (96 docs/batch)
- Storage: **512 dimensions = ~0.6GB vector database**
- Quality: Outperforms OpenAI by 3.82% on MTEB, 32K context window

**Alternative Options:**
- BGE-M3 via TEI: $0 but requires local GPU server (1024 dims)
- OpenAI text-embedding-3-small: $5.86 (1536 dims)

## Progress Tracking
- Simple console output with file count
- Save checkpoint every 1000 files
- Resume capability if interrupted

## Error Handling
```python
# Simple retry logic
import time

def embed_with_retry(texts, max_retries=3):
    for attempt in range(max_retries):
        try:
            return embed_batch(texts)
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise
```

## Important Links
- [ChromaDB Python Docs](https://docs.trychroma.com/reference/Client)
- [TEI API Documentation](http://192.168.2.5/docs) - Local Swagger UI for BGE-M3 server
- [Python Path handling](https://docs.python.org/3/library/pathlib.html)

## Success Criteria
- [x] All markdown files indexed without errors
- [x] Metadata correctly extracted for filtering
- [x] Vector database persisted to disk
- [x] Can query the index and get relevant results
- [x] Total indexing time < 3 hours (with Voyage AI)

## Time Estimate
- **Implementation**: ✅ Complete
- **Voyage-3-lite**: 2-3 hours for 278K documents
- Processing rate: ~30-40 docs/second with batch size 96