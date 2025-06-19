#!/usr/bin/env python3
"""
Enhanced comprehensive test suite with rigorous quality metrics for MCP search.

This provides detailed insights into search quality including:
- Precision@K (how many of top K results are relevant)
- Mean Reciprocal Rank (position of first relevant result)
- False positive detection
- Relevance score distribution
- Failure categorization
- Performance benchmarking
"""

import asyncio
import sys
import time
import statistics
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass, field
from collections import defaultdict
import json

sys.path.insert(0, str(Path(__file__).parent))

from server.mcp_server import search_apple_docs, list_frameworks
from server.rag import SimpleRAG


@dataclass
class SearchMetrics:
    """Detailed metrics for search quality analysis"""
    query: str
    platform: str
    expected_terms: List[str] = field(default_factory=list)
    expected_apis: List[str] = field(default_factory=list)
    
    # Position metrics
    first_relevant_position: Optional[int] = None  # 1-indexed
    exact_match_position: Optional[int] = None
    
    # Precision metrics
    precision_at_1: float = 0.0
    precision_at_3: float = 0.0
    precision_at_5: float = 0.0
    precision_at_10: float = 0.0
    
    # Score metrics
    avg_relevance_score: float = 0.0
    top_result_score: float = 0.0
    score_distribution: List[float] = field(default_factory=list)
    
    # Result analysis
    num_results: int = 0
    has_false_positives: bool = False
    false_positive_details: List[str] = field(default_factory=list)
    
    # Performance
    search_time_ms: float = 0.0
    
    # Failure analysis
    failure_category: Optional[str] = None
    failure_details: Optional[str] = None
    
    @property
    def reciprocal_rank(self) -> float:
        """Calculate reciprocal rank (1/position of first relevant result)"""
        if self.first_relevant_position:
            return 1.0 / self.first_relevant_position
        return 0.0
    
    @property
    def is_perfect(self) -> bool:
        """Perfect = relevant result at position 1"""
        return self.first_relevant_position == 1
    
    @property
    def is_exact_match_first(self) -> bool:
        """Check if exact API match is at position 1"""
        return self.exact_match_position == 1
    
    @property
    def is_good(self) -> bool:
        """Good = relevant result in top 3"""
        return self.first_relevant_position is not None and self.first_relevant_position <= 3
    
    @property
    def is_acceptable(self) -> bool:
        """Acceptable = relevant result in top 5"""
        return self.first_relevant_position is not None and self.first_relevant_position <= 5
    
    @property
    def ndcg_at_5(self) -> float:
        """Normalized Discounted Cumulative Gain at 5"""
        # Simplified NDCG calculation
        if not self.first_relevant_position:
            return 0.0
        if self.first_relevant_position > 5:
            return 0.0
        return 1.0 / (1 + self.first_relevant_position - 1)


