#!/bin/bash
# Cleanup script for V2 migration

echo "🧹 Cleaning up old V1 files and test artifacts..."

# Remove Python cache directories
find . -type d -name "__pycache__" | grep -v "/venv/" | xargs rm -rf 2>/dev/null

# Remove mypy cache
rm -rf .mypy_cache mcp-server/.mypy_cache

# Remove test result files
rm -f scripts/*_results.json scripts/*_results.txt
rm -f .hashes/test_*.json

# Remove old log files
find . -name "*.log" -mtime +7 | grep -v "/venv/" | xargs rm -f 2>/dev/null

# Clean up any .DS_Store files (macOS)
find . -name ".DS_Store" | xargs rm -f 2>/dev/null

# Remove pytest cache
rm -rf .pytest_cache mcp-server/.pytest_cache

echo "✅ Cleanup complete!"
echo ""
echo "Note: This script preserves:"
echo "  - Virtual environments (/venv/)"
echo "  - Documentation files"
echo "  - Source code"
echo "  - Docker volumes"
echo "  - Configuration files"