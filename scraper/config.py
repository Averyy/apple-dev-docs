"""Configuration settings for Apple Documentation Scraper."""

import os
from pathlib import Path
from typing import Optional


class Config:
    """Centralized configuration for the scraper."""
    
    # Base URLs
    BASE_URL = "https://developer.apple.com"
    DOCUMENTATION_URL = f"{BASE_URL}/documentation"
    TECHNOLOGIES_URL = f"{DOCUMENTATION_URL}/technologies"
    
    # Rate limiting (optimized for JSON API endpoints)
    RATE_LIMIT_DELAY = float(os.getenv("RATE_LIMIT_DELAY", "0.2"))
    MAX_CONCURRENT_REQUESTS = int(os.getenv("MAX_CONCURRENT_REQUESTS", "5"))
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
    
    # Development settings
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    TEST_MODE = os.getenv("TEST_MODE", "false").lower() == "true"
    DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
    
    # Puppeteer settings
    PUPPETEER_HEADLESS = os.getenv("PUPPETEER_HEADLESS", "true").lower() == "true"
    PUPPETEER_TIMEOUT = int(os.getenv("PUPPETEER_TIMEOUT", "60000"))
    
    @classmethod
    def ensure_directories(cls) -> None:
        """Create required directories if they don't exist."""
        for directory in [cls.OUTPUT_DIR, cls.CACHE_DIR, cls.METADATA_DIR]:
            directory.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def get_framework_output_dir(cls, framework_id: str) -> Path:
        """Get the output directory for a specific framework."""
        return cls.OUTPUT_DIR / framework_id
    
    @classmethod
    def get_hash_file(cls, framework_id: str) -> Path:
        """Get the hash file path for a specific framework."""
        return cls.CACHE_DIR / f"{framework_id}_hashes.json"
    
    @classmethod
    def get_metadata_file(cls, filename: str) -> Path:
        """Get a metadata file path."""
        return cls.METADATA_DIR / filename