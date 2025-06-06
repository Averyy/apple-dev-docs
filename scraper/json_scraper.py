"""JSON-based Apple documentation scraper that uses Apple's data endpoints."""

import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Set
from urllib.parse import urljoin, urlparse

from scraper.base import BaseAppleScraper
from scraper.utils.logger import get_logger
from scraper.utils.markdown_converter import AppleDocMarkdownConverter

logger = get_logger(__name__)


class AppleJSONDocumentationScraper(BaseAppleScraper):
    """Scraper that uses Apple's JSON data endpoints instead of HTML pages."""
    
    # Base URL for JSON data
    JSON_BASE_URL = "https://developer.apple.com/tutorials/data/documentation"
    
    def __init__(self, framework_id: str, framework_name: Optional[str] = None) -> None:
        """Initialize JSON-based scraper.
        
        Args:
            framework_id: Framework identifier (e.g., 'swiftui', 'uikit')
            framework_name: Human-readable name (defaults to framework_id)
        """
        super().__init__(
            framework_id=framework_id,
            framework_name=framework_name or framework_id.replace('-', ' ').title()
        )
        self.markdown_converter = AppleDocMarkdownConverter(self.output_dir)
        self.discovered_urls: Set[str] = set()
        self.processed_urls: Set[str] = set()
        self._discovery_batch_size = 1000  # Process URLs in batches to manage memory
        self.topic_hierarchy: Dict[str, Dict[str, List[str]]] = {}  # Track topic organization
    
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
    
    async def discover_urls(self) -> List[str]:
        """Discover all documentation URLs for the framework."""
        logger.info("discovering_urls_via_json", framework=self.framework_name)
        
        # Start with the framework's main JSON file
        framework_json_url = f"{self.JSON_BASE_URL}/{self.framework_id}.json"
        
        # Extract topic hierarchy from main framework page
        await self._extract_topic_hierarchy(framework_json_url)
        
        await self._discover_from_json(framework_json_url)
        
        # Convert discovered JSON URLs to documentation URLs
        doc_urls = [
            self._convert_json_url_to_doc_url(url) 
            for url in self.discovered_urls
        ]
        
        logger.info(
            "urls_discovered",
            framework=self.framework_name,
            total=len(doc_urls),
            sample=doc_urls[:5] if doc_urls else []
        )
        
        return sorted(doc_urls)
    
    async def scrape_framework(self) -> Dict[str, Any]:
        """Override base scrape_framework to use streaming approach."""
        self.stats["start_time"] = time.time()
        
        await self.discover_and_scrape_streaming()
        
        self.stats["end_time"] = time.time()
        self.stats["duration"] = self.stats["end_time"] - self.stats["start_time"]
        
        logger.info(
            "framework_scrape_complete",
            framework=self.framework_name,
            stats=self.stats
        )
        
        return self.stats
    
    async def discover_and_scrape_streaming(self):
        """Discover URLs and scrape them immediately for real-time feedback."""
        logger.info("starting_streaming_discovery_and_scrape", framework=self.framework_name)
        
        # Create progress file immediately
        progress_file = self.output_dir / "scraping_progress.txt" 
        progress_file.parent.mkdir(parents=True, exist_ok=True)
        progress_file.write_text(f"Starting {self.framework_name} streaming scrape...\n")
        
        # Start with the framework's main JSON file
        framework_json_url = f"{self.JSON_BASE_URL}/{self.framework_id}.json"
        
        # Extract topic hierarchy from main framework page
        await self._extract_topic_hierarchy(framework_json_url)
        
        # Scrape the main framework page first
        main_doc_url = f"https://developer.apple.com/documentation/{self.framework_id}"
        progress_file.write_text(f"Scraping main page: {main_doc_url}\n")
        await self._scrape_and_save_url(main_doc_url)
        
        # Use iterative approach instead of recursion to avoid stack overflow
        try:
            await self._discover_and_scrape_iterative(framework_json_url, progress_file)
        finally:
            # Final progress update - ALWAYS execute this even if an error occurs
            self._update_progress_file(progress_file, "COMPLETED", final=True)
            logger.info(
                "framework_scraping_finalized",
                framework=self.framework_name,
                pages_scraped=self.stats['pages_scraped'],
                pages_skipped=self.stats['pages_skipped'],
                pages_failed=self.stats['pages_failed']
            )
        
    def _update_progress_file(self, progress_file: Path, last_url: str, final: bool = False) -> None:
        """Update progress file with current statistics."""
        if final:
            content = f"""Completed scraping {self.framework_name}!
Total pages scraped: {self.stats['pages_scraped']}
Pages skipped (unchanged): {self.stats['pages_skipped']}
Pages failed: {self.stats['pages_failed']}
"""
        else:
            content = f"""Scraping {self.framework_name} in progress...
Last scraped: {last_url}
Progress: {self.stats['pages_scraped']} scraped, {self.stats['pages_skipped']} skipped, {self.stats['pages_failed']} failed
"""
        progress_file.write_text(content)
        
    async def _scrape_and_save_url(self, url: str) -> bool:
        """Scrape a single URL and save it immediately."""
        try:
            data = await self.scrape_page(url)
            if data:
                await self.save_page_data(url, data)
                return True
            return False
        except Exception as e:
            logger.error("failed_to_scrape_url", url=url, error=str(e))
            return False
    
    async def _discover_and_scrape_from_json(self, json_url: str, progress_file) -> None:
        """Discover URLs from JSON and scrape them immediately."""
        if json_url in self.processed_urls:
            return
        
        self.processed_urls.add(json_url)
        
        # Fetch the JSON data - for discovery, we need content even if unchanged
        result = await self.fetch_page_with_etag(json_url, use_etag=False)
        if not result:
            return
        response_text = result[0]
        
        try:
            data = json.loads(response_text)
            
            # This JSON file is valid documentation - scrape it immediately
            doc_url = self._convert_json_url_to_doc_url(json_url)
            scraped = await self._scrape_and_save_url(doc_url)
            
            if scraped:
                # Update progress with current stats
                self._update_progress_file(progress_file, doc_url)
                
                # Log progress every 10 files
                if self.stats['pages_scraped'] % 10 == 0:
                    logger.info(
                        "scraping_progress",
                        scraped=self.stats['pages_scraped'],
                        skipped=self.stats['pages_skipped'],
                        failed=self.stats['pages_failed']
                    )
            
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
                    logger.debug(f"Processing {section_name} with {len(data[section_name])} items")
                    await self._extract_and_scrape_links_from_sections(data[section_name], progress_file)
            
            # Handle references separately as it's a dict
            if 'references' in data and isinstance(data['references'], dict):
                logger.debug(f"Processing references with {len(data['references'])} items")
                # References don't have identifiers directly, skip for now
                    
        except json.JSONDecodeError:
            logger.warning("failed_to_parse_json", url=json_url)
    
    async def _discover_and_scrape_iterative(self, initial_json_url: str, progress_file) -> None:
        """Iterative version of discovery to avoid recursion depth issues."""
        from collections import deque
        
        # Queue of URLs to process
        url_queue = deque([initial_json_url])
        
        logger.info(f"starting_iterative_discovery", initial_url=initial_json_url)
        
        # Track queue size for monitoring
        max_queue_size = 0
        processed_count = 0
        
        while url_queue:
            # Monitor queue growth for debugging
            current_queue_size = len(url_queue)
            max_queue_size = max(max_queue_size, current_queue_size)
            
            # Get next URL to process
            json_url = url_queue.popleft()
            
            # Skip if already processed
            if json_url in self.processed_urls:
                continue
                
            self.processed_urls.add(json_url)
            processed_count += 1
            
            # Log progress periodically
            if processed_count % 100 == 0:
                logger.info(
                    "iterative_discovery_progress",
                    processed=processed_count,
                    queue_size=current_queue_size,
                    max_queue_size=max_queue_size
                )
            
            try:
                # Fetch the JSON data
                result = await self.fetch_page_with_etag(json_url, use_etag=False)
                if not result:
                    continue
                response_text = result[0]
                
                # Parse JSON
                try:
                    data = json.loads(response_text)
                except json.JSONDecodeError:
                    logger.warning("failed_to_parse_json", url=json_url)
                    continue
                
                # Scrape this page immediately
                doc_url = self._convert_json_url_to_doc_url(json_url)
                scraped = await self._scrape_and_save_url(doc_url)
                
                if scraped:
                    # Update progress
                    self._update_progress_file(progress_file, doc_url)
                    
                    # Log progress every 10 files
                    if self.stats['pages_scraped'] % 10 == 0:
                        logger.info(
                            "scraping_progress",
                            scraped=self.stats['pages_scraped'],
                            skipped=self.stats['pages_skipped'],
                            failed=self.stats['pages_failed'],
                            queue_size=current_queue_size
                        )
                
                # Extract new URLs and add to queue (instead of recursing)
                new_urls = self._extract_urls_from_json_data(data)
                
                # Filter and add new URLs to queue
                for new_url in new_urls:
                    if new_url not in self.processed_urls:
                        url_queue.append(new_url)
                        
            except Exception as e:
                logger.error("error_processing_url", url=json_url, error=str(e))
                continue
        
        logger.info(
            "iterative_discovery_complete",
            total_processed=processed_count,
            max_queue_size=max_queue_size,
            framework=self.framework_name
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
                                # Only process identifiers for the current framework
                                identifier_lower = identifier.lower()
                                framework_check = f"com.apple.{self.framework_id.lower()}"
                                if framework_check in identifier_lower or f"/{self.framework_id.lower()}/" in identifier_lower or f"/{self.framework_id}/" in identifier:
                                    json_url = self._convert_identifier_to_json_url(identifier)
                                    if json_url:
                                        urls.append(json_url)
        
        return urls
    
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
            
            return f"{self.JSON_BASE_URL}/{path_lower}.json"
            
        except Exception as e:
            logger.error(f"Error converting identifier {identifier}: {e}")
            return None
    
    async def _extract_and_scrape_links_from_sections(self, sections: List[Dict], progress_file) -> None:
        """Extract links from sections and scrape them immediately."""
        for section in sections:
            if 'identifiers' in section:
                identifiers = section.get('identifiers', [])
                section_title = section.get('title', 'Unknown')
                logger.info(f"Found section '{section_title}' with {len(identifiers)} identifiers")
                await self._process_and_scrape_identifiers(identifiers, progress_file)
    
    async def _process_and_scrape_identifiers(self, identifiers: List[str], progress_file) -> None:
        """Process identifiers and scrape them immediately."""
        logger.info(f"Processing batch of {len(identifiers)} identifiers")
        for identifier in identifiers:
            if identifier.startswith('doc://'):
                # Only process identifiers for the current framework
                # Handle case-insensitive comparison properly
                identifier_lower = identifier.lower()
                framework_check = f"com.apple.{self.framework_id.lower()}"
                if framework_check in identifier_lower or f"/{self.framework_id.lower()}/" in identifier_lower or f"/{self.framework_id}/" in identifier:
                    await self._process_and_scrape_identifier(identifier, progress_file)
    
    async def _process_and_scrape_identifier(self, identifier: str, progress_file) -> None:
        """Process a single identifier and scrape it immediately."""
        try:
            # Convert doc://com.apple.watchkit/documentation/WatchKit/WKApplication to 
            # https://developer.apple.com/tutorials/data/documentation/watchkit/wkapplication.json
            
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
        except Exception as e:
            logger.error(f"Error processing identifier {identifier}: {e}")
            return
        
        # Now path is like "WatchKit/WKApplication" or "WatchKit/setting-up-a-watchos-project"
        # Convert to lowercase and ensure it starts with framework_id
        path_lower = path.lower()
        
        # If it starts with framework_id/, keep it. Otherwise prepend framework_id
        if not path_lower.startswith(f"{self.framework_id.lower()}/"):
            # Replace any case variation of current framework with our framework_id
            if path_lower.startswith(f'{self.framework_id.lower()}/'):
                # Already correct
                pass
            else:
                path_lower = f"{self.framework_id.lower()}/{path_lower}"
        
        json_url = f"{self.JSON_BASE_URL}/{path_lower}.json"
        
        if json_url not in self.processed_urls:
            logger.debug(f"Processing new URL: {json_url}")
            await self._discover_and_scrape_from_json(json_url, progress_file)
        else:
            logger.debug(f"Skipping already processed: {json_url}")
    
    async def _extract_topic_hierarchy(self, framework_json_url: str) -> None:
        """Extract topic hierarchy from main framework page for organized file structure."""
        # For topic hierarchy, we need the content even if unchanged
        result = await self.fetch_page_with_etag(framework_json_url, use_etag=False)
        if not result:
            return
        response_text = result[0]
        
        try:
            data = json.loads(response_text)
            
            # Extract topic sections and their items
            for section in data.get('topicSections', []):
                section_title = section.get('title', 'Other')
                # Create URL-safe folder name
                folder_name = self._slugify(section_title)
                
                # Track URLs in this topic
                topic_urls = []
                for identifier in section.get('identifiers', []):
                    if identifier.startswith('doc://'):
                        parts = identifier.split('/documentation/')
                        if len(parts) == 2:
                            path = parts[1]
                            if path.lower().startswith(self.framework_id.lower()):
                                doc_url = f"https://developer.apple.com/documentation/{path}"
                                topic_urls.append(doc_url)
                
                if topic_urls:
                    self.topic_hierarchy[folder_name] = {
                        'title': section_title,
                        'urls': topic_urls
                    }
            
            logger.info(
                "extracted_topic_hierarchy",
                framework=self.framework_name,
                topics=list(self.topic_hierarchy.keys())
            )
            
        except json.JSONDecodeError:
            logger.warning("failed_to_parse_framework_json", url=framework_json_url)
    
    def _slugify(self, text: str) -> str:
        """Convert text to URL-safe folder name."""
        import re
        # Convert to lowercase and replace spaces/special chars with hyphens
        slug = re.sub(r'[^\w\s-]', '', text.lower())
        slug = re.sub(r'[\s_-]+', '-', slug)
        return slug.strip('-')
    
    async def _discover_from_json(self, json_url: str) -> None:
        """Discover URLs from a JSON file.
        
        Args:
            json_url: URL of the JSON file
        """
        if json_url in self.processed_urls:
            return
        
        self.processed_urls.add(json_url)
        
        # Fetch the JSON data - for discovery, we need content even if unchanged
        result = await self.fetch_page_with_etag(json_url, use_etag=False)
        if not result:
            return
        response_text = result[0]
        
        try:
            data = json.loads(response_text)
            
            # This JSON file is valid documentation
            self.discovered_urls.add(json_url)
            
            # Extract related documentation from various sections
            sections_to_check = [
                'topicSections',
                'relationshipsSections', 
                'seeAlsoSections',
                'references'
            ]
            
            for section_name in sections_to_check:
                if section_name in data:
                    await self._extract_links_from_sections(data[section_name])
            
            # Check for child pages in primaryContentSections
            if 'primaryContentSections' in data:
                for section in data['primaryContentSections']:
                    if 'identifiers' in section:
                        await self._process_identifiers(section['identifiers'])
                        
        except json.JSONDecodeError:
            logger.debug("not_json_content", url=json_url)
    
    async def _extract_links_from_sections(self, sections: List[Dict]) -> None:
        """Extract documentation links from sections."""
        for section in sections:
            if isinstance(section, dict):
                # Look for identifiers
                if 'identifiers' in section:
                    await self._process_identifiers(section['identifiers'])
                
                # Look for nested items
                if 'items' in section:
                    for item in section['items']:
                        if 'identifier' in item:
                            await self._process_identifier(item['identifier'])
    
    async def _process_identifiers(self, identifiers: List[str]) -> None:
        """Process a list of identifiers."""
        for identifier in identifiers:
            await self._process_identifier(identifier)
    
    async def _process_identifier(self, identifier: str) -> None:
        """Process a single identifier and discover its JSON URL."""
        # Skip external symbols
        if 'externally.resolved' in identifier:
            return
        
        # Extract path from identifier like "doc://com.apple.SwiftUI/documentation/SwiftUI/Text"
        if identifier.startswith('doc://'):
            parts = identifier.split('/documentation/')
            if len(parts) == 2:
                path = parts[1]
                # Only process URLs for this framework
                if path.lower().startswith(self.framework_id.lower()):
                    json_url = f"{self.JSON_BASE_URL}/{path}.json"
                    if json_url not in self.processed_urls:
                        await self._discover_from_json(json_url)
    
    async def extract_page_data(self, soup: Any, url: str) -> Optional[Dict[str, Any]]:
        """Extract data from JSON instead of HTML.
        
        Args:
            soup: Ignored (for compatibility)
            url: Documentation URL
            
        Returns:
            Extracted data
        """
        # Convert to JSON URL
        json_url = self._convert_doc_url_to_json_url(url)
        
        # Fetch JSON data with ETag support for efficient caching
        result = await self.fetch_page_with_etag(json_url)
        if not result:
            # Either failed or 304 Not Modified (content unchanged)
            return None
        
        response_text, etag = result
        
        try:
            json_data = json.loads(response_text)
            # Basic validation
            if not self._validate_json_structure(json_data):
                logger.warning("invalid_json_structure", url=json_url)
                return None
            
            # Always store hash for the JSON URL (with or without ETag)
            self.hash_manager.update_hash(json_url, response_text, etag)
            
            # Also store hash for the documentation URL to track what we've scraped
            self.hash_manager.update_hash(url, response_text, etag)
            
            return self._extract_from_json(json_data, url)
        except json.JSONDecodeError as e:
            logger.error("json_parse_error", url=json_url, error=str(e))
            return None
    
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
        data['symbol_kind'] = metadata.get('symbolKind', '')
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
                    # Extract description from content
                    content = param.get('content', [])
                    for item in content:
                        if item.get('type') == 'paragraph':
                            desc_parts = []
                            for inline in item.get('inlineContent', []):
                                if inline.get('type') == 'text':
                                    desc_parts.append(inline['text'])
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
    
    async def save_page_data(self, url: str, data: Dict[str, Any]) -> None:
        """Save extracted data as markdown with organized folder structure.
        
        Args:
            url: Source URL
            data: Extracted data
        """
        # Ensure topic hierarchy is extracted for the main framework page
        if url == f'https://developer.apple.com/documentation/{self.framework_id}' and not self.topic_hierarchy:
            framework_json_url = f"{self.JSON_BASE_URL}/{self.framework_id}.json"
            await self._extract_topic_hierarchy(framework_json_url)
        
        # Convert to markdown
        markdown_content = self.markdown_converter.convert_page(data)
        
        # Determine organized file path
        file_path = self._get_organized_file_path(url, data)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save markdown file
        file_path.write_text(markdown_content, encoding='utf-8')
        
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
        
        # Clear URL caches periodically to manage memory
        if len(self.discovered_urls) > self._discovery_batch_size:
            self._cleanup_url_caches()
    
    def _get_organized_file_path(self, url: str, data: Dict[str, Any]) -> Path:
        """Generate organized file path based on URL hierarchy (mirrors Apple's structure).
        
        Args:
            url: Source URL
            data: Extracted data containing title and other metadata
            
        Returns:
            Path object for the organized file location following URL structure
        """
        # Extract the path components from URL (handle case-insensitive framework names)
        # WatchKit URLs use 'WatchKit' but framework_id is 'watchkit'
        framework_variants = [
            self.framework_id,
            self.framework_id.capitalize(),
            self.framework_id.upper(),
            self.framework_id.lower(),
            'WatchKit' if self.framework_id.lower() == 'watchkit' else self.framework_id
        ]
        
        framework_patterns = [f'https://developer.apple.com/documentation/{variant}' for variant in set(framework_variants)]
        
        url_path = None
        for pattern in framework_patterns:
            if url.startswith(pattern):
                url_path = url.replace(pattern, '').lstrip('/')
                break
        
        # Fallback if no pattern matches
        if url_path is None:
            logger.warning("failed_to_parse_url_path", url=url, framework_id=self.framework_id)
            # Use full URL as fallback (this was causing the https: folders)
            safe_url = url.replace('https://', '').replace('http://', '').replace('/', '-')
            return self.output_dir / f"{safe_url}.md"
        
        if not url_path:
            # Main framework page: watchkit.md
            return self.output_dir / f"{self.framework_id}.md"
        
        # Split path into segments
        path_segments = url_path.split('/')
        
        # Always use the full URL path structure, just with lowercase and clean filenames
        if len(path_segments) == 1:
            # Single segment: watchkit/enabling-background-sessions.md
            filename = self._create_clean_filename(path_segments[0], data)
            return self.output_dir / f"{filename}.md"
        else:
            # Multiple segments: watchkit/wkapplication/shared.md
            # All segments except last become folders
            folder_path = Path(*[segment.lower() for segment in path_segments[:-1]])
            filename = self._create_clean_filename(path_segments[-1], data)
            return self.output_dir / folder_path / f"{filename}.md"
    
    def _extract_api_name_from_url(self, url: str) -> str:
        """Extract the API name from the documentation URL."""
        # Handle the main framework page
        if url == f'https://developer.apple.com/documentation/{self.framework_id}':
            return self.framework_id
        
        # Remove framework prefix and get the last part
        url_path = url.replace(f'https://developer.apple.com/documentation/{self.framework_id}/', '')
        
        # If we still have the full URL, it means it didn't match the pattern above
        if url_path.startswith('https://'):
            # Extract from the full URL path
            path_parts = url.split('/')
            return path_parts[-1] if path_parts else 'unknown'
        
        # Get the last segment (the actual API name)
        if '/' in url_path:
            return url_path.split('/')[-1]
        return url_path or self.framework_id
    
    def _find_topic_folder_for_url(self, url: str) -> Optional[str]:
        """Find which topic folder this URL belongs to."""
        for folder_name, topic_info in self.topic_hierarchy.items():
            if url in topic_info['urls']:
                return folder_name
        
        # Fallback: try to match by URL pattern if direct match fails
        api_name = self._extract_api_name_from_url(url)
        for folder_name, topic_info in self.topic_hierarchy.items():
            for topic_url in topic_info['urls']:
                if api_name in topic_url:
                    return folder_name
        
        return None
    
    def _create_clean_filename(self, api_name: str, data: Dict[str, Any]) -> str:
        """Create a clean, readable filename."""
        # Start with the API name
        base_name = api_name
        
        # Handle special cases for better readability
        symbol_kind = data.get('symbol_kind', '').lower()
        
        # For methods, clean up parameter syntax but preserve important info
        if '(' in base_name and ')' in base_name:
            # Convert init?(rawValue: Int) -> init-rawvalue
            # Convert shared() -> shared
            # Convert applicationDidFinishLaunching() -> applicationdidfinishlaunching
            base_name = base_name.replace('?', '').replace('!', '')
            base_name = base_name.replace('(', '-').replace(')', '')
            base_name = base_name.replace(':', '').replace(' ', '').replace(',', '-')
        
        # Remove other special characters and convert to lowercase with hyphens
        clean_name = self._slugify(base_name)
        
        # Ensure it doesn't start with numbers or special chars
        if clean_name and clean_name[0].isdigit():
            clean_name = f"api-{clean_name}"
        
        return clean_name or 'unknown'
    
    def _cleanup_url_caches(self) -> None:
        """Clean up URL caches to prevent memory issues."""
        # Keep only recent processed URLs
        if len(self.processed_urls) > self._discovery_batch_size // 2:
            processed_list = list(self.processed_urls)
            # Keep the last half of processed URLs
            self.processed_urls = set(processed_list[-self._discovery_batch_size // 2:])
        
        # Clear discovered URLs that have been processed
        self.discovered_urls = self.discovered_urls - self.processed_urls
        
        logger.info(
            "cleaned_url_caches",
            discovered_count=len(self.discovered_urls),
            processed_count=len(self.processed_urls)
        )
    
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
            
            # Handle any nested content recursively for item types that don't process content themselves
            # Skip recursive processing for items that handle their own content (aside, table, etc.)
            if ('content' in item and isinstance(item['content'], list) and 
                item_type not in ['aside', 'table', 'imageBlock']):
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
    
    def create_framework_readme(self) -> None:
        """Create a README.md file for the framework with overview and navigation."""
        readme_path = self.output_dir / "README.md"
        
        content = f"""# {self.framework_name} Documentation

{self._get_framework_description()}

## Overview

{self._get_framework_overview()}

## Getting Started

```swift
import {self.framework_name.replace(' ', '')}

// Basic example code here
```

## Topics

{self._get_organized_topics()}

## Platform Requirements

{self._get_platform_requirements()}

---
*Source: [Apple Developer - {self.framework_name}](https://developer.apple.com/documentation/{self.framework_id})*
"""
        
        readme_path.write_text(content, encoding='utf-8')
        logger.info("created_framework_readme", framework=self.framework_name)
    
    def _get_framework_description(self) -> str:
        """Get framework description based on known frameworks."""
        descriptions = {
            "swiftui": "SwiftUI is Apple's modern declarative framework for building user interfaces across all Apple platforms.",
            "uikit": "UIKit provides the window and view architecture for implementing your interface on iOS and tvOS.",
            "metal": "Metal provides near-direct access to the graphics processing unit (GPU) for high-performance graphics and compute.",
            "foundation": "Foundation provides a base layer of functionality for apps and frameworks.",
            "coreml": "Core ML integrates machine learning models into your app.",
            "arkit": "ARKit combines device motion tracking, camera scene capture, and advanced scene processing.",
        }
        return descriptions.get(self.framework_id.lower(), 
                               f"{self.framework_name} framework for Apple platforms.")
    
    def _get_framework_overview(self) -> str:
        """Get framework overview text."""
        # This could be enhanced to fetch from the framework's main JSON
        return f"The {self.framework_name} framework provides essential functionality for Apple platform development."
    
    def _get_organized_topics(self) -> str:
        """Get organized topic list based on extracted hierarchy."""
        if not self.topic_hierarchy:
            return "- Getting Started\n- Key Concepts\n- Common Tasks\n- Best Practices"
        
        topics = []
        for folder_name, topic_info in self.topic_hierarchy.items():
            title = topic_info['title']
            topics.append(f"- [{title}]({folder_name}/)")
        
        return "\n".join(topics)
    
    def _get_platform_requirements(self) -> str:
        """Get platform requirements."""
        # This could be enhanced based on discovered documentation
        return "- iOS 13.0+\n- macOS 10.15+\n- tvOS 13.0+\n- watchOS 6.0+"