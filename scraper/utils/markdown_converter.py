"""Convert Apple documentation HTML to clean markdown."""

import re
from pathlib import Path
from typing import Dict, Final, List, Optional, Any

from scraper.utils.logger import get_logger

logger = get_logger(__name__)

# The start of a block that can't share a line with a label before it ("- `x`:",
# "> **Note**:"): a list item, a code fence (its info string holds no backtick,
# as in CommonMark: "```x``" opens a code span), a table row, a quote, a heading
BLOCK_START: Final = re.compile(r'(?:[-*+]|\d{1,9}[.)])(?: |$)|```[^`\n]*(?:\n|$)|\||>|#{1,6}(?: |$)')


def join_blocks(blocks: List[str], indent: int) -> str:
    """Blocks rendered as one list item's (or quote's) content, to follow its
    marker or label: the first block on that line, each later block after a
    blank line, and every line after the first indented by indent spaces (an
    empty line stays empty), so that no line of a list or code listing in it
    leaves the item."""
    pad = ' ' * indent
    first, *rest = '\n\n'.join(blocks).split('\n')
    return '\n'.join([first] + [f"{pad}{line}" if line else '' for line in rest])


def labeled(label: str, content: str, indent: int) -> str:
    """A label ("- `x`:", "- **term**:", "**Note**:") followed by its content
    (join_blocks, indented by indent): on the label's line after a space, or,
    when the content starts with a block that can't share that line
    (BLOCK_START: a list, code listing, table, quote or heading), after a
    blank line, its first line indented too."""
    if BLOCK_START.match(content):
        return f"{label}\n\n{' ' * indent}{content}"
    return f"{label} {content}"


def quote_blocks(label: str, blocks: List[str]) -> str:
    """Blocks rendered as a "> <label> …" quote (labeled): every line
    prefixed "> " (an empty one is ">")."""
    text = labeled(label, join_blocks(blocks, 0), 0)
    return '\n'.join(f"> {line}" if line else '>' for line in text.split('\n'))


class AppleDocMarkdownConverter:
    """Convert Apple documentation HTML to markdown with proper formatting."""
    
    def __init__(self, output_dir: Optional[Path] = None) -> None:
        """Initialize markdown converter.
        
        Args:
            output_dir: Directory where markdown files are saved for cross-linking
        """
        self.output_dir = output_dir
    
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
        
        # Deprecation summary, after the abstract and the Availability list
        if data.get('deprecation_summary'):
            sections.append(data['deprecation_summary'])

        # Declaration: one fence per declaration (a label names its platforms
        # when one language has several), the constraints it's available
        # under, then the symbol's other overloads
        if data.get('declaration'):
            sections.append("## Declaration")
            for declaration in data['declaration']:
                if declaration.get('label'):
                    sections.append(f"*{declaration['label']}*")
                sections.append(self._format_code_block(declaration['code'], declaration['language']))
        if data.get('conformance'):
            sections.append(data['conformance'])
        if data.get('other_declarations'):
            sections.append("**Other overloads**:")
            for declaration in data['other_declarations']:
                sections.append(self._format_code_block(declaration['code'], declaration['language']))

        # Details and Possible Values (keys, REST types), in Apple's order
        for detail in data.get('detail_sections') or []:
            sections.append(f"## {detail['title']}")
            sections.append(detail['content'])
        
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
        
        # A protocol requirement's default implementations
        if data.get('default_implementations'):
            sections.append("## Default Implementations")
            sections.append(self._format_topics(data['default_implementations']))

        # Tasks/Tutorial content
        if data.get('tasks'):
            sections.append("## Tasks")
            for task in data['tasks']:
                sections.append(f"### {task.get('title', 'Task')}")
                sections.append(task.get('content', ''))
        
        # REST API Documentation
        if data.get('rest_endpoint'):
            sections.append("## Endpoint")
            sections.append(f"`{data['rest_endpoint']}`")

        # REST parameters, by group (path, query, header)
        if data.get('rest_parameters'):
            sections.append("## Parameters")
            for group in data['rest_parameters']:
                if group.get('title'):
                    sections.append(f"### {group['title']}")
                sections.append(group['items'])

        if data.get('properties'):
            sections.append("## Properties")
            sections.append(data['properties'])

        if data.get('rest_body'):
            sections.append("## Request Body")
            sections.append(data['rest_body'])
        
        if data.get('rest_responses'):
            sections.append("## Responses")
            sections.append(data['rest_responses'])
        
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
            
        # The page's role as Apple names it (Instance Method, Article, Sample Code…)
        if data.get('role_heading'):
            lines.append(f"**Role**: {data['role_heading']}")

        if data.get('required'):
            lines.append("**Required**: Yes")
        
        # A sample code project's download
        if data.get('sample_download'):
            download = data['sample_download']
            lines.append(f"**Download**: [{download['name']}]({download['url']})")

        return "  \n".join(lines) if lines else ""
    
    def _format_availability(self, availability: List[Dict[str, Any]]) -> str:
        """Format availability information, one platform per line:
        "- <platform>[ <introduced>+][ (Beta)][ - Deprecated[ in <version>][ (renamed: <name>)]]"
        (the deprecation message is the page's summary, not the line's)."""
        if not availability:
            return ""
        
        lines = ["**Availability**:"]
        for item in availability:
            platform = item.get('platform', 'Unknown')

            # A platform without an introduced version is named alone
            line = f"- {platform}"
            if item.get('introduced'):
                line += f" {item['introduced']}+"
            
            # Add beta indicator
            if item.get('beta', False):
                line += " (Beta)"
            
            # Add deprecation information
            if item.get('deprecated', False):
                dep_info = "Deprecated"
                if item.get('deprecated_at'):
                    dep_info += f" in {item['deprecated_at']}"
                if item.get('renamed'):
                    dep_info += f" (renamed: {item['renamed']})"
                line += f" - {dep_info}"
            
            lines.append(line)
        
        return "\n".join(lines)
    
    def _format_code_block(self, code: str, language: str = "swift") -> str:
        """Format a code block with proper language tag."""
        if not code:
            return ""
        
        # Clean up code
        code = code.strip()
        
        return f"```{language}\n{code}\n```"
    
    def _format_parameters(self, parameters: List[Dict[str, str]]) -> str:
        """Format parameter list."""
        if not parameters:
            return ""
        
        lines = []
        for param in parameters:
            name = param.get('name', 'unknown')
            description = param.get('description', '')
            param_type = param.get('type', '')
            
            head = f"- `{name}` ({param_type}):" if param_type else f"- `{name}`:"
            lines.append(labeled(head, description, 2))
        
        return "\n".join(lines)
    
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
    
    def _format_see_also(self, see_also: List[Dict[str, Any]]) -> str:
        """Format see also section, by group under its title."""
        if not see_also:
            return ""
        
        lines = []
        for group in see_also:
            group_title = group.get('title', '')
            if group_title:
                lines.append(f"### {group_title}")

            for item in group.get('items', []):
                title = item.get('name', '')
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