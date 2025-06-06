# Task 3: Implement Simple RAG Engine

## Objective
Build a minimal retrieval engine that searches Apple docs and returns raw results to Claude (no GPT-4 needed).

## Prerequisites
- Task 2 completed (vector index built)
- Understanding of vector similarity search
- TEI BGE-M3 server running (at 192.168.2.5)

## Why No GPT-4?
Since Claude is already an LLM:
1. **Claude handles reasoning**: No need for another LLM
2. **Cost savings**: 2,500x cheaper (just embedding costs)
3. **Simpler architecture**: Less code, fewer dependencies
4. **Faster responses**: No generation step needed
5. **Claude gets full context**: Can see all retrieved chunks directly

## Implementation Components

### 1. Simple Search Class
```python
# rag.py
import chromadb
import requests
from typing import List, Dict, Optional

class SimpleRAG:
    def __init__(self):
        self.tei_url = "http://192.168.2.5/embed"
        self.chroma = chromadb.PersistentClient(path="./vectorstore")
        self.collection = self.chroma.get_collection("apple_docs")
```

### 2. Basic Search Method
```python
async def search(self, 
                query: str, 
                framework: Optional[str] = None,
                limit: int = 5) -> List[Dict]:
    
    # 1. Embed the query using TEI
    response = requests.post(
        self.tei_url,
        json={"inputs": [query]}
    )
    embedding = response.json()[0]  # TEI returns nested array
    
    # 2. Search with optional filtering
    where_clause = {"framework": framework} if framework else None
    
    results = self.collection.query(
        query_embeddings=[embedding],
        n_results=limit,
        where=where_clause
    )
    
    # 3. Format results for Claude
    formatted_results = []
    for i in range(len(results['documents'][0])):
        formatted_results.append({
            "content": results['documents'][0][i],
            "metadata": results['metadatas'][0][i],
            "distance": results['distances'][0][i] if 'distances' in results else None
        })
    
    return formatted_results
```

### 3. Query Enhancement (Optional)
Simple query expansion without LLM:
```python
def expand_query(self, query: str) -> str:
    # Simple keyword expansion
    expansions = {
        "swiftui": "SwiftUI View",
        "uikit": "UIKit UIViewController",
        "async": "async await Task concurrency",
        "list": "List ForEach ScrollView",
        "button": "Button ButtonStyle onTapGesture"
    }
    
    query_lower = query.lower()
    for key, expansion in expansions.items():
        if key in query_lower:
            query = f"{query} {expansion}"
    
    return query
```

### 3.5 Markdown Handling Based on Environment
```python
import os

class SimpleRAG:
    def __init__(self):
        # ... existing init ...
        self.keep_markdown = os.getenv('KEEP_MARKDOWN_FILES', 'true').lower() == 'true'
    
    async def process_changed_document(self, url: str, new_etag: str):
        # Download JSON
        json_data = await self.download_json(url)
        
        # Convert to markdown
        markdown_content = self.json_to_markdown(json_data)
        
        # Generate embedding and store in vector DB
        await self.embed_and_store(markdown_content, metadata)
        
        # Handle markdown based on environment
        if self.keep_markdown:
            # Save to disk for development/debugging
            self.save_markdown_file(markdown_content, url)
        # else: discard markdown (production mode)
```

### 4. Advanced Search Features

#### a. Multi-Query Search
Search with multiple related queries:
```python
async def multi_search(self, queries: List[str], limit: int = 3) -> List[Dict]:
    all_results = []
    seen_ids = set()
    
    for query in queries:
        results = await self.search(query, limit=limit)
        for result in results:
            # Deduplicate results
            doc_id = result['metadata'].get('file_path')
            if doc_id not in seen_ids:
                seen_ids.add(doc_id)
                all_results.append(result)
    
    return all_results
```

#### b. Get Specific API Documentation
Direct lookup by API name:
```python
async def get_api_doc(self, api_name: str, framework: str) -> Optional[Dict]:
    results = await self.search(
        query=api_name,
        framework=framework,
        limit=10
    )
    
    # Find exact match
    for result in results:
        if result['metadata']['api_name'].lower() == api_name.lower():
            return result
    
    # Return best match if no exact match
    return results[0] if results else None
```

### 5. Results Formatting
Format results for optimal Claude consumption:
```python
def format_for_mcp(self, results: List[Dict]) -> str:
    formatted = []
    
    for i, result in enumerate(results, 1):
        meta = result['metadata']
        formatted.append(
            f"## Result {i}: {meta['api_name']} ({meta['framework']})\n"
            f"**URL**: {meta['url']}\n"
            f"**Content**:\n{result['content']}\n"
            f"---\n"
        )
    
    return "\n".join(formatted)
```

## Cost Analysis

### Per Query Costs
- Query embedding: **$0** (using local TEI server)
- No generation costs!
- Total: **$0 per query**

### Monthly Costs
- **$0** - All embeddings done locally via TEI
- Compare to OpenAI approach: $0.06/month
- Compare to GPT-4 approach: ~$150/month
- **Savings: Infinite!**

## Simple Enhancement Options

1. **Query Caching** (if needed later):
   - Cache common queries in memory
   - Simple dict with query → results

2. **Metadata Filtering**:
   - Filter by platform (iOS/macOS)
   - Filter by doc type (class/method/property)

3. **Similarity Threshold**:
   - Only return results above certain similarity
   - Helps Claude focus on relevant content

## Important Links
- [ChromaDB Query API](https://docs.trychroma.com/reference/Collection#query)
- [TEI API Documentation](http://192.168.2.5/docs) - Local Swagger UI for BGE-M3 server
- [TEI GitHub](https://github.com/huggingface/text-embeddings-inference)
- [BGE-M3 Model](https://huggingface.co/BAAI/bge-m3)

## Success Criteria
- [ ] Can search and retrieve relevant documents
- [ ] Results include proper metadata
- [ ] Framework filtering works correctly
- [ ] Response time < 500ms
- [ ] Claude can understand and use the results

## Time Estimate
4-6 hours to implement (much simpler than before!)