"""Content hash management for incremental updates."""

import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Final, Iterable, Optional, Set, List, Tuple

from scraper.utils.logger import get_logger

logger = get_logger(__name__)

# Per-entry run counters, kept on an entry's JSON-URL key only while > 0.
# update_hash, mark_error and keep_file carry them over; callers reset them explicitly.
COUNTER_FIELDS: Final = ("consecutive_failures", "consecutive_local_errors")

# Metadata keys every save rewrites; any other key is preserved as loaded.
RUN_METADATA_KEYS: Final = ("last_updated", "total_pages", "session_id")

# The mass-removal valve: more orphan candidates than this in one framework
# (or at least half its files) are confirmed on a second clean run first.
VALVE_MAX_ORPHANS: Final = 1000

# Present only on a hash file whose last save came from a framework run that
# may not have reached every page it has: its discovery didn't finish
# (interrupted, or raised), or a failure of ours blocked its cleanup (e.g. a
# failed fetch keeps the pages under it unreached). Its session_id, which only
# the pages reached carry (see HashManager.mark_partial).
PARTIAL_SESSION_KEY: Final = "partial_session"

# The longest file name, in bytes, on the filesystems we write to (ext4, APFS)
NAME_MAX: Final = 255


def valve_trips(orphans: int, files: int) -> bool:
    """Whether a framework's orphan candidates are a mass removal, held for confirmation.

    The candidates trip the valve when they are at least half of the
    framework's files or more than VALVE_MAX_ORPHANS. Nothing is deleted that
    run; the scrape's cleanup keeps them in metadata.pending_orphans and
    deletes the ones the next clean run finds orphaned again
    (confirm-then-delete).

    Args:
        orphans: How many orphan candidates the framework has
        files: How many .md files its docs dir has (the candidates included)
    """
    return orphans > 0 and (orphans * 2 >= files or orphans > VALVE_MAX_ORPHANS)


def read_hash_file(path: Path) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, Any]]:
    """A hash file's entries and metadata, as saved.

    A file with neither key loads as empty (e.g. HIG's flat dict).

    Raises:
        OSError: The file can't be read
        ValueError: It isn't UTF-8 JSON, or isn't shaped like a hash file
    """
    with open(path, 'r') as f:
        data = json.load(f)
    hashes = data.get("hashes", {}) if isinstance(data, dict) else None
    metadata = data.get("metadata", {}) if isinstance(data, dict) else None
    if not isinstance(hashes, dict) or not isinstance(metadata, dict):
        raise ValueError("not a hash file: expected an object whose 'hashes' and 'metadata' are objects")
    return hashes, metadata


def same_name_any_case(path: Path) -> List[Path]:
    """The entries of path's parent named like path in any casing, an exact match first.

    Framework identity is case-insensitive (Apple flips a framework's URL
    casing), so a framework's docs dir or hash file can carry another casing
    than the id a run uses. Empty when the parent can't be listed.
    """
    try:
        matches = [p for p in path.parent.iterdir() if p.name.lower() == path.name.lower()]
    except OSError:
        return []
    return sorted(matches, key=lambda p: (p.name != path.name, p.name))


