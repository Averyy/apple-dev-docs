"""Base scraper class for Apple documentation."""

import asyncio
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, ClassVar, Dict, Final, Optional, Union

import httpx

from scraper.config import Config
from scraper.sink import Sink
from scraper.utils.hash_manager import HashManager
from scraper.utils.logger import get_logger
from scraper.utils.rate_limiter import AdaptiveRateLimiter


logger = get_logger(__name__)


class NotModified(Enum):
    """Type of the NOT_MODIFIED sentinel (a one-member enum, so mypy narrows on it)."""

    NOT_MODIFIED = "not_modified"


# The server answered 304 Not Modified (no request sends If-None-Match, so a
# 304 is unasked for; it is still not a failure).
NOT_MODIFIED: Final = NotModified.NOT_MODIFIED


@dataclass(frozen=True)
class FetchFailed:
    """A fetch that produced no usable response.

    Attributes:
        status: HTTP status of the last response, or None if no response
            arrived (timeout, connection or other network error)
        error: Error message, in the form HashManager.mark_error records it
        transient: True for a failure worth retrying on a later run (5xx, a
            429 that outlasted its retries, network errors); False for any
            other 4xx, which is returned without retrying
    """

    status: Optional[int]
    error: str
    transient: bool


# The content on 200, NOT_MODIFIED on 304, FetchFailed otherwise
FetchResult = Union[str, NotModified, FetchFailed]


