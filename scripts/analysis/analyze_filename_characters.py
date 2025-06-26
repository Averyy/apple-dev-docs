#!/usr/bin/env python3
"""Analyze all characters used in markdown filenames."""

from pathlib import Path
from collections import Counter
import re

def analyze_filenames():
    """Find all special characters in markdown filenames."""
    docs_path = Path("../documentation")
    
    # Track all characters
    all_chars = Counter()
    special_chars = Counter()
    
    # Track filenames with special chars
    special_examples = {}
    
    # Get all markdown files
    md_files = list(docs_path.rglob("*.md"))
    
    print(f"Analyzing {len(md_files):,} markdown files...\n")
    
    for file_path in md_files:
        # Get relative path from documentation folder
        rel_path = file_path.relative_to(docs_path)
        path_str = str(rel_path)
        
        # Count all characters
        for char in path_str:
            all_chars[char] += 1
            
            # Check if it's a special character (not alphanumeric, -, _, or /)
            if not re.match(r'[a-zA-Z0-9/_-]', char):
                special_chars[char] += 1
                
                # Save example
                if char not in special_examples:
                    special_examples[char] = []
                if len(special_examples[char]) < 3:
                    special_examples[char].append(path_str)
    
    # Print results
    print("Special characters found in filenames:")
    print("(Note: Meilisearch only allows: a-z A-Z 0-9 - _)\n")
    
    for char, count in special_chars.most_common():
        print(f"'{char}' : {count:6,} occurrences")
        if char in special_examples:
            print(f"  Examples:")
            for example in special_examples[char][:2]:
                print(f"    {example}")
        print()
    
    # Check for specific problematic characters
    print("\nChecking for known problematic characters:")
    problematic = ['.', ' ', '(', ')', '+', ':', ',', "'", '"', '&', '!', '?', '@', '#', '$', '%', '^', '*', '=', '{', '}', '[', ']', '|', '\\', ';', '<', '>', '~', '`']
    
    found_problematic = []
    for char in problematic:
        if char in special_chars:
            found_problematic.append((char, special_chars[char]))
    
    if found_problematic:
        print("Found these problematic characters that need handling:")
        for char, count in found_problematic:
            print(f"  '{char}': {count:,} occurrences")
    else:
        print("No additional problematic characters found!")
    
    # Show character frequency
    print("\n\nAll characters by frequency:")
    for char, count in all_chars.most_common(20):
        if char == '\n':
            char_display = '\\n'
        elif char == ' ':
            char_display = 'space'
        else:
            char_display = char
        print(f"  '{char_display}': {count:,}")

if __name__ == "__main__":
    analyze_filenames()