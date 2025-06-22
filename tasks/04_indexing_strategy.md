# Meilisearch Indexing Strategy

## Document Structure Analysis

Based on examination of actual documentation files, documents have:

### Metadata Pattern
```markdown
# API Name

**Framework**: FrameworkName
**Kind**: protocol/class/struct/etc (optional)

Description paragraph...

**Availability**:
- iOS 13.0+
- macOS 10.15+
- etc.
```

### Content Sections
- Overview
- Declaration
- Parameters
- Return Value
- Discussion
- Related content
- Code examples

## Indexing Strategy

### 1. Document ID Generation
```python
def generate_document_id(file_path: str) -> str:
    """Generate unique ID from file path"""
    # Example: documentation/SwiftUI/View.md -> swiftui_view
    parts = file_path.split('/')
    framework = parts[-2].lower()
    api_name = parts[-1].replace('.md', '').lower()
    return f"{framework}_{api_name}"
```

### 2. Metadata Extraction
```python
import re
from pathlib import Path

def extract_metadata(content: str, file_path: str) -> dict:
    """Extract metadata from markdown content"""
    metadata = {
        "file_path": file_path,
        "relative_path": str(Path(file_path).relative_to(DOCS_ROOT))
    }
    
    # Extract title (first # heading)
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if title_match:
        metadata["api_name"] = title_match.group(1)
        metadata["title"] = title_match.group(1)
    
    # Extract framework
    framework_match = re.search(r'\*\*Framework\*\*:\s*(.+)', content)
    if framework_match:
        metadata["framework"] = framework_match.group(1).strip()
    
    # Extract kind (optional)
    kind_match = re.search(r'\*\*Kind\*\*:\s*(.+)', content)
    if kind_match:
        metadata["kind"] = kind_match.group(1).strip()
    
    # Extract availability/platforms
    platforms = []
    availability_section = re.search(
        r'\*\*Availability\*\*:(.*?)(?=\n## |\n#|\Z)', 
        content, 
        re.DOTALL
    )
    if availability_section:
        platform_pattern = r'- (iOS|iPadOS|macOS|tvOS|watchOS|visionOS|Mac Catalyst)'
        platforms = re.findall(platform_pattern, availability_section.group(1))
    metadata["platforms"] = list(set(platforms))
    
    # Extract overview (first paragraph after title/metadata)
    overview_match = re.search(
        r'^[^#\*\n]+$\n\n(.+?)(?=\n## |\n#### |\n\*\*|\Z)',
        content,
        re.MULTILINE | re.DOTALL
    )
    if overview_match:
        metadata["overview"] = overview_match.group(1).strip()
    
    # Detect if this is a framework main page
    metadata["is_framework_main"] = file_path.endswith(f"/{metadata.get('framework', '')}.md")
    
    # Generate approximate URL
    rel_path = metadata["relative_path"].replace('.md', '')
    metadata["url"] = f"https://developer.apple.com/{rel_path}"
    
    return metadata
```

### 3. Document Splitting Strategy

For large documents, split intelligently:

```python
def split_document(content: str, metadata: dict, max_size: int = 50000) -> list:
    """Split large documents into logical chunks"""
    if len(content) <= max_size:
        return [{**metadata, "content": content, "chunk_index": 0, "total_chunks": 1}]
    
    # Split by major sections
    sections = re.split(r'\n## ', content)
    chunks = []
    
    for i, section in enumerate(sections):
        if i > 0:
            section = f"## {section}"  # Re-add the header
        
        chunk_metadata = metadata.copy()
        chunk_metadata.update({
            "content": section,
            "chunk_index": i,
            "total_chunks": len(sections),
            "id": f"{metadata['id']}_chunk_{i}"
        })
        chunks.append(chunk_metadata)
    
    return chunks
```

### 4. Meilisearch Index Configuration

```python
async def configure_index(client):
    """Configure Meilisearch index settings"""
    index = client.index("apple-docs")
    
    # Searchable attributes (priority order matters!)
    await index.update_searchable_attributes([
        "api_name",      # Highest priority for exact API matches
        "title",         # Second priority
        "overview",      # Third priority for summaries
        "content",       # Full content search
        "framework"      # Framework name search
    ])
    
    # Filterable attributes
    await index.update_filterable_attributes([
        "framework",
        "platforms",
        "is_framework_main",
        "kind"
    ])
    
    # Sortable attributes
    await index.update_sortable_attributes([
        "api_name",
        "framework"
    ])
    
    # Ranking rules (order matters!)
    await index.update_ranking_rules([
        "words",           # Number of words matched
        "typo",            # Typo tolerance
        "proximity",       # Proximity of matched words
        "attribute",       # Attribute priority (searchable attrs order)
        "sort",            # User-defined sort
        "exactness"        # Exact matches
    ])
    
    # Typo tolerance
    await index.update_typo_tolerance({
        "enabled": True,
        "minWordSizeForTypos": {
            "oneTypo": 4,
            "twoTypos": 8
        },
        "disableOnWords": ["iOS", "macOS", "API", "URL", "ID"],
        "disableOnAttributes": ["api_name", "framework"]
    })
    
    # Stop words (minimal for technical docs)
    await index.update_stop_words(["the", "a", "an"])
    
    # Synonyms for common patterns
    await index.update_synonyms({
        "swiftui": ["swift ui"],
        "uikit": ["ui kit"],
        "coreml": ["core ml", "machine learning"],
        "arkit": ["ar kit", "augmented reality"],
        "async": ["asynchronous"],
        "sync": ["synchronous"]
    })
```

