# Task 6: Docker Deployment with Auto-Rescraping

## Objective
Deploy the MCP server as a Docker container with persistent volumes and automatic rescraping every 3 months.

## Architecture Overview

```
Docker Container
├── MCP Server (Port 3000)          # Always running, serves queries
└── Scheduler (Background)          # Checks hourly, rescrapes every 3 months at midnight

Docker Volumes (Persist across updates)
├── vectorstore/    # ChromaDB vector database (~8GB)
├── metadata/       # ETags, hashes, update timestamps (~100MB)
├── scraped/        # Raw documentation files (~2GB)
└── logs/           # Application logs (~50MB)
```

## Implementation

### 1. Dockerfile (Multi-Process Container)

The Dockerfile uses supervisor to run both MCP server and scheduler:
- MCP server: Always available for queries
- Scheduler: Runs rescraping every 3 months at midnight
- Pre-built vectorstore: Embedded in image for fast first start

Key features:
- Multi-stage build for smaller image
- Supervisor for process management
- Smart startup script that extracts pre-built data on first run

### 2. Docker Volumes for Persistence

```bash
# Create named volumes (one-time setup)
docker volume create apple-docs-vectorstore
docker volume create apple-docs-metadata
docker volume create apple-docs-scraped  # Optional in production
docker volume create apple-docs-logs

# Run container with persistent volumes
docker run -d \
  --name apple-docs-mcp \
  -p 127.0.0.1:3000:3000 \
  -v apple-docs-vectorstore:/data/vectorstore \
  -v apple-docs-metadata:/data/metadata \
  -v apple-docs-scraped:/data/scraped \
  -v apple-docs-logs:/var/log/supervisor \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  -e KEEP_MARKDOWN_FILES=false \  # Production: Don't keep markdown
  --restart unless-stopped \
  ghcr.io/yourusername/apple-developer-docs-mcp:latest
```

### Environment Variables

- `KEEP_MARKDOWN_FILES` (default: `true`): Controls markdown file retention
  - `true` (Default/Development): Keeps markdown files after embedding for debugging
  - `false` (Production): Deletes markdown after embedding to save space
  - If not specified, defaults to `true` to preserve markdown files (safe default)

With `KEEP_MARKDOWN_FILES=false`, the scraped volume is barely used (~100MB for temporary files).

### Production vs Development Examples

**Development (keep files for debugging):**
```bash
docker run -d \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  -e KEEP_MARKDOWN_FILES=true \
  ...
```

**Production (save space):**
```bash
docker run -d \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  -e KEEP_MARKDOWN_FILES=false \
  ...
```

### 3. Automatic Rescraping System

The scheduler (`scripts/schedule_rescrape.py`):
- Runs continuously in background
- Checks every hour if it's time to rescrape
- At midnight every 3 months: triggers update check
- Uses ETags for efficient change detection (HEAD requests only)
- For changed documents:
  1. Downloads JSON from Apple
  2. Converts to markdown (in memory)
  3. Updates ETag in metadata
  4. Generates new embedding
  5. If `KEEP_MARKDOWN_FILES=false`: Discards markdown
  6. If `KEEP_MARKDOWN_FILES=true`: Saves markdown to disk

### 4. Simplified Startup Strategy

**Current startup script complexity**: The Dockerfile includes an elaborate startup script that checks for pre-built data, extracts archives, shows statistics, etc.

**Simplification options**:

**Option A: Keep Smart Startup (Recommended)**
- Maintains current functionality for ease of use
- Automatically handles first-run setup
- Shows helpful status information

**Option B: Minimal Startup Script**
```bash
#!/bin/bash
# Simple startup - just run the services
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
```

**Option C: No Pre-Built Data**
- Remove pre-built vectorstore complexity
- Always build on first run (takes 1-2 hours)
- Simpler Dockerfile but slower first deployment

**Recommendation**: Keep the current smart startup since it provides:
- Instant startup when pre-built data exists  
- Clear status messages for debugging
- Automatic fallback to building if needed

The complexity is worth it for the user experience improvement.

### 5. GitHub Actions CI/CD

`.github/workflows/deploy.yml`:
- Builds Docker image on push to main
- Pushes to ghcr.io (GitHub Container Registry)
- Optional: Include pre-built vectorstore in image

## Deployment Steps

### Initial Setup
1. Build vectorstore locally with existing docs
2. Create GitHub Actions workflow
3. Push to trigger Docker build
4. Deploy to server with quick-start script

### Quick Deploy Script
```bash
# deploy/quick-start.sh handles everything:
- Creates Docker volumes
- Pulls latest image
- Starts container
- Checks health
- Shows connection info
```

## Cost Analysis

### One-Time Costs
- Initial vectorstore build: ~$5

### Ongoing Costs (with ETags)
- Quarterly rescrape checks: ~$0.01 (HEAD requests)
- Embedding updates (5% change rate): ~$0.25/quarter
- Total: ~$1/year

## Monitoring

### Check Status
```bash
# View both processes
docker exec apple-docs-mcp supervisorctl status

# Check last update
docker exec apple-docs-mcp cat /data/metadata/last_update.txt

# View logs
docker logs apple-docs-mcp
```

### Manual Operations
```bash
# Force immediate rescrape
docker exec apple-docs-mcp python /app/scripts/auto_rescrape_and_embed.py

# Restart MCP server only
docker exec apple-docs-mcp supervisorctl restart mcp-server
```

## Key Benefits

1. **Zero Maintenance**: Fully automated updates
2. **Fast Startup**: Pre-built data = instant availability
3. **Persistent Data**: Survives container updates
4. **Efficient Updates**: ETags minimize bandwidth/costs
5. **Always Available**: MCP server runs during updates

## Time Estimate
- Initial setup: 2-3 hours
- Deployment: 15 minutes
- Ongoing maintenance: 0 (fully automated)