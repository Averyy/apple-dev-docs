"""Base scraper class for Apple documentation."""

import asyncio
import time
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Tuple

import httpx

from scraper.config import Config
from scraper.utils.hash_manager import HashManager
from scraper.utils.logger import get_logger
from scraper.utils.rate_limiter import AdaptiveRateLimiter


logger = get_logger(__name__)


class BaseAppleScraper(ABC):
    """Base class for all Apple documentation scrapers."""
    
    def __init__(
        self,
        framework_id: str,
        framework_name: str,
        base_url: Optional[str] = None
    ) -> None:
        """Initialize base scraper.
        
        Args:
            framework_id: Unique identifier for the framework
            framework_name: Human-readable name of the framework
            base_url: Base URL for the framework documentation
        """
        framework_id = self._canonical_framework_id(framework_id)
        self.framework_id = framework_id
        self.framework_name = framework_name
        self.base_url = base_url or f"{Config.DOCUMENTATION_URL}/{framework_id}"
        
        # Set up paths - use framework_name for proper case in directory
        self.output_dir = Config.get_framework_output_dir(framework_id, framework_name)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize components - use framework_name for proper case in hash file
        self.hash_manager = HashManager(Config.get_hash_file(framework_id, framework_name))
        self.rate_limiter = AdaptiveRateLimiter(initial_delay=Config.RATE_LIMIT_DELAY)
        self.session: Optional[httpx.AsyncClient] = None
        
        # Statistics
        self.stats = {
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
    
    @staticmethod
    def _canonical_framework_id(framework_id: str) -> str:
        """Reconcile framework id casing with any existing hash file.

        Apple's technologies.json changes URL casing between runs (e.g.
        'cryptokit' vs 'CryptoKit'). Framework identity is case-insensitive,
        so an existing hash file's casing wins over the incoming one to keep
        one directory and one hash file per framework.
        """
        suffix = "_hashes.json"
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
        """Async context manager exit."""
        if self.session:
            await self.session.aclose()
        self.hash_manager.save()
    
    async def fetch_page_with_etag(self, url: str, use_etag: bool = True) -> Optional[Tuple[str, Optional[str]]]:
        """Fetch a page with ETag support for efficient caching.
        
        Args:
            url: URL to fetch
            use_etag: Whether to use ETag for conditional requests
            
        Returns:
            Tuple of (content, etag) or None if failed/304 Not Modified
        """
        if not self.session:
            raise RuntimeError("Scraper must be used as async context manager")
        
        # Rate limiting
        await self.rate_limiter.acquire()
        
        # Prepare headers with ETag if available
        headers = {}
        if use_etag:
            stored_etag = self.hash_manager.get_etag(url)
            if stored_etag:
                headers["If-None-Match"] = stored_etag
        
        start_time = time.time()
        retries = 0
        last_error = None
        
        while retries <= Config.MAX_RETRIES:
            try:
                response = await self.session.get(url, headers=headers)
                
                # Handle 304 Not Modified (content unchanged via ETag)
                if response.status_code == 304:
                    response_time = time.time() - start_time
                    self.rate_limiter.record_success(response_time)
                    logger.debug("content_not_modified_etag", url=url, response_time=f"{response_time:.2f}s")
                    return None  # Indicates no change
                
                response.raise_for_status()
                
                # Record success
                response_time = time.time() - start_time
                self.rate_limiter.record_success(response_time)
                
                # Extract ETag from response headers
                etag = response.headers.get("ETag")
                
                logger.debug(
                    "page_fetched",
                    url=url,
                    status=response.status_code,
                    response_time=f"{response_time:.2f}s",
                    etag=etag[:8] if etag else None
                )
                
                return (response.text, etag)
                
            except httpx.HTTPStatusError as e:
                last_error = e
                if e.response.status_code == 429:  # Rate limited
                    self.rate_limiter.record_error("rate_limit")
                    wait_time = (retries + 1) * Config.RETRY_BACKOFF_FACTOR * 10
                    logger.warning(
                        "rate_limited",
                        url=url,
                        retry=retries,
                        wait_time=f"{wait_time}s"
                    )
                    await asyncio.sleep(wait_time)
                elif e.response.status_code >= 500:  # Server error
                    self.rate_limiter.record_error("server_error")
                    wait_time = (retries + 1) * Config.RETRY_BACKOFF_FACTOR
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
                    self.hash_manager.mark_error(url, f"HTTP {e.response.status_code}")
                    return None
                    
            except Exception as e:
                last_error = e
                self.rate_limiter.record_error("network_error")
                logger.error(
                    "fetch_error",
                    url=url,
                    error=str(e),
                    retry=retries
                )
                
                if retries < Config.MAX_RETRIES:
                    wait_time = (retries + 1) * Config.RETRY_BACKOFF_FACTOR
                    await asyncio.sleep(wait_time)
            
            retries += 1
        
        # All retries exhausted
        self.hash_manager.mark_error(url, str(last_error))
        self.stats["pages_failed"] += 1
        return None
    
    @abstractmethod
    async def save_page_data(self, url: str, data: Dict[str, Any]) -> None:
        """Save extracted data to disk.
        
        Args:
            url: Source URL
            data: Extracted data
        """
        pass