### 5. Incremental Indexing

```python
import hashlib
from datetime import datetime

class IncrementalIndexer:
    def __init__(self, index, hash_file="indexing_hashes.json"):
        self.index = index
        self.hash_file = hash_file
        self.hashes = self.load_hashes()
    
    def should_index(self, file_path: str, content: str) -> bool:
        """Check if file needs re-indexing"""
        content_hash = hashlib.sha256(content.encode()).hexdigest()
        
        if file_path not in self.hashes:
            return True
            
        return self.hashes[file_path] != content_hash
    
    async def index_document(self, file_path: str, content: str):
        """Index a single document"""
        metadata = extract_metadata(content, file_path)
        metadata["last_indexed"] = datetime.utcnow().isoformat()
        
        # Split if needed
        documents = split_document(content, metadata)
        
        # Add to Meilisearch
        await self.index.add_documents(documents)
        
        # Update hash
        content_hash = hashlib.sha256(content.encode()).hexdigest()
        self.hashes[file_path] = content_hash
```

## Performance Optimizations

### 1. Batch Processing
```python
async def index_in_batches(documents: list, batch_size: int = 100):
    """Index documents in batches for better performance"""
    for i in range(0, len(documents), batch_size):
        batch = documents[i:i + batch_size]
        await index.add_documents(batch)
        await asyncio.sleep(0.1)  # Rate limiting
```

### 2. Parallel Processing
```python
async def process_files_parallel(file_paths: list, max_concurrent: int = 10):
    """Process files in parallel with concurrency limit"""
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def process_file(file_path):
        async with semaphore:
            content = await read_file_async(file_path)
            await indexer.index_document(file_path, content)
    
    tasks = [process_file(fp) for fp in file_paths]
    await asyncio.gather(*tasks)
```

### 3. Memory Management
```python
def process_large_dataset():
    """Process files in chunks to manage memory"""
    CHUNK_SIZE = 1000
    
    all_files = list(Path(DOCS_ROOT).rglob("*.md"))
    
    for i in range(0, len(all_files), CHUNK_SIZE):
        chunk = all_files[i:i + CHUNK_SIZE]
        asyncio.run(process_files_parallel(chunk))
        
        # Clear any caches
        gc.collect()
```

## Search Quality Improvements

### 1. Boost Exact Matches
Configure Meilisearch to heavily weight exact matches in api_name field:
- Use attribute position in searchable attributes
- Disable typos on api_name field
- Use exactness ranking rule

### 2. Handle CamelCase
Pre-process queries to handle CamelCase:
```python
def preprocess_query(query: str) -> str:
    """Split CamelCase for better matching"""
    # URLSession -> URL Session
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', query)
```

### 3. Framework Context
When searching within a framework, boost results from that framework:
```python
# Use filter for hard requirement
filter = f'framework = "{framework}"'

# Or use optional filter for soft boost (if Meilisearch supports)
```

## Monitoring and Validation

### 1. Index Statistics
```python
async def validate_index():
    """Validate index completeness"""
    stats = await index.get_stats()
    
    expected_frameworks = 361
    actual_frameworks = len(await index.get_distinct_attribute_values("framework"))
    
    print(f"Documents indexed: {stats['numberOfDocuments']}")
    print(f"Frameworks: {actual_frameworks}/{expected_frameworks}")
    
    # Check for missing frameworks
    if actual_frameworks < expected_frameworks:
        print("WARNING: Some frameworks may be missing")
```

### 2. Search Quality Tests
```python
test_queries = [
    ("URLSession", "Foundation", "URLSession class should be first"),
    ("View protocol", "SwiftUI", "SwiftUI View should be first"),
    ("async await", None, "Should find async/await content"),
    ("machine learning", None, "Should find Core ML content")
]

for query, framework, expectation in test_queries:
    results = await index.search(query, filter=f'framework={framework}' if framework else None)
    print(f"Query: {query} - {expectation}")
    print(f"Top result: {results['hits'][0]['title'] if results['hits'] else 'No results'}")
```

## Common Issues and Solutions

### Issue: Large Documents Timing Out
**Solution**: Split documents more aggressively, use streaming

### Issue: Poor Search Relevance
**Solution**: Adjust searchable attribute order, add synonyms

### Issue: Slow Indexing
**Solution**: Increase batch size, use more parallel workers

### Issue: Memory Usage
**Solution**: Process in chunks, clear caches between batches

### Issue: Special Characters in API Names
**Solution**: Proper escaping in filters, test edge cases