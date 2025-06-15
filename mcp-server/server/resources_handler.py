"""
MCP Resources Handler
Implements resources/list and resources/read for browsing Apple documentation
"""

import os
from pathlib import Path
from typing import List, Dict, Any, Optional
import json

class ResourcesHandler:
    def __init__(self, docs_path: str = "/Users/avery/Code/apple-developer-docs/documentation"):
        self.docs_path = Path(docs_path)
        self._framework_cache = None
    
    def _get_frameworks(self) -> List[str]:
        """Get list of available frameworks"""
        if self._framework_cache is None:
            self._framework_cache = []
            if self.docs_path.exists():
                for item in self.docs_path.iterdir():
                    if item.is_dir() and not item.name.startswith('.'):
                        self._framework_cache.append(item.name)
            self._framework_cache.sort()
        return self._framework_cache
    
    def _parse_uri(self, uri: str) -> tuple[str, str]:
        """Parse docs://framework/page URI"""
        if not uri.startswith("docs://"):
            raise ValueError(f"Invalid URI scheme: {uri}")
        
        path = uri[7:]  # Remove "docs://"
        parts = path.split('/', 1)
        
        if len(parts) == 1:
            return parts[0], "index"
        return parts[0], parts[1]
    
    async def list_resources(self, limit: int = 100) -> Dict[str, Any]:
        """List available documentation resources"""
        resources = []
        
        # Add framework index resources
        for framework in self._get_frameworks()[:limit]:
            resources.append({
                "uri": f"docs://{framework}/index",
                "name": f"{framework} Documentation",
                "description": f"Complete {framework} framework documentation",
                "mimeType": "text/markdown"
            })
        
        return {"resources": resources}
    
    async def read_resource(self, uri: str) -> Dict[str, Any]:
        """Read a specific documentation resource"""
        try:
            framework, page = self._parse_uri(uri)
            
            # Special handling for index
            if page == "index":
                return await self._read_framework_index(framework)
            
            # Read specific documentation page
            doc_path = self.docs_path / framework / f"{page}.md"
            
            if not doc_path.exists():
                # Try without .md extension
                doc_path = self.docs_path / framework / page
                if not doc_path.exists():
                    raise FileNotFoundError(f"Resource not found: {uri}")
            
            with open(doc_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return {
                "uri": uri,
                "mimeType": "text/markdown",
                "text": content
            }
            
        except Exception as e:
            raise ValueError(f"Failed to read resource {uri}: {str(e)}")
    
    async def _read_framework_index(self, framework: str) -> Dict[str, Any]:
        """Generate an index of all docs in a framework"""
        framework_path = self.docs_path / framework
        
        if not framework_path.exists():
            raise FileNotFoundError(f"Framework not found: {framework}")
        
        # Build index content
        content = f"# {framework} Documentation Index\n\n"
        content += f"Browse all documentation for the {framework} framework.\n\n"
        
        # Group by category
        categories = {}
        for doc_file in framework_path.glob("*.md"):
            if doc_file.name == f"{framework}.md":
                continue  # Skip main framework file
            
            # Simple categorization based on file name patterns
            name = doc_file.stem
            if name.endswith("protocol") or name.endswith("delegate"):
                category = "Protocols"
            elif name[0].isupper():
                category = "Classes"
            elif name.startswith("k") and name[1].isupper():
                category = "Constants"
            else:
                category = "Functions"
            
            if category not in categories:
                categories[category] = []
            
            categories[category].append({
                "name": name,
                "uri": f"docs://{framework}/{name}"
            })
        
        # Format categories
        for category, items in sorted(categories.items()):
            content += f"\n## {category}\n\n"
            for item in sorted(items, key=lambda x: x["name"]):
                content += f"- [{item['name']}]({item['uri']})\n"
        
        return {
            "uri": f"docs://{framework}/index",
            "mimeType": "text/markdown", 
            "text": content
        }
    
    def get_resource_templates(self) -> List[Dict[str, Any]]:
        """Get URI templates for dynamic resource access"""
        return [
            {
                "uriTemplate": "docs://{framework}/{page}",
                "name": "Apple Documentation Page",
                "description": "Access any Apple documentation page directly by framework and page name",
                "mimeType": "text/markdown"
            },
            {
                "uriTemplate": "docs://{framework}/index",
                "name": "Framework Documentation Index", 
                "description": "Browse all documentation in a framework",
                "mimeType": "text/markdown"
            }
        ]