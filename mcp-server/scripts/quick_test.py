#!/usr/bin/env python3
"""
Quick test with just a few files
"""
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from build_index import VectorIndexBuilder
from server.config import DOCS_PATH


def quick_test():
    """Test with just 10 files from SwiftUI"""
    print("\nQuick Index Test")
    print("================\n")
    
    # Find SwiftUI directory
    swiftui_dir = DOCS_PATH / "SwiftUI"
    if not swiftui_dir.exists():
        print(f"❌ SwiftUI directory not found at {swiftui_dir}")
        return
    
    # Get first 10 markdown files
    md_files = list(swiftui_dir.glob("*.md"))[:10]
    print(f"Found {len(md_files)} files to index from SwiftUI")
    
    # Create a temp directory with just these files
    temp_dir = Path("temp_test")
    temp_dir.mkdir(exist_ok=True)
    
    temp_swiftui = temp_dir / "SwiftUI"
    temp_swiftui.mkdir(exist_ok=True)
    
    # Copy files
    for f in md_files:
        content = f.read_text()
        (temp_swiftui / f.name).write_text(content)
        print(f"  - {f.name}")
    
    # Index just these files
    print(f"\nIndexing {len(md_files)} files...")
    
    builder = VectorIndexBuilder(docs_path=temp_dir)
    builder.build_index(force_rebuild=True)
    builder.verify_index()
    
    # Clean up
    import shutil
    shutil.rmtree(temp_dir)
    
    print("\n✅ Quick test complete!")


if __name__ == "__main__":
    quick_test()