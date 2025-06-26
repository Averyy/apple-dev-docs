#!/usr/bin/env python3
"""
Simple Meilisearch Enhancement for CamelCase
Focuses on the most impactful improvements
"""

import meilisearch
from rich.console import Console

console = Console()


def enhance_meilisearch():
    """Apply simple but effective enhancements"""
    client = meilisearch.Client("http://localhost:7700", "local_test_key")
    index = client.index("apple-docs")
    
    console.print("[yellow]Enhancing Meilisearch for better search...[/yellow]\n")
    
    # 1. Add key synonyms for camelCase patterns
    console.print("1. Adding synonyms for common patterns...")
    
    synonyms = {
        # UIKit patterns
        "uiviewcontroller": ["ui view controller", "uiviewcontroller", "UIViewController", "view controller"],
        "uitableview": ["ui table view", "uitableview", "UITableView", "table view"],
        "uicollectionview": ["ui collection view", "uicollectionview", "UICollectionView", "collection view"],
        "uinavigationcontroller": ["ui navigation controller", "uinavigationcontroller", "UINavigationController", "navigation controller"],
        
        # Foundation patterns  
        "nspredicate": ["ns predicate", "nspredicate", "NSPredicate", "predicate"],
        "nspersistentcontainer": ["ns persistent container", "nspersistentcontainer", "NSPersistentContainer", "persistent container"],
        "nsurlsession": ["ns url session", "nsurlsession", "NSURLSession", "url session", "URLSession", "urlsession"],
        
        # SwiftUI patterns
        "asyncimage": ["async image", "asyncimage", "AsyncImage"],
        "navigationstack": ["navigation stack", "navigationstack", "NavigationStack"],
        "geometryreader": ["geometry reader", "geometryreader", "GeometryReader"],
        
        # StoreKit patterns
        "skstoreproductviewcontroller": ["sk store product view controller", "skstoreproductviewcontroller", "SKStoreProductViewController", "store product view controller"],
        
        # Common abbreviations
        "vc": ["view controller", "viewcontroller", "vc"],
        "tv": ["table view", "tableview", "tv"],
        "cv": ["collection view", "collectionview", "cv"],
        
        # Framework abbreviations
        "ui": ["ui", "uikit", "user interface"],
        "ns": ["ns", "foundation"],
        "sk": ["sk", "storekit", "store kit"],
        "av": ["av", "avfoundation", "audio video"],
        "ar": ["ar", "arkit", "augmented reality"],
    }
    
    task = index.update_synonyms(synonyms)
    client.wait_for_task(task.task_uid, timeout_in_ms=30000)
    console.print("[green]✅ Synonyms added![/green]\n")
    
    # 2. Update settings for better matching
    console.print("2. Updating search settings...")
    
    settings = {
        # Make sure typo tolerance is fully enabled
        "typoTolerance": {
            "enabled": True,
            "minWordSizeForTypos": {
                "oneTypo": 3,  # More aggressive
                "twoTypos": 6
            },
            "disableOnWords": [],
            "disableOnAttributes": []
        }
    }
    
    task = index.update_settings(settings)
    client.wait_for_task(task.task_uid, timeout_in_ms=30000)
    console.print("[green]✅ Settings updated![/green]\n")
    
    # 3. Test the improvements
    console.print("3. Testing enhanced search...\n")
    
    test_queries = [
        ("ui view controller", "UIViewController"),
        ("async image", "AsyncImage"),
        ("persistent container", "NSPersistentContainer"),
        ("sk store product view controller", "SKStoreProductViewController"),
    ]
    
    for query, expected in test_queries:
        results = index.search(query, {"limit": 3})
        found = False
        
        for hit in results["hits"]:
            if expected.lower() in str(hit).lower():
                found = True
                break
        
        status = "✅" if found else "❌"
        console.print(f"{status} '{query}' → {expected}")
    
    console.print("\n[bold green]Meilisearch enhanced successfully![/bold green]")


if __name__ == "__main__":
    enhance_meilisearch()