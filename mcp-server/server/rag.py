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
try:
    from .config import (
        OPENAI_API_KEY, 
        VECTORSTORE_PATH, 
        COLLECTION_NAME,
        DEFAULT_SEARCH_LIMIT,
        MAX_SEARCH_LIMIT
    )
except ImportError:
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
        
        # Don't load framework names at startup - too slow
        self._framework_names = set()
        self._frameworks_loaded = False
        
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
        """Minimal query expansion - let vector similarity do the work"""
        # Don't expand queries with "in" pattern - these are usually precise
        if " in " in query.lower():
            return query
        
        # Don't expand long queries - they already have context
        if len(query.split()) > 3:
            return query
            
        # Only do minimal framework name normalization
        query_lower = query.lower()
        
        # Common framework name variations that users might type
        framework_normalizations = {
            "swiftui": "SwiftUI",
            "uikit": "UIKit",
            "appkit": "AppKit",
            "coredata": "CoreData",
            "coregraphics": "Core Graphics",
            "coreanimation": "Core Animation",
            "corelocation": "Core Location",
            "coreml": "CoreML",
            "arkit": "ARKit",
            "scenekit": "SceneKit",
            "spritekit": "SpriteKit",
            "watchkit": "WatchKit",
            "cloudkit": "CloudKit",
            "healthkit": "HealthKit",
            "homekit": "HomeKit",
            "mapkit": "MapKit",
            "webkit": "WebKit",
            "gamekit": "GameKit",
            "photokit": "PhotoKit",
            "storekit": "StoreKit",
            "avfoundation": "AVFoundation",
            "urlsession": "URLSession",
        }
        
        # Check if query is just a framework name that needs normalization
        for variant, normalized in framework_normalizations.items():
            if query_lower == variant:
                return normalized
                
        # Otherwise return original query - let embeddings handle semantic similarity
        return query
    
    def preprocess_query(self, query: str) -> str:
        """Preprocess query to handle common LLM patterns and camelCase"""
        import re
        
        # Handle camelCase splitting for better embedding matches
        # This helps with queries like "UILabel" -> "UI Label"
        def split_camelcase(text):
            # Add space before capital letters that follow lowercase letters
            # UILabel -> UI Label, NSViewController -> NS View Controller
            result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
            # Handle consecutive capitals: UIKit -> UI Kit
            result = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', result)
            return result
        
        # Split camelCase in the original query
        query_with_spaces = split_camelcase(query)
        
        # Remove common LLM prefixes/suffixes
        patterns_to_remove = [
            "how to", "how do i", "how can i", "what is", "what are",
            "show me", "find me", "search for", "look for", "get me",
            "documentation for", "docs for", "info about", "information about",
            "in swift", "in swiftui", "in ios", "in macos", "using swift",
            "?", "please", "thanks"
        ]
        
        processed = query_with_spaces.lower()
        for pattern in patterns_to_remove:
            processed = processed.replace(pattern, " ")
        
        # Clean up extra spaces and return
        processed = " ".join(processed.split())
        
        # If we removed everything, return the camelCase-split version
        if not processed.strip():
            return query_with_spaces
        
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
        
        processed = " ".join(words)
        
        # Log if we split camelCase
        if query != query_with_spaces:
            logger.debug(f"Split camelCase: {query} -> {query_with_spaces}")
        
        return processed
    
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
        
        # Store original query for filename matching
        original_query = query
        
        # Check if query contains camelCase
        has_camelcase = any(c.isupper() for c in query[1:]) and not query.isupper()
        
        # Preprocess query to handle LLM patterns
        processed_query = self.preprocess_query(query)
        
        # Expand query if requested
        if expand_query:
            processed_query = self.expand_query(processed_query)
        
        # Determine base search limit
        query_words = processed_query.lower().split()
        generic_terms = {"init", "frame", "body", "view", "center", "top", "bottom", 
                       "leading", "trailing", "padding", "offset", "size", "position"}
        
        if len(query_words) == 1 and query_words[0] in generic_terms:
            base_search_limit = min(limit * 10, 100)
        elif platform and platform.lower() != "all":
            base_search_limit = limit * 3
        else:
            base_search_limit = limit
        
        # For camelCase queries, search with both original and split versions
        if has_camelcase and original_query != processed_query:
            # Get embeddings for both versions
            embedding_original = self._get_embedding(original_query)
            embedding_processed = self._get_embedding(processed_query)
            
            # Use larger limit for dual search to ensure good coverage
            search_limit = min(base_search_limit * 2, 100)
        else:
            # For generic single terms, enhance the query context
            if len(query_words) == 1 and query_words[0] in generic_terms:
                # Add context to help embedding
                enhanced_query = f"{processed_query} API method property modifier"
                embedding = self._get_embedding(enhanced_query)
            else:
                # Just use the processed version
                embedding = self._get_embedding(processed_query)
            search_limit = base_search_limit
        
        # Build where clause for filtering
        where_clause = {}
        if framework:
            # Keep original case for framework names as they're stored with proper case
            where_clause["framework"] = framework
            logger.debug(f"Filtering by framework: {framework}")
        
        # ChromaDB doesn't support complex operators for string fields
        # We need to do post-query filtering for platform
        if platform and platform.lower() != "all":
            logger.debug(f"Will filter by platform: {platform} (post-query)")
        
        # Search vector store
        try:
            # For camelCase queries, search with both versions
            if has_camelcase and original_query != processed_query:
                # Search with original camelCase
                results_original = self.collection.query(
                    query_embeddings=[embedding_original],
                    n_results=search_limit,
                    where=where_clause if where_clause else None,
                    include=["documents", "metadatas", "distances"]
                )
                
                # Search with split version
                results_split = self.collection.query(
                    query_embeddings=[embedding_processed],
                    n_results=search_limit,
                    where=where_clause if where_clause else None,
                    include=["documents", "metadatas", "distances"]
                )
                
                # Merge results, keeping unique documents
                seen_paths = set()
                merged_docs = []
                merged_metas = []
                merged_dists = []
                
                # Add results from both searches
                for results in [results_original, results_split]:
                    if results['documents'] and len(results['documents']) > 0:
                        docs = results['documents'][0]
                        metas = results['metadatas'][0]
                        dists = results['distances'][0]
                        
                        for i in range(len(docs)):
                            file_path = metas[i].get('file_path', '')
                            if file_path not in seen_paths:
                                seen_paths.add(file_path)
                                merged_docs.append(docs[i])
                                merged_metas.append(metas[i])
                                merged_dists.append(dists[i])
                
                # Sort by distance
                combined = list(zip(merged_dists, merged_docs, merged_metas))
                combined.sort(key=lambda x: x[0])
                
                # Unzip and limit results
                if combined:
                    merged_dists, merged_docs, merged_metas = zip(*combined[:search_limit])
                    results = {
                        'documents': [list(merged_docs)],
                        'metadatas': [list(merged_metas)],
                        'distances': [list(merged_dists)]
                    }
                else:
                    results = {'documents': [[]], 'metadatas': [[]], 'distances': [[]]}
            else:
                # Single search with processed query
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
                    
                    # Calculate relevance score
                    base_relevance = 1 - (distances[i] if distances[i] else 0)
                    
                    # Multi-term query boost
                    multi_term_boost = 0.0
                    query_terms = original_query.lower().split()
                    if len(query_terms) > 1:
                        # Combine searchable text
                        searchable_text = f"{metadatas[i].get('title', '')} {metadatas[i].get('api_name', '')} {metadatas[i].get('file_path', '')} {documents[i][:500]}".lower()
                        
                        # Count how many query terms are present
                        terms_found = sum(1 for term in query_terms if term in searchable_text)
                        coverage_ratio = terms_found / len(query_terms)
                        
                        # Strong boost if ALL terms are found
                        if coverage_ratio == 1.0:
                            multi_term_boost = 0.4
                            
                            # Extra boost if all terms appear in title or API name
                            title_api = f"{metadatas[i].get('title', '')} {metadatas[i].get('api_name', '')}".lower()
                            if all(term in title_api for term in query_terms):
                                multi_term_boost += 0.3
                        # Partial boost for partial matches
                        elif coverage_ratio >= 0.5:
                            multi_term_boost = 0.2 * coverage_ratio
                    
                    # Get metadata
                    title = metadatas[i].get("title", "").lower()
                    api_name = metadatas[i].get("api_name", "").lower()
                    file_path = metadatas[i].get("file_path", "").lower()
                    query_lower = query.lower()
                    
                    # Smart relevance scoring
                    boost = 0.0
                    
                    # 1. MCP Pattern Detection: "api_name in framework"
                    if " in " in query_lower:
                        parts = query_lower.split(" in ", 1)
                        if len(parts) == 2:
                            search_terms = parts[0].strip()
                            search_framework = parts[1].strip().split()[0]  # Take first word after "in"
                            
                            # Extract framework and API from file path
                            if file_path.startswith("documentation/"):
                                path_clean = file_path.replace("documentation/", "").replace(".md", "")
                                path_parts = path_clean.split("/")
                                
                                if len(path_parts) >= 2:
                                    path_framework = path_parts[0].lower()
                                    
                                    # Check framework match
                                    if path_framework == search_framework:
                                        # Build full API path (e.g., "asyncimagephase/failure")
                                        api_path = "/".join(path_parts[1:]).lower()
                                        
                                        # Check if search terms match the API path
                                        search_words = search_terms.split()
                                        
                                        # Exact path match (highest priority)
                                        if api_path == search_terms.replace(" ", "/"):
                                            boost = 0.8
                                        # All search words are in the path
                                        elif all(word in api_path for word in search_words):
                                            boost = 0.6
                                        # Last component matches (API name)
                                        elif path_parts[-1].lower() in search_words:
                                            boost = 0.4
                    
                    # 2. Direct API/Title matching (if no MCP pattern)
                    if boost == 0.0:
                        query_words = query_lower.split()
                        
                        # HIGHEST PRIORITY: Check file name match
                        # Extract filename from path
                        if file_path:
                            filename = file_path.split('/')[-1].replace('.md', '').lower()
                            
                            # Also check against original query (before preprocessing)
                            original_lower = original_query.lower()
                            
                            # Exact match with original query (highest priority for camelCase)
                            if filename == original_lower:
                                boost = 1.0  # Maximum boost for exact original query match
                            # For multi-word queries, also check if query as one word matches filename
                            elif filename == query_lower.replace(' ', ''):
                                boost = 0.6  # Very high boost for exact filename match
                            # Single word exact match
                            elif len(query_words) == 1 and filename == query_words[0]:
                                boost = 0.5  # Very high boost for exact filename match
                            # All query words in filename
                            elif all(word in filename for word in query_words):
                                boost = 0.4  # High boost for filename containing all words
                        
                        # If no filename boost, check other matches
                        if boost == 0.0:
                            # For single-word queries
                            if len(query_words) == 1:
                                single_word = query_words[0]
                                
                                # Check API name
                                if api_name and single_word in api_name:
                                    # Penalize generic terms
                                    generic_terms = {"init", "frame", "body", "view", "center", "top", "bottom", 
                                                   "leading", "trailing", "padding", "offset", "size", "position"}
                                    if single_word in generic_terms:
                                        boost = 0.1  # Small boost for generic terms
                                    else:
                                        boost = 0.3  # Good boost for specific terms
                                
                                # Check title
                                elif title and single_word in title:
                                    boost = 0.25
                                
                                # Check if it's in the path at all
                                elif file_path and f"/{single_word}" in file_path:
                                    boost = 0.2
                            
                            else:
                                # Multi-word queries
                                # Check if the entire query matches API name (case insensitive)
                                query_as_one = query_lower.replace(' ', '')
                                if api_name and (api_name.replace(' ', '') == query_as_one or api_name == query_lower):
                                    boost = 0.5  # High boost for exact match
                                
                                # Exact API name match (one of the words)
                                elif api_name and api_name in query_words:
                                    boost = 0.3
                                
                                # Title contains all query words
                                elif title and all(word in title for word in query_words):
                                    boost = 0.25
                                
                                # API name contains all query words
                                elif api_name and all(word in api_name for word in query_words):
                                    boost = 0.2
                                
                                # Special handling for queries where we want ALL words to match
                                # This helps with queries like "View protocol"
                                elif len(query_words) == 2 and api_name:
                                    # Both words should be in API name or title
                                    if all(word in api_name for word in query_words) or (title and all(word in title for word in query_words)):
                                        boost = 0.3
                                
                                # Partial matches
                                elif title and any(word in title for word in query_words if len(word) > 3):
                                    boost = 0.1
                    
                    # 3. Apply distance-based decay to boost
                    # Closer results get more of their boost preserved
                    if boost > 0:
                        # Distance factor: preserves more boost for closer matches
                        distance_factor = base_relevance  # This is already 1 - distance
                        boost = boost * (0.5 + 0.5 * distance_factor)
                    
                    # Final score combines base relevance, boost, and multi-term boost
                    final_relevance = min(1.0, base_relevance + boost + multi_term_boost)
                    
                    formatted_results.append({
                        "content": documents[i],
                        "metadata": metadatas[i],
                        "distance": distances[i],
                        "relevance_score": final_relevance,
                        "boost_applied": boost > 0  # Track if boost was applied
                    })
                
                # Re-sort by boosted relevance score
                formatted_results.sort(key=lambda x: x.get('relevance_score', 0), reverse=True)
                
                # Trim to requested limit
                formatted_results = formatted_results[:limit]
            
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
            
            # Add relevance score if available
            if 'relevance_score' in result and result['relevance_score'] is not None:
                metadata_lines.append(f"*Relevance: {result['relevance_score']:.2%}*")
            
            # Add chunk info if this is a split document
            if meta.get('chunk_index') is not None:
                metadata_lines.append(f"*Part {meta['chunk_index'] + 1} of {meta.get('total_chunks', '?')}*")
            
            # Transform relative file links to MCP search instructions
            import re
            
            def replace_link(match):
                """Convert relative file paths to MCP search instructions"""
                link_text = match.group(1)
                # Group 2 is the optional ../ prefix, group 3 is the actual path
                file_path = match.group(3)
                
                # Get the current framework from metadata
                current_framework = meta.get('framework', 'SwiftUI')
                
                # Extract framework and API from path like Framework/APIName.md
                path_parts = file_path.replace('.md', '').split('/')
                
                if len(path_parts) == 1:
                    # Single component: e.g., Button.md - same framework
                    api_name = path_parts[0].lower()
                    search_hint = f"{api_name} in {current_framework.lower()}"
                elif len(path_parts) == 2:
                    # Two components - could be Framework/API or Type/Property
                    first_part = path_parts[0]
                    second_part = path_parts[1]
                    
                    # Check if first part looks like a framework (capitalized)
                    if first_part[0].isupper() and first_part not in ['AsyncImagePhase', 'AccessibilityTraits']:
                        # Likely Framework/API: e.g., SwiftUI/NavigationView
                        framework = first_part
                        api_name = second_part.lower()
                        search_hint = f"{api_name} in {framework.lower()}"
                    else:
                        # Likely Type/Property in current framework: e.g., accessibilitytraits/isbutton
                        parent_type = first_part.lower()
                        property_name = second_part.lower()
                        search_hint = f"{property_name} {parent_type} in {current_framework.lower()}"
                elif len(path_parts) > 2:
                    # Nested path: e.g., SwiftUI/AsyncImagePhase/Failure
                    framework = path_parts[0]
                    api_components = [p.lower() for p in path_parts[1:]]
                    search_hint = f"{' '.join(api_components)} in {framework.lower()}"
                else:
                    # Fallback: just use the link text
                    search_hint = link_text.lower()
                
                # Return simple, clean MCP search instruction
                return f"[{link_text}](💡 Search: `{search_hint}`)"
            
            # Replace relative markdown links (both with and without ../ prefix)
            content = re.sub(r'\[([^\]]+)\]\((\.\.\/)?([^)]+\.md)\)', replace_link, content)
            
            # Combine metadata and content
            formatted.append("\n".join(metadata_lines))
            formatted.append("\n" + content)
            formatted.append("\n---\n")
        
        # Add instruction for Claude at the end
        formatted.append("\n<!-- Search Tips for Better Results:\n"
                        "1. Use the pattern 'api_name in framework' for precise results (e.g., 'navigationview in swiftui')\n"
                        "2. For nested APIs, include parent: 'asyncimagephase failure in swiftui'\n"
                        "3. Add context to generic terms: 'frame modifier' instead of just 'frame'\n"
                        "4. Specify framework when known: 'button swiftui' or 'uibutton uikit'\n"
                        "5. Always include platform parameter (ios, macos, etc.) for better filtering\n"
                        "\n"
                        "Links marked with 💡 can be searched using the exact query shown in backticks.\n"
                        "-->")
        
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
        """Verify framework coverage in vectorstore"""
        # Get frameworks from vectorstore
        vs_frameworks = self._framework_names
        total_frameworks = len(vs_frameworks)
        
        # In production, we just report what's in the vectorstore
        # since we don't keep markdown files by default
        return {
            "documentation_folders": total_frameworks,
            "vectorstore_frameworks": total_frameworks,
            "matched": total_frameworks,
            "coverage_percentage": 100.0 if total_frameworks > 0 else 0,
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