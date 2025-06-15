"""
MCP Prompts Handler
Implements prompts/list and prompts/get for reusable query templates
"""

from typing import List, Dict, Any, Optional
from datetime import datetime

class PromptsHandler:
    def __init__(self, rag_engine):
        self.rag = rag_engine
        self.prompts = self._define_prompts()
    
    def _define_prompts(self) -> Dict[str, Dict[str, Any]]:
        """Define available prompt templates"""
        return {
            "explain_api": {
                "name": "explain_api",
                "description": "Get a detailed explanation of an Apple API with examples. Best for understanding specific APIs, their properties, methods, and usage patterns.",
                "arguments": [
                    {
                        "name": "api_name",
                        "description": "Name of the API (e.g., 'Button', 'NavigationView', 'URLSession')",
                        "required": True
                    },
                    {
                        "name": "framework",
                        "description": "Framework name (e.g., 'SwiftUI', 'UIKit'). Leave empty to search all.",
                        "required": False
                    },
                    {
                        "name": "platform",
                        "description": "Target platform (ios, macos, tvos, watchos, visionos, all)",
                        "required": False
                    }
                ]
            },
            "compare_apis": {
                "name": "compare_apis",
                "description": "Compare two similar APIs and understand their differences",
                "arguments": [
                    {
                        "name": "api1",
                        "description": "First API to compare",
                        "required": True
                    },
                    {
                        "name": "api2",
                        "description": "Second API to compare",
                        "required": True
                    },
                    {
                        "name": "platform",
                        "description": "Target platform for comparison",
                        "required": False
                    }
                ]
            },
            "migration_guide": {
                "name": "migration_guide",
                "description": "Create a migration guide from one framework to another",
                "arguments": [
                    {
                        "name": "from_framework",
                        "description": "Source framework (e.g., 'UIKit')",
                        "required": True
                    },
                    {
                        "name": "to_framework",
                        "description": "Target framework (e.g., 'SwiftUI')",
                        "required": True
                    },
                    {
                        "name": "component",
                        "description": "Specific component to migrate (e.g., 'Button', 'TableView')",
                        "required": True
                    }
                ]
            },
            "platform_availability": {
                "name": "platform_availability",
                "description": "Check which platforms support a specific API",
                "arguments": [
                    {
                        "name": "api_name",
                        "description": "Name of the API to check",
                        "required": True
                    },
                    {
                        "name": "framework",
                        "description": "Framework name (optional)",
                        "required": False
                    }
                ]
            },
            "code_example": {
                "name": "code_example",
                "description": "Find code examples for a specific API or pattern",
                "arguments": [
                    {
                        "name": "topic",
                        "description": "API or pattern to find examples for",
                        "required": True
                    },
                    {
                        "name": "platform",
                        "description": "Target platform",
                        "required": False
                    },
                    {
                        "name": "complexity",
                        "description": "Example complexity (basic, intermediate, advanced)",
                        "required": False
                    }
                ]
            },
            "usage_guide": {
                "name": "usage_guide",
                "description": "Get guidance on how to effectively search Apple documentation using this MCP server",
                "arguments": [
                    {
                        "name": "topic",
                        "description": "What you need help with: 'search_tips', 'platform_guide', 'framework_discovery', or 'general'",
                        "required": False
                    }
                ]
            }
        }
    
    async def list_prompts(self) -> Dict[str, Any]:
        """List available prompt templates"""
        prompts_list = []
        
        for prompt_id, prompt_def in self.prompts.items():
            prompts_list.append({
                "name": prompt_def["name"],
                "description": prompt_def["description"],
                "arguments": prompt_def["arguments"]
            })
        
        return {"prompts": prompts_list}
    
    async def get_prompt(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Get a specific prompt with arguments filled"""
        if name not in self.prompts:
            raise ValueError(f"Unknown prompt: {name}")
        
        prompt_def = self.prompts[name]
        
        # Validate required arguments
        for arg in prompt_def["arguments"]:
            if arg["required"] and arg["name"] not in arguments:
                raise ValueError(f"Missing required argument: {arg['name']}")
        
        # Generate prompt based on template
        if name == "explain_api":
            return await self._generate_explain_api_prompt(arguments)
        elif name == "compare_apis":
            return await self._generate_compare_apis_prompt(arguments)
        elif name == "migration_guide":
            return await self._generate_migration_prompt(arguments)
        elif name == "platform_availability":
            return await self._generate_platform_prompt(arguments)
        elif name == "code_example":
            return await self._generate_code_example_prompt(arguments)
        elif name == "usage_guide":
            return await self._generate_usage_guide_prompt(arguments)
        else:
            raise ValueError(f"Prompt not implemented: {name}")
    
    async def _generate_explain_api_prompt(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Generate explanation prompt for an API"""
        api_name = args["api_name"]
        framework = args.get("framework")
        platform = args.get("platform", "all")
        
        # Search for the API
        results = await self.rag.search(
            query=api_name,
            framework=framework,
            platform=platform,
            limit=5
        )
        
        # Format documentation
        docs_content = self._format_search_results(results)
        
        prompt_text = f"""Please provide a comprehensive explanation of the {api_name} API.

Based on the Apple documentation below, cover:
1. What this API is and its primary purpose
2. When and why to use it
3. Key properties and methods
4. Common use cases and patterns
5. Code examples demonstrating proper usage
6. Platform availability and version requirements
7. Best practices and performance considerations
8. Common pitfalls to avoid

Documentation:
{docs_content}"""
        
        return {
            "description": f"Comprehensive explanation of {api_name}",
            "messages": [
                {
                    "role": "user",
                    "content": {
                        "type": "text",
                        "text": prompt_text
                    }
                }
            ]
        }
    
    async def _generate_compare_apis_prompt(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comparison prompt for two APIs"""
        api1 = args["api1"]
        api2 = args["api2"]
        platform = args.get("platform", "all")
        
        # Search for both APIs
        results1 = await self.rag.search(api1, platform=platform, limit=3)
        results2 = await self.rag.search(api2, platform=platform, limit=3)
        
        docs1 = self._format_search_results(results1)
        docs2 = self._format_search_results(results2)
        
        prompt_text = f"""Compare and contrast {api1} and {api2}.

Analyze:
1. Core similarities and differences
2. Use cases for each
3. Performance characteristics
4. Platform availability
5. Migration considerations
6. When to use one over the other

{api1} Documentation:
{docs1}

{api2} Documentation:
{docs2}"""
        
        return {
            "description": f"Comparison of {api1} vs {api2}",
            "messages": [
                {
                    "role": "user",
                    "content": {
                        "type": "text",
                        "text": prompt_text
                    }
                }
            ]
        }
    
    async def _generate_migration_prompt(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Generate migration guide prompt"""
        from_fw = args["from_framework"]
        to_fw = args["to_framework"]
        component = args["component"]
        
        # Search for component in both frameworks
        old_results = await self.rag.search(
            f"{component} {from_fw}",
            framework=from_fw,
            limit=3
        )
        new_results = await self.rag.search(
            f"{component} {to_fw}",
            framework=to_fw,
            limit=3
        )
        
        old_docs = self._format_search_results(old_results)
        new_docs = self._format_search_results(new_results)
        
        prompt_text = f"""Create a migration guide for {component} from {from_fw} to {to_fw}.

Include:
1. Key API differences
2. Step-by-step migration process
3. Code examples showing before/after
4. Handling of deprecated features
5. New capabilities to leverage
6. Common migration challenges and solutions

{from_fw} {component} Documentation:
{old_docs}

{to_fw} {component} Documentation:
{new_docs}"""
        
        return {
            "description": f"Migration guide: {component} from {from_fw} to {to_fw}",
            "messages": [
                {
                    "role": "user",
                    "content": {
                        "type": "text",
                        "text": prompt_text
                    }
                }
            ]
        }
    
    async def _generate_platform_prompt(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Generate platform availability prompt"""
        api_name = args["api_name"]
        framework = args.get("framework")
        
        # Search across all platforms
        all_results = []
        platforms = ["ios", "macos", "tvos", "watchos", "visionos"]
        
        for platform in platforms:
            results = await self.rag.search(
                api_name,
                framework=framework,
                platform=platform,
                limit=2
            )
            if results:
                all_results.append((platform, results))
        
        docs_by_platform = ""
        for platform, results in all_results:
            docs_by_platform += f"\n### {platform.upper()}\n"
            docs_by_platform += self._format_search_results(results)
        
        prompt_text = f"""Analyze platform availability for {api_name}.

Based on the documentation below, provide:
1. Which platforms support this API
2. Version requirements for each platform
3. Platform-specific differences or limitations
4. Recommended approaches for cross-platform usage
5. Fallback strategies for unsupported platforms

Platform Documentation:
{docs_by_platform}"""
        
        return {
            "description": f"Platform availability analysis for {api_name}",
            "messages": [
                {
                    "role": "user", 
                    "content": {
                        "type": "text",
                        "text": prompt_text
                    }
                }
            ]
        }
    
    async def _generate_code_example_prompt(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Generate code examples prompt"""
        topic = args["topic"]
        platform = args.get("platform", "all")
        complexity = args.get("complexity", "intermediate")
        
        # Search for examples
        results = await self.rag.search(
            f"{topic} example code sample",
            platform=platform,
            limit=5,
        )
        
        docs = self._format_search_results(results)
        
        prompt_text = f"""Provide {complexity} code examples for {topic}.

Based on the documentation below, create:
1. A basic example showing core usage
2. A more complex example demonstrating advanced features
3. Best practices implementation
4. Error handling patterns
5. Performance optimizations
6. Integration with other APIs

Make examples practical and well-commented.

Documentation:
{docs}"""
        
        return {
            "description": f"{complexity.capitalize()} code examples for {topic}",
            "messages": [
                {
                    "role": "user",
                    "content": {
                        "type": "text",
                        "text": prompt_text
                    }
                }
            ]
        }
    
    async def _generate_usage_guide_prompt(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Generate usage guide for the MCP server"""
        topic = args.get("topic", "general")
        
        guides = {
            "search_tips": """## Effective Search Tips for Apple Docs MCP

1. **Use Specific Technical Terms**
   - Good: "URLSession async await", "NavigationStack path"
   - Avoid: "how to make network calls", "navigation in SwiftUI"

2. **Include Framework Names**
   - "SwiftUI List selection" instead of just "List selection"
   - "UIKit UITableView" instead of just "table view"

3. **Platform Filtering**
   - Always specify platform (use "all" for cross-platform)
   - Start specific (ios), then broaden to "all" if needed

4. **Query Patterns That Work Well**
   - API + feature: "Button custom style"
   - Framework + pattern: "Combine error handling"
   - Platform + capability: "visionOS spatial audio"

5. **Limit Parameter**
   - Default 5 is usually sufficient
   - Increase to 10-20 for broad topics
   - Use include_full_content=true sparingly""",
            
            "platform_guide": """## Platform Search Guide

Available platforms:
- **ios**: iPhone and iPad specific
- **ipados**: iPad-specific features
- **macos**: Mac development
- **tvos**: Apple TV
- **watchos**: Apple Watch
- **visionos**: Vision Pro
- **catalyst**: Mac Catalyst
- **all**: Cross-platform search

Best practices:
1. Start with specific platform
2. Use "all" when looking for shared APIs
3. Some frameworks are platform-specific
4. Check framework availability with list_frameworks""",
            
            "framework_discovery": """## Framework Discovery Guide

1. **List All Frameworks**
   - Use list_frameworks without parameters
   - Returns all 360 frameworks

2. **Platform-Specific Frameworks**
   - list_frameworks with platform="ios"
   - Shows only that platform's frameworks
   - Includes detailed descriptions

3. **Common Framework Patterns**
   - UI frameworks: SwiftUI, UIKit, AppKit
   - System: Foundation, CoreFoundation
   - Media: AVFoundation, CoreImage
   - Data: CoreData, CloudKit

4. **Finding the Right Framework**
   - Start with list_frameworks
   - Look for keywords in descriptions
   - Then search within that framework""",
            
            "general": """## Apple Docs MCP Server Usage Guide

This server provides semantic search over 341,207 Apple documentation pages.

**Key Features:**
1. search_apple_docs - Natural language search
2. list_frameworks - Discover available frameworks
3. resources/read - Direct documentation access
4. prompts/* - Pre-built query templates

**Best Practices:**
- Always specify platform (even if "all")
- Use exact Apple terminology
- Start narrow, then broaden search
- Leverage prompts for complex queries
- Batch related searches

**Quick Start:**
search_apple_docs("SwiftUI Button", platform="ios", framework="SwiftUI")"""
        }
        
        guide_text = guides.get(topic, guides["general"])
        
        return {
            "description": f"Usage guide: {topic}",
            "messages": [
                {
                    "role": "user",
                    "content": {
                        "type": "text",
                        "text": f"Please help me understand how to use the Apple Docs MCP server effectively:\n\n{guide_text}"
                    }
                }
            ]
        }
    def _format_search_results(self, results: List[Dict[str, Any]]) -> str:
        """Format search results for prompt inclusion"""
        if not results:
            return "No documentation found."
        
        formatted = []
        for i, result in enumerate(results, 1):
            meta = result.get('metadata', {})
            content = result.get('content', '')
            
            formatted.append(f"--- Result {i} ---")
            formatted.append(f"Framework: {meta.get('framework', 'Unknown')}")
            formatted.append(f"API: {meta.get('api_name', 'Unknown')}")
            formatted.append(f"Platforms: {meta.get('platforms', 'Unknown')}")
            formatted.append(f"Content:\n{content}")
            formatted.append("")
        
        return '\n'.join(formatted)