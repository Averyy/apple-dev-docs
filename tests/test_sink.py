"""The DocC site, the sinks and the D6 modules (1.1 + D6).

Step 1a (a refactor with no new behavior):
- site.DocCSite: one site's URLs; APPLE gives the Apple scraper, the naming
  and the links every URL they use, and the scraper builds each from its site;
- sink.Sink: one docs dir and its hash file with this run's state for its
  pages; a framework job's primary sink is its own dir and hash file;
- sink.SinkRegistry: one sink per site and dir (in any casing), created on
  first use; a run's jobs share one, and a top-level sink's hash manager
  leaves memory once no job in flight uses it.

Step 1b (the behavior), through whole scrape.py runs against a fake Apple:
- the reference resolver (references[id].url, fragments stripped) and the
  scope rule (the job's framework, or the page's bundle; never by substring);
- routing: a module's pages go to its own dir and hash file (metadata.module,
  the parent's child_modules), a same-bundle sibling's page to the sibling's
  sink (a handoff, one hop; metadata.handoff_from), deduplicated per sink,
  with the page's links for every job that reaches it;
- the multi-writer end of run (finish_run) and the D6 removal rules 1–5:
  a module unlinked by its only parent goes after 2 clean runs, one with
  another parent stays, a deleted or renamed parent is pruned, a renamed or
  promoted module, a protected failure or a parent unlisted for one run
  deletes nothing, the subset runs never clean a module whose other parent
  didn't run; the namespace_collision check; the stale error entries
  (section anchors, item 8) leave through the normal cleanup.

Item 2 (1.4): a protocol requirement's default implementations
(defaultImplementationsSections) are crawled like its other links: its own
framework's, a module's, and a same-bundle sibling's (a handoff), each
removed by its sink's normal orphan cleanup once no longer listed.

Item 3 (1.5, D1): the pages only a page's Objective-C/C variant curates (its
occ variantOverrides) are crawled through its occ view, built once per page
with the patched references and shared with its conversion, which lists them
in their occ groups; an occ view that can't be built is a local error that
still queues the links its operations list.

Batch 7 B4-a: an overload group's page (externalID ending in ::OverloadGroup)
links its other overloads (otherDeclarations), each crawled and saved as a
page of its own, kept while the group lists it and removed by the normal
orphan cleanup once it doesn't; an overload's own page links none of its
siblings (nor the preferred overload, whose page is a copy of the group's).
"""

import asyncio
import dataclasses
import hashlib
import json
import os
import re
import shutil
import sys
from collections import deque
from pathlib import Path
from typing import Any, Deque, Dict, Iterator, List, Optional, Sequence, Set, Tuple
from unittest import mock
from urllib.parse import unquote

import httpx
import pytest
from structlog.testing import capture_logs
from structlog.typing import EventDict

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts', 'utilities')))

import scrape_all_frameworks
from cleanup_orphans_at_end import MODULE_UNLINKED_RUNS, remove_framework
from scraper import json_scraper
from scraper.base import FetchFailed
from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper, OccViewError, PageLink
from scraper.sink import Sink, SinkRegistry
from scraper.site import APPLE, DocCSite
from scraper.utils.hash_manager import COUNTER_FIELDS
from scraper.utils.naming import DOC_URL_PREFIX, JSON_URL_PREFIX, page_path
from tests.test_failure_policy import FW, SITE, Apple, FrameworkList, Runs, Site, file_of, routes_for, sandbox_runs
from tests.test_fetch_results import Spec, doc_url, json_url, ok, status

EXAMPLE = DocCSite(
    name="example",
    site_url="https://docs.example.org",
    doc_base="https://docs.example.org/documentation",
    json_base="https://docs.example.org/data/documentation",
    bundle_prefix="doc://org.example.",
)


@pytest.fixture
def dirs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(Config, "OUTPUT_DIR", tmp_path / "documentation")
    monkeypatch.setattr(Config, "CACHE_DIR", tmp_path / ".hashes")
    return tmp_path


def write_hash_file(name: str, hashes: Dict[str, Dict[str, Any]]) -> Path:
    path = Config.CACHE_DIR / f"{name}_hashes.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"metadata": {}, "hashes": hashes}))
    return path


def loaded(sink: Sink) -> bool:
    """Whether a sink's hash manager is in memory."""
    return sink.loaded


class TestDocCSite:
    def test_apple_is_every_apple_url(self) -> None:
        assert APPLE.doc_prefix == DOC_URL_PREFIX == "https://developer.apple.com/documentation/"
        assert APPLE.json_prefix == JSON_URL_PREFIX == "https://developer.apple.com/tutorials/data/documentation/"
        assert AppleJSONDocumentationScraper.JSON_BASE_URL == APPLE.json_base
        assert (Config.BASE_URL, Config.DOCUMENTATION_URL) == (APPLE.site_url, APPLE.doc_base)

    def test_urls(self) -> None:
        assert APPLE.doc_url("swiftui/view") == "https://developer.apple.com/documentation/swiftui/view"
        assert APPLE.url("/documentation/swiftui/view") == "https://developer.apple.com/documentation/swiftui/view"
        assert APPLE.is_own_identifier("doc://com.apple.SwiftUI/documentation/SwiftUI/View")
        assert not APPLE.is_own_identifier("doc://org.swift.docc/documentation/DocC")
        assert EXAMPLE.doc_url("kit/a") == "https://docs.example.org/documentation/kit/a"
        assert EXAMPLE.json_prefix == "https://docs.example.org/data/documentation/"

    def test_a_site_is_frozen(self) -> None:
        with pytest.raises(dataclasses.FrozenInstanceError):
            APPLE.site_url = "https://example.com"  # type: ignore[misc]

    def test_the_scraper_builds_every_url_from_its_site(self, dirs: Path) -> None:
        """No literal Apple URL: the conversions, references, doc:// literals and the
        bundle test of the Topics fallback all follow the scraper's site."""
        scraper = AppleJSONDocumentationScraper("Kit")
        assert scraper.site is APPLE
        assert scraper.root_json_url == f"{APPLE.json_prefix}Kit.json"
        scraper.site = EXAMPLE
        assert scraper._convert_json_url_to_doc_url(f"{EXAMPLE.json_prefix}kit/a.json") == f"{EXAMPLE.doc_prefix}kit/a"
        assert scraper._convert_doc_url_to_json_url(f"{EXAMPLE.doc_prefix}kit/a") == f"{EXAMPLE.json_prefix}kit/a.json"
        assert scraper._convert_identifier_to_json_url("doc://org.example.kit/documentation/Kit/A") == (
            f"{EXAMPLE.json_prefix}kit/a.json")
        assert scraper._reference_url("/documentation/kit/a") == f"{EXAMPLE.doc_prefix}kit/a"
        assert scraper._reference_url("https://other.example/x") == "https://other.example/x"
        assert scraper._rewrite_doc_literals("See doc://org.example.kit/documentation/Kit/A.") == (
            f"See {EXAMPLE.doc_prefix}Kit/A.")
        groups = scraper._topic_groups(
            [{"title": "Topics", "identifiers": ["doc://org.example.kit/documentation/Kit/B", "doc://com.apple.x/documentation/X"]}],
            {},
        )
        assert [item["url"] for item in groups[0]["items"]] == [
            f"{EXAMPLE.doc_prefix}Kit/B", "doc://com.apple.x/documentation/X"]


class TestSink:
    def test_a_sink_is_its_dir_and_hash_file(self, dirs: Path) -> None:
        live = f"{APPLE.json_prefix}testkit/a.json"
        write_hash_file("TestKit", {
            live: {"hash": "h", "file_path": "documentation/TestKit/a.md"},
            f"{APPLE.doc_prefix}testkit/a": {"hash": "h", "file_path": "documentation/TestKit/a.md"},
            f"{APPLE.json_prefix}testkit/gone.json": {"status": "error", "error": "HTTP 404"},
        })
        sink = Sink(APPLE, "TestKit", "Test Kit", {"swiftui": "SwiftUI"}, 7)
        assert (sink.site, sink.dir_name, sink.framework_name) == (APPLE, "TestKit", "Test Kit")
        assert sink.output_dir == Config.OUTPUT_DIR / "TestKit"
        assert sink.hash_manager.cache_file == Config.CACHE_DIR / "TestKit_hashes.json"
        assert sink.hash_manager.output_dir == sink.output_dir and sink.hash_manager.render_version == 7
        assert live in sink.hash_manager.hashes
        # Only the live JSON-URL entries count as known pages
        assert sink.known_pages == 1
        assert sink.known_dirs == {"swiftui": "SwiftUI", "testkit": "TestKit"}
        converter = sink.markdown_converter
        assert converter.output_dir == sink.output_dir and converter.known_dirs == sink.known_dirs
        assert (sink.processed_urls, sink.fetch_failures, sink.fetch_ok, sink.gone) == (set(), {}, set(), set())
        assert (sink.local_errors, sink.saved_ok, sink.path_owner_map) == ({}, set(), None)
        # The docs dir is created on the first file write only
        assert not sink.output_dir.exists()

    def test_the_primary_sink_is_the_frameworks_own(self, dirs: Path) -> None:
        """The framework's docs dir, hash file (its casing) and title, which its pages name."""
        write_hash_file("TestKit", {})
        scraper = AppleJSONDocumentationScraper("testkit", "Test Kit")
        sink = scraper.sink
        assert scraper.framework_id == sink.dir_name == "TestKit" and sink.framework_name == "Test Kit"
        assert scraper.hash_manager is sink.hash_manager
        assert scraper.output_dir == sink.output_dir == Config.OUTPUT_DIR / "TestKit"
        assert scraper.markdown_converter is sink.markdown_converter
        page = {"metadata": {"title": "A"}, "references": {}}
        data = scraper._extract_from_json(sink, page, f"{APPLE.doc_prefix}testkit/a", None)
        assert (data["framework"], data["framework_id"]) == ("Test Kit", "TestKit")
        assert scraper._get_organized_file_path(sink, f"{APPLE.doc_prefix}testkit/a", {}) == sink.output_dir / "a.md"


