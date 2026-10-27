# MCP Server Implementation

This directory contains the MCP server implementation for Apple Developer Documentation search.

**Current Version:** 3.5.1 (`SERVER_VERSION` in `apple_docs_mcp.py`; CI derives the image version label from it)

## Architecture

```
mcp-server/
├── apple_docs_mcp.py         # Main MCP server (HTTP via Streamable HTTP)
├── scripts/                  # startup_check.py (index on start), docker_index_helper.sh
├── docker/                   # startup.sh, supervisord.conf
├── tests/                    # Test suite
├── Dockerfile                # All-in-one image (Meilisearch + MCP server)
├── docker-compose.yml        # Production compose
├── docker-compose.local.yml  # Local build for testing
└── requirements.txt          # Python dependencies
```

## Transport

The server uses **Streamable HTTP** transport only. For STDIO clients (like Claude Desktop), use `mcp-remote` as a bridge:

```bash
npx -y mcp-remote https://xdocs.dev/mcp
```

## Available Tools

| Tool | Description |
|------|-------------|
| `search_apple_docs` | Search documentation with wildcard support (`*`, `?`) |
| `expand_result` | Get full content for a symbol name or file path |
| `list_frameworks` | Browse frameworks with optional filtering |
| `get_version` | Get server version and status |

## Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server (requires Meilisearch)
python apple_docs_mcp.py --port 8000
```

## Docker Deployment

```bash
docker-compose up -d
```

## Changelog

### v3.5.1
- A type typed without its prefix and in lower case within a framework ranks first among the pages titled with that word: a name in lower case says nothing about case, and so nothing about a prefix either, so the type ranks as high as the best of them and the more general page comes first (`Metal device` → `MTLDevice`, 7th before, behind the `device` properties of Metal's types; `AppKit window` → `NSWindow`, `UIKit button` → `UIButton`, `Contacts contact` → `CNContact`). A type titled with the word itself ranks so too, and comes before the one named so after a prefix (`Foundation url` → `URL`, 4th before; `Foundation data` → `Data`, then `NSData`). Such a type goes before the other pages it ties with (`AppKit color` → `NSColor`, before AppKit's shorter-path `Color` API collection). Not for a name written `@name`, which asks for its own kinds. The results' note names the types' own spelling ("the types named 'ContactStore' after a prefix"), not the spellings looked up
- The words before the last are also looked up in the singular (in any case), as a compound name has them, so a framework named in the plural finds its types (`Contacts store` → `CNContactStore`, 6th before; `Photos library` → `PHPhotoLibrary`, 18th)
- Measured on the local index (405,421 documents) against 3.5.0: golden (57 and 66), the audit's 80 queries, 57 probes and 350 random titles unchanged; 30 unprefixed-name probes top-1 23 → 30; 24 framework-word queries 16 → 19; 61 new framework + word queries 28 → 54, none worse

### v3.5.0
- A name written as Swift uses it finds its page: `@State`, `@Model`, `@MainActor`, `#Preview` are compared without the `@`/`#` (Meilisearch reads them as separators), and such a name is only a type that can be an attribute (a property wrapper, result builder or global actor: a class, struct, enum, actor or typealias), an attached macro, or for `#Name` a freestanding macro, whose page is titled `Name(…)` (`@Model` → SwiftData's `Model()`; `@State` and `@Model` were past the top 100). A one-word `@name` that no type or macro has (`@escaping`, `@objc`, `@main`, `@discardableResult`) is one of Swift's built-in attributes: it is searched as `name attribute`, which finds The Swift Programming Language's Attributes chapter, and the results say so. A wildcard pattern written so (`@State*`, `#Preview?`) matches the names without the sigil, of those kinds
- A query that names a framework (`CareKit OCKTask`, `WidgetKit timeline provider`, `App Intents AppIntent`, `SwiftData @Model`) looks the rest of it up within that framework: the type it names, or the name its words spell. A nested module or package is named by any part of its name (`CareKit` for `CareKit/CareKitStore`, `swift-log` for `swift-log/Logging`), for this and for the title boosts. The whole query's spelled name is still looked up everywhere (`photos picker` → `PhotosPicker`)
- `Type.member` finds the member under its type (`Product.purchase` → `purchase(options:)`, 21st before; `DispatchQueue.main.async` → `async(execute:)`, 81st; `Text.font`, `View.sheet`, `Color.red`, `UIApplication.shared`), ranked as the name it is, or as a named symbol within a longer query; `expand_result` reads `Type.member` and `@Name` too (they were "not found")
- A type's name without its prefix finds it within a framework the search filters on or the query names (`Button` with `framework: "UIKit"` → `UIButton`, `Metal command queue` → `MTLCommandQueue`, `Speech recognizer` → `SFSpeechRecognizer`), ranked after a page titled with the name itself. The indexer records it (`api_name_unprefixed`: 2-4 leading capitals before a capitalized word, for types only; `PROCESSOR_VERSION` 5, which also gives a page whose text starts with a quote banner (the HIG's "Updated" line) its first paragraph as summary, so the first start rebuilds the index by swap; the indexer now also rebuilds whenever the live index lacks a filterable, sortable or searchable attribute its settings name, so a new field never arrives by an in-place settings task). Until the rebuild is swapped in the server doesn't look it up (it reads the index's filterable attributes)
- A multi-word query that names no page prefers, slightly, the pages whose title holds most of its words (a symbol by its name, not its argument labels): `tab bar design guidelines` → HIG Tab bars, `Keychain store password`, `how to show a sheet in SwiftUI` → `sheet(isPresented:onDismiss:content:)`, golden questions on location permission and local notifications; long release notes and technotes that hold every word somewhere rank below them
- Equally relevant pages go a deprecated one after the others (`accessibilityLabel`: SpriteKit's before RealityKit's deprecated one)
- A result from a long page shows the part that best matches: every part holds the page's title, so the words the title doesn't hold break a near-tie (`in-app purchase App Store review guidelines` → App Review Guidelines Part 5, which holds 3.1.1, not Part 7)
- A link to an overload with no page of its own (`text/init(_)-1a4oh.md`: Apple lists every overload on its group page, whose preferred one is the unsuffixed page) leads to that page in hints and `expand_result` (284 links, 113 targets); a link that stays a `search:` hint drops the DocC hash from its words (`expm1(_)`, not `expm1(_) xkzx`)
- `expand_result`'s `sections` follow both DocC layouts: in the one from render version 5 (Apple's content headings at their own level, `## Overview` holding `####` headings) a section holds its deeper headings (18 pages' `overview` was cut at its first `####`, e.g. `Swift-Org/userdocs/commands.md` 5,227 → 103 characters); in the older one (`#### Overview` beside `## Declaration`) nothing changes
- Measured on the local index (403,704 documents) against 3.4.3: golden hit@3 0.860 → 0.895, MRR 0.824 → 0.857; 9 new golden entries (66: 0.909 / 0.877, expand@1 13/13); the 2026-10-26 audit's 80 queries with an expected page top-1 52 → 61, top-3 64 → 70; 350 random titles unchanged but one deprecated page

### v3.4.3
- `summary_mode` results show the overview's local links as hints too (`NavigationLink (-> expand_result: documentation/SwiftUI/navigationlink.md)`), as the content and the deprecation note do; the overview is cut to 400 characters after that, never inside a hint or a link. The indexer's own 500-character cut of an overview no longer falls inside a link either (259 overviews ended in half a link; until the rebuild below, such a half link isn't shown)
- A result's link is valid markdown: a character a URL can't hold is percent-encoded (`Configuration%20File.md`: seven sourcekit-lsp docs had spaces in their URL), and so are the parentheses of a URL whose parentheses don't pair up (20 pages, 15 Apple and 5 Swift Package Index, whose URL the site cut inside its argument list). The scrapers now encode the URLs they build from file names (GitHub pages, DocC catalog assets) and the page URLs they write (MLX `RENDER_VERSION` 3: the next MLX scrape rewrites those seven docs)
- No page is indexed with an empty title: a page without a `# ` heading takes its front matter's title, else its first heading of any level, else its file name, and a `# ` line in code is never a title (`documentation/MLX/mlx-lm/README.md`, which starts at `## MLX LM`, showed `## 1.  (NN%)`; `PROCESSOR_VERSION` 4, so the first start rebuilds the index by swap). Until then a result without a title shows its file name
- A search filtering on a framework the index doesn't have says so, with the closest framework names and `list_frameworks`; one filtering on a platform that isn't one (`android`) says so and lists the platforms (`ios`, `ipados`, `mac catalyst`, `macos`, `tvos`, `visionos`, `watchos`, or `all`) instead of searching
- `expand_result` with a section the page doesn't have (`sections=["no_such_section"]`) names it and lists the page's sections, instead of returning only the page's title

### v3.4.2
- `/health`'s defaults follow the corpus after Batch 4 (~404K documents): `healthy` from 363,000 documents (`MIN_EXPECTED_DOCS`, ~90%), and indexing progress counted against 404,000 (`EXPECTED_FULL_INDEX_SIZE`)

### v3.4.1
- Equally relevant pages go the shallower path within its framework first, then the shorter: a type at its framework's root before another source's page one folder down (`LanguageModelSession`: Foundation Models' class before the Python SDK's `api/session`)

### v3.4.0
- Results mark a deprecated page (`Type: method | Deprecated`) and say what to use instead (`Deprecated: Use UNNotificationRequest instead.`, its links as hints). The indexer flags a page deprecated when it has Apple's deprecation summary or every platform it lists is deprecated (`deprecated`, `deprecation`; `PROCESSOR_VERSION` 3, so the first start rebuilds the index by swap)
- A deprecated page whose deprecation summary holds every word of the query ranks lower, unless the query names it: the summary says what to use instead, so it holds the words of its replacement's task (`schedule local notification` found five deprecated UIKit methods, whose summary reads "Use the UNUserNotificationCenter class to schedule local notifications instead", before the UserNotifications article and APIs)

### v3.3.0
- A query of two or more words also finds the type or framework whose name they spell (`vision entitlement services`, `async image`, `navigation stack`, `url session` find `VisionEntitlementServices`, `AsyncImage`, `NavigationStack`, `URLSession`): it ranks right after a page titled with the query itself and above every other page (the total says "and the pages named 'asyncimage'" when it came from past the top matches). Meilisearch keeps a CamelCase name as one word, which the words matched only as typos
- Local links in results and in `expand_result` become the path of the page they lead to (`Button (-> expand_result: documentation/SwiftUI/button.md)`), for links relative to the framework's directory or to the page, percent-encoded or with a `#fragment`, and for link text holding brackets (`[var locations: [Accessory.LocationName]](…)`, 16K Topics links that stayed raw); a link whose page isn't in the docs stays a `search:` hint
- `expand_result`'s `sections` keep their subsections (`topics` its groups, `overview` its subheadings) and stop at the next heading of their level, and their links become hints too
- Responses stay within `token_budget`, counted in characters (the per-result estimates undercounted by up to ~1 token a result)
- A page without a Kind line gets its `Type` from its Role line once re-scraped: `collection` for an API collection, `sample-code` for sample code, else `article`. Like articles, API collections and sample code get no named-symbol boost (the smaller boost for the symbol one word of a longer query names)

### v3.2.0
- `search_apple_docs` returns one result per page, not one per indexed chunk of a long page; such a result shows the part that matched (`Part 3 of 6`)
- Results are ranked by Meilisearch's relevance (`_rankingScore`) plus a boost for the page whose title is the name asked for (the query may also name its framework, in one word or several: `Button SwiftUI`, `Core Data NSPersistentContainer`); a name typed all in lower case matches a title in any case (`color`, `text`, `accessibility` find SwiftUI's `Color` and `Text` and the Accessibility framework, not the properties of that name), and a smaller boost goes to the symbol one word of a longer query names, typed with its capitals (`Concurrency Task`, `date formatting DateFormatter`, `Core Graphics CGPoint`); equally relevant pages come the more general first: the shorter path within its framework (a type before its members), then the page on more platforms (Foundation's `UserDefaults` before TVMLKit JS's). The relevance % and `relevance_threshold` use this score
- A one-word query also searches the types named so, when the top 100 matches were cut: Meilisearch scores every page titled with a common name alike, so `String`, `Data`, `Color`, `State` and `Image` missed their type's page (the total says "and the types named 'Data'")
- Questions ("What is NavigationStack?", "How do I present a sheet in SwiftUI?", or without the `?`, a question word followed by another such word) are searched without their question and function words; a page titled with the question itself still counts as an exact title
- A wildcard pattern is matched against the top 100 matches for its literal text and, when it starts with 2+ literal characters, every API name starting with them, up to 10,000 (`UI*Controller`, `CL*Manager`, which found nothing before); the total says when either was cut. Wildcard results are ranked by how closely the name fits the pattern ignoring case (the relevance %), names in the pattern's case first (`UI*` lists `UIKey` before `uid`) unless the pattern is all lowercase
- Result links are labelled by their host: "View on Apple Developer" only for Apple's pages ("View on GitHub", "View on ml-explore.github.io"...)
- `expand_result` returns the whole page (all its chunks, not one); a page over ~20K tokens comes in parts, each reply holding as many as fit, and the new `part` argument starts at any of them. `sections` are taken from the whole page
- `expand_result`'s symbol lookup chooses among the types named exactly so, every page named so and the top 100 matches: a type before a member, the simplest overload, the most general page (`Text`, `View`, `Color`, `Data`, `UserDefaults` and `viewDidLoad` find SwiftUI's, Foundation's and UIKit's pages). The other-frameworks note counts every framework with a page of that name and names at most 8
- A result's `Type` comes from its page's Kind line (`article` without one) and its platforms from the page's Availability list when it has one; a nested type is named by its own name (`Publishers.Map` is `Map`)
- `/health` reports only the live `apple-docs` index. A rebuild is now built beside it and swapped in (search serves the whole index throughout), so it no longer shows as `indexing` (503) or turns the container unhealthy, and `documents` stays the live count until the swap; only the ~3.5 min after an update or a swap is `indexing`. A start with no doc changes queues no index task, so `/health` stays 200 through it
- Fixed: a search running while `/health` was polled could fail with "Search temporarily unavailable" (`missing_content_type`)

