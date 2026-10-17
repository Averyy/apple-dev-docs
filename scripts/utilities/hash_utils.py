"""
Shared hash and file utilities for incremental scraping and indexing.

All scrapers use these functions to track file changes and avoid
re-processing unchanged content, and to write their files atomically.
"""

import hashlib
import json
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Tuple

logger = logging.getLogger(__name__)

# Metadata keys save_hashes writes itself on every save; every other key is
# the caller's (metadata=) and is written as given.
RUN_METADATA_KEYS = ("last_updated", "total_files", "source")

# The longest file name, in bytes, on the filesystems we write to (ext4, APFS)
NAME_MAX = 255


class HashFileError(Exception):
    """A hash file exists but can't be read as a hash file."""


def write_text_atomic(path: Path, text: str) -> None:
    """Write a file whole or not at all (UTF-8).

    The text goes to "<name>.tmp" next to the file, which then replaces it
    (os.replace), so a write that fails (e.g. a full disk) or is interrupted
    leaves the previous file as it was, and its temp file is removed (*.tmp
    is git-ignored). A name too long for the suffix gets a short temp name.
    The same as the Apple scraper's (scraper/utils/hash_manager.py
    write_text_atomic).

    Raises:
        OSError: The write failed
    """
    name = f"{path.name}.tmp"
    if len(os.fsencode(name)) > NAME_MAX:
        name = f"{hashlib.sha1(os.fsencode(path.name)).hexdigest()}.tmp"
    temp_file = path.with_name(name)
    try:
        temp_file.write_text(text, encoding='utf-8')
        os.replace(temp_file, path)
    except BaseException:
        try:
            temp_file.unlink(missing_ok=True)
        except OSError:
            pass
        raise


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


def read_hash_file(hash_file: Path) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """A hash file's hashes and metadata, as saved.

    Supports both formats: the old flat dict (all hashes, no metadata) and
    {"metadata": {...}, "hashes": {...}}. A missing file reads as empty.

    Raises:
        HashFileError: The file exists but can't be read, isn't valid JSON or
            UTF-8, or doesn't have either shape
    """
    if not hash_file.exists():
        return {}, {}
    try:
        with open(hash_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (OSError, ValueError) as e:  # ValueError covers JSON and UTF-8 decode errors
        raise HashFileError(f"{hash_file}: {e}") from e
    if not isinstance(data, dict):
        raise HashFileError(f"{hash_file}: expected a JSON object")
    if "hashes" not in data:
        return data, {}
    hashes, metadata = data["hashes"], data.get("metadata", {})
    if not isinstance(hashes, dict) or not isinstance(metadata, dict):
        raise HashFileError(f"{hash_file}: 'hashes' and 'metadata' must be JSON objects")
    return hashes, metadata


def load_hashes(hash_file: Path) -> Dict[str, Any]:
    """
    Load stored file hashes for incremental updates.

    Supports both old format (flat dict) and new format (with metadata).
    A file that can't be read loads as empty (logged).
    """
    try:
        return read_hash_file(hash_file)[0]
    except HashFileError as e:
        logger.warning(f"Could not load hash file {hash_file}: {e}")
        return {}


def load_metadata(hash_file: Path) -> Dict[str, Any]:
    """
    Load a hash file's metadata: what save_hashes wrote, including every key
    given to its metadata= argument.

    Empty for the old flat format, a missing file, or one that can't be read
    (logged).
    """
    try:
        return read_hash_file(hash_file)[1]
    except HashFileError as e:
        logger.warning(f"Could not load hash file {hash_file}: {e}")
        return {}


def save_hashes(
    hash_file: Path,
    hashes: Mapping[str, Any],
    source: Optional[str] = None,
    include_metadata: bool = True,
    metadata: Optional[Mapping[str, Any]] = None,
) -> bool:
    """
    Save file hashes for next run.

    The file is replaced atomically (written to a temporary file next to it,
    then renamed), so a crash mid-save never leaves a truncated hash file.

    Args:
        hash_file: Path to save hashes to
        hashes: Dict mapping file paths/URLs to their hashes
        source: Optional source identifier (e.g., "scrape_swift_docs.py")
        include_metadata: If True, wrap hashes with metadata (last_updated, total_files)
        metadata: More metadata keys to save, each written as given (e.g.
            sources, failure_counts, pending_orphans); the caller leaves out
            a key it doesn't want kept. The keys save_hashes writes itself
            (RUN_METADATA_KEYS) can't be overridden.

    Returns:
        True if the file was written; False if the write failed (logged)
    """
    data: Dict[str, Any]
    if include_metadata:
        file_metadata: Dict[str, Any] = {
            "last_updated": datetime.now().isoformat(),
            "total_files": len(hashes),
        }
        if source:
            file_metadata["source"] = source
        for key, value in (metadata or {}).items():
            if key not in RUN_METADATA_KEYS:
                file_metadata[key] = value
        data = {"metadata": file_metadata, "hashes": dict(hashes)}
    else:
        data = dict(hashes)

    try:
        hash_file.parent.mkdir(parents=True, exist_ok=True)
        write_text_atomic(hash_file, json.dumps(data, indent=2))
        return True
    except (OSError, TypeError, ValueError) as e:
        logger.error(f"Could not save hash file {hash_file}: {e}")
        return False


def has_content_changed(
    hashes: Mapping[str, Any],
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
    old_hash: Any = hashes.get(key, "")

    # Handle both flat format and nested format with 'hash' key
    if isinstance(old_hash, dict):
        old_hash = old_hash.get('hash', '')

    return bool(new_hash != old_hash)