class BaseAppleScraper(ABC):
    """Base class for all Apple documentation scrapers."""

    # The version of the scraper's converter output (file names and links
    # included), stored in each framework's hash file after a clean run; a
    # framework whose stored version differs is rendered again whole
    # (HashManager.stale). Set by the subclass; None renders nothing again
    RENDER_VERSION: ClassVar[Optional[int]] = None

    def __init__(
        self,
        framework_id: str,
        framework_name: str,
        base_url: Optional[str] = None,
        hash_dir: Optional[Path] = None,
        rate_limiter: Optional[AdaptiveRateLimiter] = None,
        max_retries: Optional[int] = None,
        retry_backoff: Optional[float] = None,
    ) -> None:
        """Initialize base scraper.
        
        Args:
            framework_id: Unique identifier for the framework
            framework_name: Human-readable name of the framework
            base_url: Base URL for the framework documentation
            hash_dir: The dir of its site's hash files, whose casing of the
                id wins (_canonical_framework_id); Apple's by default
            rate_limiter: A limiter shared with other jobs (a DocC site's
                jobs share one, so the site sees one job's rate); its own by
                default
            max_retries: A request's retries after a 5xx, 429 or network
                error (its site's, DocCSite.max_retries); Config.MAX_RETRIES
                by default
            retry_backoff: The wait before a request's n-th retry is n times
                this (ten times after a 429; its site's,
                DocCSite.retry_backoff); Config.RETRY_BACKOFF_FACTOR by default
        """
        framework_id = self._canonical_framework_id(framework_id, hash_dir)
        self.framework_id = framework_id
        self.framework_name = framework_name
        self.base_url = base_url or f"{Config.DOCUMENTATION_URL}/{framework_id}"
        
        # Initialize components. The framework's docs dir and hash file are
        # its primary sink's, which the subclass sets up (hash_manager)
        self.rate_limiter = rate_limiter or AdaptiveRateLimiter(initial_delay=Config.RATE_LIMIT_DELAY)
        self.max_retries = max_retries
        self.retry_backoff = retry_backoff
        self.session: Optional[httpx.AsyncClient] = None
        
        # Statistics
        self.stats: Dict[str, Any] = {
            "pages_scraped": 0,
            "pages_skipped": 0,
            "pages_failed": 0,
            "start_time": None,
            "end_time": None
        }
        
        logger.info(
            "scraper_initialized",
            framework=framework_name,
            framework_id=framework_id,
            base_url=self.base_url
        )
    
    @property
    @abstractmethod
    def hash_manager(self) -> HashManager:
        """The framework's own hash file (its primary sink's): saved on exit."""

    @staticmethod
    def _canonical_framework_id(framework_id: str, hash_dir: Optional[Path] = None) -> str:
        """Reconcile framework id casing with any existing hash file.

        Apple's technologies.json changes URL casing between runs (e.g.
        'cryptokit' vs 'CryptoKit'). Framework identity is case-insensitive,
        so an existing hash file's casing wins over the incoming one to keep
        one directory and one hash file per framework.

        Args:
            framework_id: The id, as it comes
            hash_dir: Its site's hash dir (a namespaced site's is
                .hashes/<namespace>/); Apple's by default
        """
        suffix = "_hashes.json"
        if hash_dir is None:
            hash_dir = Config.get_hash_file(framework_id).parent
        if not hash_dir.exists():
            return framework_id
        wanted = f"{framework_id.lower()}{suffix}"
        candidates = [
            p.name[: -len(suffix)]
            for p in hash_dir.glob(f"*{suffix}")
            if p.name.lower() == wanted
        ]
        if not candidates or framework_id in candidates:
            return framework_id
        if len(candidates) > 1:
            logger.warning(
                "multiple_casing_candidates",
                requested=framework_id,
                candidates=sorted(candidates),
            )
        existing_id = sorted(candidates)[0]
        logger.info(
            "framework_id_casing_reconciled",
            requested=framework_id,
            using=existing_id,
        )
        return existing_id

    async def __aenter__(self) -> "BaseAppleScraper":
        """Async context manager entry."""
        self.session = httpx.AsyncClient(
            timeout=Config.REQUEST_TIMEOUT,
            headers={"User-Agent": Config.USER_AGENT},
            follow_redirects=True
        )
        return self
    
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Async context manager exit.

        A failed hash save raises (unless the scrape already did), so the
        framework fails and orphan cleanup skips it: this run's entries (new
        pages, counters, error entries) weren't saved, and its cleanup would
        prune and write pending_orphans onto the previous run's hash file.
        """
        if self.session:
            await self.session.aclose()
        if not self.hash_manager.save() and exc_type is None:
            raise OSError(f"failed to save hash file {self.hash_manager.cache_file}")
    
    async def fetch_page(self, url: str) -> FetchResult:
        """Fetch a page, unconditionally (no If-None-Match is sent).
        
        Never writes the URL's hash entry: callers decide what a failure
        means for it.
        
        Args:
            url: URL to fetch
            
        Returns:
            The content on success, NOT_MODIFIED on 304 Not Modified, or
            FetchFailed on a 4xx or once retries are exhausted
        """
        if not self.session:
            raise RuntimeError("Scraper must be used as async context manager")
        
        # Rate limiting
        await self.rate_limiter.acquire()
        
        start_time = time.time()
        retries = 0
        last_error: Optional[Exception] = None
        
        max_retries = self.max_retries if self.max_retries is not None else Config.MAX_RETRIES
        backoff = self.retry_backoff if self.retry_backoff is not None else Config.RETRY_BACKOFF_FACTOR
        while retries <= max_retries:
            try:
                response = await self.session.get(url)
                
                # 304 Not Modified: unasked for, but raise_for_status would
                # make it a non-transient failure
                if response.status_code == 304:
                    response_time = time.time() - start_time
                    self.rate_limiter.record_success(response_time)
                    logger.debug("content_not_modified", url=url, response_time=f"{response_time:.2f}s")
                    return NOT_MODIFIED
                
                response.raise_for_status()
                
                # Record success
                response_time = time.time() - start_time
                self.rate_limiter.record_success(response_time)
                
                logger.debug(
                    "page_fetched",
                    url=url,
                    status=response.status_code,
                    response_time=f"{response_time:.2f}s"
                )
                
                return response.text
                
            except httpx.HTTPStatusError as e:
                last_error = e
                if e.response.status_code == 429:  # Rate limited
                    self.rate_limiter.record_error("rate_limit")
                    wait_time = (retries + 1) * backoff * 10
                    logger.warning(
                        "rate_limited",
                        url=url,
                        retry=retries,
                        wait_time=f"{wait_time}s"
                    )
                    await asyncio.sleep(wait_time)
                elif e.response.status_code >= 500:  # Server error
                    self.rate_limiter.record_error("server_error")
                    wait_time = (retries + 1) * backoff
                    logger.warning(
                        "server_error",
                        url=url,
                        status=e.response.status_code,
                        retry=retries
                    )
                    await asyncio.sleep(wait_time)
                else:
                    # Client error (4xx), don't retry
                    logger.error(
                        "http_error",
                        url=url,
                        status=e.response.status_code,
                        error=str(e)
                    )
                    return FetchFailed(
                        status=e.response.status_code,
                        error=f"HTTP {e.response.status_code}",
                        transient=False
                    )
                    
            except Exception as e:
                last_error = e
                self.rate_limiter.record_error("network_error")
                logger.error(
                    "fetch_error",
                    url=url,
                    error=str(e),
                    retry=retries
                )
                
                if retries < max_retries:
                    wait_time = (retries + 1) * backoff
                    await asyncio.sleep(wait_time)
            
            retries += 1
        
        # All retries exhausted (5xx, 429 or network error)
        self.stats["pages_failed"] += 1
        status = last_error.response.status_code if isinstance(last_error, httpx.HTTPStatusError) else None
        return FetchFailed(status=status, error=str(last_error), transient=True)
    
    @abstractmethod
    async def save_page_data(self, sink: Sink, url: str, data: Dict[str, Any]) -> bool:
        """Save extracted data to disk.
        
        Args:
            sink: The page's sink
            url: Source URL
            data: Extracted data

        Returns:
            True if the file was written
        """
        pass
