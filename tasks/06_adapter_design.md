# Meilisearch Adapter Layer Design

## Overview

The adapter layer bridges the gap between our existing MCP API (`search_apple_docs`, `list_frameworks`) and the generic meilisearch-mcp tools. This is necessary because meilisearch-mcp provides general-purpose search tools while our API is specifically tailored for Apple documentation.

## Architecture

```
Claude Code <--> Our MCP Server <--> Adapter <--> meilisearch-mcp <--> Meilisearch
                 (search_apple_docs)           (search tool)
```

## Adapter Implementation

### Core Adapter Class

```python
import asyncio
import json
from typing import List, Dict, Optional, Any
from dataclasses import dataclass
import logging

@dataclass
class SearchResult:
    framework: str
    api_name: str
    title: str
    content: str
    url: str
    platforms: List[str]
    relevance_score: float

class MeilisearchMCPAdapter:
    """Adapts our Apple Docs MCP API to meilisearch-mcp tools"""
    
    def __init__(self, meilisearch_url: str, api_key: Optional[str] = None):
        self.meilisearch_url = meilisearch_url
        self.api_key = api_key
        self.index_name = "apple-docs"
        self.mcp_client = None  # Will be meilisearch-mcp client
        
    async def initialize(self):
        """Initialize connection to meilisearch-mcp"""
        # Set up meilisearch-mcp client
        # This would use the stdio wrapper to communicate
        pass
        
    async def search_apple_docs(
        self,
        query: str,
        framework: Optional[str] = None,
        platform: Optional[str] = None,
        limit: int = 10,
        include_full_content: bool = False
    ) -> List[SearchResult]:
        """
        Implements our search_apple_docs API using meilisearch-mcp
        """
        # Build filter expression
        filters = self._build_filters(framework, platform)
        
        # Determine attributes to retrieve
        attributes = self._get_attributes(include_full_content)
        
        # Call meilisearch-mcp search
        raw_results = await self._search_meilisearch(
            query=query,
            filters=filters,
            limit=limit,
            attributes=attributes
        )
        
        # Transform results
        results = self._transform_results(raw_results)
        
        # Apply link transformation
        results = self._transform_links(results)
        
        return results
        
    async def list_frameworks(
        self,
        platform: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Lists available frameworks with summaries
        Uses faceted search to get framework counts
        """
        # Get all framework main pages
        filters = ["is_framework_main = true"]
        if platform and platform != "all":
            filters.append(f'platforms IN [{platform}]')
            
        # Search for all framework main pages
        raw_results = await self._search_meilisearch(
            query="",  # Empty query to get all
            filters=" AND ".join(filters),
            limit=400,  # We have 361+ frameworks
            attributes=["framework", "title", "platforms", "summary"]
        )
        
        # Transform to framework list format
        return self._transform_framework_list(raw_results)
        
    def _build_filters(
        self,
        framework: Optional[str],
        platform: Optional[str]
    ) -> str:
        """Build Meilisearch filter expression"""
        filters = []
        
        if framework:
            # Escape special characters in framework name
            escaped = framework.replace('"', '\\"')
            filters.append(f'framework = "{escaped}"')
            
        if platform and platform != "all":
            # Handle multiple platforms
            if "," in platform:
                platforms = [p.strip() for p in platform.split(",")]
                platform_filters = [f'platforms IN [{p}]' for p in platforms]
                filters.append(f"({' OR '.join(platform_filters)})")
            else:
                filters.append(f'platforms IN [{platform}]')
                
        return " AND ".join(filters) if filters else ""
        
    def _get_attributes(self, include_full_content: bool) -> List[str]:
        """Determine which attributes to retrieve"""
        base_attrs = [
            "id", "framework", "api_name", "title", 
            "overview", "url", "file_path", "platforms"
        ]
        
        if include_full_content:
            base_attrs.append("content")
            
        return base_attrs
        
    async def _search_meilisearch(
        self,
        query: str,
        filters: str,
        limit: int,
        attributes: List[str]
    ) -> Dict[str, Any]:
        """Execute search via meilisearch-mcp"""
        # This would call the meilisearch-mcp search tool
        # For now, showing the expected format
        search_params = {
            "indexUid": self.index_name,
            "q": query,
            "limit": limit,
            "attributesToRetrieve": attributes
        }
        
        if filters:
            search_params["filter"] = filters
            
        # Call meilisearch-mcp
        # return await self.mcp_client.search(**search_params)
        return {}  # Placeholder
        
    def _transform_results(
        self,
        raw_results: Dict[str, Any]
    ) -> List[SearchResult]:
        """Transform Meilisearch results to our format"""
        results = []
        
        for hit in raw_results.get("hits", []):
            result = SearchResult(
                framework=hit.get("framework", ""),
                api_name=hit.get("api_name", ""),
                title=hit.get("title", ""),
                content=hit.get("content", hit.get("overview", "")),
                url=hit.get("url", ""),
                platforms=hit.get("platforms", []),
                relevance_score=hit.get("_rankingScore", 0.0)
            )
            results.append(result)
            
        return results
        
    def _transform_links(
        self,
        results: List[SearchResult]
    ) -> List[SearchResult]:
        """
        Transform relative links to MCP search instructions
        Preserves existing functionality
        """
        import re
        
        for result in results:
            # Pattern to match relative markdown links
            pattern = r'\[([^\]]+)\]\((?!http)([^)]+)\)'
            
            def replace_link(match):
                text = match.group(1)
                path = match.group(2)
                
                # Extract framework and API from path
                parts = path.strip('/').split('/')
                if len(parts) >= 2:
                    framework = parts[0]
                    api = parts[-1].replace('.md', '')
                    return f'[{text}](search for "{api} in {framework}")'
                return match.group(0)
                
            result.content = re.sub(pattern, replace_link, result.content)
            
        return results
        
    def _transform_framework_list(
        self,
        raw_results: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Transform results to framework list format"""
        frameworks = {}
        
        for hit in raw_results.get("hits", []):
            framework = hit.get("framework")
            if framework and framework not in frameworks:
                frameworks[framework] = {
                    "name": framework,
                    "summary": hit.get("summary", ""),
                    "platforms": hit.get("platforms", []),
                    "document_count": 1  # Would get from facets
                }
                
        return sorted(
            frameworks.values(),
            key=lambda f: f["name"].lower()
        )
```

