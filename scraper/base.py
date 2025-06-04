"""Base scraper class for Apple documentation."""

import asyncio
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
from urllib.parse import urljoin, urlparse

import httpx
from bs4 import BeautifulSoup

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
        self.framework_id = framework_id
        self.framework_name = framework_name
        self.base_url = base_url or f"{Config.DOCUMENTATION_URL}/{framework_id}"
        
        # Set up paths
        self.output_dir = Config.get_framework_output_dir(framework_id)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize components
        self.hash_manager = HashManager(Config.get_hash_file(framework_id))
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
    
    async def fetch_page(self, url: str) -> Optional[str]:
        """Fetch a page with rate limiting and error handling.
        
        Args:
            url: URL to fetch
            
        Returns:
            Page content or None if failed
        """
        # Use the new ETag-enabled method but return only content for backward compatibility
        result = await self.fetch_page_with_etag(url)
        return result[0] if result else None
    
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
    
    async def scrape_page(self, url: str) -> Optional[Dict[str, Any]]:
        """Scrape a single documentation page.
        
        Args:
            url: URL to scrape
            
        Returns:
            Extracted data or None if failed
        """
        # Check if content has changed
        content = await self.fetch_page(url)
        if not content:
            return None
        
        # Check hash to avoid re-processing unchanged content
        if not self.hash_manager.has_changed(url, content) and not Config.DEBUG:
            logger.debug("content_unchanged", url=url)
            self.stats["pages_skipped"] += 1
            return None
        
        # Parse and extract data
        try:
            soup = BeautifulSoup(content, 'html.parser')
            data = await self.extract_page_data(soup, url)
            
            if data:
                # Update hash for successful extraction
                self.hash_manager.update_hash(url, content)
                self.stats["pages_scraped"] += 1
                return data
            else:
                logger.warning("no_data_extracted", url=url)
                return None
                
        except Exception as e:
            logger.error(
                "parse_error",
                url=url,
                error=str(e)
            )
            self.hash_manager.mark_error(url, f"Parse error: {str(e)}")
            self.stats["pages_failed"] += 1
            return None
    
    @abstractmethod
    async def extract_page_data(self, soup: BeautifulSoup, url: str) -> Optional[Dict[str, Any]]:
        """Extract structured data from a page.
        
        Args:
            soup: BeautifulSoup object of the page
            url: URL of the page
            
        Returns:
            Extracted data or None if failed
        """
        pass
    
    @abstractmethod
    async def discover_urls(self) -> List[str]:
        """Discover all URLs to scrape for this framework.
        
        Returns:
            List of URLs to scrape
        """
        pass
    
    async def scrape_framework(self) -> Dict[str, Any]:
        """Scrape the entire framework documentation.
        
        Returns:
            Summary statistics
        """
        self.stats["start_time"] = time.time()
        
        logger.info(
            "starting_framework_scrape",
            framework=self.framework_name,
            base_url=self.base_url
        )
        
        # Create progress indicator file immediately
        progress_file = self.output_dir / "scraping_progress.txt"
        progress_file.parent.mkdir(parents=True, exist_ok=True)
        progress_file.write_text(f"Starting {self.framework_name} discovery...\n")
        
        # Discover all URLs
        urls = await self.discover_urls()
        
        # Update progress file
        progress_file.write_text(f"Found {len(urls)} pages to scrape. Starting...\n")
        
        logger.info(
            "urls_discovered",
            framework=self.framework_name,
            total_urls=len(urls)
        )
        
        # Filter out unchanged URLs if not in debug mode
        if not Config.DEBUG:
            unchanged_urls = self.hash_manager.get_unchanged_urls()
            urls = [url for url in urls if url not in unchanged_urls]
            logger.info(
                "filtered_unchanged_urls",
                remaining=len(urls),
                skipped=len(unchanged_urls)
            )
        
        # Scrape pages in batches
        batch_size = Config.MAX_CONCURRENT_REQUESTS
        progress_file = self.output_dir / "scraping_progress.txt"
        
        for i in range(0, len(urls), batch_size):
            batch = urls[i:i + batch_size]
            tasks = [self.scrape_page(url) for url in batch]
            results = await asyncio.gather(*tasks)
            
            # Process results
            for url, data in zip(batch, results):
                if data:
                    await self.save_page_data(url, data)
            
            # Progress update
            progress = min(i + batch_size, len(urls))
            
            # Update progress file for Finder visibility
            progress_text = f"Progress: {progress}/{len(urls)} ({(progress/len(urls)*100):.1f}%)\n"
            progress_text += f"Files saved: {self.stats['pages_scraped']}\n"
            progress_text += f"Last updated: {time.strftime('%H:%M:%S')}\n"
            progress_file.write_text(progress_text)
            
            logger.info(
                "scraping_progress",
                framework=self.framework_name,
                progress=f"{progress}/{len(urls)}",
                percentage=f"{(progress/len(urls)*100):.1f}%"
            )
        
        self.stats["end_time"] = time.time()
        self.stats["duration"] = self.stats["end_time"] - self.stats["start_time"]
        
        logger.info(
            "framework_scrape_complete",
            framework=self.framework_name,
            stats=self.stats
        )
        
        # Create framework README if it doesn't exist
        if hasattr(self, 'create_framework_readme'):
            self.create_framework_readme()
        
        return self.stats
    
    @abstractmethod
    async def save_page_data(self, url: str, data: Dict[str, Any]) -> None:
        """Save extracted data to disk.
        
        Args:
            url: Source URL
            data: Extracted data
        """
        pass
    
    def get_relative_path(self, url: str) -> Path:
        """Convert URL to relative file path.
        
        Args:
            url: Full URL
            
        Returns:
            Relative path for saving
        """
        parsed = urlparse(url)
        path = parsed.path.replace(f"/documentation/{self.framework_id}/", "")
        
        # Clean up path
        if path.endswith('/'):
            path = path[:-1]
        if not path:
            path = "index"
        
        # Replace special characters
        path = path.replace('/', '_')
        
        return Path(f"{path}.md")