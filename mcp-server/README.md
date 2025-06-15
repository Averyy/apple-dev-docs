# Apple Docs MCP Server

A high-performance Model Context Protocol (MCP) server providing semantic search over 341,207 Apple Developer Documentation pages with full MCP specification compliance.

## Features

- **Streamable HTTP Transport**: Full MCP 2025-03-26 specification compliance
- **341,207 Documents**: Complete Apple developer documentation coverage
- **360 Frameworks**: All Apple frameworks indexed with metadata
- **Sub-500ms Search**: Optimized ChromaDB vector search
- **Platform Filtering**: iOS, macOS, tvOS, watchOS, visionOS, Catalyst
- **MCP Resources**: Browse documentation structure
- **MCP Prompts**: Pre-built templates for common queries
- **Session Management**: Stateful connections with proper handshake

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

1. **Setup Environment**
   ```bash
   cd mcp-server
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure API Keys**
   ```bash
   cp ../.env.example ../.env
   # Edit ../.env and add:
   # OPENAI_API_KEY=your-openai-key
   # MCP_API_KEY=your-generated-key
   ```

3. **Build Vector Index** (if not already built)
   ```bash
   python scripts/build_index.py --force
   ```

4. **Start Server**
   ```bash
   make server
   # Or directly:
   python server/mcp_server.py
   ```

   Server runs at `http://localhost:8080/mcp` with:
   - Streamable HTTP transport
   - Bearer token authentication
   - Full MCP protocol support

## Testing

```bash
# Run comprehensive test suite
python tests/test_streamable_http.py

# Or legacy tests
make test
```

Tests verify:
- Initialize/initialized handshake
- Session management
- Tools (search_apple_docs, list_frameworks)
- Resources (list, read)
- Prompts (list, get)
- Batch requests
- SSE streaming

## MCP Protocol Usage

### 1. Initialize Connection
```bash
curl -X POST http://localhost:8080/mcp \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": "init-1",
    "method": "initialize",
    "params": {
      "protocolVersion": "1.0.0",
      "clientInfo": {
        "name": "my-client",
        "version": "1.0.0"
      }
    }
  }'
```

### 2. Search Documentation
```bash
curl -X POST http://localhost:8080/mcp \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": "search-1",
    "method": "tools/call",
    "params": {
      "name": "search_apple_docs",
      "arguments": {
        "query": "SwiftUI Button",
        "platform": "ios",
        "limit": 5
      }
    }
  }'
```

### 3. Browse Resources
```bash
# List available documentation
curl -X POST http://localhost:8080/mcp \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"jsonrpc": "2.0", "id": 1, "method": "resources/list"}'

# Read specific documentation
curl -X POST http://localhost:8080/mcp \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "resources/read",
    "params": {"uri": "docs://SwiftUI/Button"}
  }'
```

### 4. Use Prompts
```bash
curl -X POST http://localhost:8080/mcp \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "prompts/get",
    "params": {
      "name": "migration_guide",
      "arguments": {
        "from_framework": "UIKit",
        "to_framework": "SwiftUI",
        "component": "Button"
      }
    }
  }'
```

## Client Integration

### Claude CLI (Recommended)
```bash
# Add the MCP server to Claude
claude mcp add --transport sse apple-docs http://localhost:8080/mcp \
  -e AUTHORIZATION="Bearer YOUR_MCP_API_KEY"

# For remote server
claude mcp add --transport sse apple-docs http://YOUR_SERVER_IP:8080/mcp \
  -e AUTHORIZATION="Bearer YOUR_MCP_API_KEY"
```

This adds the following to your Claude configuration:
```json
{
  "mcpServers": {
    "apple-docs": {
      "type": "sse",
      "url": "http://YOUR_SERVER_IP:8080/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_MCP_API_KEY"
      }
    }
  }
}
```

### Direct HTTP API
Any HTTP client can connect:
- Endpoint: `http://localhost:8080/mcp`
- Authentication: `Authorization: Bearer YOUR_MCP_API_KEY`
- Protocol: JSON-RPC 2.0 over HTTP POST
- Transport: Streamable HTTP with SSE support

## Configuration

Key environment variables:
- `OPENAI_API_KEY`: Required for embeddings
- `MCP_API_KEY`: Bearer token for API authentication
- `VECTORSTORE_PATH`: ChromaDB location (default: `./vectorstore`)
- `MCP_PORT`: Server port (default: 8080)
