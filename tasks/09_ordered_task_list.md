# Meilisearch Migration - Ordered Task List

All tasks numbered in execution order. Build and test everything locally first, Docker is only for production deployment.

---

## 01_install_meilisearch_locally
**Time**: 30 minutes  
**Dependencies**: None

**Deliverable**: Meilisearch running locally on your development machine

**Steps**:
```bash
# macOS
brew install meilisearch

# Or download binary
curl -L https://install.meilisearch.com | sh

# Start locally
meilisearch --master-key="local_test_key"
```

**Acceptance Criteria**:
- [ ] Meilisearch running on http://localhost:7700
- [ ] Can access health endpoint
- [ ] Can create test index

---

## 02_create_metadata_extractor
**Time**: 2-3 hours  
**Dependencies**: None

**Deliverable**: `scripts/metadata_extractor.py`

**Implementation**:
```python
# Core functions to implement:
def extract_metadata(content: str, file_path: str) -> dict
def generate_document_id(file_path: str) -> str
def extract_platforms(content: str) -> list
def extract_framework_info(content: str) -> dict
```

**Acceptance Criteria**:
- [ ] Extracts framework, API name, platforms correctly
- [ ] Handles missing metadata gracefully
- [ ] Unit tests pass
- [ ] Works on 10 sample documents

**Test Command**:
```bash
python scripts/metadata_extractor.py documentation/SwiftUI/View.md
```

---

## 03_create_document_processor
**Time**: 2 hours  
**Dependencies**: 02_create_metadata_extractor

**Deliverable**: `scripts/document_processor.py`

**Implementation**:
- Document chunking for large files
- Overview extraction
- URL generation
- Content cleaning

**Acceptance Criteria**:
- [ ] Splits documents >50KB intelligently
- [ ] Preserves code blocks intact
- [ ] Generates correct URLs
- [ ] Maintains chunk relationships

**Test Command**:
```bash
python scripts/document_processor.py --test documentation/StoreKit/
```

---

## 04_build_indexing_script
**Time**: 3-4 hours  
**Dependencies**: 02, 03

**Deliverable**: `scripts/index_to_meilisearch.py`

**Features**:
- Read all .md files
- Extract metadata
- Process documents
- Batch upload to Meilisearch
- Progress tracking
- Hash-based incremental updates

**Acceptance Criteria**:
- [ ] Indexes documents to local Meilisearch
- [ ] Shows progress with rich output
- [ ] Supports --dry-run mode
- [ ] Tracks file hashes for updates
- [ ] Handles errors gracefully

**Test Command**:
```bash
# Dry run first
python scripts/index_to_meilisearch.py --dry-run --limit 100

# Then real run
python scripts/index_to_meilisearch.py --limit 100
```

---

## 05_configure_meilisearch_index
**Time**: 1 hour  
**Dependencies**: 04

**Deliverable**: `scripts/configure_index.py`

**Configuration**:
- Searchable attributes priority
- Filterable attributes
- Typo tolerance
- Synonyms
- Ranking rules

**Acceptance Criteria**:
- [ ] Index settings applied successfully
- [ ] Search prioritizes API names
- [ ] Filtering works for platforms/frameworks
- [ ] Typo tolerance configured

**Test Command**:
```bash
python scripts/configure_index.py
curl http://localhost:7700/indexes/apple-docs/settings
```

---

## 06_benchmark_current_system
**Time**: 2 hours  
**Dependencies**: None

**Deliverable**: `tests/chromadb_baseline.py` and baseline metrics report

**Metrics to Capture**:
- Search latency (p50, p95, p99)
- Relevance quality scores
- Memory usage
- Query patterns that work well
- Query patterns that fail

**Acceptance Criteria**:
- [ ] Baseline performance documented
- [ ] Test query set created (50+ queries)
- [ ] Relevance quality metrics captured
- [ ] Report generated in `benchmarks/chromadb_baseline.json`

