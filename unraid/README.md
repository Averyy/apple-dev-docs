# Apple Docs MCP Server - Unraid Template

This template allows you to run the Apple Developer Documentation MCP Server on your Unraid server.

## Features

- 🔍 **Search 323,096 Apple documentation pages** with AI-powered semantic search
- 🚀 **Sub-500ms response times** with ChromaDB vector database
- 🤖 **MCP Integration** for AI assistants like Claude
- 📱 **Platform filtering** for iOS, macOS, tvOS, watchOS, visionOS
- 🔄 **Automatic weekly updates** (Sundays at 1 AM)
- 🔐 **Bearer token authentication** for secure access

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
   https://github.com/Averyy/apple-dev-docs/tree/main/unraid
   ```
3. Click Save
4. The template will appear in "Add Container" dropdown

## Configuration

### Required Settings

1. **OpenAI API Key**: 
   - Get from https://platform.openai.com/api-keys
   - Only used for text-embedding-3-small model
   - Cost: ~$4 initial, <$0.10 per update

2. **MCP API Key**:
   - Generate with: `openssl rand -hex 32`
   - Used for API authentication
   - Save this for client configuration!

### Optional Settings

- **Keep Markdown Files**: 
  - `true`: Keeps documentation files (~2GB)
  - `false`: Saves disk space (recommended)

- **Timezone**: Set for weekly update schedule

### Storage Paths

Default paths (can be changed):
- `/mnt/cache/appdata/apple-docs-mcp/vectorstore` - Vector database
- `/mnt/cache/appdata/apple-docs-mcp/hashes` - Update tracking
- `/mnt/cache/appdata/apple-docs-mcp/documentation` - Markdown files
- `/mnt/cache/appdata/apple-docs-mcp/logs` - Container logs

## First Run

On first start, the container will:
1. Check for existing data
2. If no data found, offer to build the index (~4-6 hours)
3. Run self-tests to verify setup
4. Start the MCP server on port 8080

### Pre-built Data (Optional)

To skip the initial 4-6 hour build:

1. Copy your existing data to Unraid:
   ```bash
   # From your local machine
   scp -r mcp-server/vectorstore/ root@unraid:/mnt/cache/appdata/apple-docs-mcp/
   scp -r .hashes/ root@unraid:/mnt/cache/appdata/apple-docs-mcp/
   ```

2. Start the container - it will detect and use existing data

## Client Configuration

### Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "apple-docs": {
      "type": "sse",
      "url": "http://YOUR_UNRAID_IP:8080/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_MCP_API_KEY"
      }
    }
  }
}
```

### Testing

```bash
# Health check
curl http://YOUR_UNRAID_IP:8080/health

# Test search (requires auth)
curl -H "Authorization: Bearer YOUR_MCP_API_KEY" \
  http://YOUR_UNRAID_IP:8080/health
```

## Monitoring

### View Logs
```bash
# In Unraid terminal
docker logs apple-docs-mcp

# Or view specific logs
docker exec apple-docs-mcp tail -f /data/logs/mcp-server.log
```

### Check Status
```bash
docker exec apple-docs-mcp supervisorctl status
```

## Troubleshooting

### Container won't start
- Check logs: Click container icon → Logs
- Verify API keys are set correctly
- Ensure port 8080 is not in use

### No search results
- Wait for initial index build (4-6 hours)
- Check vectorstore path has data
- Verify OpenAI API key is valid

### High CPU/Memory usage
- Normal during initial indexing
- After indexing: ~200MB RAM, minimal CPU

## Updates

The container automatically updates documentation weekly. To force an update:

```bash
docker exec apple-docs-mcp python /app/scraper/auto_scrape_and_embed.py --embed --yes
```

## Support

- GitHub Issues: https://github.com/Averyy/apple-dev-docs/issues
- Unraid Forum Thread: [Link to your thread]

## Resource Requirements

- **CPU**: 1-2 cores (4+ during indexing)
- **RAM**: 2GB minimum (4GB recommended)
- **Disk**: 3-5GB for full installation
- **Network**: Required for API access and updates