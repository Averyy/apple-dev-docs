#!/usr/bin/env python3
"""
Validate that documentation is ready for indexing
"""
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from server.config import DOCS_PATH
from server.logger import get_logger

logger = get_logger(__name__)


def validate_documentation():
    """Validate the documentation directory structure"""
    print("\nValidating Documentation Structure")
    print("==================================\n")
    
    # Check if docs directory exists
    if not DOCS_PATH.exists():
        print(f"✗ Documentation directory not found: {DOCS_PATH}")
        return False
    
    print(f"✓ Documentation directory found: {DOCS_PATH}")
    
    # Count frameworks
    frameworks = [d for d in DOCS_PATH.iterdir() if d.is_dir() and not d.name.startswith('.')]
    print(f"✓ Found {len(frameworks)} frameworks")
    
    # Sample some frameworks
    sample_frameworks = sorted(frameworks[:5], key=lambda x: x.name)
    print(f"\nSample frameworks:")
    
    total_files = 0
    for framework in sample_frameworks:
        md_files = list(framework.glob("*.md"))
        total_files += len(md_files)
        print(f"  - {framework.name}: {len(md_files)} files")
    
    # Check for some expected frameworks
    expected = ["SwiftUI", "UIKit", "Foundation"]
    found_expected = []
    
    for exp in expected:
        if any(f.name.lower() == exp.lower() for f in frameworks):
            found_expected.append(exp)
    
    print(f"\nCore frameworks check:")
    for exp in expected:
        if exp in found_expected:
            print(f"  ✓ {exp}")
        else:
            print(f"  ✗ {exp} (not found)")
    
    # Estimate total file count
    print(f"\nEstimating total documentation files...")
    
    # Quick sample to estimate
    sample_size = min(10, len(frameworks))
    sample_count = 0
    
    for framework in frameworks[:sample_size]:
        sample_count += len(list(framework.glob("*.md")))
    
    estimated_total = (sample_count / sample_size) * len(frameworks)
    
    print(f"✓ Estimated ~{int(estimated_total):,} markdown files across all frameworks")
    
    # Check file readability
    print(f"\nChecking file readability...")
    test_file = None
    
    for framework in frameworks:
        md_files = list(framework.glob("*.md"))
        if md_files:
            test_file = md_files[0]
            break
    
    if test_file:
        try:
            content = test_file.read_text()
            print(f"✓ Successfully read test file: {test_file.name}")
            print(f"  Size: {len(content):,} characters")
            
            # Check for expected content
            has_framework = "Framework:" in content or "**Framework**:" in content
            has_content = len(content) > 100
            
            if has_framework and has_content:
                print(f"✓ File contains expected markdown structure")
            else:
                print(f"⚠ File may have unexpected structure")
                
        except Exception as e:
            print(f"✗ Error reading file: {e}")
            return False
    
    print(f"\n{'='*40}")
    print(f"✓ Documentation is ready for indexing!")
    print(f"  Frameworks: {len(frameworks)}")
    print(f"  Estimated files: ~{int(estimated_total):,}")
    
    return True


if __name__ == "__main__":
    if validate_documentation():
        sys.exit(0)
    else:
        sys.exit(1)