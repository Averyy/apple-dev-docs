#!/usr/bin/env python3
"""Unit tests for MCP server functions."""

import asyncio
import re
import sys
import time
import unittest
from collections import Counter
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, Iterator, List, Optional, Tuple
from unittest.mock import MagicMock, patch

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import apple_docs_mcp
from apple_docs_mcp import (
    EXPAND_FIELDS, EXPAND_TOKEN_CAP, FILE_CHUNKS_LIMIT, cut_text, escape_filter_value,
    estimate_tokens, expand_result, get_file_chunks, search_apple_docs, RateLimitMiddleware,
)


class TestEscapeFilterValue(unittest.TestCase):
    """Test filter value escaping and sanitization."""

    def test_escape_quotes(self):
        """Test escaping double quotes."""
        result = escape_filter_value('test"value')
        self.assertEqual(result, 'test\\"value')

    def test_escape_backslashes(self):
        """Test escaping backslashes."""
        result = escape_filter_value("test\\value")
        self.assertEqual(result, "test\\\\value")

    def test_escape_both(self):
        """Test escaping both quotes and backslashes."""
        result = escape_filter_value('test\\"value')
        self.assertEqual(result, 'test\\\\\\"value')

    def test_max_length_truncation(self):
        """Test that values are truncated to max_length."""
        long_value = "a" * 200
        result = escape_filter_value(long_value, max_length=100)
        self.assertEqual(len(result), 100)

    def test_max_length_default(self):
        """Test default max_length of 100."""
        long_value = "a" * 150
        result = escape_filter_value(long_value)
        self.assertEqual(len(result), 100)

    def test_max_length_none_no_truncation(self):
        """Test max_length=None keeps the whole value (file paths)."""
        long_path = "documentation/" + "a" * 300 + ".md"
        result = escape_filter_value(long_path, max_length=None)
        self.assertEqual(result, long_path)

    def test_control_char_removal(self):
        """Test that control characters are removed."""
        result = escape_filter_value("test\x00\x01\x02value")
        self.assertEqual(result, "testvalue")

    def test_control_char_null_byte(self):
        """Test null byte removal."""
        result = escape_filter_value("before\x00after")
        self.assertEqual(result, "beforeafter")

    def test_newline_removal(self):
        """Test newline removal (control char)."""
        result = escape_filter_value("line1\nline2")
        self.assertNotIn("\n", result)

    def test_tab_removal(self):
        """Test tab removal (control char)."""
        result = escape_filter_value("col1\tcol2")
        self.assertNotIn("\t", result)

    def test_empty_string(self):
        """Test empty string handling."""
        result = escape_filter_value("")
        self.assertEqual(result, "")

    def test_none_handling(self):
        """Test None handling (returns as-is)."""
        result = escape_filter_value(None)
        self.assertIsNone(result)

    def test_normal_framework_name(self):
        """Test normal framework names pass through."""
        result = escape_filter_value("SwiftUI")
        self.assertEqual(result, "SwiftUI")

    def test_framework_with_hyphen(self):
        """Test framework names with hyphens."""
        result = escape_filter_value("Core-Data")
        self.assertEqual(result, "Core-Data")

    def test_unicode_preserved(self):
        """Test that unicode is preserved (printable chars)."""
        result = escape_filter_value("日本語")
        self.assertEqual(result, "日本語")


class TestRateLimitMiddleware(unittest.TestCase):
    """Test rate limiter functionality."""

    def setUp(self):
        """Set up test middleware."""
        self.app = MagicMock()
        self.middleware = RateLimitMiddleware(
            self.app, requests_per_minute=60, api_key="test_key"
        )

    def test_cleanup_stale_entries_removes_old(self):
        """Test that stale entries are removed."""
        now = time.time()
        old_time = now - 120  # 2 minutes ago (outside 60s window)

        # Add some old entries
        self.middleware.request_counts["192.168.1.1"] = [old_time, old_time]
        self.middleware.request_counts["192.168.1.2"] = [old_time]

        # Add a recent entry
        self.middleware.request_counts["192.168.1.3"] = [now - 30]  # 30s ago

        # Run cleanup
        window_start = now - 60
        self.middleware._cleanup_stale_entries(now, window_start)

        # Old IPs should be removed entirely
        self.assertNotIn("192.168.1.1", self.middleware.request_counts)
        self.assertNotIn("192.168.1.2", self.middleware.request_counts)

        # Recent IP should remain
        self.assertIn("192.168.1.3", self.middleware.request_counts)

    def test_cleanup_stale_entries_updates_timestamp(self):
        """Test that cleanup updates last_cleanup timestamp."""
        now = time.time()
        old_cleanup_time = self.middleware._last_cleanup

        self.middleware._cleanup_stale_entries(now, now - 60)

        self.assertEqual(self.middleware._last_cleanup, now)
        self.assertNotEqual(self.middleware._last_cleanup, old_cleanup_time)

    def test_cleanup_interval_default(self):
        """Test default cleanup interval is 5 minutes."""
        self.assertEqual(self.middleware._cleanup_interval, 300)

    def test_check_rate_limit_allows_under_limit(self):
        """Test that requests under limit are allowed.

        _check_rate_limit returns False when request is allowed (not rate limited).
        """
        # First request should always be allowed
        result = self.middleware._check_rate_limit("192.168.1.1")
        self.assertFalse(result)  # False = allowed

    def test_check_rate_limit_blocks_over_limit(self):
        """Test that requests over limit are blocked.

        _check_rate_limit returns True when rate limit is exceeded (should block).
        """
        client_ip = "192.168.1.1"

        # Fill up the rate limit
        now = time.time()
        self.middleware.request_counts[client_ip] = [now] * 60

        # Next request should be blocked
        result = self.middleware._check_rate_limit(client_ip)
        self.assertTrue(result)  # True = blocked

    def test_check_rate_limit_cleans_old_entries(self):
        """Test that old entries are cleaned for current IP."""
        client_ip = "192.168.1.1"
        now = time.time()

        # Add old entries (outside window)
        self.middleware.request_counts[client_ip] = [now - 120, now - 90]

        # Make a new request
        result = self.middleware._check_rate_limit(client_ip)

        # Old entries should be cleaned, new one added
        self.assertEqual(len(self.middleware.request_counts[client_ip]), 1)
        self.assertFalse(result)  # False = allowed (under limit after cleanup)

    def test_is_authenticated_valid(self):
        """Test valid API key is accepted."""
        request = MagicMock()
        request.headers = {"authorization": "Bearer test_key"}

        result = self.middleware._is_authenticated(request)
        self.assertTrue(result)

    def test_is_authenticated_invalid(self):
        """Test invalid API key is rejected."""
        request = MagicMock()
        request.headers = {"authorization": "Bearer wrong_key"}

        result = self.middleware._is_authenticated(request)
        self.assertFalse(result)

    def test_is_authenticated_missing(self):
        """Test missing API key is rejected."""
        request = MagicMock()
        request.headers = {}

        result = self.middleware._is_authenticated(request)
        self.assertFalse(result)

    def test_is_authenticated_wrong_scheme(self):
        """Test wrong auth scheme is rejected."""
        request = MagicMock()
        request.headers = {"authorization": "Basic test_key"}

        result = self.middleware._is_authenticated(request)
        self.assertFalse(result)

    def test_get_client_ip_direct(self):
        """Test getting client IP from direct connection."""
        request = MagicMock()
        request.headers = {}
        request.client.host = "192.168.1.1"

        result = self.middleware._get_client_ip(request)
        self.assertEqual(result, "192.168.1.1")

    def test_get_client_ip_forwarded(self):
        """Test X-Forwarded-For uses the rightmost token (the one Caddy appends)."""
        request = MagicMock()
        request.headers = {"x-forwarded-for": "10.0.0.1, 192.168.1.1"}

        result = self.middleware._get_client_ip(request)
        self.assertEqual(result, "192.168.1.1")


_FILTER_RE = re.compile(r'(\w+) = "((?:[^"\\]|\\.)*)"')
_IN_FILTER_RE = re.compile(r'(\w+) IN \[([^\]]*)\]')
_STARTS_WITH_FILTER_RE = re.compile(r'(\w+) STARTS WITH "((?:[^"\\]|\\.)*)"')
_QUOTED_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')


