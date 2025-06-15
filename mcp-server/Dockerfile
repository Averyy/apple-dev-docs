# Multi-stage Dockerfile for Apple Docs MCP Server
# Following Docker best practices for production Python applications

# Stage 1: Builder
FROM python:3.11-slim as builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy requirements first for better caching
COPY mcp-server/requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

# Running as root for Unraid compatibility
# RUN useradd -m -u 1000 -s /bin/bash mcpuser

# Install runtime dependencies and timezone data
RUN apt-get update && apt-get install -y \
    supervisor \
    curl \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are callable
ENV PATH=/root/.local/bin:$PATH

# Create app directory and data directories
WORKDIR /app
RUN mkdir -p /data/vectorstore /data/hashes /data/documentation /data/logs \
    /var/log/supervisor

# Copy application code
COPY mcp-server/server/ /app/server/
COPY mcp-server/scripts/ /app/scripts/
COPY mcp-server/requirements.txt /app/

# Copy scraper code
COPY scraper/ /app/scraper/

# Copy supervisor configuration
COPY mcp-server/docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Copy startup script
COPY mcp-server/docker/startup.sh /app/startup.sh
RUN chmod +x /app/startup.sh

# Environment variables (can be overridden at runtime)
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV MCP_PORT=8080
ENV VECTORSTORE_PATH=/data/vectorstore
ENV HASHES_PATH=/data/hashes
ENV DOCUMENTATION_PATH=/data/documentation
ENV LOG_PATH=/data/logs
ENV KEEP_MARKDOWN_FILES=true
# Default timezone to US Eastern (EST/EDT)
ENV TZ=America/New_York

# Expose MCP server port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Use startup script
ENTRYPOINT ["/app/startup.sh"]