**Test Command**:
```bash
python tests/chromadb_baseline.py --save-report benchmarks/chromadb_baseline.json
```

---

## 07_test_search_quality
**Time**: 2 hours  
**Dependencies**: 05, 06

**Deliverable**: `tests/test_search_quality.py`

**Test Cases**:
- API name searches
- Framework filtering
- Platform filtering
- Typo tolerance
- Multi-word queries
- MCP pattern queries ("api_name in framework")
- CamelCase queries

**Acceptance Criteria**:
- [ ] All test queries return expected results
- [ ] Performance better than ChromaDB baseline
- [ ] Relevance scoring correct
- [ ] Filters work properly
- [ ] Special patterns handled

**Test Command**:
```bash
python tests/test_search_quality.py -v --compare-baseline benchmarks/chromadb_baseline.json
```

---

## 08_install_meilisearch_mcp
**Time**: 1 hour  
**Dependencies**: None

**Deliverable**: meilisearch-mcp package installed and tested

**Steps**:
```bash
# Install package
pip install meilisearch-mcp

# Or from source
git clone https://github.com/meilisearch/meilisearch-mcp
cd meilisearch-mcp && pip install -e .
```

**Acceptance Criteria**:
- [ ] Package installed successfully
- [ ] Can import in Python
- [ ] Basic connection test works
- [ ] Understand available tools

---

## 09_create_stdio_wrapper
**Time**: 4-5 hours  
**Dependencies**: 08

**Deliverable**: `mcp-server/stdio_wrapper.py`

**Implementation**:
- Launch meilisearch-mcp as subprocess
- Forward stdio bidirectionally
- Handle errors and restarts
- Health checks with HTTP endpoint exposure
- Session management forwarding
- Bearer token authentication handling
- FastMCP transport compatibility

**Acceptance Criteria**:
- [ ] Wrapper starts meilisearch-mcp
- [ ] Forwards messages correctly
- [ ] Handles connection to local Meilisearch
- [ ] Health endpoint accessible
- [ ] Session IDs preserved
- [ ] Bearer auth works
- [ ] Test mode works

**Test Command**:
```bash
# Test locally
MEILISEARCH_URL=http://localhost:7700 \
MCP_API_KEY=test_key \
python mcp-server/stdio_wrapper.py --test

# Test health endpoint
curl http://localhost:8080/health
```

---

## 10_build_api_adapter
**Time**: 6-8 hours  
**Dependencies**: 09

**Deliverable**: `mcp-server/meilisearch_adapter.py`

**Implementation**:
- Map search_apple_docs to meilisearch-mcp search
- Map list_frameworks to faceted search
- Handle filter building
- Transform links
- **Query preprocessing**:
  - CamelCase splitting (URLSession → URL Session)
  - LLM pattern removal
  - Query expansion for framework normalization
- **Relevance scoring algorithm**:
  - MCP pattern detection ("api_name in framework")
  - Multi-term coverage boost calculation
  - Generic term penalty (init, frame, etc.)
  - Distance-based relevance decay
  - Filename matching priority

**Acceptance Criteria**:
- [ ] search_apple_docs() works identically to current
- [ ] list_frameworks() returns all frameworks
- [ ] Platform filtering works
- [ ] Link transformation correct
- [ ] CamelCase queries handled
- [ ] MCP patterns boost correctly
- [ ] Multi-term queries scored properly
- [ ] Relevance matches or exceeds ChromaDB

**Test Command**:
```bash
python -m pytest tests/test_meilisearch_adapter.py -v
python tests/test_relevance_scoring.py
```

---

## 11_integrate_adapter_with_mcp
**Time**: 4-5 hours  
**Dependencies**: 10

**Deliverable**: Updated `mcp-server/server/mcp_server.py`

