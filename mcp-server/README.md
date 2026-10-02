# MCP Server Implementation

This directory contains the MCP server implementation for Apple Developer Documentation search.

**Current Version:** 3.0.1 (`SERVER_VERSION` in `apple_docs_mcp.py`; CI derives the image version label from it)

## Architecture

```
mcp-server/
├── apple_docs_mcp.py         # Main MCP server (HTTP via Streamable HTTP)
├── scripts/                  # startup_check.py (index on start), docker_index_helper.sh
├── docker/                   # startup.sh, supervisord.conf
├── tests/                    # Test suite
├── Dockerfile                # All-in-one image (Meilisearch + MCP server)
├── docker-compose.yml        # Production compose
├── docker-compose.local.yml  # Local build for testing
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

### v3.0.1
- Questions ending in `?` are searched as text; `?` is a wildcard only in single-word queries
- Token-budget pagination no longer skips or repeats results; results are numbered by overall rank
- `token_budget` also limits the first result (truncated with a pointer to `expand_result`)
- Honest totals ("ranked from the top N matches") and a clear message for an offset past the end
- `expand_result` treats any input without `/` or `.md` as a symbol (e.g. `withAnimation`)
- Symbol lookup prefers an exact-case title, then that name's function page (`Button` → SwiftUI `Button`, `withAnimation` → `withAnimation(_:_:)`)
- `serverInfo.version` reports the server version

### v3.0.0
- Removed `choose_framework`/`current_framework` (their state was shared by all clients)
- Wildcard matching can no longer freeze the server; input lengths are capped
- `expand_result` accepts full-length paths; errors are returned as MCP errors
- Text-only results (no duplicate structured content); periodic restarts removed

### v2.x
- Not recorded here; see the git history of `apple_docs_mcp.py`

### v1.1.0
- Added wildcard search support (`*View`, `UI*`, `Button?`)
- Added `get_version` tool for status information
- Enhanced `expand_result` to accept symbol names
- Improved error messages with contextual suggestions
- Added query filtering to `list_frameworks`

### v1.0.0
- Initial release with `search_apple_docs`, `expand_result`, `list_frameworks`
