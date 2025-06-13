# Apple Docs MCP Server

This is the Model Context Protocol (MCP) server for Apple Developer Documentation. It provides semantic search capabilities over the scraped Apple documentation with platform-aware filtering and framework discovery.

## Features

- **Semantic Search**: Query 323,000+ Apple documentation pages using natural language
- **Platform Filtering**: Filter results by platform (iOS, macOS, tvOS, etc.)
- **Framework Discovery**: List all available frameworks with summaries and platform availability
- **Sub-500ms Response Time**: Optimized for fast, accurate results
- **Enhanced Metadata**: Includes platform availability and framework summaries

## Project Structure

```
mcp-server/                    # All MCP-related code lives here
├── server/                    # Core MCP server implementation
│   ├── config.py             # Configuration settings
│   ├── rag.py                # RAG engine with platform filtering
│   ├── mcp_server.py         # MCP server (HTTP API)
│   └── logger.py             # Logging configuration
├── scripts/                   # Utility scripts
│   ├── build_index.py        # Build vector index with metadata extraction
│   └── delete_collection.py  # Utility to clean vectorstore
├── vectorstore/              # ChromaDB storage (created by scripts)
├── tests/                    # Test suite
│   ├── test_mcp_server.py    # Comprehensive MCP tests
│   └── test_list_frameworks.py # Framework listing tests
├── docs/                     # Documentation
│   ├── MCP_CLIENT_CONFIG.md  # MCP client setup guide
│   └── INDEXING_GUIDE.md     # Vectorstore building guide
└── requirements.txt          # Dependencies
```

## Task Breakdown

All tasks are implemented within this `mcp-server/` directory:

- **Task 02**: `scripts/build_index.py` - Builds the vector index from scraped docs
- **Task 03**: `server/rag.py` - Implements the retrieval engine
- **Task 04**: `server/mcp_server.py` - Creates the HTTP-based MCP server
- **Task 05**: Tests in `tests/` directory
- **Task 06**: Docker deployment (Dockerfile in this directory)

## Relationship to Main Project

The MCP server reads from the scraped documentation in `../documentation/` but operates independently. The scraper can continue running without any interference.

## Quick Start

1. **Environment Setup** (Task 01) ✅
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Build Vector Index** ✅
   ```bash
   python scripts/build_index.py --force  # Full rebuild with enhanced metadata
   # Or incremental update (will use existing metadata if available):
   python scripts/build_index.py
   ```
   
   **Note**: After the recent fixes, use `--force` to rebuild with:
   - Correct framework names (bug fix for parts[0] vs parts[-2])
   - Platform metadata extraction (ios, macos, tvos, etc.)
   - Framework summaries from overview sections
   - Enhanced metadata for platform-aware filtering

3. **Run MCP Server** ✅
   ```bash
   python server/mcp_server.py
   # Or use make:
   make server
   ```
   
   The server now provides:
   - `search_apple_docs`: Search with **required** platform filter (use "all" for cross-platform)
   - `list_frameworks`: Discover frameworks with summaries and platform availability

## Testing

Run comprehensive tests:
```bash
make test  # Run all tests
# Or individually:
python tests/test_mcp_server.py      # Test MCP endpoints
python tests/test_list_frameworks.py  # Test framework listing
```

## API Examples

### Search with Platform Filter (Required)
```bash
curl -X POST http://localhost:8080/mcp/tools/call \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "search_apple_docs",
    "arguments": {
      "query": "SwiftUI button tap handling",
      "platform": "ios",      # Required! Use "all" for cross-platform
      "limit": 5
    }
  }'
```

### List Available Frameworks
```bash
curl -X POST http://localhost:8080/mcp/tools/call \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "list_frameworks",
    "arguments": {}
  }'
```

## Configuration

Key environment variables:
- `OPENAI_API_KEY`: Required for embeddings
- `MCP_API_KEY`: Bearer token for API authentication
- `VECTORSTORE_PATH`: ChromaDB location (default: `./vectorstore`)
- `MCP_PORT`: Server port (default: 8080)