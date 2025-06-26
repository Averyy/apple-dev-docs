#!/bin/bash
set -e

echo "🚀 Starting Apple Docs MCP Server V2 Container with Meilisearch"
echo "============================================================="

# Check required environment variables
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ Error: OPENAI_API_KEY environment variable is required"
    exit 1
fi

if [ -z "$MCP_API_KEY" ]; then
    echo "❌ Error: MCP_API_KEY environment variable is required"
    exit 1
fi

if [ -z "$MEILI_MASTER_KEY" ]; then
    echo "❌ Error: MEILI_MASTER_KEY environment variable is required"
    exit 1
fi

# Create necessary directories
mkdir -p /data/meilisearch /data/hashes /data/documentation /data/logs

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
    echo "⚠️  No Meilisearch data found. This shouldn't happen!"
    echo "   The Docker image should include pre-indexed data."
fi

# Check last update time
if [ -f "/data/hashes/last_update.txt" ]; then
    echo "📅 Last update: $(cat /data/hashes/last_update.txt)"
else
    echo "📅 No previous updates recorded"
fi

# Set up environment
export MEILISEARCH_PATH=/data/meilisearch
export HASHES_PATH=/data/hashes
export DOCUMENTATION_PATH=/data/documentation
export LOG_PATH=/data/logs
export MEILI_DB_PATH=/data/meilisearch
export MEILI_HTTP_ADDR=${MEILI_HTTP_ADDR:-http://localhost:7700}

echo ""
echo "🔧 Configuration:"
echo "  - MCP Type: STDIO with optional HTTP wrapper"
echo "  - HTTP Wrapper: ${ENABLE_HTTP_WRAPPER:-false}"
if [ "${ENABLE_HTTP_WRAPPER}" = "true" ]; then
    echo "  - HTTP Port: ${HTTP_PORT:-8080}"
    echo "  - Remote Access: Enabled at http://<server-ip>:${HTTP_PORT:-8080}/mcp"
fi
echo "  - Meilisearch URL: ${MEILI_HTTP_ADDR:-http://localhost:7700}"
echo "  - Keep Markdown Files: ${KEEP_MARKDOWN_FILES:-true}"
echo "  - Auto-Rescrape Enabled: ${ENABLE_AUTO_RESCRAPE:-false}"
if [ "${ENABLE_AUTO_RESCRAPE}" = "true" ]; then
    echo "  - Rescrape Schedule: Weekly on Sundays at 1:00 AM"
fi
echo ""

# Create a marker file for first run
if [ ! -f "/data/hashes/.initialized" ]; then
    echo "📝 Initial container setup completed."
    touch /data/hashes/.initialized
    
    # Record initial setup time if not already present
    if [ ! -f "/data/hashes/last_update.txt" ]; then
        date '+%Y-%m-%d %H:%M:%S' > /data/hashes/last_update.txt
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
        http://localhost:7700/indexes/apple_docs/stats 2>/dev/null | \
        python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('numberOfDocuments', 0))" 2>/dev/null || echo "0")
    
    if [ "$DOC_COUNT" -gt 300000 ]; then
        echo "📊 Documents indexed: $(printf "%'d" $DOC_COUNT) ✅"
    elif [ "$DOC_COUNT" -gt 0 ]; then
        echo "⚠️  Only $DOC_COUNT documents indexed (expected >300,000)"
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