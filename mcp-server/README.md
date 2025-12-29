# MCP Server Implementation

This directory contains the MCP server implementation for Apple Developer Documentation search.

**Current Version:** 1.1.0

## Architecture

```
mcp-server/
├── apple_docs_mcp.py         # Main MCP server (HTTP via Streamable HTTP)
├── config.py                 # Configuration
├── logger.py                 # Logging setup
├── shared_utilities.py       # Shared utilities
├── scripts/                  # Utility scripts
├── docker/                   # Docker configs
├── tests/                    # Test suite
└── requirements.txt          # Python dependencies
```

## Transport

The server uses **Streamable HTTP** transport only. For STDIO clients (like Claude Desktop), use `mcp-remote` as a bridge:

```bash
npx -y mcp-remote https://xdocs.dev/mcp
```

## Available Tools

| Tool | Description |
|------|-------------|
| `search_apple_docs` | Search documentation with wildcard support (`*`, `?`) |
| `expand_result` | Get full content for a symbol name or file path |
| `list_frameworks` | Browse frameworks with optional filtering |
| `choose_framework` | Set active framework (stateless - use `framework` param instead) |
| `current_framework` | Show current framework selection |
| `get_version` | Get server version and status |

## Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server (requires Meilisearch)
python apple_docs_mcp.py --port 8000
```

## Docker Deployment

```bash
docker-compose up -d
```

## Changelog

### v1.1.0
- Added wildcard search support (`*View`, `UI*`, `Button?`)
- Added `get_version` tool for status information
- Enhanced `expand_result` to accept symbol names
- Improved error messages with contextual suggestions
- Added query filtering to `list_frameworks`

### v1.0.0
- Initial release with `search_apple_docs`, `expand_result`, `list_frameworks`

