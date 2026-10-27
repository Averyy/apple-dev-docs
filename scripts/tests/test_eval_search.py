#!/usr/bin/env python3
"""The golden-query eval runner (scripts/tests/eval_search.py): URL resolution, hit parsing, scoring."""

import json
import logging
import os
import re
import socket
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

import httpx
import pytest

import eval_search as ev
from eval_search import EvalError, Expectation, GoldenQuery, Hit, McpClient, QueryResult

SWIFT_BOOK_URL = "https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Concurrency.md"
HIG_URL = "https://developer.apple.com/design/human-interface-guidelines/buttons"
NAV_URL = "https://developer.apple.com/documentation/swiftui/navigationstack"
FRAME_URL = "https://developer.apple.com/documentation/swiftui/view/frame(width:height:alignment:)"
STATE_URL = "https://developer.apple.com/documentation/swiftui/state"

# search_apple_docs output as server 3.1.0 sends it (summary_mode, limit 3)
SERVER_RESPONSE = """Search Results: frame
Showing 1-3 of 100 results (ranked from the top 100 matches)

## 1. frame (100%)
Framework: AppKit | Type: property
Path: `documentation/AppKit/nscollectionlayoutgroupcustomitem/frame.md`
[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutgroupcustomitem/frame)

**Framework**: AppKit **Kind**: property

---

## 2. frame (100%)
Framework: AppKit | Type: property
Path: `documentation/AppKit/nscollectionlayoutvisibleitem/frame.md`
[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutvisibleitem/frame)

**Framework**: AppKit **Kind**: property **Required**: Yes

---

## 3. frame (100%)
Framework: AppKit | Type: property
Path: `documentation/AppKit/nscollectionviewlayoutattributes/frame.md`
[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/frame)

**Framework**: AppKit **Kind**: property

---


97 more results available. Use offset=3 to continue"""

# expand_result("View") as server 3.1.0 sends it (trailing spaces dropped): the
# page, then the note naming the other frameworks
VIEW_PAGE_URL = "https://developer.apple.com/documentation/appintents/confirmationactionname/view"
EXPAND_RESPONSE = """# view

**Framework**: App Intents
**Kind**: property

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static var view: ConfirmationActionName { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/confirmationactionname/view)*

---
Note: 'View' also matches pages in AppKit; showing AppIntents. Pass framework (e.g. framework="AppKit") to choose another."""

NO_RESULTS = """No results found for 'zzqq'
   Framework: SwiftUI

Suggestions:
   - Try simpler keywords
   - Use wildcards: Button* or NSTable*
   - Try without framework filter"""

# Characters str.splitlines() breaks at but SSE and the server's "\n"-joined text
# don't: a title, overview or page can hold any of them inside a line
LINE_SEPARATORS = ["\u2028", "\u2029", "\u0085", "\x0b", "\x0c", "\x1c", "\x1d", "\x1e"]