**Changes**:
- Import MeilisearchAdapter
- Replace RAG calls with adapter
- Maintain exact API signatures
- Add fallback error handling
- **Implement MCP Resources**:
  - `resource://frameworks` - Framework summary
  - `resource://stats` - Index statistics
- **Implement MCP Prompts**:
  - `analyze_api` prompt
  - `compare_frameworks` prompt
- **FastMCP transport setup**:
  - Session management
  - Bearer token authentication
  - Health endpoint
  - Root endpoint

**Acceptance Criteria**:
- [ ] All existing tests pass
- [ ] No API changes
- [ ] Error handling works
- [ ] Resources return correct data
- [ ] Prompts generate correctly
- [ ] FastMCP transport works
- [ ] Session management functional
- [ ] Bearer auth enforced

**Test Command**:
```bash
# Run existing test suite
cd mcp-server && python -m pytest tests/ -v

# Test resources
curl http://localhost:8080/mcp/v1/resources/frameworks
curl http://localhost:8080/mcp/v1/resources/stats
```

---

## 12_test_full_local_setup
**Time**: 2 hours  
**Dependencies**: 10

**Deliverable**: `tests/test_local_integration.py`

**Testing**:
- End-to-end search flow
- All tool functions
- Error scenarios
- Performance benchmarks

**Acceptance Criteria**:
- [ ] Complete search flow works locally
- [ ] All filters work
- [ ] Performance meets targets
- [ ] No regressions from ChromaDB

**Test Command**:
```bash
# Full integration test
python tests/test_local_integration.py --benchmark
```

---

## 13_create_performance_comparison
**Time**: 2 hours  
**Dependencies**: 11

**Deliverable**: `tests/performance_comparison.py`

**Metrics**:
- Search latency (p50, p95, p99)
- Indexing speed
- Memory usage
- Concurrent request handling

**Acceptance Criteria**:
- [ ] Meilisearch faster than ChromaDB
- [ ] <100ms p95 latency
- [ ] Lower memory usage
- [ ] Handles 10+ concurrent requests

**Test Command**:
```bash
python tests/performance_comparison.py --save-report
```

---

## 14_configure_claude_desktop_local
**Time**: 1 hour  
**Dependencies**: 11

**Deliverable**: Updated Claude Desktop config for local testing

**Configuration**:
```json
{
  "mcpServers": {
    "apple-docs-local": {
      "command": "python",
      "args": ["path/to/stdio_wrapper.py"],
      "env": {
        "MEILISEARCH_URL": "http://localhost:7700",
        "MEILISEARCH_API_KEY": "local_test_key"
      }
    }
  }
}
```

**Acceptance Criteria**:
- [ ] Claude Desktop connects to local wrapper
- [ ] Search commands work
- [ ] No errors in logs
- [ ] Can switch between old/new

---

## 15_validate_with_users
**Time**: 1 week (passive)  
**Dependencies**: 13

**Deliverable**: Validation report

**Testing**:
- Use locally for 1 week
- Track any issues
- Compare search quality
- Gather feedback

**Acceptance Criteria**:
- [ ] No major issues found
- [ ] Search quality equal or better
- [ ] Performance acceptable
- [ ] Ready for production

---

## 16_create_docker_deployment
**Time**: 3-4 hours  
**Dependencies**: 15

**Deliverable**: `docker/docker-compose.yml` and deployment scripts

**Components**:
- Meilisearch container
- Environment configuration
- Volume mounts
- Health checks
- Backup setup
- **Self-test integration**:
  - Migrate current self_test.py
  - Run on container startup
  - Supervisor configuration
  - Startup validation

**Acceptance Criteria**:
- [ ] Docker compose works
- [ ] Data persists across restarts
- [ ] Backups configured
- [ ] Monitoring ready
- [ ] Self-test runs on startup
- [ ] Health checks pass
- [ ] Supervisor manages processes

**Test Command**:
```bash
cd docker && docker-compose up
./scripts/test_docker_deployment.sh

# Check self-test logs
docker-compose logs | grep "self-test"
```

