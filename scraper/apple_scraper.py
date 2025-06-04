"""Generic Apple documentation scraper that works for any framework."""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, Tag

from scraper.base import BaseAppleScraper
from scraper.utils.logger import get_logger
from scraper.utils.markdown_converter import AppleDocMarkdownConverter

logger = get_logger(__name__)


class AppleDocumentationScraper(BaseAppleScraper):
    """Generic scraper for any Apple documentation framework."""
    
    def __init__(self, framework_id: str, framework_name: Optional[str] = None) -> None:
        """Initialize scraper for a specific framework.
        
        Args:
            framework_id: Framework identifier (e.g., 'swiftui', 'uikit')
            framework_name: Human-readable name (defaults to framework_id)
        """
        super().__init__(
            framework_id=framework_id,
            framework_name=framework_name or framework_id.replace('-', ' ').title()
        )
        self.markdown_converter = AppleDocMarkdownConverter()
        self.discovered_urls: Set[str] = set()
        self.processed_urls: Set[str] = set()
    
    async def discover_urls(self) -> List[str]:
        """Discover all documentation URLs for the framework."""
        logger.info("discovering_urls", framework=self.framework_name)
        
        # Start with the framework's main page
        await self._discover_from_page(self.base_url)
        
        # Also check common sections
        common_sections = [
            "essentials", "app-structure", "data-and-storage", "views",
            "user-interface", "drawing-and-graphics", "animations",
            "app-services", "media", "web", "developer-tools"
        ]
        
        for section in common_sections:
            section_url = f"{self.base_url}/{section}"
            await self._discover_from_page(section_url)
        
        # Convert set to sorted list
        urls = sorted(list(self.discovered_urls))
        logger.info(
            "urls_discovered",
            framework=self.framework_name,
            total=len(urls),
            sample=urls[:5] if urls else []
        )
        
        return urls
    
    async def _discover_from_page(self, url: str) -> None:
        """Discover URLs from a single page.
        
        Args:
            url: Page URL to discover from
        """
        if url in self.processed_urls:
            return
        
        self.processed_urls.add(url)
        content = await self.fetch_page(url)
        
        if not content:
            return
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all documentation links
        for link in soup.find_all('a', href=True):
            href = link['href']
            
            # Convert relative URLs to absolute
            absolute_url = urljoin(url, href)
            
            # Check if it's a documentation URL for this framework
            if self._is_valid_doc_url(absolute_url):
                self.discovered_urls.add(absolute_url)
                
                # If it's a category page, explore it too
                if self._is_category_page(absolute_url, link):
                    await self._discover_from_page(absolute_url)
    
    def _is_valid_doc_url(self, url: str) -> bool:
        """Check if URL is a valid documentation URL for this framework.
        
        Args:
            url: URL to check
            
        Returns:
            True if valid documentation URL
        """
        parsed = urlparse(url)
        path = parsed.path
        
        # Must be on Apple developer site
        if parsed.netloc != "developer.apple.com":
            return False
        
        # Must be in documentation section
        if not path.startswith("/documentation/"):
            return False
        
        # Must be for this framework
        if not path.startswith(f"/documentation/{self.framework_id}"):
            return False
        
        # Exclude certain types of pages
        excluded_patterns = [
            '/changes/', '/revisions/', '?changes=',
            '.json', '.xml', '.rss', '/feed'
        ]
        
        for pattern in excluded_patterns:
            if pattern in path:
                return False
        
        return True
    
    def _is_category_page(self, url: str, link_element: Tag) -> bool:
        """Check if a URL is likely a category/index page.
        
        Args:
            url: URL to check
            link_element: The link element
            
        Returns:
            True if likely a category page
        """
        # Check URL patterns
        path = urlparse(url).path
        category_patterns = [
            '/essentials', '/fundamentals', '/overview',
            '-organization', '-structure', '-data',
            '/views', '/controls', '/layouts'
        ]
        
        for pattern in category_patterns:
            if pattern in path:
                return True
        
        # Check link context
        parent = link_element.parent
        if parent and parent.name in ['h2', 'h3', 'h4']:
            return True
        
        # Check CSS classes
        classes = link_element.get('class', [])
        if any('category' in cls or 'section' in cls for cls in classes):
            return True
        
        return False
    
    async def extract_page_data(self, soup: BeautifulSoup, url: str) -> Optional[Dict[str, Any]]:
        """Extract structured data from a documentation page.
        
        Args:
            soup: BeautifulSoup object
            url: Page URL
            
        Returns:
            Extracted data
        """
        data = {
            'source_url': url,
            'framework': self.framework_name,
            'framework_id': self.framework_id
        }
        
        # Extract title
        title_elem = soup.find('h1') or soup.find('title')
        if title_elem:
            data['title'] = title_elem.get_text().strip()
        else:
            logger.warning("no_title_found", url=url)
            return None
        
        # Extract metadata
        data.update(self._extract_metadata(soup))
        
        # Extract availability
        data['availability'] = self._extract_availability(soup)
        
        # Extract declaration
        data['declaration'] = self._extract_declaration(soup)
        
        # Extract brief description
        brief = soup.find('div', class_='abstract') or soup.find('p', class_='intro')
        if brief:
            data['brief_description'] = brief.get_text().strip()
        
        # Extract overview/discussion
        overview = self._extract_section(soup, ['overview', 'discussion'])
        if overview:
            data['overview'] = str(overview)
        
        # Extract parameters
        data['parameters'] = self._extract_parameters(soup)
        
        # Extract return value
        return_section = self._extract_section(soup, ['return-value', 'returns'])
        if return_section:
            data['return_value'] = return_section.get_text().strip()
        
        # Extract code examples
        data['code_examples'] = self._extract_code_examples(soup)
        
        # Extract topics/related APIs
        data['topics'] = self._extract_topics(soup)
        
        # Extract see also section
        data['see_also'] = self._extract_see_also(soup)
        
        return data
    
    def _extract_metadata(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Extract metadata like SDK, module, import statements."""
        metadata = {}
        
        # Look for metadata in various locations
        meta_section = soup.find('section', class_='metadata')
        if meta_section:
            for item in meta_section.find_all('div', class_='metadata-item'):
                label = item.find('span', class_='metadata-label')
                value = item.find('span', class_='metadata-value')
                if label and value:
                    key = label.get_text().strip().lower().replace(' ', '_')
                    metadata[key] = value.get_text().strip()
        
        # Extract import statement
        import_elem = soup.find('code', string=lambda s: s and s.startswith('import '))
        if import_elem:
            metadata['import_statement'] = import_elem.get_text().strip()
        
        # Extract inheritance
        inherits = soup.find('span', string='Inherits From')
        if inherits and inherits.next_sibling:
            metadata['inherits_from'] = inherits.next_sibling.get_text().strip()
        
        # Extract conformance
        conforms = soup.find('span', string='Conforms To')
        if conforms and conforms.next_sibling:
            protocols = [p.strip() for p in conforms.next_sibling.get_text().split(',')]
            metadata['conforms_to'] = protocols
        
        return metadata
    
    def _extract_availability(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        """Extract platform availability information."""
        availability = []
        
        # Look for availability badges/tags
        availability_section = soup.find('section', class_='availability')
        if availability_section:
            for badge in availability_section.find_all(['span', 'div'], class_='badge'):
                text = badge.get_text().strip()
                parts = text.split(' ', 1)
                if len(parts) >= 2:
                    availability.append({
                        'platform': parts[0],
                        'version': parts[1]
                    })
        
        # Also check inline availability
        for elem in soup.find_all(text=lambda t: 'Available in' in t or 'Deprecated in' in t):
            parent = elem.parent
            if parent:
                text = parent.get_text().strip()
                # Parse availability text
                if 'Available in' in text:
                    parts = text.split('Available in')[1].strip().split(',')
                    for part in parts:
                        part = part.strip()
                        if ' ' in part:
                            platform, version = part.split(' ', 1)
                            availability.append({
                                'platform': platform,
                                'version': version
                            })
        
        return availability
    
    def _extract_declaration(self, soup: BeautifulSoup) -> Dict[str, str]:
        """Extract code declarations."""
        declarations = {}
        
        # Look for declaration section
        declaration_section = soup.find('section', class_='declaration')
        if declaration_section:
            # Swift declaration
            swift_code = declaration_section.find('code', class_='swift')
            if swift_code:
                declarations['swift'] = swift_code.get_text().strip()
            
            # Objective-C declaration
            objc_code = declaration_section.find('code', class_='objc')
            if objc_code:
                declarations['objc'] = objc_code.get_text().strip()
        
        # Alternative: look for pre blocks with language classes
        if not declarations:
            for pre in soup.find_all('pre'):
                code = pre.find('code')
                if code:
                    classes = code.get('class', [])
                    if 'language-swift' in classes or 'swift' in classes:
                        declarations['swift'] = code.get_text().strip()
                    elif 'language-objc' in classes or 'objc' in classes:
                        declarations['objc'] = code.get_text().strip()
        
        return declarations
    
    def _extract_section(self, soup: BeautifulSoup, section_names: List[str]) -> Optional[Tag]:
        """Extract a section by multiple possible names."""
        for name in section_names:
            # Try finding by ID
            section = soup.find(id=name)
            if section:
                return section
            
            # Try finding by class
            section = soup.find('section', class_=name)
            if section:
                return section
            
            # Try finding by heading
            heading = soup.find(['h2', 'h3'], string=lambda s: s and name.lower() in s.lower())
            if heading:
                # Get content after heading
                content = []
                for sibling in heading.find_next_siblings():
                    if sibling.name in ['h2', 'h3']:
                        break
                    content.append(str(sibling))
                if content:
                    return BeautifulSoup(''.join(content), 'html.parser')
        
        return None
    
    def _extract_parameters(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        """Extract parameter information."""
        parameters = []
        
        param_section = self._extract_section(soup, ['parameters', 'params'])
        if param_section:
            # Look for parameter list
            for param_item in param_section.find_all(['dt', 'li']):
                param_name = param_item.find('code')
                if param_name:
                    param_desc = param_item.find_next_sibling(['dd', 'p'])
                    param_data = {
                        'name': param_name.get_text().strip()
                    }
                    if param_desc:
                        param_data['description'] = param_desc.get_text().strip()
                    
                    # Try to extract type
                    type_elem = param_item.find('span', class_='type')
                    if type_elem:
                        param_data['type'] = type_elem.get_text().strip()
                    
                    parameters.append(param_data)
        
        return parameters
    
    def _extract_code_examples(self, soup: BeautifulSoup) -> List[Dict[str, Any]]:
        """Extract code examples."""
        examples = []
        
        # Look for code example sections
        example_sections = soup.find_all('section', class_=['code-example', 'example'])
        for section in example_sections:
            example = {}
            
            # Get title
            title = section.find(['h3', 'h4'])
            if title:
                example['title'] = title.get_text().strip()
            
            # Get description
            desc = section.find('p')
            if desc:
                example['description'] = desc.get_text().strip()
            
            # Get code
            code_block = section.find('pre') or section.find('code')
            if code_block:
                example['code'] = code_block.get_text().strip()
                
                # Detect language
                code_elem = code_block.find('code') if code_block.name == 'pre' else code_block
                if code_elem:
                    classes = code_elem.get('class', [])
                    for cls in classes:
                        if 'language-' in cls:
                            example['language'] = cls.replace('language-', '')
                            break
                    else:
                        example['language'] = 'swift'  # Default for Apple docs
            
            if 'code' in example:
                examples.append(example)
        
        return examples
    
    def _extract_topics(self, soup: BeautifulSoup) -> List[Dict[str, Any]]:
        """Extract topics/related APIs."""
        topics = []
        
        topics_section = self._extract_section(soup, ['topics', 'related'])
        if topics_section:
            # Find topic groups
            for group in topics_section.find_all(['section', 'div'], class_='topic-group'):
                topic = {}
                
                # Get group title
                title = group.find(['h3', 'h4'])
                if title:
                    topic['title'] = title.get_text().strip()
                
                # Get items in group
                items = []
                for link in group.find_all('a'):
                    item = {
                        'name': link.get_text().strip(),
                        'url': urljoin(self.base_url, link.get('href', ''))
                    }
                    
                    # Get description if available
                    desc = link.find_next_sibling('p')
                    if desc:
                        item['description'] = desc.get_text().strip()
                    
                    items.append(item)
                
                if items:
                    topic['items'] = items
                    topics.append(topic)
        
        return topics
    
    def _extract_see_also(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        """Extract see also links."""
        see_also = []
        
        see_also_section = self._extract_section(soup, ['see-also', 'seealso', 'related-documentation'])
        if see_also_section:
            for link in see_also_section.find_all('a'):
                see_also.append({
                    'title': link.get_text().strip(),
                    'url': urljoin(self.base_url, link.get('href', ''))
                })
        
        return see_also
    
    async def save_page_data(self, url: str, data: Dict[str, Any]) -> None:
        """Save extracted data as markdown.
        
        Args:
            url: Source URL
            data: Extracted data
        """
        # Convert to markdown
        markdown_content = self.markdown_converter.convert_page(data)
        
        # Determine file path
        file_path = self.output_dir / self.get_relative_path(url)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save markdown file
        file_path.write_text(markdown_content, encoding='utf-8')
        
        logger.debug(
            "saved_page",
            url=url,
            file=str(file_path),
            size=len(markdown_content)
        )