def search_text(query: str, hits: Sequence[Tuple[str, str, str]],
                framework: str = "", platform: str = "") -> str:
    """Build a response in search_apple_docs' format (apple_docs_mcp.py)."""
    if not hits:
        return f"No results found for '{query}'\n\nSuggestions:\n   - Try simpler keywords"
    output = [f"Search Results: {query}", f"Showing 1-{len(hits)} of {len(hits)} results", ""]
    if framework:
        output.append(f"Framework: {framework}")
    if platform:
        output.append(f"Platform: {platform}")
    output.append("")
    for rank, (title, path, url) in enumerate(hits, 1):
        lines = [f"## {rank}. {title} (85%)", "Framework: SwiftUI | Type: struct", f"Path: `{path}`",
                 f"[View on Apple Developer]({url})", ""]
        output.append("\n".join(lines + ["An overview.", "\n---\n"]))
    return "\n".join(output)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def apple_page(title: str, url: str) -> str:
    """An Apple page as markdown_converter writes it, ending with its footer."""
    return f"# {title}\n\nOverview.\n\n---\n\n*[View on Apple Developer]({url})*"


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A repo with Apple, HIG, Swift and MLX hash files in their real formats."""
    swiftui: Dict[str, Any] = {
        "https://developer.apple.com/tutorials/data/documentation/swiftui/navigationstack.json":
            {"hash": "a", "file_path": "documentation/SwiftUI/navigationstack.md"},
        # Doc-URL keys keep Apple's casing; expectations are lowercase
        "https://developer.apple.com/documentation/SwiftUI/NavigationStack":
            {"hash": "a", "file_path": "documentation/SwiftUI/navigationstack.md"},
        "https://developer.apple.com/documentation/swiftui/view/frame(width:height:alignment:)":
            {"hash": "b", "file_path": "documentation/SwiftUI/view/frame-widthheightalignment.md"},
        # A doc-URL key whose file was never written
        "https://developer.apple.com/documentation/swiftui/gone":
            {"hash": "c", "file_path": "documentation/SwiftUI/gone.md"},
        # Error entries carry no file
        "https://developer.apple.com/documentation/swiftui/broken":
            {"status": "error", "error": "HTTP 500"},
        # Two pages whose names collide share a file, which holds the one its footer names
        STATE_URL: {"hash": "g", "file_path": "documentation/SwiftUI/state.md"},
        STATE_URL + "()": {"hash": "g", "file_path": "documentation/SwiftUI/state.md"},
        "https://developer.apple.com/documentation/swiftui/nofooter":
            {"hash": "h", "file_path": "documentation/SwiftUI/nofooter.md"},
    }
    write(tmp_path / ".hashes" / "SwiftUI_hashes.json",
          json.dumps({"metadata": {"total_pages": 3}, "hashes": swiftui}))
    write(tmp_path / ".hashes" / "UIKit_hashes.json", json.dumps({"hashes": {
        "https://developer.apple.com/documentation/uikit/uiview":
            {"hash": "d", "file_path": "/home/runner/work/apple-dev-docs/apple-dev-docs/documentation/UIKit/uiview.md"},
    }}))
    # HIG: a flat dict keyed by JSON URLs, never doc-URL keys
    write(tmp_path / ".hashes" / "hig_docs_hashes.json", json.dumps({
        "https://developer.apple.com/tutorials/data/design/human-interface-guidelines/buttons.json":
            {"hash": "e", "file_path": "/home/runner/work/apple-dev-docs/apple-dev-docs/documentation/HIG/buttons.md"},
    }))
    # Swift/MLX: bare digests
    write(tmp_path / ".hashes" / "swift_docs_hashes.json", json.dumps({
        "metadata": {"total_files": 1},
        "hashes": {"swiftlang/swift-book:TSPL.docc/LanguageGuide/Concurrency.md": "f"},
    }))
    write(tmp_path / "documentation" / "SwiftUI" / "navigationstack.md",
          apple_page("NavigationStack", NAV_URL))
    write(tmp_path / "documentation" / "SwiftUI" / "view" / "frame-widthheightalignment.md",
          apple_page("frame(width:height:alignment:)", FRAME_URL))
    write(tmp_path / "documentation" / "SwiftUI" / "state.md", apple_page("State", STATE_URL))
    write(tmp_path / "documentation" / "SwiftUI" / "nofooter.md", "# No footer\n")
    write(tmp_path / "documentation" / "UIKit" / "uiview.md",
          apple_page("UIView", "https://developer.apple.com/documentation/uikit/uiview"))
    write(tmp_path / "documentation" / "Swift-Book" / "LanguageGuide" / "Concurrency.md",
          f"---\nsource: swiftlang/swift-book\nurl: {SWIFT_BOOK_URL}\n---\n\n# Concurrency\n")
    write(tmp_path / "documentation" / "HIG" / "buttons.md",
          f"---\nurl: {HIG_URL}\nframework: HIG\n---\n\n# Buttons\n")
    write(tmp_path / "documentation" / "HIG" / "no-front-matter.md", "# Plain\n")
    return tmp_path


def golden(*expected: str, query: str = "q") -> GoldenQuery:
    return GoldenQuery(query, "", "", tuple(expected))


# --- golden file -------------------------------------------------------------

def test_repo_golden_file_is_valid() -> None:
    queries = ev.load_golden(ev.REPO_ROOT / ev.GOLDEN_FILE)
    assert len(queries) >= 40
    assert all(1 <= len(q.expected) <= ev.TOP_K for q in queries)
    # expand_result's symbol window (3.12) is measured on the symbols it misses
    unfiltered_lookups = {q.query for q in queries if q.expand and not q.framework}
    assert {"List", "Text", "View", "viewDidLoad"} <= unfiltered_lookups
    # 3.12's ranking example, where the isResponding property (85%) outranks the
    # class page, is measured on the class page alone
    unfiltered = {q.query: q.expected for q in queries if not q.framework and not q.platform}
    assert unfiltered["LanguageModelSession respond"] == (
        "https://developer.apple.com/documentation/foundationmodels/languagemodelsession",)


def test_load_golden_reads_optional_filters_and_expand(tmp_path: Path) -> None:
    path = tmp_path / "golden.json"
    path.write_text(json.dumps([
        {"query": "NavigationStack", "framework": "SwiftUI", "expected_top3": [NAV_URL],
         "expand": True},
        {"query": " WKWebView ", "platform": "ios", "expected_top3": [NAV_URL, FRAME_URL]},
        {"query": "frame", "expected_top3": [FRAME_URL], "expand": False},
    ]))
    assert ev.load_golden(path) == [
        GoldenQuery("NavigationStack", "SwiftUI", "", (NAV_URL,), expand=True),
        GoldenQuery("WKWebView", "", "ios", (NAV_URL, FRAME_URL)),
        GoldenQuery("frame", "", "", (FRAME_URL,)),
    ]


@pytest.mark.parametrize("entries, message", [
    ({"query": "q"}, "non-empty JSON list"),
    ([], "non-empty JSON list"),
    (["q"], "not a JSON object"),
    ([{"query": "q", "expected_top3": [NAV_URL], "note": "x"}], "unknown key(s) note"),
    ([{"query": " ", "expected_top3": [NAV_URL]}], "'query' must be"),
    ([{"query": "q", "framework": "", "expected_top3": [NAV_URL]}], "'framework' must be"),
    ([{"query": "q", "platform": 3, "expected_top3": [NAV_URL]}], "'platform' must be"),
    ([{"query": "q"}], "'expected_top3' must list"),
    ([{"query": "q", "expected_top3": []}], "'expected_top3' must list"),
    ([{"query": "q", "expected_top3": [NAV_URL, FRAME_URL, HIG_URL, SWIFT_BOOK_URL]}],
     "'expected_top3' must list"),
    ([{"query": "q", "expected_top3": ["swiftui/navigationstack"]}], "'expected_top3' must list"),
    ([{"query": "q", "expected_top3": [NAV_URL, NAV_URL.replace("navigationstack", "NavigationStack")]}], "repeats a URL"),
    ([{"query": "q", "expected_top3": [NAV_URL]}, {"query": "q", "expected_top3": [FRAME_URL]}],
     "duplicate query"),
    ([{"query": "q", "expected_top3": [NAV_URL], "expand": "yes"}], "'expand' must be true or false"),
    ([{"query": "q", "platform": "ios", "expected_top3": [NAV_URL], "expand": True}],
     "'expand' takes no platform"),
    ([{"query": "What is NavigationStack?", "expected_top3": [NAV_URL], "expand": True}],
     "'expand' needs a symbol name"),
    ([{"query": "documentation/SwiftUI/navigationstack.md", "expected_top3": [NAV_URL],
       "expand": True}], "'expand' needs a symbol name"),
    ([{"query": "navigationstack.md", "expected_top3": [NAV_URL], "expand": True}],
     "'expand' needs a symbol name"),
    ([{"query": "UIView*", "expected_top3": [NAV_URL], "expand": True}], "'expand' needs a symbol name"),
])
def test_load_golden_rejects_invalid_files(tmp_path: Path, entries: Any, message: str) -> None:
    path = tmp_path / "golden.json"
    path.write_text(json.dumps(entries))
    with pytest.raises(EvalError, match=re.escape(message)):
        ev.load_golden(path)


def test_load_golden_rejects_unparseable_json(tmp_path: Path) -> None:
    path = tmp_path / "golden.json"
    path.write_text("[{")
    with pytest.raises(EvalError, match="can't read golden queries"):
        ev.load_golden(path)


# --- URL resolution ----------------------------------------------------------

def test_apple_url_resolves_case_insensitively_through_doc_url_keys(repo: Path) -> None:
    [lower], [mixed] = ev.resolve_expectations(
        [golden(NAV_URL), golden("https://developer.apple.com/documentation/swiftui/NAVIGATIONSTACK",
                                 query="q2")], repo)
    assert lower == Expectation(NAV_URL, frozenset({"documentation/swiftui/navigationstack.md"}))
    assert mixed.paths == lower.paths


def test_apple_url_with_absolute_file_path_resolves_to_its_doc_path(repo: Path) -> None:
    [[expectation]] = ev.resolve_expectations(
        [golden("https://developer.apple.com/documentation/uikit/uiview")], repo)
    assert expectation.paths == frozenset({"documentation/uikit/uiview.md"})


def test_doc_url_index_skips_json_keys_error_entries_and_digests(repo: Path) -> None:
    index = ev.load_doc_url_index(repo / ".hashes")
    assert set(index) == {
        NAV_URL,
        FRAME_URL,
        STATE_URL,
        STATE_URL + "()",
        "https://developer.apple.com/documentation/swiftui/gone",
        "https://developer.apple.com/documentation/swiftui/nofooter",
        "https://developer.apple.com/documentation/uikit/uiview",
    }
    assert index[NAV_URL] == {"documentation/SwiftUI/navigationstack.md"}


def test_shared_file_resolves_only_for_the_page_its_footer_names(repo: Path) -> None:
    [[owner]] = ev.resolve_expectations([golden(STATE_URL)], repo)
    assert owner.paths == frozenset({"documentation/swiftui/state.md"})
    with pytest.raises(EvalError, match=re.escape(
            f"{STATE_URL}() resolves to documentation/SwiftUI/state.md "
            f"(footer: {STATE_URL}), which holds another page")):
        ev.resolve_expectations([golden(STATE_URL + "()")], repo)


def test_apple_page_without_footer_does_not_resolve(repo: Path) -> None:
    with pytest.raises(EvalError, match=re.escape(
            "resolves to documentation/SwiftUI/nofooter.md (footer: None)")):
        ev.resolve_expectations(
            [golden("https://developer.apple.com/documentation/swiftui/nofooter")], repo)


def test_footer_url_reads_the_last_line(tmp_path: Path) -> None:
    page = tmp_path / "failure.md"
    url = "https://developer.apple.com/documentation/swiftui/asyncimagephase/failure(_:)"
    page.write_text("x" * 5000 + apple_page("failure(_:)", url) + "\n\n")
    assert ev.footer_url(page) == url
    page.write_text(apple_page("x", url) + "\n\nMore text after the footer.\n")
    assert ev.footer_url(page) is None
    page.write_text(apple_page("x", f"<{url}>"))
    assert ev.footer_url(page) is None


# A URL Apple cut inside its argument list, and its footer's (markdown_url)
CUT_URL = "https://developer.apple.com/documentation/metal/x/draw(_:patchstart:patch-4mdz8"
CUT_FOOTER_URL = CUT_URL.replace("draw(", "draw%28")


def test_footer_url_decodes_an_encoded_parenthesis(tmp_path: Path) -> None:
    page = tmp_path / "draw.md"
    for written in (CUT_FOOTER_URL, CUT_URL):  # an older rendering has it as it is
        page.write_text(apple_page("draw", written))
        assert ev.footer_url(page) == CUT_URL
    assert ev.parse_expand_result(apple_page("draw", CUT_FOOTER_URL) + "\n") == CUT_URL


@pytest.mark.parametrize("separator", LINE_SEPARATORS)
def test_footer_url_splits_lines_only_at_newlines(tmp_path: Path, separator: str) -> None:
    page = tmp_path / "frame.md"
    write(page, apple_page(f"frame{separator}x", FRAME_URL).replace("Overview.", f"Over{separator}view."))
    assert ev.footer_url(page) == FRAME_URL
    # A footer must be a line of its own, as parse_expand_result reads it too
    write(page, apple_page("frame", FRAME_URL).replace("\n*[View", f"\nSee also{separator}*[View"))
    assert ev.footer_url(page) is None


def test_non_apple_urls_resolve_to_front_matter_urls(repo: Path) -> None:
    [[swift_book], [hig]] = ev.resolve_expectations(
        [golden(SWIFT_BOOK_URL), golden(HIG_URL, query="q2")], repo)
    assert swift_book == Expectation(SWIFT_BOOK_URL, frozenset())
    assert hig == Expectation(HIG_URL, frozenset())


def test_every_unresolved_expectation_is_reported(repo: Path) -> None:
    queries = [
        golden(NAV_URL, "https://developer.apple.com/documentation/swiftui/missing"),
        golden("https://developer.apple.com/documentation/swiftui/gone", query="q2"),
        golden("https://developer.apple.com/documentation/swiftui/broken", query="q3"),
        # A HIG JSON-URL key is not a doc-URL key, and HIG pages match by front matter
        golden("https://developer.apple.com/design/human-interface-guidelines/menus", query="q4"),
        golden(SWIFT_BOOK_URL.lower(), query="q5"),
    ]
    with pytest.raises(EvalError) as raised:
        ev.resolve_expectations(queries, repo)
    message = str(raised.value)
    assert "swiftui/missing is not a doc-URL key" in message
    assert "documentation/SwiftUI/gone.md, which doesn't exist" in message
    assert "swiftui/broken is not a doc-URL key" in message
    assert "human-interface-guidelines/menus is no doc's front-matter url" in message
    assert f"{SWIFT_BOOK_URL.lower()} is no doc's front-matter url" in message
    assert NAV_URL not in message


def test_front_matter_scan_skips_apple_framework_dirs(repo: Path) -> None:
    write(repo / "documentation" / "SwiftUI" / "fm.md", "---\nurl: https://example.com/x\n---\n# X\n")
    with pytest.raises(EvalError, match="example.com/x is no doc's front-matter url"):
        ev.resolve_expectations([golden("https://example.com/x")], repo)


# --- hit parsing -------------------------------------------------------------

def test_parse_server_response() -> None:
    hits = ev.parse_search_results(SERVER_RESPONSE)
    assert [h.rank for h in hits] == [1, 2, 3]
    assert hits[0] == Hit(
        1, "frame", "documentation/AppKit/nscollectionlayoutgroupcustomitem/frame.md",
        "https://developer.apple.com/documentation/appkit/nscollectionlayoutgroupcustomitem/frame")


def test_parse_filtered_response_with_any_link_label_and_parenthesized_url() -> None:
    text = search_text("frame", [
        ("frame(width:height:alignment:)", "documentation/SwiftUI/view/frame-widthheightalignment.md",
         FRAME_URL),
        ("Concurrency", "documentation/Swift-Book/LanguageGuide/Concurrency.md", SWIFT_BOOK_URL),
    ], framework="SwiftUI", platform="ios").replace(
        f"[View on Apple Developer]({SWIFT_BOOK_URL})", f"[View on GitHub]({SWIFT_BOOK_URL})")
    hits = ev.parse_search_results(text)
    assert [(h.title, h.url) for h in hits] == [
        ("frame(width:height:alignment:)", FRAME_URL),
        ("Concurrency", SWIFT_BOOK_URL),
    ]


def test_parse_hit_from_a_long_page_with_its_part() -> None:
    # A hit from a page indexed in parts names its part on the Framework line
    text = SERVER_RESPONSE.replace("Framework: AppKit | Type: property\nPath: `documentation/AppKit/"
                                   "nscollectionlayoutvisibleitem",
                                   "Framework: AppKit | Type: property | Part 2 of 3\nPath: `documentation/"
                                   "AppKit/nscollectionlayoutvisibleitem")
    assert text != SERVER_RESPONSE
    assert ev.parse_search_results(text) == ev.parse_search_results(SERVER_RESPONSE)


def test_parse_no_results_response() -> None:
    assert ev.parse_search_results(NO_RESULTS) == []


def test_parse_ignores_header_like_lines_in_a_body() -> None:
    text = SERVER_RESPONSE.replace(
        "**Framework**: AppKit **Kind**: property **Required**: Yes",
        "## 7. Steps\nNot a result header.")
    assert [h.rank for h in ev.parse_search_results(text)] == [1, 2, 3]


@pytest.mark.parametrize("separator", LINE_SEPARATORS)
def test_parse_splits_lines_only_at_newlines(separator: str) -> None:
    text = (SERVER_RESPONSE.replace("## 2. frame (100%)", f"## 2. frame{separator}x (100%)")
            .replace("**Kind**: property **Required**", f"**Kind**: property{separator}**Required**"))
    hits = ev.parse_search_results(text)
    assert [(h.rank, h.title) for h in hits] == [(1, "frame"), (2, f"frame{separator}x"), (3, "frame")]


@pytest.mark.parametrize("text, message", [
    ("", "empty search response"),
    ("Search temporarily unavailable.", "unrecognized search response"),
    ("Search Results: frame\n\n## 1. frame (100%)", "no 'Showing"),
    (SERVER_RESPONSE.replace(
        "Path: `documentation/AppKit/nscollectionlayoutvisibleitem/frame.md`\n", ""),
     r"result 2 \('frame'\) has no 'Path:' line"),
    (SERVER_RESPONSE.replace("Showing 1-3", "Showing 1-4"), r"ranks \[1, 2, 3\].*shows 1-4"),
    (SERVER_RESPONSE.replace("## 2. frame", "## 5. frame"), r"ranks \[1, 5, 3\]"),
    # A link line the parser can't read would drop the url non-Apple expectations
    # match on, so it is an error, never a silent miss
    (SERVER_RESPONSE.replace(
        "[View on Apple Developer](https://developer.apple.com/documentation/appkit/"
        "nscollectionlayoutvisibleitem/frame)\n", ""),
     r"result 2 \('frame'\) has no link line"),
    (SERVER_RESPONSE.replace("[View on Apple Developer](", "Link: <").replace("/frame)\n", "/frame>\n"),
     r"result 1 \('frame'\): unexpected header line 'Link: <https://"),
    (SERVER_RESPONSE.replace("/nscollectionlayoutvisibleitem/frame)", "/nscollectionlayoutvisibleitem/frame )"),
     r"result 2 \('frame'\): unexpected header line '\[View on Apple Developer\]"),
    # A link whose target isn't an absolute http(s) URL could never equal an
    # expected URL: CommonMark's angle-bracket form, and a relative path
    (SERVER_RESPONSE.replace("](https://developer.apple.com/documentation/appkit/nscollectionlayoutvisibleitem",
                             "](<https://developer.apple.com/documentation/appkit/nscollectionlayoutvisibleitem")
     .replace("/nscollectionlayoutvisibleitem/frame)", "/nscollectionlayoutvisibleitem/frame>)"),
     r"result 2 \('frame'\): unexpected header line '\[View on Apple Developer\]\(<https://"),
    (SERVER_RESPONSE.replace("](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes",
                             "](documentation/AppKit/nscollectionviewlayoutattributes"),
     r"result 3 \('frame'\): unexpected header line '\[View on Apple Developer\]\(documentation/"),
    (SERVER_RESPONSE.replace("Type: property\nPath: `documentation/AppKit/nscollectionviewlayoutattributes",
                             "Type: property\nPart 1 of 2\nPath: `documentation/AppKit/"
                             "nscollectionviewlayoutattributes"),
     r"result 3 \('frame'\): unexpected header line 'Part 1 of 2'"),
    (SERVER_RESPONSE.replace("Path: `documentation/AppKit/nscollectionlayoutgroupcustomitem/frame.md`\n",
                             "Path: `documentation/AppKit/nscollectionlayoutgroupcustomitem/frame.md`\n" * 2),
     r"result 1 \('frame'\): unexpected header line 'Path: "),
])
def test_unparseable_responses_raise(text: str, message: str) -> None:
    with pytest.raises(EvalError, match=message):
        ev.parse_search_results(text)


def test_parse_expand_result_names_the_page_by_its_footer() -> None:
    assert ev.parse_expand_result(EXPAND_RESPONSE) == VIEW_PAGE_URL
    # Without the other-frameworks note (a unique name, or framework passed)
    page = EXPAND_RESPONSE.split("\n\n---\nNote: ")[0]
    assert ev.parse_expand_result(page + "\n") == VIEW_PAGE_URL


LONG_PATH = "documentation/AppIntents/entityproperty.md"
FIRST_PART_NOTE = (f"Parts 1-2 of 3 of `{LONG_PATH}`: the page is too long for one response. For the next "
                   "part, pass this file_path with part=3.")
LAST_PART = ("## See Also\n\n- [EntityQuery](entityquery.md)\n\n---\n\n"
             f"*[View on Apple Developer]({VIEW_PAGE_URL})*\n\n---\nPart 3 of 3 of `{LONG_PATH}` (the end of the page).")


def test_parse_expand_result_of_a_page_in_parts_names_it_by_the_last_parts_footer() -> None:
    first = "# EntityProperty\n\n**Framework**: App Intents\n\n## Topics\n\n- [A](a.md)\n\n---\n" + FIRST_PART_NOTE
    assert ev.expand_part(first) == ev.ExpandPart(1, 2, 3, LONG_PATH)
    assert ev.expand_part(LAST_PART) == ev.ExpandPart(3, 3, 3, LONG_PATH)
    assert ev.expand_part(EXPAND_RESPONSE) is None
    # A reply that reaches the last part holds the footer itself
    to_the_end = (f"## Topics\n\n---\n\n*[View on Apple Developer]({VIEW_PAGE_URL})*\n\n---\n"
                  f"Parts 2-3 of 3 of `{LONG_PATH}` (the end of the page).")
    assert ev.expand_part(to_the_end) == ev.ExpandPart(2, 3, 3, LONG_PATH)
    assert ev.parse_expand_result(to_the_end) == VIEW_PAGE_URL
    assert ev.parse_expand_result(first, LAST_PART) == VIEW_PAGE_URL
    # The first part alone has no footer
    with pytest.raises(EvalError, match="names no page"):
        ev.parse_expand_result(first)
    # Followed by the other-frameworks note
    with_note = first + "\nNote: 'EntityProperty' also matches pages in AppKit; showing AppIntents."
    assert ev.expand_part(with_note) == ev.ExpandPart(1, 2, 3, LONG_PATH)
    assert ev.parse_expand_result(with_note, LAST_PART) == VIEW_PAGE_URL
    # A non-Apple doc's front matter starts its first part
    swift = f"---\nurl: {SWIFT_BOOK_URL}\n---\n\n# Concurrency\n\n---\n" + FIRST_PART_NOTE
    assert ev.parse_expand_result(swift, "## Actors\n\n---\nPart 3 of 3 of `x.md` (the end of the page).") == SWIFT_BOOK_URL


def test_parse_expand_result_names_another_doc_by_its_front_matter_url() -> None:
    text = (f"---\nsource: swiftlang/swift-book\nurl: {SWIFT_BOOK_URL}\n---\n\n# Concurrency\n\n"
            "Perform asynchronous operations.\n\n---\nNote: 'Concurrency' also matches pages in "
            "Swift; showing Swift-Book. Pass framework (e.g. framework=\"Swift\") to choose another.")
    assert ev.parse_expand_result(text) == SWIFT_BOOK_URL


@pytest.mark.parametrize("text", [
    "Symbol 'zzqq' not found",
    "Symbol 'zzqq' not found in framework 'SwiftUI'",
    "Symbol 'Lis' not found\n\nSimilar:\n   - List (SwiftUI)",
])
def test_parse_expand_result_symbol_not_found_is_no_page(text: str) -> None:
    assert ev.parse_expand_result(text) is None


@pytest.mark.parametrize("text, message", [
    ("", "empty expand_result response"),
    ("No content available", "names no page .* starting 'No content available'"),
    ("---\nNote: 'View' also matches pages in AppKit; showing AppIntents.", "names no page .* '---'"),
    # A chunk of a large page without its footer can't be named, so it isn't scored
    ("## Topics\n\n- [A](a.md)\n", "names no page .* starting '## Topics'"),
    # The footer must end the page, not sit in its middle
    (EXPAND_RESPONSE.replace("\n\n---\nNote: ", "\n\nMore text.\n\n---\nNote: "), "names no page"),
    # A footer whose target isn't an absolute http(s) URL names no page
    (EXPAND_RESPONSE.replace(f"]({VIEW_PAGE_URL})*", f"](<{VIEW_PAGE_URL}>)*"),
     "names no page .* starting '# view'"),
])
def test_parse_expand_result_without_a_page_url_raises(text: str, message: str) -> None:
    with pytest.raises(EvalError, match=message):
        ev.parse_expand_result(text)


@pytest.mark.parametrize("separator", LINE_SEPARATORS)
def test_parse_expand_result_splits_lines_only_at_newlines(separator: str) -> None:
    text = (EXPAND_RESPONSE.replace("# view\n", f"# view{separator}x\n")
            .replace("static var view", f"static{separator}var view"))
    assert ev.parse_expand_result(text) == VIEW_PAGE_URL
    text = (f"---\nsource: swiftlang/swift-book\nurl: {SWIFT_BOOK_URL}\n---\n\n"
            f"# Concurrency{separator}x\n\nPerform{separator}asynchronous operations.")
    assert ev.parse_expand_result(text) == SWIFT_BOOK_URL
    # A footer must be a line of its own, as footer_url reads it when resolving
    with pytest.raises(EvalError, match="names no page"):
        ev.parse_expand_result(EXPAND_RESPONSE.replace("\n*[View", f"\nSee also{separator}*[View"))


# --- scoring -----------------------------------------------------------------

def test_apple_expectation_matches_the_hit_path_case_insensitively() -> None:
    expectation = Expectation(NAV_URL, frozenset({"documentation/swiftui/navigationstack.md"}))
    assert expectation.matches(Hit(1, "t", "documentation/SwiftUI/NavigationStack.md",
                                   "https://developer.apple.com/documentation/swiftui/x"))
    # Apple pages match by path only: today's generated link can name the URL for another file
    assert not expectation.matches(Hit(1, "t", "documentation/SwiftUI/other.md", NAV_URL))


def test_non_apple_expectation_matches_the_hit_url_exactly() -> None:
    expectation = Expectation(SWIFT_BOOK_URL, frozenset())
    path = "documentation/Swift-Book/LanguageGuide/Concurrency.md"
    assert expectation.matches(Hit(1, "t", path, SWIFT_BOOK_URL))
    assert not expectation.matches(Hit(1, "t", path, SWIFT_BOOK_URL.lower()))
    # The URL generate_url makes from the path when a doc has no front-matter url
    assert not expectation.matches(Hit(
        1, "t", path, "https://developer.apple.com/documentation/swift-book/languageguide/concurrency"))


def test_expand_page_matches_apple_urls_case_insensitively_and_others_exactly() -> None:
    apple = Expectation(NAV_URL, frozenset({"documentation/swiftui/navigationstack.md"}))
    assert apple.matches_page("https://developer.apple.com/documentation/SwiftUI/NavigationStack")
    assert not apple.matches_page("https://developer.apple.com/documentation/swiftui/navigationlink")
    swift_book = Expectation(SWIFT_BOOK_URL, frozenset())
    assert swift_book.matches_page(SWIFT_BOOK_URL)
    assert not swift_book.matches_page(SWIFT_BOOK_URL.lower())


def test_first_match_rank_takes_the_best_ranked_expected_url() -> None:
    hits = [Hit(1, "a", "documentation/A/a.md", "https://developer.apple.com/documentation/a/a"),
            Hit(2, "b", "documentation/B/b.md", "https://developer.apple.com/documentation/b/b"),
            Hit(3, "c", "documentation/C/c.md", SWIFT_BOOK_URL)]
    expectations = [Expectation(SWIFT_BOOK_URL, frozenset()),
                    Expectation(NAV_URL, frozenset({"documentation/b/b.md"}))]
    assert ev.first_match_rank(hits, expectations) == 2
    assert ev.first_match_rank(hits[:1], expectations) is None
    assert ev.first_match_rank([], expectations) is None


def test_hit_at_3_and_mrr() -> None:
    def result(rank: Optional[int]) -> QueryResult:
        return QueryResult(golden(NAV_URL), (), rank)

    results = [result(1), result(3), result(4), result(None)]
    assert [r.hit_at_k for r in results] == [True, True, False, False]
    assert [r.reciprocal_rank for r in results] == [1.0, 1 / 3, 0.25, 0.0]
    hit_rate, mrr = ev.summarize(results)
    assert hit_rate == 0.5
    assert mrr == pytest.approx((1 + 1 / 3 + 0.25) / 4)
    assert ev.summarize([]) == (0.0, 0.0)


# --- MCP client --------------------------------------------------------------

def rpc_reply(request_id: Any, result: Optional[Dict[str, Any]] = None,
              error: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    reply: Dict[str, Any] = {"jsonrpc": "2.0", "id": request_id}
    if error is not None:
        reply["error"] = error
    else:
        reply["result"] = result or {}
    return reply


def sse(*messages: Dict[str, Any]) -> httpx.Response:
    body = "".join(f"event: message\ndata: {json.dumps(m)}\n\n" for m in messages)
    return httpx.Response(200, text=body, headers={"content-type": "text/event-stream"})


def server_sse(message: Dict[str, Any], line_end: str = "\r\n") -> httpx.Response:
    """A reply as the server stack sends it: mcp's compact JSON, which leaves
    U+2028, U+2029 and U+0085 raw, in one sse_starlette event (CRLF line ends)."""
    data = json.dumps(message, ensure_ascii=False, separators=(",", ":"))
    body = f"event: message{line_end}data: {data}{line_end}{line_end}"
    return httpx.Response(200, text=body, headers={"content-type": "text/event-stream"})


Handler = Callable[[httpx.Request], httpx.Response]


class FakeServer:
    """search_apple_docs and expand_result over MCP: initialize, the initialized
    notification, tools/call."""

    def __init__(self, answers: Optional[Dict[str, str]] = None,
                 session_id: Optional[str] = None,
                 expand_answers: Optional[Dict[str, str]] = None) -> None:
        self.answers = answers or {}
        self.expand_answers = expand_answers or {}
        self.session_id = session_id
        self.requests: List[httpx.Request] = []
        self.calls: List[Dict[str, Any]] = []
        self.expand_calls: List[Dict[str, Any]] = []
        self.tools: List[str] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if request.method == "DELETE":
            return httpx.Response(200)
        message = json.loads(request.content)
        method = message["method"]
        if method == "initialize":
            headers = {"mcp-session-id": self.session_id} if self.session_id else {}
            response = sse(
                {"jsonrpc": "2.0", "method": "notifications/message", "params": {"data": "hi"}},
                rpc_reply(message["id"], {"protocolVersion": "2025-06-18",
                                          "serverInfo": {"name": "apple-docs", "version": "9.9"},
                                          "capabilities": {}}))
            response.headers.update(headers)
            return response
        if method == "notifications/initialized":
            return httpx.Response(202)
        assert method == "tools/call"
        name = message["params"]["name"]
        arguments = message["params"]["arguments"]
        self.tools.append(name)
        if name == "expand_result":
            self.expand_calls.append(arguments)
            symbol = arguments["file_path"]
            key = f"{symbol} part={arguments['part']}" if "part" in arguments else symbol
            text = self.expand_answers.get(key, f"Symbol '{symbol}' not found")
        else:
            assert name == "search_apple_docs"
            self.calls.append(arguments)
            text = self.answers.get(arguments["query"], f"No results found for '{arguments['query']}'")
        return httpx.Response(200, json=rpc_reply(
            message["id"], {"content": [{"type": "text", "text": text}], "isError": False}))


def client_for(handler: Handler, api_key: str = "test123") -> McpClient:
    return McpClient("http://eval.test/mcp", api_key, transport=httpx.MockTransport(handler))


def test_client_initializes_and_calls_a_tool() -> None:
    server = FakeServer({"frame": SERVER_RESPONSE}, session_id="s-1")
    with client_for(server) as client:
        client.initialize()
        assert client.server_info == {"name": "apple-docs", "version": "9.9"}
        assert client.call_tool("search_apple_docs", {"query": "frame"}) == SERVER_RESPONSE

    initialize, initialized, call, delete = server.requests
    assert initialize.headers["authorization"] == "Bearer test123"
    assert "text/event-stream" in initialize.headers["accept"]
    assert "mcp-protocol-version" not in initialize.headers
    for later in (initialized, call, delete):
        assert later.headers["mcp-protocol-version"] == "2025-06-18"
        assert later.headers["mcp-session-id"] == "s-1"
    assert delete.method == "DELETE"


def test_client_without_api_key_or_session_sends_neither() -> None:
    server = FakeServer()
    with client_for(server, api_key="") as client:
        client.initialize()
        client.call_tool("search_apple_docs", {"query": "x"})
    assert [r.method for r in server.requests] == ["POST", "POST", "POST"]
    assert all("authorization" not in r.headers and "mcp-session-id" not in r.headers
               for r in server.requests)


def failing(response: Callable[[Dict[str, Any]], httpx.Response]) -> Handler:
    """A server that initializes, then answers tools/call with response(message)."""
    def handler(request: httpx.Request) -> httpx.Response:
        message = json.loads(request.content)
        if message["method"] == "tools/call":
            return response(message)
        return FakeServer()(request)
    return handler


@pytest.mark.parametrize("handler, message", [
    (failing(lambda m: httpx.Response(500, text="Internal Server Error")),
     "HTTP 500 from http://eval.test/mcp for tools/call: Internal Server Error"),
    (failing(lambda m: httpx.Response(429, json={"error": "Rate limit exceeded"})), "HTTP 429"),
    (failing(lambda m: httpx.Response(200, json=rpc_reply(
        m["id"], error={"code": -32602, "message": "Invalid params"}))),
     "tools/call failed: JSON-RPC error .*Invalid params"),
    (failing(lambda m: httpx.Response(200, json=rpc_reply(m["id"], {
        "content": [{"type": "text", "text": "Search temporarily unavailable."}], "isError": True}))),
     "search_apple_docs returned an error: Search temporarily unavailable"),
    (failing(lambda m: httpx.Response(200, json=rpc_reply(m["id"], {"content": []}))),
     "returned no text content"),
    (failing(lambda m: httpx.Response(200, json=rpc_reply(m["id"] + 1, {}))),
     "no JSON-RPC reply to request"),
    (failing(lambda m: httpx.Response(200, text="data: {not json\n\n",
                                      headers={"content-type": "text/event-stream"})),
     "can't parse the reply"),
    (failing(lambda m: httpx.Response(200, text="<html>", headers={"content-type": "text/html"})),
     "unexpected Content-Type 'text/html'"),
])
def test_client_failures_raise(handler: Handler, message: str) -> None:
    with client_for(handler) as client:
        client.initialize()
        with pytest.raises(EvalError, match=message):
            client.call_tool("search_apple_docs", {"query": "x"})


@pytest.mark.parametrize("line_end", ["\r\n", "\n", "\r"])
@pytest.mark.parametrize("separator", ["\u2028", "\u2029", "\u0085"])
def test_sse_data_lines_end_only_at_cr_or_lf(separator: str, line_end: str) -> None:
    text = (SERVER_RESPONSE.replace("## 2. frame (100%)", f"## 2. frame{separator}x (100%)")
            .replace("**Kind**: property **Required**", f"**Kind**: property{separator}**Required**"))

    def handler(request: httpx.Request) -> httpx.Response:
        message = json.loads(request.content)
        if message["method"] == "tools/call":
            return server_sse(rpc_reply(message["id"], {
                "content": [{"type": "text", "text": text}], "isError": False}), line_end)
        return FakeServer()(request)

    with client_for(handler) as client:
        client.initialize()
        reply = client.call_tool("search_apple_docs", {"query": "frame"})
    assert reply == text
    assert [h.title for h in ev.parse_search_results(reply)] == ["frame", f"frame{separator}x", "frame"]


def test_unreachable_server_raises() -> None:
    def refuse(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("Connection refused", request=request)

    with client_for(refuse) as client:
        with pytest.raises(EvalError, match="can't reach http://eval.test/mcp: ConnectError"):
            client.initialize()


def test_failed_initialized_notification_raises() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if json.loads(request.content)["method"] == "notifications/initialized":
            return httpx.Response(400, text="Bad Request")
        return FakeServer()(request)

    with client_for(handler) as client:
        with pytest.raises(EvalError, match="HTTP 400 .* notifications/initialized"):
            client.initialize()


# --- whole runs --------------------------------------------------------------

def golden_file(tmp_path: Path, entries: List[Dict[str, Any]]) -> Path:
    path = tmp_path / "golden.json"
    path.write_text(json.dumps(entries))
    return path


GOLDEN = [
    {"query": "NavigationStack", "framework": "SwiftUI", "expected_top3": [NAV_URL]},
    {"query": "async let", "expected_top3": [SWIFT_BOOK_URL]},
    {"query": "frame", "platform": "ios", "expected_top3": [FRAME_URL]},
]

ANSWERS = {
    "NavigationStack": search_text("NavigationStack", [
        ("NavigationStack", "documentation/SwiftUI/navigationstack.md", NAV_URL)], framework="SwiftUI"),
    "async let": search_text("async let", [
        ("TaskGroup", "documentation/Swift/taskgroup.md",
         "https://developer.apple.com/documentation/swift/taskgroup"),
        # The same file under the URL generate_url makes, which isn't the expected one
        ("Concurrency", "documentation/Swift-Book/LanguageGuide/Concurrency.md",
         "https://developer.apple.com/documentation/swift-book/languageguide/concurrency"),
        ("Concurrency", "documentation/Swift-Book/LanguageGuide/Concurrency.md", SWIFT_BOOK_URL),
        ("Concurrency", "documentation/Swift-Book/LanguageGuide/Concurrency.md", SWIFT_BOOK_URL)]),
}


def test_run_eval_scores_each_query(repo: Path, tmp_path: Path) -> None:
    queries = ev.load_golden(golden_file(tmp_path, GOLDEN))
    expectations = ev.resolve_expectations(queries, repo)
    server = FakeServer(ANSWERS)
    with client_for(server) as client:
        client.initialize()
        results = ev.run_eval(client, queries, expectations)
    assert [r.rank for r in results] == [1, 3, None]
    assert server.calls == [
        {"query": "NavigationStack", "summary_mode": True, "limit": ev.RESULT_LIMIT,
         "token_budget": ev.TOKEN_BUDGET, "framework": "SwiftUI"},
        {"query": "async let", "summary_mode": True, "limit": ev.RESULT_LIMIT,
         "token_budget": ev.TOKEN_BUDGET},
        {"query": "frame", "summary_mode": True, "limit": ev.RESULT_LIMIT,
         "token_budget": ev.TOKEN_BUDGET, "platform": "ios"},
    ]
    report = "\n".join(ev.format_report(results))
    assert "  1 hit  rank  1  RR 1.000  NavigationStack [framework=SwiftUI]" in report
    assert "  3 MISS rank  -  RR 0.000  frame [platform=ios]\n      top 3: (no results)" in report
    assert "hit@3:  2/3 = 0.667" in report
    assert f"MRR@{ev.RESULT_LIMIT}: 0.444" in report


def test_run_eval_names_the_query_whose_response_cannot_be_parsed(repo: Path, tmp_path: Path) -> None:
    queries = ev.load_golden(golden_file(tmp_path, GOLDEN))
    expectations = ev.resolve_expectations(queries, repo)
    server = FakeServer({**ANSWERS, "async let": "Search Results: async let\n\n## 1. x"})
    with client_for(server) as client:
        client.initialize()
        with pytest.raises(EvalError, match="query 'async let': search response has no 'Showing"):
            ev.run_eval(client, queries, expectations)


UIVIEW_URL = "https://developer.apple.com/documentation/uikit/uiview"
STATE_NOTE = ("\n\n---\nNote: 'State' also matches pages in SwiftUI; showing AppIntents. Pass "
              "framework (e.g. framework=\"SwiftUI\") to choose another.")

GOLDEN_EXPAND: List[Dict[str, Any]] = [
    {"query": "NavigationStack", "framework": "SwiftUI", "expected_top3": [NAV_URL], "expand": True},
    {"query": "async let", "expected_top3": [SWIFT_BOOK_URL]},
    {"query": "State", "expected_top3": [STATE_URL], "expand": True},
    {"query": "Concurrency", "expected_top3": [SWIFT_BOOK_URL], "expand": True},
    {"query": "UIView", "expected_top3": [UIVIEW_URL], "expand": True},
]

EXPAND_ANSWERS = {
    # The expected page, named in another case than the expectation
    "NavigationStack": apple_page("NavigationStack", NAV_URL.replace("navigationstack", "NavigationStack")),
    # Another framework's page of that name
    "State": apple_page("State", "https://developer.apple.com/documentation/appintents/state") + STATE_NOTE,
    # A non-Apple doc, named by its front-matter url
    "Concurrency": f"---\nurl: {SWIFT_BOOK_URL}\n---\n\n# Concurrency\n",
    # "UIView": not found
}


def test_run_eval_scores_expand_result_symbol_lookups(repo: Path, tmp_path: Path) -> None:
    queries = ev.load_golden(golden_file(tmp_path, GOLDEN_EXPAND))
    expectations = ev.resolve_expectations(queries, repo)
    server = FakeServer(ANSWERS, expand_answers=EXPAND_ANSWERS)
    with client_for(server) as client:
        client.initialize()
        results = ev.run_eval(client, queries, expectations)

    # Each expand entry's lookup follows its search; the others make none
    assert server.tools == ["search_apple_docs", "expand_result", "search_apple_docs",
                            "search_apple_docs", "expand_result", "search_apple_docs",
                            "expand_result", "search_apple_docs", "expand_result"]
    assert server.expand_calls == [{"file_path": "NavigationStack", "framework": "SwiftUI"},
                                   {"file_path": "State"}, {"file_path": "Concurrency"},
                                   {"file_path": "UIView"}]
    assert [(r.expand_page, r.expand_hit) for r in results] == [
        (NAV_URL.replace("navigationstack", "NavigationStack"), True),
        (None, False),
        ("https://developer.apple.com/documentation/appintents/state", False),
        (SWIFT_BOOK_URL, True),
        (None, False),
    ]
    # The search scores are unchanged by the lookups
    assert [r.rank for r in results] == [1, 3, None, None, None]
    assert ev.summarize_expand(results) == (2, 4)

    report = "\n".join(ev.format_report(results))
    assert "hit@3:  2/5 = 0.400" in report
    assert "expand_result symbol lookups (the page it returns for the query):" in report
    assert ("  1 hit  NavigationStack [framework=SwiftUI] -> "
            "https://developer.apple.com/documentation/swiftui/NavigationStack") in report
    assert "  3 MISS State -> https://developer.apple.com/documentation/appintents/state" in report
    assert f"  4 hit  Concurrency -> {SWIFT_BOOK_URL}" in report
    assert "  5 MISS UIView -> (symbol not found)" in report
    assert "  2 " not in report.split("expand_result symbol lookups")[1]
    assert report.endswith("expand@1: 2/4 = 0.500")


def test_run_eval_reads_the_footer_from_the_last_part_of_a_long_page(repo: Path, tmp_path: Path) -> None:
    nav_path = "documentation/SwiftUI/navigationstack.md"
    queries = ev.load_golden(golden_file(tmp_path, [
        {"query": "NavigationStack", "framework": "SwiftUI", "expected_top3": [NAV_URL], "expand": True}]))
    expectations = ev.resolve_expectations(queries, repo)
    server = FakeServer(ANSWERS, expand_answers={
        "NavigationStack": (f"# NavigationStack\n\n## Topics\n\n---\nParts 1-2 of 3 of `{nav_path}`: the page "
                            "is too long for one response. For the next part, pass this file_path with part=3."),
        f"{nav_path} part=3": (f"## See Also\n\n---\n\n*[View on Apple Developer]({NAV_URL})*\n\n---\n"
                               f"Part 3 of 3 of `{nav_path}` (the end of the page)."),
    })
    with client_for(server) as client:
        client.initialize()
        results = ev.run_eval(client, queries, expectations)
    assert server.expand_calls == [{"file_path": "NavigationStack", "framework": "SwiftUI"},
                                   {"file_path": nav_path, "part": 3}]
    assert [(r.expand_page, r.expand_hit) for r in results] == [(NAV_URL, True)]


def test_report_without_expand_lookups_has_no_expand_section(repo: Path, tmp_path: Path) -> None:
    queries = ev.load_golden(golden_file(tmp_path, GOLDEN))
    expectations = ev.resolve_expectations(queries, repo)
    with client_for(FakeServer(ANSWERS)) as client:
        client.initialize()
        results = ev.run_eval(client, queries, expectations)
    assert "expand" not in "\n".join(ev.format_report(results))


def test_run_eval_names_the_query_whose_expand_result_names_no_page(repo: Path, tmp_path: Path) -> None:
    queries = ev.load_golden(golden_file(tmp_path, GOLDEN_EXPAND))
    expectations = ev.resolve_expectations(queries, repo)
    server = FakeServer(ANSWERS, expand_answers={**EXPAND_ANSWERS, "State": "No content available"})
    with client_for(server) as client:
        client.initialize()
        with pytest.raises(EvalError, match="query 'State': expand_result response names no page"):
            ev.run_eval(client, queries, expectations)


def test_run_eval_waits_between_all_tool_calls(repo: Path, tmp_path: Path,
                                               monkeypatch: pytest.MonkeyPatch) -> None:
    sleeps: List[float] = []
    monkeypatch.setattr(ev.time, "sleep", sleeps.append)
    queries = ev.load_golden(golden_file(tmp_path, GOLDEN_EXPAND))
    expectations = ev.resolve_expectations(queries, repo)
    server = FakeServer(ANSWERS, expand_answers=EXPAND_ANSWERS)
    with client_for(server) as client:
        client.initialize()
        ev.run_eval(client, queries, expectations, delay=4.0)
    assert sleeps == [4.0] * (len(server.tools) - 1)


def test_delay_help_counts_every_tool_call(monkeypatch: pytest.MonkeyPatch,
                                           capsys: pytest.CaptureFixture[str]) -> None:
    """The help is the only description of --delay, so it must name what the
    test above spaces out: expand_result lookups as well as searches."""
    monkeypatch.setenv("COLUMNS", "200")
    with pytest.raises(SystemExit) as exit_info:
        ev.main(["--help"])
    assert exit_info.value.code == 0
    help_text = " ".join(capsys.readouterr().out.split())
    assert ("--delay DELAY seconds between tool calls (searches and expand_result lookups), "
            "for a rate-limited server") in help_text


def test_main_scores_and_saves(repo: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
                               capsys: pytest.CaptureFixture[str]) -> None:
    server = FakeServer(ANSWERS, expand_answers=EXPAND_ANSWERS)
    real_client = ev.McpClient

    def fake_client(url: str, api_key: str, timeout: float) -> McpClient:
        return real_client(url, api_key, timeout, transport=httpx.MockTransport(server))

    monkeypatch.setattr(ev, "McpClient", fake_client)
    saved = tmp_path / "baseline.json"
    status = ev.main(["--repo-root", str(repo), "--golden", str(golden_file(tmp_path, GOLDEN_EXPAND)),
                      "--url", "http://eval.test/mcp", "--save", str(saved)])
    assert status == 0
    out = capsys.readouterr().out
    assert "hit@3:  2/5 = 0.400" in out
    assert "expand@1: 2/4 = 0.500" in out
    data = json.loads(saved.read_text())
    assert data["server"] == {"url": "http://eval.test/mcp", "name": "apple-docs", "version": "9.9"}
    assert (data["queries"], data["hit_at_3"], data["mrr"]) == (5, 0.4, 0.2667)
    assert (data["expand_lookups"], data["expand_hit_at_1"]) == (4, 0.5)
    assert [r["rank"] for r in data["results"]] == [1, 3, None, None, None]
    assert data["results"][1]["top"][2] == {
        "path": "documentation/Swift-Book/LanguageGuide/Concurrency.md", "url": SWIFT_BOOK_URL}
    assert [r.get("expand") for r in data["results"]] == [
        {"page": NAV_URL.replace("navigationstack", "NavigationStack"), "hit": True},
        None,
        {"page": "https://developer.apple.com/documentation/appintents/state", "hit": False},
        {"page": SWIFT_BOOK_URL, "hit": True},
        {"page": None, "hit": False},
    ]


def closed_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port: int = sock.getsockname()[1]
    return port


def test_main_fails_loudly_when_the_server_is_unreachable(
        repo: Path, tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    url = f"http://127.0.0.1:{closed_port()}/mcp"
    with caplog.at_level(logging.ERROR):
        status = ev.main(["--repo-root", str(repo), "--golden", str(golden_file(tmp_path, GOLDEN)),
                          "--url", url, "--timeout", "5"])
    assert status == 1
    assert f"can't reach {url}: ConnectError" in caplog.text


def test_main_fails_before_searching_when_an_expectation_does_not_resolve(
        repo: Path, tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    entries = GOLDEN + [{"query": "gone", "expected_top3": [
        "https://developer.apple.com/documentation/swiftui/missing"]}]
    with caplog.at_level(logging.ERROR):
        status = ev.main(["--repo-root", str(repo), "--golden", str(golden_file(tmp_path, entries)),
                          "--url", f"http://127.0.0.1:{closed_port()}/mcp"])
    assert status == 1
    assert "unresolved expectations" in caplog.text
    assert "can't reach" not in caplog.text


def test_imports_when_mcp_server_scripts_package_comes_first(tmp_path: Path) -> None:
    """mcp-server/scripts is a package too, and a pytest run that collects
    mcp-server/tests first puts mcp-server/ ahead of the repo root on sys.path."""
    code = ("import sys; sys.path[:0] = sys.argv[1:]; import eval_search; "
            "print(eval_search.MetadataExtractor.__module__)")
    env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        [sys.executable, "-c", code, str(ev.REPO_ROOT / "mcp-server"), str(Path(ev.__file__).parent)],
        cwd=tmp_path, env=env, capture_output=True, text=True, timeout=60)
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "metadata_extractor"
