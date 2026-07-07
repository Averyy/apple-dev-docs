# Multi-stage Dockerfile for Apple Docs MCP Server V2 with Meilisearch
# All-in-one container with Meilisearch search engine and MCP server

# Server version - update this when releasing new versions
ARG SERVER_VERSION=2.4.0
# Build timestamps (set by CI/CD)
ARG BUILD_TIME=unknown
ARG DOCS_UPDATED=unknown

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

# Re-declare ARGs after FROM to make them available in this stage
ARG SERVER_VERSION=2.4.0
ARG BUILD_TIME=unknown
ARG DOCS_UPDATED=unknown

# Add labels for version tracking and metadata
LABEL org.opencontainers.image.title="Apple Docs MCP Server"
LABEL org.opencontainers.image.description="MCP server for searching Apple Developer Documentation"
LABEL org.opencontainers.image.version="${SERVER_VERSION}"
LABEL org.opencontainers.image.source="https://github.com/averyy/apple-developer-docs"
LABEL maintainer="averyy"

# SECURITY NOTE: Container runs as root for Unraid/NAS compatibility.
# Unraid requires containers to run as root or specific UIDs for volume permissions.
#
# To run as non-root (recommended for non-Unraid deployments):
# 1. Uncomment the useradd line and USER directive below
# 2. Update the COPY --from=builder line to use /home/mcpuser/.local
# 3. Ensure your volume mounts have appropriate permissions
#
# RUN useradd -m -u 1000 -s /bin/bash mcpuser
# USER mcpuser

# Install runtime dependencies, timezone data, and Meilisearch.
# TARGETARCH (set by buildx) picks the matching release asset so local arm64
# builds run natively (the amd64 release binary segfaults under QEMU
# emulation); CI builds linux/amd64 for production. The trailing --version
# call makes a broken binary fail the build instead of the container start.
ARG TARGETARCH
RUN apt-get update && apt-get install -y \
    supervisor \
    curl \
    tzdata \
    wget \
    && rm -rf /var/lib/apt/lists/* \
    && case "$TARGETARCH" in \
         arm64) MEILI_ARCH=aarch64; MEILI_SHA256=84028a6cd8874ffb539e3309dbe04028781ea6e9c74b36cc136c6fdf53efa861 ;; \
         *) MEILI_ARCH=amd64; MEILI_SHA256=4b9733aedbfa9a6dc0c2b07e38a58369f713a3603a27f409e6cb40081a180e26 ;; \
       esac \
    && wget -qO /usr/bin/meilisearch "https://github.com/meilisearch/meilisearch/releases/download/v1.49.0/meilisearch-linux-${MEILI_ARCH}" \
    && echo "${MEILI_SHA256}  /usr/bin/meilisearch" | sha256sum -c - \
    && chmod +x /usr/bin/meilisearch \
    && /usr/bin/meilisearch --version

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
ENV RATE_LIMIT_REQUESTS=60
# Public hostnames accepted by fastmcp's Host header guard (localhost always allowed)
ENV ALLOWED_HOSTS=xdocs.dev,www.xdocs.dev
# Default timezone to US Eastern (EST/EDT)
ENV TZ=America/New_York
# Build timestamps for health endpoint
ENV BUILD_TIME=${BUILD_TIME}
ENV DOCS_UPDATED=${DOCS_UPDATED}

# Expose HTTP port for native MCP server
EXPOSE 8000

# Health check against the MCP app itself, using the public hostname so
# app-level failures (e.g. Host header rejection) surface as unhealthy.
# The app returns 503 while the index is below serving threshold, so the
# container honestly reports unhealthy during an initial full reindex.
HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=3 \
    CMD curl -f -H "Host: ${ALLOWED_HOSTS%%,*}" "http://localhost:${HTTP_PORT:-8000}/health" || exit 1

# Use startup script
ENTRYPOINT ["/app/startup.sh"]