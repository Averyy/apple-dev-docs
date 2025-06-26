"""
Configuration settings for Apple Docs MCP Server
"""

import os

# Search configuration
DEFAULT_SEARCH_LIMIT = 10
MAX_SEARCH_LIMIT = 50

# Server configuration
MCP_PORT = int(os.getenv("MCP_PORT", "8000"))

# Meilisearch configuration
MEILISEARCH_URL = os.getenv("MEILI_HTTP_ADDR", "http://localhost:7700")
MEILISEARCH_API_KEY = os.getenv("MEILI_SEARCH_KEY", os.getenv("MEILI_MASTER_KEY", ""))
MEILISEARCH_INDEX = "apple-docs"

# Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")