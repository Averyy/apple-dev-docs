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
        self.collection = self.chroma.get_collection(COLLECTION_NAME)
        logger.info(f"Connected to ChromaDB collection '{COLLECTION_NAME}' with {self.collection.count()} documents")
        
        # Cache for embeddings (simple in-memory cache)
        self._embedding_cache = {}
        
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
        """Simple query expansion without LLM"""
        # Common Apple framework expansions
        expansions = {
            "swiftui": "SwiftUI View ViewModifier ViewBuilder",
            "uikit": "UIKit UIViewController UIView",
            "async": "async await Task concurrency AsyncSequence",
            "list": "List ForEach ScrollView VStack",
            "button": "Button ButtonStyle onTapGesture action",
            "navigation": "NavigationView NavigationLink NavigationStack",
            "state": "State StateObject ObservedObject Binding",
            "animation": "animation withAnimation transition",
            "gesture": "gesture onTapGesture DragGesture",
            "metal": "Metal MTLDevice MTLCommandBuffer shader",
            "combine": "Combine Publisher Subscriber PassthroughSubject",
            "coredata": "CoreData NSManagedObject NSPersistentContainer",
            "network": "URLSession URLRequest async await",
            "json": "JSONEncoder JSONDecoder Codable",
            "error": "Error throw try catch Result"
        }
        
        query_lower = query.lower()
        expanded_terms = []
        
        # Check each expansion
        for key, expansion in expansions.items():
            if key in query_lower:
                expanded_terms.append(expansion)
        
        # Combine original query with expansions
        if expanded_terms:
            expanded_query = f"{query} {' '.join(expanded_terms)}"
            logger.debug(f"Expanded query: {query} -> {expanded_query}")
            return expanded_query
        
        return query
    
    async def search(self, 
                    query: str, 
                    framework: Optional[str] = None,
                    limit: int = DEFAULT_SEARCH_LIMIT,
                    expand_query: bool = True) -> List[Dict[str, Any]]:
        """
        Search Apple documentation with optional framework filtering.
        
        Args:
            query: Search query
            framework: Optional framework to filter by (e.g., 'SwiftUI', 'UIKit')
            limit: Maximum number of results to return
            expand_query: Whether to expand the query with related terms
            
        Returns:
            List of search results with content and metadata
        """
        start_time = time.time()
        
        # Expand query if requested
        if expand_query:
            query = self.expand_query(query)
        
        # Get embedding for query
        embedding = self._get_embedding(query)
        
        # Build where clause for filtering
        where_clause = None
        if framework:
            where_clause = {"framework": framework}
            logger.debug(f"Filtering by framework: {framework}")
        
        # Search vector store
        try:
            results = self.collection.query(
                query_embeddings=[embedding],
                n_results=limit,
                where=where_clause,
                include=["documents", "metadatas", "distances"]
            )
            
            # Format results
            formatted_results = []
            if results['documents'] and len(results['documents']) > 0:
                documents = results['documents'][0]
                metadatas = results['metadatas'][0]
                distances = results['distances'][0] if 'distances' in results else [None] * len(documents)
                
                for i in range(len(documents)):
                    formatted_results.append({
                        "content": documents[i],
                        "metadata": metadatas[i],
                        "distance": distances[i],
                        "relevance_score": 1 - (distances[i] if distances[i] else 0)  # Convert distance to relevance
                    })
            
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
            "total_documents": self.collection.count(),
            "collection_name": "apple_docs",
            "embedding_model": "text-embedding-3-small",
            "cache_size": len(self._embedding_cache)
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