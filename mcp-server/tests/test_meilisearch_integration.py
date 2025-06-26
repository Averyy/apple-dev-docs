#!/usr/bin/env python3
"""
Comprehensive End-to-End Integration Tests for Meilisearch MCP Server
Task 12: Test Full Local Setup

This test suite validates:
1. End-to-end integration testing
2. Performance validation with larger dataset
3. Error recovery scenarios  
4. Session management verification
"""

import asyncio
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from unittest.mock import patch
import pytest
import httpx
from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from meilisearch_adapter import MeilisearchRAGAdapter
from stdio_wrapper import MeilisearchStdioWrapper

console = Console()


class MeilisearchIntegrationTests:
    """Comprehensive integration tests for the Meilisearch MCP stack."""
    
    def __init__(self):
        self.meilisearch_url = os.getenv("MEILI_HTTP_ADDR", "http://localhost:7700")
        self.meilisearch_key = os.getenv("MEILI_MASTER_KEY", "local_test_key")
        self.test_results = {
            "passed": 0,
            "failed": 0,
            "errors": [],
            "performance_metrics": {},
            "start_time": datetime.now()
        }
        self.adapter: Optional[MeilisearchRAGAdapter] = None
        self.wrapper: Optional[MeilisearchStdioWrapper] = None
    
    async def setup(self):
        """Initialize test environment."""
        console.print("\n[bold blue]🔧 Setting up test environment...[/bold blue]")
        
        # Ensure Meilisearch is running first
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.meilisearch_url}/health")
                if response.status_code != 200:
                    raise Exception("Meilisearch is not healthy")
            console.print("✅ Meilisearch is running and healthy")
        except Exception as e:
            console.print(f"[red]❌ Meilisearch is not running: {e}[/red]")
            console.print("Please start Meilisearch with: cd meilisearch && ./start.sh")
            sys.exit(1)
        
        # Initialize adapter (no parameters needed)
        self.adapter = MeilisearchRAGAdapter()
        
        # Initialize the adapter's wrapper
        try:
            await self.adapter._ensure_initialized()
            console.print("✅ Meilisearch adapter initialized")
        except Exception as e:
            console.print(f"[red]❌ Failed to initialize adapter: {e}[/red]")
            sys.exit(1)
        
        # Get the wrapper reference for direct testing
        self.wrapper = self.adapter.wrapper
    
    async def teardown(self):
        """Clean up test environment."""
        if self.wrapper and self.wrapper.process:
            await self.wrapper.stop()
    
    def record_success(self, test_name: str, message: str = ""):
        """Record a successful test."""
        self.test_results["passed"] += 1
        console.print(f"✅ {test_name}: {message}")
    
    def record_failure(self, test_name: str, error: str):
        """Record a failed test."""
        self.test_results["failed"] += 1
        self.test_results["errors"].append(f"{test_name}: {error}")
        console.print(f"[red]❌ {test_name}: {error}[/red]")
    
    async def test_adapter_initialization(self):
        """Test 1: Verify adapter initializes correctly."""
        test_name = "Adapter Initialization"
        try:
            assert self.adapter is not None
            assert self.adapter.wrapper is not None
            assert self.adapter._initialized is True
            
            # Test wrapper is running
            assert self.wrapper.is_running is True
            assert self.wrapper.process is not None
            
            # Check wrapper stats
            stats = self.wrapper.get_stats()
            assert "wrapper_stats" in stats
            assert stats["subprocess_healthy"] is True
            
            self.record_success(test_name, f"Wrapper healthy: {stats['subprocess_healthy']}")
        except Exception as e:
            self.record_failure(test_name, str(e))
    
    async def test_basic_search(self):
        """Test 2: Verify basic search functionality."""
        test_name = "Basic Search"
        try:
            # Search for a common term
            results = await self.adapter.search("SwiftUI", platform="all", limit=5)
            
            # Check if we got results
            if len(results) > 0:
                assert all("score" in r for r in results), "Results missing score"
                assert all("metadata" in r for r in results), "Results missing metadata"
                self.record_success(test_name, f"Found {len(results)} results")
            else:
                # If no results, check if wrapper is working
                stats = self.wrapper.get_stats()
                if stats["wrapper_stats"]["failed_queries"] > 0:
                    self.record_failure(test_name, "Search requests failing - check meilisearch-mcp configuration")
                else:
                    self.record_failure(test_name, "No search results found - check if apple-docs index exists")
        except Exception as e:
            self.record_failure(test_name, str(e))
    
    async def test_platform_filtering(self):
        """Test 3: Verify platform-specific filtering."""
        test_name = "Platform Filtering"
        try:
            platforms = ["ios", "macos", "watchos", "tvos", "visionos"]
            platform_results = {}
            
            for platform in platforms:
                results = await self.adapter.search("View", platform=platform, limit=3)
                platform_results[platform] = len(results)
                
                # Verify platform filter is applied
                for result in results:
                    if "platforms" in result["metadata"]:
                        assert platform in [p.lower() for p in result["metadata"]["platforms"]], \
                            f"Result doesn't match platform filter: {platform}"
            
            self.record_success(test_name, f"Results per platform: {platform_results}")
        except Exception as e:
            self.record_failure(test_name, str(e))
    
    async def test_performance_large_dataset(self):
        """Test 4: Performance validation with larger queries."""
        test_name = "Performance (Large Dataset)"
        try:
            queries = [
                "SwiftUI Button",
                "UIViewController lifecycle",
                "AsyncSequence protocol",
                "CloudKit synchronization", 
                "Metal shader functions",
                "StoreKit in-app purchase",
                "ARKit scene understanding",
                "CoreML model training"
            ]
            
            latencies = []
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console
            ) as progress:
                task = progress.add_task("Running performance tests...", total=len(queries))
                
                for query in queries:
                    start_time = time.time()
                    results = await self.adapter.search(query, platform="all", limit=10)
                    latency = (time.time() - start_time) * 1000  # Convert to ms
                    latencies.append(latency)
                    progress.advance(task)
            
            # Calculate metrics
            avg_latency = sum(latencies) / len(latencies)
            max_latency = max(latencies)
            min_latency = min(latencies)
            
            self.test_results["performance_metrics"]["search_latencies"] = {
                "avg_ms": round(avg_latency, 2),
                "max_ms": round(max_latency, 2),
                "min_ms": round(min_latency, 2),
                "queries_tested": len(queries)
            }
            
            # Verify performance targets (should be < 50ms avg)
            assert avg_latency < 50, f"Average latency {avg_latency}ms exceeds 50ms target"
            
            self.record_success(test_name, 
                f"Avg: {avg_latency:.2f}ms, Max: {max_latency:.2f}ms, Min: {min_latency:.2f}ms")
        except Exception as e:
            self.record_failure(test_name, str(e))
    
    async def test_framework_listing(self):
        """Test 5: Verify framework listing functionality."""
        test_name = "Framework Listing"
        try:
            frameworks = await self.adapter.list_frameworks()
            
            assert len(frameworks) > 0, "No frameworks found"
            assert all("name" in f for f in frameworks), "Frameworks missing name"
            assert all("document_count" in f for f in frameworks), "Frameworks missing document count"
            
            # Find some common frameworks
            framework_names = [f["name"] for f in frameworks]
            expected_frameworks = ["SwiftUI", "UIKit", "Foundation"]
            found_frameworks = [f for f in expected_frameworks if f in framework_names]
            
            self.record_success(test_name, 
                f"Found {len(frameworks)} frameworks including: {', '.join(found_frameworks[:5])}")
        except Exception as e:
            self.record_failure(test_name, str(e))
    
    async def test_error_recovery(self):
        """Test 6: Error recovery scenarios."""
        test_name = "Error Recovery"
        try:
            # Test 1: Invalid query handling
            try:
                results = await self.adapter.search("", platform="all", limit=5)
                # Empty query should still work
                assert isinstance(results, list)
            except Exception:
                # Should handle gracefully
                pass
            
            # Test 2: Invalid platform handling
            results = await self.adapter.search("test", platform="invalid_platform", limit=5)
            assert isinstance(results, list), "Should handle invalid platform gracefully"
            
            # Test 3: Extreme limit handling
            results = await self.adapter.search("test", platform="all", limit=1000)
            assert len(results) <= 1000, "Should respect maximum limit"
            
            self.record_success(test_name, "All error scenarios handled gracefully")
        except Exception as e:
            self.record_failure(test_name, str(e))
    
    async def test_session_management(self):
        """Test 7: Session management for MCP protocol."""
        test_name = "Session Management"
        try:
            # The wrapper should already be running from setup
            assert self.wrapper is not None, "Wrapper not initialized"
            assert self.wrapper.process is not None, "Wrapper process not running"
            
            # Send test message
            test_request = {
                "jsonrpc": "2.0",
                "id": "test-1", 
                "method": "tools/list",
                "params": {}
            }
            
            response = await self.wrapper.send_mcp_request("tools/list", {})
            assert response is not None, "No response from wrapper"
            
            # Test wrapper stats
            stats = self.wrapper.get_stats()
            assert stats["wrapper_stats"]["total_queries"] > 0, "No requests tracked"
            assert stats["wrapper_stats"]["successful_queries"] > 0 or stats["wrapper_stats"]["failed_queries"] > 0, "No responses tracked"
            
            self.record_success(test_name, f"Session management working, {stats['wrapper_stats']['total_queries']} queries processed")
        except Exception as e:
            self.record_failure(test_name, str(e))
    
    async def test_concurrent_operations(self):
        """Test 8: Concurrent search operations."""
        test_name = "Concurrent Operations"
        try:
            queries = ["SwiftUI", "UIKit", "CoreData", "CloudKit", "Metal"]
            
            # Run searches concurrently
            start_time = time.time()
            tasks = [
                self.adapter.search(query, platform="all", limit=5)
                for query in queries
            ]
            results = await asyncio.gather(*tasks)
            duration = time.time() - start_time
            
            # Verify all searches completed
            assert len(results) == len(queries), "Not all concurrent searches completed"
            assert all(isinstance(r, list) for r in results), "Invalid result format"
            
            self.test_results["performance_metrics"]["concurrent_operations"] = {
                "queries": len(queries),
                "total_duration_seconds": round(duration, 2),
                "avg_per_query_seconds": round(duration / len(queries), 2)
            }
            
            self.record_success(test_name, 
                f"Completed {len(queries)} concurrent searches in {duration:.2f}s")
        except Exception as e:
            self.record_failure(test_name, str(e))
    
    async def test_search_quality(self):
        """Test 9: Search result quality and relevance."""
        test_name = "Search Quality"
        try:
            quality_tests = [
                ("SKStoreProductViewController", "StoreKit", "api_name match"),
                ("AsyncImage", "SwiftUI", "framework match"),
                ("viewDidLoad", "UIKit", "lifecycle method"),
                ("@Published", "Combine", "property wrapper")
            ]
            
            quality_results = []
            for query, expected_framework, test_type in quality_tests:
                results = await self.adapter.search(query, platform="all", limit=3)
                
                if results:
                    top_result = results[0]
                    framework = top_result["metadata"].get("framework", "")
                    score = top_result.get("score", 0)
                    
                    # Check if expected framework appears in top results
                    frameworks_found = [r["metadata"].get("framework", "") for r in results[:3]]
                    match_found = expected_framework in frameworks_found
                    
                    quality_results.append({
                        "query": query,
                        "expected": expected_framework,
                        "found": frameworks_found[0] if frameworks_found else "None",
                        "match": match_found,
                        "score": score
                    })
            
            # Calculate match rate
            if quality_results:
                matches = sum(1 for r in quality_results if r["match"])
                match_rate = (matches / len(quality_results)) * 100
            else:
                matches = 0
                match_rate = 0
            
            self.test_results["performance_metrics"]["search_quality"] = {
                "tests_run": len(quality_results),
                "matches": matches,
                "match_rate_percent": round(match_rate, 1)
            }
            
            self.record_success(test_name, f"Match rate: {match_rate:.1f}% ({matches}/{len(quality_results)})")
        except Exception as e:
            self.record_failure(test_name, str(e))
    
    async def test_stats_endpoint(self):
        """Test 10: Verify stats and monitoring endpoints."""
        test_name = "Stats Endpoint"
        try:
            # Get initial stats from adapter
            initial_metrics = self.adapter.search_metrics.copy()
            
            # Perform a search
            await self.adapter.search("test", platform="ios", limit=1)
            
            # Check stats are updated
            assert self.adapter.search_metrics["total_searches"] > initial_metrics["total_searches"], "Stats not updating"
            
            # Get wrapper stats
            wrapper_stats = self.wrapper.get_stats()
            assert wrapper_stats["subprocess_healthy"] is True, "Subprocess not healthy"
            assert wrapper_stats["wrapper_stats"]["total_queries"] > 0, "No queries tracked"
            
            self.record_success(test_name, f"Total searches tracked: {self.adapter.search_metrics['total_searches']}")
        except Exception as e:
            self.record_failure(test_name, str(e))
    
    def print_summary(self):
        """Print comprehensive test summary."""
        duration = (datetime.now() - self.test_results["start_time"]).total_seconds()
        
        console.print("\n[bold blue]📊 Test Summary[/bold blue]")
        console.print("=" * 50)
        
        # Results table
        table = Table(title="Test Results")
        table.add_column("Status", style="bold")
        table.add_column("Count", justify="right")
        table.add_row("✅ Passed", str(self.test_results["passed"]), style="green")
        table.add_row("❌ Failed", str(self.test_results["failed"]), style="red")
        table.add_row("Total", str(self.test_results["passed"] + self.test_results["failed"]))
        console.print(table)
        
        # Performance metrics
        if self.test_results["performance_metrics"]:
            console.print("\n[bold]Performance Metrics:[/bold]")
            metrics = self.test_results["performance_metrics"]
            
            if "search_latencies" in metrics:
                latencies = metrics["search_latencies"]
                console.print(f"  Search Latency: avg={latencies['avg_ms']}ms, "
                            f"max={latencies['max_ms']}ms, min={latencies['min_ms']}ms")
            
            if "concurrent_operations" in metrics:
                concurrent = metrics["concurrent_operations"]
                console.print(f"  Concurrent Ops: {concurrent['queries']} queries in "
                            f"{concurrent['total_duration_seconds']}s")
            
            if "search_quality" in metrics:
                quality = metrics["search_quality"]
                console.print(f"  Search Quality: {quality['match_rate_percent']}% match rate")
        
        # Errors
        if self.test_results["errors"]:
            console.print("\n[bold red]Errors:[/bold red]")
            for error in self.test_results["errors"]:
                console.print(f"  • {error}")
        
        console.print(f"\n[bold]Total Duration:[/bold] {duration:.2f} seconds")
        
        # Overall result
        if self.test_results["failed"] == 0:
            console.print("\n[bold green]🎉 All tests passed![/bold green]")
        else:
            console.print(f"\n[bold red]⚠️  {self.test_results['failed']} tests failed[/bold red]")
    
    async def run_all_tests(self):
        """Run all integration tests."""
        console.print("[bold green]🚀 Starting Meilisearch Integration Tests[/bold green]")
        console.print("=" * 50)
        
        await self.setup()
        
        # Run all tests
        tests = [
            self.test_adapter_initialization(),
            self.test_basic_search(),
            self.test_platform_filtering(),
            self.test_performance_large_dataset(),
            self.test_framework_listing(),
            self.test_error_recovery(),
            self.test_session_management(),
            self.test_concurrent_operations(),
            self.test_search_quality(),
            self.test_stats_endpoint()
        ]
        
        for test in tests:
            await test
            await asyncio.sleep(0.1)  # Small delay between tests
        
        await self.teardown()
        self.print_summary()
        
        # Return exit code
        return 0 if self.test_results["failed"] == 0 else 1


async def main():
    """Main entry point."""
    tester = MeilisearchIntegrationTests()
    exit_code = await tester.run_all_tests()
    sys.exit(exit_code)


if __name__ == "__main__":
    asyncio.run(main())