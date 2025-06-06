# Task 2: Build Vector Index

## Objective
Create a one-time indexing script to convert all Apple documentation into searchable vector embeddings using direct API calls.

## Prerequisites
- Task 1 completed (environment setup)
- OpenAI API key configured
- Apple documentation in markdown format

## Implementation Steps

### 1. Embedding Model
- **OpenAI text-embedding-3-small**: 1536 dimensions, $0.02/1M tokens
- Best balance of quality, cost, and integration

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

### 5. Direct ChromaDB Usage
```python
import chromadb
from openai import OpenAI

client = OpenAI()
chroma = chromadb.PersistentClient(path="./vectorstore")
collection = chroma.create_collection("apple_docs")

# Batch process embeddings
def embed_batch(texts):
    response = client.embeddings.create(
        input=texts,
        model="text-embedding-3-small"
    )
    return [e.embedding for e in response.data]
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

## Cost Estimation (Updated for Actual Data)
- ~45K documents × ~1000 tokens/doc = ~45M tokens
- Using text-embedding-3-small: ~$0.90 one-time cost
- With one-file-per-embedding: ~50K embeddings total
- Final cost: **~$1-2** (not $5!)
- Storage: ~1.6GB for vector database (not 8GB!)

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
- [OpenAI Embeddings API](https://platform.openai.com/docs/api-reference/embeddings)
- [Python Path handling](https://docs.python.org/3/library/pathlib.html)

## Success Criteria
- [ ] All markdown files indexed without errors
- [ ] Metadata correctly extracted for filtering
- [ ] Vector database persisted to disk
- [ ] Can query the index and get relevant results
- [ ] Total indexing time < 5 hours

## Time Estimate
1-2 hours to implement, 1 hour to run initial indexing (50K embeddings, not 200K!)