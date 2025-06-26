#!/usr/bin/env python3
"""
Configure Meilisearch index settings for Apple Developer documentation.

This script sets up the optimal configuration for searching Apple docs,
including searchable attributes, filters, ranking rules, and typo tolerance.
"""

import os
import sys
import json
import argparse
from typing import Dict, List
import meilisearch
from rich.console import Console
from rich.table import Table
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

console = Console()

class IndexConfigurator:
    """Configure Meilisearch index settings"""
    
    def __init__(self, meilisearch_url: str, api_key: str, index_name: str = "apple-docs"):
        """
        Initialize configurator
        
        Args:
            meilisearch_url: URL of Meilisearch instance
            api_key: Master key or API key for Meilisearch
            index_name: Name of the index to configure
        """
        self.client = meilisearch.Client(meilisearch_url, api_key)
        self.index_name = index_name
        self.index = self.client.index(index_name)
        
    def get_current_settings(self) -> Dict:
        """Get current index settings"""
        return self.index.get_settings()
    
    def configure_searchable_attributes(self):
        """Configure searchable attributes with priority order"""
        searchable_attributes = [
            "api_name",           # Highest priority - exact API names
            "title",              # Document title
            "overview",           # Short description
            "content_cleaned",    # Main content (cleaned for search)
            "framework",          # Framework name
            "kind",              # Type (class, struct, etc.)
            "platforms"          # Platform names
        ]
        
        console.print("📝 Configuring searchable attributes...")
        task = self.index.update_searchable_attributes(searchable_attributes)
        self.client.wait_for_task(task.task_uid if hasattr(task, 'task_uid') else task['taskUid'])
        console.print("[green]✓ Searchable attributes configured[/green]")
        
    def configure_filterable_attributes(self):
        """Configure attributes that can be used in filters"""
        filterable_attributes = [
            "framework",          # Filter by framework
            "platforms",          # Filter by platform
            "kind",              # Filter by type
            "is_framework_main", # Filter main framework pages
            "file_size",         # Filter by size
            "last_modified"      # Filter by date
        ]
        
        console.print("🔍 Configuring filterable attributes...")
        task = self.index.update_filterable_attributes(filterable_attributes)
        self.client.wait_for_task(task.task_uid if hasattr(task, 'task_uid') else task['taskUid'])
        console.print("[green]✓ Filterable attributes configured[/green]")
        
    def configure_sortable_attributes(self):
        """Configure attributes that can be used for sorting"""
        sortable_attributes = [
            "last_modified",     # Sort by modification date
            "file_size",         # Sort by file size
            "api_name"          # Sort alphabetically by API name
        ]
        
        console.print("🔤 Configuring sortable attributes...")
        task = self.index.update_sortable_attributes(sortable_attributes)
        self.client.wait_for_task(task.task_uid if hasattr(task, 'task_uid') else task['taskUid'])
        console.print("[green]✓ Sortable attributes configured[/green]")
        
    def configure_ranking_rules(self):
        """Configure ranking rules for relevance"""
        ranking_rules = [
            "words",              # Number of query words found
            "typo",               # Fewer typos = higher rank
            "proximity",          # Words close together rank higher
            "attribute",          # Prioritize by searchable attribute order
            "sort",               # User-defined sort
            "exactness",          # Exact matches rank highest
            "api_name:asc"       # Alphabetical by API name as tiebreaker
        ]
        
        console.print("📊 Configuring ranking rules...")
        task = self.index.update_ranking_rules(ranking_rules)
        self.client.wait_for_task(task.task_uid if hasattr(task, 'task_uid') else task['taskUid'])
        console.print("[green]✓ Ranking rules configured[/green]")
        
    def configure_typo_tolerance(self):
        """Configure typo tolerance settings"""
        typo_tolerance = {
            "enabled": True,
            "minWordSizeForTypos": {
                "oneTypo": 4,    # Allow 1 typo for words >= 4 chars
                "twoTypos": 8    # Allow 2 typos for words >= 8 chars
            },
            "disableOnAttributes": ["api_name"],  # No typos on API names
            "disableOnWords": []
        }
        
        console.print("✏️ Configuring typo tolerance...")
        task = self.index.update_typo_tolerance(typo_tolerance)
        self.client.wait_for_task(task.task_uid if hasattr(task, 'task_uid') else task['taskUid'])
        console.print("[green]✓ Typo tolerance configured[/green]")
        
    def configure_synonyms(self):
        """Configure synonyms for common Apple terms"""
        synonyms = {
            # Framework variations
            "swiftui": ["swift ui"],
            "uikit": ["ui kit"],
            "coredata": ["core data"],
            "corelocation": ["core location"],
            "coregraphics": ["core graphics"],
            "coreanimation": ["core animation"],
            "corebluetooth": ["core bluetooth"],
            "arkit": ["ar kit"],
            "realitykit": ["reality kit"],
            "gamekit": ["game kit"],
            "healthkit": ["health kit"],
            "homekit": ["home kit"],
            "storekit": ["store kit"],
            "cloudkit": ["cloud kit"],
            "mapkit": ["map kit"],
            "webkit": ["web kit"],
            
            # Common abbreviations
            "vc": ["viewcontroller", "view controller"],
            "nav": ["navigation"],
            "bg": ["background"],
            "fg": ["foreground"],
            
            # Platform variations
            "ios": ["iphone os"],
            "macos": ["mac os", "osx", "os x"],
            "watchos": ["watch os"],
            "tvos": ["tv os", "apple tv"],
            "visionos": ["vision os", "vision pro"]
        }
        
        console.print("🔄 Configuring synonyms...")
        task = self.index.update_synonyms(synonyms)
        self.client.wait_for_task(task.task_uid if hasattr(task, 'task_uid') else task['taskUid'])
        console.print("[green]✓ Synonyms configured[/green]")
        
    def configure_stop_words(self):
        """Configure stop words (words to ignore in search)"""
        stop_words = [
            "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
            "of", "with", "by", "from", "up", "about", "into", "through", "during",
            "before", "after", "above", "below", "between", "under", "again",
            "further", "then", "once"
        ]
        
        console.print("🛑 Configuring stop words...")
        task = self.index.update_stop_words(stop_words)
        self.client.wait_for_task(task.task_uid if hasattr(task, 'task_uid') else task['taskUid'])
        console.print("[green]✓ Stop words configured[/green]")
        
    def configure_faceting(self):
        """Configure faceting settings"""
        # Faceting is configured as part of general settings
        settings = {
            "faceting": {
                "maxValuesPerFacet": 100  # Maximum number of facet values
            }
        }
        
        console.print("🎭 Configuring faceting...")
        task = self.index.update_settings(settings)
        self.client.wait_for_task(task.task_uid if hasattr(task, 'task_uid') else task['taskUid'])
        console.print("[green]✓ Faceting configured[/green]")
        
    def configure_pagination(self):
        """Configure pagination settings"""
        # Pagination is configured as part of general settings
        settings = {
            "pagination": {
                "maxTotalHits": 5000  # Maximum results to return
            }
        }
        
        console.print("📄 Configuring pagination...")
        task = self.index.update_settings(settings)
        self.client.wait_for_task(task.task_uid if hasattr(task, 'task_uid') else task['taskUid'])
        console.print("[green]✓ Pagination configured[/green]")
        
    def configure_all(self, show_before: bool = False):
        """Apply all configurations"""
        console.print("\n[bold]Configuring Meilisearch Index for Apple Documentation[/bold]\n")
        
        if show_before:
            console.print("[yellow]Current settings:[/yellow]")
            self.display_settings(self.get_current_settings())
            console.print()
        
        # Apply all configurations
        self.configure_searchable_attributes()
        self.configure_filterable_attributes()
        self.configure_sortable_attributes()
        self.configure_ranking_rules()
        self.configure_typo_tolerance()
        self.configure_synonyms()
        self.configure_stop_words()
        self.configure_faceting()
        self.configure_pagination()
        
        # Show final settings
        console.print("\n[green]All configurations applied successfully![/green]\n")
        console.print("[yellow]Final settings:[/yellow]")
        self.display_settings(self.get_current_settings())
        
    def display_settings(self, settings: Dict):
        """Display settings in a readable format"""
        # Create a summary table
        table = Table(title="Index Settings", show_header=True)
        table.add_column("Setting", style="cyan")
        table.add_column("Value", style="green")
        
        # Add key settings
        table.add_row("Searchable Attributes", str(len(settings.get('searchableAttributes', []))) + " configured")
        table.add_row("Filterable Attributes", str(len(settings.get('filterableAttributes', []))) + " configured")
        table.add_row("Sortable Attributes", str(len(settings.get('sortableAttributes', []))) + " configured")
        table.add_row("Ranking Rules", str(len(settings.get('rankingRules', []))) + " rules")
        table.add_row("Typo Tolerance", "Enabled" if settings.get('typoTolerance', {}).get('enabled', True) else "Disabled")
        table.add_row("Synonyms", str(len(settings.get('synonyms', {}))) + " configured")
        table.add_row("Stop Words", str(len(settings.get('stopWords', []))) + " words")
        
        console.print(table)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Configure Meilisearch index settings for Apple Developer documentation"
    )
    parser.add_argument(
        "--url",
        default=os.getenv("MEILI_HTTP_ADDR", "http://localhost:7700"),
        help="Meilisearch URL (default: http://localhost:7700 or MEILI_HTTP_ADDR env)"
    )
    parser.add_argument(
        "--api-key",
        default=os.getenv("MEILI_MASTER_KEY", ""),
        help="Meilisearch API key (default: MEILI_MASTER_KEY env)"
    )
    parser.add_argument(
        "--index",
        default="apple-docs",
        help="Index name to configure (default: apple-docs)"
    )
    parser.add_argument(
        "--show-before",
        action="store_true",
        help="Show current settings before applying new ones"
    )
    parser.add_argument(
        "--show-only",
        action="store_true",
        help="Only show current settings without making changes"
    )
    
    args = parser.parse_args()
    
    # Validate Meilisearch connection
    try:
        client = meilisearch.Client(args.url, args.api_key)
        health = client.health()
        console.print(f"[green]✓ Connected to Meilisearch at {args.url}[/green]")
    except Exception as e:
        console.print(f"[red]✗ Could not connect to Meilisearch at {args.url}: {e}[/red]")
        sys.exit(1)
    
    # Initialize configurator
    configurator = IndexConfigurator(
        meilisearch_url=args.url,
        api_key=args.api_key,
        index_name=args.index
    )
    
    if args.show_only:
        console.print("\n[yellow]Current index settings:[/yellow]")
        configurator.display_settings(configurator.get_current_settings())
    else:
        configurator.configure_all(show_before=args.show_before)


if __name__ == "__main__":
    main()