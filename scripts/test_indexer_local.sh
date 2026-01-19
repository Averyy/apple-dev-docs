#!/bin/bash
# Local testing script for the indexer fix
# Tests the OOM fix by running a force rebuild against local Meilisearch

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "=========================================="
echo "Apple Docs Indexer - Local Test"
echo "=========================================="
echo ""

# Check if Meilisearch is running
if ! curl -s http://localhost:7700/health > /dev/null 2>&1; then
    echo "❌ Meilisearch is not running on localhost:7700"
    echo ""
    echo "Start it with:"
    echo "  cd meilisearch && docker compose up -d"
    echo ""
    echo "Or install and run locally:"
    echo "  brew install meilisearch"
    echo "  meilisearch --master-key=test_key"
    exit 1
fi

echo "✅ Meilisearch is running"
echo ""

# Set up environment
export MEILI_HTTP_ADDR="http://localhost:7700"
export MEILI_MASTER_KEY="${MEILI_MASTER_KEY:-local_test_key}"

# Check current index status
DOC_COUNT=$(curl -s -H "Authorization: Bearer $MEILI_MASTER_KEY" \
    "http://localhost:7700/indexes/apple-docs/stats" 2>/dev/null | \
    python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('numberOfDocuments', 0))" 2>/dev/null || echo "0")

echo "📊 Current index: $DOC_COUNT documents"
echo ""

# Count local documentation files
DOC_FILES=$(find "$PROJECT_ROOT/documentation" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
echo "📁 Local documentation: $DOC_FILES markdown files"
echo ""

# Parse arguments
FORCE=""
LIMIT_VALUE=""
DRY_RUN=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --force)
            FORCE="true"
            shift
            ;;
        --limit)
            LIMIT_VALUE="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN="true"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [--force] [--limit N] [--dry-run]"
            exit 1
            ;;
    esac
done

# Build command arguments array (safer than eval)
CMD_ARGS=("$SCRIPT_DIR/index_to_meilisearch.py" "--docs-path" "$PROJECT_ROOT/documentation")
[[ -n "$FORCE" ]] && CMD_ARGS+=("--force")
[[ -n "$LIMIT_VALUE" ]] && CMD_ARGS+=("--limit" "$LIMIT_VALUE")
[[ -n "$DRY_RUN" ]] && CMD_ARGS+=("--dry-run")

echo "🚀 Running indexer:"
echo "   python3 ${CMD_ARGS[*]}"
echo ""
echo "=========================================="
echo ""

# Run the indexer directly (no eval)
python3 "${CMD_ARGS[@]}"

echo ""
echo "=========================================="

# Check final state
NEW_COUNT=$(curl -s -H "Authorization: Bearer $MEILI_MASTER_KEY" \
    "http://localhost:7700/indexes/apple-docs/stats" 2>/dev/null | \
    python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('numberOfDocuments', 0))" 2>/dev/null || echo "0")

echo ""
echo "📊 Final index: $NEW_COUNT documents"
echo "✅ Test complete"
