#!/bin/bash

# Start Meilisearch with data stored in the project directory
# This ensures all data stays within the apple-developer-docs folder

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DATA_DIR="$PROJECT_ROOT/meilisearch/data"

# Create data directory if it doesn't exist
mkdir -p "$DATA_DIR"

echo "Starting Meilisearch..."
echo "Data directory: $DATA_DIR"
echo "Master key: local_test_key"
echo "URL: http://localhost:7700"

# Start Meilisearch with proper data path
meilisearch \
    --master-key "local_test_key" \
    --db-path "$DATA_DIR" \
    --http-addr "127.0.0.1:7700" \
    --max-indexing-memory "2Gb" \
    --http-payload-size-limit "200MB" \
    --log-level "INFO"