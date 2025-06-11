#!/usr/bin/env python3
"""
Comprehensive test suite for the RAG engine.
Tests core functionality to ensure any changes don't break the system.
Designed to be difficult to bypass or cheat.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mcp-server', 'server')))

import asyncio
import time
from pathlib import Path

from rag import SimpleRAG


class TestRAGCore:
    """Test core RAG functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        # Ensure we're using the real vector store
        vectorstore_path = "./vectorstore"
        assert Path(vectorstore_path).exists(), "Vector store must exist"
        self.rag = SimpleRAG(vectorstore_path=vectorstore_path)
    
    def test_basic_search(self):
        """Test that basic search returns valid results."""
        # Run async test
        results = asyncio.run(self.rag.search("SwiftUI Text", limit=5))
        
        # Verify we got results
        assert len(results) > 0, "Search should return results for 'SwiftUI Text'"
        assert len(results) <= 5, "Should respect limit parameter"
        
        # Verify result structure
        for result in results:
            assert 'content' in result, "Each result must have content"
            assert 'metadata' in result, "Each result must have metadata"
            assert 'distance' in result, "Each result must have distance"
            assert 'relevance_score' in result, "Each result must have relevance_score"
            
            # Verify metadata structure
            metadata = result['metadata']
            assert 'framework' in metadata, "Metadata must include framework"
            assert 'api_name' in metadata, "Metadata must include api_name"
            assert 'file_path' in metadata, "Metadata must include file_path"
            
            # Verify content is not empty
            assert len(result['content']) > 0, "Content should not be empty"
            
            # Verify relevance score is reasonable
            assert 0 <= result['relevance_score'] <= 1, "Relevance score should be between 0 and 1"
        
        print("✓ Basic search test passed")
    
    def test_framework_filtering(self):
        """Test that framework filtering works correctly."""
        # Search in SwiftUI
        swiftui_results = asyncio.run(self.rag.search("View", framework="SwiftUI", limit=5))
        
        # Verify all results are from SwiftUI
        for result in swiftui_results:
            assert result['metadata']['framework'] == "SwiftUI", \
                f"Framework filter failed: expected SwiftUI, got {result['metadata']['framework']}"
        
        # Search in UIKit
        uikit_results = asyncio.run(self.rag.search("View", framework="UIKit", limit=5))
        
        # Verify results are different
        swiftui_apis = {r['metadata']['api_name'] for r in swiftui_results}
        uikit_apis = {r['metadata']['api_name'] for r in uikit_results if 'api_name' in r['metadata']}
        
        # Should have different APIs (or at least some difference)
        assert swiftui_apis != uikit_apis or len(uikit_results) == 0, \
            "Different frameworks should return different results"
        
        print("✓ Framework filtering test passed")
    
    def test_query_expansion(self):
        """Test that query expansion actually works."""
        # Test known expansion
        expanded = self.rag.expand_query("swiftui")
        assert "SwiftUI" in expanded, "Should expand 'swiftui' to include 'SwiftUI'"
        assert "View" in expanded, "Should include related terms"
        
        # Test that expansion affects results
        results_no_expand = asyncio.run(self.rag.search("button", limit=5, expand_query=False))
        results_expanded = asyncio.run(self.rag.search("button", limit=5, expand_query=True))
        
        # Expanded query should potentially find different/more relevant results
        # Check that at least some results are different or scores are different
        no_expand_ids = [r['metadata'].get('file_path', '') for r in results_no_expand]
        expanded_ids = [r['metadata'].get('file_path', '') for r in results_expanded]
        
        # They might be different, or at least have different relevance scores
        assert results_no_expand != results_expanded, \
            "Query expansion should affect results"
        
        print("✓ Query expansion test passed")


