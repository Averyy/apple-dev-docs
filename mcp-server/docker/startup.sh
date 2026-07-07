#!/bin/bash
set -e

echo "🚀 Starting Apple Docs MCP Server V2 Container with Meilisearch"
echo "============================================================="

# Check required environment variables
if [ -z "$MEILI_MASTER_KEY" ]; then
    echo "❌ Error: MEILI_MASTER_KEY environment variable is required"
    echo "   Generate one with: openssl rand -hex 32"
    exit 1
fi

# Check optional API key (for rate limit bypass)
if [ -z "$MCP_API_KEY" ]; then
    echo "ℹ️  Note: MCP_API_KEY not set - all requests subject to rate limiting (30/min)"
    echo "   Set MCP_API_KEY to enable authenticated access that bypasses rate limits"
fi

# Create necessary directories (documentation comes from image)
mkdir -p /data/meilisearch /data/logs

# Ensure proper permissions for Meilisearch directory
chmod 755 /data/meilisearch
chown root:root /data/meilisearch

# Test if Meilisearch binary works
echo "🔍 Testing Meilisearch binary..."
if ! /usr/bin/meilisearch --help > /dev/null 2>&1; then
    echo "❌ Meilisearch binary is not working properly"
    exit 1
fi
echo "✅ Meilisearch binary is functional"

# Documentation and hashes now come directly from the image (no volumes)

# Check if pre-indexed data exists
if [ -f "/data/.indexed" ]; then
    echo "✅ Using pre-indexed documentation"
    DOC_COUNT=$(find /data/documentation -name "*.md" | wc -l)
    echo "📊 Found $DOC_COUNT pre-scraped documents"
    echo "🚀 Server will be ready in seconds!"
elif [ -d "/data/meilisearch/data.ms" ]; then
    echo "✅ Found existing Meilisearch database"
    echo "📁 Meilisearch data directory found"
    echo "   Document count will be verified after Meilisearch starts"
else
    echo "📋 No Meilisearch database found yet"
    DOC_COUNT=$(find /data/documentation -name "*.md" 2>/dev/null | wc -l)
    if [ "$DOC_COUNT" -gt 0 ]; then
        echo "📚 Found $DOC_COUNT pre-scraped documents ready for indexing"
        echo "🔨 Automatic indexing will begin after Meilisearch starts (~4 minutes)"
    else
        echo "⚠️  No documentation found! Please check volume mounts."
    fi
fi

# Check last update time (stored in logs volume to avoid Meilisearch issues)
if [ -f "/data/logs/last_update.txt" ]; then
    echo "📅 Last update: $(cat /data/logs/last_update.txt)"
else
    echo "📅 No previous updates recorded"
fi

# Set up environment
export MEILISEARCH_PATH=/data/meilisearch
export DOCUMENTATION_PATH=/data/documentation
export LOG_PATH=/data/logs
export MEILI_DB_PATH=/data/meilisearch
export MEILI_HTTP_ADDR=${MEILI_HTTP_ADDR:-http://localhost:7700}

echo ""
echo "🔧 Configuration:"
echo "  - MCP Type: Native HTTP (Streamable HTTP transport)"
echo "  - HTTP Port: ${HTTP_PORT:-8000}"
echo "  - MCP Endpoint: http://<server-ip>:${HTTP_PORT:-8000}/mcp"
echo "  - Meilisearch URL: ${MEILI_HTTP_ADDR:-http://localhost:7700}"
if [ -n "$MCP_API_KEY" ]; then
    echo "  - Rate Limiting: Enabled (API key bypasses limits)"
else
    echo "  - Rate Limiting: Enabled (30 req/min per IP)"
fi
echo ""

# Create a marker file for first run (store in logs volume to avoid Meilisearch issues)
if [ ! -f "/data/logs/.initialized" ]; then
    echo "📝 Initial container setup completed."
    touch /data/logs/.initialized
    
    # Record initial setup time if not already present
    if [ ! -f "/data/logs/last_update.txt" ]; then
        date '+%Y-%m-%d %H:%M:%S' > /data/logs/last_update.txt
    fi
fi

echo "🎯 Starting services with supervisor..."
echo ""

# Create a post-startup script to check Meilisearch
cat > /app/check_meilisearch.sh << 'EOF'
#!/bin/bash
sleep 10  # Give Meilisearch time to start

if curl -s http://localhost:7700/health > /dev/null 2>&1; then
    echo "✅ Meilisearch is healthy"
    
    # Check document count
    DOC_COUNT=$(curl -s -H "Authorization: Bearer $MEILI_MASTER_KEY" \
        http://localhost:7700/indexes/apple-docs/stats 2>/dev/null | \
        python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('numberOfDocuments', 0))" 2>/dev/null || echo "0")
    
    if [ "$DOC_COUNT" -gt 290000 ]; then
        echo "📊 Documents indexed: $(printf "%'d" $DOC_COUNT) ✅"
    elif [ "$DOC_COUNT" -gt 0 ]; then
        echo "⚠️  Only $DOC_COUNT documents indexed (expected >290,000)"
        echo "   Run indexing script: cd /app/scripts && python3 index_to_meilisearch.py"
    else
        echo "📋 No documents indexed yet"
        echo "   Run indexing script: cd /app/scripts && python3 index_to_meilisearch.py"
    fi
else
    echo "⚠️  Meilisearch not responding yet"
fi
EOF
chmod +x /app/check_meilisearch.sh

# Run check in background after startup
(sleep 15 && /app/check_meilisearch.sh) &

# Start supervisor (runs both MCP server and scheduler)
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf