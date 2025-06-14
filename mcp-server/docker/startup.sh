#!/bin/bash
set -e

echo "🚀 Starting Apple Docs MCP Server Container"
echo "==========================================="

# Check required environment variables
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ Error: OPENAI_API_KEY environment variable is required"
    exit 1
fi

if [ -z "$MCP_API_KEY" ]; then
    echo "❌ Error: MCP_API_KEY environment variable is required"
    exit 1
fi

# Create necessary directories
mkdir -p /data/vectorstore /data/hashes /data/documentation /data/logs

# Check if vectorstore exists
if [ -d "/data/vectorstore/chroma" ]; then
    echo "✅ Found existing vectorstore"
    
    # Get document count if possible
    if command -v python > /dev/null; then
        DOC_COUNT=$(python -c "
import chromadb
try:
    client = chromadb.PersistentClient(path='/data/vectorstore')
    collection = client.get_collection('apple_docs')
    print(collection.count())
except:
    print('unknown')
" 2>/dev/null || echo "unknown")
        echo "📊 Documents in vectorstore: $DOC_COUNT"
    fi
else
    echo "⚠️  No vectorstore found. It will be built on first scrape."
    echo "   This process will take 1-2 hours and cost ~$4-6 in OpenAI API fees."
fi

# Check last update time
if [ -f "/data/hashes/last_update.txt" ]; then
    echo "📅 Last update: $(cat /data/hashes/last_update.txt)"
else
    echo "📅 No previous updates recorded"
fi

# Set up environment
export VECTORSTORE_PATH=/data/vectorstore
export HASHES_PATH=/data/hashes
export DOCUMENTATION_PATH=/data/documentation
export LOG_PATH=/data/logs

echo ""
echo "🔧 Configuration:"
echo "  - MCP Port: ${MCP_PORT:-8080}"
echo "  - Keep Markdown Files: ${KEEP_MARKDOWN_FILES:-true}"
echo "  - Rescrape Schedule: Weekly on Sundays at 1:00 AM"
echo ""

# Create a marker file for first run
if [ ! -f "/data/hashes/.initialized" ]; then
    echo "📝 First run detected. Marking as initialized."
    touch /data/hashes/.initialized
    
    # Record initial setup time
    date '+%Y-%m-%d %H:%M:%S' > /data/hashes/last_update.txt
fi

echo "🎯 Starting services with supervisor..."
echo ""

# Check if we should run self-tests (on first startup)
if [ ! -f "/data/hashes/.self_test_completed" ]; then
    echo "🧪 First startup detected. Self-tests will run after services start."
    echo "   Check /data/logs/self-test.log for results."
    echo ""
fi

# Start supervisor (runs both MCP server and scheduler)
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf