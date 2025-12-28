# Multi-stage Dockerfile for Apple Docs MCP Server V2 with Meilisearch
# All-in-one container with Meilisearch search engine and MCP server

# Server version - update this when releasing new versions
ARG SERVER_VERSION=1.1.0

# Stage 1: Builder
FROM python:3.11-slim AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy requirements first for better caching
COPY mcp-server/requirements.txt mcp-requirements.txt
COPY requirements.txt main-requirements.txt
RUN pip install --user --no-cache-dir -r mcp-requirements.txt && \
    pip install --user --no-cache-dir -r main-requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

# Re-declare ARG after FROM to make it available in this stage
ARG SERVER_VERSION=1.1.0

# Add labels for version tracking and metadata
LABEL org.opencontainers.image.title="Apple Docs MCP Server"
LABEL org.opencontainers.image.description="MCP server for searching Apple Developer Documentation"
LABEL org.opencontainers.image.version="${SERVER_VERSION}"
LABEL org.opencontainers.image.source="https://github.com/averyy/apple-developer-docs"
LABEL maintainer="averyy"

# Running as root for Unraid compatibility
# RUN useradd -m -u 1000 -s /bin/bash mcpuser

# Install runtime dependencies, timezone data, and Meilisearch
RUN apt-get update && apt-get install -y \
    supervisor \
    curl \
    tzdata \
    wget \
    && rm -rf /var/lib/apt/lists/* \
    && wget -qO /usr/bin/meilisearch https://github.com/meilisearch/meilisearch/releases/download/v1.9.0/meilisearch-linux-amd64 \
    && chmod +x /usr/bin/meilisearch

# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are callable
ENV PATH=/root/.local/bin:$PATH

# Create app directory and data directories
WORKDIR /app
RUN mkdir -p /data/meilisearch /data/logs \
    /var/log/supervisor

# Copy application code
COPY mcp-server/ /app/mcp-server/
COPY scripts/ /app/scripts/

# Scraper not included - scraping requires persistent storage

# Copy pre-scraped documentation only (hashes not needed in Docker)
COPY documentation/ /data/documentation/

# Copy supervisor configuration
COPY mcp-server/docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Copy startup script and helpers
COPY mcp-server/docker/startup.sh /app/startup.sh
COPY mcp-server/scripts/docker_index_helper.sh /app/scripts/
RUN chmod +x /app/startup.sh /app/scripts/docker_index_helper.sh

# Note: Indexing happens automatically on first run via startup_check.py
# Meilisearch must be running, so we can't pre-index during build

# Environment variables (can be overridden at runtime)
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV HTTP_PORT=8000
ENV MEILISEARCH_PATH=/data/meilisearch
ENV DOCUMENTATION_PATH=/data/documentation
ENV LOG_PATH=/data/logs
# Meilisearch configuration
ENV MEILI_HTTP_ADDR=http://localhost:7700
ENV MEILI_DB_PATH=/data/meilisearch
# Rate limiting (requests per minute)
ENV RATE_LIMIT_REQUESTS=30
# Default timezone to US Eastern (EST/EDT)
ENV TZ=America/New_York

# Expose HTTP port for native MCP server
EXPOSE 8000

# Health check for Meilisearch (STDIO MCP server doesn't have HTTP endpoint)
HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=3 \
    CMD curl -f http://localhost:7700/health || exit 1

# Use startup script
ENTRYPOINT ["/app/startup.sh"]