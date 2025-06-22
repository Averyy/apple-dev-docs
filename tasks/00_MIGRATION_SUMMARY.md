# Meilisearch Migration - Executive Summary

## Overview
Migrate Apple Developer Documentation search from ChromaDB (vector embeddings) to Meilisearch (full-text search) to improve search quality, reduce costs, and simplify operations.

## Key Benefits
- **Better Search Quality**: Full-text search more suitable for API documentation
- **Cost Reduction**: No OpenAI API costs for embeddings
- **Performance**: Sub-100ms search latency
- **Simplicity**: No embedding generation or vector math
- **Maintainability**: Easier to debug and understand

## Architecture Change
```
Before: Docs → OpenAI Embeddings → ChromaDB → RAG Engine → MCP Server
After:  Docs → Meilisearch → Adapter → meilisearch-mcp → Stdio Wrapper → MCP Server
```

## Critical Discoveries

### 1. API Compatibility Challenge
- **Issue**: meilisearch-mcp provides generic tools, not our specific API
- **Solution**: Adapter layer to maintain backward compatibility

### 2. Network Architecture
- **Issue**: Meilisearch on separate server (192.168.2.5)
- **Solution**: Stdio wrapper to bridge network gap

### 3. Document Structure
- **Issue**: Large documents may need splitting
- **Solution**: Intelligent chunking strategy preserving context

## Files to Remove (Post-Migration)
1. `mcp-server/server/rag.py`
2. `mcp-server/server/rag_improvements.py`
3. `mcp-server/scripts/build_index.py`
4. `mcp-server/tests/test_embedding_features.py`
5. `mcp-server/test_comprehensive_metrics.py`
6. `mcp-server/test_comprehensive_search.py`

**Keep**: `vectorstore/` directories for rollback capability

## Implementation Components

### 1. Docker Deployment (`docker-compose.yml`)
- Meilisearch v1.6 with production settings
- Persistent storage volume
- Health checks and auto-restart
- 200MB payload limit for large docs

### 2. Indexing Script (`meilisearch_index.py`)
- Metadata extraction from markdown
- Intelligent document splitting
- Incremental updates via hashing
- Progress tracking

### 3. Stdio Wrapper (`meilisearch_stdio_wrapper.py`)
- Subprocess management for meilisearch-mcp
- Network bridge to remote Meilisearch
- Error handling and health checks
- Logging for debugging

### 4. Adapter Layer (`meilisearch_adapter.py`)
- Maps our API to meilisearch-mcp tools
- Handles filter building
- Link transformation
- Framework listing implementation

### 5. Index Configuration
- **Searchable**: api_name > title > overview > content > framework
- **Filterable**: framework, platforms, is_framework_main, kind
- **Typo tolerance**: Enabled with exceptions for technical terms
- **Synonyms**: Common variations (swiftui → swift ui)

## Risk Mitigations

| Risk | Mitigation |
|------|------------|
| Search quality degradation | Extensive testing, attribute prioritization |
| Performance issues | Native filtering, proper indexing |
| API breaking changes | Adapter layer maintains compatibility |
| Deployment failures | Incremental rollout, keep ChromaDB |
| Data loss | Backups, hash-based change tracking |

## Success Metrics
- ✓ All 361+ frameworks searchable
- ✓ <100ms search latency (95th percentile)
- ✓ Platform filtering works correctly
- ✓ Link transformation preserved
- ✓ Zero data loss
- ✓ Backward compatible API

## Timeline
- **Week 1**: Infrastructure setup, initial indexing
- **Week 2**: Adapter development, integration
- **Week 3**: Testing, performance tuning
- **Week 4**: Deployment, monitoring, cleanup

## Next Steps
1. Review and approve all design documents
2. Provision Meilisearch Docker environment
3. Begin implementation starting with indexing script
4. Incremental testing at each phase
5. Production deployment with monitoring

## Documents Created
1. `meilisearch-migration-plan.md` - Complete migration strategy
2. `stdio-wrapper-design.md` - Network bridge design
3. `meilisearch-adapter-design.md` - API compatibility layer
4. `meilisearch-indexing-strategy.md` - Document processing approach
5. `meilisearch-deployment-checklist.md` - Step-by-step deployment guide

All components have been designed to work together while maintaining the existing API contract and providing a smooth migration path with rollback capability.