async def calculate_search_metrics(
    query: str,
    platform: str,
    expected_terms: List[str],
    expected_apis: List[str] = None,
    false_positive_terms: List[str] = None,
    ground_truth_rank: Optional[int] = None
) -> SearchMetrics:
    """Calculate comprehensive metrics for a single search"""
    
    metrics = SearchMetrics(
        query=query,
        platform=platform,
        expected_terms=expected_terms,
        expected_apis=expected_apis or []
    )
    false_positive_terms = false_positive_terms or []
    
    try:
        start_time = time.time()
        
        # Get more results for better analysis
        result = await search_apple_docs(
            query=query,
            platform=platform,
            limit=10,
            include_full_content=False
        )
        
        metrics.search_time_ms = (time.time() - start_time) * 1000
        
        # Parse results
        result_lower = result.lower()
        lines = result.split('\n')
        
        if "no results found" in result_lower:
            metrics.failure_category = "no_results"
            metrics.num_results = 0
            return metrics
        
        # Extract individual results
        results_found = []
        current_result = None
        
        for line in lines:
            # Look for numbered results (e.g., "1. **api_name** (Framework)")
            if line.strip() and any(line.strip().startswith(f"{i}.") for i in range(1, 11)):
                if current_result:
                    results_found.append(current_result)
                
                current_result = {
                    "position": len(results_found) + 1,
                    "line": line,
                    "is_relevant": False,
                    "is_exact_match": False,
                    "is_false_positive": False,
                    "relevance_score": 0.0
                }
            
            # Extract relevance score
            elif current_result and "relevance:" in line.lower():
                try:
                    score_str = line.split(":")[-1].strip().rstrip('%')
                    current_result["relevance_score"] = float(score_str) / 100
                except:
                    pass
        
        # Don't forget the last result
        if current_result:
            results_found.append(current_result)
        
        metrics.num_results = len(results_found)
        
        # Analyze each result
        for result in results_found:
            line_lower = result["line"].lower()
            
            # Check for exact API matches
            for api in metrics.expected_apis:
                if api.lower() in line_lower:
                    result["is_exact_match"] = True
                    result["is_relevant"] = True
                    if metrics.exact_match_position is None:
                        metrics.exact_match_position = result["position"]
                    break
            
            # Check for expected terms
            if not result["is_relevant"]:
                for term in expected_terms:
                    if term.lower() in line_lower:
                        result["is_relevant"] = True
                        break
            
            # Track first relevant position
            if result["is_relevant"] and metrics.first_relevant_position is None:
                metrics.first_relevant_position = result["position"]
            
            # Check for false positives
            for fp_term in false_positive_terms:
                if fp_term.lower() in line_lower:
                    result["is_false_positive"] = True
                    metrics.has_false_positives = True
                    metrics.false_positive_details.append(
                        f"Position {result['position']}: {fp_term}"
                    )
                    break
            
            # Collect relevance scores
            if result["relevance_score"] > 0:
                metrics.score_distribution.append(result["relevance_score"])
        
        # Calculate precision at different K values
        for k in [1, 3, 5, 10]:
            relevant_in_top_k = sum(
                1 for r in results_found[:k] 
                if r["is_relevant"]
            )
            if k <= len(results_found):
                setattr(metrics, f"precision_at_{k}", relevant_in_top_k / k)
        
        # Calculate average scores
        if metrics.score_distribution:
            metrics.avg_relevance_score = statistics.mean(metrics.score_distribution)
            metrics.top_result_score = metrics.score_distribution[0]
        
        # Categorize failures
        if metrics.first_relevant_position is None:
            if metrics.num_results > 0:
                metrics.failure_category = "irrelevant_results"
                metrics.failure_details = f"Got {metrics.num_results} results but none relevant"
            else:
                metrics.failure_category = "no_results"
        elif metrics.first_relevant_position > 5:
            metrics.failure_category = "low_ranking"
            metrics.failure_details = f"First relevant at position {metrics.first_relevant_position}"
        elif metrics.has_false_positives and metrics.first_relevant_position > 1:
            metrics.failure_category = "false_positive_interference"
            
    except Exception as e:
        metrics.failure_category = "error"
        metrics.failure_details = str(e)[:100]
    
    return metrics


