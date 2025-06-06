"""Convert Apple documentation HTML to clean markdown."""

import re
from pathlib import Path
from typing import Dict, List, Optional, Any

import markdownify
from bs4 import BeautifulSoup, NavigableString, Tag

from scraper.utils.logger import get_logger

logger = get_logger(__name__)


class AppleDocMarkdownConverter:
    """Convert Apple documentation HTML to markdown with proper formatting."""
    
    def __init__(self, output_dir: Optional[Path] = None) -> None:
        """Initialize markdown converter.
        
        Args:
            output_dir: Directory where markdown files are saved for cross-linking
        """
        self.converter = markdownify.MarkdownConverter(
            heading_style="ATX",
            autolinks=False,
            code_language_callback=self._detect_language,
            strip=["style", "script"],
        )
        self.output_dir = output_dir
    
    def _detect_language(self, el: Tag) -> Optional[str]:
        """Detect programming language from code element.
        
        Args:
            el: BeautifulSoup Tag element
            
        Returns:
            Language identifier or None
        """
        # Check class names
        classes = el.get("class", [])
        for cls in classes:
            if "language-swift" in cls or "swift" in cls.lower():
                return "swift"
            elif "language-objc" in cls or "objective-c" in cls.lower():
                return "objc"
            elif "language-c" in cls or cls == "c":
                return "c"
            elif "language-cpp" in cls or "c++" in cls.lower():
                return "cpp"
            elif "language-metal" in cls or "metal" in cls.lower():
                return "metal"
            elif "language-javascript" in cls or "js" in cls.lower():
                return "javascript"
            elif "language-json" in cls:
                return "json"
        
        # Check data attributes
        if el.get("data-language"):
            return el["data-language"]
        
        # Default to Swift for Apple docs
        return "swift"
    
    def convert_page(self, data: Dict[str, Any]) -> str:
        """Convert extracted page data to markdown.
        
        Args:
            data: Extracted page data
            
        Returns:
            Formatted markdown content
        """
        sections = []
        
        # Title and metadata
        sections.append(f"# {data.get('title', 'Untitled')}")
        sections.append(self._format_metadata(data))
        
        # Brief description
        if data.get('brief_description'):
            sections.append(data['brief_description'])
        
        # Availability badges
        if data.get('availability'):
            sections.append(self._format_availability(data['availability']))
        
        # Declaration
        if data.get('declaration'):
            sections.append("## Declaration")
            sections.append(self._format_code_block(
                data['declaration'].get('swift', ''),
                'swift'
            ))
            if data['declaration'].get('objc'):
                sections.append(self._format_code_block(
                    data['declaration']['objc'],
                    'objc'
                ))
        
        # Mentions (related documentation links) - comes right after Declaration per Apple's structure
        if data.get('mentions'):
            sections.append("## Mentions")
            sections.append(self._format_mentions(data['mentions']))
        
        # Main content - preserves the original structure with inline code examples
        if data.get('content'):
            # The content field now contains everything in the original order
            # including headings, paragraphs, and code examples
            sections.append(data['content'])
        
        # Legacy fields for backward compatibility (if still present)
        if data.get('overview') and not data.get('content'):
            sections.append("## Overview")
            sections.append(data['overview'])
        
        # Parameters
        if data.get('parameters'):
            sections.append("## Parameters")
            sections.append(self._format_parameters(data['parameters']))
        
        # Return value
        if data.get('return_value'):
            sections.append("## Return Value")
            sections.append(data['return_value'])
        
        # Discussion (legacy - only if content not present)
        if data.get('discussion') and not data.get('content'):
            sections.append("## Discussion")
            sections.append(data['discussion'])
        
        # Code examples (legacy - only if not already in content)
        if data.get('code_examples') and not data.get('content'):
            sections.append("## Code Examples")
            for example in data['code_examples']:
                if example.get('title'):
                    sections.append(f"### {example['title']}")
                if example.get('description'):
                    sections.append(example['description'])
                if example.get('code'):
                    sections.append(self._format_code_block(
                        example['code'],
                        example.get('language', 'swift')
                    ))
        
        # Topics/Related APIs (main content section)
        if data.get('topics'):
            sections.append("## Topics")
            sections.append(self._format_topics(data['topics']))
        
        # Tasks/Tutorial content
        if data.get('tasks'):
            sections.append("## Tasks")
            for task in data['tasks']:
                sections.append(f"### {task.get('title', 'Task')}")
                sections.append(task.get('content', ''))
        
        # REST API Documentation
        if data.get('rest_body'):
            sections.append("## Request Body")
            sections.append(data['rest_body'])
        
        if data.get('rest_responses'):
            sections.append("## Responses")
            sections.append(data['rest_responses'])
        
        # Possible Values (for enums/options)
        if data.get('possible_values'):
            sections.append("## Possible Values")
            sections.append(data['possible_values'])
        
        # Thrown Errors
        if data.get('thrown_errors'):
            sections.append("## Thrown Errors")
            sections.append(data['thrown_errors'])
        
        # Relationships (Inherited By, Conforming Types, etc.)
        if data.get('relationships'):
            sections.append("## Relationships")
            sections.append(self._format_relationships(data['relationships']))
        
        # See Also (should be near the end)
        if data.get('see_also'):
            sections.append("## See Also")
            sections.append(self._format_see_also(data['see_also']))
        
        # Source URL
        if data.get('source_url'):
            sections.append(f"\n---\n\n*[View on Apple Developer]({data['source_url']})*")
        
        return "\n\n".join(filter(None, sections))
    
    def _format_metadata(self, data: Dict[str, Any]) -> str:
        """Format metadata section."""
        lines = []
        
        if data.get('framework'):
            lines.append(f"**Framework**: {data['framework']}")
        
        if data.get('module'):
            lines.append(f"**Module**: {data['module']}")
        
        if data.get('sdk'):
            lines.append(f"**SDK**: {data['sdk']}")
        
        if data.get('import_statement'):
            lines.append(f"**Import**: `{data['import_statement']}`")
        
        if data.get('inherits_from'):
            lines.append(f"**Inherits From**: {data['inherits_from']}")
        
        if data.get('conforms_to'):
            protocols = ", ".join(data['conforms_to'])
            lines.append(f"**Conforms To**: {protocols}")
        
        if data.get('symbol_kind'):
            lines.append(f"**Kind**: {data['symbol_kind']}")
            
        if data.get('required'):
            lines.append("**Required**: Yes")
        
        return "  \n".join(lines) if lines else ""
    
    def _format_availability(self, availability: List[Dict[str, str]]) -> str:
        """Format availability information."""
        if not availability:
            return ""
        
        lines = ["**Availability**:"]
        for item in availability:
            platform = item.get('platform', 'Unknown')
            version = item.get('version', '')
            
            line = f"- {platform} {version}"
            
            # Add beta indicator
            if item.get('beta', False):
                line += " (Beta)"
            
            # Add deprecation information
            if item.get('deprecated', False):
                dep_info = "Deprecated"
                if item.get('deprecated_at'):
                    dep_info += f" in {item['deprecated_at']}"
                if item.get('deprecation_message'):
                    dep_info += f": {item['deprecation_message']}"
                line += f" - {dep_info}"
            
            lines.append(line)
        
        return "\n".join(lines)
    
    def _convert_to_local_link(self, apple_url: str, link_text: str) -> str:
        """Convert Apple documentation URL to local markdown link if file exists.
        
        Args:
            apple_url: Apple documentation URL
            link_text: Text to display for the link
            
        Returns:
            Markdown link (local if file exists, otherwise Apple URL)
        """
        if not self.output_dir or not apple_url.startswith('https://developer.apple.com/documentation/'):
            return f"[{link_text}]({apple_url})"
        
        # Extract path from Apple URL
        try:
            url_path = apple_url.replace('https://developer.apple.com/documentation/', '')
            
            # Convert to local markdown path
            # e.g., "uikit/uitableviewdatasource" -> "uitableviewdatasource.md"
            path_parts = url_path.split('/')
            if len(path_parts) >= 2:
                framework = path_parts[0]
                api_name = path_parts[-1]  # Get the last part (actual API name)
                
                # Look for corresponding markdown file
                local_file = self.output_dir / f"{api_name}.md"
                
                if local_file.exists():
                    # Create relative path from current location
                    relative_path = f"{api_name}.md"
                    return f"[{link_text}]({relative_path})"
        
        except Exception:
            # If anything goes wrong, fall back to Apple URL
            pass
        
        # Fallback to Apple URL
        return f"[{link_text}]({apple_url})"
    
    def _format_code_block(self, code: str, language: str = "swift") -> str:
        """Format a code block with proper language tag."""
        if not code:
            return ""
        
        # Clean up code
        code = code.strip()
        
        return f"```{language}\n{code}\n```"
    
    def _convert_html_content(self, html: str) -> str:
        """Convert HTML content to markdown."""
        if not html:
            return ""
        
        # Pre-process HTML to handle Apple-specific patterns
        soup = BeautifulSoup(html, 'html.parser')
        
        # Handle code samples
        for code in soup.find_all('code'):
            # Preserve inline code
            if code.parent.name != 'pre':
                code.string = f"`{code.get_text()}`"
        
        # Handle aside/note blocks
        for aside in soup.find_all('aside'):
            aside_type = aside.get('class', ['note'])[0]
            content = aside.get_text().strip()
            
            if aside_type == 'warning':
                aside.string = f"> ⚠️ **Warning**: {content}"
            elif aside_type == 'important':
                aside.string = f"> ❗ **Important**: {content}"
            else:
                aside.string = f"> **Note**: {content}"
        
        # Convert to markdown
        markdown = self.converter.convert(str(soup))
        
        # Post-process markdown
        markdown = self._clean_markdown(markdown)
        
        return markdown
    
    def _clean_markdown(self, markdown: str) -> str:
        """Clean up converted markdown."""
        # Remove excessive blank lines
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        
        # Fix code block formatting
        markdown = re.sub(r'```\s*\n\s*```', '', markdown)
        
        # Remove trailing spaces
        markdown = re.sub(r' +$', '', markdown, flags=re.MULTILINE)
        
        return markdown.strip()
    
    def _format_parameters(self, parameters: List[Dict[str, str]]) -> str:
        """Format parameter list."""
        if not parameters:
            return ""
        
        lines = []
        for param in parameters:
            name = param.get('name', 'unknown')
            description = param.get('description', '')
            param_type = param.get('type', '')
            
            if param_type:
                lines.append(f"- `{name}` ({param_type}): {description}")
            else:
                lines.append(f"- `{name}`: {description}")
        
        return "\n".join(lines)
    
    def _convert_to_local_link(self, apple_url: str, link_text: str) -> str:
        """Convert Apple documentation URL to local markdown link if file exists.
        
        Args:
            apple_url: Apple documentation URL
            link_text: Text to display for the link
            
        Returns:
            Markdown link (local if file exists, otherwise Apple URL)
        """
        if not self.output_dir or not apple_url.startswith('https://developer.apple.com/documentation/'):
            return f"[{link_text}]({apple_url})"
        
        # Extract path from Apple URL
        try:
            url_path = apple_url.replace('https://developer.apple.com/documentation/', '')
            
            # Convert to local markdown path
            # e.g., "uikit/uitableviewdatasource" -> "uitableviewdatasource.md"
            path_parts = url_path.split('/')
            if len(path_parts) >= 2:
                framework = path_parts[0]
                api_name = path_parts[-1]  # Get the last part (actual API name)
                
                # Look for corresponding markdown file
                local_file = self.output_dir / f"{api_name}.md"
                
                if local_file.exists():
                    # Create relative path from current location
                    relative_path = f"{api_name}.md"
                    return f"[{link_text}]({relative_path})"
        
        except Exception:
            # If anything goes wrong, fall back to Apple URL
            pass
        
        # Fallback to Apple URL
        return f"[{link_text}]({apple_url})"
    
    def _format_topics(self, topics: List[Dict[str, Any]]) -> str:
        """Format topics/related APIs section."""
        if not topics:
            return ""
        
        lines = []
        for topic in topics:
            title = topic.get('title', '')
            if title:
                lines.append(f"### {title}")
            
            for item in topic.get('items', []):
                name = item.get('name', '')
                url = item.get('url', '')
                description = item.get('description', '')
                
                if url:
                    dual_link = self._create_dual_link(url, name)
                    lines.append(f"- {dual_link}")
                else:
                    lines.append(f"- {name}")
                
                if description:
                    lines.append(f"  {description}")
        
        return "\n".join(lines)
    
    def _format_see_also(self, see_also: List[Dict[str, str]]) -> str:
        """Format see also section."""
        if not see_also:
            return ""
        
        lines = []
        for item in see_also:
            title = item.get('title', '')
            url = item.get('url', '')
            description = item.get('description', '')
            
            if url:
                dual_link = self._create_dual_link(url, title)
                if description:
                    lines.append(f"- {dual_link}")
                    lines.append(f"  {description}")
                else:
                    lines.append(f"- {dual_link}")
            else:
                if description:
                    lines.append(f"- {title}")
                    lines.append(f"  {description}")
                else:
                    lines.append(f"- {title}")
        
        return "\n".join(lines)
    
    def _format_relationships(self, relationships: List[Dict[str, Any]]) -> str:
        """Format relationships section (Inherited By, Conforming Types, etc.)."""
        if not relationships:
            return ""
        
        lines = []
        for relationship in relationships:
            title = relationship.get('title', '')
            if title:
                lines.append(f"### {title}")
            
            for item in relationship.get('items', []):
                name = item.get('name', '')
                url = item.get('url', '')
                
                if url:
                    dual_link = self._create_dual_link(url, name)
                    lines.append(f"- {dual_link}")
                else:
                    lines.append(f"- {name}")
        
        return "\n".join(lines)
    
    def _format_mentions(self, mentions: List[Dict[str, str]]) -> str:
        """Format mentions section."""
        if not mentions:
            return ""
        
        lines = []
        for item in mentions:
            title = item.get('title', '')
            url = item.get('url', '')
            
            if url:
                dual_link = self._create_dual_link(url, title)
                lines.append(f"- {dual_link}")
            else:
                lines.append(f"- {title}")
        
        return "\n".join(lines)
    
    def _create_dual_link(self, apple_url: str, link_text: str) -> str:
        """Create a local markdown link from an Apple documentation URL.
        
        Args:
            apple_url: Apple documentation URL
            link_text: Text to display for the link
            
        Returns:
            Markdown link to local file (or Apple URL for cross-framework references)
        """
        if not self.output_dir or not apple_url.startswith('https://developer.apple.com/documentation/'):
            return f"[{link_text}]({apple_url})"
        
        # Extract API name from Apple URL
        try:
            url_path = apple_url.replace('https://developer.apple.com/documentation/', '')
            path_parts = url_path.split('/')
            
            if len(path_parts) >= 1:
                # Check if this is a cross-framework reference
                framework_in_url = path_parts[0].lower()
                current_framework = str(self.output_dir.name).lower()
                
                if framework_in_url != current_framework:
                    # Cross-framework reference - link to other framework's local files
                    if len(path_parts) == 2:
                        # Direct child of other framework: ../Swift/BitwiseCopyable.md
                        cross_framework_path = f"../{path_parts[0]}/{path_parts[1]}.md"
                    else:
                        # Nested path in other framework
                        last_part = path_parts[-1].replace('()', '')
                        nested_path = '/'.join(path_parts[1:-1])
                        if nested_path:
                            cross_framework_path = f"../{path_parts[0]}/{nested_path}/{last_part}.md"
                        else:
                            cross_framework_path = f"../{path_parts[0]}/{last_part}.md"
                    
                    return f"[{link_text}]({cross_framework_path})"
                
                # Same framework - create local link
                # Handle nested paths properly
                if len(path_parts) == 2:
                    # Direct child of framework
                    local_path = f"{path_parts[-1]}.md"
                else:
                    # Nested path - preserve subdirectory structure
                    # For watchkit/wkapplicationdelegate/main() -> wkapplicationdelegate/main.md
                    # Remove parentheses from method names
                    last_part = path_parts[-1].replace('()', '')
                    nested_path = '/'.join(path_parts[1:-1])
                    if nested_path:
                        local_path = f"{nested_path}/{last_part}.md"
                    else:
                        local_path = f"{last_part}.md"
                
                return f"[{link_text}]({local_path})"
        
        except Exception:
            # If anything goes wrong, fall back to Apple URL only
            pass
        
        # Fallback to Apple URL only
        return f"[{link_text}]({apple_url})"