# Meilisearch Migration Plan

## Overview

This document outlines the migration plan from ChromaDB (vector database) to Meilisearch (full-text search engine) for the Apple Developer Documentation MCP server.

## Rationale

The documentation files are not performing well with embeddings-based search. Meilisearch offers:
- Superior full-text search capabilities
- Exact pattern matching for API names
- Powerful filtering and faceting
- Lower operational complexity (no embeddings needed)
- Better performance for documentation search use cases

## Architecture Changes

### Current Architecture (ChromaDB)
```
Documentation Files -> Embeddings (OpenAI) -> ChromaDB -> MCP Server
```

### New Architecture (Meilisearch)
```
Documentation Files -> Meilisearch -> Meilisearch MCP -> Stdio Wrapper -> MCP Server
```

## Implementation Plan

### Phase 1: Infrastructure Setup

#### 1.1 Docker Deployment
- Deploy Meilisearch in Docker container
- Configure persistent volume for data (gitignore if >50MB)
- Set up master key for security
- Configure for network access on 192.168.2.5

```yaml
# docker-compose.yml
version: '3.8'
services:
  meilisearch:
    image: getmeili/meilisearch:latest
    ports:
      - "7700:7700"
    environment:
      - MEILI_MASTER_KEY=${MEILI_MASTER_KEY}
      - MEILI_ENV=production
    volumes:
      - ./meilisearch-data:/meili_data
    restart: unless-stopped
```

#### 1.2 Stdio Wrapper
Create a Python stdio wrapper that:
- Launches meilisearch-mcp server as subprocess
- Handles stdio communication between Claude Code and remote Meilisearch
- Manages authentication and connection parameters
- Provides graceful error handling

### Phase 2: Data Migration

#### 2.1 Index Design

Primary index: `apple-docs`

Document Structure:
```json
{
  "id": "framework_api_name",
  "framework": "SwiftUI",
  "api_name": "View",
  "title": "View Protocol Reference",
  "content": "Full markdown content...",
  "overview": "First paragraph of content",
  "url": "https://developer.apple.com/...",
  "file_path": "/documentation/SwiftUI/View.md",
  "platforms": ["iOS", "macOS", "tvOS"],
  "is_framework_main": false,
  "last_modified": "2024-01-15T10:30:00Z"
}
```

#### 2.2 Meilisearch Configuration

Searchable Attributes (in priority order):
1. `api_name`
2. `title`
3. `overview`
4. `content`
5. `framework`

Filterable Attributes:
- `framework`
- `platforms`
- `is_framework_main`

Sortable Attributes:
- `last_modified`
- `api_name`

#### 2.3 Indexing Script
Create `meilisearch_index.py` that:
- Reads all markdown files from documentation/
- Extracts metadata (framework, API name, platforms)
- Creates documents for Meilisearch
- Handles incremental updates via hash tracking
- Shows progress with rich console output

### Phase 3: MCP Server Integration

#### 3.1 Update MCP Server
Modify `mcp_server.py` to:
- Use meilisearch-mcp client instead of RAG engine
- Maintain existing API interface (search_apple_docs, list_frameworks)
- Transform search parameters to Meilisearch format
- Handle response transformation

#### 3.2 Search Implementation
Map current search features to Meilisearch:

| Current Feature | Meilisearch Implementation |
|----------------|---------------------------|
| Platform filtering | Use filter: `platforms IN [ios, macos]` |
| Framework filtering | Use filter: `framework = SwiftUI` |
| Relevance boosting | Configure searchable attributes order |
| Link transformation | Keep existing post-processing |
| Full content return | Use Meilisearch's built-in feature |

### Phase 4: Testing & Validation

#### 4.1 Test Suite
- Unit tests for stdio wrapper
- Integration tests for search queries
- Performance benchmarks vs ChromaDB
- Platform filtering validation
- Framework discovery tests

#### 4.2 Validation Queries
Test common search patterns:
- API name searches (e.g., "URLSession")
- Framework + API searches (e.g., "SwiftUI View")
- Platform-specific searches
- Framework listing with summaries

### Phase 5: Deployment

#### 5.1 Deployment Steps
1. Deploy Meilisearch container
2. Run indexing script
3. Deploy stdio wrapper
4. Update MCP server configuration
5. Test deployed server at 192.168.2.5
6. Update documentation

#### 5.2 Rollback Plan
- Keep ChromaDB vectorstore intact
- Maintain old RAG code (commented)
- Document rollback procedure
- Keep performance metrics for comparison

## Benefits of Migration

1. **Better Search Quality**
   - Exact matching for API names
   - Fuzzy search for typos
   - Better handling of camelCase
   - No LLM pattern false positives

2. **Improved Performance**
   - No embedding generation needed
   - Faster indexing (no OpenAI API calls)
   - Lower latency searches
   - Better caching capabilities

3. **Operational Simplicity**
   - No OpenAI API dependency for indexing
   - Simpler debugging (readable index)
   - Better monitoring tools
   - Easier to understand/maintain

4. **Cost Savings**
   - No OpenAI embedding costs
   - Lower computational requirements
   - Reduced memory usage

## Risk Mitigation

- **Risk**: Search quality degradation
  - **Mitigation**: Extensive testing, A/B comparison, gradual rollout

- **Risk**: Deployment complexity
  - **Mitigation**: Docker containerization, detailed runbooks

- **Risk**: Data loss
  - **Mitigation**: Keep ChromaDB intact, backup procedures