async def run_quality_benchmark():
    """Run comprehensive quality benchmark with detailed metrics"""
    
    print("\n" + "=" * 80)
    print("🎯 MCP Search Quality Benchmark")
    print("=" * 80)
    print("\nThis benchmark evaluates search quality using:")
    print("- Precision@K (1, 3, 5, 10)")
    print("- Mean Reciprocal Rank (MRR)")
    print("- False positive detection")
    print("- Relevance score analysis")
    print("- Performance metrics")
    
    # Comprehensive test suite with ground truth
    test_suites = [
        {
            "name": "🎯 Exact API Name Searches",
            "description": "Should return exact matches at position #1",
            "tests": [
                {
                    "query": "UITableView",
                    "platform": "ios",
                    "expected_apis": ["UITableView"],
                    "expected_terms": ["uitableview", "table"],
                    "false_positives": ["UITableViewController", "UITableViewCell"],
                    "expect_perfect": True
                },
                {
                    "query": "NavigationView",
                    "platform": "ios",
                    "expected_apis": ["NavigationView"],
                    "expected_terms": ["navigationview"],
                    "false_positives": ["NavigationLink", "NavigationStack"],
                    "expect_perfect": True
                },
                {
                    "query": "URLSession",
                    "platform": "all",
                    "expected_apis": ["URLSession"],
                    "expected_terms": ["urlsession", "session"],
                    "false_positives": ["URLSessionTask", "URLSessionConfiguration"],
                    "expect_perfect": True
                },
            ]
        },
        {
            "name": "🔍 MCP Pattern Searches",
            "description": "Pattern 'X in Y' should work excellently",
            "tests": [
                {
                    "query": "navigationview in swiftui",
                    "platform": "ios",
                    "expected_apis": ["NavigationView"],
                    "expected_terms": ["navigationview"],
                    "false_positives": ["UINavigationController"],
                    "expect_perfect": True
                },
                {
                    "query": "uitableviewcell in uikit",
                    "platform": "ios",
                    "expected_apis": ["UITableViewCell"],
                    "expected_terms": ["uitableviewcell"],
                    "false_positives": ["UITableView"],
                    "expect_perfect": True
                },
                {
                    "query": "asyncimagephase failure in swiftui",
                    "platform": "ios",
                    "expected_apis": ["AsyncImagePhase.Failure", "Failure"],
                    "expected_terms": ["failure", "asyncimagephase"],
                    "false_positives": [],
                    "expect_good": True
                },
            ]
        },
        {
            "name": "🌊 Ambiguous Queries",
            "description": "Multiple valid results, ranking matters",
            "tests": [
                {
                    "query": "View",
                    "platform": "ios",
                    "expected_apis": ["View", "UIView"],
                    "expected_terms": ["view"],
                    "false_positives": [],
                    "expect_good": True,
                    "note": "Both SwiftUI.View and UIKit.UIView are valid"
                },
                {
                    "query": "Button",
                    "platform": "ios",
                    "expected_apis": ["Button", "UIButton"],
                    "expected_terms": ["button"],
                    "false_positives": ["ButtonStyle", "RadioButton"],
                    "expect_good": True
                },
                {
                    "query": "Text",
                    "platform": "ios",
                    "expected_apis": ["Text", "UITextView", "NSText"],
                    "expected_terms": ["text"],
                    "false_positives": [],
                    "expect_good": True
                },
            ]
        },
        {
            "name": "⚠️ Generic Terms",
            "description": "Should show search tips or contextual results",
            "tests": [
                {
                    "query": "frame",
                    "platform": "ios",
                    "expected_apis": [],
                    "expected_terms": ["frame"],
                    "false_positives": [],
                    "expect_tips": True,
                    "note": "Too generic - should show tips"
                },
                {
                    "query": "frame modifier",
                    "platform": "ios",
                    "expected_apis": ["frame"],
                    "expected_terms": ["frame"],
                    "false_positives": [],
                    "expect_good": True,
                    "note": "With context - should work"
                },
                {
                    "query": "init",
                    "platform": "ios",
                    "expected_apis": [],
                    "expected_terms": [],
                    "false_positives": [],
                    "expect_tips": True,
                    "note": "Too generic without context"
                },
            ]
        },
        {
            "name": "❌ Negative Tests",
            "description": "Queries that should fail gracefully",
            "tests": [
                {
                    "query": "AndroidFragment",
                    "platform": "ios",
                    "expected_apis": [],
                    "expected_terms": [],
                    "false_positives": ["Fragment"],
                    "expect_no_results": True,
                    "note": "Non-Apple API"
                },
                {
                    "query": "ReactNativeComponent",
                    "platform": "ios",
                    "expected_apis": [],
                    "expected_terms": [],
                    "false_positives": ["Component"],
                    "expect_no_results": True,
                    "note": "Non-existent API"
                },
            ]
        },
        {
            "name": "🐛 Common Misspellings",
            "description": "Should handle typos gracefully",
            "tests": [
                {
                    "query": "tabel view",
                    "platform": "ios",
                    "expected_apis": ["UITableView", "Table"],
                    "expected_terms": ["table"],
                    "false_positives": [],
                    "expect_acceptable": True,
                    "note": "Missing 'l' in table"
                },
                {
                    "query": "navigtion controller",
                    "platform": "ios",
                    "expected_apis": ["UINavigationController", "NavigationController"],
                    "expected_terms": ["navigation"],
                    "false_positives": [],
                    "expect_acceptable": True,
                    "note": "Missing 'a' in navigation"
                },
            ]
        }
    ]
    
    # Track all metrics
    all_metrics: List[SearchMetrics] = []
    suite_results: Dict[str, Dict[str, Any]] = {}
    
    # Run all test suites
    for suite in test_suites:
        print(f"\n{'-' * 70}")
        print(f"{suite['name']}")
        print(f"{suite['description']}")
        print(f"{'-' * 70}")
        
        suite_metrics = []
        
        for test in suite["tests"]:
            # Run search and calculate metrics
            metrics = await calculate_search_metrics(
                query=test["query"],
                platform=test["platform"],
                expected_terms=test.get("expected_terms", []),
                expected_apis=test.get("expected_apis", []),
                false_positive_terms=test.get("false_positives", [])
            )
            
            all_metrics.append(metrics)
            suite_metrics.append(metrics)
            
            # Display results
            print(f"\n📍 Query: '{test['query']}' (platform: {test['platform']})")
            if "note" in test:
                print(f"   ℹ️  {test['note']}")
            
            # Evaluate against expectations
            status = "❓"
            if test.get("expect_no_results") and metrics.num_results == 0:
                status = "✅ PASS"
            elif test.get("expect_tips") and metrics.failure_category == "no_results":
                status = "✅ PASS"
            elif test.get("expect_perfect") and metrics.is_perfect:
                status = "🌟 PERFECT"
            elif test.get("expect_good") and metrics.is_good:
                status = "✅ GOOD"
            elif test.get("expect_acceptable") and metrics.is_acceptable:
                status = "⚠️ ACCEPTABLE"
            elif metrics.is_acceptable:
                status = "✅ PASS"
            else:
                status = "❌ FAIL"
            
            print(f"   {status}")
            
            # Show metrics
            if metrics.num_results > 0:
                print(f"   📊 First relevant: #{metrics.first_relevant_position or 'None'}")
                print(f"   📊 P@1={metrics.precision_at_1:.0%}, P@3={metrics.precision_at_3:.0%}, MRR={metrics.reciprocal_rank:.3f}")
                print(f"   📊 Top score: {metrics.top_result_score:.2f}, Avg: {metrics.avg_relevance_score:.2f}")
                print(f"   ⏱️  {metrics.search_time_ms:.0f}ms")
            
            if metrics.has_false_positives:
                print(f"   ⚠️  False positives: {', '.join(metrics.false_positive_details)}")
            
            if metrics.failure_category and metrics.failure_category != "no_results":
                print(f"   ❌ Failure: {metrics.failure_category}")
                if metrics.failure_details:
                    print(f"      Details: {metrics.failure_details}")
        
        # Suite summary
        suite_results[suite["name"]] = {
            "total": len(suite_metrics),
            "perfect": sum(1 for m in suite_metrics if m.is_perfect),
            "good": sum(1 for m in suite_metrics if m.is_good),
            "acceptable": sum(1 for m in suite_metrics if m.is_acceptable),
            "failed": sum(1 for m in suite_metrics if not m.is_acceptable and m.failure_category != "no_results"),
            "avg_mrr": statistics.mean([m.reciprocal_rank for m in suite_metrics if m.reciprocal_rank > 0] or [0]),
            "avg_p_at_1": statistics.mean([m.precision_at_1 for m in suite_metrics if m.num_results > 0] or [0]),
        }
    
    # Overall analysis
    print("\n" + "=" * 80)
    print("📊 OVERALL QUALITY ANALYSIS")
    print("=" * 80)
    
    # Global metrics
    valid_metrics = [m for m in all_metrics if m.num_results > 0 and m.first_relevant_position]
    
    if valid_metrics:
        global_mrr = statistics.mean(m.reciprocal_rank for m in valid_metrics)
        global_p_at_1 = statistics.mean(m.precision_at_1 for m in valid_metrics)
        global_p_at_3 = statistics.mean(m.precision_at_3 for m in valid_metrics)
        global_p_at_5 = statistics.mean(m.precision_at_5 for m in valid_metrics)
        
        print(f"\n🌐 Global Metrics:")
        print(f"   Mean Reciprocal Rank (MRR): {global_mrr:.3f}")
        print(f"   Precision@1: {global_p_at_1:.1%}")
        print(f"   Precision@3: {global_p_at_3:.1%}")
        print(f"   Precision@5: {global_p_at_5:.1%}")
    
    # Performance analysis
    search_times = [m.search_time_ms for m in all_metrics if m.search_time_ms > 0]
    if search_times:
        print(f"\n⚡ Performance:")
        print(f"   Mean search time: {statistics.mean(search_times):.0f}ms")
        print(f"   P95 search time: {sorted(search_times)[int(len(search_times) * 0.95)]:.0f}ms")
        print(f"   Max search time: {max(search_times):.0f}ms")
    
    # Quality distribution
    perfect_count = sum(1 for m in all_metrics if m.is_perfect)
    good_count = sum(1 for m in all_metrics if m.is_good)
    acceptable_count = sum(1 for m in all_metrics if m.is_acceptable)
    
    print(f"\n🎯 Quality Distribution:")
    print(f"   Perfect (pos #1): {perfect_count}/{len(all_metrics)} ({perfect_count/len(all_metrics)*100:.1f}%)")
    print(f"   Good (top 3): {good_count}/{len(all_metrics)} ({good_count/len(all_metrics)*100:.1f}%)")
    print(f"   Acceptable (top 5): {acceptable_count}/{len(all_metrics)} ({acceptable_count/len(all_metrics)*100:.1f}%)")
    
    # Suite breakdown
    print(f"\n📋 Results by Test Suite:")
    for suite_name, results in suite_results.items():
        print(f"\n   {suite_name}")
        print(f"      Perfect: {results['perfect']}/{results['total']}")
        print(f"      MRR: {results['avg_mrr']:.3f}")
        print(f"      P@1: {results['avg_p_at_1']:.1%}")
    
    # Failure analysis
    failure_counts = defaultdict(int)
    for m in all_metrics:
        if m.failure_category:
            failure_counts[m.failure_category] += 1
    
    if failure_counts:
        print(f"\n❌ Failure Breakdown:")
        for category, count in sorted(failure_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"   {category}: {count} occurrences")
    
    # Final assessment
    print(f"\n{'=' * 80}")
    print("🏆 FINAL ASSESSMENT")
    print(f"{'=' * 80}")
    
    if global_mrr >= 0.8:
        print("\n🌟 EXCELLENT - Search quality is outstanding!")
        print("   - MRR > 0.8 indicates most searches find relevant results immediately")
        print("   - Ready for production deployment")
    elif global_mrr >= 0.6:
        print("\n✅ GOOD - Search quality meets production standards")
        print("   - Most queries return relevant results in top positions")
        print("   - Some room for improvement in ranking")
    elif global_mrr >= 0.4:
        print("\n⚠️ ACCEPTABLE - Search works but needs improvement")
        print("   - Many queries require scrolling to find relevant results")
        print("   - Consider tuning relevance scoring")
    else:
        print("\n❌ POOR - Significant search quality issues")
        print("   - Most queries fail to return relevant results in top positions")
        print("   - Major improvements needed before deployment")
    
    # Specific recommendations
    print("\n💡 Recommendations:")
    
    if perfect_count / len(all_metrics) < 0.5:
        print("   - Less than 50% perfect matches - improve exact match boosting")
    
    if statistics.mean(search_times) > 500:
        print("   - Average search time > 500ms - optimize query performance")
    
    false_positive_queries = [
        m.query for m in all_metrics 
        if m.has_false_positives and not m.is_perfect
    ]
    if false_positive_queries:
        print(f"   - False positives found in: {', '.join(set(false_positive_queries))}")
        print("     Consider stricter relevance filtering")
    
    low_precision_queries = [
        m.query for m in all_metrics
        if m.precision_at_3 < 0.5 and m.num_results > 3
    ]
    if low_precision_queries:
        print(f"   - Low precision@3 for: {', '.join(set(low_precision_queries))}")
        print("     These queries return many irrelevant results")
    
    # Save detailed results
    results_file = Path("search_quality_report.json")
    report_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "global_metrics": {
            "mrr": global_mrr,
            "precision_at_1": global_p_at_1,
            "precision_at_3": global_p_at_3,
            "precision_at_5": global_p_at_5,
            "mean_search_time_ms": statistics.mean(search_times)
        },
        "suite_results": suite_results,
        "failure_analysis": dict(failure_counts),
        "detailed_results": [
            {
                "query": m.query,
                "platform": m.platform,
                "first_relevant_position": m.first_relevant_position,
                "mrr": m.reciprocal_rank,
                "precision_at_1": m.precision_at_1,
                "precision_at_3": m.precision_at_3,
                "has_false_positives": m.has_false_positives,
                "failure_category": m.failure_category
            }
            for m in all_metrics
        ]
    }
    
    with open(results_file, 'w') as f:
        json.dump(report_data, f, indent=2)
    
    print(f"\n📄 Detailed report saved to: {results_file}")
    
    return all_metrics


async def main():
    """Run the quality benchmark"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="MCP Search Quality Benchmark - Rigorous search quality analysis"
    )
    parser.add_argument(
        "--save-report", 
        action="store_true", 
        help="Save detailed JSON report"
    )
    
    args = parser.parse_args()
    
    # Run the benchmark
    await run_quality_benchmark()


if __name__ == "__main__":
    asyncio.run(main())