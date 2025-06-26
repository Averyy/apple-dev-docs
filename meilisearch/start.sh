#!/bin/bash

# Start Meilisearch locally for development

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting Meilisearch for Apple Developer Docs...${NC}"

# Check if .env exists
if [ ! -f .env ]; then
    echo -e "${YELLOW}No .env file found. Creating from .env.example...${NC}"
    cp .env.example .env
    echo -e "${YELLOW}Please update .env with your configuration if needed.${NC}"
fi

# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Start Meilisearch
echo -e "${GREEN}Starting Meilisearch container...${NC}"
docker-compose up -d

# Wait for health check
echo -e "${GREEN}Waiting for Meilisearch to be healthy...${NC}"
attempt=0
max_attempts=30

while [ $attempt -lt $max_attempts ]; do
    if docker-compose exec -T meilisearch curl -sf http://localhost:7700/health > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Meilisearch is healthy!${NC}"
        break
    fi
    echo -n "."
    sleep 2
    attempt=$((attempt + 1))
done

if [ $attempt -eq $max_attempts ]; then
    echo -e "${RED}✗ Meilisearch failed to start. Check logs:${NC}"
    docker-compose logs meilisearch
    exit 1
fi

# Display connection info
echo -e "\n${GREEN}Meilisearch is running!${NC}"
echo -e "URL: ${YELLOW}http://localhost:7700${NC}"
echo -e "Master Key: ${YELLOW}${MEILI_MASTER_KEY}${NC}"
echo -e "\nTest with:"
echo -e "  ${YELLOW}curl http://localhost:7700/health${NC}"
echo -e "\nView logs:"
echo -e "  ${YELLOW}docker-compose logs -f meilisearch${NC}"
echo -e "\nStop with:"
echo -e "  ${YELLOW}docker-compose down${NC}"