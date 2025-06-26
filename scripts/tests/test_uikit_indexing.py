#!/usr/bin/env python3
"""Test script to investigate UIKit indexing issue."""

import os
import sys
from pathlib import Path
from collections import defaultdict

# Add parent directory to path to import local modules
sys.path.append(str(Path(__file__).parent.parent))

from scripts.metadata_extractor import MetadataExtractor
from scripts.document_processor import DocumentProcessor

def main():
    # Initialize processors
    metadata_extractor = MetadataExtractor()
    document_processor = DocumentProcessor()
    
    # Track statistics
    framework_counts = defaultdict(int)
    errors = []
    uikit_files = []
    
    # Find all UIKit markdown files
    uikit_path = Path("../documentation/UIKit")
    all_files = list(uikit_path.rglob("*.md"))
    
    print(f"Found {len(all_files)} total .md files in UIKit directory\n")
    
    # Sample some files to check metadata extraction
    sample_size = min(100, len(all_files))
    print(f"Sampling {sample_size} files to check metadata extraction...\n")
    
    for i, file_path in enumerate(all_files[:sample_size]):
        try:
            # Read content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract metadata
            metadata = metadata_extractor.extract_metadata(content, str(file_path))
            framework = metadata.get('framework', 'Unknown')
            framework_counts[framework] += 1
            
            if framework == 'UIKit':
                uikit_files.append(str(file_path))
            
            # Show first few examples
            if i < 5:
                print(f"File: {file_path}")
                print(f"  Framework: {framework}")
                print(f"  ID: {metadata.get('id', 'N/A')}")
                print(f"  Title: {metadata.get('title', 'N/A')}")
                print()
                
        except Exception as e:
            errors.append((str(file_path), str(e)))
    
    # Summary
    print("\nFramework extraction summary:")
    for framework, count in sorted(framework_counts.items()):
        print(f"  {framework}: {count} files")
    
    if errors:
        print(f"\nErrors encountered: {len(errors)}")
        for file_path, error in errors[:5]:
            print(f"  {file_path}: {error}")
    
    # Check full directory structure
    print("\n\nChecking directory structure depth...")
    depth_counts = defaultdict(int)
    for file_path in all_files:
        rel_path = file_path.relative_to(Path("../documentation"))
        depth = len(rel_path.parts) - 1  # -1 to exclude the filename
        depth_counts[depth] += 1
    
    print("Files by directory depth:")
    for depth, count in sorted(depth_counts.items()):
        print(f"  Depth {depth}: {count} files")
    
    # Show some deep paths
    deep_files = [f for f in all_files if len(f.relative_to(Path("../documentation")).parts) > 3]
    if deep_files:
        print(f"\nExample deep paths ({len(deep_files)} total):")
        for f in deep_files[:5]:
            rel_path = f.relative_to(Path("../documentation"))
            print(f"  {rel_path}")
            # Check metadata for deep file
            try:
                with open(f, 'r', encoding='utf-8') as file:
                    content = file.read()
                metadata = metadata_extractor.extract_metadata(content, str(f))
                print(f"    Framework: {metadata.get('framework', 'Unknown')}")
                print(f"    ID: {metadata.get('id', 'N/A')}")
            except Exception as e:
                print(f"    Error: {e}")

if __name__ == "__main__":
    main()