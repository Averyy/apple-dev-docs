# Meilisearch Deployment Checklist

## Pre-Deployment Requirements

### Infrastructure
- [ ] Docker installed on deployment server (192.168.2.5)
- [ ] Sufficient disk space for Meilisearch data (estimate: 2-5GB)
- [ ] Network connectivity between Claude Code machine and server
- [ ] Firewall rules allow port 7700 (Meilisearch)

### Dependencies
- [ ] Python 3.9+ on both machines
- [ ] meilisearch-mcp package available
- [ ] Required Python packages: aiohttp, meilisearch-python-async

## Phase 1: Meilisearch Setup

### 1.1 Create Docker Compose
```yaml
# docker-compose.yml
version: '3.8'
services:
  meilisearch:
    image: getmeili/meilisearch:v1.6
    container_name: apple-docs-meilisearch
    ports:
      - "7700:7700"
    environment:
      - MEILI_MASTER_KEY=${MEILI_MASTER_KEY}
      - MEILI_ENV=production
      - MEILI_DB_PATH=/meili_data
      - MEILI_HTTP_PAYLOAD_SIZE_LIMIT=200Mb
      - MEILI_MAX_INDEXING_MEMORY=2Gb
      - MEILI_MAX_INDEXING_THREADS=4
    volumes:
      - ./meilisearch-data:/meili_data
      - ./dumps:/dumps
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:7700/health"]
      interval: 10s
      timeout: 5s
      retries: 5
```

### 1.2 Environment Configuration
```bash
# .env
MEILI_MASTER_KEY=your-secure-master-key-min-16-chars
MEILISEARCH_URL=http://192.168.2.5:7700
MEILISEARCH_API_KEY=${MEILI_MASTER_KEY}
```

### 1.3 Deployment Commands
```bash
# On deployment server (192.168.2.5)
cd /path/to/deployment
docker-compose up -d

# Verify health
curl http://localhost:7700/health

# Check logs
docker-compose logs -f meilisearch
```

### 1.4 Gitignore Setup
```gitignore
# Meilisearch data
meilisearch-data/
*.ms.snapshot
*.ms.update
dumps/
```

## Phase 2: Initial Data Load

### 2.1 Index Creation Script
```python
# scripts/create_index.py
import asyncio
from meilisearch_python_async import Client

async def create_index():
    client = Client(
        'http://192.168.2.5:7700',
        api_key=os.getenv('MEILISEARCH_API_KEY')
    )
    
    # Create index
    index = client.index('apple-docs')
    await index.create(primary_key='id')
    
    # Configure settings (from indexing strategy)
    await configure_index(index)
    
    print("Index created successfully")

if __name__ == "__main__":
    asyncio.run(create_index())
```

### 2.2 Run Indexing
```bash
# From project root
python mcp-server/scripts/meilisearch_index.py --all

# Monitor progress
tail -f indexing.log
```

### 2.3 Verify Indexing
```bash
# Check document count
curl -H "Authorization: Bearer $MEILISEARCH_API_KEY" \
  http://192.168.2.5:7700/indexes/apple-docs/stats

# Test search
curl -X POST http://192.168.2.5:7700/indexes/apple-docs/search \
  -H "Authorization: Bearer $MEILISEARCH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "URLSession"}'
```

## Phase 3: Stdio Wrapper Deployment

### 3.1 Install Dependencies
```bash
# On Claude Code machine
pip install meilisearch-mcp aiohttp

# Verify installation
python -c "import meilisearch_mcp; print('OK')"
```

### 3.2 Configure Wrapper
```bash
# Create wrapper directory
mkdir -p ~/mcp-servers/apple-docs

# Copy wrapper script
cp meilisearch_stdio_wrapper.py ~/mcp-servers/apple-docs/

# Set permissions
chmod +x ~/mcp-servers/apple-docs/meilisearch_stdio_wrapper.py
```

### 3.3 Test Wrapper Standalone
```bash
# Test health check
MEILISEARCH_URL=http://192.168.2.5:7700 \
MEILISEARCH_API_KEY=your-key \
python ~/mcp-servers/apple-docs/meilisearch_stdio_wrapper.py --test

# Test with meilisearch-mcp
echo '{"jsonrpc": "2.0", "method": "initialize", "params": {"protocolVersion": "1.0.0"}, "id": 1}' | \
MEILISEARCH_URL=http://192.168.2.5:7700 \
python ~/mcp-servers/apple-docs/meilisearch_stdio_wrapper.py
```

## Phase 4: Claude Desktop Integration

