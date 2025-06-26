#!/usr/bin/env python3
"""Verify that all documents were properly indexed in Meilisearch."""

import os
import sys
import json
from pathlib import Path
from collections import defaultdict
import meilisearch
from rich.console import Console
from rich.table import Table
from dotenv import load_dotenv

load_dotenv()

console = Console()

def count_filesystem_files(docs_path: Path) -> dict:
    """Count actual markdown files in filesystem by framework."""
    framework_counts = defaultdict(int)
    total = 0
    
    for framework_dir in docs_path.iterdir():
        if framework_dir.is_dir() and not framework_dir.name.startswith('.'):
            md_files = list(framework_dir.rglob("*.md"))
            framework_counts[framework_dir.name] = len(md_files)
            total += len(md_files)
    
    return dict(framework_counts), total

def check_meilisearch_counts(client, index_name: str) -> dict:
    """Check document counts in Meilisearch."""
    try:
        index = client.index(index_name)
        
        # Get total documents
        stats = index.get_stats()
        # stats is an object, not a dict
        total_docs = stats.number_of_documents if hasattr(stats, 'number_of_documents') else 0
        
        # Get framework counts
        framework_counts = {}
        
        # Get unique frameworks using facets
        facet_result = index.search('', {
            'facets': ['framework'],
            'limit': 0
        })
        
        if 'facetDistribution' in facet_result and 'framework' in facet_result['facetDistribution']:
            framework_counts = facet_result['facetDistribution']['framework']
        
        return framework_counts, total_docs
        
    except Exception as e:
        console.print(f"[red]Error accessing Meilisearch: {e}[/red]")
        return {}, 0

def verify_hash_file(hash_file_path: Path) -> dict:
    """Check what's in the hash file."""
    if not hash_file_path.exists():
        return {}, 0
    
    with open(hash_file_path, 'r') as f:
        hashes = json.load(f)
    
    framework_counts = defaultdict(int)
    for file_path in hashes.keys():
        parts = Path(file_path).parts
        if len(parts) > 0:
            framework = parts[0]
            framework_counts[framework] += 1
    
    return dict(framework_counts), len(hashes)

def main():
    """Run comprehensive verification."""
    docs_path = Path("../documentation")
    hash_file = Path("../.hashes/meilisearch_hashes.json")
    
    console.print("\n[bold]🔍 Meilisearch Indexing Verification[/bold]\n")
    
    # 1. Count filesystem files
    console.print("📁 Counting filesystem files...")
    fs_counts, fs_total = count_filesystem_files(docs_path)
    
    # 2. Check hash file
    console.print("📋 Checking hash file...")
    hash_counts, hash_total = verify_hash_file(hash_file)
    
    # 3. Check Meilisearch
    console.print("🔍 Checking Meilisearch index...")
    client = meilisearch.Client(
        os.getenv('MEILI_HTTP_ADDR', 'http://localhost:7700'),
        os.getenv('MEILI_MASTER_KEY', '')
    )
    
    ms_counts, ms_total = check_meilisearch_counts(client, 'apple-docs')
    
    # 4. Create comparison table
    console.print("\n[bold]Framework Comparison[/bold]")
    
    table = Table(title="Document Counts by Framework")
    table.add_column("Framework", style="cyan")
    table.add_column("Filesystem", style="green", justify="right")
    table.add_column("Hash File", style="yellow", justify="right")
    table.add_column("Meilisearch", style="blue", justify="right")
    table.add_column("FS-MS Diff", style="red", justify="right")
    table.add_column("Status", style="magenta")
    
    # Get all frameworks
    all_frameworks = set(fs_counts.keys()) | set(ms_counts.keys())
    
    # Focus on problematic frameworks first
    problematic = ['UIKit', 'Foundation', 'AppKit', 'Swift', 'SwiftUI', 'kernel', 'Matter']
    other_frameworks = sorted(all_frameworks - set(problematic))
    
    total_missing = 0
    
    for framework in problematic + other_frameworks:
        fs_count = fs_counts.get(framework, 0)
        hash_count = hash_counts.get(framework, 0)
        ms_count = int(ms_counts.get(framework, 0))
        diff = fs_count - ms_count
        total_missing += max(0, diff)
        
        status = "✓" if diff == 0 else f"❌ -{diff}" if diff > 0 else f"⚠️ +{-diff}"
        
        # Only show frameworks with differences or key ones
        if diff != 0 or framework in problematic:
            table.add_row(
                framework,
                f"{fs_count:,}",
                f"{hash_count:,}",
                f"{ms_count:,}",
                f"{diff:+,}",
                status
            )
    
    console.print(table)
    
    # Summary
    console.print("\n[bold]Summary[/bold]")
    summary_table = Table(show_header=False)
    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Value", style="yellow")
    
    summary_table.add_row("Total files in filesystem", f"{fs_total:,}")
    summary_table.add_row("Total files in hash file", f"{hash_total:,}")
    summary_table.add_row("Total documents in Meilisearch", f"{ms_total:,}")
    summary_table.add_row("Expected documents (with chunking)", "~340,769")
    summary_table.add_row("Missing documents", f"{fs_total - ms_total:,}")
    summary_table.add_row("Indexing failures reported", "519 tasks")
    
    console.print(summary_table)
    
    # Check for specific UIKit files
    console.print("\n[bold]UIKit Spot Check[/bold]")
    try:
        result = client.index('apple-docs').search('UIViewController', {
            'filter': 'framework = "UIKit"',
            'limit': 5
        })
        console.print(f"UIViewController search results: {result.get('estimatedTotalHits', 0)} hits")
        
        # Check a deep path file
        result2 = client.index('apple-docs').search('configuration', {
            'filter': 'framework = "UIKit" AND file_path CONTAINS "uipastecontrol"',
            'limit': 1
        })
        console.print(f"Deep path file search: {result2.get('estimatedTotalHits', 0)} hits")
    except Exception as e:
        console.print(f"[red]Search error: {e}[/red]")

if __name__ == "__main__":
    main()