def write_text_atomic(path: Path, text: str) -> None:
    """Write a file whole or not at all (UTF-8).

    The text goes to "<name>.tmp" next to the file, which then replaces it
    (os.replace), so a write that fails (e.g. a full disk) or is interrupted
    leaves the previous file as it was, and its temp file is removed (*.tmp
    is git-ignored). A name too long for the suffix gets a short temp name.
    The same as the other scrapers' (scripts/utilities/hash_utils.py
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


class HashManager:
    """Manage content hashes for incremental scraping."""
    
    def __init__(self, cache_file: Path, output_dir: Optional[Path] = None, resume_session: bool = False) -> None:
        """Initialize hash manager with a cache file.
        
        Args:
            cache_file: Path to the JSON file storing hashes
            output_dir: The dir of the files the entries record, if there is
                one (see save)
            resume_session: Keep the session the cache file holds (its
                session_id and last_updated) instead of starting one: for a
                manager reloaded after the scrape to prune entries or write
                pending_orphans, so old-way orphan detection still compares
                against the scrape's session
        """
        self.cache_file = cache_file
        self.output_dir = output_dir
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        # Why the cache file exists but couldn't be loaded (the manager then
        # starts empty), else None
        self.load_error: Optional[str] = None
        hashes, metadata = self._load_hashes()
        self.hashes: Dict[str, Dict[str, Any]] = hashes
        # Nested metadata (e.g. root_gone_runs, failure_storm_runs), without
        # the per-run keys save() writes itself
        self.metadata: Dict[str, Any] = {
            key: value for key, value in metadata.items() if key not in RUN_METADATA_KEYS
        }
        # A file that failed to load is replaced by the next save
        self._modified = self.load_error is not None
        # The session_id the cache file holds (its last save's), which old-way
        # orphan detection compares the entries against
        saved_session_id = metadata.get("session_id")
        self.saved_session_id: Optional[str] = saved_session_id if isinstance(saved_session_id, str) else None
        self.session_id = datetime.utcnow().isoformat()  # Track current scraping session
        # The last_updated a save writes; None writes the time of the save
        self._last_updated: Optional[str] = None
        if resume_session and self.saved_session_id:
            self.session_id = self.saved_session_id
            last_updated = metadata.get("last_updated")
            self._last_updated = last_updated if isinstance(last_updated, str) else None
        # URLs whose entries this session touched (update_hash, touch): the
        # in-memory record of what the run saw live, the new way of finding
        # orphans that D5's shadow mode compares with the session_id one
        self.touched: Set[str] = set()
    
    def _load_hashes(self) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, Any]]:
        """Load existing hashes and metadata from cache file.

        A file that can't be read, isn't UTF-8 JSON or isn't shaped like a
        hash file loads nothing and sets load_error.
        """
        if self.cache_file.exists():
            try:
                hashes, metadata = read_hash_file(self.cache_file)
                logger.info(
                    "loaded_hash_cache",
                    file=str(self.cache_file),
                    entries=len(hashes)
                )
                return hashes, metadata
            except (OSError, ValueError) as e:  # ValueError: not UTF-8, JSON or a hash file
                self.load_error = str(e)
                logger.error(
                    "failed_to_load_hash_cache",
                    file=str(self.cache_file),
                    error=str(e)
                )
        return {}, {}

    def _worth_saving(self) -> bool:
        """False when the manager holds nothing a later run needs.

        That is no entry with a file_path, no per-entry counter and no
        metadata beyond total_pages/root_gone_runs (and partial_session,
        which only describes the entries).
        """
        if any(key not in ("root_gone_runs", PARTIAL_SESSION_KEY) for key in self.metadata):
            return True
        return any(
            entry.get("file_path") or any(field in entry for field in COUNTER_FIELDS)
            for entry in self.hashes.values()
        )

    def _on_disk(self) -> bool:
        """Whether the cache file or the output dir exists (True if that can't be told).

        Either matches in any casing, as an output file does (on a lost hash
        file, the framework id takes technologies.json's casing, which may
        not be its docs dir's).
        """
        return any(
            path is not None and self._output_file_on_disk(str(path)) is not False
            for path in (self.cache_file, self.output_dir)
        )

    def save(self) -> bool:
        """Save hashes to cache file if modified.

        The data goes to a temp file that then replaces the cache file, so a
        failed write (e.g. a full disk) leaves the previous file whole.

        A manager holding nothing worth saving (see _worth_saving) writes
        nothing while neither the cache file nor the output dir exists: a
        removed framework that is still listed, whose root keeps returning
        404 after its dir and hash file were deleted, must not re-create its
        hash file every run. While either exists, every change is written:
        root_gone_runs counts on until the removal deletes both (also when no
        entry has a file_path left, e.g. the root's was the only one, or the
        hash file was lost next to its docs), a prune of the last files
        sticks, and a cache file that failed to load is replaced (left as it
        is, it would fail to load on every run).

        Returns:
            False if the save failed (logged; the manager stays modified),
            else True, including when there was nothing to save
        """
        if not self._modified:
            return True
        if not self._worth_saving() and not self._on_disk():
            logger.info("skipped_empty_hash_cache", file=str(self.cache_file))
            return True
            
        temp_file = self.cache_file.with_name(f"{self.cache_file.name}.tmp")
        try:
            data = {
                "metadata": {
                    "last_updated": self._last_updated or datetime.utcnow().isoformat(),
                    "total_pages": len(self.hashes),
                    "session_id": self.session_id,  # Store current session ID in metadata
                    **self.metadata
                },
                "hashes": self.hashes
            }
            
            with open(temp_file, 'w') as f:
                json.dump(data, f, indent=2)
            os.replace(temp_file, self.cache_file)
            
            logger.info(
                "saved_hash_cache",
                file=str(self.cache_file),
                entries=len(self.hashes)
            )
            self._modified = False
            self.saved_session_id = self.session_id
            return True
        except OSError as e:
            logger.error(
                "failed_to_save_hash_cache",
                file=str(self.cache_file),
                error=str(e)
            )
            try:
                temp_file.unlink(missing_ok=True)
            except OSError:
                pass
            return False
    
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

        # Self-heal: if the recorded output file is gone (e.g. deleted by
        # orphan cleanup while the hash entry survived), the page must be
        # re-scraped regardless of what ETags/hashes say.
        if self._output_file_missing(stored_data):
            logger.info(
                "output_file_missing_rescrape",
                url=url,
                file=stored_data.get("file_path"),
            )
            return True

        # Primary: ETag comparison (fast, server-validated)
        if etag and "etag" in stored_data:
            if etag == stored_data["etag"]:
                logger.debug("content_unchanged_via_etag", url=url, etag=etag[:8])
                return False
            else:
                # ETags differ — but Apple may regenerate ETags without changing content
                # (e.g., CDN redeployment). Fall through to hash comparison for certainty.
                logger.debug(
                    "etag_changed_checking_hash",
                    url=url,
                    old_etag=stored_data["etag"][:8],
                    new_etag=etag[:8]
                )

        # Content hash comparison (reliable, content-based)
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
            entry = self.hashes[url]
            # Never send If-None-Match when the output file is missing — a
            # 304 would short-circuit the re-scrape needed to restore it.
            if self._output_file_missing(entry):
                return None
            return entry.get("etag")
        return None

    @staticmethod
    def _output_file_missing(entry: Dict[str, Any]) -> bool:
        """True if the entry records an output file that is known not to exist.

        A file whose existence can't be told (see _output_file_on_disk) isn't
        missing: its entry and etag are kept, as for a file on disk.
        """
        file_path = entry.get("file_path")
        if not file_path:
            return False
        return HashManager._output_file_on_disk(file_path) is False

    @staticmethod
    def _output_file_on_disk(file_path: str) -> Optional[bool]:
        """Whether an output file (or dir) exists: True, False, or None if that can't be told.

        Falls back to a case-insensitive sibling check so this agrees with
        get_orphaned_files' view of existence when recorded casing drifts
        from on-disk casing (e.g. hash files shared across macOS/Linux).
        That check also answers for a path stat can't check: a name over the
        filesystem's limit is never in its dir's listing. None when its dir
        can't be checked or listed either (e.g. no permission on it), where
        a save fails too. Never raises: keep_file runs it for a page whose
        save just failed for such a reason.
        """
        path = Path(file_path)
        try:
            if path.exists():
                return True
        except OSError:
            pass
        parent = path.parent
        try:
            if not parent.is_dir():
                return False
            wanted = path.name.lower()
            return any(child.name.lower() == wanted for child in parent.iterdir())
        except OSError:
            return None

    def remove(self, url: str) -> bool:
        """Remove a single entry, persisting the removal on next save.

        Returns True if the entry existed.
        """
        if url in self.hashes:
            del self.hashes[url]
            self._modified = True
            return True
        return False

    def prune_missing_files(self) -> int:
        """Remove entries whose recorded output file no longer exists.

        Called after orphan cleanup deletes files, so entries don't outlive
        their files and accumulate forever.

        Returns:
            Number of entries removed.
        """
        dead = [url for url, entry in self.hashes.items() if self._output_file_missing(entry)]
        for url in dead:
            del self.hashes[url]
        if dead:
            self._modified = True
        return len(dead)

    def update_hash(self, url: str, content: str, etag: Optional[str] = None, file_path: Optional[Path] = None) -> None:
        """Update hash and ETag for a URL.
        
        Args:
            url: URL of the content
            content: Content to hash
            etag: Optional ETag from HTTP response headers
            file_path: Optional file path where content is saved
        """
        current_hash = self.get_content_hash(content)
        entry: Dict[str, Any] = {
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

        self.hashes[url] = self._with_counters(url, entry)
        self.touched.add(url)
        self._modified = True

        if etag:
            logger.debug("updated_hash_and_etag", url=url, hash=current_hash[:8], etag=etag[:8])
        else:
            logger.debug("updated_hash", url=url, hash=current_hash[:8])
    
    def mark_error(self, url: str, error: str) -> None:
        """Mark a URL as having an error.
        
        The entry loses its file_path, session_id and etag but keeps its
        run counters, so a failure count survives the error entry.

        Args:
            url: URL that failed
            error: Error message
        """
        entry: Dict[str, Any] = {
            "hash": "",
            "last_checked": datetime.utcnow().isoformat(),
            "status": "error",
            "error": error
        }
        self.hashes[url] = self._with_counters(url, entry)
        self._modified = True
        logger.debug("marked_error", url=url, error=error)

    def _with_counters(self, url: str, entry: Dict[str, Any]) -> Dict[str, Any]:
        """Carry the URL's current run counters over to its replacement entry."""
        old = self.hashes.get(url, {})
        for field in COUNTER_FIELDS:
            if field in old:
                entry[field] = old[field]
        return entry

    def touch(self, url: str) -> None:
        """Record that this run saw the URL's page live, leaving its content fields alone.

        Refreshes session_id and last_checked, and adds the URL to the
        touched set, so orphan detection (both ways) keeps the entry's file.
        """
        entry = self.hashes[url]
        entry["session_id"] = self.session_id
        entry["last_checked"] = datetime.utcnow().isoformat()
        self.touched.add(url)
        self._modified = True

    def keep_file(self, url: str, file_path: Path) -> bool:
        """Record a live page's file that is on disk but no live entry records.

        For a page this run saw live but couldn't save, whose entry lost its
        file_path (e.g. D8 marked both keys in a run whose cleanup didn't
        delete the file): the entry records the file again and is touched, so
        orphan detection keeps it. Its hash is unknown and it has no etag, so
        the next run refetches and converts the page again. Run counters
        carry over.

        Returns:
            True if the file is on disk and is now recorded; False, changing
            nothing, if it isn't (or that can't be told).
        """
        if self._output_file_on_disk(str(file_path)) is not True:
            return False
        entry: Dict[str, Any] = {
            "hash": "",
            "status": "unchanged" if url in self.hashes else "new",
            "file_path": str(file_path),
        }
        self.hashes[url] = self._with_counters(url, entry)
        self.touch(url)
        logger.debug("kept_file", url=url, file=str(file_path))
        return True

    def get_counter(self, url: str, field: str) -> int:
        """A run counter of the URL's entry (0 when absent)."""
        return int(self.hashes.get(url, {}).get(field, 0))

    def set_counter(self, url: str, field: str, value: int) -> None:
        """Set a run counter on the URL's entry; it is stored only while > 0."""
        entry = self.hashes.get(url)
        if entry is None:
            if value > 0:
                raise KeyError(f"no hash entry for {url}")
            return
        if value > 0:
            if entry.get(field) != value:
                entry[field] = value
                self._modified = True
        elif field in entry:
            del entry[field]
            self._modified = True

    def get_metadata(self, key: str, default: Any = None) -> Any:
        """A preserved metadata value."""
        return self.metadata.get(key, default)

    def set_metadata(self, key: str, value: Any) -> None:
        """Set a preserved metadata value; a falsy value (0, None, empty) removes it.

        Every change marks the manager modified, so save() writes it even on
        a run that changed nothing else.
        """
        if value:
            if self.metadata.get(key) != value:
                self.metadata[key] = value
                self._modified = True
        elif key in self.metadata:
            del self.metadata[key]
            self._modified = True

    def mark_partial(self) -> None:
        """Mark this session's save as one from a framework run that may not
        have reached every page it has (metadata.partial_session = its
        session_id): its discovery didn't finish, or its cleanup is blocked.

        Only the pages it reached carry the session, so old-way orphan
        detection against it would take every page it didn't reach for an
        orphan: the standalone orphan tools skip a framework so marked, as the
        scrape's own cleanup skips a blocked one, until a run that finishes
        its discovery unblocked drops the key. Set only when the save writes
        anyway (the manager is modified): otherwise the file stays as its
        last save left it.
        """
        if self._modified:
            self.set_metadata(PARTIAL_SESSION_KEY, self.session_id)

    @property
    def partial(self) -> bool:
        """The hash file's last save came from a framework run that may not
        have reached every page it has (see mark_partial)."""
        return PARTIAL_SESSION_KEY in self.metadata

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
    
    def touched_this_session(self) -> bool:
        """Whether any entry received this session's session_id (the zero-touched guard's test)."""
        return any(entry.get("session_id") == self.session_id for entry in self.hashes.values())

    @staticmethod
    def framework_files(framework_dir: Path) -> Set[Path]:
        """The .md files under a framework's docs dir (none if it doesn't exist)."""
        if not framework_dir.is_dir():
            return set()
        return set(framework_dir.rglob("*.md"))

    @staticmethod
    def _unrecorded(existing_files: Set[Path], recorded: Iterable[str]) -> Set[Path]:
        """The existing files that no recorded path names.

        A recorded path names its file exactly, else in any casing (recorded
        casing can drift from the disk's, e.g. hash files shared across macOS
        and Linux). Files are matched by name against the listing, never by
        stat: on a case-insensitive filesystem a recorded path in another
        casing exists, yet isn't the path the listing gives, so its live file
        would look orphaned. A path that matches only other casings, of
        several files, keeps all of them.
        """
        by_lower: Dict[str, List[Path]] = {}
        for existing in existing_files:
            by_lower.setdefault(str(existing).lower(), []).append(existing)
        kept: Set[Path] = set()
        for file_path in recorded:
            path = Path(file_path)
            if path in existing_files:
                kept.add(path)
            else:
                kept.update(by_lower.get(str(path).lower(), ()))
        return existing_files - kept

    def get_orphaned_files(self, framework_dir: Path, existing_files: Optional[Set[Path]] = None) -> List[Path]:
        """Find markdown files that exist on disk but weren't updated in recent session.
        
        This is the core of orphan detection - files that exist but weren't touched
        in the most recent scraping session are likely removed from Apple's docs.
        The old way (D5): the most recent session is the one the cache file
        holds (its last save's).
        
        Args:
            framework_dir: Directory to check for orphaned files
            existing_files: The .md files under it, if already listed
            
        Returns:
            List of orphaned file paths
        """
        if existing_files is None:
            if not framework_dir.exists():
                return []
            existing_files = self.framework_files(framework_dir)

        # The session ID from the last save, else the newest one an entry holds
        latest_session_id = self.saved_session_id
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

        # Orphans are files that exist but weren't touched in the latest session
        orphaned = self._unrecorded(existing_files, (
            data["file_path"]
            for data in self.hashes.values()
            if data.get("session_id") == latest_session_id and data.get("file_path")
        ))

        logger.info(
            "orphan_detection_results",
            framework_dir=str(framework_dir),
            existing_files=len(existing_files),
            touched_files=len(existing_files) - len(orphaned),
            orphaned_files=len(orphaned),
            latest_session_id=latest_session_id
        )

        return sorted(list(orphaned))

    def get_untouched_files(self, framework_dir: Path, existing_files: Optional[Set[Path]] = None) -> List[Path]:
        """Markdown files on disk that no entry this session touched records.

        The new way of finding orphans (D5): from the in-memory touched set,
        with no session_id read back. Valid only in the process that scraped
        the framework; a manager loaded later touched nothing.

        Args:
            framework_dir: Directory to check for orphaned files
            existing_files: The .md files under it, if already listed
        """
        if existing_files is None:
            existing_files = self.framework_files(framework_dir)
        return sorted(self._unrecorded(existing_files, (
            self.hashes[url]["file_path"]
            for url in self.touched
            if self.hashes.get(url, {}).get("file_path")
        )))