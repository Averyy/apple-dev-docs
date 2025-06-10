"""Content hash management for incremental updates."""

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, Set, List

from scraper.utils.logger import get_logger

logger = get_logger(__name__)


class HashManager:
    """Manage content hashes for incremental scraping."""
    
    def __init__(self, cache_file: Path) -> None:
        """Initialize hash manager with a cache file.
        
        Args:
            cache_file: Path to the JSON file storing hashes
        """
        self.cache_file = cache_file
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        self.hashes: Dict[str, Dict[str, str]] = self._load_hashes()
        self._modified = False
        self.session_id = datetime.utcnow().isoformat()  # Track current scraping session
    
    def _load_hashes(self) -> Dict[str, Dict[str, str]]:
        """Load existing hashes from cache file."""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r') as f:
                    data = json.load(f)
                    logger.info(
                        "loaded_hash_cache",
                        file=str(self.cache_file),
                        entries=len(data.get("hashes", {}))
                    )
                    return data.get("hashes", {})
            except (json.JSONDecodeError, IOError) as e:
                logger.error(
                    "failed_to_load_hash_cache",
                    file=str(self.cache_file),
                    error=str(e)
                )
        return {}
    
    def save(self) -> None:
        """Save hashes to cache file if modified."""
        if not self._modified:
            return
            
        try:
            data = {
                "metadata": {
                    "last_updated": datetime.utcnow().isoformat(),
                    "total_pages": len(self.hashes),
                    "session_id": self.session_id  # Store current session ID in metadata
                },
                "hashes": self.hashes
            }
            
            with open(self.cache_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            logger.info(
                "saved_hash_cache",
                file=str(self.cache_file),
                entries=len(self.hashes)
            )
            self._modified = False
        except IOError as e:
            logger.error(
                "failed_to_save_hash_cache",
                file=str(self.cache_file),
                error=str(e)
            )
    
    def get_content_hash(self, content: str) -> str:
        """Generate SHA-256 hash of content.
        
        Args:
            content: Content to hash
            
        Returns:
            Hex digest of the hash
        """
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    
    def has_changed(self, url: str, content: str, etag: Optional[str] = None) -> bool:
        """Check if content has changed since last scrape.
        
        Uses ETags for fast comparison when available, with hash as fallback.
        
        Args:
            url: URL of the content
            content: Current content
            etag: Optional ETag from HTTP response headers
            
        Returns:
            True if content has changed or is new
        """
        if url not in self.hashes:
            logger.debug("new_content", url=url)
            return True
        
        stored_data = self.hashes[url]
        
        # Primary: ETag comparison (fast, server-validated)
        if etag and "etag" in stored_data:
            if etag == stored_data["etag"]:
                logger.debug("content_unchanged_via_etag", url=url, etag=etag[:8])
                return False
            else:
                logger.debug(
                    "content_changed_via_etag",
                    url=url,
                    old_etag=stored_data["etag"][:8],
                    new_etag=etag[:8]
                )
                return True
        
        # Fallback: Hash comparison (reliable, content-based)
        current_hash = self.get_content_hash(content)
        stored_hash = stored_data.get("hash")
        
        if stored_hash != current_hash:
            logger.debug(
                "content_changed_via_hash",
                url=url,
                old_hash=stored_hash[:8] if stored_hash else "none",
                new_hash=current_hash[:8]
            )
            return True
        
        logger.debug("content_unchanged_via_hash", url=url)
        return False
    
    def get_etag(self, url: str) -> Optional[str]:
        """Get stored ETag for a URL to use in If-None-Match header.
        
        Args:
            url: URL to get ETag for
            
        Returns:
            Stored ETag or None if not available
        """
        if url in self.hashes:
            return self.hashes[url].get("etag")
        return None
    
    def update_hash(self, url: str, content: str, etag: Optional[str] = None, file_path: Optional[Path] = None) -> None:
        """Update hash and ETag for a URL.
        
        Args:
            url: URL of the content
            content: Content to hash
            etag: Optional ETag from HTTP response headers
            file_path: Optional file path where content is saved
        """
        current_hash = self.get_content_hash(content)
        entry = {
            "hash": current_hash,
            "last_checked": datetime.utcnow().isoformat(),
            "status": "unchanged" if url in self.hashes else "new",
            "session_id": self.session_id  # Track which session updated this
        }
        
        # Store ETag if provided for faster future comparisons
        if etag:
            entry["etag"] = etag
            
        # Store file path if provided for orphan detection
        if file_path:
            entry["file_path"] = str(file_path)
            
        self.hashes[url] = entry
        self._modified = True
        
        if etag:
            logger.debug("updated_hash_and_etag", url=url, hash=current_hash[:8], etag=etag[:8])
        else:
            logger.debug("updated_hash", url=url, hash=current_hash[:8])
    
    def mark_error(self, url: str, error: str) -> None:
        """Mark a URL as having an error.
        
        Args:
            url: URL that failed
            error: Error message
        """
        self.hashes[url] = {
            "hash": "",
            "last_checked": datetime.utcnow().isoformat(),
            "status": "error",
            "error": error
        }
        self._modified = True
        logger.debug("marked_error", url=url, error=error)
    
    def get_unchanged_urls(self) -> Set[str]:
        """Get URLs that haven't changed since last scrape.
        
        Returns:
            Set of URLs with unchanged content
        """
        return {
            url for url, data in self.hashes.items()
            if data.get("status") == "unchanged"
        }
    
    def get_error_urls(self) -> Set[str]:
        """Get URLs that had errors during last scrape.
        
        Returns:
            Set of URLs with errors
        """
        return {
            url for url, data in self.hashes.items()
            if data.get("status") == "error"
        }
    
    def get_statistics(self) -> Dict[str, int]:
        """Get hash cache statistics.
        
        Returns:
            Dictionary with statistics
        """
        statuses: Dict[str, int] = {}
        for data in self.hashes.values():
            status = data.get("status", "unknown")
            statuses[status] = statuses.get(status, 0) + 1
        
        return {
            "total": len(self.hashes),
            **statuses
        }
    
    def get_orphaned_files(self, framework_dir: Path) -> List[Path]:
        """Find markdown files that exist on disk but weren't updated in recent session.
        
        This is the core of orphan detection - files that exist but weren't touched
        in the most recent scraping session are likely removed from Apple's docs.
        
        Args:
            framework_dir: Directory to check for orphaned files
            
        Returns:
            List of orphaned file paths
        """
        if not framework_dir.exists():
            return []
            
        # Get all markdown files in the framework directory
        existing_files = set(framework_dir.rglob("*.md"))
        
        # Find the most recent session ID
        # First check metadata for the session ID from the last save
        latest_session_id = None
        
        # Try to load metadata to get the latest session ID
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r') as f:
                    full_data = json.load(f)
                    latest_session_id = full_data.get("metadata", {}).get("session_id")
            except:
                pass
        
        # If not in metadata, find from hash entries
        if not latest_session_id:
            for data in self.hashes.values():
                if "session_id" in data and data["session_id"]:
                    session_id = data["session_id"]
                    if latest_session_id is None or session_id > latest_session_id:
                        latest_session_id = session_id
        
        # If no session IDs found, all files are potentially orphaned
        if not latest_session_id:
            logger.warning("no_session_ids_found", framework_dir=str(framework_dir))
            return sorted(list(existing_files))
        
        # Get files that were touched in the latest session
        touched_files = set()
        
        # Create a mapping of lowercase paths to actual paths for case-insensitive matching
        existing_files_map = {str(f).lower(): f for f in existing_files}
        
        for data in self.hashes.values():
            if (data.get("session_id") == latest_session_id and 
                "file_path" in data):
                file_path_str = data["file_path"]
                
                # Try exact match first
                file_path = Path(file_path_str)
                if file_path.exists():
                    touched_files.add(file_path)
                else:
                    # Try case-insensitive match
                    lower_path = str(file_path).lower()
                    if lower_path in existing_files_map:
                        touched_files.add(existing_files_map[lower_path])
        
        # Orphans are files that exist but weren't touched in the latest session
        orphaned = existing_files - touched_files
        
        logger.info(
            "orphan_detection_results",
            framework_dir=str(framework_dir),
            existing_files=len(existing_files),
            touched_files=len(touched_files),
            orphaned_files=len(orphaned),
            latest_session_id=latest_session_id
        )
        
        return sorted(list(orphaned))