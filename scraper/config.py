"""Configuration settings for Apple Documentation Scraper."""

import os
from pathlib import Path
from typing import Optional

from scraper.site import APPLE


class Config:
    """Centralized configuration for the scraper."""
    
    # Base URLs (developer.apple.com's, site.APPLE)
    BASE_URL = APPLE.site_url
    DOCUMENTATION_URL = APPLE.doc_base
    TECHNOLOGIES_URL = f"{DOCUMENTATION_URL}/technologies"
    
    # Rate limiting (optimized for JSON API endpoints)
    RATE_LIMIT_DELAY = float(os.getenv("RATE_LIMIT_DELAY", "0.1"))
    REQUEST_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "30.0"))
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
    RETRY_BACKOFF_FACTOR = float(os.getenv("RETRY_BACKOFF_FACTOR", "2.0"))
    
    # User agent
    USER_AGENT = os.getenv(
        "USER_AGENT",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    
    # Storage paths
    OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "./documentation"))
    CACHE_DIR = Path(os.getenv("CACHE_DIR", "./.hashes"))
    METADATA_DIR = Path(os.getenv("METADATA_DIR", "./_metadata"))
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = os.getenv("LOG_FORMAT", "console")
    LOG_FILE = Path(os.getenv("LOG_FILE", "./scraper.log")) if os.getenv("LOG_FILE") else None
    
    # Concurrent page fetches within a single framework, used by the JSON
    # scraper's streaming discovery path (the main production path). Default
    # 1 = sequential, the long-standing behavior (GitHub Actions keeps this).
    # Raise via env for faster manual runs.
    INTRA_FRAMEWORK_CONCURRENCY = max(1, int(os.getenv("INTRA_FRAMEWORK_CONCURRENCY", "1")))

    # Development settings
    TEST_MODE = os.getenv("TEST_MODE", "false").lower() == "true"
    DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
    
    @classmethod
    def ensure_directories(cls) -> None:
        """Create required directories if they don't exist."""
        for directory in [cls.OUTPUT_DIR, cls.CACHE_DIR, cls.METADATA_DIR]:
            directory.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def get_framework_output_dir(
        cls, framework_id: str, framework_name: Optional[str] = None, namespace: str = ""
    ) -> Path:
        """Get the output directory for a specific framework.
        
        Args:
            framework_id: Framework ID (usually lowercase)
            framework_name: Framework display name (not used for directory)
            namespace: Its DocC site's namespace (site.DocCSite.namespace):
                documentation/<namespace>/<id>; "" for Apple's
        """
        # Always use framework_id for directory to match Apple's URL structure
        return cls.get_docs_dir(namespace) / framework_id
    
    @classmethod
    def get_hash_file(cls, framework_id: str, framework_name: Optional[str] = None, namespace: str = "") -> Path:
        """Get the hash file path for a specific framework.
        
        Args:
            framework_id: Framework ID (usually lowercase)
            framework_name: Framework display name (not used for filename)
            namespace: Its DocC site's namespace: .hashes/<namespace>/<id>_hashes.json
        """
        # Always use framework_id for hash file to match directory structure
        return cls.get_hash_dir(namespace) / f"{framework_id}_hashes.json"

    @classmethod
    def get_docs_dir(cls, namespace: str = "") -> Path:
        """A DocC site's docs root: documentation/<namespace> (the docs root itself for Apple's)."""
        return cls.OUTPUT_DIR / namespace if namespace else cls.OUTPUT_DIR

    @classmethod
    def get_hash_dir(cls, namespace: str = "") -> Path:
        """A DocC site's hash dir: .hashes/<namespace> (.hashes itself for Apple's)."""
        return cls.CACHE_DIR / namespace if namespace else cls.CACHE_DIR
    
    @classmethod
    def get_metadata_file(cls, filename: str) -> Path:
        """Get a metadata file path."""
        return cls.METADATA_DIR / filename