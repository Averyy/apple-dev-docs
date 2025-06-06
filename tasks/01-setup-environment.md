# Task 1: Environment Setup

## Objective
Set up the development environment for the Apple Docs MCP server with minimal dependencies.

## Prerequisites
- Python 3.11+
- TEI server running locally (BGE-M3 at 192.168.2.5)
- 5GB+ free disk space (2GB vector database + 1.2GB docs + workspace)

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
requests              # For TEI server communication
python-dotenv         # Environment management
tqdm                  # Progress bars for indexing
httpx                 # Async HTTP client (for ETag collection)
```

### 3. Environment Configuration
Create `.env` file:
```
# Required
TEI_URL=http://192.168.2.5/embed  # TEI BGE-M3 server
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
import requests
import mcp

# Test TEI connection
response = requests.post("http://192.168.2.5/embed", 
                        json={"inputs": ["test"]})
print(f"✓ TEI server accessible: {response.status_code == 200}")
print("✓ All imports working!")
```

## Important Links
- [MCP SDK Documentation](https://modelcontextprotocol.io/docs)
- [ChromaDB Python Client](https://docs.trychroma.com/getting-started)
- [TEI API Documentation](http://192.168.2.5/docs) - Local Swagger UI for BGE-M3 server

## Success Criteria
- [ ] Virtual environment created and activated
- [ ] All dependencies installed without errors
- [ ] Environment variables configured
- [ ] Can import all required libraries
- [ ] Documentation directory accessible

## Time Estimate
15-20 minutes (much simpler now!)