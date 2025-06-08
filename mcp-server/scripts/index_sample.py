#!/usr/bin/env python3
"""
Index a sample of frameworks for testing
"""
import os
import sys
import shutil
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from server.config import DOCS_PATH
from build_index import VectorIndexBuilder


def create_sample_index():
    """Create index with just a few frameworks for testing"""
    print("\nCreating Sample Index")
    print("====================\n")
    
    # Find some small frameworks to test with
    frameworks = []
    target_frameworks = ["SwiftUI", "Foundation", "UIKit"]  # Priority frameworks
    
    for framework_dir in DOCS_PATH.iterdir():
        if framework_dir.is_dir() and not framework_dir.name.startswith('.'):
            # Check if it's one of our target frameworks
            if framework_dir.name in target_frameworks:
                frameworks.insert(0, framework_dir)  # Add to front
            else:
                frameworks.append(framework_dir)
    
    # Limit to first 3 frameworks
    sample_frameworks = frameworks[:3]
    
    print(f"Found {len(frameworks)} total frameworks")
    print(f"Indexing sample of {len(sample_frameworks)} frameworks:")
    
    total_files = 0
    for fw in sample_frameworks:
        file_count = len(list(fw.glob("*.md")))
        total_files += file_count
        print(f"  - {fw.name}: {file_count} files")
    
    print(f"\nTotal files to index: {total_files}")
    
    # Temporarily limit the docs path to just these frameworks
    original_docs_path = os.environ.get('DOCS_PATH', '../documentation')
    
    # Create a temporary directory with symlinks to sample frameworks
    temp_docs = Path("temp_sample_docs")
    temp_docs.mkdir(exist_ok=True)
    
    for fw in sample_frameworks:
        target = temp_docs / fw.name
        if not target.exists():
            target.symlink_to(fw.resolve())
    
    # Update environment to point to temp docs
    os.environ['DOCS_PATH'] = str(temp_docs)
    
    try:
        # Run indexer with temp path directly
        from build_index import VectorIndexBuilder
        builder = VectorIndexBuilder(docs_path=temp_docs)
        builder.build_index(force_rebuild=True)
        builder.verify_index()
        
    finally:
        # Restore original path
        os.environ['DOCS_PATH'] = original_docs_path
        
        # Clean up temp directory
        shutil.rmtree(temp_docs, ignore_errors=True)
    
    print("\n✅ Sample indexing complete!")
    print("   You can now test the full indexing with:")
    print("   python scripts/build_index.py")


if __name__ == "__main__":
    create_sample_index()