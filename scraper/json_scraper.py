"""JSON-based Apple documentation scraper that uses Apple's data endpoints."""

import asyncio
import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Deque, Dict, Final, List, Literal, Optional, Set
from urllib.parse import urlparse

from scraper.base import NOT_MODIFIED, BaseAppleScraper, FetchFailed
from scraper.config import Config
from scraper.utils.hash_manager import same_name_any_case, write_text_atomic
from scraper.utils.logger import get_logger
from scraper.utils.markdown_converter import AppleDocMarkdownConverter

logger = get_logger(__name__)

# 404/410: Apple removed the page. A removal, never a block.
GONE_STATUSES: Final = (404, 410)

# A 200 whose body is not JSON is treated as a transient fetch failure.
INVALID_JSON: Final = "invalid json"

# A page's fetch failure (D8) or local error counts once per framework run; at
# this many consecutive runs it stops blocking cleanup and flags the run.
PERSISTENT_FAILURE_RUNS: Final = 3

# More fetch failures in one run than max(5, 1% of the framework's pages) is a
# failure storm: they block but aren't counted, unless the storm lasts
# FAILURE_STORM_RUNS consecutive runs.
FAILURE_STORM_MIN: Final = 5
FAILURE_STORM_SHARE: Final = 0.01
FAILURE_STORM_RUNS: Final = 3

# How a page's fetch failed this run (see _handle_fetch_failure):
# previously_good: a page with a live entry failed; it is kept and touched.
# after_304: a 304 proved the page live, then its discovery refetch failed.
# never_good: a transient failure on a URL with no live entry.
FailureKind = Literal["previously_good", "after_304", "never_good"]


@dataclass(frozen=True)
class PageFetchFailure:
    """A page fetch failure of this run that counts toward D8."""

    kind: FailureKind
    failure: FetchFailed


@dataclass
class OrphanScan:
    """A framework's orphan candidates, computed right after its hash file was saved.

    The end-of-run cleanup works from these, so neither the scraper nor its
    hash manager (every entry of the framework) is kept until then.

    Attributes:
        framework_dir: The framework's docs dir (its output dir, or that dir
            in another casing)
        hash_file: The framework's hash file
        files: How many .md files the docs dir holds
        orphans: The orphan candidates: the .md files no entry this run
            touched records (HashManager.get_untouched_files)
        pending_orphans: metadata.pending_orphans as the run's save left it:
            the candidates an earlier clean run held for confirmation
    """

    framework_dir: Path
    hash_file: Path
    files: int
    orphans: List[Path]
    pending_orphans: List[str]


@dataclass
class FrameworkOutcome:
    """What a framework run means for orphan cleanup and the run's exit code.

    Attributes:
        framework_id: The framework's id, as its output dir and hash file use it
        blocks: Why orphan cleanup must skip the framework this run (our own
            failed requests or errors), reason -> the URLs or messages
        persistent_fetch_failures: URLs whose fetch failed for the
            PERSISTENT_FAILURE_RUNS-th consecutive run (or more); they no
            longer block cleanup but flag the run
        persistent_local_errors: URLs whose convert/save failed for the
            PERSISTENT_FAILURE_RUNS-th consecutive run (or more); same
        root_fetch_failed: The root failed with something other than 404/410,
            or with a 404/410 after it answered 200/304 in this run (our
            failure: it blocks cleanup and never reaches D8)
        root_gone_runs: Consecutive runs the root returned 404/410, if it did
            this run and never answered 200/304 (else 0); cleanup skips the
            framework, which isn't our failure, until the end-of-run pass
            deletes it at 2
        failure_storm: Too many fetch failures this run (see FAILURE_STORM_*)
        raised: The error, if the framework's scrape raised
        stats: The scraper's stats
        orphan_scan: The framework's orphan candidates, for a framework the
            end-of-run cleanup may clean (see scan_orphans)
    """

    framework_id: str
    blocks: Dict[str, List[str]] = field(default_factory=dict)
    persistent_fetch_failures: List[str] = field(default_factory=list)
    persistent_local_errors: List[str] = field(default_factory=list)
    root_fetch_failed: bool = False
    root_gone_runs: int = 0
    failure_storm: bool = False
    raised: Optional[str] = None
    stats: Dict[str, Any] = field(default_factory=dict)
    orphan_scan: Optional[OrphanScan] = None

    def block(self, reason: str, detail: str) -> None:
        """Block this framework's orphan cleanup for this run."""
        details = self.blocks.setdefault(reason, [])
        if detail not in details:
            details.append(detail)

    @property
    def blocked(self) -> bool:
        """Cleanup is blocked by a failure of ours (an error for the run)."""
        return bool(self.blocks) or self.raised is not None

    @property
    def skip_cleanup(self) -> bool:
        """Orphan cleanup must leave this framework alone this run."""
        return self.blocked or self.root_gone_runs > 0