### 4.1 Update Configuration
```json
// ~/Library/Application Support/Claude/claude_desktop_config.json
{
  "mcpServers": {
    "apple-docs": {
      "command": "/usr/bin/python3",
      "args": [
        "/Users/username/mcp-servers/apple-docs/meilisearch_stdio_wrapper.py"
      ],
      "env": {
        "MEILISEARCH_URL": "http://192.168.2.5:7700",
        "MEILISEARCH_API_KEY": "your-secure-key",
        "PYTHONUNBUFFERED": "1",
        "MEILISEARCH_WRAPPER_LOG_LEVEL": "INFO"
      }
    }
  }
}
```

### 4.2 Restart Claude
```bash
# Quit Claude Desktop completely
# Restart Claude Desktop
# Check MCP server status in Claude
```

### 4.3 Test in Claude
Test queries in Claude:
- "Search SwiftUI View"
- "List all frameworks"
- "Search URLSession in Foundation"

## Phase 5: Adapter Integration

### 5.1 Deploy Adapter
```bash
# Copy adapter to MCP server
cp meilisearch_adapter.py mcp-server/server/

# Update MCP server to use adapter
cp mcp_server_meilisearch.py mcp-server/server/mcp_server.py

# Update imports
```

### 5.2 Test Adapter
```python
# test_adapter.py
import asyncio
from meilisearch_adapter import MeilisearchMCPAdapter

async def test():
    adapter = MeilisearchMCPAdapter(
        "http://192.168.2.5:7700",
        "your-api-key"
    )
    
    # Test search
    results = await adapter.search_apple_docs(
        "URLSession",
        framework="Foundation"
    )
    print(f"Found {len(results)} results")
    
    # Test framework list
    frameworks = await adapter.list_frameworks()
    print(f"Found {len(frameworks)} frameworks")

asyncio.run(test())
```

## Phase 6: Production Validation

### 6.1 Performance Tests
```bash
# Concurrent search test
python tests/load_test_meilisearch.py --concurrent 10 --queries 100

# Expected: <100ms p95 latency
```

### 6.2 Functionality Tests
- [ ] Search by API name returns exact match first
- [ ] Platform filtering works correctly
- [ ] Framework filtering works correctly
- [ ] Link transformation preserves MCP format
- [ ] Framework list includes all 361+ frameworks
- [ ] Full content retrieval works

### 6.3 Error Handling Tests
- [ ] Network disconnection handled gracefully
- [ ] Invalid queries return helpful errors
- [ ] Authentication failures are clear
- [ ] Timeout handling works

## Phase 7: Monitoring Setup

### 7.1 Logging
```bash
# Check wrapper logs
tail -f /tmp/meilisearch_wrapper.log

# Check Meilisearch logs
docker-compose logs -f meilisearch

# Check MCP server logs
tail -f ~/Library/Logs/Claude/mcp-server-apple-docs.log
```

### 7.2 Health Monitoring
```bash
# Create health check script
cat > check_health.sh << 'EOF'
#!/bin/bash
# Check Meilisearch
curl -f http://192.168.2.5:7700/health || echo "Meilisearch DOWN"

# Check index
curl -f -H "Authorization: Bearer $MEILISEARCH_API_KEY" \
  http://192.168.2.5:7700/indexes/apple-docs/stats || echo "Index ERROR"
EOF

chmod +x check_health.sh
```

### 7.3 Backup Strategy
```bash
# Create backup script
cat > backup_meilisearch.sh << 'EOF'
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
curl -X POST http://192.168.2.5:7700/dumps \
  -H "Authorization: Bearer $MEILISEARCH_API_KEY"
echo "Backup initiated: $DATE"
EOF

# Schedule daily backups
crontab -e
# Add: 0 2 * * * /path/to/backup_meilisearch.sh
```

## Rollback Plan

### If Issues Occur:
1. **Immediate**: Switch Claude config back to ChromaDB server
2. **Investigate**: Check logs for errors
3. **Fix Forward**: Apply fixes without full rollback if possible
4. **Full Rollback**: If needed, restore ChromaDB MCP server

### Rollback Commands:
```bash
# Stop Meilisearch
docker-compose down

# Restore Claude config
cp ~/claude_desktop_config.json.backup ~/Library/Application Support/Claude/claude_desktop_config.json

# Restart Claude
# Verify ChromaDB server works
```

## Success Criteria Validation

- [ ] All test queries return relevant results
- [ ] Search latency <100ms for 95% of queries
- [ ] No errors in logs after 1 hour of operation
- [ ] Memory usage stable
- [ ] CPU usage reasonable (<50% average)
- [ ] All 361+ frameworks accessible
- [ ] Platform filtering accurate
- [ ] Link transformation working

## Post-Deployment

### Week 1 Monitoring:
- Daily log reviews
- Performance metrics collection
- User feedback gathering
- Issue tracking

### Optimization Opportunities:
- Tune ranking rules based on usage
- Add more synonyms
- Adjust typo tolerance
- Optimize frequently searched queries

### Documentation Updates:
- Update README with new search behavior
- Document API changes
- Create troubleshooting guide
- Update development setup guide