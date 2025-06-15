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

# Check if vectorstore exists - look for chroma.sqlite3
if [ -f "/data/vectorstore/chroma.sqlite3" ]; then
    echo "✅ Found existing vectorstore database"
    
    # Show what's in the vectorstore directory
    echo "📁 Vectorstore contents:"
    ls -lah /data/vectorstore/ | head -5
    
    # Get document count if possible
    if command -v python > /dev/null; then
        DOC_COUNT=$(python -c "
import chromadb
try:
    client = chromadb.PersistentClient(path='/data/vectorstore')
    collection = client.get_collection('apple_docs')
    print(collection.count())
except:
    print('0')
" 2>/dev/null || echo "0")
        
        if [ "$DOC_COUNT" -gt 0 ]; then
            echo "📊 Documents in vectorstore: $(printf "%'d" $DOC_COUNT)"
        else
            echo "⚠️  Vectorstore exists but is empty"
        fi
    fi
else
    echo "⚠️  No vectorstore found. It will be built on first scrape."
    echo "   This process will take 4-6 hours and cost ~$4-6 in OpenAI API fees."
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
    echo "📝 Initial container setup completed."
    touch /data/hashes/.initialized
    
    # Record initial setup time if not already present
    if [ ! -f "/data/hashes/last_update.txt" ]; then
        date '+%Y-%m-%d %H:%M:%S' > /data/hashes/last_update.txt
    fi
fi

echo "🎯 Starting services with supervisor..."
echo ""

# Check if we should run self-tests (on first container deployment)
if [ ! -f "/data/hashes/.self_test_completed" ]; then
    echo "🧪 Self-tests will run after services start."
    echo "   Check /data/logs/self-test.log for results."
    echo ""
    # Create the marker file so we don't show this message repeatedly
    touch /data/hashes/.self_test_completed
fi

# Start supervisor (runs both MCP server and scheduler)
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf