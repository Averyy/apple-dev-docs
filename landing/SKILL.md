---
name: searching-apple-docs
description: Searches Apple developer documentation for Swift, SwiftUI, UIKit, AppKit, and 370+ frameworks. Useful for looking up iOS/macOS/visionOS APIs, checking method signatures, finding platform availability, or debugging Apple framework issues.
---

# Searching Apple Documentation

335K pre-indexed Apple developer documents.

## Default Workflow

**Step 1:** Search with summaries first
```
apple-docs:search_apple_docs(
  query: "NavigationStack",
  framework: "SwiftUI",
  summary_mode: true
)
```
→ Results include `Path: documentation/SwiftUI/navigationstack.md`

**Step 2:** Expand using the path from results
```
apple-docs:expand_result(
  file_path: "documentation/SwiftUI/navigationstack.md"
)
```

That's it for most lookups. Add complexity only when needed.

## Tool Reference

| Tool | Purpose |
|------|---------|
| `apple-docs:search_apple_docs` | Find symbols, search documentation |
| `apple-docs:expand_result` | Get full documentation for a symbol |
| `apple-docs:list_frameworks` | Browse available frameworks |

## When Search Fails

**No results?**
1. Check framework spelling with `apple-docs:list_frameworks`
2. Use exact Apple terminology (e.g., `NavigationStack` not "nav stack")
3. Remove generic words, keep symbol names

**Too many irrelevant results?**
- Add `framework` parameter
- Add `strict_framework: true`
- Increase `relevance_threshold` (0.0-1.0)

**Results truncated?**
- Increase `token_budget` (default 5000, max 25000)
- Use `offset` for pagination

## Parameters

### apple-docs:search_apple_docs

| Parameter | Default | Notes |
|-----------|---------|-------|
| `query` | *required* | Use exact symbol names |
| `framework` | all | "SwiftUI", "UIKit", "Foundation", etc. |
| `platform` | all | ios, macos, visionos, watchos, tvos |
| `summary_mode` | false | **Use `true` for initial searches** |
| `limit` | 10 | 1-20 |
| `offset` | 0 | For pagination |
| `strict_framework` | false | Exclude cross-framework results |
| `token_budget` | 5000 | 1000-25000 |
| `relevance_threshold` | 0.0 | 0.0-1.0, higher = stricter |

### apple-docs:expand_result

| Parameter | Notes |
|-----------|-------|
| `file_path` | Path from search results (`documentation/SwiftUI/button.md`) or symbol name (`Button`) |
| `sections` | Optional: `["declaration", "overview"]` to limit output |

**Note:** Symbol-only lookups (e.g., `file_path: "Button"`) resolve ambiguously across all frameworks. "Button" may return WebKit JS instead of SwiftUI. Use the full path from search results for precise lookups.

### apple-docs:list_frameworks

| Parameter | Notes |
|-----------|-------|
| `query` | Optional filter: "UI", "Core", "Kit" |

## Examples

**Look up a symbol:**
```
apple-docs:search_apple_docs(query: "AsyncImage", framework: "SwiftUI", summary_mode: true)
→ Path: documentation/SwiftUI/asyncimage.md

apple-docs:expand_result(file_path: "documentation/SwiftUI/asyncimage.md")
```

**Check platform availability:**
```
apple-docs:search_apple_docs(query: "RealityView", platform: "visionos")
→ Check "Availability" in results
```

**Find framework name:**
```
apple-docs:list_frameworks(query: "Core")
→ CoreData, CoreLocation, CoreML, etc.
```
