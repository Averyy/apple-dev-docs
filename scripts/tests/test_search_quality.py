#!/usr/bin/env python3
"""
Test Meilisearch search quality against ChromaDB baseline.

This script runs the same test queries used in the ChromaDB baseline
against Meilisearch and compares latency and relevance metrics.
"""

import json
import time
import argparse
from datetime import datetime
from typing import Dict, List, Any, Tuple, Optional
import statistics
from pathlib import Path

import meilisearch
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

class MeilisearchQualityTest:
    """Test Meilisearch search quality and performance."""
    
    def __init__(self, meilisearch_url: str, api_key: str, index_name: str = "apple-docs"):
        """Initialize the test client."""
        self.client = meilisearch.Client(meilisearch_url, api_key)
        self.index = self.client.index(index_name)
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "system": "Meilisearch",
            "metrics": {},
            "test_queries": [],
            "quality_scores": {},
            "comparison": {}
        }
        
    def get_test_queries(self) -> List[Tuple[str, str, List[str]]]:
        """Get test queries from ChromaDB baseline.
        Returns: List of (query, expected_framework, expected_platforms)
        """
        return [
            # API name searches
            ("View", "SwiftUI", ["iOS", "macOS", "tvOS", "watchOS"]),
            ("UIView", "UIKit", ["iOS", "tvOS"]),
            ("NSView", "AppKit", ["macOS"]),
            ("URLSession", "Foundation", ["iOS", "macOS", "tvOS", "watchOS"]),
            ("SKScene", "SpriteKit", ["iOS", "macOS", "tvOS", "watchOS"]),
            ("SKStore", "StoreKit", ["iOS", "macOS", "tvOS", "watchOS"]),
            
            # Framework searches
            ("SwiftUI framework", "SwiftUI", []),
            ("Core Data framework", "CoreData", []),
            ("Combine publisher", "Combine", []),
            ("storekit", "StoreKit", []),
            ("uikit", "UIKit", []),
            ("swiftui", "SwiftUI", []),
            
            # Multi-word queries
            ("navigation controller", "UIKit", ["iOS", "tvOS"]),
            ("scene delegate", "UIKit", ["iOS"]),
            ("core location manager", "CoreLocation", ["iOS", "macOS", "tvOS", "watchOS"]),
            ("async image", "SwiftUI", []),
            ("view controller", "UIKit", []),
            
            # CamelCase queries
            ("URLSessionDataTask", "Foundation", []),
            ("NSManagedObjectContext", "CoreData", []),
            ("UICollectionViewFlowLayout", "UIKit", ["iOS", "tvOS"]),
            ("NSAttributedString", "Foundation", []),
            
            # MCP pattern queries
            ("View in SwiftUI", "SwiftUI", []),
            ("Button in UIKit", "UIKit", []),
            ("Publisher in Combine", "Combine", []),
            ("SKStore in StoreKit", "StoreKit", []),
            
            # Platform-specific queries
            ("watchOS complications", "ClockKit", ["watchOS"]),
            ("tvOS focus engine", "UIKit", ["tvOS"]),
            ("macOS menu bar", "AppKit", ["macOS"]),
            ("ios UIView", "UIKit", ["iOS"]),
            ("macos NSWindow", "AppKit", ["macOS"]),
            
            # Common patterns
            ("init", None, []),  # Should return many results
            ("frame", None, []),  # Common across frameworks
            ("delegate", None, []),  # Common pattern
            
            # Complex queries
            ("async await swift concurrency", "Swift", []),
            ("state management swiftui", "SwiftUI", []),
            ("core data migration", "CoreData", []),
        ]
    
    def measure_latency(self, query: str, platform: Optional[str] = None, iterations: int = 5) -> Dict[str, float]:
        """Measure search latency statistics."""
        latencies = []
        
        for _ in range(iterations):
            start = time.time()
            try:
                opt_params = {
                    "limit": 10,
                }
                if platform:
                    opt_params["filter"] = f'platforms = "{platform}"'
                
                self.index.search(query, opt_params)
                latencies.append((time.time() - start) * 1000)  # Convert to ms
            except Exception as e:
                console.print(f"[red]Error during search: {e}[/red]")
                latencies.append(float('inf'))
        
        # Remove outliers (top and bottom 10%)
        if len(latencies) > 10:
            sorted_latencies = sorted(latencies)
            trim_count = len(latencies) // 10
            latencies = sorted_latencies[trim_count:-trim_count] if trim_count > 0 else sorted_latencies
        
        return {
            "min": min(latencies) if latencies else 0,
            "max": max(latencies) if latencies else 0,
            "mean": statistics.mean(latencies) if latencies else 0,
            "median": statistics.median(latencies) if latencies else 0,
            "p95": sorted(latencies)[int(len(latencies) * 0.95)] if latencies else 0,
            "p99": sorted(latencies)[int(len(latencies) * 0.99)] if latencies else 0,
        }
    
    def measure_relevance(self, query: str, expected_framework: Optional[str] = None) -> Dict[str, Any]:
        """Measure search relevance and quality."""
        try:
            results = self.index.search(query, {"limit": 10})
            hits = results.get("hits", [])
            
            metrics = {
                "total_results": len(hits),
                "has_results": len(hits) > 0,
                "processing_time_ms": results.get("processingTimeMs", 0),
                "query": results.get("query", query),
            }
            
            if expected_framework and hits:
                # Check if expected framework appears in top results
                top_1_match = hits[0].get("framework", "").lower() == expected_framework.lower()
                top_3_match = any(h.get("framework", "").lower() == expected_framework.lower() for h in hits[:3])
                top_5_match = any(h.get("framework", "").lower() == expected_framework.lower() for h in hits[:5])
                
                # Find rank of expected framework
                expected_rank = -1
                for i, hit in enumerate(hits):
                    if hit.get("framework", "").lower() == expected_framework.lower():
                        expected_rank = i + 1
                        break
                
                metrics.update({
                    "top_1_accuracy": top_1_match,
                    "top_3_accuracy": top_3_match,
                    "top_5_accuracy": top_5_match,
                    "expected_framework_rank": expected_rank
                })
            
            return metrics
            
        except Exception as e:
            return {"error": str(e), "has_results": False}
    
    def load_baseline(self, baseline_path: str = "benchmarks/chromadb_baseline.json") -> Optional[Dict]:
        """Load ChromaDB baseline results for comparison."""
        try:
            with open(baseline_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            console.print(f"[yellow]Warning: Could not load baseline: {e}[/yellow]")
            return None
    
    def run_tests(self, verbose: bool = False) -> None:
        """Run complete test suite."""
        console.print("\n[bold cyan]🔍 Meilisearch Search Quality Test[/bold cyan]\n")
        
        # 1. Index stats
        console.print("[bold]📊 Gathering index statistics...[/bold]")
        try:
            stats = self.index.get_stats()
            doc_count = stats["numberOfDocuments"]
            self.results["metrics"]["document_count"] = doc_count
            console.print(f"   Documents in index: [green]{doc_count:,}[/green]")
            if "fieldDistribution" in stats and "api_name" in stats["fieldDistribution"]:
                console.print(f"   Index size: [green]{stats['fieldDistribution']['api_name']:,}[/green] unique API names")
        except Exception as e:
            console.print(f"   [red]Error getting stats: {e}[/red]")
        
        # 2. Latency benchmarks
        console.print("\n[bold]⏱️  Measuring search latency...[/bold]")
        test_queries = self.get_test_queries()
        
        all_latencies = []
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Testing queries...", total=len(test_queries[:20]))
            
            for query, _, _ in test_queries[:20]:  # Use first 20 for latency
                if query:  # Skip empty query
                    latency = self.measure_latency(query)
                    all_latencies.append(latency["mean"])
                    progress.update(task, advance=1)
        
        self.results["metrics"]["latency"] = {
            "overall_mean_ms": statistics.mean(all_latencies),
            "overall_p95_ms": sorted(all_latencies)[int(len(all_latencies) * 0.95)],
            "overall_p99_ms": sorted(all_latencies)[int(len(all_latencies) * 0.99)],
        }
        
        console.print(f"   Mean latency: [green]{self.results['metrics']['latency']['overall_mean_ms']:.2f}ms[/green]")
        console.print(f"   P95 latency: [green]{self.results['metrics']['latency']['overall_p95_ms']:.2f}ms[/green]")
        console.print(f"   P99 latency: [green]{self.results['metrics']['latency']['overall_p99_ms']:.2f}ms[/green]")
        
        # 3. Platform filter latency
        console.print("\n[bold]🎯 Measuring platform filter performance...[/bold]")
        platform_latencies = {}
        for platform in ["iOS", "macOS", "watchOS", "tvOS"]:
            latency = self.measure_latency("View", platform=platform)
            platform_latencies[platform] = latency["mean"]
            console.print(f"   {platform}: [green]{latency['mean']:.2f}ms[/green]")
        
        self.results["metrics"]["platform_filter_latency_ms"] = platform_latencies
        
        # 4. Relevance and quality
        console.print("\n[bold]✨ Measuring search quality...[/bold]")
        quality_metrics = {
            "top_1_accuracy": [],
            "top_3_accuracy": [],
            "top_5_accuracy": [],
            "has_results_rate": [],
        }
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Testing relevance...", total=len(test_queries))
            
            for query, expected_framework, _ in test_queries:
                if query:  # Skip empty query
                    relevance = self.measure_relevance(query, expected_framework)
                    
                    if expected_framework and "top_1_accuracy" in relevance:
                        quality_metrics["top_1_accuracy"].append(relevance["top_1_accuracy"])
                        quality_metrics["top_3_accuracy"].append(relevance["top_3_accuracy"])
                        quality_metrics["top_5_accuracy"].append(relevance["top_5_accuracy"])
                    
                    quality_metrics["has_results_rate"].append(relevance.get("has_results", False))
                    
                    if verbose:
                        self.results["test_queries"].append({
                            "query": query,
                            "expected_framework": expected_framework,
                            "relevance": relevance
                        })
                    
                    progress.update(task, advance=1)
        
        # Calculate quality scores
        self.results["quality_scores"] = {
            "top_1_accuracy": statistics.mean(quality_metrics["top_1_accuracy"]) if quality_metrics["top_1_accuracy"] else 0,
            "top_3_accuracy": statistics.mean(quality_metrics["top_3_accuracy"]) if quality_metrics["top_3_accuracy"] else 0,
            "top_5_accuracy": statistics.mean(quality_metrics["top_5_accuracy"]) if quality_metrics["top_5_accuracy"] else 0,
            "has_results_rate": statistics.mean(quality_metrics["has_results_rate"]) if quality_metrics["has_results_rate"] else 0,
        }
        
        console.print(f"\n   Top-1 accuracy: [green]{self.results['quality_scores']['top_1_accuracy']:.1%}[/green]")
        console.print(f"   Top-3 accuracy: [green]{self.results['quality_scores']['top_3_accuracy']:.1%}[/green]")
        console.print(f"   Top-5 accuracy: [green]{self.results['quality_scores']['top_5_accuracy']:.1%}[/green]")
        console.print(f"   Has results rate: [green]{self.results['quality_scores']['has_results_rate']:.1%}[/green]")
        
        # 5. Compare with baseline
        baseline = self.load_baseline()
        if baseline:
            self.compare_with_baseline(baseline)
    
    def compare_with_baseline(self, baseline: Dict) -> None:
        """Compare results with ChromaDB baseline."""
        console.print("\n[bold]📈 Comparison with ChromaDB Baseline[/bold]\n")
        
        # Create comparison table
        table = Table(title="Performance Comparison")
        table.add_column("Metric", style="cyan")
        table.add_column("ChromaDB", style="yellow")
        table.add_column("Meilisearch", style="green")
        table.add_column("Improvement", style="bold")
        
        # Latency comparison
        chromadb_mean = baseline["metrics"]["latency"]["overall_mean_ms"]
        meili_mean = self.results["metrics"]["latency"]["overall_mean_ms"]
        improvement = ((chromadb_mean - meili_mean) / chromadb_mean) * 100
        
        table.add_row(
            "Mean Latency",
            f"{chromadb_mean:.2f}ms",
            f"{meili_mean:.2f}ms",
            f"{improvement:+.1f}%" if improvement > 0 else f"{improvement:.1f}%"
        )
        
        # P95 latency
        chromadb_p95 = baseline["metrics"]["latency"]["overall_p95_ms"]
        meili_p95 = self.results["metrics"]["latency"]["overall_p95_ms"]
        improvement = ((chromadb_p95 - meili_p95) / chromadb_p95) * 100
        
        table.add_row(
            "P95 Latency",
            f"{chromadb_p95:.2f}ms",
            f"{meili_p95:.2f}ms",
            f"{improvement:+.1f}%" if improvement > 0 else f"{improvement:.1f}%"
        )
        
        # Quality comparison
        if "quality_scores" in baseline:
            chromadb_top1 = baseline["quality_scores"].get("top_1_accuracy", 0)
            meili_top1 = self.results["quality_scores"]["top_1_accuracy"]
            improvement = ((meili_top1 - chromadb_top1) / chromadb_top1) * 100 if chromadb_top1 > 0 else 0
            
            table.add_row(
                "Top-1 Accuracy",
                f"{chromadb_top1:.1%}",
                f"{meili_top1:.1%}",
                f"{improvement:+.1f}%" if improvement > 0 else f"{improvement:.1f}%"
            )
            
            chromadb_top3 = baseline["quality_scores"].get("top_3_accuracy", 0)
            meili_top3 = self.results["quality_scores"]["top_3_accuracy"]
            improvement = ((meili_top3 - chromadb_top3) / chromadb_top3) * 100 if chromadb_top3 > 0 else 0
            
            table.add_row(
                "Top-3 Accuracy",
                f"{chromadb_top3:.1%}",
                f"{meili_top3:.1%}",
                f"{improvement:+.1f}%" if improvement > 0 else f"{improvement:.1f}%"
            )
        
        console.print(table)
        
        # Store comparison
        self.results["comparison"] = {
            "baseline_system": "ChromaDB",
            "latency_improvement": ((chromadb_mean - meili_mean) / chromadb_mean) * 100,
            "quality_change": ((meili_top1 - chromadb_top1) / chromadb_top1) * 100 if chromadb_top1 > 0 else 0
        }
    
    def save_results(self, output_path: str) -> None:
        """Save test results to JSON file."""
        with open(output_path, 'w') as f:
            json.dump(self.results, f, indent=2)
        console.print(f"\n[green]✅ Results saved to {output_path}[/green]")


def main():
    parser = argparse.ArgumentParser(description="Test Meilisearch search quality")
    parser.add_argument("--url", default="http://localhost:7700", help="Meilisearch URL")
    parser.add_argument("--api-key", default="local_test_key", help="Meilisearch API key")
    parser.add_argument("--index", default="apple-docs", help="Index name")
    parser.add_argument("--verbose", action="store_true", help="Include detailed query results")
    parser.add_argument("--output", default="meilisearch_quality_results.json", help="Output file for results")
    
    args = parser.parse_args()
    
    tester = MeilisearchQualityTest(args.url, args.api_key, args.index)
    tester.run_tests(verbose=args.verbose)
    tester.save_results(args.output)


if __name__ == "__main__":
    main()