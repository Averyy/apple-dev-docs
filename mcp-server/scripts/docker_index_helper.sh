#!/bin/bash
# Helper script to run indexing inside the Docker container

echo "🚀 Apple Docs V2 Indexing Helper"
echo "================================"
echo ""

# Check if we're inside the container
if [ ! -f /.dockerenv ]; then
    echo "⚠️  This script should be run inside the Docker container"
    echo "   Use: docker exec -it apple-docs-mcp /app/scripts/docker_index_helper.sh"
    exit 1
fi

# Check if Meilisearch is running
if ! curl -s http://localhost:7700/health > /dev/null 2>&1; then
    echo "❌ Meilisearch is not running"
    echo "   Please ensure the container is fully started"
    exit 1
fi

echo "✅ Meilisearch is running"

# Check if already pre-indexed
if [ -f "/data/.indexed" ]; then
    echo ""
    echo "🎉 Documentation is already pre-indexed!"
    echo "   This Docker image includes pre-scraped Apple documentation."
    echo "   No indexing needed - you're ready to go!"
    echo ""
    exit 0
fi

# Check current document count
DOC_COUNT=$(curl -s -H "Authorization: Bearer $MEILI_MASTER_KEY" \
    http://localhost:7700/indexes/apple-docs/stats 2>/dev/null | \
    python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('numberOfDocuments', 0))" 2>/dev/null || echo "0")

if [ "$DOC_COUNT" -gt 300000 ]; then
    echo "📊 Current documents: $(printf "%'d" $DOC_COUNT)"
    echo ""
    echo "✅ Index appears complete!"
    echo "   No need to re-index unless you want to update the data."
    echo ""
    read -p "Do you want to re-index anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Exiting without re-indexing."
        exit 0
    fi
elif [ "$DOC_COUNT" -gt 0 ]; then
    echo "⚠️  Current documents: $(printf "%'d" $DOC_COUNT)"
    echo "   This is less than expected (>300,000)"
    echo ""
else
    echo "📋 No documents indexed yet"
    echo ""
fi

echo "Starting indexing process..."
echo "This will take approximately 4 minutes."
echo ""

# Run the indexing script
cd /app/scripts
python3 index_to_meilisearch.py

echo ""
echo "✅ Indexing complete!"

# Check final count
FINAL_COUNT=$(curl -s -H "Authorization: Bearer $MEILI_MASTER_KEY" \
    http://localhost:7700/indexes/apple-docs/stats 2>/dev/null | \
    python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('numberOfDocuments', 0))" 2>/dev/null || echo "0")

echo "📊 Final document count: $(printf "%'d" $FINAL_COUNT)"

if [ "$FINAL_COUNT" -gt 300000 ]; then
    echo "✅ Success! Your Apple Docs V2 server is ready to use."
else
    echo "⚠️  Document count is lower than expected."
    echo "   Please check /data/logs/meilisearch.log for any errors."
fi