---

## 17_index_full_dataset_production
**Time**: 2-4 hours  
**Dependencies**: 15

**Deliverable**: All documents indexed in production

**Steps**:
1. Deploy Meilisearch to 192.168.2.5
2. Run full indexing
3. Verify document count
4. Test searches

**Acceptance Criteria**:
- [ ] All 361+ frameworks indexed
- [ ] Document count matches
- [ ] Search quality verified
- [ ] Performance acceptable

---

## 18_switch_production_traffic
**Time**: 1 hour  
**Dependencies**: 16

**Deliverable**: Production Claude using Meilisearch

**Steps**:
1. Update production config
2. Monitor for errors
3. Quick rollback ready
4. Validate functionality

**Acceptance Criteria**:
- [ ] Production switched successfully
- [ ] No increase in errors
- [ ] Users notice no degradation
- [ ] Rollback procedure tested

---

## 19_cleanup_old_files
**Time**: 1 hour  
**Dependencies**: 17 + 1 week stable

**Deliverable**: ChromaDB code removed

**Files to remove**:
- `mcp-server/server/rag.py`
- `mcp-server/server/rag_improvements.py`
- `mcp-server/scripts/build_index.py`
- Related tests

**Acceptance Criteria**:
- [ ] Old files removed
- [ ] Dependencies updated
- [ ] All tests still pass
- [ ] Git history preserved

---

## Quick Start Commands

```bash
# Start here - install and test locally
brew install meilisearch
meilisearch --master-key="test"

# Begin with metadata extraction
python scripts/metadata_extractor.py documentation/SwiftUI/View.md

# Test indexing with small batch
python scripts/index_to_meilisearch.py --limit 10

# Verify search works
curl -X POST http://localhost:7700/indexes/apple-docs/search \
  -H 'Authorization: Bearer test' \
  -d '{"q": "View"}'
```

## Daily Progress Tracking

After each task, verify:
1. Code committed with task number (e.g., "01_install_meilisearch_locally: Complete")
2. Tests passing
3. Next task's dependencies met
4. No blockers for tomorrow

Remember: **Everything runs locally first**. Docker is only for task 16+.

## Task Tracking

### Quick Reference
| Task | Dependencies | Estimated Hours | Priority |
|------|--------------|-----------------|----------|
| 01 Install Meilisearch | None | 0.5 | High |
| 02 Metadata Extractor | None | 2-3 | High |
| 03 Document Processor | 02 | 2 | High |
| 04 Indexing Script | 02, 03 | 3-4 | High |
| 05 Configure Index | 04 | 1 | High |
| 06 Benchmark ChromaDB | None | 2 | High |
| 07 Test Search Quality | 05, 06 | 2 | High |
| 08 Install MCP Package | None | 1 | High |
| 09 Stdio Wrapper | 08 | 4-5 | High |
| 10 API Adapter | 09 | 6-8 | High |
| 11 MCP Integration | 10 | 4-5 | High |
| 12 Full Local Test | 11 | 2 | High |
| 13 Performance Compare | 12 | 2 | Medium |
| 14 Claude Desktop | 12 | 1 | High |
| 15 User Validation | 14 | 1 week | High |
| 16 Docker Deploy | 15 | 3-4 | High |
| 17 Production Index | 16 | 2-4 | High |
| 18 Switch Traffic | 17 | 1 | High |
| 19 Cleanup | 18 + 1 week | 1 | Low |

**Total Estimated Time**: 60-85 hours (increased due to additional features)

### Key Changes from Original Plan
- Added task 06 for ChromaDB baseline benchmarking
- Enhanced task 09 with session management and auth
- Enhanced task 10 with query preprocessing and relevance scoring
- Enhanced task 11 with resources, prompts, and FastMCP
- Enhanced task 16 with self-test integration
- All features from current implementation preserved