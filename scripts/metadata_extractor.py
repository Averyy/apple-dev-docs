#!/usr/bin/env python3
"""Extract metadata from Apple Developer documentation markdown files."""

import re
import os
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
import yaml
import argparse
from datetime import datetime

class MetadataExtractor:
    """Extract structured metadata from Apple documentation markdown files."""
    
    def __init__(self):
        # Common platform mappings
        self.platform_mappings = {
            "ios": "iOS",
            "macos": "macOS", 
            "mac os": "macOS",
            "mac os x": "macOS",
            "osx": "macOS",
            "os x": "macOS",
            "tvos": "tvOS",
            "watchos": "watchOS",
            "visionos": "visionOS",
            "vision os": "visionOS",
            "catalyst": "Mac Catalyst",
            "mac catalyst": "Mac Catalyst",
            "ipad": "iPadOS",
            "ipados": "iPadOS"
        }
        
        # Framework name normalization
        self.framework_aliases = {
            "swiftui": "SwiftUI",
            "swift ui": "SwiftUI",
            "uikit": "UIKit", 
            "ui kit": "UIKit",
            "appkit": "AppKit",
            "app kit": "AppKit",
            "storekit": "StoreKit",
            "store kit": "StoreKit",
            "spritekit": "SpriteKit",
            "sprite kit": "SpriteKit",
            "scenekit": "SceneKit",
            "scene kit": "SceneKit",
            "coredata": "CoreData",
            "core data": "CoreData",
            "corelocation": "CoreLocation",
            "core location": "CoreLocation",
            "avfoundation": "AVFoundation",
            "av foundation": "AVFoundation",
            "foundation": "Foundation",
            "combine": "Combine",
            "metal": "Metal",
            "cloudkit": "CloudKit",
            "cloud kit": "CloudKit",
            "healthkit": "HealthKit",
            "health kit": "HealthKit",
            "gamekit": "GameKit",
            "game kit": "GameKit",
            "mapkit": "MapKit",
            "map kit": "MapKit",
            "webkit": "WebKit",
            "web kit": "WebKit",
            "realitykit": "RealityKit",
            "reality kit": "RealityKit",
            "arkit": "ARKit",
            "ar kit": "ARKit"
        }
        
    def extract_metadata(self, content: str, file_path: str) -> Dict[str, Any]:
        """Extract all metadata from a documentation file.
        
        Args:
            content: The markdown content
            file_path: Path to the file for context
            
        Returns:
            Dictionary containing extracted metadata
        """
        metadata = {
            "id": self.generate_document_id(file_path),
            "file_path": self.normalize_file_path(file_path),
            "framework": self.extract_framework(content, file_path),
            "api_name": self.extract_api_name(content, file_path),
            "title": self.extract_title(content),
            "platforms": self.extract_platforms(content),
            "kind": self.extract_kind(content),
            "overview": self.extract_overview(content),
            "is_framework_main": self.is_framework_main_page(content, file_path),
            "last_modified": self.get_file_modified_time(file_path),
            "url": self.generate_url(file_path),
            "file_size": os.path.getsize(file_path) if os.path.exists(file_path) else 0
        }
        
        # Clean up None values
        return {k: v for k, v in metadata.items() if v is not None}
    
    def normalize_file_path(self, file_path: str) -> str:
        """Convert absolute file path to relative path starting from documentation/"""
        path = Path(file_path)
        parts = list(path.parts)
        
        # Find the documentation directory and return path from there
        if "documentation" in parts:
            doc_index = parts.index("documentation")
            relative_parts = parts[doc_index:]  # Include 'documentation' itself
            return "/".join(relative_parts)
        
        # Fallback: if no documentation found, return just the filename
        return path.name
    
    def generate_document_id(self, file_path: str) -> str:
        """Generate a unique document ID from file path."""
        # Convert to Path object
        path = Path(file_path)
        
        # Find the documentation root directory
        parts = list(path.parts)
        doc_index = -1
        for i, part in enumerate(parts):
            if part == "documentation":
                doc_index = i
                break
        
        # If we found 'documentation', use everything after it
        if doc_index >= 0:
            relevant_parts = parts[doc_index + 1:]  # Skip 'documentation' itself
        else:
            # Fallback: use the whole path
            relevant_parts = parts
        
        # Remove .md extension from last part
        if relevant_parts and relevant_parts[-1].endswith('.md'):
            relevant_parts[-1] = relevant_parts[-1][:-3]
            
        # Join with underscores and normalize
        # This preserves the full path structure: framework/class/method
        # Replace all invalid characters with underscores (Meilisearch only allows alphanumeric, hyphens, underscores)
        doc_id = "_".join(relevant_parts).lower()
        # Replace any character that's not alphanumeric, hyphen, or underscore
        # This handles dots from paths like "swift.struct/method.md"
        doc_id = re.sub(r'[^a-z0-9_-]', '_', doc_id)
        return doc_id
    
    def extract_framework(self, content: str, file_path: str) -> str:
        """Extract framework name from content or path."""
        # Try to get from file path first
        path_parts = Path(file_path).parts
        
        # Look for documentation/FrameworkName pattern
        if "documentation" in path_parts:
            idx = path_parts.index("documentation")
            if idx + 1 < len(path_parts):
                framework = path_parts[idx + 1]
                # Normalize framework name
                return self.normalize_framework_name(framework)
        
        # Try to extract from content
        # Look for "Framework: Name" pattern
        framework_match = re.search(r'(?:Framework|Module):\s*(\w+)', content, re.IGNORECASE)
        if framework_match:
            return self.normalize_framework_name(framework_match.group(1))
        
        # Look for imports or module declarations
        import_match = re.search(r'import\s+(\w+)', content)
        if import_match:
            return self.normalize_framework_name(import_match.group(1))
        
        # Default to first directory under documentation
        if len(path_parts) > 1:
            return self.normalize_framework_name(path_parts[1])
        
        return "Unknown"
    
    def normalize_framework_name(self, name: str) -> str:
        """Normalize framework name to consistent casing."""
        name_lower = name.lower()
        return self.framework_aliases.get(name_lower, name)
    
    def extract_api_name(self, content: str, file_path: str) -> str:
        """Extract API/class/protocol name."""
        # Try to extract from content first
        # Look for class/struct/protocol declarations
        api_patterns = [
            r'(?:class|struct|protocol|enum|actor)\s+(\w+)',
            r'#\s*(?:class|struct|protocol|enum|type|Class|Type)\s+(\w+)',
            r'^#\s+(\w+)\s*$',  # First level header
        ]
        
        for pattern in api_patterns:
            match = re.search(pattern, content, re.MULTILINE)
            if match:
                return match.group(1)
        
        # Extract from title
        title = self.extract_title(content)
        if title:
            # Remove common suffixes
            for suffix in [" Class", " Protocol", " Structure", " Enumeration", " Type"]:
                if title.endswith(suffix):
                    return title[:-len(suffix)]
            # Return first word of title if it looks like an API name
            first_word = title.split()[0] if title else ""
            if first_word and first_word[0].isupper():
                return first_word
        
        # Get from filename as last resort
        filename = Path(file_path).stem
        if filename and filename != "index":
            return filename
        
        return "Unknown"
    
    def extract_title(self, content: str) -> str:
        """Extract document title."""
        # Look for first level header
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
        
        # Look for title in metadata
        metadata_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
        if metadata_match:
            return metadata_match.group(1).strip()
        
        return ""
    
    def extract_platforms(self, content: str) -> List[str]:
        """Extract supported platforms."""
        platforms = set()
        
        # Look for platform badges or lists
        platform_patterns = [
            r'(?:Platforms?|Available on|Supported on):\s*([^\n]+)',
            r'!\[.*?\]\(.*?badge.*?(ios|macos|tvos|watchos|visionos|catalyst).*?\)',
            r'`(?:iOS|macOS|tvOS|watchOS|visionOS|Mac Catalyst)(?:\s+[\d.]+)?`',
            r'@available\s*\(([^)]+)\)',
        ]
        
        for pattern in platform_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    match = match[0]
                
                # Parse platform list
                for part in re.split(r'[,;|]', match):
                    part = part.strip().lower()
                    for key, value in self.platform_mappings.items():
                        if key in part:
                            platforms.add(value)
        
        # If no platforms found, check for common indicators
        content_lower = content.lower()
        for key, value in self.platform_mappings.items():
            if key in content_lower:
                platforms.add(value)
        
        return sorted(list(platforms))
    
    def extract_kind(self, content: str) -> str:
        """Extract the kind of API (class, protocol, struct, etc.)."""
        kind_patterns = [
            (r'(?:^|\s)class\s+\w+', 'class'),
            (r'(?:^|\s)struct\s+\w+', 'struct'),
            (r'(?:^|\s)protocol\s+\w+', 'protocol'),
            (r'(?:^|\s)enum\s+\w+', 'enum'),
            (r'(?:^|\s)actor\s+\w+', 'actor'),
            (r'(?:^|\s)typealias\s+\w+', 'typealias'),
            (r'(?:^|\s)extension\s+\w+', 'extension'),
            (r'#\s*(?:Class|Structure|Protocol|Enumeration|Type)\s+\w+', 'type'),
        ]
        
        for pattern, kind in kind_patterns:
            if re.search(pattern, content, re.IGNORECASE | re.MULTILINE):
                return kind
        
        # Check for function/method
        if re.search(r'(?:^|\s)func\s+\w+', content):
            return 'function'
        
        # Check for property
        if re.search(r'(?:^|\s)(?:var|let)\s+\w+', content):
            return 'property'
        
        return 'unknown'
    
    def extract_overview(self, content: str) -> str:
        """Extract overview or description."""
        # Look for Overview section
        overview_match = re.search(
            r'(?:##?\s*(?:Overview|Description|Summary|Introduction))\s*\n+([^\n#]+(?:\n[^\n#]+)*)',
            content,
            re.IGNORECASE | re.MULTILINE
        )
        
        if overview_match:
            overview = overview_match.group(1).strip()
            # Clean up the overview
            overview = re.sub(r'\s+', ' ', overview)
            return overview[:500]  # Limit to 500 chars
        
        # Try to get first non-empty paragraph after title
        lines = content.split('\n')
        found_title = False
        overview_lines = []
        skip_empty = True
        
        for i, line in enumerate(lines):
            # Found title
            if line.startswith('#') and not found_title:
                found_title = True
                continue
            
            # After title, collect non-empty lines
            if found_title:
                line_stripped = line.strip()
                
                # Skip initial empty lines
                if skip_empty and not line_stripped:
                    continue
                elif line_stripped:
                    skip_empty = False
                
                # Stop at next header or after paragraph break
                if line_stripped.startswith('#'):
                    break
                elif not line_stripped and overview_lines:
                    # Paragraph break - we have our overview
                    break
                elif line_stripped:
                    overview_lines.append(line_stripped)
        
        if overview_lines:
            return ' '.join(overview_lines)[:500]
        
        return ""
    
    def is_framework_main_page(self, content: str, file_path: str) -> bool:
        """Check if this is a framework's main page."""
        path = Path(file_path)
        
        # Check if it's an index file
        if path.stem.lower() in ['index', 'readme', 'overview']:
            return True
        
        # Check if file name matches framework name
        if path.parent.name == "documentation" and path.stem == path.parent.parent.name:
            return True
        
        # Check content for framework-level indicators
        framework_indicators = [
            r'^\s*#\s+\w+\s+Framework',
            r'^\s*#\s+\w+\s+Module',
            r'^\s*#\s+About\s+\w+',
            r'^\s*#\s+\w+\s+Overview',
        ]
        
        for pattern in framework_indicators:
            if re.search(pattern, content, re.IGNORECASE | re.MULTILINE):
                return True
        
        return False
    
    def get_file_modified_time(self, file_path: str) -> str:
        """Get file modification time."""
        try:
            if os.path.exists(file_path):
                mtime = os.path.getmtime(file_path)
                return datetime.fromtimestamp(mtime).isoformat()
        except:
            pass
        return datetime.now().isoformat()
    
    def generate_url(self, file_path: str) -> str:
        """Generate Apple Developer documentation URL from file path."""
        path = Path(file_path)
        
        # Extract path components
        parts = list(path.parts)
        
        # Find documentation index
        if "documentation" in parts:
            idx = parts.index("documentation")
            url_parts = parts[idx+1:]
        else:
            url_parts = parts[-2:] if len(parts) > 1 else parts
        
        # Remove .md extension
        if url_parts and url_parts[-1].endswith('.md'):
            url_parts[-1] = url_parts[-1][:-3]
        
        # Build URL
        url_path = "/".join(url_parts).lower()
        return f"https://developer.apple.com/documentation/{url_path}"

def main():
    """CLI for testing metadata extraction."""
    parser = argparse.ArgumentParser(description="Extract metadata from Apple documentation")
    parser.add_argument("file_path", help="Path to markdown file")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--debug", action="store_true", help="Show debug information")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file_path):
        print(f"Error: File not found: {args.file_path}")
        return 1
    
    extractor = MetadataExtractor()
    
    try:
        with open(args.file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata = extractor.extract_metadata(content, args.file_path)
        
        if args.json:
            print(json.dumps(metadata, indent=2))
        else:
            print(f"Metadata for: {args.file_path}\n")
            for key, value in metadata.items():
                if isinstance(value, list):
                    print(f"{key:20s}: {', '.join(value)}")
                else:
                    print(f"{key:20s}: {value}")
        
        return 0
        
    except Exception as e:
        print(f"Error processing file: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit(main())