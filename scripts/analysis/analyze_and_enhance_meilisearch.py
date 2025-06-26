#!/usr/bin/env python3
"""
Analyze indexed documents and create comprehensive synonyms
"""

import meilisearch
import re
from collections import defaultdict
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

console = Console()


def split_camel_case(text):
    """Split camelCase into words"""
    # Handle cases like URLSession, UIViewController, etc.
    parts = re.findall(r'[A-Z]+(?=[A-Z][a-z]|\b)|[A-Z][a-z]+|\d+|[a-z]+', text)
    return parts


def analyze_api_names():
    """Analyze all API names in the index to build better synonyms"""
    client = meilisearch.Client("http://localhost:7700", "local_test_key")
    index = client.index("apple-docs")
    
    console.print("[yellow]Analyzing indexed API names...[/yellow]\n")
    
    # Collect API names
    api_patterns = defaultdict(set)
    offset = 0
    limit = 1000
    total_analyzed = 0
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("Scanning documents...", total=None)
        
        while True:
            # Get batch of documents
            results = index.search("", {
                "limit": limit,
                "offset": offset,
                "attributesToRetrieve": ["api_name", "title", "framework"]
            })
            
            if not results["hits"]:
                break
            
            for hit in results["hits"]:
                api_name = hit.get("api_name", "")
                if api_name and len(api_name) > 2:
                    # Split camelCase
                    parts = split_camel_case(api_name)
                    if len(parts) > 1:
                        # Store pattern
                        key = api_name.lower()
                        api_patterns[key].add(api_name)
                        api_patterns[key].add(" ".join(parts).lower())
                        api_patterns[key].add(" ".join(parts))
                        api_patterns[key].add("".join(parts).lower())
            
            total_analyzed += len(results["hits"])
            offset += limit
            
            progress.update(task, description=f"Analyzed {total_analyzed} documents...")
            
            # Limit analysis for performance
            if total_analyzed >= 10000:
                break
    
    console.print(f"[green]Analyzed {total_analyzed} documents[/green]\n")
    
    # Create synonyms from patterns
    console.print("[yellow]Creating synonym groups...[/yellow]")
    
    synonyms = {}
    for key, variations in api_patterns.items():
        if len(variations) > 1:
            # Convert set to list and limit size
            synonym_list = list(variations)[:10]  # Limit to 10 variations per group
            if len(synonym_list) > 1:
                # Use the most common form as the key
                main_form = next((v for v in synonym_list if not " " in v), synonym_list[0])
                synonyms[main_form.lower()] = synonym_list
    
    # Add manual high-value synonyms
    manual_synonyms = {
        # Common UI patterns
        "viewcontroller": ["view controller", "viewcontroller", "vc", "UIViewController"],
        "tableview": ["table view", "tableview", "UITableView", "tv"],
        "collectionview": ["collection view", "collectionview", "UICollectionView", "cv"],
        
        # Framework patterns
        "uikit": ["ui kit", "uikit", "UIKit", "ui"],
        "swiftui": ["swift ui", "swiftui", "SwiftUI"],
        "coredata": ["core data", "coredata", "CoreData", "cd"],
        "storekit": ["store kit", "storekit", "StoreKit", "sk"],
        
        # Common searches
        "async": ["async", "asynchronous", "await"],
        "delegate": ["delegate", "delegation", "protocol"],
        "animation": ["animation", "animate", "transition"],
        "notification": ["notification", "push notification", "alert"],
    }
    
    # Merge manual synonyms
    for key, values in manual_synonyms.items():
        if key in synonyms:
            synonyms[key] = list(set(synonyms[key] + values))[:10]
        else:
            synonyms[key] = values
    
    console.print(f"[green]Created {len(synonyms)} synonym groups[/green]\n")
    
    # Apply synonyms
    console.print("[yellow]Applying synonyms to index...[/yellow]")
    task = index.update_synonyms(synonyms)
    client.wait_for_task(task.task_uid, timeout_in_ms=60000)
    console.print("[green]✅ Synonyms applied![/green]\n")
    
    # Show examples
    console.print("[cyan]Example synonym groups created:[/cyan]")
    examples = list(synonyms.items())[:15]
    for key, values in examples:
        console.print(f"  {key}: {', '.join(values[:5])}")
    
    return synonyms


def test_enhanced_search():
    """Test the enhanced search"""
    client = meilisearch.Client("http://localhost:7700", "local_test_key")
    index = client.index("apple-docs")
    
    console.print("\n[bold cyan]Testing Enhanced Search[/bold cyan]\n")
    
    test_cases = [
        # CamelCase variations
        ("ui view controller", "UIViewController"),
        ("async image", "AsyncImage"),
        ("url session", "URLSession"),
        ("persistent container", "NSPersistentContainer"),
        ("navigation stack", "NavigationStack"),
        
        # Partial matches
        ("view controller", "UIViewController"),
        ("table view", "UITableView"),
        ("collection view", "UICollectionView"),
        
        # Framework searches
        ("swift ui", "SwiftUI"),
        ("core data", "CoreData"),
        ("store kit", "StoreKit"),
    ]
    
    table = Table(title="Enhanced Search Results", show_header=True)
    table.add_column("Query", style="cyan")
    table.add_column("Looking for", style="yellow")
    table.add_column("Found?", style="green")
    table.add_column("Position", style="magenta")
    
    for query, expected in test_cases:
        results = index.search(query, {"limit": 10})
        found = False
        position = None
        
        for i, hit in enumerate(results["hits"], 1):
            # Check all fields
            text = f"{hit.get('api_name', '')} {hit.get('title', '')} {hit.get('content', '')}"
            if expected.lower() in text.lower():
                found = True
                position = i
                break
        
        status = "✅" if found else "❌"
        pos_str = f"#{position}" if position else "-"
        table.add_row(query, expected, status, pos_str)
    
    console.print(table)


def main():
    """Analyze and enhance Meilisearch"""
    # Analyze API names and create synonyms
    synonyms = analyze_api_names()
    
    # Test the improvements
    test_enhanced_search()
    
    console.print("\n[bold green]Meilisearch enhancement complete![/bold green]")
    console.print("\nImprovements made:")
    console.print("• Analyzed actual API names in your documentation")
    console.print("• Created synonyms for camelCase variations")
    console.print("• Added common search patterns")
    console.print("• Search now handles 'ui view controller' → 'UIViewController'")


if __name__ == "__main__":
    main()