"""
Shared hash utilities for incremental scraping and indexing.

All scrapers use these functions to track file changes and avoid
re-processing unchanged content.
"""

import hashlib
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

logger = logging.getLogger(__name__)


def compute_hash(content: str) -> str:
    """Compute SHA-256 hash of string content."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def compute_file_hash(file_path: Path) -> str:
    """Compute SHA-256 hash of a file, reading in chunks for memory efficiency."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def load_hashes(hash_file: Path) -> Dict[str, str]:
    """
    Load stored file hashes for incremental updates.

    Supports both old format (flat dict) and new format (with metadata).
    """
    if hash_file.exists():
        try:
            with open(hash_file, 'r') as f:
                data = json.load(f)
                # Support both old format (flat dict) and new format (with metadata)
                if isinstance(data, dict) and "hashes" in data:
                    return data["hashes"]
                return data
        except (OSError, json.JSONDecodeError, KeyError) as e:
            logger.warning(f"Could not load hash file {hash_file}: {e}")
    return {}


def save_hashes(
    hash_file: Path,
    hashes: Dict[str, str],
    source: Optional[str] = None,
    include_metadata: bool = True
) -> None:
    """
    Save file hashes for next run.

    Args:
        hash_file: Path to save hashes to
        hashes: Dict mapping file paths/URLs to their hashes
        source: Optional source identifier (e.g., "scrape_swift_docs.py")
        include_metadata: If True, wrap hashes with metadata (last_updated, total_files)
    """
    hash_file.parent.mkdir(parents=True, exist_ok=True)

    if include_metadata:
        data = {
            "metadata": {
                "last_updated": datetime.now().isoformat(),
                "total_files": len(hashes),
            },
            "hashes": hashes
        }
        if source:
            data["metadata"]["source"] = source
    else:
        data = hashes

    try:
        with open(hash_file, 'w') as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        logger.error(f"Could not save hash file {hash_file}: {e}")


def has_content_changed(
    hashes: Dict[str, str],
    key: str,
    content: str
) -> bool:
    """
    Check if content has changed since last scrape.

    Args:
        hashes: Dict of stored hashes
        key: Key to look up (file path or URL)
        content: Current content to compare

    Returns:
        True if content is new or changed, False if unchanged
    """
    new_hash = compute_hash(content)
    old_hash = hashes.get(key, "")

    # Handle both flat format and nested format with 'hash' key
    if isinstance(old_hash, dict):
        old_hash = old_hash.get('hash', '')

    return new_hash != old_hash
