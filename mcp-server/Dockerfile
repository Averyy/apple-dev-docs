# Multi-stage Dockerfile for Apple Docs MCP Server V2 with Meilisearch
# All-in-one container with Meilisearch search engine and MCP server

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
RUN mkdir -p /data/meilisearch /data/hashes /data/documentation /data/logs \
    /var/log/supervisor

# Copy application code
COPY mcp-server/ /app/mcp-server/
COPY scripts/ /app/scripts/

# Copy scraper code
COPY scraper/ /app/scraper/
COPY scrape.py /app/
COPY requirements.txt /app/

# Copy pre-scraped documentation and hashes
COPY documentation/ /data/documentation/
COPY .hashes/ /data/hashes/

# Keep a backup copy for volume mounting scenarios
COPY documentation/ /app/documentation_backup/

# Copy supervisor configuration
COPY mcp-server/docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Copy startup script and helpers
COPY mcp-server/docker/startup.sh /app/startup.sh
COPY mcp-server/scripts/docker_index_helper.sh /app/scripts/
COPY mcp-server/scripts/debug_http_wrapper.sh /app/mcp-server/scripts/
RUN chmod +x /app/startup.sh /app/scripts/docker_index_helper.sh /app/mcp-server/scripts/debug_http_wrapper.sh

# Note: Indexing happens automatically on first run via startup_check.py
# Meilisearch must be running, so we can't pre-index during build

# Environment variables (can be overridden at runtime)
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV HTTP_PORT=8080
ENV MEILISEARCH_PATH=/data/meilisearch
ENV HASHES_PATH=/data/hashes
ENV DOCUMENTATION_PATH=/data/documentation
ENV LOG_PATH=/data/logs
# Meilisearch configuration
ENV MEILI_HTTP_ADDR=http://localhost:7700
ENV MEILI_DB_PATH=/data/meilisearch
# HTTP wrapper enabled by default for remote access
ENV ENABLE_HTTP_WRAPPER=true
# Auto-rescraping (disabled by default)
ENV ENABLE_AUTO_RESCRAPE=false
# Default timezone to US Eastern (EST/EDT)
ENV TZ=America/New_York

# Expose HTTP port for remote access wrapper
EXPOSE 8080

# Health check for Meilisearch (STDIO MCP server doesn't have HTTP endpoint)
HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=3 \
    CMD curl -f http://localhost:7700/health || exit 1

# Use startup script
ENTRYPOINT ["/app/startup.sh"]