class TestSinkRegistry:
    def test_one_sink_per_site_and_dir_in_any_casing(self, dirs: Path) -> None:
        sinks = SinkRegistry({"swiftui": "SwiftUI"})
        sink = sinks.get(APPLE, "TestKit", "Test Kit", 1)
        assert sinks.get(APPLE, "testkit", "testkit", 2) is sink
        assert (sink.dir_name, sink.framework_name, sink.hash_manager.render_version) == ("TestKit", "Test Kit", 1)
        assert sinks.get(APPLE, "OtherKit", "Other Kit", 1) is not sink
        assert sinks.get(EXAMPLE, "TestKit", "Test Kit", 1) is not sink
        assert sink.known_dirs == {"swiftui": "SwiftUI", "testkit": "TestKit"}

    def test_scrapers_share_the_runs_sinks(self, dirs: Path) -> None:
        sinks = SinkRegistry({"swiftui": "SwiftUI"})
        scraper = AppleJSONDocumentationScraper("TestKit", sinks=sinks)
        assert scraper.sinks is sinks and sinks.get(APPLE, "testkit", "x", 1) is scraper.sink
        assert scraper.sink.known_dirs == {"swiftui": "SwiftUI", "testkit": "TestKit"}
        # On its own, a scraper has its own sinks, which know no other dir
        alone = AppleJSONDocumentationScraper("TestKit")
        assert alone.sinks is not sinks and alone.sink is not scraper.sink
        assert alone.sink.known_dirs == {"testkit": "TestKit"}

    def test_release_saves_and_drops_the_manager_and_keeps_the_runs_state(self, dirs: Path) -> None:
        """A released sink's next use loads its hash file again, with the run's touched set."""
        sinks = SinkRegistry()
        sink = sinks.get(APPLE, "TestKit", "Test Kit", 1)
        url = f"{APPLE.json_prefix}testkit/a.json"
        sink.hash_manager.update_hash(url, "body", Path("documentation/TestKit/a.md"))
        sink.processed_urls.add(url)
        manager = sink.hash_manager
        assert sink.release() and not sink.loaded
        assert Config.get_hash_file("TestKit").exists()
        assert sinks.get(APPLE, "testkit", "x", 1) is sink and sink.processed_urls == {url}
        again = sink.hash_manager
        assert again is not manager and again.hashes[url] == manager.hashes[url] and url in again.touched

    def test_a_top_level_sink_is_released_once_no_job_in_flight_uses_it(self, dirs: Path) -> None:
        sinks = SinkRegistry()
        sink = sinks.get(APPLE, "TestKit", "Test Kit", 1)
        sink.users.update({"testkit", "otherkit"})
        sink.pages_in_flight = 1
        sinks.job_done("testkit")
        sinks.job_done("otherkit")
        assert loaded(sink)  # a page still in flight records into it
        sink.pages_in_flight = 0
        sinks.release_if_idle(sink)
        assert not loaded(sink)
        # A module's sink stays loaded until the end of the run
        module = sinks.get(APPLE, "Intents", "Intents", 1, module=True)
        sinks.release_if_idle(module)
        assert loaded(module)
        sinks.save_all()
        assert not loaded(module) and sinks.all() == []

    async def test_a_run_shares_one_registry_and_each_job_leaves_it(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """scrape.py's jobs get their sinks from the run's registry, which holds none once they're done."""
        runs: Runs = sandbox_runs(tmp_path, monkeypatch)
        other = "otherkit"
        other_site: Site = {other: [f"{other}/one"], f"{other}/one": []}
        apple = Apple({**routes_for(SITE), **routes_for(other_site)})
        registries: List[SinkRegistry] = []

        class Registry(SinkRegistry):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                super().__init__(*args, **kwargs)
                registries.append(self)

        class MockedScraper(AppleJSONDocumentationScraper):
            async def __aenter__(self) -> "MockedScraper":
                assert self.sinks is registries[0]
                self.session = httpx.AsyncClient(transport=httpx.MockTransport(apple), follow_redirects=True)
                return self

        monkeypatch.setattr(scrape_all_frameworks, "SinkRegistry", Registry)
        monkeypatch.setattr(scrape_all_frameworks, "AppleJSONDocumentationScraper", MockedScraper)
        monkeypatch.setattr(scrape_all_frameworks, "AppleFrameworkListScraper", FrameworkList)
        monkeypatch.setattr(sys, "argv", [
            "scrape.py", "--frameworks", FW, other, "--yes", "--cleanup-orphans", "--auto-cleanup",
        ])
        assert await scrape_all_frameworks.scrape_everything() == 0
        assert apple.unrouted == [] and len(registries) == 1
        # The run's frameworks are linked locally, and every sink was saved and left
        assert registries[0].known_dirs == {FW: FW, other: other}
        assert registries[0].all() == []
        for path in SITE:
            assert file_of(path).exists(), path
        assert runs.saved()["hashes"] and runs.saved(other)["hashes"]


# ---------------------------------------------------------------------------
# Step 1b: the resolver, the scope rule, routing and the D6 removal rules
# ---------------------------------------------------------------------------

A = "com.apple.umbrella"  # Umbrella's bundle: its pages', and its module ModKit's
B = "com.apple.otherbrella"  # Otherbrella's (ModKit's second parent)
S = "com.apple.sibkit"  # shared by Sibkit and SibkitUI, two top-level technologies

# (a page's cased documentation path, the bundle its identifier names)
Link = Tuple[str, str]
# cased documentation path -> (the page's bundle, its links)
Pages = Dict[str, Tuple[str, List[Link]]]


def topic_page(
    path: str,
    bundle: str,
    links: Sequence[Link] = (),
    implementations: Sequence[Link] = (),
    occ: Optional[List[Dict[str, Any]]] = None,
) -> str:
    """A page whose links resolve through their references (url /documentation/<path, lowercased>).

    implementations: a protocol requirement's default implementations
    (defaultImplementationsSections, 1.4), linked by no other section
    occ: its Objective-C/C variant's patch (variantOverrides, 1.5)
    """
    identifiers = [f"doc://{link_bundle}/documentation/{link}" for link, link_bundle in links]
    implementation_ids = [f"doc://{link_bundle}/documentation/{link}" for link, link_bundle in implementations]
    body: Dict[str, Any] = {
        "identifier": {"url": f"doc://{bundle}/documentation/{path}", "interfaceLanguage": "swift"},
        "metadata": {"title": path.split("/")[-1], "symbolKind": "class", "roleHeading": "Class"},
        "abstract": [{"type": "text", "text": f"The {path} page."}],
        "topicSections": [{"title": "Topics", "identifiers": identifiers}],
        "references": {
            identifier: {"type": "topic", "url": f"/documentation/{link.lower()}", "title": link.split("/")[-1],
                         "identifier": identifier, "kind": "symbol", "role": "symbol"}
            for identifier, (link, _) in zip(identifiers + implementation_ids, [*links, *implementations])
        },
    }
    if implementations:
        body["defaultImplementationsSections"] = [
            {"anchor": "Proto-Implementations", "title": "Proto Implementations", "identifiers": implementation_ids}]
    if occ is not None:
        body["variantOverrides"] = [{"traits": [{"interfaceLanguage": "occ"}], "patch": occ}]
    return json.dumps(body)


def d6_routes(
    pages: Pages,
    overrides: Optional[Dict[str, List[Spec]]] = None,
    implementations: Optional[Dict[str, List[Link]]] = None,
    occ: Optional[Dict[str, List[Dict[str, Any]]]] = None,
) -> Dict[str, List[Spec]]:
    """Each page answers 200 with an ETag of its body (never stored; 304 on a match, never asked for), unless overridden.

    implementations: a page's path -> its default implementations
    occ: a page's path -> its Objective-C/C variant's patch
    """
    routes: Dict[str, List[Spec]] = {}
    for path, (bundle, links) in pages.items():
        body = topic_page(path, bundle, links, (implementations or {}).get(path, ()), (occ or {}).get(path))
        routes[json_url(path.lower())] = [ok(body, "E-" + hashlib.sha256(body.encode()).hexdigest()[:12])]
    for path, specs in (overrides or {}).items():
        routes[json_url(path.lower())] = specs
    return routes


def doc_file(path: str) -> Path:
    """A page's file: its dir is its first segment, as cased (relative, as in production)."""
    dir_name = path.split("/")[0]
    relative = page_path(dir_name, doc_url(path.lower()))
    assert relative is not None
    return Path("documentation") / relative


def metadata(name: str) -> Dict[str, Any]:
    """A hash file's metadata, as saved."""
    data: Dict[str, Any] = json.loads(Config.get_hash_file(name).read_text())
    return dict(data["metadata"])


def module_of(name: str) -> Dict[str, Any]:
    module: Dict[str, Any] = metadata(name)["module"]
    return module


def docs() -> Set[Path]:
    """Every doc file in the sandbox."""
    return set(Path("documentation").rglob("*.md"))


def sandbox_bytes() -> Dict[str, bytes]:
    """Every doc and hash file in the sandbox, with its bytes."""
    return {str(path): path.read_bytes() for root in ("documentation", ".hashes")
            for path in Path(root).rglob("*") if path.is_file()}


UMBRELLA: Pages = {
    "Umbrella": (A, [("Umbrella/guide", A), ("ModKit", A)]),
    "Umbrella/guide": (A, []),
    # ModKit links back to an umbrella page nothing else links
    "ModKit": (A, [("ModKit/Thing", A), ("Umbrella/back", A)]),
    "ModKit/Thing": (A, []),
    "Umbrella/back": (A, []),
}
OTHERKIT: Pages = {"Otherkit": (A, [("Otherkit/one", A)]), "Otherkit/one": (A, [])}


def without(pages: Pages, path: str, link: str) -> Pages:
    """The pages, with one page no longer linking to one target."""
    bundle, links = pages[path]
    return {**pages, path: (bundle, [entry for entry in links if entry[0] != link])}


class D6Runs:
    """Whole scrape.py runs (--cleanup-orphans --auto-cleanup) over one sandbox, against a fake Apple."""

    def __init__(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        self.runs = sandbox_runs(tmp_path, monkeypatch)
        self.monkeypatch = monkeypatch
        self.events: List[EventDict] = []
        self.requests: List[str] = []

    async def scrape(
        self,
        pages: Pages,
        listed: Sequence[str],
        *names: str,
        overrides: Optional[Dict[str, List[Spec]]] = None,
        concurrent: int = 20,
        delays: Optional[Dict[str, float]] = None,
        implementations: Optional[Dict[str, List[Link]]] = None,
        occ: Optional[Dict[str, List[Dict[str, Any]]]] = None,
        redirects: Optional[Dict[str, str]] = None,
    ) -> int:
        """One run: technologies.json lists `listed`; --frameworks names, else --all.

        delays: a URL fragment -> seconds its response waits (a page in flight)
        implementations: a page's path -> its default implementations
        occ: a page's path -> its Objective-C/C variant's patch
        """
        apple = Apple(d6_routes(pages, overrides, implementations, occ), redirects)

        async def handler(request: httpx.Request) -> httpx.Response:
            for fragment, seconds in (delays or {}).items():
                if fragment in str(request.url):
                    await asyncio.sleep(seconds)
            # Apple's URL space is case-insensitive (a job's root URL has its id's casing)
            return apple(httpx.Request(request.method, str(request.url).lower(), headers=request.headers))

        class MockedScraper(AppleJSONDocumentationScraper):
            async def __aenter__(self) -> "MockedScraper":
                self.session = httpx.AsyncClient(transport=httpx.MockTransport(handler), follow_redirects=True)
                return self

        frameworks = [{"id": framework, "title": framework} for framework in listed]

        class Listed:
            async def __aenter__(self) -> "Listed":
                return self

            async def __aexit__(self, *exc: Any) -> None:
                return None

            async def fetch_all_frameworks(self) -> List[Dict[str, str]]:
                return [dict(framework) for framework in frameworks]

        self.monkeypatch.setattr(scrape_all_frameworks, "AppleJSONDocumentationScraper", MockedScraper)
        self.monkeypatch.setattr(scrape_all_frameworks, "AppleFrameworkListScraper", Listed)
        selection = ["--frameworks", *names] if names else ["--all"]
        self.monkeypatch.setattr(sys, "argv", [
            "scrape.py", *selection, "--yes", "--cleanup-orphans", "--auto-cleanup", "--concurrent", str(concurrent),
        ])
        with capture_logs() as events:
            code: int = await scrape_all_frameworks.scrape_everything()
        self.events = events
        self.requests = [url for url, _ in apple.requests]
        return code

    def logged(self, event: str) -> List[EventDict]:
        return [e for e in self.events if e["event"] == event]


@pytest.fixture
def d6(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[D6Runs]:
    yield D6Runs(tmp_path, monkeypatch)


class TestResolver:
    """The reference resolver and the scope rule (1.1)."""

    def test_a_link_resolves_through_its_reference(self, dirs: Path) -> None:
        scraper = AppleJSONDocumentationScraper("SiriKit")
        intents = "doc://com.apple.sirikit/documentation/Intents"
        anchor = "doc://com.apple.sirikit/documentation/SiriKit/A#a-section"
        dots = "doc://com.apple.swift/documentation/Swift/Comparable/...(_:_:)"
        refs = {
            intents: {"type": "topic", "url": "/documentation/intents"},
            anchor: {"type": "topic", "url": "/documentation/sirikit/a#a-section"},
            dots: {"type": "topic", "url": "/documentation/swift/comparable/'...(_:_:)"},
            "doc://com.apple.sirikit/tutorials/T": {"type": "topic", "url": "/tutorials/t"},
            "doc://com.apple.sirikit/documentation/SiriKit/L": {"type": "link", "url": "https://example.com/l"},
            "doc://com.apple.sirikit/documentation/SiriKit/N": {"type": "topic"},
        }
        # Apple's own URL: a module is /documentation/intents, never sirikit/intents
        assert scraper._resolve(intents, refs) == PageLink(
            json_url=f"{JSON_URL_PREFIX}intents.json", segment="intents", dir_name="Intents",
            bundle="com.apple.sirikit", identifier=intents)
        # A section anchor is its page; Apple's ' escape stays as it is
        assert scraper._resolve(anchor, refs).json_url == f"{JSON_URL_PREFIX}sirikit/a.json"  # type: ignore[union-attr]
        assert scraper._resolve(dots, refs).json_url == (  # type: ignore[union-attr]
            f"{JSON_URL_PREFIX}swift/comparable/'...(_:_:).json")
        # Not a documentation page: a tutorial, an external link, a reference with no URL
        for identifier in ("doc://com.apple.sirikit/tutorials/T", "doc://com.apple.sirikit/documentation/SiriKit/L",
                           "doc://com.apple.sirikit/documentation/SiriKit/N"):
            assert scraper._resolve(identifier, refs) is None
        assert scraper.reference_fallbacks == 0
        # No reference: the identifier's own path (never the framework's id prepended), counted
        fallback = scraper._resolve("doc://com.apple.sirikit/documentation/Intents/INIntent#x", {})
        assert fallback is not None
        assert (fallback.json_url, fallback.dir_name) == (f"{JSON_URL_PREFIX}intents/inintent.json", "Intents")
        assert scraper.reference_fallbacks == 1

    def test_the_scope_rule_follows_the_framework_and_its_bundle_never_a_substring(self, dirs: Path) -> None:
        sinks = SinkRegistry(top_level={"apple": ["HealthKit", "SwiftUI", "Foundation"]})
        scraper = AppleJSONDocumentationScraper("HealthKit", sinks=sinks)
        targets = [
            ("doc://com.apple.healthkit/documentation/HealthKit/HKUnit", "/documentation/healthkit/hkunit"),
            # Same bundle, no top-level technology: a module
            ("doc://com.apple.healthkit/documentation/HealthKitUI", "/documentation/healthkitui"),
            # Same bundle, another top-level technology: its own sink (a handoff)
            ("doc://com.apple.healthkit/documentation/SwiftUI/View", "/documentation/swiftui/view"),
            # Another bundle: out of scope, whatever its name holds ("healthkit" in "healthkitui")
            ("doc://com.apple.healthkitui/documentation/HealthKitUI/X", "/documentation/healthkitui/x"),
            ("doc://com.apple.documentation/documentation/Foundation/NSString", "/documentation/foundation/nsstring"),
            # The framework's own pages, from any bundle
            ("doc://com.apple.other/documentation/HealthKit/Other", "/documentation/healthkit/other"),
        ]
        page = {
            "identifier": {"url": "doc://com.apple.healthkit/documentation/HealthKit"},
            "topicSections": [{"title": "Topics", "identifiers": [identifier for identifier, _ in targets]}],
            "references": {identifier: {"type": "topic", "url": url} for identifier, url in targets},
        }
        assert scraper._extract_urls_from_json_data(page) == [
            f"{JSON_URL_PREFIX}healthkit/hkunit.json", f"{JSON_URL_PREFIX}healthkitui.json",
            f"{JSON_URL_PREFIX}swiftui/view.json", f"{JSON_URL_PREFIX}healthkit/other.json",
        ]
        # Another technology's root is its own job's; the job's own root keeps its id's casing
        root_links = {
            "identifier": {"url": "doc://com.apple.healthkit/documentation/HealthKit"},
            "topicSections": [{"title": "Topics", "identifiers": ["doc://com.apple.healthkit/documentation/SwiftUI",
                                                                  "doc://com.apple.healthkit/documentation/HealthKit"]}],
            "references": {"doc://com.apple.healthkit/documentation/SwiftUI": {"type": "topic", "url": "/documentation/swiftui"},
                           "doc://com.apple.healthkit/documentation/HealthKit": {"type": "topic", "url": "/documentation/healthkit"}},
        }
        assert scraper._extract_urls_from_json_data(root_links) == [f"{JSON_URL_PREFIX}healthkit.json"]
        queue: List[str] = []
        scraper._enqueue([f"{JSON_URL_PREFIX}healthkit.json"], queue)  # type: ignore[arg-type]
        assert queue == [scraper.root_json_url] == [f"{JSON_URL_PREFIX}HealthKit.json"]
        # Routing: the own sink, a module's (cased from the identifier), the sibling's (its title)
        assert scraper._route(f"{JSON_URL_PREFIX}healthkit/hkunit.json") is scraper.sink
        module = scraper._route(f"{JSON_URL_PREFIX}healthkitui.json")
        sibling = scraper._route(f"{JSON_URL_PREFIX}swiftui/view.json")
        assert module is not None and sibling is not None
        assert (module.dir_name, module.module, module.framework_name) == ("HealthKitUI", True, "HealthKitUI")
        assert (sibling.dir_name, sibling.module) == ("SwiftUI", False)
        assert module.parents_this_run == sibling.parents_this_run == {"healthkit"}

    def test_a_standalone_scraper_takes_its_top_level_set_from_the_hash_files(self, dirs: Path) -> None:
        write_hash_file("SwiftUI", {f"{APPLE.json_prefix}swiftui/view.json": {"hash": "h"}})
        write_hash_file("Intents", {f"{APPLE.json_prefix}intents/x.json": {"hash": "h"}})
        intents = Config.get_hash_file("Intents")
        data = json.loads(intents.read_text())
        data["metadata"]["module"] = {"parents": {"sirikit": {"unlinked_clean_runs": 0}}}
        intents.write_text(json.dumps(data))
        (Config.CACHE_DIR / "broken_hashes.json").write_text("{")
        write_hash_file("hig_docs", {"https://developer.apple.com/tutorials/data/design/x.json": {"hash": "h"}})
        assert SinkRegistry().top_level(APPLE) == {"swiftui", "broken"}


class TestModules:
    """A module's pages go to its own dir and hash file, crawled through its parent."""

    async def test_a_module_gets_its_own_dir_and_hash_file_and_a_rerun_changes_nothing(self, d6: D6Runs) -> None:
        assert await d6.scrape(UMBRELLA, ["Umbrella"], "Umbrella") == 0
        assert docs() == {doc_file(path) for path in UMBRELLA}
        assert doc_file("ModKit/Thing") == Path("documentation/ModKit/thing.md")
        assert "**Framework**: ModKit" in doc_file("ModKit/Thing").read_text()
        assert "**Framework**: Umbrella" in doc_file("Umbrella/back").read_text()
        assert module_of("ModKit") == {"bundle": A, "parents": {"umbrella": {"unlinked_clean_runs": 0}}}
        assert metadata("ModKit")["render"] == {"version": AppleJSONDocumentationScraper.RENDER_VERSION}
        assert metadata("Umbrella")["child_modules"] == {"modkit": {}}
        assert "module" not in metadata("Umbrella")
        # Each page fetched once, never under its umbrella's id
        assert not any("umbrella/modkit" in url for url in d6.requests)
        before = sandbox_bytes()
        assert await d6.scrape(UMBRELLA, ["Umbrella"], "Umbrella") == 0
        assert sandbox_bytes() == before
        # Rule 5: the parent's size in the largest-first sort counts its module's
        assert scrape_all_frameworks.scan_hash_dir(Config.CACHE_DIR).page_counts["umbrella"] == 6 + 4

    async def test_a_modules_root_is_crawled_even_when_its_parent_links_only_pages_under_it(
        self, d6: D6Runs
    ) -> None:
        """Accelerate's simd-library links simd's symbols, never simd: the pages only simd's root links."""
        pages: Pages = {
            "Umbrella": (A, [("ModKit/Thing", A)]),
            "ModKit/Thing": (A, []),
            "ModKit": (A, [("ModKit/Thing", A), ("ModKit/Overload", A)]),
            "ModKit/Overload": (A, []),
        }
        assert await d6.scrape(pages, ["Umbrella"]) == 0
        assert {doc_file("ModKit"), doc_file("ModKit/Overload")} <= docs()
        # A module without a root page (Apple answers 404): nothing but its pages
        rootless = {path: page for path, page in pages.items() if path != "ModKit"}
        rootless["Umbrella"] = (A, [("ModKit/Thing", A), ("ModKit/Overload", A)])
        assert await d6.scrape(rootless, ["Umbrella"]) == 0
        assert doc_file("ModKit/Overload").exists() and not doc_file("ModKit").exists()

    async def test_a_module_unlinked_by_its_only_parent_goes_after_2_clean_runs(self, d6: D6Runs) -> None:
        assert await d6.scrape(UMBRELLA, ["Umbrella"]) == 0
        unlinked = without(UMBRELLA, "Umbrella", "ModKit")
        for run in range(1, MODULE_UNLINKED_RUNS):
            assert await d6.scrape(unlinked, ["Umbrella"]) == 0
            assert module_of("ModKit")["parents"] == {"umbrella": {"unlinked_clean_runs": run}}
            assert doc_file("ModKit/Thing").exists()
        assert await d6.scrape(unlinked, ["Umbrella"]) == 0
        assert not Config.get_hash_file("ModKit").exists() and not (Path("documentation") / "ModKit").exists()
        assert "child_modules" not in metadata("Umbrella")
        assert [e["reason"] for e in d6.logged("framework_removed")] == ["module_unlinked"]

    async def test_a_module_with_two_parents_stays_while_one_still_links_it(self, d6: D6Runs) -> None:
        pages: Pages = {**UMBRELLA, "Otherbrella": (B, [("ModKit", B)])}
        assert await d6.scrape(pages, ["Umbrella", "Otherbrella"]) == 0
        assert module_of("ModKit")["parents"] == {
            "otherbrella": {"unlinked_clean_runs": 0}, "umbrella": {"unlinked_clean_runs": 0}}
        files = docs()
        stops = without(pages, "Otherbrella", "ModKit")
        for run in (1, 2, 3):
            assert await d6.scrape(stops, ["Umbrella", "Otherbrella"]) == 0
            assert module_of("ModKit")["parents"] == {
                "otherbrella": {"unlinked_clean_runs": run}, "umbrella": {"unlinked_clean_runs": 0}}
            assert docs() == files

    @pytest.mark.parametrize("concurrent,delays", [(1, None), (20, {"/modkit.json": 0.05, "/modkit/thing.json": 0.05})],
                             ids=["done", "in-flight"])
    async def test_a_dedup_hit_gives_the_second_parent_the_pages_links(
        self, d6: D6Runs, concurrent: int, delays: Optional[Dict[str, float]]
    ) -> None:
        """A page of Otherbrella only a module page links: reached though Umbrella fetched the module."""
        pages: Pages = {**UMBRELLA, "Otherbrella": (B, [("ModKit", B)]),
                 "ModKit/Thing": (A, [("Otherbrella/hidden", B)]), "Otherbrella/hidden": (B, [])}
        for run in (1, 2):
            assert await d6.scrape(pages, ["Umbrella", "Otherbrella"], concurrent=concurrent, delays=delays) == 0
            assert doc_file("Otherbrella/hidden").exists(), run
            # The module's pages are fetched once a run, by one parent
            assert d6.requests.count(json_url("modkit/thing")) == 1
            assert module_of("ModKit")["parents"] == {
                "otherbrella": {"unlinked_clean_runs": 0}, "umbrella": {"unlinked_clean_runs": 0}}

    def test_a_dedup_hit_on_a_page_whose_404_is_pending_skips_both_jobs_cleanup(self, dirs: Path) -> None:
        """Its links aren't read this run: the pages only it links stay untouched in either job's scope."""
        site = dataclasses.replace(APPLE, page_gone_runs=2)
        sinks = SinkRegistry(top_level={APPLE.name: ["Umbrella", "Otherbrella"]})
        first = AppleJSONDocumentationScraper("Umbrella", sinks=sinks, site=site)
        second = AppleJSONDocumentationScraper("Otherbrella", sinks=sinks, site=site)
        url = json_url("umbrella/guide")
        first.hash_manager.update_hash(url, "content", file_path=doc_file("Umbrella/guide"))
        first._handle_fetch_failure(first.sink, url, FetchFailed(404, "HTTP 404", False))
        assert first.sink.gone_pending == {url} and url in first.hash_manager.touched
        queue: Deque[str] = deque()
        second._take_links(first.sink, url, queue)
        assert not queue and first.sink.dedup_jobs == {url: {"otherbrella"}}
        outcomes = {"umbrella": first.outcome, "otherbrella": second.outcome}
        json_scraper.apply_sink_failure_policy(first.sink, outcomes.get, "Umbrella")
        for outcome in outcomes.values():
            assert outcome.gone_pending == {url: 1} and outcome.skip_cleanup and not outcome.blocked
        assert first.hash_manager.get_counter(url, "consecutive_gone") == 1

    async def test_a_module_pages_failure_blocks_its_parent_and_is_counted_in_the_modules_file(
        self, d6: D6Runs
    ) -> None:
        assert await d6.scrape(UMBRELLA, ["Umbrella"]) == 0
        files = docs()
        assert await d6.scrape(UMBRELLA, ["Umbrella"], overrides={"ModKit/Thing": [status(502)]}) == 1
        assert docs() == files
        entry = json.loads(Config.get_hash_file("ModKit").read_text())["hashes"][json_url("modkit/thing")]
        assert entry["consecutive_failures"] == 1 and entry["file_path"] == str(doc_file("ModKit/Thing"))

    async def test_a_parent_run_with_a_protected_failure_deletes_nothing(self, d6: D6Runs) -> None:
        assert await d6.scrape(UMBRELLA, ["Umbrella"]) == 0
        files = docs()
        unlinked = without(UMBRELLA, "Umbrella", "ModKit")
        for _ in (1, 2):
            assert await d6.scrape(unlinked, ["Umbrella"], overrides={"Umbrella/guide": [status(502)]}) == 1
            # Unclean runs don't count
            assert module_of("ModKit")["parents"] == {"umbrella": {"unlinked_clean_runs": 0}}
            assert docs() == files

    async def test_a_module_no_parent_reached_loses_its_counts_only_when_a_parent_ran(self, d6: D6Runs) -> None:
        """A run that doesn't fetch a page ends its streaks (D8, a pending 404/410), its module unreached too;
        a run whose parents didn't run (a subset run) neither counts nor resets."""
        pages: Pages = {**UMBRELLA, **OTHERKIT}
        assert await d6.scrape(pages, ["Umbrella", "Otherkit"]) == 0
        hash_file = Config.get_hash_file("ModKit")
        data = json.loads(hash_file.read_text())
        thing = json_url("modkit/thing")
        data["hashes"][thing].update(consecutive_failures=2, consecutive_gone=1, consecutive_local_errors=1)
        hash_file.write_text(json.dumps(data))
        before = hash_file.read_bytes()
        # Its only parent didn't run: kept as they are
        assert await d6.scrape(pages, ["Umbrella", "Otherkit"], "Otherkit") == 0
        assert hash_file.read_bytes() == before and not d6.logged("unreached_module_counts_reset")
        # Its parent ran and didn't route it a page: the fetch streaks end, the local-error count stays
        assert await d6.scrape(without(pages, "Umbrella", "ModKit"), ["Umbrella", "Otherkit"], "Umbrella") == 0
        entry = json.loads(hash_file.read_text())["hashes"][thing]
        assert {k: v for k, v in entry.items() if k.startswith("consecutive_")} == {"consecutive_local_errors": 1}
        assert [e["counts"] for e in d6.logged("unreached_module_counts_reset")] == [2]

    async def test_a_parent_unlisted_for_one_run_keeps_its_modules(self, d6: D6Runs) -> None:
        pages: Pages = {**UMBRELLA, **OTHERKIT}
        assert await d6.scrape(pages, ["Umbrella", "Otherkit"]) == 0
        files = docs()
        module = module_of("ModKit")
        # The pre-scrape counted it once (unlisted_runs 1): its hash file stays
        hash_file = Config.get_hash_file("Umbrella")
        data = json.loads(hash_file.read_text())
        data["metadata"]["unlisted_runs"] = 1
        hash_file.write_text(json.dumps(data))
        assert await d6.scrape(pages, ["Otherkit"]) == 0
        assert docs() == files and module_of("ModKit") == module

    async def test_a_removed_parent_is_pruned_and_its_parentless_module_deleted(self, d6: D6Runs) -> None:
        pages: Pages = {**UMBRELLA, **OTHERKIT}
        assert await d6.scrape(pages, ["Umbrella", "Otherkit"]) == 0
        # The pre-scrape removes it after 2 unlisted runs (docs dir and hash file)
        remove_framework("Umbrella", Config.get_framework_output_dir("Umbrella"), Config.get_hash_file("Umbrella"),
                         reason="unlisted")
        assert await d6.scrape(pages, ["Otherkit"]) == 0
        assert not Config.get_hash_file("ModKit").exists() and not doc_file("ModKit/Thing").exists()
        assert [e["reason"] for e in d6.logged("framework_removed")] == ["module_parentless"]
        assert doc_file("Otherkit/one").exists()

    async def test_a_renamed_parent_takes_over_the_module(self, d6: D6Runs) -> None:
        pages: Pages = {"Umbrella": (A, [("ModKit", A)]), "ModKit": (A, [("ModKit/Thing", A)]),
                        "ModKit/Thing": (A, []), **OTHERKIT}
        assert await d6.scrape(pages, ["Umbrella", "Otherkit"]) == 0
        remove_framework("Umbrella", Config.get_framework_output_dir("Umbrella"), Config.get_hash_file("Umbrella"),
                         reason="unlisted")
        renamed = {**pages, "Umbrella2": (A, [("ModKit", A)])}
        assert await d6.scrape(renamed, ["Umbrella2", "Otherkit"]) == 0
        assert module_of("ModKit")["parents"] == {"umbrella2": {"unlinked_clean_runs": 0}}
        assert doc_file("ModKit/Thing").exists() and d6.logged("framework_removed") == []

    async def test_a_renamed_module_is_a_new_one_and_the_old_one_goes(self, d6: D6Runs) -> None:
        pages: Pages = {"Umbrella": (A, [("ModKit", A)]), "ModKit": (A, [("ModKit/Thing", A)]),
                        "ModKit/Thing": (A, [])}
        assert await d6.scrape(pages, ["Umbrella"]) == 0
        renamed: Pages = {"Umbrella": (A, [("NewKit", A)]), "NewKit": (A, [("NewKit/Thing", A)]),
                          "NewKit/Thing": (A, [])}
        for _ in range(MODULE_UNLINKED_RUNS):
            assert await d6.scrape(renamed, ["Umbrella"]) == 0
            assert doc_file("NewKit/Thing").exists()
        assert not Config.get_hash_file("ModKit").exists()
        assert metadata("Umbrella")["child_modules"] == {"newkit": {}}

    async def test_a_promoted_module_keeps_its_dir_and_is_judged_as_a_framework(self, d6: D6Runs) -> None:
        assert await d6.scrape(UMBRELLA, ["Umbrella"]) == 0
        files = docs()
        # technologies.json now lists ModKit: its own job; Umbrella hands it its pages (one hop)
        assert await d6.scrape(UMBRELLA, ["Umbrella", "ModKit"], concurrent=1) == 0
        assert docs() == files
        assert "module" not in metadata("ModKit")
        # Umbrella links only ModKit's root, which is ModKit's own job's: no handoff
        assert "handoff_from" not in metadata("ModKit")
        # back: only ModKit's pages link it, which Umbrella no longer follows: ModKit's job hands it over
        assert metadata("Umbrella")["handoff_from"] == {"modkit": {}}
        assert "child_modules" not in metadata("Umbrella")
        assert await d6.scrape(UMBRELLA, ["Umbrella", "ModKit"]) == 0
        assert docs() == files
        # Umbrella alone: its handoff writer didn't run, so it isn't cleaned (back, untouched, stays)
        assert await d6.scrape(UMBRELLA, ["Umbrella", "ModKit"], "Umbrella") == 0
        assert docs() == files


class TestSubsetRuns:
    """Rule 1 under --frameworks: a module is cleaned only when every parent ran clean."""

    async def test_its_only_parent_alone_finds_no_orphan_in_the_module(self, d6: D6Runs) -> None:
        pages: Pages = {**UMBRELLA, **OTHERKIT}
        assert await d6.scrape(pages, ["Umbrella", "Otherkit"]) == 0
        files = docs()
        assert await d6.scrape(pages, ["Umbrella", "Otherkit"], "Umbrella") == 0
        assert docs() == files
        assert [e for e in d6.logged("orphans_deleted")] == []

    async def test_one_of_two_parents_alone_leaves_the_module_and_the_others_counter(self, d6: D6Runs) -> None:
        # OnlyUmbrella: a module page only Umbrella's pages link
        pages: Pages = {**UMBRELLA, "Umbrella/guide": (A, [("ModKit/OnlyUmbrella", A)]), "ModKit/OnlyUmbrella": (A, []),
                 "Otherbrella": (B, [("ModKit", B)])}
        assert await d6.scrape(pages, ["Umbrella", "Otherbrella"]) == 0
        files = docs()
        assert doc_file("ModKit/OnlyUmbrella") in files
        for _ in (1, 2):
            assert await d6.scrape(pages, ["Umbrella", "Otherbrella"], "Otherbrella") == 0
            assert docs() == files
            assert module_of("ModKit")["parents"] == {
                "otherbrella": {"unlinked_clean_runs": 0}, "umbrella": {"unlinked_clean_runs": 0}}


SIBLINGS: Pages = {
    "Sibkit": (S, [("Sibkit/a", S)]),
    "Sibkit/a": (S, []),
    # A Sibkit page only its bundle sibling links (a handoff); its own link is
    # followed too: by Sibkit's job, or by its writer once Sibkit's crawl has ended
    "SibkitUI": (S, [("SibkitUI/b", S), ("Sibkit/hidden", S)]),
    "SibkitUI/b": (S, []),
    "Sibkit/hidden": (S, [("Sibkit/deeper", S)]),
    "Sibkit/deeper": (S, []),
}


class TestHandoff:
    """A same-bundle sibling's page goes to the sibling's own sink (the measured 1.1 question)."""

    async def test_a_page_only_a_bundle_sibling_links_is_handed_off_and_removed_once_unlinked(
        self, d6: D6Runs
    ) -> None:
        listed = ["Sibkit", "SibkitUI"]
        hidden, deeper = json_url("sibkit/hidden"), json_url("sibkit/deeper")
        # One job at a time: Sibkit's crawl ends before SibkitUI hands it hidden
        assert await d6.scrape(SIBLINGS, listed, concurrent=1) == 0
        assert doc_file("Sibkit/hidden").exists() and "**Framework**: Sibkit" in doc_file("Sibkit/hidden").read_text()
        assert not doc_file("Sibkit/deeper").exists()
        assert metadata("Sibkit")["handoff_from"] == {"sibkitui": {}}
        assert "handoff_from" not in metadata("SibkitUI")
        # hidden's links, as Sibkit's scope has them: the seeds of Sibkit's next crawl
        assert metadata("Sibkit")["handoff_links"] == {hidden: [[deeper, "Sibkit", S]]}
        assert d6.logged("link_coverage")[0]["gaps"] == 1
        # Fetched by Sibkit's own job on the next run, and every run
        assert await d6.scrape(SIBLINGS, listed, concurrent=1) == 0
        assert "**Framework**: Sibkit" in doc_file("Sibkit/deeper").read_text()
        assert d6.requests.count(deeper) == 1 and d6.logged("link_coverage")[0]["gaps"] == 0
        before = sandbox_bytes()
        assert await d6.scrape(SIBLINGS, listed) == 0
        assert sandbox_bytes() == before
        # Sibkit alone: its handoff writer didn't run, so it isn't cleaned, and its seeds stay
        assert await d6.scrape(SIBLINGS, listed, "Sibkit") == 0
        assert doc_file("Sibkit/hidden").exists() and doc_file("Sibkit/deeper").exists()
        assert metadata("Sibkit")["handoff_links"] == {hidden: [[deeper, "Sibkit", S]]}
        # Unlinked, with both jobs clean: hidden goes, its seeds with it; deeper, seeded
        # this run, goes on the next one (normal orphan cleanup)
        unlinked = without(SIBLINGS, "SibkitUI", "Sibkit/hidden")
        assert await d6.scrape(unlinked, listed) == 0
        assert not doc_file("Sibkit/hidden").exists() and doc_file("Sibkit/deeper").exists()
        assert "handoff_links" not in metadata("Sibkit")
        assert await d6.scrape(unlinked, listed) == 0
        assert not doc_file("Sibkit/deeper").exists() and doc_file("Sibkit/a").exists()

    async def test_a_handoff_pages_links_are_the_same_whichever_job_ends_first(self, d6: D6Runs) -> None:
        """kernel/ionetworkstats: only IOKit's header page lists it, so it is a handoff, and its
        members were never fetched. Only its own job (Sibkit's) follows its links: at the end of
        its crawl when the handoff came first, from the seeds the handoff page left on the last
        run when it came late. After two runs, both orders give the same files and hash files
        (handoff_from, a module's parents and counters, the seeds), with a page that both
        Sibkit's own crawl and the handoff page reach, a module page, another bundle's page in
        Sibkit, SibkitUI's page in its bundle (a handoff from Sibkit) and in another bundle (a
        link seed of SibkitUI's), and a third technology's."""
        other = "com.apple.other"
        listed = ["Sibkit", "SibkitUI", "Thirdkit"]
        pages: Pages = {
            **SIBLINGS,
            "Sibkit/a": (S, [("Sibkit/both", S)]),
            "Sibkit/hidden": (S, [("Sibkit/deeper", S), ("Sibkit/both", S), ("Sibkit/xb", other),
                                  ("SibkitUI/extra", S), ("SibkitUI/xb", other), ("Thirdkit/t", S), ("SibMod/m", S)]),
            "Sibkit/both": (S, []), "Sibkit/xb": (S, []), "SibkitUI/extra": (S, []), "SibkitUI/xb": (S, []),
            "Thirdkit": (S, []), "Thirdkit/t": (S, []), "SibMod": (S, []), "SibMod/m": (S, []),
        }
        results = []
        for late, delays in (("writer", {"sibkitui/b.json": 0.3}), ("primary", {"sibkit/a.json": 0.3})):
            for root in ("documentation", ".hashes"):
                shutil.rmtree(root, ignore_errors=True)
            for _ in range(2):
                assert await d6.scrape(pages, listed, delays=delays) == 0
            drained = [e["handoffs"] for e in d6.logged("crawl_drain") if e["framework"] == "Sibkit"]
            # How Sibkit got hidden's links depends on the order (taken, or seeded only)...
            assert (any(drained)) == (late == "primary")
            # ...what they reach doesn't: its own segment in any bundle, another only in its bundle
            for path in ("Sibkit/deeper", "Sibkit/both", "Sibkit/xb", "SibkitUI/extra", "Thirdkit/t", "SibMod/m"):
                assert doc_file(path).exists(), path
            # SibkitUI/xb, which no scope reaches (another bundle's link to another
            # technology): a link seed of SibkitUI's, fetched by its own job
            assert "**Framework**: SibkitUI" in doc_file("SibkitUI/xb").read_text()
            assert metadata("SibkitUI")["link_seeds"] == [[json_url("sibkitui/xb"), "SibkitUI", other]]
            assert metadata("Thirdkit")["handoff_from"] == {"sibkit": {}}
            assert metadata("SibkitUI")["handoff_from"] == {"sibkit": {}}
            assert metadata("Sibkit")["handoff_from"] == {"sibkitui": {}}
            assert module_of("SibMod")["parents"] == {"sibkit": {"unlinked_clean_runs": 0}}
            assert metadata("Sibkit")["handoff_links"] == {json_url("sibkit/hidden"): sorted(
                [json_url(path.lower()), path.split("/")[0], other if path == "Sibkit/xb" else S]
                for path in ("Sibkit/deeper", "Sibkit/both", "Sibkit/xb", "SibkitUI/extra", "Thirdkit/t", "SibMod/m"))}
            assert d6.logged("link_coverage")[0]["gaps"] == 0
            results.append(sandbox_bytes())
        assert results[0] == results[1]

    async def test_a_handoff_page_whose_fetch_fails_keeps_its_seeds_and_deletes_nothing(self, d6: D6Runs) -> None:
        listed = ["Sibkit", "SibkitUI"]
        for _ in range(2):
            assert await d6.scrape(SIBLINGS, listed, concurrent=1) == 0
        files, seeds = docs(), metadata("Sibkit")["handoff_links"]
        assert doc_file("Sibkit/deeper") in files
        # SibkitUI's fetch of hidden fails (5xx): the writer is blocked, Sibkit still
        # crawls deeper from its seeds, nothing is deleted, the seeds stay
        failing = {"Sibkit/hidden": [status(503)]}
        for _ in range(2):
            assert await d6.scrape(SIBLINGS, listed, overrides=failing, concurrent=1) != 0
            assert docs() == files and metadata("Sibkit")["handoff_links"] == seeds
            assert d6.requests.count(json_url("sibkit/deeper")) == 1
        assert await d6.scrape(SIBLINGS, listed, concurrent=1) == 0
        assert docs() == files


class TestInlineLinks:
    """A page only an inline reference names is Apple's page too: crawled when no curation reaches it."""

    async def test_an_inline_only_page_is_crawled_and_removed_once_unlinked(self, d6: D6Runs) -> None:
        pages: Pages = {**UMBRELLA, "Umbrella/note": (A, [])}
        guide = json.loads(topic_page("Umbrella/guide", A, []))
        note = f"doc://{A}/documentation/Umbrella/note"
        guide["abstract"] = [{"type": "text", "text": "See "}, {"type": "reference", "identifier": note}]
        guide["references"][note] = {"type": "topic", "url": "/documentation/umbrella/note", "title": "note",
                                     "identifier": note, "kind": "article", "role": "article"}
        inline = {"Umbrella/guide": [ok(json.dumps(guide), "E-guide")]}
        assert await d6.scrape(pages, ["Umbrella"], overrides=inline) == 0
        assert doc_file("Umbrella/note").exists() and d6.requests.count(json_url("umbrella/note")) == 1
        assert "See [note](./note.md)" in doc_file("Umbrella/guide").read_text()
        before = sandbox_bytes()
        assert await d6.scrape(pages, ["Umbrella"], overrides=inline) == 0
        assert sandbox_bytes() == before
        # Unlinked: removed by the normal orphan cleanup
        assert await d6.scrape(pages, ["Umbrella"]) == 0
        assert not doc_file("Umbrella/note").exists()


class TestLinkCoverage:
    async def test_a_linked_page_no_job_fetches_is_reported(self, d6: D6Runs, tmp_path: Path) -> None:
        """A page Otherkit's crawl never reaches, linked from Umbrella in another bundle (so
        Umbrella's job never follows it): a gap, logged and written to the report. A page
        whose entry is an error entry (a firewall's 403) isn't one."""
        other = "com.apple.other"
        pages: Pages = {**UMBRELLA, **OTHERKIT, "Otherkit/hidden": (A, []),
                        "Umbrella/guide": (A, [("Otherkit/hidden", other), ("Otherkit/blocked", other)])}
        report = tmp_path / "coverage.md"
        d6.monkeypatch.setenv("LINK_COVERAGE_REPORT", str(report))
        assert await d6.scrape(pages, ["Umbrella", "Otherkit"],
                               overrides={"Otherkit/one": [ok(topic_page("Otherkit/one", A, [("Otherkit/blocked", A)]),
                                                              "E-one")],
                                          "Otherkit/blocked": [status(403)]}) == 0
        gaps = d6.logged("link_coverage_gaps")
        assert [e["count"] for e in gaps] == [1] and gaps[0]["frameworks"] == {"Otherkit": 1}
        assert gaps[0]["examples"] == [f"{doc_url('otherkit/hidden')} <- {doc_url('umbrella/guide')}"]
        lines = report.read_text().splitlines()
        assert lines[0].startswith("Link coverage: 1 ") and "| Otherkit | 1 |" in lines
        assert f"- {doc_url('otherkit/hidden')} (linked from {doc_url('umbrella/guide')})" in lines
        # A link seed of Otherkit's: fetched by its own job on the next run, then every run
        assert metadata("Otherkit")["link_seeds"] == [[json_url("otherkit/hidden"), "Otherkit", other]]
        for _ in range(2):
            assert await d6.scrape(pages, ["Umbrella", "Otherkit"],
                                   overrides={"Otherkit/one": [ok(topic_page("Otherkit/one", A,
                                                                             [("Otherkit/blocked", A)]), "E-one")],
                                              "Otherkit/blocked": [status(403)]}) == 0
            assert "**Framework**: Otherkit" in doc_file("Otherkit/hidden").read_text()
            assert d6.logged("link_coverage")[0]["gaps"] == 0
            assert report.read_text().startswith("Link coverage: 0 ")

    async def test_a_gone_link_seed_on_a_multi_writer_sink_settles(self, d6: D6Runs) -> None:
        """A cross-bundle link to a page that answers 404, in a sink with handoff writers
        (deferred): the seed stays, its page is fetched once a run, its error entry stays,
        and nothing changes from run to run."""
        other = "com.apple.other"
        pages: Pages = {**UMBRELLA, **OTHERKIT, "Otherkit/x": (A, []),
                        "Umbrella/guide": (A, [("Otherkit/gone", other), ("Otherkit/x", A)])}
        overrides = {"Otherkit/gone": [status(404)]}
        for _ in range(3):
            assert await d6.scrape(pages, ["Umbrella", "Otherkit"], overrides=overrides) == 0
        assert metadata("Otherkit")["handoff_from"] == {"umbrella": {}}
        settled = sandbox_bytes()
        for _ in range(4):
            assert await d6.scrape(pages, ["Umbrella", "Otherkit"], overrides=overrides) == 0
            assert sandbox_bytes() == settled
            assert d6.requests.count(json_url("otherkit/gone")) == 1
        assert metadata("Otherkit")["link_seeds"] == [[json_url("otherkit/gone"), "Otherkit", other]]

    @pytest.mark.parametrize("late", ["umbrella/guide.json", "thirdkit.json"])
    async def test_a_link_seed_is_the_same_whichever_linking_page_comes_first(self, d6: D6Runs, late: str) -> None:
        pages: Pages = {**UMBRELLA, **OTHERKIT, "Otherkit/hidden": (A, []),
                        "Umbrella/guide": (A, [("Otherkit/hidden", "com.apple.x")]),
                        "Thirdkit": ("com.apple.t", [("Otherkit/hidden", "com.apple.y")])}
        assert await d6.scrape(pages, ["Umbrella", "Otherkit", "Thirdkit"], delays={late: 0.2}) == 0
        assert metadata("Otherkit")["link_seeds"] == [[json_url("otherkit/hidden"), "Otherkit", "com.apple.x"]]

    async def test_a_run_whose_root_fails_keeps_the_seeds(self, d6: D6Runs) -> None:
        """No own reach without a root: the seeds stay as stored, not every page of the sink."""
        listed = ["Sibkit", "SibkitUI"]
        # SibkitUI also links pages Sibkit's own crawl reaches: a (a handoff link,
        # with a link of its own) and b2 (another bundle's)
        pages: Pages = {**SIBLINGS, "Sibkit": (S, [("Sibkit/a", S), ("Sibkit/b2", S)]),
                        "Sibkit/a": (S, [("Sibkit/a/child", S)]), "Sibkit/a/child": (S, []), "Sibkit/b2": (S, []),
                        "SibkitUI/b": (S, [("Sibkit/a", S), ("Sibkit/b2", "com.apple.other")])}
        for _ in range(2):
            assert await d6.scrape(pages, listed, concurrent=1) == 0
        before = metadata("Sibkit")
        assert set(before["handoff_links"]) == {json_url("sibkit/hidden")} and "link_seeds" not in before
        assert await d6.scrape(pages, listed, overrides={"Sibkit": [status(503)]}, concurrent=1) != 0
        after = metadata("Sibkit")
        assert after["handoff_links"] == before["handoff_links"] and "link_seeds" not in after

    async def test_a_link_healed_by_a_redirect_or_a_removal_pending_is_no_gap(self, d6: D6Runs) -> None:
        """The release run's 259: 213 link references to old URLs (numeric ids, underscores)
        already linked where Apple's web page redirects, and 41 whose web page answered 404
        once (removed: their text on the next run), were counted; neither is a crawl gap."""
        guide = json.loads(topic_page("Umbrella/guide", A, []))
        old, removed = doc_url("umbrella/1402872-back"), doc_url("umbrella/removed")
        guide["abstract"] = [{"type": "reference", "identifier": url, "isActive": True} for url in (old, removed)]
        guide["references"].update({url: {"type": "link", "identifier": url, "title": url.rsplit("/", 1)[-1],
                                          "url": url} for url in (old, removed)})
        overrides = {"Umbrella/guide": [ok(json.dumps(guide), "E-guide")]}
        redirects = {old: "/documentation/umbrella/back"}
        assert await d6.scrape(UMBRELLA, ["Umbrella"], overrides=overrides, redirects=redirects) == 0
        assert "[1402872-back](./back.md)" in doc_file("Umbrella/guide").read_text()
        assert d6.logged("link_coverage")[0]["gaps"] == 0
        # On the next run the removed page is its text (two 404s in a row); still no gap
        assert await d6.scrape(UMBRELLA, ["Umbrella"], overrides=overrides, redirects=redirects) == 0
        assert "[1402872-back](./back.md)" in doc_file("Umbrella/guide").read_text()
        assert "](./removed.md)" not in doc_file("Umbrella/guide").read_text()
        assert d6.logged("link_coverage")[0]["gaps"] == 0


def implementation_files(path: str) -> List[Path]:
    """The files a page's ## Default Implementations section links, each resolved from the page's own file."""
    file = doc_file(path)
    section = file.read_text().split("\n## Default Implementations\n", 1)[1].split("\n## ", 1)[0]
    return [Path(os.path.normpath(file.parent / unquote(href))) for href in re.findall(r"\]\(([^)\s]+\.md)\)", section)]


# A protocol requirement and its default implementations, which only its
# defaultImplementationsSections link (1.4): one in Umbrella, one in its module ModKit
REQUIREMENT: Pages = {
    **UMBRELLA,
    "Umbrella/guide": (A, [("Umbrella/Proto", A)]),
    "Umbrella/Proto": (A, [("Umbrella/Proto/run()", A)]),
    "Umbrella/Proto/run()": (A, []),
    "Umbrella/Proto/run()-1xq7p": (A, []),
    "ModKit/Thing/run()-3ngto": (A, []),
}
IMPLEMENTATIONS: Dict[str, List[Link]] = {
    "Umbrella/Proto/run()": [("Umbrella/Proto/run()-1xq7p", A), ("ModKit/Thing/run()-3ngto", A)],
}


class TestDefaultImplementations:
    """A protocol requirement's default implementations are crawled (1.4): its own, a module's, a sibling's."""

    async def test_they_are_discovered_written_and_removed_once_no_longer_listed(self, d6: D6Runs) -> None:
        assert await d6.scrape(REQUIREMENT, ["Umbrella"], implementations=IMPLEMENTATIONS) == 0
        assert docs() == {doc_file(path) for path in REQUIREMENT}
        assert "**Framework**: ModKit" in doc_file("ModKit/Thing/run()-3ngto").read_text()
        # The requirement's own file keeps its name, and its links reach its default
        # implementations; ModKit's dir is new this run, yet its page is linked locally (the
        # module dirs a page's own links route to, _module_link_dirs, item 4)
        assert doc_file("Umbrella/Proto/run()") == Path("documentation/Umbrella/proto/run().md")
        assert implementation_files("Umbrella/Proto/run()") == [
            doc_file("Umbrella/Proto/run()-1xq7p"), doc_file("ModKit/Thing/run()-3ngto")]
        assert f"]({doc_url('modkit/thing/run()-3ngto')})" not in doc_file("Umbrella/Proto/run()").read_text()
        assert json_url("umbrella/proto/run()-1xq7p") in Config.get_hash_file("Umbrella").read_text()
        before = sandbox_bytes()
        assert await d6.scrape(REQUIREMENT, ["Umbrella"], implementations=IMPLEMENTATIONS) == 0
        assert sandbox_bytes() == before
        # No longer listed: each leaves through its sink's normal orphan cleanup
        assert await d6.scrape(REQUIREMENT, ["Umbrella"], implementations={
            "Umbrella/Proto/run()": [("ModKit/Thing/run()-3ngto", A)]}) == 0
        assert docs() == {doc_file(path) for path in REQUIREMENT} - {doc_file("Umbrella/Proto/run()-1xq7p")}
        assert await d6.scrape(REQUIREMENT, ["Umbrella"]) == 0
        assert docs() == {doc_file(path) for path in UMBRELLA} | {
            doc_file("Umbrella/Proto"), doc_file("Umbrella/Proto/run()")}
        assert "## Default Implementations" not in doc_file("Umbrella/Proto/run()").read_text()

    async def test_one_in_a_bundle_sibling_is_handed_off_and_cleaned_only_when_its_writer_ran(
        self, d6: D6Runs
    ) -> None:
        """Swift's Equatable.==(_:_:) lists Distributed's DistributedActor.==(_:_:), which no Distributed page links."""
        listed = ["Sibkit", "SibkitUI"]
        pages: Pages = {
            "Sibkit": (S, [("Sibkit/a", S)]),
            "Sibkit/a": (S, []),
            "Sibkit/a/run()-6673q": (S, [("Sibkit/a/run()-6673q/deeper", S)]),
            "Sibkit/a/run()-6673q/deeper": (S, []),
            "SibkitUI": (S, [("SibkitUI/b", S)]),
            "SibkitUI/b": (S, [("SibkitUI/b/run()", S)]),
            "SibkitUI/b/run()": (S, []),
        }
        implementations: Dict[str, List[Link]] = {"SibkitUI/b/run()": [("Sibkit/a/run()-6673q", S)]}
        assert await d6.scrape(pages, listed, implementations=implementations) == 0
        handed_off = doc_file("Sibkit/a/run()-6673q")
        assert handed_off.exists() and "**Framework**: Sibkit" in handed_off.read_text()
        assert implementation_files("SibkitUI/b/run()") == [handed_off]
        # The handed-off page's own links in Sibkit are Sibkit's job's: taken at the
        # end of its crawl, or from the seeds the page left (the next run at most)
        assert await d6.scrape(pages, listed, implementations=implementations) == 0
        assert d6.requests.count(json_url("sibkit/a/run()-6673q/deeper")) == 1
        deeper = doc_file("Sibkit/a/run()-6673q/deeper")
        assert "**Framework**: Sibkit" in deeper.read_text()
        assert metadata("Sibkit")["handoff_from"] == {"sibkitui": {}}
        assert json_url("sibkit/a/run()-6673q") in Config.get_hash_file("Sibkit").read_text()
        assert json_url("sibkit/a/run()-6673q") not in Config.get_hash_file("SibkitUI").read_text()
        before = sandbox_bytes()
        assert await d6.scrape(pages, listed, implementations=implementations) == 0
        assert sandbox_bytes() == before
        # Sibkit alone: its handoff writer didn't run, so the page it alone reaches stays (rule 1)
        assert await d6.scrape(pages, listed, "Sibkit") == 0
        assert handed_off.exists() and deeper.exists()
        assert d6.logged("orphans_deleted") == []
        # No longer listed, with both jobs clean: removed by the normal orphan cleanup
        # (the page, then what only its seeds still reached)
        for _ in range(3):
            assert await d6.scrape(pages, listed) == 0
        assert not handed_off.exists() and not deeper.exists() and doc_file("Sibkit/a").exists()


def overload_page(path: str, members: Sequence[str], group: bool, links: Sequence[Link] = (), bundle: str = A) -> str:
    """An overload's page (B4): its declaration lists the other overloads (otherDeclarations),
    each resolved through its references. group: the group's page (DocC's externalID
    ending in ::OverloadGroup), a copy of the preferred overload's."""
    body = json.loads(topic_page(path, bundle, links))
    name = path.split("/")[-1]
    body["metadata"]["externalID"] = f"s:7Umbrella4TextV{name}" + ("::OverloadGroup" if group else "")
    others = []
    for member in members:
        identifier = f"doc://{bundle}/documentation/{member}"
        others.append({"identifier": identifier,
                       "tokens": [{"kind": "keyword", "text": "init"}, {"kind": "text", "text": f"({member[-5:]})"}]})
        body["references"][identifier] = {"type": "topic", "url": f"/documentation/{member.lower()}",
                                          "title": "init(_:)", "identifier": identifier, "kind": "symbol",
                                          "role": "symbol"}
    body["primaryContentSections"] = [{"kind": "declarations", "declarations": [{
        "languages": ["swift"], "platforms": ["iOS"],
        "tokens": [{"kind": "keyword", "text": "init"}, {"kind": "text", "text": f"({name})"}],
        "otherDeclarations": {"displayIndex": 0, "declarations": others}}]}]
    return json.dumps(body)


GROUP = "Umbrella/Text/init(_:)"
PREFERRED = "Umbrella/Text/init(_:)-1a4oh"
MEMBERS = ["Umbrella/Text/init(_:)-9d1g4", "Umbrella/Text/init(_:)-4k7ab"]
# Umbrella/guide links an overload inline (its dead link before B4)
OVERLOADS: Pages = {
    **UMBRELLA,
    "Umbrella/guide": (A, [("Umbrella/Text", A)]),
    "Umbrella/Text": (A, [(GROUP, A)]),
}


def overload_routes(members: Sequence[str] = tuple(MEMBERS)) -> Dict[str, List[Spec]]:
    """The group's page lists members; each member's own page lists its siblings and
    the preferred overload (whose page, a copy of the group's, is never crawled)."""
    routes: Dict[str, List[Spec]] = {
        GROUP: [ok(overload_page(GROUP, members, group=True), "")],
        PREFERRED: [ok(overload_page(PREFERRED, MEMBERS, group=False), "")],
    }
    for member in MEMBERS:
        routes[member] = [ok(overload_page(member, [PREFERRED, *(m for m in MEMBERS if m != member)],
                                           group=False), "")]
    guide = json.loads(topic_page("Umbrella/guide", A, [("Umbrella/Text", A)]))
    identifier = f"doc://{A}/documentation/{MEMBERS[0]}"
    guide["abstract"] = [{"type": "text", "text": "Use "}, {"type": "reference", "identifier": identifier,
                                                            "isActive": True}]
    guide["references"][identifier] = {"type": "topic", "url": f"/documentation/{MEMBERS[0].lower()}",
                                       "title": "init(_:)", "identifier": identifier, "kind": "symbol",
                                       "role": "symbol"}
    routes["Umbrella/guide"] = [ok(json.dumps(guide), "")]
    return routes


class TestOverloadGroups:
    """B4-a: an overload group's page links its other overloads, each crawled and saved
    as a page of its own; an overload's own page links none of its siblings."""

    @staticmethod
    def cross_linked(*targets: str) -> Pages:
        """OVERLOADS, with Otherbrella's page linking targets in Umbrella from another bundle
        (as Updates/swiftui links SwiftUI's preferred overloads): no scope follows them."""
        return {**OVERLOADS, "Otherbrella": (B, [(target, A) for target in targets])}

    async def test_a_preferred_overload_linked_from_another_bundle_is_never_a_seed(self, d6: D6Runs) -> None:
        """Its page is a copy of its group's (B4): never stored as a seed, never fetched, no
        file, over two runs, and no coverage gap; a non-preferred one is the group's, fetched once."""
        listed = ["Umbrella", "Otherbrella"]
        pages = self.cross_linked(PREFERRED, MEMBERS[1])
        for _ in range(2):
            assert await d6.scrape(pages, listed, overrides=overload_routes()) == 0
            assert json_url(PREFERRED.lower()) not in d6.requests and not doc_file(PREFERRED).exists()
            assert d6.requests.count(json_url(MEMBERS[1].lower())) == 1 and doc_file(MEMBERS[1]).exists()
            assert "link_seeds" not in metadata("Umbrella")
            assert d6.logged("link_coverage")[0]["gaps"] == 0

    async def test_a_preferred_overload_seed_an_older_run_stored_is_dropped_and_its_copy_removed(
        self, d6: D6Runs
    ) -> None:
        """A seed run 2 of the 059042bb1d6 release stored (its copy fetched and saved): never
        fetched again, dropped from the seeds, and its copy removed by the normal orphan cleanup."""
        listed = ["Umbrella", "Otherbrella"]
        pages = self.cross_linked(PREFERRED)
        # The older rule: no preferred-overload check
        with mock.patch("scraper.json_scraper.preferred_overload", lambda *args, **kwargs: False):
            for _ in range(2):
                assert await d6.scrape(pages, listed, overrides=overload_routes()) == 0
        assert metadata("Umbrella")["link_seeds"] == [[json_url(PREFERRED.lower()), "Umbrella", A]]
        assert doc_file(PREFERRED).exists()
        assert await d6.scrape(pages, listed, overrides=overload_routes()) == 0
        assert json_url(PREFERRED.lower()) not in d6.requests and "link_seeds" not in metadata("Umbrella")
        assert not doc_file(PREFERRED).exists() and doc_file(GROUP).exists()

    async def test_a_group_page_that_is_a_handoff_page_keeps_its_overloads_as_seeds(self, d6: D6Runs) -> None:
        """A group's page only a bundle sibling links (a handoff page, out of its own crawl's
        reach, with a file): its listed overloads are its handoff links, fetched by its own
        job every run and kept; the preferred-overload rule applies only to a group in reach."""
        group, members = "Sibkit/Text/init(_:)", ["Sibkit/Text/init(_:)-9d1g4", "Sibkit/Text/init(_:)-4k7ab"]
        pages: Pages = {**SIBLINGS, "SibkitUI": (S, [("SibkitUI/b", S), (group, S)])}
        routes = {group: [ok(overload_page(group, members, group=True, bundle=S), "")]}
        for member in members:
            routes[member] = [ok(overload_page(member, [m for m in members if m != member], group=False, bundle=S), "")]
        listed = ["Sibkit", "SibkitUI"]
        for _ in range(4):
            assert await d6.scrape(pages, listed, overrides=routes) == 0
        assert doc_file(group).exists() and all(doc_file(member).exists() for member in members)
        assert sorted(entry[0] for entry in metadata("Sibkit")["handoff_links"][json_url(group.lower())]) == sorted(
            json_url(member.lower()) for member in members)
        assert d6.logged("orphans_deleted") == [] and d6.logged("link_coverage")[0]["gaps"] == 0
        before = sandbox_bytes()
        assert await d6.scrape(pages, listed, overrides=routes) == 0
        assert sandbox_bytes() == before

    def test_only_a_group_page_links_its_other_overloads(self, dirs: Path) -> None:
        scraper = AppleJSONDocumentationScraper("Umbrella")
        group = scraper._page_links(json.loads(overload_page(GROUP, MEMBERS, group=True, links=[("Umbrella", A)])))
        assert [link.json_url for link in group.links] == [
            json_url("umbrella"), *(json_url(member.lower()) for member in MEMBERS)]
        member = scraper._page_links(json.loads(overload_page(MEMBERS[0], [PREFERRED, MEMBERS[1]], group=False)))
        assert member.links == ()
        # Its occ view's declarations are read the same way
        body = json.loads(overload_page(GROUP, [], group=True))
        occ_member = "Umbrella/Text/init(_:)-0cc01"
        body["references"][f"doc://{A}/documentation/{occ_member}"] = {
            "type": "topic", "url": f"/documentation/{occ_member.lower()}", "title": "init"}
        body["variantOverrides"] = [{"traits": [{"interfaceLanguage": "occ"}], "patch": [
            {"op": "add", "path": "/primaryContentSections/0/declarations/0/otherDeclarations/declarations/0",
             "value": {"identifier": f"doc://{A}/documentation/{occ_member}", "tokens": []}}]}]
        links = scraper._page_links(body, scraper._occ_view(body)).links
        assert [link.json_url for link in links] == [json_url(occ_member.lower())]

    async def test_the_overloads_are_crawled_kept_and_removed_with_the_group(self, d6: D6Runs) -> None:
        assert await d6.scrape(OVERLOADS, ["Umbrella"], overrides=overload_routes()) == 0
        assert docs() == {doc_file(path) for path in (*OVERLOADS, GROUP, *MEMBERS)}
        # Named like any page: the group's init(_).md, each overload's with its suffix
        assert doc_file(MEMBERS[0]) == Path("documentation/Umbrella/text/init(_)-9d1g4.md")
        assert doc_file(GROUP) == Path("documentation/Umbrella/text/init(_).md")
        # The preferred overload's page (a copy of the group's) is never fetched
        assert json_url(PREFERRED.lower()) not in d6.requests
        member = doc_file(MEMBERS[0]).read_text()
        assert "**Framework**: Umbrella" in member and "**Other overloads**:" in member
        # The inline link to an overload is to its file (it was a dead link before B4)
        guide = doc_file("Umbrella/guide")
        link = re.search(r"Use \[`?init\(_:\)`?\]\(([^)]+\.md)\)", guide.read_text())
        assert link is not None and (guide.parent / unquote(link.group(1))).resolve() == doc_file(MEMBERS[0]).resolve()
        hashes = Config.get_hash_file("Umbrella").read_text()
        assert all(json_url(path.lower()) in hashes for path in MEMBERS)

        # Reached again through the group every run: nothing changes
        before = sandbox_bytes()
        assert await d6.scrape(OVERLOADS, ["Umbrella"], overrides=overload_routes()) == 0
        assert sandbox_bytes() == before

        # Apple drops an overload from the group: removed by the normal orphan cleanup
        assert await d6.scrape(OVERLOADS, ["Umbrella"], overrides=overload_routes(MEMBERS[:1])) == 0
        assert docs() == {doc_file(path) for path in (*OVERLOADS, GROUP, MEMBERS[0])}
        assert json_url(MEMBERS[1].lower()) not in Config.get_hash_file("Umbrella").read_text()
        # The group goes: so do its overloads, but the one the guide links inline,
        # which is still Apple's page (an inline link no curation reaches is followed)
        assert await d6.scrape(without(OVERLOADS, "Umbrella/Text", GROUP), ["Umbrella"],
                               overrides=overload_routes()) == 0
        assert docs() == {doc_file(path) for path in (*OVERLOADS, MEMBERS[0])}


def occ_curation(
    links: Sequence[Link], references: str = "per-key", broken: bool = False, title: str = "Functions"
) -> List[Dict[str, Any]]:
    """An occ variant's patch, as Apple's: its own curation (/topicSections, replaced
    wholesale) and references, and operations on keys the view leaves out (1.5).

    Each link's reference is titled "<name>Ref", the Objective-C/C name only the
    occ variant has. references: how they reach it: per key (CGContext, Network)
    or in a whole /references (IOKit's root); broken: an operation on a reference
    that doesn't exist (the view can't be built)
    """
    identifiers = [f"doc://{bundle}/documentation/{path}" for path, bundle in links]
    refs = {
        identifier: {"type": "topic", "url": f"/documentation/{path.lower()}", "title": f"{path.split('/')[-1]}Ref",
                     "identifier": identifier, "kind": "symbol", "role": "symbol"}
        for identifier, (path, _) in zip(identifiers, links)
    }
    ops: List[Dict[str, Any]] = [
        {"op": "replace", "path": "/identifier/interfaceLanguage", "value": "occ"},
        # Keys the view leaves out: these would fail it
        {"op": "replace", "path": "/hierarchy/paths/0", "value": []},
        {"op": "replace", "path": "/variants/3/paths", "value": []},
        {"op": "replace", "path": "/topicSections", "value": [{"title": title, "identifiers": identifiers}]},
    ]
    if references == "whole":
        ops.append({"op": "replace", "path": "/references", "value": refs})
    else:
        ops.extend({"op": "add", "path": "/references/" + identifier.replace("~", "~0").replace("/", "~1"), "value": ref}
                   for identifier, ref in refs.items())
    if broken:
        ops.append({"op": "replace", "path": "/references/doc:~1~1com.apple.umbrella~1documentation~1Gone/title",
                    "value": "Gone"})
    return ops


# Umbrella/guide lists Umbrella/shared in both curations; only its Objective-C/C
# curation lists Umbrella/CThing and its module's ModKit/CThing (1.5)
OBJC: Pages = {
    **UMBRELLA,
    "Umbrella/guide": (A, [("Umbrella/shared", A)]),
    "Umbrella/shared": (A, []),
    "Umbrella/CThing": (A, []),
    "ModKit/CThing": (A, []),
}
OBJC_LINKS: List[Link] = [("Umbrella/shared", A), ("Umbrella/CThing", A), ("ModKit/CThing", A)]
OBJC_ONLY = {doc_file("Umbrella/CThing"), doc_file("ModKit/CThing")}
OBJC_ID = "doc://com.apple.umbrella/documentation/Umbrella/CThing"


class TestObjectiveCCuration:
    """1.5 (D1): the pages only a page's Objective-C/C variant (occ) curates are crawled through
    its occ view, built once per page; a view that can't be built is a local error that keeps them."""

    def test_the_links_are_the_union_of_both_curations_through_the_patched_references(self, dirs: Path) -> None:
        scraper = AppleJSONDocumentationScraper("Umbrella")
        for references in ("per-key", "whole"):
            page = json.loads(topic_page("Umbrella/guide", A, [("Umbrella/shared", A)],
                                         occ=occ_curation(OBJC_LINKS, references)))
            # Without the view: the Swift curation only
            assert scraper._extract_urls_from_json_data(page) == [json_url("umbrella/shared")]
            view = scraper._occ_view(page)
            assert view is not None and view["references"] is not page["references"]
            # The Swift links first, then the occ-only ones, each once; the page is never changed
            links = scraper._page_links(page, view)
            assert [link.json_url for link in links.links] == [
                json_url("umbrella/shared"), json_url("umbrella/cthing"), json_url("modkit/cthing")]
            assert page["topicSections"][0]["identifiers"] == ["doc://com.apple.umbrella/documentation/Umbrella/shared"]
            assert "doc://com.apple.umbrella/documentation/Umbrella/CThing" not in page["references"]
        # No occ operation on the view's keys: no view (its curation is the Swift one)
        page = json.loads(topic_page("Umbrella/guide", A, [("Umbrella/shared", A)], occ=[
            {"op": "replace", "path": "/metadata/title", "value": "guideRef"}]))
        assert scraper._occ_view(page) is None
        # A whole-document replace (76 pages, e.g. IOKit's root): its curation and references
        whole = json.loads(topic_page("Umbrella/guide", A, [("Umbrella/CThing", A)]))
        page = json.loads(topic_page("Umbrella/guide", A, [("Umbrella/shared", A)], occ=[
            {"op": "replace", "path": "", "value": whole},
            {"op": "replace", "path": "/metadata/missing/title", "value": "x"}]))
        assert [link.json_url for link in scraper._page_links(page, scraper._occ_view(page)).links] == [
            json_url("umbrella/shared"), json_url("umbrella/cthing")]

    def test_a_view_that_cant_be_built_still_gives_the_links_its_operations_list(self, dirs: Path) -> None:
        scraper = AppleJSONDocumentationScraper("Umbrella")
        for references in ("per-key", "whole"):
            page = json.loads(topic_page("Umbrella/guide", A, [("Umbrella/shared", A)],
                                         occ=occ_curation(OBJC_LINKS, references, broken=True)))
            with pytest.raises(OccViewError, match="^occ view: KeyError"):
                scraper._occ_view(page)
            # Read from the operations' values, resolved through the references their values update
            links = scraper._page_links(page, scraper._occ_fallback(page))
            assert [link.json_url for link in links.links] == [
                json_url("umbrella/shared"), json_url("umbrella/cthing"), json_url("modkit/cthing")]
            assert scraper.reference_fallbacks == 0
        # A section's identifiers added one by one, a reference's url patched field by field
        cthing = "doc://com.apple.umbrella/documentation/Umbrella/CThing"
        page = json.loads(topic_page("Umbrella/guide", A, [("Umbrella/CThing", A)], occ=[
            {"op": "add", "path": "/topicSections/0/identifiers/-", "value": "doc://com.apple.umbrella/documentation/X"},
            {"op": "replace", "path": "/references/" + cthing.replace("/", "~1") + "/url",
             "value": "/documentation/umbrella/cthing-objc"},
            "not an operation",
            {"op": "remove", "path": "/topicSections/1"},
        ]))
        with pytest.raises(OccViewError):
            scraper._occ_view(page)
        assert [link.json_url for link in scraper._page_links(page, scraper._occ_fallback(page)).links] == [
            json_url("umbrella/cthing"), json_url("x")]
        assert scraper._occ_fallback({"variantOverrides": "occ"}) == {
            "topicSections": [{"identifiers": []}], "references": {}}

    def test_the_occ_only_links_are_rendered_in_their_occ_groups(self, dirs: Path) -> None:
        scraper = AppleJSONDocumentationScraper("Umbrella")
        page = json.loads(topic_page("Umbrella/guide", A, [("Umbrella/shared", A)]))
        page["topicSections"][0]["title"] = "Functions"
        shared = "doc://com.apple.umbrella/documentation/Umbrella/shared"
        page["relationshipsSections"] = [{"title": "Conforms To", "type": "conformsTo", "identifiers": [shared]}]
        occ = occ_curation(OBJC_LINKS)
        macro = "doc://com.apple.umbrella/documentation/Umbrella/MACRO"
        occ[3]["value"].append({"title": "Macros", "identifiers": [macro, shared]})
        occ.append({"op": "add", "path": "/references/" + macro.replace("/", "~1"), "value": {
            "type": "topic", "url": "/documentation/umbrella/macro", "title": "MACRO", "kind": "symbol",
            "role": "symbol", "abstract": [{"type": "text", "text": "A macro."}]}})
        occ.append({"op": "replace", "path": "/relationshipsSections", "value": [
            {"title": "Conforms To", "type": "conformsTo", "identifiers": [shared, macro]},
            {"title": "Inherits From", "type": "inheritsFrom", "identifiers": [macro, OBJC_ID]}]})
        page["variantOverrides"] = [{"traits": [{"interfaceLanguage": "occ"}], "patch": occ}]
        data = scraper._extract_from_json(scraper.sink, page, doc_url("umbrella/guide"), scraper._occ_view(page))
        # Swift's group first; the occ-only links join the group of the same title, the others follow
        assert [(group["title"], [item["name"] for item in group["items"]]) for group in data["topics"]] == [
            ("Functions", ["shared", "CThingRef", "CThingRef"]), ("Macros", ["MACRO"])]
        assert data["topics"][1]["items"][0]["description"] == "A macro."
        assert [(group["title"], [item["name"] for item in group["items"]]) for group in data["relationships"]] == [
            ("Conforms To", ["shared", "MACRO"]), ("Inherits From", ["CThingRef"])]
        assert data["see_also"] == [] and data["default_implementations"] == []
        # Without its view, the page shows its Swift curation only
        data = scraper._extract_from_json(scraper.sink, page, doc_url("umbrella/guide"), None)
        assert [len(group["items"]) for group in data["topics"]] == [1]

    async def test_objc_only_pages_are_added_rendered_and_removed_with_the_curation(
        self, d6: D6Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        patched: List[Any] = []
        real = json_scraper.apply_json_patch

        def counted(document: Any, patch: List[Dict[str, Any]]) -> Any:
            patched.append(document)
            return real(document, patch)

        monkeypatch.setattr(json_scraper, "apply_json_patch", counted)
        occ = {"Umbrella/guide": occ_curation(OBJC_LINKS)}
        assert await d6.scrape(OBJC, ["Umbrella"], occ=occ) == 0
        assert docs() == {doc_file(path) for path in OBJC}
        assert "**Framework**: ModKit" in doc_file("ModKit/CThing").read_text()
        # The guide's one fetch built its occ view once, for its links and its file
        assert len(patched) == 1
        guide = doc_file("Umbrella/guide").read_text()
        topics = guide.split("## Topics", 1)[1]
        assert topics.count("(./shared.md)") == 1 and topics.index("### Topics") < topics.index("### Functions")
        assert "- [CThingRef](./cthing.md)" in topics
        assert d6.logged("page_save_failed") == []
        before = sandbox_bytes()
        assert await d6.scrape(OBJC, ["Umbrella"], occ=occ) == 0
        assert sandbox_bytes() == before
        # Apple drops the Objective-C/C curation: its pages leave through the normal orphan cleanup
        assert await d6.scrape(OBJC, ["Umbrella"]) == 0
        assert docs() == {doc_file(path) for path in OBJC} - OBJC_ONLY
        assert "CThing" not in doc_file("Umbrella/guide").read_text()

    async def test_a_view_that_cant_be_built_keeps_its_objc_pages_through_3_runs(self, d6: D6Runs) -> None:
        """A local error: it blocks 2 runs, then flags the 3rd, whose cleanup runs; the
        pages only its occ variant links are kept every run. A later clean run, the page unchanged, resets its count."""
        assert await d6.scrape(OBJC, ["Umbrella"], occ={"Umbrella/guide": occ_curation(OBJC_LINKS)}) == 0
        stray = Path("documentation/Umbrella/stray.md")
        stray.write_text("# stray\n")
        broken = {"Umbrella/guide": occ_curation(OBJC_LINKS, broken=True)}
        guide = json_url("umbrella/guide")
        stored = json.loads(Config.get_hash_file("Umbrella").read_text())["hashes"][guide]["hash"]
        for run in (1, 2, 3):
            assert await d6.scrape(OBJC, ["Umbrella"], occ=broken) == 1
            assert [e["url"] for e in d6.logged("page_save_failed")] == [guide]
            assert d6.logged("error_processing_url") == []
            entry = json.loads(Config.get_hash_file("Umbrella").read_text())["hashes"][guide]
            assert entry["consecutive_local_errors"] == run and entry["hash"] == stored
            assert docs() >= OBJC_ONLY
            # Blocked twice; the 3rd run's cleanup runs
            assert stray.exists() == (run < 3)
        assert [e["url"] for e in d6.logged("persistent_local_error")] == [guide]
        # Apple's variant is fine again (the page as stored: unchanged)
        assert await d6.scrape(OBJC, ["Umbrella"], occ={"Umbrella/guide": occ_curation(OBJC_LINKS)}) == 0
        entry = json.loads(Config.get_hash_file("Umbrella").read_text())["hashes"][guide]
        assert "consecutive_local_errors" not in entry and entry["hash"] == stored
        assert docs() == {doc_file(path) for path in OBJC}

    async def test_a_stored_unchanged_page_whose_view_cant_be_built_is_a_local_error(
        self, d6: D6Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Saved before 1.5, unchanged since: its one request reads the links."""
        broken = {"Umbrella/guide": occ_curation(OBJC_LINKS, broken=True)}
        with monkeypatch.context() as before_d1:
            before_d1.setattr(AppleJSONDocumentationScraper, "_occ_view", lambda self, data: None)
            assert await d6.scrape(OBJC, ["Umbrella"], occ=broken) == 0
        assert not docs() & OBJC_ONLY
        guide = json_url("umbrella/guide")
        for run in (1, 2, 3):
            assert await d6.scrape(OBJC, ["Umbrella"], occ=broken) == 1
            assert d6.requests.count(guide) == 1  # one unconditional GET
            assert d6.logged("error_processing_url") == []
            entry = json.loads(Config.get_hash_file("Umbrella").read_text())["hashes"][guide]
            assert entry["consecutive_local_errors"] == run
            assert docs() == {doc_file(path) for path in OBJC}


class TestNamespaceCollision:
    """No Apple technology or module may take another scraper's top-level dir."""

    def test_the_other_scrapers_dirs_come_from_their_configs(self, tmp_path: Path) -> None:
        dirs = scrape_all_frameworks.other_scraper_dirs()
        assert {"hig", "swift-book", "mlx", "mlx-swift", "coremltools"} <= set(dirs)
        assert dirs["mlx-swift"] == "MLX-Swift"
        scripts = tmp_path / "scripts"
        scripts.mkdir()
        (scripts / "scrape_mlx_docs.py").write_text('S = [Source(output_dir="Kit/sub"), Source(output_dir="Two")]\n')
        (scripts / "scrape_swift_docs.py").write_text('OUTPUT_DIR = Path(__file__).parent / "documentation" / "Book"\n')
        (scripts / "scrape_hig_docs.py").write_text('OUTPUT_DIR = Path(__file__).parent / "documentation"\n')
        with pytest.raises(ValueError):
            scrape_all_frameworks.other_scraper_dirs(scripts, import_mlx=False)
        (scripts / "scrape_hig_docs.py").write_text('OUTPUT_DIR = BASE / "documentation" / "HIG"\n')
        assert scrape_all_frameworks.other_scraper_dirs(scripts, import_mlx=False) == {
            "kit": "Kit", "two": "Two", "book": "Book", "hig": "HIG"}

    def test_the_mlx_scrapers_configured_sources_and_its_literal_dirs_agree(self) -> None:
        """Where wafer-py is missing, the MLX source's literal output_dirs stand in for configured_sources()."""
        pytest.importorskip("wafer")
        assert scrape_all_frameworks.other_scraper_dirs() == scrape_all_frameworks.other_scraper_dirs(import_mlx=False)

    async def test_a_colliding_technology_or_module_is_refused(self, d6: D6Runs) -> None:
        pages: Pages = {**UMBRELLA, "Umbrella/guide": (A, [("MLX", A)]), "MLX": (A, []), "HIG": (A, [])}
        assert await d6.scrape(pages, ["Umbrella", "HIG"]) == 1
        assert not (Path("documentation") / "MLX").exists() and not (Path("documentation") / "HIG").exists()
        assert json_url("mlx") not in d6.requests and json_url("hig") not in d6.requests
        assert sorted(e["dir"] for e in d6.logged("namespace_collision")) == ["HIG", "MLX"]
        assert doc_file("ModKit/Thing").exists()


    async def test_unreadable_other_scraper_dirs_stop_the_run(self, d6: D6Runs) -> None:
        """Without the reserved dirs nothing is routed: the run stops before any page is written."""
        def unreadable(*args: object, **kwargs: object) -> Dict[str, str]:
            raise OSError("scripts/scrape_hig_docs.py: unreadable")

        d6.monkeypatch.setattr(scrape_all_frameworks, "other_scraper_dirs", unreadable)
        assert await d6.scrape(UMBRELLA, ["Umbrella"]) == 2
        assert not doc_file("Umbrella/guide").exists() and not d6.requests

class TestStaleErrorEntries:
    """Item 8: a section anchor's URL is never requested; its old error entry leaves through the cleanup."""

    async def test_anchors_are_their_pages_and_unlinked_error_entries_are_dropped(self, d6: D6Runs) -> None:
        pages: Pages = {**UMBRELLA, "Umbrella": (A, [("Umbrella/guide#a-section", A), ("ModKit", A)])}
        assert await d6.scrape(pages, ["Umbrella"]) == 0
        assert not any("#" in url for url in d6.requests)
        assert doc_file("Umbrella/guide").exists()
        # What earlier runs left: an anchor's 404, and a module page under its umbrella's id
        hash_file = Config.get_hash_file("Umbrella")
        data = json.loads(hash_file.read_text())
        stale = [json_url("umbrella/guide#a-section"), json_url("umbrella/modkit")]
        for url in stale:
            data["hashes"][url] = {"status": "error", "error": "HTTP 404"}
        # A never-good failure's count: no page links it any more, so its streak
        # ends (the reset drops the count) and the entry goes too
        flaky = json_url("umbrella/flaky")
        data["hashes"][flaky] = {"status": "error", "error": "HTTP 502", "consecutive_failures": 1}
        # A local error's count isn't reset by a run that doesn't reach the page: kept
        local = json_url("umbrella/local")
        data["hashes"][local] = {"status": "error", "error": "local error: x", "consecutive_local_errors": 1}
        hash_file.write_text(json.dumps(data))
        assert await d6.scrape(pages, ["Umbrella"]) == 0
        hashes = json.loads(hash_file.read_text())["hashes"]
        assert not {*stale, flaky} & set(hashes)
        assert hashes[local] == {"status": "error", "error": "local error: x", "consecutive_local_errors": 1}
        assert [e["dropped"] for e in d6.logged("dropped_stale_error_entries")] == [3]

    def test_an_error_entry_with_a_run_count_is_never_stale(self, dirs: Path) -> None:
        """Every run counter keeps its error entry, the 404/410 count (consecutive_gone) too."""
        write_hash_file("Umbrella", {
            **{json_url(f"umbrella/{counter}"): {"status": "error", "error": "HTTP 404", counter: 1}
               for counter in COUNTER_FIELDS},
            json_url("umbrella/plain"): {"status": "error", "error": "HTTP 404"},
        })
        sink = SinkRegistry().get(APPLE, "Umbrella", "Umbrella", None)
        assert "consecutive_gone" in COUNTER_FIELDS
        assert json_scraper.stale_error_entries(sink) == [json_url("umbrella/plain")]

    async def test_a_blocked_run_drops_nothing(self, d6: D6Runs) -> None:
        assert await d6.scrape(UMBRELLA, ["Umbrella"]) == 0
        hash_file = Config.get_hash_file("Umbrella")
        data = json.loads(hash_file.read_text())
        data["hashes"][json_url("umbrella/gone")] = {"status": "error", "error": "HTTP 404"}
        hash_file.write_text(json.dumps(data))
        assert await d6.scrape(UMBRELLA, ["Umbrella"], overrides={"Umbrella/guide": [status(502)]}) == 1
        assert json_url("umbrella/gone") in json.loads(hash_file.read_text())["hashes"]
