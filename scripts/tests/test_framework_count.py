#!/usr/bin/env python3
"""
Test script to verify all frameworks are properly indexed in Meilisearch
"""

import os
import sys
from pathlib import Path
import meilisearch
from rich.console import Console
from rich.table import Table

console = Console()

def count_documentation_frameworks():
    """Count frameworks in the documentation directory"""
    docs_path = Path("./documentation")
    if not docs_path.exists():
        docs_path = Path("../documentation")
    
    frameworks = set()
    for framework_dir in docs_path.iterdir():
        if framework_dir.is_dir() and not framework_dir.name.startswith('.'):
            frameworks.add(framework_dir.name)
    
    return sorted(frameworks)

def check_meilisearch_frameworks():
    """Check frameworks indexed in Meilisearch"""
    url = os.getenv("MEILI_HTTP_ADDR", "http://localhost:7700")
    api_key = os.getenv("MEILI_MASTER_KEY", "local_test_key")
    
    try:
        client = meilisearch.Client(url, api_key)
        index = client.index("apple-docs")
        
        # Get all frameworks via facets with pagination
        # Meilisearch limits facets to 100 by default
        all_frameworks = set()
        
        # First, get a large sample to find all frameworks
        results = index.search("", {
            "facets": ["framework"], 
            "limit": 1000,
            "attributesToRetrieve": ["framework"]
        })
        
        # Extract frameworks from facet distribution
        facet_frameworks = results.get("facetDistribution", {}).get("framework", {})
        all_frameworks.update(facet_frameworks.keys())
        
        # Also extract from actual hits to catch any missed
        for hit in results.get("hits", []):
            if "framework" in hit:
                all_frameworks.add(hit["framework"])
        
        indexed_frameworks = all_frameworks
        
        return sorted(indexed_frameworks)
    except Exception as e:
        console.print(f"[red]Error connecting to Meilisearch: {e}[/red]")
        return []

def main():
    console.print("[bold]Apple Developer Documentation Framework Verification[/bold]\n")
    
    # Count documentation frameworks
    doc_frameworks = count_documentation_frameworks()
    console.print(f"📁 Frameworks in documentation directory: [green]{len(doc_frameworks)}[/green]")
    
    # Check indexed frameworks
    indexed_frameworks = check_meilisearch_frameworks()
    console.print(f"🔍 Frameworks indexed in Meilisearch: [yellow]{len(indexed_frameworks)}[/yellow]")
    
    # Find missing frameworks
    missing = set(doc_frameworks) - set(indexed_frameworks)
    
    # Critical frameworks that MUST be present
    critical_frameworks = {
        "SwiftUI", "UIKit", "Foundation", "CoreData", "Combine",
        "RealityKit", "Metal", "MetalKit", "Vision", "CoreML",
        "AVFoundation", "StoreKit", "WidgetKit", "CloudKit", "MapKit",
        "WebKit", "PDFKit", "PencilKit", "PhotoKit", "SpriteKit",
        "SceneKit", "GameKit", "HealthKit", "HomeKit", "CarPlay"
    }
    
    missing_critical = critical_frameworks & missing
    
    # Display results
    if missing:
        console.print(f"\n❌ [red]Missing {len(missing)} frameworks![/red]")
        
        if missing_critical:
            console.print(f"\n[bold red]CRITICAL: Missing {len(missing_critical)} essential frameworks:[/bold red]")
            table = Table(title="Missing Critical Frameworks", show_header=False)
            table.add_column("Framework", style="red")
            
            for fw in sorted(missing_critical):
                table.add_row(fw)
            
            console.print(table)
        
        # Show sample of other missing frameworks
        other_missing = missing - missing_critical
        if other_missing and len(other_missing) > 10:
            console.print(f"\n[yellow]Plus {len(other_missing)} other frameworks (showing first 10):[/yellow]")
            for fw in sorted(other_missing)[:10]:
                console.print(f"  - {fw}")
    else:
        console.print("\n✅ [green]All frameworks are properly indexed![/green]")
    
    # Summary table
    console.print("\n")
    summary = Table(title="Framework Index Summary")
    summary.add_column("Status", style="bold")
    summary.add_column("Count", justify="right")
    
    summary.add_row("Documentation Frameworks", str(len(doc_frameworks)))
    summary.add_row("Indexed Frameworks", str(len(indexed_frameworks)))
    summary.add_row("Missing Frameworks", str(len(missing)), style="red" if missing else "green")
    summary.add_row("Missing Critical", str(len(missing_critical)), style="red" if missing_critical else "green")
    
    console.print(summary)
    
    # Test result
    min_required = 360
    if len(indexed_frameworks) < min_required:
        console.print(f"\n[bold red]❌ FAIL: Need at least {min_required} frameworks, found {len(indexed_frameworks)}[/bold red]")
        console.print("\n[yellow]To fix: Run the indexing script with correct parameters:[/yellow]")
        console.print("cd /Users/avery/Code/apple-developer-docs")
        console.print("python3 scripts/index_to_meilisearch.py --docs-path ./documentation --api-key local_test_key")
        return 1
    else:
        console.print(f"\n[bold green]✅ PASS: {len(indexed_frameworks)} frameworks indexed (minimum: {min_required})[/bold green]")
        return 0

if __name__ == "__main__":
    sys.exit(main())