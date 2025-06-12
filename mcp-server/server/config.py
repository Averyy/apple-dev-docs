"""
Configuration for Apple Docs MCP Server
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Get the project root directory (where .env file is located)
# This works whether we run from mcp-server/ or from project root
project_root = Path(__file__).parent.parent.parent  # server/config.py -> server -> mcp-server -> project root

# Load environment variables from project root
env_path = project_root / '.env'
if env_path.exists():
    load_dotenv(env_path)
else:
    # Try mcp-server directory as fallback
    mcp_env_path = Path(__file__).parent.parent / '.env'
    if mcp_env_path.exists():
        load_dotenv(mcp_env_path)

# Required settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MCP_API_KEY = os.getenv("MCP_API_KEY")

# Legacy TEI URL (kept for backward compatibility)
TEI_URL = os.getenv("TEI_URL", "http://192.168.2.5/embed")

# Optional settings with defaults
# Resolve paths relative to project root, not current working directory
VECTORSTORE_PATH = project_root / os.getenv("VECTORSTORE_PATH", "./vectorstore").lstrip('./')
DOCS_PATH = project_root / os.getenv("DOCS_PATH", "../documentation").lstrip('../')
KEEP_MARKDOWN_FILES = os.getenv("KEEP_MARKDOWN_FILES", "true").lower() == "true"
MCP_PORT = int(os.getenv("MCP_PORT", "8080"))

# Embedding settings
EMBEDDING_BATCH_SIZE = 96  # OpenAI supports large batches
EMBEDDING_MODEL = "text-embedding-3-small"  # OpenAI model used for vectorstore
EMBEDDING_DIMENSIONS = 1536  # text-embedding-3-small dimensions

# Search settings
DEFAULT_SEARCH_LIMIT = 5
MAX_SEARCH_LIMIT = 20

# Collection name
COLLECTION_NAME = "apple_docs"

# Ensure directories exist
VECTORSTORE_PATH.mkdir(parents=True, exist_ok=True)