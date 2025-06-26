#!/bin/bash
# Script to build the full Docker image with documentation

set -e

echo "🚀 Building Apple Docs MCP Full Image"
echo "===================================="

# Check if documentation exists
if [ ! -d "../documentation" ]; then
    echo "❌ Error: Documentation directory not found at ../documentation"
    echo "   Please run 'python scrape.py --all --yes' first"
    exit 1
fi

# Check if .hashes exists
if [ ! -d "../.hashes" ]; then
    echo "❌ Error: Hashes directory not found at ../.hashes"
    exit 1
fi

# Count documents
DOC_COUNT=$(find ../documentation -name "*.md" | wc -l)
echo "📄 Found $DOC_COUNT markdown files"

if [ "$DOC_COUNT" -lt 300000 ]; then
    echo "⚠️  Warning: Only $DOC_COUNT documents found (expected >300,000)"
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Create compressed archive
echo "📦 Compressing documentation..."
cd ..
if [ -f "documentation.tar.xz" ]; then
    echo "   Removing old archive..."
    rm documentation.tar.xz
fi

# Use xz compression for better ratio (slower but smaller)
tar -cJf documentation.tar.xz documentation/
ARCHIVE_SIZE=$(du -h documentation.tar.xz | cut -f1)
echo "✅ Created documentation.tar.xz ($ARCHIVE_SIZE)"

# Move archive to mcp-server directory
mv documentation.tar.xz mcp-server/

# Copy .hashes directory
echo "📋 Copying hash files..."
cp -r .hashes mcp-server/

cd mcp-server

# Build base image first
echo "🏗️  Building base image..."
docker build -t apple-docs-mcp:latest .

# Build full image
echo "🏗️  Building full image with documentation..."
docker build -f Dockerfile.full -t apple-docs-mcp:full .

# Cleanup
echo "🧹 Cleaning up..."
rm -f documentation.tar.xz
rm -rf .hashes

# Show results
echo ""
echo "✅ Build complete!"
echo ""
echo "Images created:"
docker images | grep apple-docs-mcp
echo ""
echo "To use the full image:"
echo "  1. Update docker-compose.yml to use 'apple-docs-mcp:full'"
echo "  2. Run: docker-compose up -d"
echo ""
echo "The full image includes:"
echo "  - $DOC_COUNT pre-scraped documents"
echo "  - Pre-built Meilisearch index"
echo "  - Ready to use in <1 minute"