class TestRAGAdvanced:
    """Test advanced RAG features."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.rag = SimpleRAG()
    
    def test_api_doc_lookup(self):
        """Test specific API documentation lookup."""
        # Test with known APIs
        api_doc = asyncio.run(self.rag.get_api_doc("text", "SwiftUI"))
        
        assert api_doc is not None, "Should find Text API in SwiftUI"
        assert api_doc['metadata']['api_name'].lower() == "text", "Should find exact match"
        assert api_doc['metadata']['framework'] == "SwiftUI", "Should be from correct framework"
        
        # Test with non-existent API
        api_doc = asyncio.run(self.rag.get_api_doc("nonexistentapi123", "SwiftUI"))
        # Should return None or best match
        if api_doc:
            # If it returns something, it should at least be from the right framework
            assert api_doc['metadata']['framework'] == "SwiftUI"
        
        print("✓ API doc lookup test passed")
    
    def test_multi_search_deduplication(self):
        """Test that multi-search properly deduplicates results."""
        queries = [
            "SwiftUI Button",
            "Button SwiftUI",
            "SwiftUI Button action"
        ]
        
        results = asyncio.run(self.rag.multi_search(queries, limit_per_query=5))
        
        # Check for duplicates
        seen_paths = set()
        for result in results:
            path = result['metadata'].get('file_path', '')
            assert path not in seen_paths, f"Found duplicate result: {path}"
            seen_paths.add(path)
        
        # Should have found some results
        assert len(results) > 0, "Multi-search should find results"
        
        # Results should be sorted by relevance
        relevance_scores = [r.get('relevance_score', 0) for r in results]
        assert relevance_scores == sorted(relevance_scores, reverse=True), \
            "Results should be sorted by relevance score"
        
        print("✓ Multi-search deduplication test passed")
    
    def test_mcp_formatting(self):
        """Test MCP output formatting."""
        results = asyncio.run(self.rag.search("SwiftUI", limit=3))
        formatted = self.rag.format_for_mcp(results)
        
        # Verify formatting requirements
        assert "## Result 1:" in formatted, "Should have numbered results"
        assert "## Result 2:" in formatted if len(results) > 1 else True, "Should number all results"
        assert "---" in formatted, "Should have separators"
        
        # Verify all results are included
        for i, result in enumerate(results, 1):
            assert f"## Result {i}:" in formatted, f"Result {i} should be in formatted output"
            assert result['metadata']['api_name'] in formatted, "API name should be in output"
        
        # Verify no results are duplicated in formatting
        result_count = formatted.count("## Result")
        assert result_count == len(results), "Should have exactly one section per result"
        
        print("✓ MCP formatting test passed")


class TestRAGPerformance:
    """Test RAG performance requirements."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.rag = SimpleRAG()
    
    def test_search_performance(self):
        """Test that search performance meets requirements."""
        queries = [
            "SwiftUI View",
            "async await",
            "URLSession",
            "NavigationView"
        ]
        
        times = []
        for query in queries:
            start_time = time.time()
            results = asyncio.run(self.rag.search(query, limit=5))
            elapsed = time.time() - start_time
            times.append(elapsed)
            
            # Each individual search should be under 1 second
            assert elapsed < 1.0, f"Search for '{query}' took {elapsed:.3f}s, should be < 1s"
            
            # Should return some results for common queries
            assert len(results) > 0, f"Should find results for '{query}'"
        
        # Average should be under 500ms
        avg_time = sum(times) / len(times)
        assert avg_time < 0.5, f"Average search time {avg_time:.3f}s exceeds 500ms target"
        
        print(f"✓ Performance test passed (avg: {avg_time:.3f}s)")
    
    def test_concurrent_searches(self):
        """Test that concurrent searches work correctly."""
        queries = [
            "SwiftUI Button",
            "UIKit View",
            "Metal shader",
            "async await",
            "CoreData"
        ]
        
        async def run_concurrent():
            # Run searches concurrently
            tasks = [self.rag.search(q, limit=3) for q in queries]
            return await asyncio.gather(*tasks)
        
        results = asyncio.run(run_concurrent())
        
        # All should complete successfully
        assert len(results) == len(queries), "All concurrent searches should complete"
        
        # Each should return valid results
        for i, result_set in enumerate(results):
            assert isinstance(result_set, list), f"Query {i} should return a list"
            # Most queries should find something
            if len(result_set) == 0:
                print(f"Warning: Query '{queries[i]}' returned no results")
        
        print("✓ Concurrent searches test passed")