class AppleJSONDocumentationScraper(BaseAppleScraper):
    """Scraper that uses Apple's JSON data endpoints instead of HTML pages."""
    
    # Base URL for JSON data
    JSON_BASE_URL = "https://developer.apple.com/tutorials/data/documentation"
    
    def __init__(self, framework_id: str, framework_name: Optional[str] = None, 
                 include_cross_refs: bool = False) -> None:
        """Initialize JSON-based scraper.
        
        Args:
            framework_id: Framework identifier (e.g., 'swiftui', 'uikit')
            framework_name: Human-readable name (defaults to framework_id)
            include_cross_refs: Whether to include cross-framework references
        """
        super().__init__(
            framework_id=framework_id,
            framework_name=framework_name or framework_id.replace('-', ' ').title()
        )
        self.markdown_converter = AppleDocMarkdownConverter(self.output_dir)
        self.processed_urls: Set[str] = set()
        self.include_cross_refs = include_cross_refs
        self.cross_framework_refs: Dict[str, Set[str]] = {}  # Track cross-framework references

        # Failure policy state for this run, applied once by scrape_framework
        self.root_json_url = f"{self.JSON_BASE_URL}/{self.framework_id}.json"
        self.outcome = FrameworkOutcome(framework_id=self.framework_id)
        self._fetch_failures: Dict[str, PageFetchFailure] = {}  # JSON URL -> D8 failure
        self._fetch_ok: Set[str] = set()  # a 200, or a 304 whose discovery refetch succeeded
        self._gone: Set[str] = set()  # answered 404/410: Apple removed the page
        self._local_errors: Dict[str, str] = {}  # JSON URL -> convert/save error
        self._saved_ok: Set[str] = set()  # pages processed without a local error
        self._root_ok = False  # the root answered 200 or 304
        self._root_gone = False  # the root answered 404/410
        # Previously good pages, the storm threshold's base when a run's
        # failures cut discovery short
        self._known_pages = sum(
            1 for url, entry in self.hash_manager.hashes.items()
            if url.startswith(self.JSON_BASE_URL) and entry.get('file_path')
        )
        if self.hash_manager.load_error is not None:
            # The hash file exists but loaded nothing, so this run can't tell
            # the pages we have from new ones. This run's save replaces the
            # file, so the block lasts one run.
            self.outcome.block("hash_load_failed", str(self.hash_manager.cache_file))
    
    def _convert_doc_url_to_json_url(self, doc_url: str) -> str:
        """Convert a documentation URL to its JSON data URL.
        
        Args:
            doc_url: Documentation URL like https://developer.apple.com/documentation/swiftui/text
            
        Returns:
            JSON URL like https://developer.apple.com/tutorials/data/documentation/swiftui/text.json
        """
        parsed = urlparse(doc_url)
        path = parsed.path
        
        # Remove /documentation/ prefix
        if path.startswith('/documentation/'):
            path = path[len('/documentation/'):]
        
        # Add .json extension if not present
        if not path.endswith('.json'):
            path += '.json'
        
        return f"{self.JSON_BASE_URL}/{path}"
    
    def _convert_json_url_to_doc_url(self, json_url: str) -> str:
        """Convert a JSON data URL back to documentation URL.
        
        Args:
            json_url: JSON URL
            
        Returns:
            Documentation URL
        """
        # Extract path from JSON URL
        path = json_url.replace(self.JSON_BASE_URL + '/', '')
        
        # Remove .json extension
        if path.endswith('.json'):
            path = path[:-5]
        
        return f"https://developer.apple.com/documentation/{path}"
    
    async def scrape_framework(self) -> Dict[str, Any]:
        """Override base scrape_framework to use streaming approach."""
        self.stats["start_time"] = time.time()
        # Being scraped means technologies.json lists the framework: its count
        # of unlisted runs (cleanup_removed_frameworks.py) starts over, also
        # when that script's own fetch failed this run. Saved by __aexit__.
        self.hash_manager.set_metadata("unlisted_runs", 0)

        await self.discover_and_scrape_streaming()
        self._apply_failure_policy()
        
        self.stats["end_time"] = time.time()
        self.stats["duration"] = self.stats["end_time"] - self.stats["start_time"]
        self.outcome.stats = self.stats
        
        # Save cross-framework references if tracking was enabled
        if self.include_cross_refs:
            self.save_cross_framework_summary()
        
        logger.info(
            "framework_scrape_complete",
            framework=self.framework_name,
            stats=self.stats
        )
        
        return self.stats
    
    async def discover_and_scrape_streaming(self) -> None:
        """Discover URLs and scrape them immediately for real-time feedback."""
        logger.info("starting_streaming_discovery_and_scrape", framework=self.framework_name)
        
        # Start with the framework's main JSON file
        framework_json_url = self.root_json_url
        
        # Scrape the main framework page first
        main_doc_url = f"https://developer.apple.com/documentation/{self.framework_id}"
        await self._scrape_and_save_url(main_doc_url)
        
        # Use iterative approach instead of recursion to avoid stack overflow
        try:
            await self._discover_and_scrape_iterative([framework_json_url])
        finally:
            # Logged even if discovery raised
            logger.info(
                "framework_scraping_finalized",
                framework=self.framework_name,
                pages_scraped=self.stats['pages_scraped'],
                pages_skipped=self.stats['pages_skipped'],
                pages_failed=self.stats['pages_failed']
            )
        
    async def _scrape_and_save_url(self, url: str) -> bool:
        """Scrape a single URL and save it immediately (via scrape_page)."""
        try:
            return await self.scrape_page(url) is not None
        except Exception as e:
            # Raised outside the page's own convert/save step: block, don't count
            logger.error("failed_to_scrape_url", url=url, error=str(e))
            self.outcome.block("exception", url)
            return False
    
    async def _discover_and_scrape_iterative(self, initial_json_urls) -> None:
        """Iterative version of discovery to avoid recursion depth issues with optimized ETag usage."""
        from collections import deque

        # Queue of URLs to process
        if isinstance(initial_json_urls, str):
            initial_json_urls = [initial_json_urls]
        url_queue = deque(initial_json_urls)

        logger.info(f"starting_iterative_discovery", initial_urls=len(initial_json_urls))
        
        # Track queue size for monitoring
        max_queue_size = 0
        processed_count = 0
        
        # Worker pool: process up to INTRA_FRAMEWORK_CONCURRENCY pages of this
        # framework at once (see todo-concurrency.md). asyncio is single-threaded,
        # so shared state (queue, processed_urls, stats, hash_manager) is safe;
        # URLs are marked processed before any await, preventing duplicates.
        in_flight: Set[asyncio.Task] = set()

        while url_queue or in_flight:
            # Launch tasks up to the concurrency limit
            while url_queue and len(in_flight) < Config.INTRA_FRAMEWORK_CONCURRENCY:
                max_queue_size = max(max_queue_size, len(url_queue))
                json_url = url_queue.popleft()
                if json_url in self.processed_urls:
                    continue
                self.processed_urls.add(json_url)
                processed_count += 1
                if processed_count % 100 == 0:
                    logger.info(
                        "iterative_discovery_progress",
                        processed=processed_count,
                        queue_size=len(url_queue),
                        max_queue_size=max_queue_size,
                    )
                in_flight.add(asyncio.create_task(
                    self._process_queued_url(json_url, url_queue)
                ))

            if not in_flight:
                continue  # queue contained only already-processed URLs

            done, in_flight = await asyncio.wait(in_flight, return_when=asyncio.FIRST_COMPLETED)
            for task in done:
                exc = task.exception()
                if exc:
                    logger.error("worker_task_error", error=str(exc))
                    self.outcome.block("worker_exception", str(exc))

        logger.info(
            "iterative_discovery_complete",
            total_processed=processed_count,
            max_queue_size=max_queue_size,
            framework=self.framework_name,
        )

    async def _process_queued_url(self, json_url: str, url_queue: Deque[str]) -> None:
        """Process a single discovered URL: fetch, enqueue children, save if changed."""
        try:
            # OPTIMIZED: Fetch JSON with ETag support for discovery
            result = await self.fetch_page_with_etag(json_url, use_etag=True)
            if isinstance(result, FetchFailed):
                # Never treated as a 304, and never refetched for discovery
                self._handle_fetch_failure(json_url, result)
                return

            if result is NOT_MODIFIED:
                # Got 304 Not Modified - content unchanged
                if self._is_root(json_url):
                    self._root_ok = True
                doc_url = self._convert_json_url_to_doc_url(json_url)
                logger.debug("content_unchanged_skip_scrape", json_url=json_url, doc_url=doc_url)
                self.stats['pages_skipped'] += 1

                # Touch the entry for orphan detection even though content
                # unchanged. PRESERVE the recorded file path: paths can
                # be data-dependent (kind-suffix disambiguation uses symbol_kind),
                # so recomputing from the URL alone with empty data would record
                # a wrong path and get the real file orphan-deleted.
                if json_url in self.hash_manager.hashes:
                    if not self.hash_manager.hashes[json_url].get('file_path'):
                        self.hash_manager.set_file_path(json_url, self._get_organized_file_path(doc_url, {}))
                    self.hash_manager.touch(json_url)

                # IMPORTANT: Still need to discover child pages!
                # The main page might be unchanged but children could be new/updated.
                if json_url in self.hash_manager.hashes:
                    # We've seen this page before - need to rediscover its children
                    # Fetch without ETag to get content for discovery
                    discovery_result = await self.fetch_page_with_etag(json_url, use_etag=False)
                    if discovery_result is NOT_MODIFIED:
                        # No body to read the links from: a failed refetch
                        discovery_result = FetchFailed(
                            status=304, error="HTTP 304 on discovery refetch", transient=True
                        )
                    elif not isinstance(discovery_result, FetchFailed):
                        try:
                            data = json.loads(discovery_result[0])
                        except json.JSONDecodeError:
                            logger.warning("failed_to_parse_json_for_rediscovery", url=json_url)
                            discovery_result = self._invalid_json_failure()
                        else:
                            # Extract URLs for discovery
                            new_urls = self._extract_urls_from_json_data(data)
                            self._enqueue(new_urls, url_queue)
                            logger.debug("rediscovered_child_urls", parent=json_url, count=len(new_urls))
                            self._fetch_ok.add(json_url)
                    if isinstance(discovery_result, FetchFailed):
                        # The 304 proved the page live; only its links are missing
                        self._handle_fetch_failure(json_url, discovery_result, after_304=True)
                return

            # Got 200 OK - content is new or changed
            response_text, etag = result

            # Parse JSON for discovery
            try:
                data = json.loads(response_text)
            except json.JSONDecodeError:
                logger.warning("failed_to_parse_json", url=json_url)
                self._handle_fetch_failure(json_url, self._invalid_json_failure())
                return
            self._fetch_ok.add(json_url)
            if self._is_root(json_url):
                self._root_ok = True

            # Links first: enqueue the children before, and independently of,
            # the save, so a convert or save error can never orphan them
            self._enqueue(self._extract_urls_from_json_data(data), url_queue)

            # Process and save this page
            doc_url = self._convert_json_url_to_doc_url(json_url)
            saved = False
            file_path: Optional[Path] = None

            # Only this inner try counts as a local error (the links are queued)
            try:
                # Check if we need to process based on content hash
                if self.hash_manager.has_changed(json_url, response_text, etag):
                    # Extract and save page data
                    page_data = self._extract_from_json(data, doc_url)
                    if page_data:
                        # Calculate file path for hash updates
                        file_path = self._get_organized_file_path(doc_url, page_data)

                        # Write the file first, then both hash keys
                        saved = await self._save_and_record(
                            json_url, doc_url, page_data, file_path, response_text, etag
                        )
                else:
                    # Content hasn't changed according to hash
                    logger.debug("content_unchanged_via_hash", url=doc_url)
                    self.stats['pages_skipped'] += 1

                    # Still need to update hash with file path for orphan detection.
                    # Reuse the stored file path, as the 304 branch does; compute
                    # one only when none is stored, and then write the file first.
                    stored_path = self.hash_manager.hashes[json_url].get('file_path')
                    if stored_path:
                        file_path = Path(stored_path)
                        # Touch both keys and record the new etag
                        self.hash_manager.update_hash(json_url, response_text, etag, file_path)
                        self.hash_manager.update_hash(doc_url, response_text, etag, file_path)
                    else:
                        page_data = self._extract_from_json(data, doc_url)
                        file_path = self._get_organized_file_path(doc_url, page_data)
                        await self._save_and_record(
                            json_url, doc_url, page_data, file_path, response_text, etag
                        )
            except Exception as e:
                self._handle_local_error(json_url, e, file_path, data)
                return
            self._saved_ok.add(json_url)

            if saved:
                self.stats['pages_scraped'] += 1

                # Log progress every 10 files
                if self.stats['pages_scraped'] % 10 == 0:
                    logger.info(
                        "scraping_progress",
                        scraped=self.stats['pages_scraped'],
                        skipped=self.stats['pages_skipped'],
                        failed=self.stats['pages_failed'],
                        queue_size=len(url_queue)
                    )

        except Exception as e:
            # Raised before the page's links were enqueued: block, don't count
            logger.error("error_processing_url", url=json_url, error=str(e))
            self.outcome.block("exception", json_url)

    def _enqueue(self, urls: List[str], url_queue: Deque[str]) -> None:
        """Queue the URLs this run hasn't processed yet."""
        for new_url in urls:
            if new_url not in self.processed_urls:
                url_queue.append(new_url)

    def _is_root(self, json_url: str) -> bool:
        """True for the framework root page's JSON URL."""
        return json_url.lower() == self.root_json_url.lower()

    @staticmethod
    def _is_previously_good(entry: Optional[Dict[str, Any]]) -> bool:
        """A live entry: it records a file and isn't an error entry."""
        return bool(entry and entry.get('file_path') and entry.get('status') != 'error')

    async def _save_and_record(
        self,
        json_url: str,
        doc_url: str,
        page_data: Dict[str, Any],
        file_path: Path,
        content: str,
        etag: Optional[str],
    ) -> bool:
        """Write the page's file, then record it on both hash keys.

        Returns:
            True if the file was written. A file that is never written (an
            unsafe path) gets an error entry instead, so no key records it.
        """
        if not await self.save_page_data(doc_url, page_data, file_path):
            self.hash_manager.mark_error(json_url, "unsafe file path")
            return False
        self.hash_manager.update_hash(json_url, content, etag, file_path)
        self.hash_manager.update_hash(doc_url, content, etag, file_path)
        return True

    def _handle_fetch_failure(self, json_url: str, failure: FetchFailed, after_304: bool = False) -> None:
        """Apply the failure policy to a fetch that gave no usable page.

        - 404/410: Apple removed the page. Its JSON-URL key becomes an error
          entry, so its file (and any subtree no longer reachable) is orphaned
          and cleaned. Never blocks.
        - Any other failure of a live page, or of a discovery refetch after a
          304: keep the entry and touch it, so its file isn't orphaned; it
          blocks cleanup and counts toward D8.
        - A URL with no live entry: an error entry. A transient failure blocks
          and counts (it may be the new parent of a moved page); a 4xx doesn't.
          A URL that no entry records but whose file is on disk, though, is a
          page we have whose entry was lost (e.g. its hash file failed to
          load): it is handled as a live page.
        - The root never reaches D8: any failure other than 404/410 keeps it
          and blocks cleanup, every run until it recovers. So does a 404/410
          after the root answered 200/304 in this run: the root is live, and
          this fetch, which reads its links, failed.

        Counting is done once per run by _apply_failure_policy.

        Args:
            json_url: The page's JSON URL
            failure: The failed fetch
            after_304: The failure is the discovery refetch after a 304
        """
        hm = self.hash_manager
        if failure.status in GONE_STATUSES:
            if not (self._is_root(json_url) and self._root_ok):
                hm.mark_error(json_url, failure.error)
                logger.info("page_gone", url=json_url, status=failure.status)
                self._gone.add(json_url)
                if self._is_root(json_url):
                    self._root_gone = True
                return
            logger.warning("root_fetch_conflict", url=json_url, status=failure.status)

        kind: FailureKind
        if after_304:
            # The 304 already touched the entry
            kind = "after_304"
        elif self._is_previously_good(hm.hashes.get(json_url)):
            hm.touch(json_url)
            kind = "previously_good"
        elif self._kept_unrecorded_file(json_url):
            kind = "previously_good"
        else:
            hm.mark_error(json_url, failure.error)
            kind = "never_good"

        if self._is_root(json_url):
            logger.error("root_fetch_failed", url=json_url, status=failure.status, error=failure.error)
            self.outcome.root_fetch_failed = True
            self.outcome.block("root_fetch_failed", json_url)
            return
        if kind == "never_good" and not failure.transient:
            # A never-good 4xx: nothing to keep, so it doesn't block (many
            # frameworks link the same 4xx URLs every run); pages reachable
            # only through it are cleaned
            return
        logger.warning(
            "page_fetch_failed", url=json_url, kind=kind, status=failure.status, error=failure.error
        )
        self._fetch_failures[json_url] = PageFetchFailure(kind, failure)

    def _handle_local_error(
        self,
        json_url: str,
        error: Exception,
        file_path: Optional[Path] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> None:
        """A convert or save error of ours: keep the page, block cleanup, count it.

        Never deletes: the page answered 200, so its file is kept. A live
        entry keeps its hash, etag and file_path (the old etag makes the next
        run refetch) and is touched, so its file is never orphaned. Without
        one, the page's file can still be on disk with no live JSON-URL key
        recording it: its JSON-URL key answered 404/410 (e.g. the root's first
        fetch this run), or D8 marked both keys, in a run whose cleanup didn't
        delete the file, or the hash file was lost. Then the JSON-URL key
        records that file again (HashManager.keep_file), so it is kept.
        Otherwise the URL gets an error entry, so its count persists. Never
        counts toward D8; counted once per run by _apply_failure_policy.

        Args:
            json_url: The page's JSON URL
            error: The convert or save error
            file_path: The path this run computed for the page's file, if it got that far
            json_data: The page's parsed JSON
        """
        logger.error("page_save_failed", url=json_url, error=str(error))
        hm = self.hash_manager
        if self._is_previously_good(hm.hashes.get(json_url)):
            hm.touch(json_url)
        else:
            on_disk = self._page_file_path(json_url, file_path, json_data)
            if on_disk is None or not hm.keep_file(json_url, on_disk):
                hm.mark_error(json_url, f"local error: {error}")
        self._local_errors[json_url] = str(error)

    def _page_file_path(
        self, json_url: str, file_path: Optional[Path], json_data: Optional[Dict[str, Any]]
    ) -> Optional[Path]:
        """Where the file of a page without a live JSON-URL entry would be.

        Its doc-URL key's recorded path if that key is live; else the path
        this run computed; else, for an error raised before that, the one its
        URL and its symbol kind give (the only extracted field the path
        depends on; the root's path needs only its URL). None if that fails
        too.
        """
        doc_url = self._convert_json_url_to_doc_url(json_url)
        doc_entry = self.hash_manager.hashes.get(doc_url)
        if doc_entry is not None and self._is_previously_good(doc_entry):
            return Path(doc_entry['file_path'])
        if file_path is not None:
            return file_path
        try:
            metadata = (json_data or {}).get('metadata', {})
            return self._get_organized_file_path(doc_url, {'symbol_kind': metadata.get('symbolKind') or ''})
        except Exception as e:
            logger.warning("page_file_path_failed", url=json_url, error=str(e))
            return None

    def _kept_unrecorded_file(self, json_url: str) -> bool:
        """Keep a failed page that no entry records but whose file is on disk.

        The file shows we have the page; only its entry was lost, by a
        failure of ours or an outside cause: the hash file failed to load
        (this run, where nothing loaded, so every page looks new), an earlier
        run couldn't record the page (a run whose hash file failed to load
        saves only the pages it reached; a failed save keeps the previous
        file, which lacks the pages saved in that run), or the hash file was
        deleted. Its JSON-URL key records that file again
        (HashManager.keep_file), so this run's save records a live page, and
        the failure counts toward D8 as for any page we have. A URL that has
        an entry is judged by it: an error entry (from a 404/410, a D8, an
        earlier never-good failure or a local error) stays never-good. The
        path comes from the URL alone (there is no JSON to read the symbol
        kind from), so a file named by its kind isn't found.

        Returns:
            True if the file was found and is now recorded
        """
        if json_url in self.hash_manager.hashes:
            return False
        file_path = self._page_file_path(json_url, None, None)
        return file_path is not None and self.hash_manager.keep_file(json_url, file_path)

    def _apply_failure_policy(self) -> None:
        """Count this run's failures once, and decide whether cleanup is blocked.

        Runs once per framework run, after discovery. Updates the per-entry
        consecutive_failures / consecutive_local_errors counters and the
        root_gone_runs / failure_storm_runs metadata, and fills self.outcome.
        """
        hm = self.hash_manager
        outcome = self.outcome

        # Root: a 404/410 counts toward root_gone_runs once per run, any 200/304 resets it
        if self._root_ok:
            if self._root_gone:
                # A 404/410, then a 200/304 on the fetch that reads the root's
                # links: the root is live (had that fetch failed, it blocked
                # as root_fetch_failed)
                logger.warning("root_fetch_conflict", framework=self.framework_name, url=self.root_json_url)
            hm.set_metadata("root_gone_runs", 0)
        elif self._root_gone:
            runs = int(hm.get_metadata("root_gone_runs", 0)) + 1
            hm.set_metadata("root_gone_runs", runs)
            outcome.root_gone_runs = runs
            if runs == 1:
                logger.warning("root_gone_pending", framework=self.framework_name, root_gone_runs=runs)
            else:
                logger.warning("root_gone", framework=self.framework_name, root_gone_runs=runs)

        # Failure storm: too many fetch failures at once aren't counted
        pages = max(self._known_pages, len(self.processed_urls))
        limit = max(FAILURE_STORM_MIN, FAILURE_STORM_SHARE * pages)
        counting = True
        if len(self._fetch_failures) > limit:
            storm_runs = int(hm.get_metadata("failure_storm_runs", 0)) + 1
            hm.set_metadata("failure_storm_runs", storm_runs)
            counting = storm_runs >= FAILURE_STORM_RUNS
            outcome.failure_storm = True
            logger.warning(
                "failure_storm",
                framework=self.framework_name,
                failures=len(self._fetch_failures),
                limit=limit,
                failure_storm_runs=storm_runs,
                counting=counting,
            )
        else:
            hm.set_metadata("failure_storm_runs", 0)

        # Resets. The D8 count is of failed runs in a row: a 200, a 304 whose
        # refetch succeeded, a 404/410 (a removal, not a failure) or a run
        # that never fetched the URL (no page reached this run links to it)
        # ends the streak, so a stale count can't lift the never-good block
        # on our first new failure. A page processed without a local error
        # resets that count.
        unfetched = {
            url for url, entry in hm.hashes.items()
            if "consecutive_failures" in entry and url not in self.processed_urls
        }
        for url in (self._fetch_ok | self._gone | unfetched) - self._fetch_failures.keys():
            hm.set_counter(url, "consecutive_failures", 0)
        for url in self._saved_ok - self._local_errors.keys():
            hm.set_counter(url, "consecutive_local_errors", 0)

        for url, page_failure in self._fetch_failures.items():
            runs = hm.get_counter(url, "consecutive_failures")
            if counting:
                runs += 1
                hm.set_counter(url, "consecutive_failures", runs)
            if runs < PERSISTENT_FAILURE_RUNS:
                outcome.block("fetch_failed", url)
                continue
            # No longer protected: it stops blocking, and flags the run
            logger.error(
                "persistent_fetch_failure",
                url=url,
                kind=page_failure.kind,
                runs=runs,
                error=page_failure.failure.error,
            )
            outcome.persistent_fetch_failures.append(url)
            if page_failure.kind == "previously_good":
                # D8: treat the page as removed. Both keys become error
                # entries (keeping the count), so its file and any subtree no
                # longer reachable are orphaned and cleaned in this run. After
                # a 304 the page is live and stays touched, so its file is kept.
                hm.mark_error(url, page_failure.failure.error)
                hm.mark_error(self._convert_json_url_to_doc_url(url), page_failure.failure.error)

        for url, error in self._local_errors.items():
            runs = hm.get_counter(url, "consecutive_local_errors") + 1
            hm.set_counter(url, "consecutive_local_errors", runs)
            if runs < PERSISTENT_FAILURE_RUNS:
                outcome.block("local_error", url)
            else:
                # Stop blocking; the entry stays touched, so its file is kept
                logger.error("persistent_local_error", url=url, runs=runs, error=error)
                outcome.persistent_local_errors.append(url)

        if outcome.blocks:
            logger.warning(
                "cleanup_blocked",
                framework=self.framework_name,
                reasons={reason: len(details) for reason, details in outcome.blocks.items()},
            )

    def scan_orphans(self) -> None:
        """Find this framework's orphan candidates, right after its hash file was saved.

        Fills self.outcome for the end-of-run cleanup, so neither the scraper
        nor its hash manager has to be kept until then:
        - A root that answered 404/410 this run: no cleanup (the end-of-run
          pass deletes the framework at 2 runs).
        - Zero-touched guard: a framework where this run touched no entry is
          never cleaned. It logs framework_zero_touched and blocks, as a
          failure of ours (every file it has would look orphaned).
        - The candidates are the .md files no entry this run touched records
          (the in-memory touched set). A blocked or raised framework keeps
          none.
        """
        outcome = self.outcome
        if outcome.root_gone_runs:
            return
        hm = self.hash_manager
        if not outcome.blocked and not hm.touched:
            logger.error("framework_zero_touched", framework=self.framework_name, framework_id=self.framework_id)
            outcome.block("zero_touched", self.framework_id)
        if outcome.blocked:
            return

        # The output dir, or that dir in another casing
        framework_dir = next(
            (path for path in same_name_any_case(self.output_dir) if path.is_dir()), self.output_dir
        )
        existing = hm.framework_files(framework_dir)
        pending = hm.get_metadata("pending_orphans")
        outcome.orphan_scan = OrphanScan(
            framework_dir=framework_dir,
            hash_file=hm.cache_file,
            files=len(existing),
            orphans=hm.get_untouched_files(framework_dir, existing),
            pending_orphans=[path for path in pending if isinstance(path, str)] if isinstance(pending, list) else [],
        )

    def _extract_urls_from_json_data(self, data: Dict[str, Any]) -> List[str]:
        """Extract all URLs from JSON data without recursing."""
        urls = []
        
        # Extract related documentation from various sections
        sections_to_check = [
            'topicSections',
            'relationshipsSections', 
            'seeAlsoSections',
            'diffAvailability',
            'variants'
        ]
        
        for section_name in sections_to_check:
            if section_name in data and isinstance(data[section_name], list):
                logger.debug(f"Extracting URLs from {section_name} with {len(data[section_name])} items")
                
                for section in data[section_name]:
                    if 'identifiers' in section:
                        identifiers = section.get('identifiers', [])
                        section_title = section.get('title', 'Unknown')
                        logger.info(f"Found section '{section_title}' with {len(identifiers)} identifiers")
                        
                        # Convert identifiers to URLs
                        for identifier in identifiers:
                            if identifier.startswith('doc://'):
                                # Check if it's for current framework
                                identifier_lower = identifier.lower()
                                framework_check = f"com.apple.{self.framework_id.lower()}"
                                is_current_framework = (framework_check in identifier_lower or 
                                                      f"/{self.framework_id.lower()}/" in identifier_lower or 
                                                      f"/{self.framework_id}/" in identifier)
                                
                                if is_current_framework:
                                    json_url = self._convert_identifier_to_json_url(identifier)
                                    if json_url:
                                        urls.append(json_url)
                                elif self.include_cross_refs:
                                    # Track cross-framework reference
                                    self._track_cross_framework_ref(identifier)
        
        return urls
    
    @staticmethod
    def _escape_dot_path_segments(path: str) -> str:
        """Escape path segments starting with '.' by adding apostrophe prefix.

        Apple's server requires path segments starting with dots (like the Swift
        range operators '...' and '..<') to be prefixed with an apostrophe in URLs.
        E.g. identifier path 'comparable/...(_:_:)' -> URL path 'comparable/\'...(_:_:)'
        """
        segments = path.split('/')
        escaped = []
        for seg in segments:
            if seg.startswith('.'):
                escaped.append(f"'{seg}")
            else:
                escaped.append(seg)
        return '/'.join(escaped)

    def _convert_identifier_to_json_url(self, identifier: str) -> Optional[str]:
        """Convert a doc:// identifier to a JSON URL."""
        try:
            # Remove doc:// prefix and /documentation/ if present
            path = identifier.replace('doc://', '')
            if '/documentation/' in path:
                # Split on /documentation/ and take the second part
                parts = path.split('/documentation/', 1)
                if len(parts) == 2:
                    path = parts[1]
                else:
                    # Fallback
                    path = path.replace('/documentation/', '')

            # Convert to lowercase and ensure it starts with framework_id
            path_lower = path.lower()

            # If it starts with framework_id/, keep it. Otherwise prepend framework_id
            if not path_lower.startswith(f"{self.framework_id.lower()}/"):
                path_lower = f"{self.framework_id.lower()}/{path_lower}"

            # Escape path segments starting with dots (e.g. range operators)
            path_lower = self._escape_dot_path_segments(path_lower)

            return f"{self.JSON_BASE_URL}/{path_lower}.json"
            
        except Exception as e:
            logger.error(f"Error converting identifier {identifier}: {e}")
            return None
    
    def _slugify(self, text: str) -> str:
        """Convert text to URL-safe folder name."""
        import re
        # Convert to lowercase and replace spaces/special chars with hyphens
        slug = re.sub(r'[^\w\s-]', '', text.lower())
        slug = re.sub(r'[\s_-]+', '-', slug)
        return slug.strip('-')
    
    async def scrape_page(self, url: str) -> Optional[Dict[str, Any]]:
        """Fetch the framework root page and save it if it changed.
        
        Writes the file first, then both hash keys. A failed fetch is never
        treated as a 304: it goes through the failure policy.
        
        Args:
            url: Documentation URL to scrape
            
        Returns:
            Extracted data if the page was saved, None if failed/unchanged
        """
        # Convert to JSON URL
        json_url = self._convert_doc_url_to_json_url(url)
        
        # Check if we have an ETag for this JSON URL
        stored_etag = self.hash_manager.get_etag(json_url)
        
        # Fetch JSON data with ETag support
        result = await self.fetch_page_with_etag(json_url)
        if isinstance(result, FetchFailed):
            self._handle_fetch_failure(json_url, result)
            return None
        if result is NOT_MODIFIED:
            # 304 Not Modified (content unchanged)
            if self._is_root(json_url):
                self._root_ok = True
            if stored_etag:
                # 304 response - content unchanged - touch the entries
                logger.debug("content_unchanged_via_etag", url=url, json_url=json_url)
                
                # Reuse the stored file_path (skip expensive recalculation)
                existing = self.hash_manager.hashes.get(json_url) or self.hash_manager.hashes.get(url) or {}
                file_path = Path(existing['file_path']) if existing.get('file_path') else self._get_organized_file_path(url, {})
                
                # Touch both URLs' entries, so orphan detection keeps the file,
                # and record the file on both. Only a missing file_path or a
                # missing key (created with the stored etag) changes an entry,
                # so a 304 alone leaves the hash file as it is.
                for key in (json_url, url):
                    if key not in self.hash_manager.hashes:
                        self.hash_manager.hashes[key] = {'etag': stored_etag}
                    self.hash_manager.touch(key)
                    self.hash_manager.set_file_path(key, file_path)
                
                self.stats["pages_skipped"] += 1
            return None
        
        response_text, etag = result
        
        try:
            json_data = json.loads(response_text)
        except json.JSONDecodeError as e:
            logger.error("json_parse_error", url=json_url, error=str(e))
            self._handle_fetch_failure(json_url, self._invalid_json_failure())
            return None
        self._fetch_ok.add(json_url)
        if self._is_root(json_url):
            self._root_ok = True
        
        # Check hash to avoid re-processing unchanged content
        if not self.hash_manager.has_changed(json_url, response_text, etag) and not self.hash_manager.has_changed(url, response_text, etag):
            logger.debug("content_unchanged", url=url)
            
            # Content unchanged, but both keys are still touched for orphan detection
            try:
                page_data = self._extract_from_json(json_data, url)
                if page_data:
                    file_path = self._get_organized_file_path(url, page_data)
                    # Touch both keys and record the new etag
                    self.hash_manager.update_hash(json_url, response_text, etag, file_path)
                    self.hash_manager.update_hash(url, response_text, etag, file_path)
            except Exception as e:
                logger.warning("failed_to_touch_unchanged_root", url=url, error=str(e))
            
            self.stats["pages_skipped"] += 1
            return None
        
        # Basic validation
        if not self._validate_json_structure(json_data):
            logger.warning("invalid_json_structure", url=json_url)
            self.stats["pages_failed"] += 1
            return None
        
        # Extract, convert and save, then record both hash keys. Only this
        # try counts as a local error: the root's links are enqueued when it
        # is processed again as the first queued URL.
        try:
            data = self._extract_from_json(json_data, url)
            
            if not data:
                logger.warning("no_data_extracted", url=url)
                self.stats["pages_failed"] += 1
                return None
                
            # Calculate file path for hash updates
            file_path = self._get_organized_file_path(url, data)
            
            # Write the file first, then both hash keys
            saved = await self._save_and_record(json_url, url, data, file_path, response_text, etag)
        except Exception as e:
            self._handle_local_error(json_url, e)
            return None
        self._saved_ok.add(json_url)
        if not saved:
            return None
        self.stats["pages_scraped"] += 1
        return data
    
    def _invalid_json_failure(self) -> FetchFailed:
        """A 200 whose body isn't JSON, as the transient failure it is treated as."""
        self.stats["pages_failed"] += 1
        return FetchFailed(status=200, error=INVALID_JSON, transient=True)
    
    def _extract_from_json(self, json_data: Dict[str, Any], doc_url: str) -> Dict[str, Any]:
        """Extract structured data from Apple's JSON format.
        
        Args:
            json_data: Parsed JSON data
            doc_url: Original documentation URL
            
        Returns:
            Extracted data in our format
        """
        # Store current URL for relative path calculation
        self._current_scraping_url = doc_url
        
        data = {
            'source_url': doc_url,
            'framework': self.framework_name,
            'framework_id': self.framework_id
        }
        
        # Extract comprehensive metadata
        metadata = json_data.get('metadata', {})
        data['title'] = metadata.get('title', 'Untitled')
        
        # Extract additional metadata fields
        data['external_id'] = metadata.get('externalID', '')
        data['symbol_kind'] = metadata.get('symbolKind') or ''  # JSON null -> ''
        data['navigator_title'] = metadata.get('navigatorTitle', '')
        data['role_heading'] = metadata.get('roleHeading', '')
        data['required'] = metadata.get('required', False)
        data['modules'] = metadata.get('modules', [])
        
        # Extract symbol fragments for detailed signature information
        if 'fragments' in metadata:
            fragments = metadata['fragments']
            data['fragments'] = [
                {
                    'kind': frag.get('kind', ''),
                    'text': frag.get('text', ''),
                    'preciseIdentifier': frag.get('preciseIdentifier', '')
                }
                for frag in fragments
            ]
        
        # Extract references for later resolution
        references = json_data.get('references', {})
        
        # Extract abstract/brief description
        abstract = json_data.get('abstract', [])
        if abstract:
            data['brief_description'] = self._resolve_inline_content(abstract, references)
        
        # Extract comprehensive availability information
        platforms = metadata.get('platforms', [])
        data['availability'] = []
        for p in platforms:
            availability_info = {
                'platform': p.get('name', 'Unknown'),
                'version': f"{p.get('introducedAt', '?')}+",
                'deprecated': p.get('deprecated', False),
                'beta': p.get('beta', False)
            }
            
            # Add deprecation details if available
            if p.get('deprecatedAt'):
                availability_info['deprecated_at'] = p['deprecatedAt']
            if p.get('deprecationMessage'):
                availability_info['deprecation_message'] = p['deprecationMessage']
            
            # Add beta information
            if p.get('isBeta', False):
                availability_info['beta'] = True
            
            # Add unconditionally deprecated flag
            if p.get('unconditionallyDeprecated', False):
                availability_info['unconditionally_deprecated'] = True
            
            data['availability'].append(availability_info)
        
        # Extract diff availability for version changes
        if 'diffAvailability' in json_data:
            diff_availability = json_data['diffAvailability']
            data['diff_availability'] = {
                'major': diff_availability.get('major', []),
                'minor': diff_availability.get('minor', [])
            }
        
        # Extract declaration
        data['declaration'] = {}
        primary_content = json_data.get('primaryContentSections', [])
        for section in primary_content:
            if section.get('kind') == 'declarations':
                for declaration in section.get('declarations', []):
                    lang = 'swift'  # Default
                    for platform in declaration.get('platforms', []):
                        if platform == 'swift':
                            lang = 'swift'
                    
                    # Reconstruct code from tokens with proper formatting
                    tokens = declaration.get('tokens', [])
                    code = self._format_declaration_from_tokens(tokens)
                    if code:
                        data['declaration'][lang] = code
        
        # Extract all content sections comprehensively
        content_sections = self._extract_all_content_sections(primary_content, references)
        data.update(content_sections)
        
        # Extract parameters
        parameters = []
        for section in primary_content:
            if section.get('kind') == 'parameters':
                for param in section.get('parameters', []):
                    param_data = {
                        'name': param.get('name', ''),
                        'description': ''
                    }
                    # Extract description from content (may have multiple paragraphs, termLists, etc.)
                    content = param.get('content', [])
                    desc_parts = self._process_content_items(content, references)
                    param_data['description'] = ' '.join(desc_parts)
                    
                    parameters.append(param_data)
        
        data['parameters'] = parameters
        
        # Extract topics with complete signatures and descriptions from references
        topics = []
        for section in json_data.get('topicSections', []):
            topic = {
                'title': section.get('title', ''),
                'items': []
            }
            for identifier in section.get('identifiers', []):
                # Look up the identifier in references to get complete information
                if identifier in references:
                    ref_data = references[identifier]
                    
                    # Get the full title (which includes complete signature for methods)
                    full_title = ref_data.get('title', identifier.split('/')[-1])
                    
                    # Try to get an even more complete signature from fragments if available
                    if 'fragments' in ref_data:
                        fragments = ref_data['fragments']
                        # Reconstruct full signature from fragments
                        signature_parts = []
                        for frag in fragments:
                            text = frag.get('text', '')
                            if text:
                                signature_parts.append(text)
                        if signature_parts:
                            reconstructed_signature = ''.join(signature_parts)
                            # Use the reconstructed signature if it's more complete than title
                            if len(reconstructed_signature) > len(full_title):
                                full_title = reconstructed_signature
                    
                    url_path = ref_data.get('url', '')
                    if url_path:
                        url = f"https://developer.apple.com{url_path}"
                    else:
                        # Fallback URL construction
                        if identifier.startswith('doc://com.apple.'):
                            parts = identifier.split('/documentation/')
                            if len(parts) == 2:
                                path = parts[1]
                                url = f"https://developer.apple.com/documentation/{path}"
                            else:
                                url = identifier
                        else:
                            url = identifier
                    
                    # Extract description/abstract from reference
                    description = ""
                    if 'abstract' in ref_data:
                        abstract_content = ref_data['abstract']
                        description = self._resolve_inline_content(abstract_content, references)
                    
                    topic['items'].append({
                        'name': full_title,
                        'url': url,
                        'description': description
                    })
                else:
                    # Fallback for identifiers not in references
                    name = identifier.split('/')[-1] if '/' in identifier else identifier
                    if identifier.startswith('doc://com.apple.'):
                        parts = identifier.split('/documentation/')
                        if len(parts) == 2:
                            path = parts[1]
                            url = f"https://developer.apple.com/documentation/{path}"
                        else:
                            url = identifier
                    else:
                        url = identifier
                    topic['items'].append({
                        'name': name,
                        'url': url,
                        'description': ''
                    })
            
            if topic['items']:
                topics.append(topic)
        
        data['topics'] = topics
        
        # Extract see also with complete signatures
        see_also = []
        for section in json_data.get('seeAlsoSections', []):
            for identifier in section.get('identifiers', []):
                if identifier in references:
                    ref_data = references[identifier]
                    # Get the full title (complete signature)
                    full_title = ref_data.get('title', identifier.split('/')[-1])
                    
                    # Try to get more complete signature from fragments
                    if 'fragments' in ref_data:
                        fragments = ref_data['fragments']
                        signature_parts = []
                        for frag in fragments:
                            text = frag.get('text', '')
                            if text:
                                signature_parts.append(text)
                        if signature_parts:
                            reconstructed_signature = ''.join(signature_parts)
                            if len(reconstructed_signature) > len(full_title):
                                full_title = reconstructed_signature
                    
                    url_path = ref_data.get('url', '')
                    if url_path:
                        url = f"https://developer.apple.com{url_path}"
                    else:
                        # Fallback URL construction
                        if identifier.startswith('doc://com.apple.'):
                            parts = identifier.split('/documentation/')
                            if len(parts) == 2:
                                path = parts[1]
                                url = f"https://developer.apple.com/documentation/{path}"
                            else:
                                url = identifier
                        else:
                            url = identifier
                    
                    # Extract description from abstract
                    description = ""
                    if 'abstract' in ref_data:
                        abstract_content = ref_data['abstract']
                        description = self._resolve_inline_content(abstract_content, references)
                    
                    see_also.append({
                        'title': full_title,
                        'url': url,
                        'description': description
                    })
                else:
                    # Fallback for identifiers not in references
                    name = identifier.split('/')[-1] if '/' in identifier else identifier
                    if identifier.startswith('doc://com.apple.'):
                        parts = identifier.split('/documentation/')
                        if len(parts) == 2:
                            path = parts[1]
                            url = f"https://developer.apple.com/documentation/{path}"
                        else:
                            url = identifier
                    else:
                        url = identifier
                    see_also.append({
                        'title': name,
                        'url': url,
                        'description': ''
                    })
        
        data['see_also'] = see_also
        
        # Extract relationships (Inherited By, Conforming Types, etc.)
        relationships = []
        for section in json_data.get('relationshipsSections', []):
            relationship = {
                'title': section.get('title', ''),
                'type': section.get('type', ''),
                'items': []
            }
            for identifier in section.get('identifiers', []):
                if identifier in references:
                    ref_data = references[identifier]
                    name = ref_data.get('title', identifier.split('/')[-1])
                    url_path = ref_data.get('url', '')
                    if url_path:
                        url = f"https://developer.apple.com{url_path}"
                    else:
                        url = identifier
                    relationship['items'].append({
                        'name': name,
                        'url': url
                    })
            if relationship['items']:
                relationships.append(relationship)
        
        data['relationships'] = relationships
        
        # Extract mentions (related documentation links)
        mentions = []
        for section in primary_content:
            if section.get('kind') == 'mentions':
                mention_items = section.get('mentions', [])
                for mention in mention_items:
                    if mention in references:
                        ref_data = references[mention]
                        mentions.append({
                            'title': ref_data.get('title', mention.split('/')[-1]),
                            'url': f"https://developer.apple.com{ref_data.get('url', '')}"
                        })
        
        data['mentions'] = mentions
        
        # Extract content headings for better organization
        content_headings = []
        for section in primary_content:
            if section.get('kind') == 'content':
                content_items = section.get('content', [])
                for item in content_items:
                    if item.get('type') == 'heading':
                        level = item.get('level', 1)
                        heading_text = self._resolve_inline_content(item.get('inlineContent', []), references)
                        if heading_text.strip():
                            content_headings.append({
                                'level': level,
                                'text': heading_text
                            })
        
        data['content_headings'] = content_headings
        
        # Extract variants (different language implementations)
        if 'variants' in json_data:
            variants = json_data['variants']
            data['variants'] = [
                {
                    'traits': variant.get('traits', []),
                    'paths': variant.get('paths', [])
                }
                for variant in variants
            ]
        
        # Extract hierarchy information for navigation
        if 'hierarchy' in json_data:
            hierarchy = json_data['hierarchy']
            data['hierarchy'] = {
                'paths': hierarchy.get('paths', []),
                'modules': hierarchy.get('modules', [])
            }
        
        return data
    
    async def save_page_data(self, url: str, data: Dict[str, Any], file_path: Optional[Path] = None) -> bool:
        """Save extracted data as markdown with organized folder structure.
        
        Args:
            url: Source URL
            data: Extracted data
            file_path: Optional pre-calculated file path
            
        Returns:
            True if the file was written, False if its path was unsafe
        """
        # Convert to markdown
        markdown_content = self.markdown_converter.convert_page(data)
        
        # Determine organized file path if not provided
        if file_path is None:
            file_path = self._get_organized_file_path(url, data)

        # Containment guard: never write outside the framework output dir
        # (mirrors the MLX scraper's is_safe_path; traversal is neutralized
        # upstream, this is defense in depth at the write sink).
        resolved = file_path.resolve()
        output_root = self.output_dir.resolve()
        if resolved != output_root and output_root not in resolved.parents:
            logger.error("unsafe_file_path_skipped", url=url, path=str(file_path))
            return False

        # Creates the framework's output dir too, on its first file
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save markdown file (whole or not at all: a failed write keeps the old doc)
        write_text_atomic(file_path, markdown_content)
        
        # Log the save for real-time feedback in Finder
        try:
            relative_path = file_path.relative_to(Path.cwd())
        except ValueError:
            relative_path = file_path
        
        logger.info(
            "file_saved",
            file=str(relative_path),
            size=len(markdown_content),
            url=url
        )
        return True
    
    def _get_organized_file_path(self, url: str, data: Dict[str, Any]) -> Path:
        """Generate organized file path based on URL hierarchy (mirrors Apple's structure).
        
        Args:
            url: Source URL
            data: Extracted data containing title and other metadata
            
        Returns:
            Path object for the organized file location following URL structure
        """
        # Match the framework prefix case-insensitively: Apple emits URL
        # casing inconsistently over time ('XCTest' vs 'xctest'), but the
        # URL space itself is case-insensitive.
        prefix = f'https://developer.apple.com/documentation/{self.framework_id}'.lower()
        url_path = None
        if url.lower().startswith(prefix):
            rest = url[len(prefix):]
            if rest == '' or rest.startswith('/'):
                url_path = rest.lstrip('/')
        
        # Fallback if no pattern matches
        if url_path is None:
            logger.warning("failed_to_parse_url_path", url=url, framework_id=self.framework_id)
            # Use full URL as fallback (this was causing the https: folders)
            safe_url = url.replace('https://', '').replace('http://', '').replace('/', '-')
            return self.output_dir / f"{safe_url}.md"
        
        if not url_path:
            # Main framework page: use framework_id to match URL structure
            return self.output_dir / f"{self.framework_id}.md"
        
        # Split path into segments
        path_segments = url_path.split('/')
        
        # Always use the full URL path structure, just with lowercase and clean filenames
        if len(path_segments) == 1:
            # Single segment: watchkit/enabling-background-sessions.md
            filename = self._create_clean_filename(path_segments[0], data)
            if filename.lower() == self.framework_id.lower():
                # A symbol named like its framework (e.g. the XCTest class in
                # the XCTest framework) would collide case-insensitively with
                # the framework root file on case-insensitive filesystems.
                kind = self._slugify(data.get('symbol_kind', '')) or 'page'
                filename = f"{filename}-{kind}"
            return self.output_dir / f"{filename}.md"
        else:
            # Multiple segments: watchkit/wkapplication/shared.md
            # All segments except last become folders
            folder_path = Path(*[segment.lower() for segment in path_segments[:-1]])
            filename = self._create_clean_filename(path_segments[-1], data)
            return self.output_dir / folder_path / f"{filename}.md"
    
    # Operator symbols to readable names for filenames
    _OPERATOR_NAMES = {
        '==': 'equal',
        '!=': 'notequal',
        '<': 'lessthan',
        '>': 'greaterthan',
        '<=': 'lessthanorequal',
        '>=': 'greaterthanorequal',
        '+': 'plus',
        '-': 'minus',
        '*': 'multiply',
        '/': 'divide',
        '%': 'modulo',
        '&': 'bitwiseand',
        '|': 'bitwiseor',
        '^': 'bitwisexor',
        '~': 'bitwisenot',
        '<<': 'leftshift',
        '>>': 'rightshift',
        '&&': 'logicaland',
        '||': 'logicalor',
        '!': 'logicalnot',
        '...': 'closedrange',
        '..<': 'halfopen',
        '??': 'nilcoalescing',
    }

    def _create_clean_filename(self, api_name: str, data: Dict[str, Any]) -> str:
        """Create a clean, readable filename."""
        # Start with the API name
        base_name = api_name

        # For methods/operators, clean up parameter syntax but preserve important info
        if '(' in base_name and ')' in base_name:
            # Extract operator before parentheses (e.g., "!=(_:_:)" -> "!=")
            op_part = base_name[:base_name.index('(')]
            if op_part in self._OPERATOR_NAMES:
                base_name = self._OPERATOR_NAMES[op_part]
            else:
                # Convert init?(rawValue: Int) -> init-rawvalue
                # Convert shared() -> shared
                base_name = base_name.replace('?', '').replace('!', '')
                base_name = base_name.replace('(', '-').replace(')', '')
                base_name = base_name.replace(':', '').replace(' ', '').replace(',', '-')

        # Remove other special characters and convert to lowercase with hyphens
        clean_name = self._slugify(base_name)

        # Ensure it doesn't start with numbers or special chars
        if clean_name and clean_name[0].isdigit():
            clean_name = f"api-{clean_name}"

        return clean_name or 'unknown'
    
    def _convert_apple_url_to_local_path(self, apple_url: str, current_page_url: str = None) -> str:
        """Convert an Apple documentation URL to a local markdown file path.
        
        Args:
            apple_url: Apple documentation URL
            current_page_url: URL of the current page (to calculate relative paths)
            
        Returns:
            Relative path to local markdown file
        """
        # Check if it's an Apple documentation URL
        if not apple_url.startswith('https://developer.apple.com/documentation/'):
            return apple_url
        
        # Extract the path after /documentation/
        url_path = apple_url.replace('https://developer.apple.com/documentation/', '')
        
        # Split into components
        parts = url_path.split('/')
        
        # Check if it's in the same framework
        if parts[0].lower() == self.framework_id.lower():
            # Same framework - create relative path
            if len(parts) == 1:
                # Main framework page
                return f"{self.framework_id}.md"
            
            # For current page context, we need to know where we are
            if current_page_url and hasattr(self, '_current_scraping_url'):
                current_path = self._current_scraping_url.replace('https://developer.apple.com/documentation/', '')
                current_parts = current_path.split('/')
                current_depth = len(current_parts) - 1
                
                if len(parts) == 2 and current_depth == 1:
                    # Same level - just the filename
                    return f"{parts[1]}.md"
                elif len(parts) == 2 and current_depth > 1:
                    # Need to go up directories
                    up_dirs = '../' * (current_depth - 1)
                    return f"{up_dirs}{parts[1]}.md"
                else:
                    # More complex nested structure
                    # Calculate relative path between current location and target
                    target_depth = len(parts) - 1
                    if current_depth == target_depth and '/'.join(current_parts[:-1]) == '/'.join(parts[:-1]):
                        # Same directory
                        return f"{parts[-1]}.md"
                    else:
                        # Different directory - go up to common ancestor
                        up_dirs = '../' * (current_depth - 1)
                        # Then navigate to target
                        if target_depth > 1:
                            down_path = '/'.join(parts[1:-1])
                            return f"{up_dirs}{down_path}/{parts[-1]}.md"
                        else:
                            return f"{up_dirs}{parts[-1]}.md"
            else:
                # Fallback - simple logic
                if len(parts) == 2:
                    return f"{parts[1]}.md"
                else:
                    # For nested paths, include the subdirectory
                    return f"{'/'.join(parts[1:])}.md"
        else:
            # Different framework - keep Apple URL
            return apple_url
    
    def _format_declaration_from_tokens(self, tokens: List[Dict[str, Any]]) -> str:
        """Format declaration tokens with proper Swift formatting.
        
        Args:
            tokens: List of token dictionaries from Apple's JSON
            
        Returns:
            Formatted declaration string
        """
        if not tokens:
            return ""
        
        parts = []
        
        # Check if declaration starts with attributes
        has_leading_attributes = False
        attribute_text = []
        i = 0
        
        # Collect all leading attributes
        while i < len(tokens) and tokens[i].get('kind') == 'attribute':
            attribute_text.append(tokens[i].get('text', ''))
            i += 1
            has_leading_attributes = True
        
        # If we have attributes, add them on their own line
        if has_leading_attributes:
            parts.append(''.join(attribute_text))
            # Skip whitespace after attributes
            while i < len(tokens) and tokens[i].get('text', '').strip() == '':
                i += 1
        
        # Add the rest of the declaration
        remaining = []
        for j in range(i, len(tokens)):
            remaining.append(tokens[j].get('text', ''))
        
        if remaining:
            parts.append(''.join(remaining))
        
        # Join lines
        result = '\n'.join(parts)
        
        # Additional formatting for long function signatures
        # If it's a function with multiple parameters and > 100 chars, format it
        if 'func ' in result and result.count(',') >= 2 and len(result) > 100:
            # This is a heuristic - in practice Apple's formatting is more complex
            # For now, keep single line to match most common cases
            pass
        
        return result
    
    def _validate_json_structure(self, json_data: Dict[str, Any]) -> bool:
        """Validate basic JSON structure from Apple API.
        
        Args:
            json_data: Parsed JSON to validate
            
        Returns:
            True if structure is valid
        """
        # Basic validation - check for required top-level fields
        required_fields = ['metadata', 'identifier']
        if not all(field in json_data for field in required_fields):
            return False
        
        # Check metadata structure
        metadata = json_data.get('metadata', {})
        if not isinstance(metadata, dict):
            return False
        
        return True
    
    def _resolve_inline_content(self, inline_content: List[Dict[str, Any]], references: Dict[str, Any]) -> str:
        """Resolve inline content with proper reference resolution.
        
        Args:
            inline_content: List of inline content items from Apple's JSON
            references: References dictionary for resolving identifiers
            
        Returns:
            Resolved text content
        """
        resolved_parts = []
        
        for item in inline_content:
            item_type = item.get('type', '')
            
            if item_type == 'text':
                resolved_parts.append(item.get('text', ''))
            elif item_type == 'reference':
                # Resolve the reference to its actual name and create a proper link
                identifier = item.get('identifier', '')
                if identifier in references:
                    ref_data = references[identifier]
                    title = ref_data.get('title', identifier.split('/')[-1])
                    
                    # Get the URL for the reference
                    url_path = ref_data.get('url', '')
                    if url_path:
                        # Convert Apple URL to local markdown path
                        apple_url = f"https://developer.apple.com{url_path}"
                        local_path = self._convert_apple_url_to_local_path(apple_url)
                        # Create a markdown link to local file
                        resolved_parts.append(f"[`{title}`]({local_path})")
                    else:
                        # Fallback to just code formatting if no URL
                        resolved_parts.append(f"`{title}`")
                else:
                    # Fallback to the last part of the identifier
                    fallback = identifier.split('/')[-1] if '/' in identifier else identifier
                    resolved_parts.append(f"`{fallback}`")
            elif item_type == 'codeVoice':
                resolved_parts.append(f"`{item.get('code', '')}`")
            elif item_type == 'emphasis':
                # Italic text - recursively resolve nested content
                inner = self._resolve_inline_content(item.get('inlineContent', []), references)
                resolved_parts.append(f"*{inner}*")
            elif item_type == 'strong':
                # Bold text - recursively resolve nested content
                inner = self._resolve_inline_content(item.get('inlineContent', []), references)
                resolved_parts.append(f"**{inner}**")
            elif item_type == 'image':
                # Handle inline images
                image_content = self._process_image(item, references)
                resolved_parts.append(image_content)
            else:
                # Handle other types as plain text
                resolved_parts.append(item.get('text', ''))
        
        return ''.join(resolved_parts)
    
    def _extract_all_content_sections(self, primary_content: List[Dict[str, Any]], references: Dict[str, Any]) -> Dict[str, Any]:
        """Extract all content from primaryContentSections comprehensively.
        
        Args:
            primary_content: List of primary content sections
            references: References for resolving inline content
            
        Returns:
            Dictionary of extracted content
        """
        extracted = {}
        
        for section in primary_content:
            kind = section.get('kind', '')
            
            if kind == 'content':
                # General content - preserve the full structure
                content_items = section.get('content', [])
                content_parts = self._process_content_items(content_items, references)
                if content_parts:
                    # Instead of separating into overview/discussion, keep as one structured content
                    full_content = '\n\n'.join(content_parts)
                    if 'content' not in extracted:
                        extracted['content'] = full_content
                    else:
                        extracted['content'] += '\n\n' + full_content
            
            elif kind == 'discussion':
                # Explicit discussion section
                content_items = section.get('content', [])
                discussion_parts = self._process_content_items(content_items, references)
                if discussion_parts:
                    extracted['discussion'] = '\n\n'.join(discussion_parts)
            
            elif kind == 'returnValue':
                # Return value documentation
                content_items = section.get('content', [])
                return_parts = self._process_content_items(content_items, references)
                if return_parts:
                    extracted['return_value'] = '\n\n'.join(return_parts)
            
            elif kind == 'task':
                # Task/tutorial sections
                content_items = section.get('content', [])
                task_parts = self._process_content_items(content_items, references)
                if task_parts:
                    if 'tasks' not in extracted:
                        extracted['tasks'] = []
                    extracted['tasks'].append({
                        'title': section.get('title', 'Task'),
                        'content': '\n\n'.join(task_parts)
                    })
            
            elif kind == 'restBody':
                # REST API body documentation
                content_items = section.get('content', [])
                rest_parts = self._process_content_items(content_items, references)
                if rest_parts:
                    extracted['rest_body'] = '\n\n'.join(rest_parts)
            
            elif kind == 'restResponses':
                # REST API responses
                content_items = section.get('content', [])
                response_parts = self._process_content_items(content_items, references)
                if response_parts:
                    extracted['rest_responses'] = '\n\n'.join(response_parts)
            
            elif kind == 'possible_values':
                # Possible values for enums/options
                content_items = section.get('content', [])
                values_parts = self._process_content_items(content_items, references)
                if values_parts:
                    extracted['possible_values'] = '\n\n'.join(values_parts)
            
            elif kind == 'thrown_errors':
                # Error documentation
                content_items = section.get('content', [])
                error_parts = self._process_content_items(content_items, references)
                if error_parts:
                    extracted['thrown_errors'] = '\n\n'.join(error_parts)

            elif kind == 'details':
                # Detail metadata (type info, platform details)
                details = section.get('details', {})
                detail_name = details.get('name', '')
                detail_values = details.get('value', [])
                if detail_name and detail_values:
                    type_info = ', '.join(v.get('baseType', '') for v in detail_values if v.get('baseType'))
                    if type_info:
                        if 'content' not in extracted:
                            extracted['content'] = ''
                        extracted['content'] += f"\n\n**Type**: {type_info}"

            elif kind == 'attributes':
                # Default value and other attributes
                attrs = section.get('attributes', [])
                attr_parts = []
                for attr in attrs:
                    attr_kind = attr.get('kind', '')
                    attr_value = attr.get('value', '')
                    if attr_kind == 'default' and attr_value:
                        attr_parts.append(f"**Default**: `{attr_value}`")
                    elif attr_kind == 'allowedValues':
                        values = attr.get('values', [])
                        if values:
                            attr_parts.append(f"**Allowed Values**: {', '.join(f'`{v}`' for v in values)}")
                if attr_parts:
                    if 'content' not in extracted:
                        extracted['content'] = ''
                    extracted['content'] += '\n\n' + '\n\n'.join(attr_parts)

            elif kind == 'properties':
                # Object properties (common in App Store Connect API)
                items = section.get('items', [])
                prop_parts = []
                for prop in items:
                    name = prop.get('name', '')
                    required = prop.get('required', False)
                    type_tokens = prop.get('type', [])
                    type_text = ''.join(t.get('text', '') for t in type_tokens)
                    prop_content = prop.get('content', [])
                    desc_parts = self._process_content_items(prop_content, references)
                    desc = ' '.join(desc_parts).strip()

                    req_marker = " *(required)*" if required else ""
                    if type_text:
                        prop_parts.append(f"- `{name}` ({type_text}){req_marker}: {desc}" if desc else f"- `{name}` ({type_text}){req_marker}")
                    else:
                        prop_parts.append(f"- `{name}`{req_marker}: {desc}" if desc else f"- `{name}`{req_marker}")
                if prop_parts:
                    extracted['properties'] = '\n'.join(prop_parts)

            elif kind == 'restEndpoint':
                # REST API endpoint URL
                tokens = section.get('tokens', [])
                endpoint = ''.join(t.get('text', '') for t in tokens)
                if endpoint:
                    extracted['rest_endpoint'] = endpoint

            elif kind == 'restParameters':
                # REST API parameters
                items = section.get('items', [])
                param_parts = []
                for param in items:
                    name = param.get('name', '')
                    required = param.get('required', False)
                    type_tokens = param.get('type', [])
                    type_text = ''.join(t.get('text', '') for t in type_tokens)
                    param_content = param.get('content', [])
                    desc_parts = self._process_content_items(param_content, references)
                    desc = ' '.join(desc_parts).strip()

                    req_marker = " *(required)*" if required else ""
                    if type_text:
                        param_parts.append(f"- `{name}` ({type_text}){req_marker}: {desc}" if desc else f"- `{name}` ({type_text}){req_marker}")
                    else:
                        param_parts.append(f"- `{name}`{req_marker}: {desc}" if desc else f"- `{name}`{req_marker}")
                if param_parts:
                    extracted['rest_parameters'] = '\n'.join(param_parts)

        return extracted
    
    def _process_content_items(self, content_items: List[Dict[str, Any]], references: Dict[str, Any]) -> List[str]:
        """Process a list of content items recursively.
        
        Args:
            content_items: List of content items to process
            references: References for resolving inline content
            
        Returns:
            List of processed content strings
        """
        processed_parts = []
        
        for item in content_items:
            item_type = item.get('type', '')
            
            if item_type == 'paragraph':
                # Standard paragraph
                resolved_content = self._resolve_inline_content(item.get('inlineContent', []), references)
                if resolved_content.strip():
                    processed_parts.append(resolved_content)
            
            elif item_type == 'heading':
                # Headings
                level = item.get('level', 1)
                heading_text = self._resolve_inline_content(item.get('inlineContent', []), references)
                
                # If heading is empty but has an anchor, convert anchor to heading text
                if not heading_text.strip() and 'anchor' in item:
                    anchor = item['anchor']
                    # Convert anchor format to readable heading
                    # e.g., "Enable-the-Audio-Background-Mode" -> "Enable the Audio Background Mode"
                    heading_text = anchor.replace('-', ' ')
                    # Capitalize appropriately (title case)
                    heading_text = ' '.join(word.capitalize() for word in heading_text.split())
                    # Special case for common words that shouldn't be capitalized
                    lowercase_words = {'the', 'and', 'or', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'a', 'an'}
                    words = heading_text.split()
                    heading_text = ' '.join(
                        word if i == 0 or word.lower() not in lowercase_words else word.lower()
                        for i, word in enumerate(words)
                    )
                
                if heading_text.strip():
                    heading_prefix = '#' * min(level + 2, 6)  # Adjust level for markdown
                    processed_parts.append(f"{heading_prefix} {heading_text}")
            
            elif item_type == 'codeListing':
                # Code blocks (already handled elsewhere but ensuring completeness)
                code_lines = item.get('code', [])
                if code_lines:
                    code = '\n'.join(code_lines)
                    language = item.get('syntax', 'swift')
                    processed_parts.append(f"```{language}\n{code}\n```")
            
            elif item_type == 'unorderedList':
                # Unordered lists
                list_items = item.get('items', [])
                list_parts = []
                for list_item in list_items:
                    list_content = self._process_content_items(list_item.get('content', []), references)
                    if list_content:
                        list_parts.append(f"- {' '.join(list_content)}")
                if list_parts:
                    processed_parts.append('\n'.join(list_parts))
            
            elif item_type == 'orderedList':
                # Ordered lists
                list_items = item.get('items', [])
                list_parts = []
                for i, list_item in enumerate(list_items, 1):
                    list_content = self._process_content_items(list_item.get('content', []), references)
                    if list_content:
                        list_parts.append(f"{i}. {' '.join(list_content)}")
                if list_parts:
                    processed_parts.append('\n'.join(list_parts))
            
            elif item_type == 'table':
                # Tables (basic implementation)
                table_content = self._process_table(item, references)
                if table_content:
                    processed_parts.append(table_content)
            
            elif item_type == 'aside':
                # Callouts/notes/warnings
                aside_content = self._process_aside(item, references)
                if aside_content:
                    processed_parts.append(aside_content)
            
            elif item_type == 'imageBlock':
                # Images
                image_content = self._process_image(item, references)
                if image_content:
                    processed_parts.append(image_content)

            elif item_type == 'termList':
                # Definition lists (term + definition pairs)
                term_parts = []
                for term_item in item.get('items', []):
                    term = term_item.get('term', {})
                    term_text = self._resolve_inline_content(term.get('inlineContent', []), references)
                    definition = term_item.get('definition', {})
                    def_content = self._process_content_items(definition.get('content', []), references)
                    if term_text:
                        term_parts.append(f"- **{term_text}**: {' '.join(def_content)}")
                if term_parts:
                    processed_parts.append('\n'.join(term_parts))

            elif item_type == 'thematicBreak':
                # Horizontal rule
                processed_parts.append('---')

            elif item_type == 'tabNavigator':
                # Tabbed content (e.g., Swift/Objective-C code examples)
                tabs = item.get('tabs', [])
                for tab in tabs:
                    title = tab.get('title', '')
                    tab_content = tab.get('content', [])
                    tab_parts = self._process_content_items(tab_content, references)
                    if tab_parts:
                        if len(tabs) > 1 and title:
                            processed_parts.append(f"**{title}**:")
                        processed_parts.extend(tab_parts)

            # Handle any nested content recursively for item types that don't process content themselves
            # Skip recursive processing for items that handle their own content (aside, table, termList, tabNavigator, etc.)
            if ('content' in item and isinstance(item['content'], list) and
                item_type not in ['aside', 'table', 'imageBlock', 'termList', 'tabNavigator']):
                nested_content = self._process_content_items(item['content'], references)
                processed_parts.extend(nested_content)
        
        return processed_parts
    
    def _process_table(self, table_item: Dict[str, Any], references: Dict[str, Any]) -> str:
        """Process table content into markdown format."""
        rows = table_item.get('rows', [])
        
        if not rows:
            return ""
        
        markdown_lines = []
        
        # In Apple's format, the header is often just "row" and actual headers are in first row
        # Process all rows, treating first row as potential header
        for row_idx, row in enumerate(rows):
            row_cells = []
            
            for cell in row:
                # Cell can be a list of content items
                if isinstance(cell, list):
                    # Extract text from all content items in the cell
                    cell_parts = []
                    for content_item in cell:
                        if isinstance(content_item, dict):
                            # Process the content item
                            processed = self._process_content_items([content_item], references)
                            if processed:
                                cell_parts.extend(processed)
                    
                    # Join all parts with space and clean up
                    cell_text = ' '.join(cell_parts).strip()
                    # Replace newlines with spaces in table cells
                    cell_text = cell_text.replace('\n', ' ')
                    row_cells.append(cell_text)
                elif isinstance(cell, dict):
                    # Single content item
                    processed = self._process_content_items([cell], references)
                    cell_text = ' '.join(processed).strip().replace('\n', ' ')
                    row_cells.append(cell_text)
                else:
                    # Plain text or other format
                    row_cells.append(str(cell))
            
            # Add row to table
            markdown_lines.append('| ' + ' | '.join(row_cells) + ' |')
            
            # Add separator after first row (header)
            if row_idx == 0:
                markdown_lines.append('| ' + ' | '.join(['---'] * len(row_cells)) + ' |')
        
        return '\n'.join(markdown_lines)
    
    def _process_aside(self, aside_item: Dict[str, Any], references: Dict[str, Any]) -> str:
        """Process aside/callout content."""
        aside_type = aside_item.get('style', 'note')
        content_items = aside_item.get('content', [])
        aside_content = self._process_content_items(content_items, references)
        
        if not aside_content:
            return ""
        
        content_text = ' '.join(aside_content)
        
        if aside_type == 'warning':
            return f"> ⚠️ **Warning**: {content_text}"
        elif aside_type == 'important':
            return f"> ❗ **Important**: {content_text}"
        elif aside_type == 'tip':
            return f"> 💡 **Tip**: {content_text}"
        else:
            return f"> **Note**: {content_text}"
    
    def _process_image(self, image_item: Dict[str, Any], references: Dict[str, Any]) -> str:
        """Process image content."""
        # For inline images in paragraphs
        if image_item.get('type') == 'image':
            image_identifier = image_item.get('identifier', '')
            
            # Look up image in references
            if image_identifier in references:
                ref_data = references[image_identifier]
                alt_text = ref_data.get('alt', '')
                
                # Get the best variant URL
                variants = ref_data.get('variants', [])
                if variants:
                    # Prefer 2x light variant
                    image_url = None
                    for variant in variants:
                        if '2x' in variant.get('traits', []) and 'light' in variant.get('traits', []):
                            image_url = variant.get('url', '')
                            break
                    # Fallback to first variant
                    if not image_url and variants:
                        image_url = variants[0].get('url', '')
                    
                    if image_url:
                        return f"![{alt_text}]({image_url})"
                
                return f"![{alt_text}](image:{image_identifier})"
            
            return f"![](image:{image_identifier})"
        
        # For imageBlock items (different structure)
        image_identifier = image_item.get('identifier', '')
        alt_text = image_item.get('alt', '')
        
        # Look up image in references
        if image_identifier in references:
            ref_data = references[image_identifier]
            # Use alt from references if not provided
            if not alt_text:
                alt_text = ref_data.get('alt', '')
            
            # Get the best variant URL
            variants = ref_data.get('variants', [])
            if variants:
                # Prefer 2x light variant
                image_url = None
                for variant in variants:
                    if '2x' in variant.get('traits', []) and 'light' in variant.get('traits', []):
                        image_url = variant.get('url', '')
                        break
                # Fallback to first variant
                if not image_url and variants:
                    image_url = variants[0].get('url', '')
                
                if image_url:
                    return f"![{alt_text}]({image_url})"
        
        return f"![{alt_text}](image:{image_identifier})" if alt_text else ""
    
    def _track_cross_framework_ref(self, identifier: str) -> None:
        """Track a cross-framework reference."""
        # Extract target framework from identifier
        if '/documentation/' in identifier:
            parts = identifier.split('/documentation/', 1)[1].split('/')
            if parts:
                target_framework = parts[0]
                if target_framework not in self.cross_framework_refs:
                    self.cross_framework_refs[target_framework] = set()
                self.cross_framework_refs[target_framework].add(identifier)
    
    def save_cross_framework_summary(self) -> None:
        """Save summary of cross-framework references if any were found."""
        if not self.cross_framework_refs:
            return
        
        summary_path = self.output_dir / "_cross_framework_refs.json"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        summary_data = {
            "source_framework": self.framework_id,
            "total_external_refs": sum(len(refs) for refs in self.cross_framework_refs.values()),
            "referenced_frameworks": list(self.cross_framework_refs.keys()),
            "references": {
                fw: list(refs) for fw, refs in self.cross_framework_refs.items()
            }
        }
        
        write_text_atomic(summary_path, json.dumps(summary_data, indent=2))
        
        logger.info(
            "saved_cross_framework_summary",
            framework=self.framework_name,
            external_refs=summary_data["total_external_refs"],
            referenced_frameworks=len(summary_data["referenced_frameworks"])
        )