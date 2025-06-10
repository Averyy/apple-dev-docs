# Apple Docs MCP Server

This is the Model Context Protocol (MCP) server for Apple Developer Documentation. It provides semantic search capabilities over the scraped Apple documentation.

## Project Structure

```
mcp-server/                    # All MCP-related code lives here
├── server/                    # Core MCP server implementation
│   ├── config.py             # Configuration settings
│   ├── rag.py                # Task 03: RAG engine (retrieval)
│   └── mcp_server.py         # Task 04: MCP server (HTTP API)
├── scripts/                   # Utility scripts
│   └── build_index.py        # Task 02: Build vector index
├── vectorstore/              # ChromaDB storage (created by scripts)
├── tests/                    # Test suite
│   └── test_chromadb.py      # Vector database tests
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

2. **Build Vector Index** (Task 02) ✅
   ```bash
   python scripts/build_index.py
   # Or use make commands:
   make index        # Build/update index
   make monitor      # Monitor progress (separate terminal)
   ```
   See [Indexing Guide](docs/INDEXING_GUIDE.md) for detailed instructions.

3. **Run MCP Server** (Task 04)
   ```bash
   python server/mcp_server.py
   ```

## Testing

Run tests before moving between tasks:
```bash
make test  # Run all tests
# Or individually:
python tests/test_chromadb.py
python tests/test_build_index.py
```