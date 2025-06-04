"""Browser-based scraper for JavaScript-rendered Apple documentation."""

import json
import re
from typing import Any, Dict, List, Optional, Set
from urllib.parse import urljoin

from scraper.base import BaseAppleScraper
from scraper.utils.logger import get_logger
from scraper.utils.markdown_converter import AppleDocMarkdownConverter

logger = get_logger(__name__)


class BrowserAppleDocumentationScraper(BaseAppleScraper):
    """Browser-based scraper for Apple documentation that handles JavaScript rendering.
    
    This scraper is designed to work with external browser automation tools
    like Puppeteer via MCP or pyppeteer.
    """
    
    def __init__(self, framework_id: str, framework_name: Optional[str] = None) -> None:
        """Initialize browser-based scraper.
        
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
    
    async def extract_page_data_from_browser(self, page_content: str, url: str) -> Optional[Dict[str, Any]]:
        """Extract data from browser-rendered page content.
        
        This method expects the page content to be extracted via browser automation
        and passed as a string containing the extracted data in JSON format.
        
        Args:
            page_content: JSON string with extracted page data
            url: Source URL
            
        Returns:
            Extracted data dictionary
        """
        try:
            # Parse the extracted data
            data = json.loads(page_content)
            
            # Add metadata
            data['source_url'] = url
            data['framework'] = self.framework_name
            data['framework_id'] = self.framework_id
            
            return data
            
        except json.JSONDecodeError as e:
            logger.error(
                "failed_to_parse_browser_data",
                url=url,
                error=str(e)
            )
            return None
        except Exception as e:
            logger.error(
                "browser_extraction_error",
                url=url,
                error=str(e)
            )
            return None
    
    @staticmethod
    def get_browser_extraction_script() -> str:
        """Get JavaScript code to extract data from Apple documentation pages.
        
        This script should be executed in the browser context to extract
        structured data from the rendered page.
        
        Returns:
            JavaScript code as a string
        """
        return '''
        (() => {
            const data = {
                title: '',
                brief_description: '',
                availability: [],
                declaration: {},
                parameters: [],
                return_value: '',
                overview: '',
                code_examples: [],
                topics: [],
                see_also: []
            };
            
            // Extract title
            const h1 = document.querySelector('h1');
            if (h1) data.title = h1.textContent.trim();
            
            // Extract brief description
            const brief = document.querySelector('.abstract, .intro, p.lead');
            if (brief) data.brief_description = brief.textContent.trim();
            
            // Extract availability
            const availBadges = document.querySelectorAll('.availability .badge, .availability span');
            availBadges.forEach(badge => {
                const text = badge.textContent.trim();
                const match = text.match(/^(.+?)\\s+([0-9.]+\\+?)$/);
                if (match) {
                    data.availability.push({
                        platform: match[1],
                        version: match[2]
                    });
                }
            });
            
            // Extract declaration
            const declSection = document.querySelector('.declaration, section.declaration');
            if (declSection) {
                const swiftCode = declSection.querySelector('code.swift, .language-swift');
                if (swiftCode) {
                    data.declaration.swift = swiftCode.textContent.trim();
                }
                const objcCode = declSection.querySelector('code.objc, .language-objc');
                if (objcCode) {
                    data.declaration.objc = objcCode.textContent.trim();
                }
            }
            
            // Extract overview
            const overviewSection = document.querySelector('#overview, section.overview');
            if (overviewSection) {
                // Get HTML content for proper conversion
                const content = overviewSection.cloneNode(true);
                // Remove the heading
                const heading = content.querySelector('h2');
                if (heading) heading.remove();
                data.overview = content.innerHTML;
            }
            
            // Extract parameters
            const paramSection = document.querySelector('#parameters, section.parameters');
            if (paramSection) {
                const paramItems = paramSection.querySelectorAll('dt, .param-item');
                paramItems.forEach(item => {
                    const name = item.querySelector('code')?.textContent.trim();
                    const desc = item.nextElementSibling?.textContent.trim();
                    if (name) {
                        data.parameters.push({
                            name: name,
                            description: desc || ''
                        });
                    }
                });
            }
            
            // Extract return value
            const returnSection = document.querySelector('#return-value, section.return-value');
            if (returnSection) {
                const content = returnSection.cloneNode(true);
                const heading = content.querySelector('h2, h3');
                if (heading) heading.remove();
                data.return_value = content.textContent.trim();
            }
            
            // Extract code examples
            const exampleSections = document.querySelectorAll('.code-example, .code-listing');
            exampleSections.forEach(section => {
                const example = {};
                const title = section.querySelector('h3, h4, .code-voice');
                if (title) example.title = title.textContent.trim();
                
                const desc = section.querySelector('p');
                if (desc) example.description = desc.textContent.trim();
                
                const code = section.querySelector('pre code, code.code-voice');
                if (code) {
                    example.code = code.textContent.trim();
                    const classes = code.className;
                    example.language = classes.includes('swift') ? 'swift' : 
                                     classes.includes('objc') ? 'objc' : 'swift';
                }
                
                if (example.code) data.code_examples.push(example);
            });
            
            // Extract topics/related APIs
            const topicsSection = document.querySelector('#topics, section.topics');
            if (topicsSection) {
                const groups = topicsSection.querySelectorAll('.topic-group, section');
                groups.forEach(group => {
                    const topic = {};
                    const title = group.querySelector('h3, h4');
                    if (title) topic.title = title.textContent.trim();
                    
                    topic.items = [];
                    const links = group.querySelectorAll('a');
                    links.forEach(link => {
                        const item = {
                            name: link.textContent.trim(),
                            url: link.href
                        };
                        const desc = link.parentElement.querySelector('p');
                        if (desc) item.description = desc.textContent.trim();
                        topic.items.push(item);
                    });
                    
                    if (topic.items.length > 0) data.topics.push(topic);
                });
            }
            
            // Extract see also
            const seeAlsoSection = document.querySelector('#see-also, section.see-also');
            if (seeAlsoSection) {
                const links = seeAlsoSection.querySelectorAll('a');
                links.forEach(link => {
                    data.see_also.push({
                        title: link.textContent.trim(),
                        url: link.href
                    });
                });
            }
            
            return JSON.stringify(data);
        })();
        '''