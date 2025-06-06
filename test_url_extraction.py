#!/usr/bin/env python3
"""Test URL extraction from markdown files."""

from pathlib import Path

def extract_url_from_file(file_path):
    """Extract Apple Developer URL from markdown file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Look for the last occurrence of the Apple Developer URL pattern
        lines = content.split('\n')
        for line in reversed(lines):
            if '*[View on Apple Developer](' in line and line.endswith(')*'):
                # Extract URL between ]( and )*
                start = line.find('](') + 2
                end = line.rfind(')*')
                if start > 1 and end > start:
                    url = line[start:end]
                    if url.startswith('https://developer.apple.com/documentation/'):
                        return url
        
        return None
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# Test files
test_files = [
    'documentation/StoreKit/skstorereviewcontroller/requestreview.md',
    'documentation/StoreKit/skpaymentqueue/showpriceconsentifneeded.md',
    'documentation/StoreKit/promoting-in-app-purchases.md',
    'documentation/Swift/keyedencodingcontainerprotocol/encode-forkey-389ei.md'
]

print("Testing URL extraction on various file patterns:")
print("=" * 80)

for file_path in test_files:
    path = Path(file_path)
    if path.exists():
        url = extract_url_from_file(path)
        if url:
            print(f"\n✅ File: {path.name}")
            print(f"   URL: {url}")
        else:
            print(f"\n❌ File: {path.name} - No URL found")
    else:
        print(f"\n⚠️  File not found: {file_path}")

# Check for Note duplication in one of the files
print("\n\nChecking for Note duplication:")
print("=" * 80)

test_file = Path('documentation/StoreKit/skstorereviewcontroller/requestreview.md')
if test_file.exists():
    content = test_file.read_text()
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if '> **Note**:' in line:
            print(f"\nFound Note at line {i+1}: {line[:80]}...")
            # Check next few lines
            for j in range(i+1, min(i+5, len(lines))):
                if lines[j].strip():
                    print(f"Line {j+1}: {lines[j][:80]}...")
                    break