"""
Configuration for Apple Docs MCP Server
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Required settings
VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY")
MCP_API_KEY = os.getenv("MCP_API_KEY")

# Legacy TEI URL (kept for backward compatibility)
TEI_URL = os.getenv("TEI_URL", "http://192.168.2.5/embed")

# Optional settings with defaults
VECTORSTORE_PATH = Path(os.getenv("VECTORSTORE_PATH", "./vectorstore"))
DOCS_PATH = Path(os.getenv("DOCS_PATH", "../documentation"))
KEEP_MARKDOWN_FILES = os.getenv("KEEP_MARKDOWN_FILES", "true").lower() == "true"
MCP_PORT = int(os.getenv("MCP_PORT", "8080"))

# Embedding settings
EMBEDDING_BATCH_SIZE = 96  # Voyage AI supports up to 128
EMBEDDING_MODEL = "voyage-3-lite"  # Voyage AI model
EMBEDDING_DIMENSIONS = 512  # voyage-3-lite dimensions

# Search settings
DEFAULT_SEARCH_LIMIT = 5
MAX_SEARCH_LIMIT = 20

# Collection name
COLLECTION_NAME = "apple_docs"

# Ensure directories exist
VECTORSTORE_PATH.mkdir(parents=True, exist_ok=True)