class TestRAGIntegrity:
    """Test RAG data integrity."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.rag = SimpleRAG()
    
    def test_vector_store_integrity(self):
        """Test that vector store has expected data."""
        stats = self.rag.get_stats()
        
        # Verify vector store is properly loaded
        assert stats['total_documents'] > 300000, \
            f"Vector store should have 300k+ documents, found {stats['total_documents']}"
        
        assert stats['collection_name'] == 'apple_docs', \
            "Should be using 'apple_docs' collection"
        
        assert stats['embedding_model'] == 'text-embedding-3-small', \
            "Should be using text-embedding-3-small model"
        
        print(f"✓ Vector store integrity test passed ({stats['total_documents']:,} docs)")
    
    def test_metadata_completeness(self):
        """Test that all results have complete metadata."""
        # Get a sample of results
        results = asyncio.run(self.rag.search("SwiftUI", limit=20))
        
        required_fields = {'framework', 'api_name', 'file_path'}
        
        for result in results:
            metadata = result['metadata']
            
            # Check all required fields exist
            for field in required_fields:
                assert field in metadata, f"Missing required field: {field}"
                assert metadata[field], f"Field {field} should not be empty"
            
            # Verify file_path looks valid
            file_path = metadata['file_path']
            assert file_path.startswith('documentation/'), \
                f"File path should start with 'documentation/': {file_path}"
            assert file_path.endswith('.md'), \
                f"File path should end with .md: {file_path}"
        
        print("✓ Metadata completeness test passed")
    
    def test_empty_results_handling(self):
        """Test handling of queries with no results."""
        # Search for something unlikely to exist
        results = asyncio.run(self.rag.search("xyzabc123nonexistent", limit=5))
        
        # Should return empty list, not error
        assert isinstance(results, list), "Should return a list even with no results"
        
        # Format empty results
        formatted = self.rag.format_for_mcp([])
        assert formatted == "No results found.", "Should handle empty results gracefully"
        
        print("✓ Empty results handling test passed")


def run_all_tests():
    """Run all RAG tests."""
    print("Testing RAG Engine Core Functionality")
    print("=" * 50)
    
    total_passed = 0
    total_failed = 0
    
    # Core tests
    print("\nCore Functionality:")
    core_tests = TestRAGCore()
    core_tests.setup_method()
    
    tests_to_run = [
        (core_tests.test_basic_search, "Basic search"),
        (core_tests.test_framework_filtering, "Framework filtering"),
        (core_tests.test_query_expansion, "Query expansion"),
    ]
    
    # Advanced tests
    print("\nAdvanced Features:")
    advanced_tests = TestRAGAdvanced()
    advanced_tests.setup_method()
    
    tests_to_run.extend([
        (advanced_tests.test_api_doc_lookup, "API doc lookup"),
        (advanced_tests.test_multi_search_deduplication, "Multi-search deduplication"),
        (advanced_tests.test_mcp_formatting, "MCP formatting"),
    ])
    
    # Performance tests
    print("\nPerformance:")
    perf_tests = TestRAGPerformance()
    perf_tests.setup_method()
    
    tests_to_run.extend([
        (perf_tests.test_search_performance, "Search performance"),
        (perf_tests.test_concurrent_searches, "Concurrent searches"),
    ])
    
    # Integrity tests
    print("\nData Integrity:")
    integrity_tests = TestRAGIntegrity()
    integrity_tests.setup_method()
    
    tests_to_run.extend([
        (integrity_tests.test_vector_store_integrity, "Vector store integrity"),
        (integrity_tests.test_metadata_completeness, "Metadata completeness"),
        (integrity_tests.test_empty_results_handling, "Empty results handling"),
    ])
    
    # Run all tests
    for test_func, test_name in tests_to_run:
        try:
            test_func()
            total_passed += 1
        except Exception as e:
            print(f"✗ {test_name} test failed: {e}")
            total_failed += 1
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Total:  {total_passed + total_failed}")
    
    if total_failed == 0:
        print("\n✅ All RAG tests passed!")
        return 0
    else:
        print(f"\n❌ {total_failed} test(s) failed!")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)