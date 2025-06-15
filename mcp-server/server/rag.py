#!/usr/bin/env python3
"""
Simple RAG (Retrieval-Augmented Generation) engine for Apple documentation.
Uses ChromaDB for vector search and OpenAI for query embeddings.
No GPT-4 needed - Claude handles all reasoning.
"""

import os
import sys
import time
import logging
from typing import List, Dict, Optional, Any
from pathlib import Path

import chromadb
import openai

# Import config from the same directory
from config import (
    OPENAI_API_KEY, 
    VECTORSTORE_PATH, 
    COLLECTION_NAME,
    DEFAULT_SEARCH_LIMIT,
    MAX_SEARCH_LIMIT
)

# Disable ChromaDB telemetry
os.environ["ANONYMIZED_TELEMETRY"] = "False"

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SimpleRAG:
    """Simple retrieval system for Apple documentation"""
    
    def __init__(self, vectorstore_path: Optional[str] = None):
        """Initialize RAG with existing vector store"""
        # Use config values
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY environment variable must be set")
        
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)
        logger.info("OpenAI API configured")
        
        # Use vectorstore path from config or parameter
        path = vectorstore_path or str(VECTORSTORE_PATH)
        
        # Connect to ChromaDB
        self.chroma = chromadb.PersistentClient(path=path)
        
        # Try to get existing collection, or return None if not found
        try:
            self.collection = self.chroma.get_collection(COLLECTION_NAME)
            doc_count = self.collection.count()
            logger.info(f"Connected to ChromaDB collection '{COLLECTION_NAME}' with {doc_count} documents")
        except Exception as e:
            logger.warning(f"Collection '{COLLECTION_NAME}' not found. Vector database needs to be built.")
            self.collection = None
        
        # Cache for embeddings (simple in-memory cache)
        self._embedding_cache = {}
        
        # Load framework names dynamically (only if collection exists)
        self._framework_names = self._load_framework_names() if self.collection else set()
        
    def _load_framework_names(self) -> set:
        """Load all unique framework names from the entire collection"""
        try:
            logger.info("Loading all framework names from vectorstore (this may take a moment)...")
            frameworks = set()
            
            # Scan ALL documents to get complete framework list
            # This runs once at startup to ensure accuracy
            batch_size = 10000
            total = self.collection.count()
            
            for offset in range(0, total, batch_size):
                limit = min(batch_size, total - offset)
                results = self.collection.get(
                    limit=limit,
                    offset=offset,
                    include=["metadatas"]
                )
                
                for metadata in results["metadatas"]:
                    framework = metadata.get("framework")
                    if framework:
                        # Add lowercase for case-insensitive matching
                        frameworks.add(framework.lower())
                
                if offset % 50000 == 0:
                    logger.debug(f"  Scanned {offset:,}/{total:,} documents...")
            
            logger.info(f"Loaded {len(frameworks)} unique framework names from {total:,} documents")
            return frameworks
            
        except Exception as e:
            logger.warning(f"Failed to load framework names: {e}")
            # Return a default set if loading fails
            return {"swiftui", "uikit", "foundation", "metal", "coredata", "combine"}
        
    def _get_embedding(self, text: str) -> List[float]:
        """Get embedding for text with caching"""
        # Check cache first
        if text in self._embedding_cache:
            logger.debug(f"Using cached embedding for query: {text[:50]}...")
            return self._embedding_cache[text]
        
        # Generate new embedding
        try:
            response = self.client.embeddings.create(
                input=text,
                model="text-embedding-3-small"
            )
            embedding = response.data[0].embedding
            
            # Cache the result (limit cache size to prevent memory issues)
            if len(self._embedding_cache) < 1000:
                self._embedding_cache[text] = embedding
            
            return embedding
        except Exception as e:
            logger.error(f"Failed to generate embedding: {e}")
            raise
    
    def expand_query(self, query: str) -> str:
        """Enhanced query expansion for better LLM-friendly search"""
        # Start with base expansions for common patterns
        expansions = {
            # Add framework names dynamically
            **{fw: f"{fw} framework apple" for fw in self._framework_names},
            # SwiftUI
            "swiftui": "SwiftUI View ViewModifier ViewBuilder framework UI",
            "view": "View ViewModifier ViewBuilder SwiftUI UIView",
            "list": "List ForEach ScrollView VStack LazyVStack collection",
            "button": "Button ButtonStyle onTapGesture action tap click press",
            "navigation": "NavigationView NavigationLink NavigationStack navigate push",
            "state": "State StateObject ObservedObject Binding Published property wrapper",
            "binding": "Binding State two-way data flow property wrapper",
            "animation": "animation withAnimation transition animate movement",
            "gesture": "gesture onTapGesture DragGesture TapGesture interaction",
            "text": "Text Label string font style attributed",
            "image": "Image UIImage NSImage photo picture icon",
            "shape": "Shape Path Circle Rectangle RoundedRectangle geometry",
            "color": "Color UIColor NSColor foregroundColor backgroundColor",
            
            # UIKit
            "uikit": "UIKit UIViewController UIView iOS framework",
            "viewcontroller": "UIViewController ViewController controller screen",
            "tableview": "UITableView TableView list collection cells",
            "collectionview": "UICollectionView CollectionView grid layout",
            
            # Async/Concurrency
            "async": "async await Task concurrency AsyncSequence asynchronous",
            "await": "async await Task concurrency asynchronous",
            "task": "Task async await concurrency thread",
            "actor": "actor Actor concurrency thread-safe isolation",
            
            # Networking
            "network": "URLSession URLRequest network HTTP API request",
            "urlsession": "URLSession network HTTP API request download upload",
            "api": "API URLSession network REST HTTP request",
            
            # Data
            "json": "JSON JSONEncoder JSONDecoder Codable serialize parse",
            "codable": "Codable JSONEncoder JSONDecoder encode decode",
            "coredata": "CoreData NSManagedObject NSPersistentContainer database",
            "userdefaults": "UserDefaults preferences settings storage",
            
            # Metal/Graphics
            "metal": "Metal MTLDevice MTLCommandBuffer shader GPU graphics",
            "shader": "shader Metal MTL GPU compute vertex fragment",
            "graphics": "graphics Metal Core Graphics drawing render",
            
            # Common patterns
            "singleton": "singleton shared instance pattern",
            "delegate": "delegate protocol delegation pattern",
            "notification": "notification NotificationCenter observer pattern",
            "error": "Error throw try catch Result failure exception",
            
            # Common typos and variations
            "colour": "color Color UIColor NSColor",
            "centre": "center alignment position",
            "initialise": "initialize init initializer"
        }
        
        query_lower = query.lower()
        query_words = query_lower.split()
        expanded_terms = []
        
        # Check each word in the query for possible expansions
        for word in query_words:
            # Direct match
            if word in expansions:
                expanded_terms.append(expansions[word])
            # Partial match (e.g., "buttons" matches "button")
            else:
                for key, expansion in expansions.items():
                    if key in word or word in key:
                        expanded_terms.append(expansion)
                        break
        
        # Also check the full query for multi-word matches
        for key, expansion in expansions.items():
            if key in query_lower and expansion not in expanded_terms:
                expanded_terms.append(expansion)
        
        # Combine original query with expansions
        if expanded_terms:
            # Deduplicate while preserving order
            seen = set()
            unique_terms = []
            for term in expanded_terms:
                if term not in seen:
                    seen.add(term)
                    unique_terms.append(term)
            
            expanded_query = f"{query} {' '.join(unique_terms)}"
            logger.debug(f"Expanded query: {query} -> {expanded_query}")
            return expanded_query
        
        return query
    
    def preprocess_query(self, query: str) -> str:
        """Preprocess query to handle common LLM patterns"""
        # Remove common LLM prefixes/suffixes
        patterns_to_remove = [
            "how to", "how do i", "how can i", "what is", "what are",
            "show me", "find me", "search for", "look for", "get me",
            "documentation for", "docs for", "info about", "information about",
            "in swift", "in swiftui", "in ios", "in macos", "using swift",
            "?", "please", "thanks"
        ]
        
        processed = query.lower()
        for pattern in patterns_to_remove:
            processed = processed.replace(pattern, " ")
        
        # Clean up extra spaces and return
        processed = " ".join(processed.split())
        
        # If we removed everything, return original
        if not processed.strip():
            return query
        
        # Capitalize proper nouns
        proper_nouns = ["swiftui", "uikit", "ios", "macos", "metal", "coredata", 
                       "urlsession", "json", "swift", "objc", "objective-c"]
        
        words = processed.split()
        for i, word in enumerate(words):
            if word.lower() in proper_nouns:
                # Find the proper capitalization
                for noun in proper_nouns:
                    if word.lower() == noun.lower():
                        words[i] = noun.replace("swiftui", "SwiftUI").replace("uikit", "UIKit").replace("ios", "iOS").replace("macos", "macOS").replace("coredata", "CoreData").replace("urlsession", "URLSession").replace("json", "JSON").replace("objc", "ObjC")
                        break
        
        return " ".join(words)
    
    async def search(self, 
                    query: str, 
                    framework: Optional[str] = None,
                    platform: Optional[str] = None,
                    limit: int = DEFAULT_SEARCH_LIMIT,
                    expand_query: bool = True) -> List[Dict[str, Any]]:
        """
        Search Apple documentation with optional framework and platform filtering.
        
        Args:
            query: Search query
            framework: Optional framework to filter by (e.g., 'SwiftUI', 'UIKit')
            platform: Optional platform to filter by (e.g., 'ios', 'macos', 'tvos')
            limit: Maximum number of results to return
            expand_query: Whether to expand the query with related terms
            
        Returns:
            List of search results with content and metadata
        """
        # Check if collection exists
        if self.collection is None:
            logger.warning("No vector database available. Please build the index first.")
            return []
            
        start_time = time.time()
        
        # Preprocess query to handle LLM patterns
        query = self.preprocess_query(query)
        
        # Expand query if requested
        if expand_query:
            query = self.expand_query(query)
        
        # Get embedding for query
        embedding = self._get_embedding(query)
        
        # Build where clause for filtering
        where_clause = {}
        if framework:
            # Keep original case for framework names as they're stored with proper case
            where_clause["framework"] = framework
            logger.debug(f"Filtering by framework: {framework}")
        
        # ChromaDB doesn't support array contains operator for metadata arrays
        # We need to do post-query filtering for platform
        if platform and platform.lower() != "all":
            logger.debug(f"Will filter by platform: {platform} (post-query)")
        
        # Search vector store
        try:
            # Get more results if platform filtering (we'll filter after)
            search_limit = limit * 3 if (platform and platform.lower() != "all") else limit
            
            results = self.collection.query(
                query_embeddings=[embedding],
                n_results=search_limit,
                where=where_clause if where_clause else None,
                include=["documents", "metadatas", "distances"]
            )
            
            # Format results
            formatted_results = []
            if results['documents'] and len(results['documents']) > 0:
                documents = results['documents'][0]
                metadatas = results['metadatas'][0]
                distances = results['distances'][0] if 'distances' in results else [None] * len(documents)
                
                for i in range(len(documents)):
                    # Platform filtering (post-query)
                    if platform and platform.lower() != "all":
                        # Platforms are stored as comma-separated string
                        platforms_str = metadatas[i].get("platforms", "")
                        doc_platforms = [p.strip() for p in platforms_str.split(",")] if platforms_str else []
                        if platform.lower() not in doc_platforms:
                            continue  # Skip this result
                    
                    formatted_results.append({
                        "content": documents[i],
                        "metadata": metadatas[i],
                        "distance": distances[i],
                        "relevance_score": 1 - (distances[i] if distances[i] else 0)  # Convert distance to relevance
                    })
                    
                    # Stop if we have enough results
                    if len(formatted_results) >= limit:
                        break
            
            elapsed = time.time() - start_time
            logger.info(f"Search completed in {elapsed:.3f}s, found {len(formatted_results)} results")
            
            return formatted_results
            
        except Exception as e:
            logger.error(f"Search failed: {e}")
            raise
    
    async def multi_search(self, queries: List[str], limit_per_query: int = 3) -> List[Dict[str, Any]]:
        """
        Search with multiple related queries and deduplicate results.
        
        Args:
            queries: List of search queries
            limit_per_query: Maximum results per individual query
            
        Returns:
            Combined and deduplicated results
        """
        all_results = []
        seen_paths = set()
        
        for query in queries:
            results = await self.search(query, limit=limit_per_query, expand_query=False)
            
            for result in results:
                # Deduplicate by file path
                file_path = result['metadata'].get('file_path', '')
                if file_path not in seen_paths:
                    seen_paths.add(file_path)
                    all_results.append(result)
        
        # Sort by relevance score
        all_results.sort(key=lambda x: x.get('relevance_score', 0), reverse=True)
        
        logger.info(f"Multi-search found {len(all_results)} unique results from {len(queries)} queries")
        return all_results
    
    async def get_api_doc(self, api_name: str, framework: str) -> Optional[Dict[str, Any]]:
        """
        Get documentation for a specific API.
        
        Args:
            api_name: Name of the API (e.g., 'TextField', 'URLSession')
            framework: Framework name (e.g., 'SwiftUI', 'Foundation')
            
        Returns:
            Best matching document or None
        """
        results = await self.search(
            query=api_name,
            framework=framework,
            limit=10,
            expand_query=False
        )
        
        # Look for exact match
        for result in results:
            if result['metadata'].get('api_name', '').lower() == api_name.lower():
                logger.info(f"Found exact match for {api_name} in {framework}")
                return result
        
        # Return best match if no exact match
        if results:
            logger.info(f"No exact match for {api_name}, returning best match")
            return results[0]
        
        logger.warning(f"No documentation found for {api_name} in {framework}")
        return None
    
    def format_for_mcp(self, results: List[Dict[str, Any]]) -> str:
        """
        Format search results for MCP/Claude consumption.
        
        Args:
            results: List of search results
            
        Returns:
            Formatted string with all results
        """
        if not results:
            return "No results found."
        
        formatted = []
        
        for i, result in enumerate(results, 1):
            meta = result['metadata']
            content = result['content']
            
            # Build result header
            header = f"## Result {i}: {meta.get('api_name', 'Unknown API')}"
            if 'framework' in meta:
                header += f" ({meta['framework']})"
            
            # Add metadata
            metadata_lines = [header]
            
            # Add file path as comment for reference
            if 'file_path' in meta:
                metadata_lines.append(f"<!-- File: {meta['file_path']} -->")
            
            # Add relevance score if available
            if 'relevance_score' in result and result['relevance_score'] is not None:
                metadata_lines.append(f"*Relevance: {result['relevance_score']:.2%}*")
            
            # Add chunk info if this is a split document
            if meta.get('chunk_index') is not None:
                metadata_lines.append(f"*Part {meta['chunk_index'] + 1} of {meta.get('total_chunks', '?')}*")
            
            # Combine metadata and content
            formatted.append("\n".join(metadata_lines))
            formatted.append("\n" + content)
            formatted.append("\n---\n")
        
        return "\n".join(formatted)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about the vector store"""
        return {
            "total_documents": self.collection.count() if self.collection else 0,
            "collection_name": "apple_docs",
            "embedding_model": "text-embedding-3-small",
            "cache_size": len(self._embedding_cache),
            "frameworks_loaded": len(self._framework_names),
            "collection_exists": self.collection is not None
        }
    
    def list_frameworks(self, platform: Optional[str] = None) -> Dict[str, Any]:
        """List all available frameworks in the vectorstore with enhanced metadata
        
        Args:
            platform: Optional platform filter (ios, macos, tvos, watchos, visionos, catalyst)
                     If None or 'all', returns all frameworks
        """
        logger.info(f"RAG list_frameworks called with platform={repr(platform)}")
        
        # Normalize platform parameter
        if platform == "" or platform is None:
            platform = None
        elif isinstance(platform, str):
            platform = platform.lower().strip()
            
        # Check if collection exists
        if self.collection is None:
            logger.warning("No vector database available for framework listing.")
            return {
                "frameworks": {},
                "by_platform": {},
                "total_count": 0,
                "platform_filter": platform,
                "error": "Vector database not initialized. Please build the index first."
            }
            
        try:
            # Get framework metadata from main framework pages
            framework_info = {}
            
            # Query for all framework main pages (limited batch for performance)
            results = self.collection.get(
                where={"is_framework_main": True},
                limit=500,  # Should cover all ~341 frameworks
                include=["metadatas"]
            )
            
            for metadata in results["metadatas"]:
                fw_name = metadata.get("framework", "").lower()
                if fw_name:
                    # Convert comma-separated string back to list
                    platforms_str = metadata.get("platforms", "")
                    platforms = [p.strip() for p in platforms_str.split(",") if p.strip()] if platforms_str else []
                    
                    framework_info[fw_name] = {
                        "name": fw_name,
                        "platforms": platforms,
                        "summary": metadata.get("summary"),
                        "title": metadata.get("title", fw_name)
                    }
            
            # Also include frameworks without main pages
            for fw in self._framework_names:
                if fw and fw not in framework_info:
                    framework_info[fw] = {
                        "name": fw,
                        "platforms": [],  # Unknown platforms
                        "summary": None,
                        "title": fw
                    }
            
            # Group by platform
            by_platform = {}
            for fw_data in framework_info.values():
                # Ensure platforms is a list
                platforms = fw_data.get("platforms", [])
                if isinstance(platforms, str):
                    # Handle case where platforms might be a string
                    logger.debug(f"Converting platforms string to list for {fw_data.get('name', 'unknown')}: {platforms}")
                    platforms = [p.strip() for p in platforms.split(",") if p.strip()] if platforms else []
                    fw_data["platforms"] = platforms
                
                for p in platforms:
                    if p not in by_platform:
                        by_platform[p] = []
                    by_platform[p].append(fw_data["name"])
            
            # Sort each platform's frameworks
            for plat in by_platform:
                by_platform[plat].sort()
            
            # Filter by platform if requested
            if platform and platform.lower() != 'all':
                platform_lower = platform.lower()
                filtered_frameworks = {}
                
                # Only include frameworks for the requested platform
                for fw_name, fw_data in framework_info.items():
                    # Ensure platforms is a list
                    platforms = fw_data.get("platforms", [])
                    if isinstance(platforms, str):
                        platforms = [p.strip() for p in platforms.split(",") if p.strip()] if platforms else []
                        fw_data["platforms"] = platforms
                    platforms_lower = [p.lower() for p in platforms]
                    if platform_lower in platforms_lower:
                        filtered_frameworks[fw_name] = fw_data
                
                # Return platform-specific data
                return {
                    "total_frameworks": len(filtered_frameworks),
                    "platform": platform,
                    "frameworks": sorted(filtered_frameworks.keys()),
                    "framework_details": filtered_frameworks,
                    "popular_frameworks": [
                        fw for fw in ["swiftui", "uikit", "foundation", "metal", "coredata",
                                     "combine", "swift", "avfoundation", "coreml", "arkit"]
                        if fw in filtered_frameworks
                    ]
                }
            
            # Return all frameworks (no platform filter)
            grouped = {}
            for fw_name in sorted(framework_info.keys()):
                if fw_name:
                    first_letter = fw_name[0].upper()
                    if first_letter not in grouped:
                        grouped[first_letter] = []
                    grouped[first_letter].append(fw_name)
            
            return {
                "total_frameworks": len(framework_info),
                "frameworks": sorted(framework_info.keys()),
                "framework_details": framework_info,
                "grouped_frameworks": grouped,
                "frameworks_by_platform": by_platform,
                "popular_frameworks": [
                    "swiftui", "uikit", "foundation", "metal", "coredata",
                    "combine", "swift", "avfoundation", "coreml", "arkit"
                ] if "swiftui" in framework_info else []
            }
            
        except Exception as e:
            logger.warning(f"Failed to load enhanced framework info: {e}")
            # Fall back to simple list
            frameworks = sorted(list(self._framework_names))
            grouped = {}
            for fw in frameworks:
                if fw:
                    first_letter = fw[0].upper()
                    if first_letter not in grouped:
                        grouped[first_letter] = []
                    grouped[first_letter].append(fw)
            
            return {
                "total_frameworks": len(frameworks),
                "frameworks": frameworks,
                "grouped_frameworks": grouped
            }
    
    def verify_frameworks(self) -> Dict[str, Any]:
        """Verify framework coverage against documentation folders"""
        from pathlib import Path
        
        # Get documentation folders
        docs_path = Path(__file__).parent.parent.parent / "documentation"
        doc_folders = set()
        if docs_path.exists():
            for item in docs_path.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    doc_folders.add(item.name.lower())
        
        # Get frameworks from vectorstore (sample-based for performance)
        vs_frameworks = self._framework_names
        
        # Calculate coverage
        matched = len(doc_folders & vs_frameworks)
        total_folders = len(doc_folders)
        coverage = (matched / total_folders * 100) if total_folders > 0 else 0
        
        return {
            "documentation_folders": total_folders,
            "vectorstore_frameworks": len(vs_frameworks),
            "matched": matched,
            "coverage_percentage": coverage,
            "status": "✅ Good" if coverage > 80 else "⚠️ Low coverage"
        }


async def main():
    """Example usage and testing"""
    import asyncio
    
    # Initialize RAG
    rag = SimpleRAG()
    
    # Print stats
    stats = rag.get_stats()
    print(f"\nVector store stats:")
    print(f"  Total documents: {stats['total_documents']:,}")
    print(f"  Collection: {stats['collection_name']}")
    print(f"  Model: {stats['embedding_model']}")
    
    # Example searches
    examples = [
        ("SwiftUI Button", None),
        ("async await", "Swift"),
        ("Metal shader", "Metal"),
        ("URLSession", "Foundation"),
        ("NavigationView", "SwiftUI")
    ]
    
    print("\n" + "="*60)
    print("Running example searches...")
    print("="*60)
    
    for query, framework in examples:
        print(f"\n🔍 Query: '{query}'" + (f" in {framework}" if framework else ""))
        
        results = await rag.search(query, framework=framework, limit=3)
        
        if results:
            print(f"Found {len(results)} results:")
            for i, result in enumerate(results, 1):
                meta = result['metadata']
                print(f"  {i}. {meta.get('api_name', 'Unknown')} ({meta.get('framework', 'Unknown')})")
                print(f"     Relevance: {result.get('relevance_score', 0):.2%}")
                if meta.get('chunk_index') is not None:
                    print(f"     Part {meta['chunk_index'] + 1} of {meta.get('total_chunks', '?')}")
        else:
            print("  No results found")
    
    # Test multi-search
    print("\n" + "="*60)
    print("Testing multi-search...")
    print("="*60)
    
    multi_results = await rag.multi_search([
        "SwiftUI List",
        "ForEach SwiftUI",
        "ScrollView"
    ], limit_per_query=2)
    
    print(f"\nMulti-search found {len(multi_results)} unique results")
    
    # Test API doc lookup
    print("\n" + "="*60)
    print("Testing specific API lookup...")
    print("="*60)
    
    api_doc = await rag.get_api_doc("TextField", "SwiftUI")
    if api_doc:
        print(f"\n✅ Found documentation for TextField")
        print(f"   File: {api_doc['metadata'].get('file_path', 'Unknown')}")
    
    # Show formatted output
    print("\n" + "="*60)
    print("Example formatted output for MCP:")
    print("="*60)
    
    sample_results = await rag.search("SwiftUI State", limit=2)
    formatted = rag.format_for_mcp(sample_results)
    print(formatted)


if __name__ == "__main__":
    # Run async main
    import asyncio
    asyncio.run(main())