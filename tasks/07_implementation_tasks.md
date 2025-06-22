# Meilisearch Implementation Tasks

## Overview
This document breaks down the Meilisearch migration into manageable tasks with clear deliverables and acceptance criteria. Tasks are organized by dependency order and can be completed incrementally.

---

## Phase 1: Infrastructure Setup

### Task 1.1: Deploy Meilisearch Docker Container
**Priority**: High  
**Dependencies**: None  
**Estimated Time**: 2-4 hours

**Deliverables**:
- `docker-compose.yml` for Meilisearch
- `.env` file with secure configuration
- Updated `.gitignore` for data directory

**Acceptance Criteria**:
- [ ] Meilisearch accessible at http://192.168.2.5:7700
- [ ] Health endpoint returns 200 OK
- [ ] Master key authentication working
- [ ] Data persisted across container restarts
- [ ] Logs accessible via `docker-compose logs`

**Verification**:
```bash
curl http://192.168.2.5:7700/health
curl -H "Authorization: Bearer $MEILI_MASTER_KEY" http://192.168.2.5:7700/keys
```

---

### Task 1.2: Create and Configure Index
**Priority**: High  
**Dependencies**: Task 1.1  
**Estimated Time**: 1-2 hours

**Deliverables**:
- `scripts/create_meilisearch_index.py`
- Index configuration applied

**Acceptance Criteria**:
- [ ] Index "apple-docs" created with primary key "id"
- [ ] Searchable attributes configured in priority order
- [ ] Filterable attributes set up (framework, platforms, etc.)
- [ ] Typo tolerance configured
- [ ] Synonyms added for common terms

**Verification**:
```bash
curl -H "Authorization: Bearer $KEY" http://192.168.2.5:7700/indexes/apple-docs/settings
```

---

## Phase 2: Data Migration

### Task 2.1: Build Metadata Extraction
**Priority**: High  
**Dependencies**: None  
**Estimated Time**: 4-6 hours

**Deliverables**:
- `scripts/extract_metadata.py` with functions:
  - `extract_metadata(content, file_path)`
  - `generate_document_id(file_path)`
  - `extract_platforms(content)`

**Acceptance Criteria**:
- [ ] Correctly extracts framework name from **Framework**: tag
- [ ] Extracts API name from # heading
- [ ] Extracts platforms from **Availability**: section
- [ ] Generates consistent document IDs
- [ ] Handles edge cases (missing metadata, special characters)
- [ ] Unit tests pass with >90% coverage

**Verification**:
```python
# Test with sample files
python scripts/test_metadata_extraction.py
```

---

### Task 2.2: Implement Document Chunking
**Priority**: Medium  
**Dependencies**: Task 2.1  
**Estimated Time**: 3-4 hours

**Deliverables**:
- `scripts/document_chunker.py` with:
  - `split_document(content, metadata, max_size=50000)`
  - Chunk relationship tracking

**Acceptance Criteria**:
- [ ] Splits documents >50KB at section boundaries
- [ ] Preserves metadata in all chunks
- [ ] Maintains chunk ordering
- [ ] Handles code blocks without breaking them
- [ ] Unit tests for various document sizes

**Verification**:
```python
# Test with large document
python scripts/test_chunking.py documentation/StoreKit/promoting-in-app-purchases.md
```

---

### Task 2.3: Create Indexing Script
**Priority**: High  
**Dependencies**: Tasks 2.1, 2.2, 1.2  
**Estimated Time**: 6-8 hours

**Deliverables**:
- `scripts/meilisearch_index.py`
- `scripts/indexing_hashes.json` for change tracking

**Acceptance Criteria**:
- [ ] Indexes all .md files in documentation/
- [ ] Tracks file hashes for incremental updates
- [ ] Shows progress with rich output
- [ ] Handles errors gracefully
- [ ] Supports --force flag for full reindex
- [ ] Batches documents for performance
- [ ] Logs detailed information

**Verification**:
```bash
# Dry run
python scripts/meilisearch_index.py --dry-run

# Full index
python scripts/meilisearch_index.py --all

# Verify count
curl -H "Authorization: Bearer $KEY" http://192.168.2.5:7700/indexes/apple-docs/stats
```