### Integration with MCP Server

```python
# In mcp_server.py

from adapter import MeilisearchMCPAdapter

class AppleDocsMCPServer:
    def __init__(self):
        self.adapter = MeilisearchMCPAdapter(
            meilisearch_url=os.getenv("MEILISEARCH_URL"),
            api_key=os.getenv("MEILISEARCH_API_KEY")
        )
        
    @mcp.tool()
    async def search_apple_docs(
        self,
        query: str,
        framework: Optional[str] = None,
        platform: Optional[str] = None,
        limit: int = 10,
        include_full_content: bool = False
    ) -> List[Dict[str, Any]]:
        """Search Apple developer documentation"""
        results = await self.adapter.search_apple_docs(
            query=query,
            framework=framework,
            platform=platform,
            limit=limit,
            include_full_content=include_full_content
        )
        
        # Convert to dict format for MCP
        return [
            {
                "framework": r.framework,
                "api_name": r.api_name,
                "title": r.title,
                "content": r.content,
                "url": r.url,
                "platforms": r.platforms,
                "relevance_score": r.relevance_score
            }
            for r in results
        ]
        
    @mcp.tool()
    async def list_frameworks(
        self,
        platform: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """List available Apple frameworks"""
        return await self.adapter.list_frameworks(platform)
```

## Key Design Decisions

### 1. Single Index Strategy
- Use one `apple-docs` index for all frameworks
- Simplifies management and improves performance
- Framework filtering done via Meilisearch filters

### 2. Filter Expression Building
- Properly escape special characters in framework names
- Support multiple platform filtering
- Use Meilisearch's native filter syntax for performance

### 3. Link Transformation
- Preserve existing behavior exactly
- Transform after search to avoid indexing overhead
- Use regex for reliable pattern matching

### 4. Framework Listing
- Use framework main pages with `is_framework_main` flag
- Get counts from faceted search if available
- Sort alphabetically for consistency

### 5. Error Handling
- Graceful degradation if meilisearch-mcp fails
- Detailed logging for debugging
- Timeout handling for network issues

## Testing Strategy

### Unit Tests
```python
def test_filter_building():
    adapter = MeilisearchMCPAdapter("http://localhost:7700")
    
    # Test single framework
    assert adapter._build_filters("SwiftUI", None) == 'framework = "SwiftUI"'
    
    # Test framework with special chars
    assert adapter._build_filters("Core ML", None) == 'framework = "Core ML"'
    
    # Test platform filtering
    assert adapter._build_filters(None, "ios") == 'platforms IN [ios]'
    
    # Test combined
    assert adapter._build_filters("UIKit", "ios,macos") == \
        'framework = "UIKit" AND (platforms IN [ios] OR platforms IN [macos])'
```

### Integration Tests
- Test with real meilisearch-mcp connection
- Verify search results match expected format
- Test link transformation preserves functionality
- Validate framework listing completeness

### Performance Tests
- Measure adapter overhead (<10ms target)
- Test with concurrent requests
- Validate memory usage remains stable

## Deployment Considerations

1. **Configuration**: Adapter configured via environment variables
2. **Logging**: Structured logging for monitoring
3. **Health Checks**: Verify meilisearch-mcp connectivity
4. **Graceful Shutdown**: Properly close connections
5. **Resource Management**: Connection pooling if needed

## Future Enhancements

1. **Caching Layer**: Cache frequent searches
2. **Query Optimization**: Pre-process common patterns
3. **Batch Operations**: Support bulk searches
4. **Metrics Collection**: Track search patterns
5. **A/B Testing**: Compare with vector search results