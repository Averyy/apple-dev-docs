#!/usr/bin/env python3
"""Simplified test to show JSON extraction works."""

import json
import urllib.request

# The page you want to see
doc_url = "https://developer.apple.com/documentation/swiftui/declaring-a-custom-view"

# Convert to JSON URL
json_url = doc_url.replace("/documentation/", "/tutorials/data/documentation/") + ".json"

print(f"Documentation URL: {doc_url}")
print(f"JSON API URL: {json_url}")
print("\n=== FETCHING JSON ===")

# Fetch the JSON
with urllib.request.urlopen(json_url) as response:
    json_data = json.loads(response.read())

# Extract key information
title = json_data.get('metadata', {}).get('title', 'Untitled')
abstract = ' '.join(item['text'] for item in json_data.get('abstract', []) if item.get('type') == 'text')

print(f"\nTitle: {title}")
print(f"Abstract: {abstract}")

# Extract overview content
print("\n=== OVERVIEW CONTENT ===")
for section in json_data.get('primaryContentSections', []):
    if section.get('kind') == 'content':
        for item in section.get('content', []):
            if item.get('type') == 'heading' and item.get('text') == 'Overview':
                print(f"\n## {item['text']}")
            elif item.get('type') == 'paragraph':
                paragraph_text = []
                for inline in item.get('inlineContent', []):
                    if inline.get('type') == 'text':
                        paragraph_text.append(inline['text'])
                    elif inline.get('type') == 'reference':
                        # Handle references
                        ref_title = inline.get('title', '')
                        if ref_title:
                            paragraph_text.append(f"[{ref_title}]")
                if paragraph_text:
                    print('\n' + ''.join(paragraph_text))

# Show some of the structured content
print("\n=== STRUCTURED SECTIONS ===")
for section in json_data.get('primaryContentSections', []):
    if section.get('kind') == 'content':
        for item in section.get('content', []):
            if item.get('type') == 'heading':
                print(f"\n### {item['text']}")
            elif item.get('type') == 'codeListing':
                print(f"\n```{item.get('syntax', 'swift')}")
                for line in item.get('code', []):
                    print(line)
                print("```")

print("\n=== MARKDOWN OUTPUT (SAMPLE) ===")
print(f"""# {title}

**Framework**: SwiftUI

{abstract}

## Overview

SwiftUI offers a declarative approach to user interface design. With a traditional imperative approach, the burden is on your controller code not only to instantiate, lay out, and configure views, but also to continually make updates as conditions change. In contrast, with a declarative approach, you create a lightweight description of your user interface by declaring views in a hierarchy that mirrors the desired layout of your interface. SwiftUI then manages drawing and updating these views in response to events like user input or state changes.

### Conform to the view protocol

Declare a custom view type by defining a structure that conforms to the [View] protocol:

```swift
struct MyView: View {{
}}
```

... (and much more content is available in the JSON)
""")