"""
Shared utilities for Apple Docs MCP servers
"""

import re

def enhance_swift_content(content):
    """Enhance Swift content with proper code block formatting."""
    if not content:
        return content
    
    # Add Swift syntax highlighting to code blocks that don't have it
    content = re.sub(
        r'```(\n(?:(?!```).)*?\n)```', 
        r'```swift\1```', 
        content, 
        flags=re.DOTALL
    )
    
    # Enhance protocol conformance sections
    content = re.sub(
        r'(Conforms to:?\s*)(.*?)(\n)', 
        r'**\1** `\2`\3', 
        content, 
        flags=re.IGNORECASE
    )
    
    # Enhance inheritance information
    content = re.sub(
        r'(Inherits from:?\s*)(.*?)(\n)', 
        r'**\1** `\2`\3', 
        content, 
        flags=re.IGNORECASE
    )
    
    return content

def extract_related_terms(content, title, api_name):
    """Extract related search terms from content for cross-references."""
    related_terms = set()
    
    # Extract class/protocol names from content
    class_pattern = r'\b[A-Z][a-zA-Z]*(?:Protocol|Delegate|DataSource|View|Controller|Manager)\b'
    related_terms.update(re.findall(class_pattern, content))
    
    # Extract framework-specific terms
    framework_pattern = r'\b(?:UI|NS|CG|CA|MK|AV|WK|SK)[A-Z][a-zA-Z]*\b'
    related_terms.update(re.findall(framework_pattern, content))
    
    # Extract method names (simplified)
    method_pattern = r'\b[a-z][a-zA-Z]*(?:With|For|In|Of|To|From)[A-Z][a-zA-Z]*\b'
    related_terms.update(re.findall(method_pattern, content))
    
    # Remove the current title and API name
    related_terms.discard(title)
    related_terms.discard(api_name)
    
    # Filter out very common/generic terms
    common_terms = {'String', 'Int', 'Bool', 'Double', 'Float', 'Data', 'URL', 'Date', 'Array', 'Dictionary'}
    related_terms -= common_terms
    
    return sorted(list(related_terms))[:5]

def format_search_results(hits, query, framework, platform, summary_mode, server_prefix=""):
    """Format search results with v1-style rich markdown and relevance scoring."""
    output = []
    
    # Header with search info
    prefix = f"{server_prefix} " if server_prefix else ""
    if not summary_mode:
        output.append(f"# {prefix}Apple Developer Documentation Search Results")
        output.append(f"**Query:** `{query}` | **Results:** {len(hits)}")
    else:
        output.append(f"{prefix}Found {len(hits)} result(s) for '{query}' (summary mode)")
    
    if framework:
        output.append(f"**Framework Filter:** {framework}")
    if platform != "all":
        output.append(f"**Platform Filter:** {platform}")
    
    output.append("")
    
    # Process each result
    for i, hit in enumerate(hits, 1):
        title = hit.get("title", "Untitled")
        framework_name = hit.get("framework", "Unknown")
        api_name = hit.get("api_name", "")
        overview = hit.get("overview", "")
        url = hit.get("url", "")
        platforms = hit.get("platforms", [])
        content = hit.get("content", "")
        kind = hit.get("kind", "")
        
        # Get relevance score
        score = hit.get("_rankingScore", 0)
        score_percent = int(score * 100) if score else 0
        
        # Get highlighted content for better presentation
        formatted_data = hit.get("_formatted", {})
        highlighted_title = formatted_data.get("title", title)
        highlighted_api = formatted_data.get("api_name", api_name)
        
        # Rich result header with relevance score
        output.append(f"## {i}. {highlighted_title} ({score_percent}%)")
        
        if highlighted_api and highlighted_api != highlighted_title:
            output.append(f"**API Name:** `{highlighted_api}`")
        
        output.append(f"**Framework:** {framework_name}")
        
        if kind:
            output.append(f"**Type:** {kind}")
            
        if platforms:
            output.append(f"**Platforms:** {', '.join(platforms)}")
        
        if url:
            output.append(f"**Documentation:** {url}")
        
        output.append("")
        
        if not summary_mode and content:
            # Full content mode - rich markdown with Swift code
            output.append("### Complete Documentation")
            output.append("")
            
            # Process content to enhance Swift code blocks
            enhanced_content = enhance_swift_content(content)
            output.append(enhanced_content)
            
            # Add cross-references and search suggestions
            related_terms = extract_related_terms(content, title, api_name)
            if related_terms:
                output.append("")
                output.append("### 💡 Related Searches")
                for term in related_terms[:5]:  # Limit to 5 suggestions
                    output.append(f"- `{term}`")
            
        else:
            # Summary mode - just overview
            if overview:
                output.append("**Overview:**")
                output.append(overview)
        
        output.append("")
        output.append("---")
        output.append("")
    
    return "\n".join(output)