def _unescape(value: str) -> str:
    return re.sub(r"\\(.)", r"\1", value).lower()


class FakeDocument:
    """A Meilisearch Document: iterable as (key, value) pairs, with no .get()."""

    def __init__(self, data: Dict[str, Any]) -> None:
        self.__dict__.update(data)

    def __iter__(self) -> Iterator[Tuple[str, Any]]:
        return iter(self.__dict__.items())


class FakeIndex:
    """An index's documents, answering the calls the tools make.

    search: the documents whose title or content holds the query (all for ""), in
    list order (their rank), filtered, made distinct and limited; with showRankingScore,
    a hit's _rankingScore is its document's (default 1.0); with facets, the
    facetDistribution of every match. get_documents: the documents the filter matches. A
    filter (=, IN, STARTS WITH, joined by AND) compares values ignoring case, as
    Meilisearch does; as in Meilisearch v1.49, a search fails on a filter value with a
    backslash (it reads the value twice), a documents fetch doesn't.
    """

    def __init__(self, documents: List[Dict[str, Any]]) -> None:
        self.documents = documents
        self.searches: List[Dict[str, Any]] = []
        self.fetches: List[Dict[str, Any]] = []

    @staticmethod
    def _matches(doc: Dict[str, Any], filter_expr: Optional[str]) -> bool:
        expr = filter_expr or ""
        for field, values in _IN_FILTER_RE.findall(expr):
            if str(doc.get(field, "")).lower() not in [_unescape(v) for v in _QUOTED_RE.findall(values)]:
                return False
        for field, value in _STARTS_WITH_FILTER_RE.findall(expr):
            if not str(doc.get(field, "")).lower().startswith(_unescape(value)):
                return False
        for field, value in _FILTER_RE.findall(_IN_FILTER_RE.sub("", expr)):
            if str(doc.get(field, "")).lower() != _unescape(value):
                return False
        return True

    @staticmethod
    def _project(doc: Dict[str, Any], fields: Optional[List[str]]) -> Dict[str, Any]:
        return {k: v for k, v in doc.items() if fields is None or k in fields}

    def search(self, query: str, params: Dict[str, Any]) -> Dict[str, Any]:
        self.searches.append(dict(params, q=query))
        if "\\" in params.get("filter", ""):
            raise Exception("invalid_search_filter: missing the following closing delimiter")
        text = query.lower()
        hits = [d for d in self.documents if self._matches(d, params.get("filter"))
                and (text in d.get("title", "").lower() or text in d.get("content", "").lower())]
        facets = {field: dict(Counter(str(d.get(field)) for d in hits if d.get(field) is not None))
                  for field in params.get("facets", [])}
        if params.get("distinct"):
            seen = set()
            unique = []
            for doc in hits:
                if doc.get(params["distinct"]) not in seen:
                    seen.add(doc.get(params["distinct"]))
                    unique.append(doc)
            hits = unique
        hits = hits[:params.get("limit", 20)]
        projected = [self._project(d, params.get("attributesToRetrieve")) for d in hits]
        if params.get("showRankingScore"):
            for hit, doc in zip(projected, hits):
                hit["_rankingScore"] = doc.get("_rankingScore", 1.0)
        return {"hits": projected, **({"facetDistribution": facets} if facets else {})}

    def get_documents(self, params: Dict[str, Any]) -> SimpleNamespace:
        self.fetches.append(dict(params))
        matches = [d for d in self.documents if self._matches(d, params.get("filter"))]
        limit = params.get("limit", 20)
        return SimpleNamespace(
            results=[FakeDocument(self._project(d, params.get("fields"))) for d in matches[:limit]],
            total=len(matches), offset=0, limit=limit)


def page_documents(file_path: str, pieces: List[str], title: str = "Concurrency",
                   framework: str = "Swift-Book", kind: str = "article",
                   index_gen: Optional[str] = None) -> List[Dict[str, Any]]:
    """The documents the indexer makes of one file: one per piece (chunk), stamped with
    the run's index_gen when given (an index built before it has none)."""
    return [{"id": f"{abs(hash(file_path))}_chunk_{i}", "title": title, "api_name": title,
             "framework": framework, "kind": kind, "overview": "", "file_path": file_path,
             "url": "https://example.com/" + file_path, "content": piece,
             "chunk_index": i, "total_chunks": len(pieces),
             **({"index_gen": index_gen} if index_gen else {})}
            for i, piece in enumerate(pieces)]


PATH = "documentation/Swift-Book/LanguageGuide/Concurrency.md"
# Three ~9K-token parts: together over EXPAND_TOKEN_CAP, any two under it
LONG_BODIES = [f"word{i} " * 6000 + "\n" for i in range(3)]
LONG_PIECES = [f"## Section {i}\n\n" + body for i, body in enumerate(LONG_BODIES)]


