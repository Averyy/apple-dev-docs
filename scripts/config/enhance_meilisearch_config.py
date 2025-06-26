#!/usr/bin/env python3
"""
Enhanced Meilisearch Configuration for Better CamelCase Handling
This script improves search by:
1. Adding camelCase splitting
2. Creating synonyms for common patterns
3. Optimizing search parameters
"""

import os
import json
import meilisearch
from pathlib import Path
from typing import Dict, List, Set
import re
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()


class MeilisearchEnhancer:
    def __init__(self, host: str = "http://localhost:7700", api_key: str = "local_test_key"):
        self.client = meilisearch.Client(host, api_key)
        self.index = self.client.index("apple-docs")
        
    def split_camel_case(self, text: str) -> List[str]:
        """Split camelCase words into components"""
        # Handle acronyms and camelCase
        # URLSession -> URL Session
        # UIViewController -> UI View Controller
        # NSPersistentContainer -> NS Persistent Container
        parts = re.findall(r'[A-Z]+(?=[A-Z][a-z]|\b)|[A-Z][a-z]+|\d+|[a-z]+', text)
        return parts
    
    def generate_synonyms_from_apis(self, sample_size: int = 1000) -> Dict[str, List[str]]:
        """Generate synonyms from actual API names in the index"""
        console.print("[yellow]Analyzing API names to generate synonyms...[/yellow]")
        
        # Get sample documents to analyze API patterns
        results = self.index.search("", {"limit": sample_size, "attributesToRetrieve": ["api_name", "title"]})
        
        synonyms = {}
        api_names = set()
        
        # Collect unique API names
        for hit in results["hits"]:
            if api_name := hit.get("api_name"):
                api_names.add(api_name)
            if title := hit.get("title"):
                # Extract potential API names from titles
                if title[0].isupper() and not " " in title:
                    api_names.add(title)
        
        # Generate synonyms for each API name
        for api_name in api_names:
            if not api_name or len(api_name) < 3:
                continue
                
            # Split camelCase
            parts = self.split_camel_case(api_name)
            if len(parts) > 1:
                # Create variations
                lowercase = api_name.lower()
                separated = " ".join(parts).lower()
                separated_title = " ".join(parts)
                
                # Add all variations as synonyms
                variations = [
                    api_name,  # Original
                    lowercase,  # uiviewcontroller
                    separated,  # ui view controller
                    separated_title,  # UI View Controller
                ]
                
                # Remove duplicates and create synonym group
                unique_variations = list(dict.fromkeys(variations))
                if len(unique_variations) > 1:
                    synonyms[api_name] = unique_variations
        
        return synonyms
    
    def create_common_synonyms(self) -> Dict[str, List[str]]:
        """Create common framework and pattern synonyms"""
        return {
            # Framework abbreviations
            "ui": ["ui", "uikit", "user interface"],
            "ns": ["ns", "foundation", "nextstep"],
            "ca": ["ca", "core animation"],
            "cg": ["cg", "core graphics"],
            "ci": ["ci", "core image"],
            "av": ["av", "audio video", "avfoundation"],
            "ar": ["ar", "augmented reality", "arkit"],
            "ml": ["ml", "machine learning", "coreml"],
            "sk": ["sk", "storekit", "sprite kit", "scene kit"],
            
            # Common patterns
            "viewcontroller": ["view controller", "viewcontroller", "vc"],
            "tableview": ["table view", "tableview", "table"],
            "collectionview": ["collection view", "collectionview", "collection"],
            "navigationcontroller": ["navigation controller", "navigationcontroller", "nav controller"],
            "tabbarcontroller": ["tab bar controller", "tabbarcontroller", "tab controller"],
            
            # Common terms
            "async": ["async", "asynchronous", "await"],
            "sync": ["sync", "synchronous"],
            "delegate": ["delegate", "delegation"],
            "protocol": ["protocol", "protocols", "interface"],
            "closure": ["closure", "closures", "block", "blocks", "completion handler"],
            "notification": ["notification", "notifications", "push notification", "local notification"],
            "animation": ["animation", "animations", "animate", "transition"],
            "gesture": ["gesture", "gestures", "gesture recognizer", "tap", "swipe", "pinch"],
            
            # Common misspellings
            "persistant": ["persistent", "persistant"],
            "calender": ["calendar", "calender"],
            "seperator": ["separator", "seperator"],
        }
    
    def apply_enhanced_settings(self):
        """Apply enhanced search settings for better camelCase handling"""
        console.print("\n[yellow]Applying enhanced search settings...[/yellow]")
        
        # Current settings plus enhancements
        settings = {
            # Searchable attributes (no change)
            "searchableAttributes": [
                "api_name",
                "title", 
                "overview",
                "content_cleaned",
                "framework",
                "kind",
                "platforms"
            ],
            
            # Enhanced ranking rules
            "rankingRules": [
                "words",
                "typo",
                "proximity",
                "attribute",
                "sort",
                "exactness",
                "api_name:asc"
            ],
            
            # Typo tolerance settings
            "typoTolerance": {
                "enabled": True,
                "minWordSizeForTypos": {
                    "oneTypo": 4,
                    "twoTypos": 8
                },
                "disableOnWords": [],  # Remove api_name restriction
                "disableOnAttributes": []  # Allow typos on all attributes
            },
            
            # Separator tokens - CRITICAL for camelCase
            "separatorTokens": [
                # These characters will be treated as word separators
                " ", "-", "_", ".", "/", "\\", ":", ",", ";", 
                "!", "?", "(", ")", "[", "]", "{", "}", 
                "<", ">", "=", "+", "*", "&", "|", "^", "~",
                "'", '"', "`", "@", "#", "$", "%"
            ],
            
            # Non-separator tokens - Keep these together
            "nonSeparatorTokens": [
                # Keep version numbers together
                "1.0", "2.0", "3.0", "4.0", "5.0",
                # Keep common prefixes
                "UI", "NS", "CG", "CA", "CI", "AV", "AR", "ML", "SK"
            ],
            
            # Dictionary for custom tokenization
            "dictionary": [
                # This would allow custom word splitting but requires Meilisearch 1.3+
                "UIViewController=UI View Controller",
                "NSPredicate=NS Predicate",
                "URLSession=URL Session"
            ],
            
            # Faceting
            "faceting": {
                "maxValuesPerFacet": 200,
                "sortFacetValuesBy": {
                    "*": "alpha",
                    "platforms": "count"
                }
            },
            
            # Pagination
            "pagination": {
                "maxTotalHits": 10000
            }
        }
        
        # Apply settings
        task = self.index.update_settings(settings)
        # Wait longer for settings to apply (30 seconds)
        self.client.wait_for_task(task.task_uid, timeout_in_ms=30000)
        console.print("[green]✅ Enhanced settings applied![/green]")
    
    def apply_synonyms(self, limit_synonyms: int = 500):
        """Apply generated and common synonyms"""
        console.print("\n[yellow]Generating and applying synonyms...[/yellow]")
        
        # Get common synonyms
        synonyms = self.create_common_synonyms()
        
        # Generate API-based synonyms
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Analyzing API names...", total=None)
            api_synonyms = self.generate_synonyms_from_apis(sample_size=2000)
            progress.update(task, completed=True)
        
        # Merge synonyms (limit to prevent performance issues)
        all_synonyms = {**synonyms}
        api_count = 0
        for api_name, variations in api_synonyms.items():
            if api_count >= limit_synonyms:
                break
            all_synonyms[api_name] = variations
            api_count += 1
        
        # Apply synonyms
        console.print(f"[blue]Applying {len(all_synonyms)} synonym groups...[/blue]")
        task = self.index.update_synonyms(all_synonyms)
        self.client.wait_for_task(task.task_uid)
        console.print("[green]✅ Synonyms applied![/green]")
        
        # Show examples
        console.print("\n[cyan]Example synonyms created:[/cyan]")
        examples = list(all_synonyms.items())[:10]
        for key, values in examples:
            console.print(f"  {key}: {', '.join(values)}")
    
    def optimize_for_camelcase(self):
        """Apply all optimizations for better camelCase search"""
        console.print("[bold green]Enhancing Meilisearch for CamelCase Search[/bold green]\n")
        
        # 1. Apply enhanced settings
        self.apply_enhanced_settings()
        
        # 2. Apply synonyms
        self.apply_synonyms()
        
        # 3. Additional index-specific settings
        console.print("\n[yellow]Applying additional optimizations...[/yellow]")
        
        # Set distinct attribute (optional)
        task = self.index.update_distinct_attribute("file_path")
        self.client.wait_for_task(task.task_uid)
        
        # Update displayed attributes to include all fields
        task = self.index.update_displayed_attributes(["*"])
        self.client.wait_for_task(task.task_uid)
        
        console.print("[green]✅ All optimizations complete![/green]")
    
    def test_enhanced_search(self):
        """Test the enhanced search capabilities"""
        console.print("\n[bold cyan]Testing Enhanced Search[/bold cyan]\n")
        
        test_queries = [
            "ui view controller",  # Separated
            "uiviewcontroller",     # Lowercase
            "persistent container", # Partial
            "async image",         # Two words
            "sk store product view controller",  # Long separation
        ]
        
        for query in test_queries:
            results = self.index.search(query, {"limit": 3})
            console.print(f"[yellow]Query: '{query}'[/yellow]")
            console.print(f"Found {results['estimatedTotalHits']} results")
            
            for i, hit in enumerate(results["hits"][:3], 1):
                api_name = hit.get("api_name", "N/A")
                console.print(f"  {i}. {api_name}")
            console.print()


def main():
    """Enhance Meilisearch configuration"""
    enhancer = MeilisearchEnhancer()
    
    # Apply all enhancements
    enhancer.optimize_for_camelcase()
    
    # Test the improvements
    enhancer.test_enhanced_search()
    
    console.print("\n[bold green]Meilisearch has been enhanced for better camelCase searching![/bold green]")
    console.print("\nKey improvements:")
    console.print("• CamelCase words are now split and searchable")
    console.print("• Common variations are linked via synonyms")
    console.print("• Typo tolerance is improved")
    console.print("• Search should now find 'UIViewController' when searching 'ui view controller'")


if __name__ == "__main__":
    main()