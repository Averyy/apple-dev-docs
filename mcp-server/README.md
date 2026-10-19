# MCP Server Implementation

This directory contains the MCP server implementation for Apple Developer Documentation search.

**Current Version:** 3.2.0 (`SERVER_VERSION` in `apple_docs_mcp.py`; CI derives the image version label from it)

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