class ToolTestCase(unittest.TestCase):
    """Runs the tools against a FakeIndex."""

    def use_index(self, documents: List[Dict[str, Any]]) -> FakeIndex:
        index = FakeIndex(documents)
        for name, value in (("meili_index", index), ("ensure_meilisearch_connection", lambda: True)):
            patcher = patch.object(apple_docs_mcp, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        return index


class TestSearchDistinct(ToolTestCase):
    """search_apple_docs returns one hit per file, showing which part of a long page matched."""

    def test_one_result_per_file_with_its_part(self) -> None:
        pieces = ["# Concurrency\n\nasync let intro\n", "## Async let\n\nasync let details\n",
                  "## Actors\n\nasync let and actors\n"]
        chunks = page_documents(PATH, pieces)
        task = page_documents("documentation/Swift/task.md", ["# Task\n\nasync let child tasks\n"],
                              title="Task", framework="Swift", kind="struct")
        # Chunk 1 ranks best, so it is the page's hit
        index = self.use_index([chunks[1], chunks[0], task[0], chunks[2]])

        result = search_apple_docs("async let", summary_mode=True)

        self.assertEqual(index.searches[0]["distinct"], "file_path")
        self.assertIn("chunk_index", index.searches[0]["attributesToRetrieve"])
        self.assertIn("total_chunks", index.searches[0]["attributesToRetrieve"])
        paths = re.findall(r"^Path: `([^`]+)`$", result, re.MULTILINE)
        self.assertEqual(sorted(paths), sorted([PATH, "documentation/Swift/task.md"]))
        self.assertIn("Showing 1-2 of 2 results", result)
        self.assertRegex(result, r"(?m)^Framework: Swift-Book \| Type: article \| Part 2 of 3$")
        # A page indexed as one document has no part
        self.assertRegex(result, r"(?m)^Framework: Swift \| Type: struct$")


ALL_PLATFORMS = ["iOS", "iPadOS", "Mac Catalyst", "macOS", "tvOS", "visionOS", "watchOS"]


def symbol_doc(file_path: str, title: str, framework: str = "UIKit", kind: str = "class",
               rank: float = 1.0, api_name: Optional[str] = None, url: Optional[str] = None,
               platforms: Optional[List[str]] = None) -> Dict[str, Any]:
    """One single-document page, with the _rankingScore a search gives it."""
    return {"id": str(abs(hash(file_path))), "title": title,
            "api_name": api_name if api_name is not None else title.split("(")[0],
            "framework": framework, "kind": kind, "overview": f"About {title}.", "file_path": file_path,
            "url": url or "https://developer.apple.com/" + file_path, "content": f"# {title}\n",
            "chunk_index": 0, "total_chunks": 1, "_rankingScore": rank,
            **({"platforms": platforms} if platforms is not None else {})}


def result_titles(result: str) -> List[str]:
    """The titles of a search_apple_docs result list, in rank order (without their %)."""
    return re.findall(r"(?m)^## \d+\. (.*) \(\d+%\)$", result)


class TestLinkLabels(ToolTestCase):
    """A result's link is labelled by its URL's host."""

    def test_label_names_the_host(self) -> None:
        self.assertEqual(apple_docs_mcp.link_label("https://developer.apple.com/documentation/swiftui/text"),
                         "View on Apple Developer")
        self.assertEqual(apple_docs_mcp.link_label("https://github.com/swiftlang/swift-book/blob/main/x.md"),
                         "View on GitHub")
        self.assertEqual(apple_docs_mcp.link_label("https://www.github.com/a"), "View on GitHub")
        self.assertEqual(apple_docs_mcp.link_label("https://ml-explore.github.io/mlx/build/html/index.html"),
                         "View on ml-explore.github.io")
        self.assertEqual(apple_docs_mcp.link_label("not a url"), "View on source")

    def test_search_results_carry_the_label(self) -> None:
        mlx = "https://ml-explore.github.io/mlx/build/html/python/array.html"
        self.use_index([symbol_doc("documentation/MLX/python/array.md", "array", "MLX", url=mlx),
                        symbol_doc("documentation/Swift/array.md", "Array", "Swift", kind="struct",
                                   url="https://developer.apple.com/documentation/swift/array")])
        result = search_apple_docs("array", summary_mode=True)
        self.assertIn(f"[View on ml-explore.github.io]({mlx})", result)
        self.assertIn("[View on Apple Developer](https://developer.apple.com/documentation/swift/array)", result)


class TestRanking(ToolTestCase):
    """Results are ordered by Meilisearch's _rankingScore plus exact-title boosts."""

    def test_meilisearch_order_decides_without_a_title_match(self) -> None:
        self.use_index([symbol_doc("documentation/A/b.md", "Second", rank=0.8),
                        symbol_doc("documentation/A/a.md", "First", rank=0.9)])
        # Neither title is the query: the higher _rankingScore comes first
        self.assertEqual(result_titles(search_apple_docs("s", summary_mode=True)), ["First", "Second"])

    def test_the_title_asked_for_beats_methods_meilisearch_scores_alike(self) -> None:
        methods = [symbol_doc(f"documentation/AVFoundation/delegate/urlsession-{i}.md",
                              f"urlSession(_:task{i}:)", "AVFoundation", kind="method") for i in range(3)]
        lower = symbol_doc("documentation/X/y/urlsession.md", "urlsession", "X", kind="property")
        session = symbol_doc("documentation/Foundation/urlsession.md", "URLSession", "Foundation")
        self.use_index(methods + [lower, session])
        titles = result_titles(search_apple_docs("URLSession", summary_mode=True))
        # Exact case, then any case, then the functions of that name
        self.assertEqual(titles[:2], ["URLSession", "urlsession"])
        self.assertEqual(sorted(titles[2:]), sorted(m["title"] for m in methods))

    def test_a_function_of_that_name_beats_a_better_scored_mention(self) -> None:
        article = symbol_doc("documentation/SwiftUI/animating-views.md", "Animating views with withAnimation",
                             "SwiftUI", kind="article", rank=0.95)
        function = symbol_doc("documentation/SwiftUI/withanimation.md", "withAnimation(_:_:)", "SwiftUI",
                              kind="function", rank=0.9)
        self.use_index([article, function])
        self.assertEqual(result_titles(search_apple_docs("withAnimation", summary_mode=True)),
                         ["withAnimation(_:_:)", "Animating views with withAnimation"])

    def test_scores_stay_between_0_and_1(self) -> None:
        exact = apple_docs_mcp.calculate_relevance_score({"title": "Text", "_rankingScore": 1.0}, "Text")
        self.assertEqual(exact, 1.0)
        self.assertEqual(apple_docs_mcp.calculate_relevance_score({"title": "Other", "_rankingScore": 1.0}, "Text"),
                         0.8)
        self.assertEqual(apple_docs_mcp.calculate_relevance_score({"title": "Other"}, "Text"), 0.0)

    def test_a_query_naming_the_framework_matches_the_title(self) -> None:
        swiftui = symbol_doc("documentation/SwiftUI/button.md", "Button", "SwiftUI", kind="struct", rank=0.94)
        article = symbol_doc("documentation/WidgetKit/swiftui-views.md", "SwiftUI views for widgets",
                             "WidgetKit", kind="article", rank=0.98)
        uikit = symbol_doc("documentation/UIKit/button.md", "Button", "UIKit", kind="property", rank=0.95)
        self.use_index([dict(doc, content="Button SwiftUI") for doc in (article, uikit, swiftui)])
        result = search_apple_docs("Button SwiftUI", summary_mode=True)
        # SwiftUI's Button: its title is the rest of the query, which beats UIKit's Button,
        # a symbol only named by one word of the query (named_symbol_boost)
        paths = re.findall(r"^Path: `([^`]+)`$", result, re.MULTILINE)
        self.assertEqual(paths, [swiftui["file_path"], uikit["file_path"], article["file_path"]])
        self.assertIn("## 1. Button (95%)", result)
        self.assertIn("## 2. Button (86%)", result)

    def test_a_query_naming_the_framework_in_several_words(self) -> None:
        container = symbol_doc("documentation/CoreData/nspersistentcontainer.md", "NSPersistentContainer",
                               "CoreData", rank=0.96)
        article = symbol_doc("documentation/CoreData/loading-a-feed.md", "Loading and displaying a large data feed",
                             "CoreData", kind="article", rank=0.99)
        self.use_index([dict(doc, content="Core Data NSPersistentContainer") for doc in (article, container)])
        titles = result_titles(search_apple_docs("Core Data NSPersistentContainer", summary_mode=True))
        self.assertEqual(titles, ["NSPersistentContainer", "Loading and displaying a large data feed"])

    def test_without_framework_words(self) -> None:
        rest = apple_docs_mcp.without_framework_words
        self.assertEqual(rest("Core Data NSPersistentContainer", "CoreData"), "NSPersistentContainer")
        self.assertEqual(rest("MLModel Core ML", "CoreML"), "MLModel")
        self.assertEqual(rest("App Intents AppShortcutsProvider", "AppIntents"), "AppShortcutsProvider")
        self.assertEqual(rest("Button SwiftUI", "SwiftUI"), "Button")
        self.assertEqual(rest("ML Stable Diffusion pipeline", "ml-stable-diffusion"), "pipeline")
        # Only whole words that spell the whole name, in order; all of the query if nothing is left
        self.assertEqual(rest("Core Animation CALayer", "CoreData"), "Core Animation CALayer")
        self.assertEqual(rest("Data Core stack", "CoreData"), "Data Core stack")
        self.assertEqual(rest("CoreDataStack", "CoreData"), "CoreDataStack")
        self.assertEqual(rest("Core Data", "CoreData"), "Core Data")
        self.assertEqual(rest("Button", ""), "Button")

    def test_a_page_titled_with_the_question_keeps_its_boost(self) -> None:
        overview = symbol_doc("documentation/coremltools/source/overview-coremltools.md", "What Is Core ML Tools?",
                              "coremltools", kind="article", rank=0.99)
        faqs = symbol_doc("documentation/coremltools/source/faqs.md", "Core ML Tools FAQs", "coremltools",
                          kind="article", rank=0.995)
        index = self.use_index([dict(doc, content="Core ML Tools") for doc in (faqs, overview)])
        for question in ("What Is Core ML Tools?", "What Is Core ML Tools"):
            result = search_apple_docs(question, summary_mode=True)
            # The question words aren't searched for, but the title is still the query asked
            self.assertEqual(index.searches[-1]["q"], "Core ML Tools")
            self.assertEqual(result_titles(result), ["What Is Core ML Tools?", "Core ML Tools FAQs"])

    def test_equal_scores_go_shortest_path_first(self) -> None:
        override = symbol_doc("documentation/UIKit/uisplitviewcontroller/viewdidload.md", "viewDidLoad()",
                              kind="method")
        base = symbol_doc("documentation/UIKit/uiviewcontroller/viewdidload.md", "viewDidLoad()", kind="method")
        self.use_index([override, base])
        result = search_apple_docs("viewDidLoad", summary_mode=True)
        paths = re.findall(r"^Path: `([^`]+)`$", result, re.MULTILINE)
        self.assertEqual(paths, [base["file_path"], override["file_path"]])

    def test_equal_scores_in_two_frameworks_go_to_the_page_on_more_platforms(self) -> None:
        # The same class in two frameworks: the whole path would favor the shorter directory name
        js = symbol_doc("documentation/tvmljs/userdefaults.md", "UserDefaults", "tvmljs", platforms=["tvOS"])
        foundation = symbol_doc("documentation/Foundation/userdefaults.md", "UserDefaults", "Foundation",
                                platforms=ALL_PLATFORMS)
        # Within a framework the shorter path still comes first, whatever the platforms
        member = symbol_doc("documentation/tvmljs/a/userdefaults.md", "UserDefaults", "tvmljs",
                            platforms=ALL_PLATFORMS)
        self.use_index([js, member, foundation])
        result = search_apple_docs("UserDefaults", summary_mode=True)
        paths = re.findall(r"^Path: `([^`]+)`$", result, re.MULTILINE)
        self.assertEqual(paths, [foundation["file_path"], js["file_path"], member["file_path"]])

    def test_a_type_past_the_top_matches_joins_them(self) -> None:
        # Meilisearch ranks every page titled "data" alike, in index order: the top matches
        # are all properties, and Foundation's Data comes after them
        properties = [symbol_doc(f"documentation/AVFAudio/class{i}/data.md", "data", "AVFAudio", kind="property")
                      for i in range(100)]
        data = symbol_doc("documentation/Foundation/data.md", "Data", "Foundation", kind="struct")
        index = self.use_index(properties + [data])
        result = search_apple_docs("Data", summary_mode=True)
        self.assertEqual(result_titles(result)[:2], ["Data", "data"])
        self.assertIn("Showing 1-10 of 101 results (ranked from the top 100 matches and the types named 'Data')\n",
                      result)
        types = index.searches[1]
        self.assertEqual((types["q"], types["filter"], types["limit"], types["distinct"]),
                         ("Data", f'api_name = "Data" AND {apple_docs_mcp.TYPE_KINDS_FILTER}',
                          apple_docs_mcp.SYMBOL_CANDIDATES, "file_path"))
        # The search's filters apply to the types too
        index.searches.clear()
        search_apple_docs("Data", framework="AVFAudio", summary_mode=True)
        self.assertEqual(index.searches[1]["filter"],
                         f'framework = "AVFAudio" AND api_name = "Data" AND {apple_docs_mcp.TYPE_KINDS_FILTER}')
        # A query of several words is no name; top matches that weren't cut hold every match
        index = self.use_index([dict(doc, content="data stream") for doc in properties] + [data])
        search_apple_docs("data stream", summary_mode=True)
        search_apple_docs("Data", framework="Foundation", summary_mode=True)
        self.assertEqual(len(index.searches), 2)

    def test_a_lowercase_name_matches_titles_in_any_case(self) -> None:
        # "color" says nothing about case: every page titled so gets the exact boost, and
        # the more general page comes first (the type at its framework's root, then the one
        # on more platforms), not the color properties Meilisearch ranks alike
        properties = [symbol_doc(f"documentation/AppKit/nscolorwell{i}/color.md", "color", "AppKit",
                                 kind="property", platforms=["macOS"]) for i in range(3)]
        color = symbol_doc("documentation/SwiftUI/color.md", "Color", "SwiftUI", kind="struct",
                           platforms=ALL_PLATFORMS)
        self.use_index(properties + [color])
        result = search_apple_docs("color", summary_mode=True)
        self.assertEqual(result_titles(result), ["Color", "color", "color", "color"])
        self.assertIn("## 1. Color (100%)", result)
        # A name with a capital still asks for that case: the other case comes after it
        self.assertEqual(apple_docs_mcp.title_boost("color", "Color"), apple_docs_mcp.TITLE_NOCASE_BOOST)
        self.assertEqual(apple_docs_mcp.title_boost("Color", "color"), apple_docs_mcp.TITLE_EXACT_BOOST)
        self.assertEqual(apple_docs_mcp.title_boost("urlSession", "URLSession"), apple_docs_mcp.TITLE_NOCASE_BOOST)

    def test_a_symbol_named_by_one_word_of_the_query(self) -> None:
        # "Concurrency Task": Meilisearch ranks the articles holding both words first, while
        # the query names the Task struct
        article = symbol_doc("documentation/Swift-Book/LanguageGuide/Concurrency.md", "Concurrency",
                             "Swift-Book", kind="article", rank=0.99)
        task = symbol_doc("documentation/Swift/task.md", "Task", "Swift", kind="struct", rank=0.9)
        tasks = symbol_doc("documentation/Swift/taskgroup.md", "TaskGroup", "Swift", kind="struct", rank=0.95)
        self.use_index([dict(doc, content="Concurrency Task") for doc in (article, tasks, task)])
        result = search_apple_docs("Concurrency Task", summary_mode=True)
        self.assertEqual(result_titles(result), ["Task", "Concurrency", "TaskGroup"])
        self.assertIn("## 1. Task (82%)", result)
        score = apple_docs_mcp.calculate_relevance_score
        boosted = {"title": "Task", "api_name": "Task", "kind": "struct", "_rankingScore": 1.0}
        self.assertEqual(score(boosted, "async Task"), 0.9)
        # Not an article (its api_name is its title), not a word without a capital (a
        # lowercase word names properties of hundreds of types), not a one-word query (the
        # title boosts decide it), and only the name as typed
        self.assertEqual(score(dict(boosted, kind="article"), "async Task"), 0.8)
        self.assertEqual(score(dict(boosted, api_name="task", title="task"), "async task"), 0.8)
        self.assertEqual(score(dict(boosted, title="Task.init"), "Task"), 0.8)
        self.assertEqual(score(boosted, "async TASK"), 0.8)
        # A title boost isn't added to
        self.assertEqual(score(dict(boosted, framework="Swift"), "Swift Task"), 1.0)
        # A capital that may only start the sentence names no symbol ("Color picker in
        # SwiftUI" asks for ColorPicker, not Color), unless another capital follows it or
        # the query is no sentence ("Color SwiftUI", "Button SwiftUI": every word a name)
        color = {"title": "Color", "api_name": "Color", "kind": "struct", "_rankingScore": 1.0}
        self.assertEqual(score(color, "Color picker in SwiftUI"), 0.8)
        self.assertEqual(score(color, "Color picker", "Color picker?"), 0.8)
        self.assertEqual(score(color, "SwiftUI Color picker"), 0.9)
        self.assertEqual(score(color, "Color SwiftUI"), 0.9)
        self.assertEqual(score(dict(boosted, title="Error", api_name="Error"), "Error handling Swift"), 0.8)
        self.assertEqual(score(boosted, "Task async"), 0.8)
        view = {"title": "NavigationView", "api_name": "NavigationView", "kind": "struct", "_rankingScore": 1.0}
        self.assertEqual(score(view, "NavigationView navigationBarTitle"), 0.9)
        self.assertEqual(score(dict(view, api_name="URLSession", title="URLSession"), "URLSession delegate"), 0.9)

    def test_relevance_threshold_applies_to_the_new_score(self) -> None:
        self.use_index([symbol_doc("documentation/A/a.md", "Text", rank=1.0),
                        symbol_doc("documentation/A/b.md", "Text views", rank=0.5)])
        result = search_apple_docs("Text", summary_mode=True, relevance_threshold=0.9)
        self.assertEqual(result_titles(result), ["Text"])
        self.assertIn("(100%)", result)


class TestQuestionQueries(ToolTestCase):
    """A question is searched without its question and function words."""

    def test_question_terms(self) -> None:
        terms = apple_docs_mcp.question_terms
        self.assertEqual(terms("What is NavigationStack?", "What is NavigationStack"), "NavigationStack")
        self.assertEqual(terms("How do I present a sheet in SwiftUI?", "How do I present a sheet in SwiftUI"),
                         "present sheet SwiftUI")
        self.assertEqual(terms("What’s new in SwiftUI?", "What’s new in SwiftUI"), "new SwiftUI")
        # Without a question mark: a question word first, and another of the words
        self.assertEqual(terms("what is a LanguageModelSession", "what is a LanguageModelSession"),
                         "LanguageModelSession")
        self.assertEqual(terms("how do I present a sheet", "how do I present a sheet"), "present sheet")
        # ...so a title that starts with a question word is searched as it is
        for title in ("What’s New", "Whose Test Constants", "How SwiftUI works"):
            self.assertEqual(terms(title, title), title)
        # Swift keywords in a plain query stay
        for query in ("is operator", "do catch", "for in loop", "where clause", "if let"):
            self.assertEqual(terms(query, query), query)
        # A one-word query, and a question of only such words, are searched as they are
        self.assertEqual(terms("What?", "What?"), "What?")
        self.assertEqual(terms("What is it?", "What is it"), "What is it")

    def test_search_sends_the_subject(self) -> None:
        index = self.use_index([symbol_doc("documentation/SwiftUI/navigationstack.md", "NavigationStack",
                                           "SwiftUI", kind="struct")])
        result = search_apple_docs("What is NavigationStack?", summary_mode=True)
        self.assertEqual(index.searches[0]["q"], "NavigationStack")
        self.assertIn("Search Results: What is NavigationStack?", result)
        self.assertEqual(result_titles(result), ["NavigationStack"])
        search_apple_docs("What’s New", summary_mode=True)
        self.assertEqual(index.searches[-1]["q"], "What’s New")


class TestWildcards(ToolTestCase):
    """A pattern with a literal prefix is matched against every name starting with it."""

    NAMES = ["UIView", "UIViewController", "UINavigationController", "UITableViewController",
             "UIAlertController", "UIButton"]

    def uikit(self) -> List[Dict[str, Any]]:
        return [symbol_doc(f"documentation/UIKit/{name.lower()}.md", name) for name in self.NAMES] + \
            [symbol_doc("documentation/AppKit/nsviewcontroller.md", "NSViewController", "AppKit")]

    def test_infix_pattern_lists_names_by_prefix(self) -> None:
        index = self.use_index(self.uikit())
        result = search_apple_docs("UI*Controller", summary_mode=True)
        self.assertEqual(index.fetches[0]["filter"], 'api_name STARTS WITH "UI"')
        self.assertEqual(index.fetches[0]["limit"], apple_docs_mcp.WILDCARD_NAME_LIMIT)
        # Closest fit first: the pattern's 12 literal characters make up most of the shortest name
        self.assertEqual(result_titles(result), ["UIViewController", "UIAlertController",
                                                 "UITableViewController", "UINavigationController"])
        self.assertIn("## 1. UIViewController (75%)", result)
        self.assertIn("Showing 1-4 of 4 results\n", result)
        # A listed name's result shows what a search hit shows, fetched by its path
        self.assertIn("Framework: UIKit | Type: class\nPath: `documentation/UIKit/uiviewcontroller.md`\n"
                      "[View on Apple Developer](https://developer.apple.com/documentation/UIKit/"
                      "uiviewcontroller.md)\n\nAbout UIViewController.", result)
        details = index.searches[-1]
        self.assertEqual(details["q"], "")
        self.assertIn('file_path IN ["documentation/UIKit/uiviewcontroller.md", ', details["filter"])

    def test_prefix_pattern_ranks_the_exact_name_first(self) -> None:
        self.use_index(self.uikit())
        result = search_apple_docs("UIView*", summary_mode=True)
        self.assertEqual(result_titles(result)[:2], ["UIView", "UIViewController"])
        self.assertIn("## 2. UIViewController (37%)", result)

    def test_names_in_the_patterns_case_come_first(self) -> None:
        uid = symbol_doc("documentation/Kit/thing/uid.md", "uid", "Kit", kind="property")
        self.use_index(self.uikit() + [uid, symbol_doc("documentation/UIKit/uikey.md", "UIKey")])
        titles = result_titles(search_apple_docs("UI*", summary_mode=True))
        # The shortest names first, but the one in another case after every name in the pattern's
        self.assertEqual(titles[:3], ["UIKey", "UIView", "UIButton"])
        self.assertEqual(titles[-1], "uid")
        # A pattern all in lower case says nothing about case: the closest fit first, in
        # any case (uid is shortest), and UIKey before uikitextension, which a lowercase
        # name preference would put first
        extension = symbol_doc("documentation/Kit/thing/uikitextension.md", "uikitextension", "Kit", kind="property")
        self.use_index(self.uikit() + [uid, extension, symbol_doc("documentation/UIKit/uikey.md", "UIKey")])
        lower = result_titles(search_apple_docs("ui*", summary_mode=True))
        self.assertEqual(lower[:5], ["uid", "UIKey", "UIView", "UIButton", "uikitextension"])
        # The case orders the names but leaves their relevance alone: a name fits a pattern
        # in another case as closely, and a threshold keeps it
        for pattern in ("UIView*", "uiview*", "uiView*"):
            result = search_apple_docs(pattern, summary_mode=True, relevance_threshold=0.9)
            self.assertEqual(result_titles(result), ["UIView"])
            self.assertIn("## 1. UIView (100%)", result)

    def test_filters_apply_to_the_listed_names(self) -> None:
        index = self.use_index(self.uikit())
        result = search_apple_docs("*View*", framework="AppKit", summary_mode=True)
        self.assertEqual(index.fetches, [])  # no literal prefix: only the top matches are filtered
        self.assertEqual(result_titles(result), ["NSViewController"])
        search_apple_docs("NS*Controller", framework="AppKit", summary_mode=True)
        self.assertEqual(index.fetches[0]["filter"], 'framework = "AppKit" AND api_name STARTS WITH "NS"')

    def test_too_many_names_says_so(self) -> None:
        self.use_index(self.uikit())
        with patch.object(apple_docs_mcp, "WILDCARD_NAME_LIMIT", 2):
            result = search_apple_docs("UI*", summary_mode=True)
        self.assertIn("(matched against the first 2 of the 6 names starting with 'UI')", result)

    def test_cut_top_matches_say_so_beside_the_listed_names(self) -> None:
        # A nested type is titled by its qualified name but named by its own: only the top
        # matches hold it, and they were cut
        members = [symbol_doc(f"documentation/Combine/publishers/m{i}.md", f"Publishers.M{i}", "Combine",
                              kind="struct", api_name=f"M{i}") for i in range(150)]
        publisher = symbol_doc("documentation/Combine/publisher.md", "Publisher", "Combine", kind="protocol")
        self.use_index(members + [publisher])
        # No name starts with 'Publishers.': only the top matches
        self.assertIn("Showing 1-10 of 100 results (ranked from the top 100 matches)\n",
                      search_apple_docs("Publishers.*", summary_mode=True))
        self.assertIn("Showing 1-10 of 101 results (ranked from the top 100 matches and every name "
                      "starting with 'Pub')\n", search_apple_docs("Pub*", summary_mode=True))
        with patch.object(apple_docs_mcp, "WILDCARD_NAME_LIMIT", 0):
            result = search_apple_docs("Pub*", summary_mode=True)
        self.assertIn("Showing 1-10 of 100 results (ranked from the top 100 matches and the first 0 of the 1 "
                      "names starting with 'Pub')\n", result)

    def test_no_results_tips_fit_the_pattern(self) -> None:
        self.use_index(self.uikit())
        # Every name starting with 'UI' was matched already: the filter or the spelling
        result = search_apple_docs("UI*Controller", platform="macos", summary_mode=True)
        self.assertTrue(result.endswith(
            "Suggestions:\n"
            "   - Check the spelling, or use fewer literal characters (the pattern is matched against the API "
            "names starting with 'UI')\n"
            "   - Try without platform filter"))
        result = search_apple_docs("*Qq", framework="UIKit", summary_mode=True)
        self.assertTrue(result.endswith(
            "Suggestions:\n"
            "   - Try a pattern that starts with 2+ literal characters (e.g., UIView*, UI*Controller)\n"
            "   - Try without framework filter"))
        self.assertTrue(search_apple_docs("Qqq", platform="ios").endswith(
            "   - Use wildcards: Button* or NSTable*\n   - Try without platform filter"))


class TestSymbolLookup(ToolTestCase):
    """expand_result's symbol lookup chooses among exact-name types, exact-name pages and the top matches."""

    def test_candidates_come_from_three_searches(self) -> None:
        index = self.use_index([symbol_doc("documentation/Foundation/data.md", "Data", "Foundation", kind="struct")])
        apple_docs_mcp.symbol_candidates("Data", "Foundation")
        filters = [s.get("filter") for s in index.searches]
        kinds = ", ".join(f'"{k}"' for k in apple_docs_mcp.TYPE_KINDS)
        self.assertEqual(filters, [f'framework = "Foundation" AND api_name = "Data" AND kind IN [{kinds}]',
                                   'framework = "Foundation" AND api_name = "Data"',
                                   'framework = "Foundation"'])
        for search in index.searches:
            self.assertEqual((search["limit"], search["distinct"]), (apple_docs_mcp.SYMBOL_CANDIDATES, "file_path"))
        # Without a framework, the pages named so also give every framework they're in
        index.searches.clear()
        candidates, frameworks = apple_docs_mcp.symbol_candidates("Data")
        self.assertEqual([s.get("facets") for s in index.searches], [None, ["framework"], None])
        self.assertEqual(([c["file_path"] for c in candidates], frameworks),
                         (["documentation/Foundation/data.md"], ["Foundation"]))

    def test_a_name_or_framework_with_a_backslash_is_never_filtered_on(self) -> None:
        # A search can't filter on a backslash (Meilisearch reads the value twice), and no
        # page has one: the name is searched for without the api_name filters
        index = self.use_index([symbol_doc("documentation/Foundation/data.md", "Data", "Foundation", kind="struct")])
        self.assertEqual(expand_result("key\\"), "Symbol 'key\\' not found")
        self.assertEqual([(s["q"], s.get("filter")) for s in index.searches], [("key\\", None)])
        index.searches.clear()
        self.assertEqual(expand_result("Data", framework="Foundation\\"),
                         "Symbol 'Data' not found in framework 'Foundation\\'")
        self.assertEqual(search_apple_docs("Data", framework="Foundation\\").splitlines()[0],
                         "No results found for 'Data'")
        self.assertEqual(search_apple_docs("Data", platform="ios\\").splitlines()[0], "No results found for 'Data'")
        self.assertEqual(index.searches, [])

    def test_a_type_found_past_the_top_matches(self) -> None:
        # Meilisearch ranks every page named "data" alike: the top matches are all properties
        properties = [symbol_doc(f"documentation/AVFAudio/class{i}/data.md", "data", "AVFAudio", kind="property")
                      for i in range(apple_docs_mcp.SYMBOL_CANDIDATES)]
        data = symbol_doc("documentation/Foundation/data.md", "Data", "Foundation", kind="struct")
        index = self.use_index(properties + [data])
        result = expand_result("Data")
        self.assertEqual(index.fetches[-1]["filter"], 'file_path = "documentation/Foundation/data.md"')
        self.assertTrue(result.startswith("# Data\n"))

    def test_pick_prefers_types_then_short_titles_then_short_paths(self) -> None:
        pick = apple_docs_mcp.pick_symbol
        text_property = symbol_doc("documentation/AVFoundation/avcaption/ruby/text.md", "Text", "AVFoundation",
                                   kind="property")
        text_struct = symbol_doc("documentation/SwiftUI/text.md", "Text", "SwiftUI", kind="struct")
        self.assertIs(pick([text_property, text_struct], "Text"), text_struct)
        # Even when nothing else tells them apart: the same title, path within the
        # framework and platforms, the member first among the candidates
        article = symbol_doc("documentation/HIG/settings.md", "Settings", "HIG", kind="article",
                             platforms=ALL_PLATFORMS)
        settings = symbol_doc("documentation/SwiftUI/settings.md", "Settings", "SwiftUI", kind="struct",
                              platforms=ALL_PLATFORMS)
        self.assertIs(pick([article, settings], "Settings"), settings)
        # The simplest overload, even on the longer path
        overload = symbol_doc("documentation/SwiftUI/withanimation-2.md",
                              "withAnimation(_:completionCriteria:_:completion:)", "SwiftUI", kind="function")
        simplest = symbol_doc("documentation/SwiftUI/view/withanimation.md", "withAnimation(_:_:)", "SwiftUI",
                              kind="function")
        self.assertIs(pick([overload, simplest], "withAnimation"), simplest)
        override = symbol_doc("documentation/AppKit/nssplitviewcontroller/viewdidload.md", "viewDidLoad()",
                              "AppKit", kind="method")
        base = symbol_doc("documentation/UIKit/uiviewcontroller/viewdidload.md", "viewDidLoad()", kind="method")
        self.assertIs(pick([override, base], "viewDidLoad"), base)
        # The same path within two frameworks: the page on more platforms, whatever the
        # frameworks' directory names
        appkit = symbol_doc("documentation/AppKit/nsviewcontroller/viewdidload.md", "viewDidLoad()", "AppKit",
                            kind="method", platforms=["macOS"])
        uikit = dict(base, platforms=["iOS", "iPadOS", "Mac Catalyst", "tvOS", "visionOS"])
        self.assertIs(pick([appkit, uikit], "viewDidLoad"), uikit)
        js = symbol_doc("documentation/tvmljs/userdefaults.md", "UserDefaults", "tvmljs", platforms=["tvOS"])
        foundation = symbol_doc("documentation/Foundation/userdefaults.md", "UserDefaults", "Foundation",
                                platforms=ALL_PLATFORMS)
        self.assertIs(pick([js, foundation], "UserDefaults"), foundation)
        # An exact-case title before a case-insensitive one, even a type's
        lower = symbol_doc("documentation/X/list.md", "list", "X", kind="struct")
        exact = symbol_doc("documentation/SwiftUI/list.md", "List", "SwiftUI", kind="property")
        self.assertIs(pick([lower, exact], "List"), exact)
        self.assertIsNone(pick([lower], "Grid"))

    def test_ambiguity_note_names_at_most_8_frameworks(self) -> None:
        others = [symbol_doc(f"documentation/Kit{i}/view.md", "view", f"Kit{i}", kind="property") for i in range(10)]
        self.use_index([symbol_doc("documentation/SwiftUI/view.md", "View", "SwiftUI", kind="protocol")] + others)
        result = expand_result("View")
        named = ", ".join(sorted(f"Kit{i}" for i in range(10))[:8])
        self.assertTrue(result.endswith(f"Note: 'View' also matches pages in {named} and 2 more; showing SwiftUI. "
                                        "Pass framework (e.g. framework=\"Kit0\") to choose another."))

    def test_ambiguity_note_names_frameworks_past_the_candidates(self) -> None:
        # More pages named init than candidates, all from one framework: the note still
        # names the others
        inits = [symbol_doc(f"documentation/ARKit/type{i}/init.md", "init()", "ARKit", kind="init") for i in range(3)]
        inits += [symbol_doc(f"documentation/Kit{i}/type/init.md", "init()", f"Kit{i}", kind="init") for i in range(2)]
        self.use_index(inits)
        with patch.object(apple_docs_mcp, "SYMBOL_CANDIDATES", 2):
            result = expand_result("init")
        self.assertTrue(result.startswith("# init()\n"))
        self.assertTrue(result.endswith("Note: 'init' also matches pages in Kit0, Kit1; showing ARKit. "
                                        "Pass framework (e.g. framework=\"Kit0\") to choose another."))


class TestExpandResult(ToolTestCase):
    """expand_result returns the whole page (every chunk), in parts when it is too long."""

    def test_path_returns_every_chunk_joined_in_order(self) -> None:
        pieces = ["# Concurrency\n\nIntro.\n", "## Tasks\n\nTask text.\n",
                  "## Actors\n\nActor text.\n\n---\n\n*[View on Apple Developer](https://example.com/c)*"]
        chunks = page_documents(PATH, pieces)
        index = self.use_index([chunks[2], chunks[0], chunks[1]])

        self.assertEqual(expand_result(PATH), "\n".join(pieces))
        self.assertEqual(index.searches, [])
        self.assertEqual(index.fetches, [{"filter": f'file_path = "{PATH}"', "fields": EXPAND_FIELDS,
                                          "limit": FILE_CHUNKS_LIMIT}])

    def test_fetches_again_when_a_file_has_more_chunks_than_the_first_fetch(self) -> None:
        pieces = ["# A\n", "## B\n", "## C\n"]
        index = self.use_index(page_documents(PATH, pieces))
        with patch.object(apple_docs_mcp, "FILE_CHUNKS_LIMIT", 2):
            self.assertEqual(expand_result(PATH), "\n".join(pieces))
        self.assertEqual([fetch["limit"] for fetch in index.fetches], [2, 3])

    def test_keeps_one_file_when_the_filter_matches_another_casing(self) -> None:
        upper = page_documents("documentation/X/Foo.md", ["# Foo\n", "## Upper\n"])
        lower = page_documents("documentation/X/foo.md", ["# foo lower\n"])
        self.use_index(upper + lower)
        self.assertEqual(expand_result("documentation/X/foo.md"), "# foo lower\n")
        self.assertEqual(expand_result("documentation/X/Foo.md"), "# Foo\n\n## Upper\n")
        # Neither casing asked for: one file's documents, never a mix
        self.assertEqual(expand_result("documentation/X/FOO.md"), "# Foo\n\n## Upper\n")

    def test_page_over_the_cap_comes_in_parts(self) -> None:
        self.use_index(page_documents(PATH, LONG_PIECES))
        self.assertGreater(estimate_tokens("\n".join(LONG_PIECES)), EXPAND_TOKEN_CAP)
        first_two = "\n".join(LONG_PIECES[:2])

        # Each reply holds its part and as many of the next ones as fit
        first = expand_result(PATH)
        self.assertEqual(first, first_two + f"\n\n---\nParts 1-2 of 3 of `{PATH}`: the page is too long "
                         "for one response. For the next part, pass this file_path with part=3.")
        self.assertEqual(expand_result(PATH, part=1),
                         first_two + f"\n\n---\nParts 1-2 of 3 of `{PATH}`. For the next part, pass "
                         "this file_path with part=3.")
        self.assertEqual(expand_result(PATH, part=2),
                         "\n".join(LONG_PIECES[1:]) + f"\n\n---\nParts 2-3 of 3 of `{PATH}` (the end of the page).")
        self.assertEqual(expand_result(PATH, part=3),
                         LONG_PIECES[2] + f"\n\n---\nPart 3 of 3 of `{PATH}` (the end of the page).")
        self.assertEqual(expand_result(PATH, part=4), f"No part 4: `{PATH}` has 3 parts.")
        for part in (1, 2, 3):
            self.assertLessEqual(estimate_tokens(expand_result(PATH, part=part)), EXPAND_TOKEN_CAP)

    def test_reading_the_parts_as_their_notes_say_gives_the_page(self) -> None:
        # Parts of every size, with relative links: each reply holds whole parts, its links
        # made search hints as in the whole page, and the replies joined are the page
        sizes = [300, 5000, 9000, 2000, 12000, 30000, 40000, 100, 47000, 800]
        pieces = [f"## Section {i}\n\nSee [Next](section-{i + 1}.md) and "
                  "[Apple](https://developer.apple.com/x).\n\n" + "x" * size + "\n"
                  for i, size in enumerate(sizes)]
        self.use_index(page_documents(PATH, pieces))
        page = apple_docs_mcp.transform_internal_links("\n".join(pieces))
        self.assertGreater(estimate_tokens(page), EXPAND_TOKEN_CAP)
        self.assertIn("Next (-> search: section 1)", page)

        texts: List[str] = []
        notes: List[str] = []
        part = 0
        while True:
            reply = expand_result(PATH, part=part)
            self.assertLessEqual(estimate_tokens(reply), EXPAND_TOKEN_CAP + 60)
            text, note = reply.split("\n\n---\n")
            self.assertNotRegex(text, r"\]\([^)]*\.md\)")
            texts.append(text)
            notes.append(note.split(" of `")[0])
            follow = re.search(r"part=(\d+)\.$", note)
            if not follow:
                self.assertTrue(note.endswith(f"of 10 of `{PATH}` (the end of the page)."))
                break
            part = int(follow.group(1))
        self.assertEqual("\n".join(texts), page)
        # Whole parts packed under the cap (~80,000 characters): 3 replies, not 10
        self.assertEqual(notes, ["Parts 1-6 of 10", "Parts 7-8 of 10", "Parts 9-10 of 10"])

    def test_whole_page_links_become_search_hints(self) -> None:
        pieces = ["# Concurrency\n\nSee [Task](../Swift/task.md).\n", "## Actors\n\n[Actor](actor.md)\n"]
        self.use_index(page_documents(PATH, pieces))
        self.assertEqual(expand_result(PATH), "# Concurrency\n\nSee Task (-> search: .. Swift task).\n\n"
                         "## Actors\n\nActor (-> search: actor)\n")

    def test_part_of_a_page_that_fits(self) -> None:
        pieces = ["# Concurrency\n\nIntro.\n", "## Tasks\n\nTask text.\n"]
        self.use_index(page_documents(PATH, pieces))
        self.assertEqual(expand_result(PATH), "\n".join(pieces))
        self.assertEqual(expand_result(PATH, part=-1), "\n".join(pieces))
        self.assertEqual(expand_result(PATH, part=1),
                         "\n".join(pieces) + f"\n\n---\nParts 1-2 of 2 of `{PATH}` (the end of the page).")
        self.assertEqual(expand_result(PATH, part=2),
                         pieces[1] + f"\n\n---\nPart 2 of 2 of `{PATH}` (the end of the page).")

    def test_part_1_of_a_one_document_page_is_the_page(self) -> None:
        self.use_index(page_documents(PATH, ["# Concurrency\n\nAll of it.\n"]))
        self.assertEqual(expand_result(PATH, part=1), "# Concurrency\n\nAll of it.\n")
        self.assertEqual(expand_result(PATH, part=2), f"No part 2: `{PATH}` has 1 part.")

    def test_oversized_part_is_cut_to_the_cap(self) -> None:
        # An index built before the chunk size held everywhere has longer chunks
        pieces = ["# Lapack\n", "## Functions\n\n```c\n" + "dsyevr_ " * 20000, "## See Also\n"]
        self.use_index(page_documents(PATH, pieces))
        # The part before it doesn't take it in
        self.assertEqual(expand_result(PATH), f"# Lapack\n\n\n---\nPart 1 of 3 of `{PATH}`: the page is too "
                         "long for one response. For the next part, pass this file_path with part=2.")
        result = expand_result(PATH, part=2)
        self.assertLessEqual(estimate_tokens(result), EXPAND_TOKEN_CAP + 60)
        self.assertIn("```\n\n[Truncated: this part is longer than one response allows.]", result)
        self.assertEqual(result.count("```") % 2, 0)
        self.assertTrue(result.endswith(f"Part 2 of 3 of `{PATH}`. For the next part, pass this file_path "
                                        "with part=3."))

    def test_sections_come_from_the_joined_text(self) -> None:
        # A section too long for one chunk continues in the next, with no heading of its own
        pieces = ["# Concurrency\n\n## Overview\n\nOverview text.\n\n## Topics\n\nfirst half\n",
                  "second half\n", "## See Also\n\nelsewhere\n"]
        self.use_index(page_documents(PATH, pieces))
        result = expand_result(PATH, sections=["topics"])
        self.assertEqual(result, "# Concurrency\n\n## Topics\nfirst half\n\nsecond half\n")
        # part pages the full text only
        self.assertEqual(expand_result(PATH, sections=["topics"], part=3), result)

    def test_sections_output_is_capped(self) -> None:
        pieces = ["# Concurrency\n\n## Topics\n\n" + LONG_BODIES[0]] + LONG_BODIES[1:]
        self.use_index(page_documents(PATH, pieces))
        result = expand_result(PATH, sections=["topics"])
        self.assertIn("word1", result)  # the section goes on into the next chunk
        self.assertLessEqual(estimate_tokens(result), EXPAND_TOKEN_CAP + 60)
        self.assertTrue(result.endswith("\n\n[Truncated to fit one response. Read the whole page in parts: "
                                        f"expand_result(file_path=\"{PATH}\", part=1).]\n"))

    def test_symbol_lookup_returns_the_whole_page_of_its_best_chunk(self) -> None:
        button = page_documents("documentation/SwiftUI/button.md", ["# Button\n\nA control.\n", "## Topics\n"],
                                title="Button", framework="SwiftUI", kind="struct")
        appkit = page_documents("documentation/AppKit/button.md", ["# Button\n\nAn AppKit one.\n"],
                                title="Button", framework="AppKit", kind="property")
        index = self.use_index([button[1], button[0], appkit[0]])

        result = expand_result("Button")

        self.assertEqual(index.searches[0]["distinct"], "file_path")
        self.assertNotIn("content", index.searches[0]["attributesToRetrieve"])
        self.assertEqual(index.fetches[0]["filter"], 'file_path = "documentation/SwiftUI/button.md"')
        self.assertEqual(result, "# Button\n\nA control.\n\n## Topics\n\n\n---\nNote: 'Button' also matches "
                         "pages in AppKit; showing SwiftUI. Pass framework (e.g. framework=\"AppKit\") "
                         "to choose another.")

    def test_symbol_lookup_of_a_long_page_notes_its_part_before_the_framework_note(self) -> None:
        button = page_documents("documentation/SwiftUI/button.md", LONG_PIECES, title="Button",
                                framework="SwiftUI", kind="struct")
        appkit = page_documents("documentation/AppKit/button.md", ["# Button\n"], title="Button",
                                framework="AppKit", kind="property")
        self.use_index(button + appkit)
        result = expand_result("Button")
        self.assertEqual(result, "\n".join(LONG_PIECES[:2]) + "\n\n---\nParts 1-2 of 3 of "
                         "`documentation/SwiftUI/button.md`: the page is too long for one response. For the "
                         "next part, pass this file_path with part=3.\nNote: 'Button' also matches pages in "
                         "AppKit; showing SwiftUI. Pass framework (e.g. framework=\"AppKit\") to choose another.")

    def test_keeps_the_newest_index_run_of_a_file(self) -> None:
        # Between an update's adds and its sweep (or after a run that stopped before it),
        # a changed file has the old run's documents its new ones didn't replace by id
        old, new = "20261016T070000000000Z", "20261019T070000000000Z"
        shrunk = page_documents(PATH, ["# New\n", "## Tasks\n"], index_gen=new) + \
            page_documents(PATH, ["# Old\n", "## Tasks\n", "## Old actors\n"], index_gen=old)[2:]
        self.use_index(shrunk)
        self.assertEqual(expand_result(PATH), "# New\n\n## Tasks\n")
        self.assertEqual(expand_result(PATH, part=3), f"No part 3: `{PATH}` has 2 parts.")

        # One document that became several (other ids), and the reverse
        chunked = page_documents(PATH, ["# Old, whole\n"], index_gen=old) + \
            page_documents(PATH, ["# New\n", "## More\n"], index_gen=new)
        self.use_index(chunked)
        self.assertEqual(expand_result(PATH), "# New\n\n## More\n")
        unchunked = page_documents(PATH, ["# Old\n", "## Gone\n"], index_gen=old) + \
            page_documents(PATH, ["# New, whole\n"], index_gen=new)
        self.use_index(unchunked)
        self.assertEqual(expand_result(PATH, part=1), "# New, whole\n")

        # Documents from an index built before index_gen are older than any stamped ones
        legacy = page_documents(PATH, ["# Legacy\n", "## A\n", "## B\n"]) + \
            page_documents(PATH, ["# New\n"], index_gen=new)
        self.use_index(legacy)
        self.assertEqual(expand_result(PATH), "# New\n")

    def test_file_not_found(self) -> None:
        self.use_index(page_documents(PATH, ["# Concurrency\n"]))
        self.assertEqual(expand_result("documentation/X/none.md"), "File not found: documentation/X/none.md")

    def test_path_length_is_counted_as_meilisearch_and_the_indexer_count_it(self) -> None:
        # Normalized (NFKD, lowercased): 'ﬁ' is 3 bytes but 'fi' (2) to Meilisearch, which
        # indexes such a path (the indexer's check passes it), and 'É' is 2 bytes but 'é'
        # decomposed (3), past the limit, so the indexer leaves that file out
        index = self.use_index([])
        ligatures = "documentation/X/" + "\ufb01" * 150 + ".md"
        self.assertGreater(len(ligatures.encode("utf-8")), apple_docs_mcp.MAX_FILTER_VALUE_BYTES)
        self.assertEqual(expand_result(ligatures), f"File not found: {ligatures}")
        self.assertEqual(len(index.fetches), 1)
        accents = "documentation/X/" + "\u00c9" * 150 + ".md"
        self.assertLessEqual(len(accents.encode("utf-8")), apple_docs_mcp.MAX_FILTER_VALUE_BYTES)
        with self.assertRaisesRegex(apple_docs_mcp.ToolError, r"file_path is too long \(469 bytes; max 468\)"):
            expand_result(accents)
        self.assertEqual(len(index.fetches), 1)

    def test_backend_failure_is_a_tool_error(self) -> None:
        class MeilisearchApiError(Exception):
            pass

        index = self.use_index([])
        failing = MagicMock(side_effect=MeilisearchApiError("index_not_found"))
        with patch.object(index, "get_documents", failing), self.assertRaises(apple_docs_mcp.ToolError):
            expand_result(PATH)
        self.assertEqual(failing.call_count, 1)  # an API error isn't retried


class TestToolDescriptions(unittest.TestCase):
    """What clients are told: FastMCP publishes a docstring's text before Args, and each
    parameter's Args entry (not its Returns section)."""

    @staticmethod
    def published() -> Dict[str, Any]:
        tools = asyncio.run(apple_docs_mcp.mcp.list_tools())
        return {tool.name: tool.to_mcp_tool() for tool in tools}

    def test_search_says_one_result_per_page_with_its_part(self) -> None:
        description = self.published()["search_apple_docs"].description
        self.assertIn("Returns one result per page", description)
        self.assertIn("'Part 3 of 6'", description)

    def test_expand_describes_parts(self) -> None:
        expand = self.published()["expand_result"]
        self.assertIn("comes in parts", expand.description)
        self.assertIn("'Parts 1-4 of 12 of `<path>`'", expand.description)
        part = expand.inputSchema["properties"]["part"]
        self.assertEqual((part["type"], part["default"]), ("integer", 0))
        self.assertIn("Part of a long page to start from", part["description"])


class TestRetries(ToolTestCase):
    """safe_get_documents retries like safe_search."""

    def test_get_documents_retries_a_transient_failure(self) -> None:
        class MeilisearchCommunicationError(Exception):
            pass

        index = self.use_index(page_documents(PATH, ["# Concurrency\n"]))
        fetch = index.get_documents
        calls: List[int] = []

        def flaky(params: Dict[str, Any]) -> SimpleNamespace:
            calls.append(1)
            if len(calls) == 1:
                raise MeilisearchCommunicationError("connection reset")
            return fetch(params)

        with patch.object(index, "get_documents", flaky), \
                patch.object(apple_docs_mcp, "init_meilisearch", lambda: True), \
                patch.object(apple_docs_mcp.time, "sleep"):
            chunks = get_file_chunks(PATH)
        self.assertEqual([c["content"] for c in chunks], ["# Concurrency\n"])
        self.assertEqual(len(calls), 2)


class TestCutText(unittest.TestCase):
    """cut_text closes a code block its cut leaves open."""

    def test_closes_an_open_code_block(self) -> None:
        self.assertEqual(cut_text("intro\n```swift\nlet x = 1\nlet y = 2\n", 25), "intro\n```swift\nlet x = 1\n```")

    def test_keeps_a_closed_code_block(self) -> None:
        self.assertEqual(cut_text("```\nx\n```\nmore text", 9), "```\nx\n```")

    def test_nothing_left(self) -> None:
        self.assertEqual(cut_text("text", -5), "")


if __name__ == "__main__":
    unittest.main()
