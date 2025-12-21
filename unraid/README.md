# Apple Docs MCP Server - Unraid Template

This template allows you to run the Apple Developer Documentation MCP Server V2 on your Unraid server.

## Features

- 🔍 **Search 340,740+ Apple documentation pages** with ultra-fast Meilisearch
- 🚀 **Sub-3ms response times** (95x faster than V1)
- 🤖 **MCP Integration** for AI assistants like Claude
- 📱 **360 frameworks** with platform filtering (iOS, macOS, tvOS, watchOS, visionOS)
- 🔄 **Optional automatic updates** (disabled by default)
- 🔐 **Bearer token authentication** for secure remote access

## Installation

### Method 1: Community Applications (After Published)

1. Search for "Apple Docs MCP" in Community Applications
2. Click Install
3. Configure the required settings (see below)
4. Click Apply

### Method 2: Manual Template Installation

1. In Unraid, go to Docker tab
2. Click "Add Container"
3. Switch to "Advanced View" (top right toggle)
4. Copy the contents of `apple-docs-mcp.xml` into the template
5. Configure settings and click Apply

### Method 3: Add Template Repository

1. In Unraid Docker tab, scroll to bottom
2. Add this repository URL to "Template repositories":
   ```
   https://github.com/averyy/apple-developer-docs/tree/main/unraid
   ```
3. Click Save
4. The template will appear in "Add Container" dropdown

## Configuration

### Required Settings

**MEILI_MASTER_KEY**: 
- Generate with: `openssl rand -hex 32`
- Required for Meilisearch to start
- Controls access to the search engine

### Recommended Settings

**MCP_API_KEY** (for remote access):
- Generate with: `openssl rand -hex 32`
- Used for HTTP API authentication
- Save this for Claude configuration!

### Optional Settings

- **ENABLE_AUTO_RESCRAPE**: 
  - `false` (default): Manual updates only
  - `true`: Weekly automatic updates
  
- **Timezone**: Set for update schedule (if enabled)

### Storage Paths

Default paths (can be changed):
- `/mnt/cache/appdata/apple-docs-mcp/meilisearch` - Search database
- `/mnt/cache/appdata/apple-docs-mcp/hashes` - Update tracking
- `/mnt/cache/appdata/apple-docs-mcp/documentation` - Pre-indexed docs
- `/mnt/cache/appdata/apple-docs-mcp/logs` - Container logs

## First Run

The container includes pre-scraped documentation and will automatically:
1. Start Meilisearch search engine
2. Check if indexing is needed
3. Auto-index if needed (~4 minutes)
4. Start the MCP server on port 8080

**No manual setup required!**

## Client Configuration

### For Claude Desktop/Code on Your Computer

1. Clone the repo to get the remote client:
   ```bash
   git clone https://github.com/averyy/apple-developer-docs.git
   cd apple-developer-docs
   pip install aiohttp  # Required dependency
   ```

2. Configure Claude to use the remote client:

   **Claude Desktop** (`~/Library/Application Support/Claude/claude_desktop_config.json`):
   ```json
   {
     "mcpServers": {
       "apple-docs": {
         "type": "stdio",
         "command": "python3",
         "args": [
           "/path/to/apple-developer-docs/apple_docs_remote_client.py",
           "--server-url",
           "http://YOUR_UNRAID_IP:8080/mcp",
           "--api-key",
           "your-mcp-api-key"
         ]
       }
     }
   }
   ```

   **Claude Code** (MCP settings):
   ```json
   {
     "mcpServers": {
       "apple-docs": {
         "type": "stdio",
         "command": "python3",
         "args": [
           "/path/to/apple-developer-docs/apple_docs_remote_client.py",
           "--server-url",
           "http://YOUR_UNRAID_IP:8080/mcp",
           "--api-key",
           "your-mcp-api-key"
         ]
       }
     }
   }
   ```

### Testing

```bash
# Health check (no auth required)
curl http://YOUR_UNRAID_IP:8080/health

# Test remote connection
python3 apple_docs_remote_client.py --server-url http://YOUR_UNRAID_IP:8080/mcp --api-key your-key --test

# Test with Claude
# In Claude: @apple-docs search_apple_docs("SwiftUI Button")
```

## Monitoring

### View Logs
```bash
# In Unraid terminal
docker logs apple-docs-mcp

# Or view specific logs
docker exec apple-docs-mcp tail -f /data/logs/meilisearch.log
```

### Check Status
```bash
docker exec apple-docs-mcp supervisorctl status
```

## Troubleshooting

### Container won't start
- Check logs: Click container icon → Logs
- Verify MEILI_MASTER_KEY is set
- Ensure port 8080 is not in use

### Claude can't connect
- Verify MCP_API_KEY matches in both Unraid and Claude config
- Check firewall allows port 8080
- Test with curl command above

### High CPU/Memory usage
- Normal during initial indexing (4 minutes)
- After indexing: ~200MB RAM, minimal CPU

## Updates

To manually update documentation:
```bash
docker exec apple-docs-mcp python /app/scripts/schedule_rescrape_v2.py --run-once
```

## Support

- GitHub Issues: https://github.com/averyy/apple-developer-docs/issues
- Unraid Forum Thread: [Coming soon]

## Resource Requirements

- **CPU**: 1-2 cores (4+ during indexing)
- **RAM**: 1.5GB minimum
- **Disk**: 1GB for database + logs
- **Network**: Required for remote access