- **Risk**: MCP compatibility issues
  - **Mitigation**: Stdio wrapper testing, error handling

## Timeline

- Week 1: Infrastructure setup and stdio wrapper
- Week 2: Indexing script and data migration
- Week 3: MCP server integration and testing
- Week 4: Deployment and documentation

## Success Criteria

1. All existing search queries work with equal or better quality
2. Search latency < 100ms for 95% of queries
3. Platform filtering works correctly
4. Framework listing maintains current functionality
5. Zero data loss during migration
6. Successful deployment on 192.168.2.5

## Files to Remove After Migration

### Core ChromaDB/RAG Files
1. `mcp-server/server/rag.py` - Main RAG engine
2. `mcp-server/server/rag_improvements.py` - Multi-term query improvements
3. `mcp-server/scripts/build_index.py` - Embedding generation script

### Test Files (Embedding-specific)
4. `mcp-server/tests/test_embedding_features.py`
5. `mcp-server/test_comprehensive_metrics.py`
6. `mcp-server/test_comprehensive_search.py`

### Scripts Referencing RAG
7. `mcp-server/scripts/self_test.py` (if it only tests RAG)
8. `mcp-server/scripts/run_self_test_on_startup.py` (if RAG-specific)

### Files to Modify (not remove)
- `mcp-server/server/config.py` - Remove embedding configurations
- `mcp-server/requirements.txt` - Remove chromadb, openai dependencies
- `mcp-server/Makefile` - Remove index-related targets
- `mcp-server/server/mcp_server.py` - Update to use Meilisearch

### Keep for Rollback
- `mcp-server/vectorstore/` directory
- `vectorstore/` directory at root

## Critical Issues & Considerations

### 1. Meilisearch-MCP Limitations

**Issue**: The meilisearch-mcp server provides generic tools that don't match our current API:
- Generic `search` tool vs our specific `search_apple_docs`
- No built-in link transformation
- No framework listing with summaries

**Solution**: Create an adapter layer that:
- Maps our MCP tools to meilisearch-mcp tools
- Handles link transformation post-search
- Implements framework listing using facets

### 2. Document Size Limitations

**Issue**: Meilisearch has practical limits:
- Default payload limit: 100MB
- Document size affects performance
- Large documents may need chunking

**Solution**: 
- Split large documentation files into logical sections
- Index with section references
- Maintain document relationships

### 3. Search Quality Differences

**Issue**: Moving from semantic to keyword search changes behavior:
- No semantic understanding of queries
- Exact matching becomes more important
- Typos handled differently

**Solution**:
- Configure typo tolerance appropriately
- Use searchable attributes priority
- Consider hybrid search for future (requires embeddings)

### 4. Platform Filtering Performance

**Issue**: Current post-query platform filtering is inefficient

**Solution**: Use Meilisearch's native filtering:
```
filter: "platforms IN [ios, macos]"
```

### 5. MCP Protocol Compatibility

**Issue**: meilisearch-mcp uses different tool signatures

**Solution**: Wrapper must translate between:
- Our tools: `search_apple_docs(query, framework, platform, limit)`
- Their tools: `search(indexUid, q, filter, limit, attributesToRetrieve)`

### 6. Multi-Index Consideration

**Issue**: Should we use one index or multiple?

**Recommendation**: Single index `apple-docs` because:
- Simpler filtering by framework
- Easier maintenance
- Better performance for our use case

### 7. Deployment Complexity

**Issue**: Running Meilisearch + meilisearch-mcp + wrapper adds layers

**Solution**: 
- Docker compose for orchestration
- Health checks at each layer
- Comprehensive logging

### 8. Data Persistence

**Issue**: Meilisearch data directory can grow large

**Solution**:
- Mount volume for `/meili_data`
- Add to `.gitignore` if >50MB
- Regular backups

### 9. Security Considerations

**Issue**: API keys and network exposure

**Solution**:
- Use master key for production
- Restrict network access
- Implement rate limiting

### 10. Testing Strategy

**Critical Tests**:
1. All 361+ frameworks searchable
2. Platform filtering works correctly
3. Link transformation preserves functionality
4. Performance meets <100ms target
5. Framework listing maintains summaries

## Updated Implementation Notes

### Meilisearch Configuration
```javascript
// Searchable attributes (priority order)
["api_name", "title", "overview", "content", "framework"]

// Filterable attributes
["framework", "platforms", "is_framework_main"]

// Faceted attributes for framework listing
["framework", "platforms"]

// Typo tolerance
{ "enabled": true, "minWordSizeForTypos": { "oneTypo": 4, "twoTypos": 8 } }
```

### Adapter Pattern
```python
class MeilisearchAdapter:
    async def search_apple_docs(self, query, framework, platform, limit):
        # Build Meilisearch filter
        filters = []
        if framework:
            filters.append(f'framework = "{framework}"')
        if platform and platform != "all":
            filters.append(f'platforms IN [{platform}]')
        
        # Call meilisearch-mcp search
        results = await self.mcp_client.search(
            indexUid="apple-docs",
            q=query,
            filter=" AND ".join(filters),
            limit=limit
        )
        
        # Transform results
        return self.transform_results(results)
```

## Next Steps

1. Review and approve this plan with all considerations
2. Set up development environment
3. Begin Phase 1 implementation
4. Create detailed task tickets for each component
5. Plan for incremental testing at each phase