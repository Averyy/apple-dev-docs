# MCP Server Implementation

This directory contains the MCP server implementation for Apple Developer Documentation search.

**Current Version:** 1.1.0

## Architecture

```
mcp-server/
├── apple_docs_stdio_mcp.py      # Main STDIO MCP server
├── apple_docs_stdio_http_bridge.py  # STDIO-to-HTTP bridge for remote access
├── http_stdio_wrapper.py        # HTTP wrapper for Docker deployment
├── meilisearch_adapter.py       # Meilisearch integration
├── config.py                    # Configuration
├── logger.py                    # Logging setup
├── scripts/                     # Utility scripts
├── tests/                       # Test suite
├── docker/                      # Docker configs
└── requirements.txt             # Python dependencies
```

## Key Components

- **STDIO Server**: Direct MCP protocol implementation for local use
- **HTTP Wrapper**: Enables remote access when deployed with Docker
- **STDIO Bridge**: Client-side tool for connecting to remote servers

## Available Tools

| Tool | Description |
|------|-------------|
| `search_apple_docs` | Search documentation with wildcard support (`*`, `?`) |
| `expand_result` | Get full content for a symbol name or file path |
| `list_frameworks` | Browse frameworks with optional filtering |
| `choose_framework` | Set active framework to scope searches |
| `current_framework` | Show current framework selection |
| `get_version` | Get server version and status |

## Changelog

### v1.1.0
- Added stateful framework selection (`choose_framework`, `current_framework`)
- Added wildcard search support (`*View`, `UI*`, `Button?`)
- Added `get_version` tool for status information
- Enhanced `expand_result` to accept symbol names (e.g., "Button") not just file paths
- Improved error messages with contextual suggestions
- Added query filtering to `list_frameworks`
- Fixed regex escaping in wildcard patterns

### v1.0.0
- Initial release with `search_apple_docs`, `expand_result`, `list_frameworks`

## Documentation

For complete documentation, see:
- [MCP Complete Guide](../docs/MCP_COMPLETE_GUIDE.md)
- [Docker Deployment](../docs/DOCKER_DEPLOYMENT_V2.md)
- [Technical Operations](../docs/TECHNICAL_OPERATIONS_GUIDE.md)