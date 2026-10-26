"""The DocC site and the sinks (1.1 + D6, step 1a: a refactor with no new behavior).

- site.DocCSite: one site's URLs; APPLE gives the Apple scraper, the naming
  and the links every URL they use, and the scraper builds each from its site;
- sink.Sink: one docs dir and its hash file with this run's state for its
  pages; a framework job's primary sink is its own dir and hash file;
- sink.SinkRegistry: one sink per site and dir (in any casing), created on
  first use; a run's jobs share one, and each job's sink leaves it once the
  job is done.
"""

import dataclasses
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

import httpx
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts', 'utilities')))

import scrape_all_frameworks
from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.sink import Sink, SinkRegistry
from scraper.site import APPLE, DocCSite
from scraper.utils.naming import DOC_URL_PREFIX, JSON_URL_PREFIX
from tests.test_failure_policy import FW, SITE, Apple, FrameworkList, Runs, Site, file_of, routes_for, sandbox_runs

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
        data = scraper._extract_from_json(sink, page, f"{APPLE.doc_prefix}testkit/a")
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

    def test_evict_drops_a_sink_and_a_later_get_loads_its_hash_file_again(self, dirs: Path) -> None:
        sinks = SinkRegistry()
        sink = sinks.get(APPLE, "TestKit", "Test Kit", 1)
        url = f"{APPLE.json_prefix}testkit/a.json"
        sink.hash_manager.update_hash(url, "body", "E1", Path("documentation/TestKit/a.md"))
        assert sink.hash_manager.save()
        sinks.evict(sink)
        again = sinks.get(APPLE, "TestKit", "Test Kit", 1)
        assert again is not sink and again.hash_manager.hashes[url]["etag"] == "E1"
        # Evicting a sink that is no longer the registered one leaves the new one
        sinks.evict(sink)
        assert sinks.get(APPLE, "TestKit", "Test Kit", 1) is again

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
        # The run's frameworks are linked locally, and every job's sink has left
        assert registries[0].known_dirs == {FW: FW, other: other}
        assert registries[0]._sinks == {}
        for path in SITE:
            assert file_of(path).exists(), path
        assert runs.saved()["hashes"] and runs.saved(other)["hashes"]
