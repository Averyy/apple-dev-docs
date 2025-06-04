"""Discover all Apple frameworks from the technologies page."""

import asyncio
import json
from pathlib import Path
from typing import Dict, List, Optional, Set
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup

from scraper.config import Config
from scraper.utils.logger import get_logger
from scraper.utils.rate_limiter import RateLimiter

logger = get_logger(__name__)


class FrameworkDiscovery:
    """Discover all Apple frameworks and their documentation URLs."""
    
    def __init__(self) -> None:
        """Initialize framework discovery."""
        self.rate_limiter = RateLimiter(requests_per_second=1.0)
        self.frameworks: List[Dict[str, str]] = []
        self._session: Optional[httpx.AsyncClient] = None
    
    async def __aenter__(self) -> "FrameworkDiscovery":
        """Async context manager entry."""
        self._session = httpx.AsyncClient(
            timeout=Config.REQUEST_TIMEOUT,
            headers={"User-Agent": Config.USER_AGENT}
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        if self._session:
            await self._session.aclose()
    
    async def discover_all_frameworks(self) -> List[Dict[str, str]]:
        """Discover all available Apple frameworks.
        
        Returns:
            List of framework information dictionaries
        """
        logger.info("starting_framework_discovery")
        
        # Start with the main technologies page
        await self._discover_from_technologies_page()
        
        # Also check documentation index
        await self._discover_from_documentation_index()
        
        # Remove duplicates and sort
        self._deduplicate_frameworks()
        
        logger.info(
            "framework_discovery_complete",
            total_frameworks=len(self.frameworks),
            sample=self.frameworks[:5]
        )
        
        return self.frameworks
    
    async def _fetch_page(self, url: str) -> Optional[str]:
        """Fetch a page with rate limiting.
        
        Args:
            url: URL to fetch
            
        Returns:
            Page content or None
        """
        if not self._session:
            raise RuntimeError("Must use as async context manager")
        
        await self.rate_limiter.acquire()
        
        try:
            response = await self._session.get(url)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logger.error("fetch_error", url=url, error=str(e))
            return None
    
    async def _discover_from_technologies_page(self) -> None:
        """Discover frameworks from the main technologies page."""
        url = Config.TECHNOLOGIES_URL
        content = await self._fetch_page(url)
        
        if not content:
            logger.error("failed_to_fetch_technologies_page")
            return
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Look for all documentation links
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Process links that look like framework documentation
            if '/documentation/' in href:
                self._process_framework_link(link)
        
        # Method 3: Check sidebar if present
        sidebar = soup.find(['nav', 'aside'], class_=['sidebar', 'navigation', 'filter'])
        if sidebar:
            for link in sidebar.find_all('a'):
                if link.get('href', '').startswith('/documentation/'):
                    self._process_framework_link(link)
    
    async def _discover_from_documentation_index(self) -> None:
        """Discover frameworks from the documentation index."""
        url = Config.DOCUMENTATION_URL
        content = await self._fetch_page(url)
        
        if not content:
            return
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Look for framework listings
        for link in soup.find_all('a', href=True):
            href = link['href']
            text = link.get_text().strip()
            
            # Check if it's a framework link
            if (href.startswith('/documentation/') and 
                href.count('/') == 2 and 
                text and 
                not any(exclude in href for exclude in ['technologies', 'sample-code', 'release-notes'])):
                
                self._process_framework_link(link)
    
    def _process_framework_link(self, link_element) -> None:
        """Process a potential framework link.
        
        Args:
            link_element: BeautifulSoup link element
        """
        href = link_element.get('href', '')
        text = link_element.get_text().strip()
        
        if not href or not text:
            return
        
        # Parse the URL
        if not href.startswith('http'):
            href = f"https://developer.apple.com{href}"
        
        parsed = urlparse(href)
        path_parts = parsed.path.strip('/').split('/')
        
        # Check if it's a valid framework URL
        if (len(path_parts) >= 2 and 
            path_parts[0] == 'documentation' and
            path_parts[1] not in ['technologies', 'sample-code']):
            
            framework_id = path_parts[1]
            
            # Clean up the framework name
            name = text
            if ' - ' in name:
                name = name.split(' - ')[0]
            if name.endswith(' Framework'):
                name = name[:-10]
            
            framework_info = {
                'id': framework_id,
                'name': name,
                'url': f"https://developer.apple.com/documentation/{framework_id}",
                'category': self._categorize_framework(framework_id, name)
            }
            
            self.frameworks.append(framework_info)
    
    def _categorize_framework(self, framework_id: str, name: str) -> str:
        """Categorize a framework based on its ID and name.
        
        Args:
            framework_id: Framework identifier
            name: Framework name
            
        Returns:
            Category name
        """
        # Define category mappings
        categories = {
            'ui': ['ui', 'kit', 'swiftui', 'appkit', 'watchkit', 'tvuikit'],
            'graphics': ['metal', 'scene', 'sprite', 'reality', 'core_graphics', 'core_image'],
            'media': ['av', 'audio', 'video', 'photo', 'image', 'vision'],
            'app_services': ['cloud', 'store', 'weather', 'map', 'location'],
            'system': ['foundation', 'security', 'network', 'file'],
            'web': ['webkit', 'safari', 'authentication'],
            'developer': ['xctest', 'instruments', 'docc'],
            'ml': ['coreml', 'createml', 'natural_language'],
            'ar': ['arkit', 'realitykit', 'roomplan'],
            'health': ['health', 'care', 'research'],
            'home': ['homekit', 'matter'],
            'platform': ['carplay', 'driverkit', 'virtualization']
        }
        
        framework_lower = framework_id.lower()
        name_lower = name.lower()
        
        for category, keywords in categories.items():
            if any(keyword in framework_lower or keyword in name_lower for keyword in keywords):
                return category
        
        return 'other'
    
    def _deduplicate_frameworks(self) -> None:
        """Remove duplicate frameworks."""
        seen_ids = set()
        unique_frameworks = []
        
        for framework in self.frameworks:
            if framework['id'] not in seen_ids:
                seen_ids.add(framework['id'])
                unique_frameworks.append(framework)
        
        # Sort by name
        self.frameworks = sorted(unique_frameworks, key=lambda f: f['name'])
    
    async def save_framework_list(self, output_path: Path) -> None:
        """Save discovered frameworks to a JSON file.
        
        Args:
            output_path: Path to save the framework list
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            'total_frameworks': len(self.frameworks),
            'frameworks': self.frameworks,
            'categories': self._get_category_summary()
        }
        
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        logger.info(
            "saved_framework_list",
            path=str(output_path),
            total=len(self.frameworks)
        )
    
    def _get_category_summary(self) -> Dict[str, int]:
        """Get summary of frameworks by category.
        
        Returns:
            Category counts
        """
        summary = {}
        for framework in self.frameworks:
            category = framework.get('category', 'other')
            summary[category] = summary.get(category, 0) + 1
        
        return summary


async def discover_frameworks() -> List[Dict[str, str]]:
    """Convenience function to discover all frameworks.
    
    Returns:
        List of framework information
    """
    async with FrameworkDiscovery() as discovery:
        frameworks = await discovery.discover_all_frameworks()
        
        # Save to metadata directory
        await discovery.save_framework_list(
            Config.get_metadata_file('frameworks.json')
        )
        
        return frameworks