---

## Phase 3: MCP Integration

### Task 3.1: Implement Stdio Wrapper
**Priority**: High  
**Dependencies**: None  
**Estimated Time**: 4-6 hours

**Deliverables**:
- `mcp-server/meilisearch_stdio_wrapper.py`
- Wrapper test script

**Acceptance Criteria**:
- [ ] Launches meilisearch-mcp as subprocess
- [ ] Forwards stdio bidirectionally
- [ ] Handles connection errors gracefully
- [ ] Implements health check
- [ ] Logs errors to file
- [ ] Supports --test flag for validation
- [ ] Handles subprocess crashes with restart

**Verification**:
```bash
# Test health check
python meilisearch_stdio_wrapper.py --test

# Test with MCP protocol
echo '{"jsonrpc": "2.0", "method": "initialize", "id": 1}' | python meilisearch_stdio_wrapper.py
```

---

### Task 3.2: Build Adapter Layer
**Priority**: High  
**Dependencies**: Task 3.1  
**Estimated Time**: 6-8 hours

**Deliverables**:
- `mcp-server/server/meilisearch_adapter.py`
- Adapter unit tests

**Acceptance Criteria**:
- [ ] Implements `search_apple_docs()` using meilisearch-mcp
- [ ] Implements `list_frameworks()` with facets
- [ ] Builds proper filter expressions
- [ ] Transforms links to MCP format
- [ ] Handles all platform filtering scenarios
- [ ] Preserves exact API compatibility
- [ ] >80% test coverage

**Verification**:
```python
# Run adapter tests
python -m pytest tests/test_meilisearch_adapter.py -v
```

---

### Task 3.3: Update MCP Server
**Priority**: High  
**Dependencies**: Task 3.2  
**Estimated Time**: 3-4 hours

**Deliverables**:
- Modified `mcp-server/server/mcp_server.py`
- Updated configuration

**Acceptance Criteria**:
- [ ] Uses MeilisearchAdapter instead of RAG
- [ ] Maintains exact same tool signatures
- [ ] Handles errors from adapter gracefully
- [ ] Preserves all existing functionality
- [ ] No breaking changes to API

**Verification**:
```python
# Test with existing test suite
python -m pytest mcp-server/tests/test_mcp_server.py
```

---

## Phase 4: Testing & Validation

### Task 4.1: Create Integration Tests
**Priority**: Medium  
**Dependencies**: Tasks 3.1-3.3  
**Estimated Time**: 4-6 hours

**Deliverables**:
- `tests/test_meilisearch_integration.py`
- Test data fixtures

**Acceptance Criteria**:
- [ ] Tests end-to-end search flow
- [ ] Tests all filter combinations
- [ ] Tests link transformation
- [ ] Tests framework listing
- [ ] Tests error scenarios
- [ ] Performance benchmarks included

**Verification**:
```bash
python -m pytest tests/test_meilisearch_integration.py -v --benchmark
```

---

### Task 4.2: Performance Testing
**Priority**: Medium  
**Dependencies**: Task 4.1  
**Estimated Time**: 2-3 hours

**Deliverables**:
- `tests/performance_test.py`
- Performance comparison report

**Acceptance Criteria**:
- [ ] Measures search latency (p50, p95, p99)
- [ ] Tests concurrent requests
- [ ] Compares with ChromaDB baseline
- [ ] Generates performance report
- [ ] Verifies <100ms p95 latency

**Verification**:
```bash
python tests/performance_test.py --concurrent 10 --duration 60
```

---

### Task 4.3: A/B Comparison Testing
**Priority**: Medium  
**Dependencies**: Task 4.1  
**Estimated Time**: 3-4 hours

**Deliverables**:
- `tests/ab_comparison.py`
- Comparison results report

**Acceptance Criteria**:
- [ ] Tests same queries on both systems
- [ ] Compares result relevance
- [ ] Identifies any regressions
- [ ] Documents behavior differences
- [ ] Generates detailed report

