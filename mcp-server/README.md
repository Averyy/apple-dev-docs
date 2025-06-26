# MCP Server Implementation

This directory contains the MCP server implementation for Apple Developer Documentation search.

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

## Documentation

For complete documentation, see:
- [MCP Complete Guide](../docs/MCP_COMPLETE_GUIDE.md)
- [Docker Deployment](../docs/DOCKER_DEPLOYMENT_V2.md)
- [Technical Operations](../docs/TECHNICAL_OPERATIONS_GUIDE.md)