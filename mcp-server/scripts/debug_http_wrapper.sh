#!/bin/bash
# Debug wrapper for HTTP STDIO wrapper

echo "=== HTTP Wrapper Debug Script ===" >&2
echo "Date: $(date)" >&2
echo "Environment variables:" >&2
echo "  ENABLE_HTTP_WRAPPER=$ENABLE_HTTP_WRAPPER" >&2
echo "  MCP_API_KEY=${MCP_API_KEY:+[SET]}" >&2
echo "  HTTP_PORT=$HTTP_PORT" >&2
echo "  MEILI_MASTER_KEY=${MEILI_MASTER_KEY:+[SET]}" >&2
echo "  MEILI_HTTP_ADDR=$MEILI_HTTP_ADDR" >&2
echo "  PYTHONUNBUFFERED=$PYTHONUNBUFFERED" >&2
echo "" >&2

if [ "$(echo $ENABLE_HTTP_WRAPPER | tr '[:upper:]' '[:lower:]')" = "true" ]; then
    echo "HTTP wrapper is enabled, starting..." >&2
    cd /app
    exec python -u /app/mcp-server/http_stdio_wrapper.py 2>&1
else
    echo "HTTP wrapper is disabled (ENABLE_HTTP_WRAPPER=$ENABLE_HTTP_WRAPPER)" >&2
    # Keep the process alive so supervisor doesn't restart
    while true; do
        sleep 86400
    done
fi