**Verification**:
```bash
python tests/ab_comparison.py --queries tests/test_queries.json
```

---

## Phase 5: Deployment

### Task 5.1: Deploy to Claude Desktop
**Priority**: High  
**Dependencies**: All Phase 4 tasks  
**Estimated Time**: 1-2 hours

**Deliverables**:
- Updated `claude_desktop_config.json`
- Deployment verification script

**Acceptance Criteria**:
- [ ] Claude Desktop config updated
- [ ] MCP server appears in Claude
- [ ] Search commands work in Claude
- [ ] No errors in Claude logs
- [ ] Rollback procedure documented

**Verification**:
- Test in Claude: "search for URLSession"
- Check logs: `~/Library/Logs/Claude/`

---

### Task 5.2: Monitor and Validate
**Priority**: High  
**Dependencies**: Task 5.1  
**Estimated Time**: Ongoing (1 week)

**Deliverables**:
- Monitoring dashboard/script
- Daily health reports

**Acceptance Criteria**:
- [ ] Daily health checks passing
- [ ] No increase in error rates
- [ ] Performance metrics stable
- [ ] User queries successful
- [ ] Backup system operational

**Verification**:
```bash
# Daily validation
./scripts/daily_health_check.sh
```

---

## Phase 6: Cleanup

### Task 6.1: Remove Obsolete Files
**Priority**: Low  
**Dependencies**: 1 week successful operation  
**Estimated Time**: 1-2 hours

**Deliverables**:
- Cleanup script
- Updated requirements.txt

**Acceptance Criteria**:
- [ ] ChromaDB files removed (keeping vectorstore/)
- [ ] Dependencies updated
- [ ] Makefile targets updated
- [ ] All tests still pass
- [ ] Git commit with clear message

**Verification**:
```bash
# Verify nothing broken
python -m pytest
make test
```

---

### Task 6.2: Documentation Update
**Priority**: Medium  
**Dependencies**: Task 6.1  
**Estimated Time**: 2-3 hours

**Deliverables**:
- Updated README.md
- Updated development docs
- Migration guide

**Acceptance Criteria**:
- [ ] README reflects new architecture
- [ ] Setup instructions updated
- [ ] Troubleshooting guide created
- [ ] Architecture diagrams updated
- [ ] API documentation current

**Verification**:
- Technical review by team
- Test setup on fresh machine

---

## Task Tracking

### Quick Reference
| Task | Dependencies | Estimated Hours | Priority |
|------|--------------|-----------------|----------|
| 1.1 Deploy Meilisearch | None | 2-4 | High |
| 1.2 Create Index | 1.1 | 1-2 | High |
| 2.1 Metadata Extraction | None | 4-6 | High |
| 2.2 Document Chunking | 2.1 | 3-4 | Medium |
| 2.3 Indexing Script | 2.1, 2.2, 1.2 | 6-8 | High |
| 3.1 Stdio Wrapper | None | 4-6 | High |
| 3.2 Adapter Layer | 3.1 | 6-8 | High |
| 3.3 Update MCP Server | 3.2 | 3-4 | High |
| 4.1 Integration Tests | 3.1-3.3 | 4-6 | Medium |
| 4.2 Performance Tests | 4.1 | 2-3 | Medium |
| 4.3 A/B Testing | 4.1 | 3-4 | Medium |
| 5.1 Deploy to Claude | Phase 4 | 1-2 | High |
| 5.2 Monitor & Validate | 5.1 | Ongoing | High |
| 6.1 Remove Old Files | 1 week ops | 1-2 | Low |
| 6.2 Update Docs | 6.1 | 2-3 | Medium |

**Total Estimated Time**: 50-75 hours

### Parallel Work Opportunities
- Tasks 1.1 and 2.1 can start immediately
- Tasks 2.1-2.2 and 3.1 can be done in parallel
- Multiple people can work on different test suites

### Critical Path
1.1 → 1.2 → 2.3 → 3.2 → 3.3 → 4.1 → 5.1 → 5.2

This represents the minimum set of tasks that must be completed sequentially for a working system.