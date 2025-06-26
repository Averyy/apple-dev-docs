#!/usr/bin/env python3
"""Find which documents are missing from Meilisearch index."""

import os
import sys
import json
from pathlib import Path
from collections import defaultdict
import meilisearch
from rich.console import Console
from rich.progress import Progress
from dotenv import load_dotenv

load_dotenv()

console = Console()

def find_missing_documents():
    """Compare hash file with Meilisearch to find missing documents."""
    hash_file = Path("../.hashes/meilisearch_hashes.json")
    
    # Load hash file
    console.print("📋 Loading hash file...")
    with open(hash_file, 'r') as f:
        hashes = json.load(f)
    
    console.print(f"  Found {len(hashes)} files in hash file")
    
    # Connect to Meilisearch
    client = meilisearch.Client(
        os.getenv('MEILI_HTTP_ADDR', 'http://localhost:7700'),
        os.getenv('MEILI_MASTER_KEY', '')
    )
    
    index = client.index('apple-docs')
    
    # Get document count by framework
    console.print("\n🔍 Checking document counts by framework...")
    
    # Group files by framework from hash file
    framework_files = defaultdict(list)
    for file_path in hashes.keys():
        parts = Path(file_path).parts
        if parts:
            framework = parts[0]
            framework_files[framework].append(file_path)
    
    missing_by_framework = {}
    
    # Check each framework
    with Progress() as progress:
        task = progress.add_task("Checking frameworks...", total=len(framework_files))
        
        for framework, files in framework_files.items():
            # Get count from Meilisearch
            try:
                result = index.search('', {
                    'filter': f'framework = "{framework}"',
                    'limit': 0
                })
                indexed_count = result.get('estimatedTotalHits', 0)
                expected_count = len(files)
                
                if indexed_count < expected_count:
                    missing_by_framework[framework] = {
                        'expected': expected_count,
                        'indexed': indexed_count,
                        'missing': expected_count - indexed_count
                    }
            except Exception as e:
                console.print(f"[red]Error checking {framework}: {e}[/red]")
            
            progress.update(task, advance=1)
    
    # Print results
    console.print("\n📊 Missing Documents by Framework:")
    total_missing = 0
    
    for framework, counts in sorted(missing_by_framework.items(), key=lambda x: x[1]['missing'], reverse=True):
        if counts['missing'] > 0:
            console.print(f"  {framework:20s}: {counts['missing']:6,} missing (expected {counts['expected']:,}, found {counts['indexed']:,})")
            total_missing += counts['missing']
    
    console.print(f"\n❌ Total missing documents: {total_missing:,}")
    
    # Sample check for specific frameworks
    console.print("\n🔬 Sampling missing documents...")
    
    # Check UIKit specifically
    if 'UIKit' in framework_files:
        console.print("\nUIKit deep dive:")
        # Get a sample of UIKit files
        uikit_files = framework_files['UIKit'][:10]
        
        for file_path in uikit_files:
            # Generate the expected document ID
            parts = Path(file_path).parts
            doc_id = "_".join(parts).lower().replace("-", "_").replace(" ", "_").replace(".md", "")
            
            # Try to get this specific document
            try:
                result = index.search('', {
                    'filter': f'id = "{doc_id}"',
                    'limit': 1
                })
                
                if result.get('estimatedTotalHits', 0) == 0:
                    console.print(f"  ❌ Missing: {file_path} (ID: {doc_id})")
                else:
                    console.print(f"  ✅ Found: {file_path}")
            except Exception as e:
                console.print(f"  ⚠️  Error checking {file_path}: {e}")
    
    # Check for pattern in missing documents
    console.print("\n🔍 Checking for patterns in file paths...")
    
    # Sample some missing documents from different frameworks
    for framework, counts in list(missing_by_framework.items())[:5]:
        if counts['missing'] > 0:
            console.print(f"\n{framework} file path samples:")
            sample_files = framework_files[framework][:5]
            for f in sample_files:
                console.print(f"  {f}")
                # Check path depth
                depth = len(Path(f).parts)
                if depth > 4:
                    console.print(f"    ⚠️  Deep path: {depth} levels")

if __name__ == "__main__":
    find_missing_documents()