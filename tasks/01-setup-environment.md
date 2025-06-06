# Task 1: Environment Setup

## Objective
Set up the development environment for the Apple Docs MCP server with minimal dependencies.

## Prerequisites
- Python 3.11+
- OpenAI API key (for embeddings only)
- 10GB+ free disk space for vector database

## Steps

### 1. Create Project Structure
```
mcp-apple-docs/
├── server/
│   ├── mcp_server.py
│   ├── rag.py
│   └── config.py
├── vectorstore/
├── scripts/
│   └── build_index.py
└── requirements.txt
```

### 2. Install Core Dependencies
Create requirements.txt with:
```
# Core dependencies only
mcp                    # Model Context Protocol SDK
fastmcp               # High-level MCP server framework (STDIO)
fastapi               # HTTP server framework (remote access)
uvicorn[standard]     # ASGI server for FastAPI
chromadb>=0.4.0       # Vector database
openai>=1.0.0         # For embeddings only
python-dotenv         # Environment management
tqdm                  # Progress bars for indexing
httpx                 # Async HTTP client (for ETag collection)
```

### 3. Environment Configuration
Create `.env` file:
```
# Required
OPENAI_API_KEY=your-key-here
MCP_API_KEY=generate-with-openssl-rand-hex-32

# Optional (with defaults)
VECTORSTORE_PATH=./vectorstore
DOCS_PATH=../documentation
KEEP_MARKDOWN_FILES=true  # defaults to true
MCP_PORT=8080            # defaults to 8080
```

Generate MCP API key:
```bash
openssl rand -hex 32
```

### 4. Verify Apple Docs Structure
Ensure scraped documentation follows expected structure:
```
documentation/
├── SwiftUI/
├── UIKit/
├── Foundation/
└── ... (other frameworks)
```

### 5. Test Basic Imports
```python
# Quick test script
import chromadb
from openai import OpenAI
import mcp

print("✓ All imports working!")
```

## Important Links
- [MCP SDK Documentation](https://modelcontextprotocol.io/docs)
- [ChromaDB Python Client](https://docs.trychroma.com/getting-started)
- [OpenAI Python Library](https://github.com/openai/openai-python)

## Success Criteria
- [ ] Virtual environment created and activated
- [ ] All dependencies installed without errors
- [ ] Environment variables configured
- [ ] Can import all required libraries
- [ ] Documentation directory accessible

## Time Estimate
15-20 minutes (much simpler now!)