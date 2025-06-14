#!/bin/bash
set -e

# Apple Docs MCP Server - Quick Deployment Script
# This script handles the complete deployment of the MCP server with Docker

echo "🍎 Apple Docs MCP Server - Quick Deployment"
echo "=========================================="
echo ""

# Check prerequisites
check_prerequisites() {
    echo "🔍 Checking prerequisites..."
    
    # Check Docker
    if ! command -v docker &> /dev/null; then
        echo "❌ Docker is not installed. Please install Docker first."
        echo "   Visit: https://docs.docker.com/get-docker/"
        exit 1
    fi
    
    # Check Docker Compose
    if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
        echo "❌ Docker Compose is not installed."
        exit 1
    fi
    
    # Check for .env file (look in parent of parent directory since we're in deploy/)
    if [ ! -f "../../.env" ]; then
        echo "❌ .env file not found in project root"
        echo "   Please create .env with:"
        echo "   - OPENAI_API_KEY=your-key"
        echo "   - MCP_API_KEY=your-key"
        exit 1
    fi
    
    # Source .env file
    set -a
    source ../../.env
    set +a
    
    # Check required environment variables
    if [ -z "$OPENAI_API_KEY" ]; then
        echo "❌ OPENAI_API_KEY not set in .env file"
        exit 1
    fi
    
    if [ -z "$MCP_API_KEY" ]; then
        echo "❌ MCP_API_KEY not set in .env file"
        exit 1
    fi
    
    echo "✅ All prerequisites met"
    echo ""
}

# Create Docker volumes
create_volumes() {
    echo "📦 Creating Docker volumes..."
    
    # Docker Compose will create the volumes automatically with the project prefix
    # No need to manually create them
    
    echo "✅ Volumes created/verified"
    echo ""
}

# Build Docker image
build_image() {
    echo "🏗️  Building Docker image..."
    echo "   This may take a few minutes on first build..."
    
    cd ..  # Go to mcp-server directory
    docker-compose build
    
    echo "✅ Image built successfully"
    echo ""
}

# Start services
start_services() {
    echo "🚀 Starting services..."
    
    # Stop any existing container
    docker-compose down 2>/dev/null || true
    
    # Start in detached mode
    docker-compose up -d
    
    echo "✅ Services started"
    echo ""
}

# Wait for health check
wait_for_health() {
    echo "⏳ Waiting for MCP server to be healthy..."
    
    local max_attempts=30
    local attempt=0
    
    while [ $attempt -lt $max_attempts ]; do
        if docker exec apple-docs-mcp curl -f http://localhost:8080/health &>/dev/null; then
            echo "✅ MCP server is healthy!"
            return 0
        fi
        
        attempt=$((attempt + 1))
        echo -n "."
        sleep 2
    done
    
    echo ""
    echo "❌ MCP server failed to become healthy"
    echo "   Check logs with: docker logs apple-docs-mcp"
    return 1
}

# Show status and connection info
show_status() {
    echo ""
    echo "📊 Deployment Status"
    echo "==================="
    
    # Container status
    docker ps --filter name=apple-docs-mcp --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    
    echo ""
    echo "📡 Connection Information"
    echo "========================"
    echo "MCP Server URL: http://localhost:8080"
    echo "Health Check: http://localhost:8080/health"
    echo ""
    echo "🔑 Authentication"
    echo "================"
    echo "Include this header in all requests:"
    echo "Authorization: Bearer $MCP_API_KEY"
    echo ""
    echo "📋 Useful Commands"
    echo "================="
    echo "View logs:        docker logs -f apple-docs-mcp"
    echo "Check processes:  docker exec apple-docs-mcp supervisorctl status"
    echo "Stop server:      docker-compose down"
    echo "Update & restart: git pull && docker-compose up -d --build"
    echo ""
    
    # Show next scheduled scrape
    echo "📅 Rescraping Schedule"
    echo "===================="
    echo "Next automatic rescrape: Next Sunday at 1:00 AM"
    echo "Force rescrape now: docker exec apple-docs-mcp python /app/scraper/auto_scrape_and_embed.py --embed --yes"
    echo ""
}

# Main execution
main() {
    check_prerequisites
    create_volumes
    build_image
    start_services
    
    if wait_for_health; then
        show_status
        echo "🎉 Deployment completed successfully!"
    else
        echo "❌ Deployment failed. Please check the logs."
        exit 1
    fi
}

# Run main function
main