### v3.1.0
- `expand_result` takes an optional `framework` for symbol lookups (`List`, `Text`, `View`, `viewDidLoad` exist in many frameworks); without it, the result notes the other frameworks that match
- `search_apple_docs`'s `strict_framework` is deprecated and has no effect: `framework` always filters. It is still accepted so older clients and skill files keep working

### v3.0.2
- Responses stay within `token_budget` (room reserved for the header and footer lines)
- A truncated result closes any code block the cut left open, so the notice and next-page hint stay readable
- Wildcard examples in the tool description use patterns that work (`UIView*`, `NS*Button`, `Button?`)

### v3.0.1
- Questions ending in `?` are searched as text; `?` is a wildcard only in single-word queries
- Token-budget pagination no longer skips or repeats results; results are numbered by overall rank
- `token_budget` also limits the first result (truncated with a pointer to `expand_result`)
- Honest totals ("ranked from the top N matches") and a clear message for an offset past the end
- `expand_result` treats any input without `/` or `.md` as a symbol (e.g. `withAnimation`)
- Symbol lookup prefers an exact-case title, then that name's function page (`Button` → SwiftUI `Button`, `withAnimation` → `withAnimation(_:_:)`)
- `serverInfo.version` reports the server version

### v3.0.0
- Removed `choose_framework`/`current_framework` (their state was shared by all clients)
- Wildcard matching can no longer freeze the server; input lengths are capped
- `expand_result` accepts full-length paths; errors are returned as MCP errors
- Text-only results (no duplicate structured content); periodic restarts removed

### v2.x
- Not recorded here; see the git history of `apple_docs_mcp.py`

### v1.1.0
- Added wildcard search support (`*View`, `UI*`, `Button?`)
- Added `get_version` tool for status information
- Enhanced `expand_result` to accept symbol names
- Improved error messages with contextual suggestions
- Added query filtering to `list_frameworks`

### v1.0.0
- Initial release with `search_apple_docs`, `expand_result`, `list_frameworks`
