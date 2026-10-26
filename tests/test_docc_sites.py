"""DocC sites other than Apple's (Batch 4 item 4: docs.swift.org as a DocCSite config).

- Naming and links per site: naming.page_path takes the site's doc prefix and
  namespace (<namespace>/<Dir>/….md), naming.dirmap the site's hash dir and
  JSON prefix, links.doc_link the site's doc prefix (a page of another site
  keeps its URL), _canonical_framework_id the site's hash dir.
- Whole scrape.py runs (--sites) against a fake DocC site: its allow-listed
  roots are jobs with their own namespace, hash files, front matter and
  footer; the scope rule never fetches an excluded path or a top-level page
  outside the allow-list (the private roots its index root lists); a module
  under the namespace (D6) is routed as Apple's are.
- Removal, all automatic (rule 7): a root dropped from the allow-list is
  deleted at the next run whose config loaded (also when 7(f) skips the
  site's jobs); a root answering 404/410 on 2 consecutive runs is deleted;
  the index root failing (5xx) skips the site and exits 1, answering 404
  uses the persisted index_roots; a module under the namespace is never a
  7(a)/(b) candidate; a site that left the config goes whole.
"""

import json
import os
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Sequence, Set, Tuple

import httpx
import pytest
from structlog.testing import capture_logs
from structlog.typing import EventDict

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts', 'utilities')))

import docc_sites
import scrape_all_frameworks
from scraper import site as site_config
from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.site import APPLE, DocCSite
from scraper.utils.links import doc_link, link_base
from scraper.utils.naming import dirmap, page_path
from tests.test_failure_policy import Apple, sandbox_runs
from tests.test_fetch_results import Spec, ok, status
from tests.test_sink import sandbox_bytes, topic_page

SITE = DocCSite(
    name="example",
    site_url="https://docs.example.org/latest",
    doc_base="https://docs.example.org/latest/documentation",
    json_base="https://docs.example.org/latest/data/documentation",
    bundle_prefix="doc://",
    label="docs.example.org",
    namespace="Example-Org",
    index_url="https://docs.example.org/latest/data/documentation.json",
    roots=("guide", "kit", "otherkit"),
    excludes=("stdlib", "kit/proposals"),
)
NS = SITE.namespace
GUIDE_B = "org.example.guide"
STD_B = "com.example.std"

# cased documentation path -> (its bundle, its links (cased path, bundle))
Pages = Dict[str, Tuple[str, List[Tuple[str, str]]]]
PAGES: Pages = {
    # The guide links its own page and a second segment of its bundle: a D6
    # module under the namespace (its root, /documentation/guide-concurrency, 404s)
    "Guide": (GUIDE_B, [("Guide/intro", GUIDE_B), ("Guide-Concurrency/one", GUIDE_B)]),
    "Guide/intro": (GUIDE_B, [("Guide", GUIDE_B)]),
    "Guide-Concurrency/one": (GUIDE_B, [("Guide-Concurrency/two", GUIDE_B)]),
    "Guide-Concurrency/two": (GUIDE_B, []),
    # Kit shares its bundle with the excluded Stdlib, the private _Private
    # (listed by the index root only), and OtherKit (allow-listed: a handoff)
    "Kit": (STD_B, [("Kit/Thing", STD_B), ("Stdlib/Array", STD_B), ("_Private/Hidden", STD_B),
                    ("OtherKit/Shared", STD_B), ("Kit/proposals", STD_B)]),
    "Kit/Thing": (STD_B, [("Kit", STD_B)]),
    "Kit/proposals": (STD_B, [("Kit/proposals/kp-0001", STD_B)]),
    "Kit/proposals/kp-0001": (STD_B, []),
    "OtherKit": (STD_B, [("OtherKit/one", STD_B)]),
    "OtherKit/one": (STD_B, []),
    "OtherKit/Shared": (STD_B, []),
    "Stdlib/Array": (STD_B, []),
    "_Private/Hidden": (STD_B, []),
}
# The index root's references: every top-level page (the allow-list's, the
# excluded Stdlib, the private _Private and a link-only Landing page)
INDEX_ROOTS = [("Guide", GUIDE_B), ("Kit", STD_B), ("OtherKit", STD_B), ("Stdlib", STD_B),
               ("_Private", STD_B), ("Landing", "Landing")]


def site_json(path: str) -> str:
    return f"{SITE.json_prefix}{path.lower()}.json"


def site_doc(path: str) -> str:
    return SITE.doc_url(path.lower())


def index_body(roots: Sequence[Tuple[str, str]] = INDEX_ROOTS) -> str:
    return json.dumps({
        "identifier": {"url": "doc://Example/documentation", "interfaceLanguage": "swift"},
        "metadata": {"title": "Example Documentation", "role": "collection"},
        "references": {
            f"doc://{bundle}/documentation/{name}": {"type": "topic", "url": f"/documentation/{name.lower()}",
                                                     "title": name}
            for name, bundle in roots
        },
    })


def kit_thing_body() -> str:
    """Kit/Thing, which also links an Apple page (an absolute URL) in its abstract."""
    body = json.loads(topic_page("Kit/Thing", STD_B, [("Kit", STD_B)]))
    apple = "doc://com.apple.documentation/documentation/swift/array"
    body["abstract"] = [{"type": "text", "text": "See "}, {"type": "reference", "identifier": apple, "isActive": True},
                        {"type": "text", "text": " and "},
                        {"type": "reference", "identifier": "doc://com.example.std/documentation/Stdlib/Array",
                         "isActive": True}]
    body["references"][apple] = {"type": "topic", "url": "https://developer.apple.com/documentation/swift/array",
                                 "title": "Array", "identifier": apple, "kind": "symbol", "role": "symbol"}
    body["references"]["doc://com.example.std/documentation/Stdlib/Array"] = {
        "type": "topic", "url": "/documentation/stdlib/array", "title": "Array", "kind": "symbol", "role": "symbol",
        "identifier": "doc://com.example.std/documentation/Stdlib/Array"}
    return json.dumps(body)


def site_routes(pages: Pages = PAGES, index: Optional[List[Spec]] = None,
                overrides: Optional[Dict[str, List[Spec]]] = None) -> Dict[str, List[Spec]]:
    """The fake site: each page 200 with an ETag of its body (never stored; 304 on a match, never asked for);
    its URLs are case-sensitive."""
    routes: Dict[str, List[Spec]] = {}
    for path, (bundle, links) in pages.items():
        body = kit_thing_body() if path == "Kit/Thing" else topic_page(path, bundle, links)
        routes[site_json(path)] = [ok(body, f"E-{abs(hash(body)) % 10**12}")]
    routes[SITE.index_url or ""] = index or [ok(index_body(), "I-1")]
    for url, specs in (overrides or {}).items():
        routes[url] = specs
    return routes


def site_file(path: str, root: str) -> Path:
    """A page's file: under the namespace, its dir cased as its root is."""
    relative = page_path(root, site_doc(path), SITE)
    assert relative is not None
    return Path("documentation") / relative


def hash_file(name: str) -> Path:
    return Path(".hashes") / NS / f"{name}_hashes.json"


def metadata_of(name: str) -> Dict[str, Any]:
    data: Dict[str, Any] = json.loads(hash_file(name).read_text())
    return dict(data["metadata"])


class SiteRuns:
    """Whole scrape.py runs (--sites example --cleanup-orphans --auto-cleanup) against the fake site."""

    def __init__(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        sandbox_runs(tmp_path, monkeypatch)
        self.monkeypatch = monkeypatch
        self.events: List[EventDict] = []
        self.requests: List[str] = []
        self.conditional: List[str] = []  # the requests that sent If-None-Match
        self.configure(SITE)

    def configure(self, *sites: DocCSite) -> None:
        """The DocC sites the config lists (site.DOCC_SITES)."""
        self.monkeypatch.setattr(site_config, "DOCC_SITES", tuple(sites))

    async def scrape(self, routes: Dict[str, List[Spec]], *args: str, apple: Optional[Dict[str, List[Spec]]] = None,
                     listed: Sequence[str] = ()) -> int:
        """One run; args default to --sites example."""
        fake = Apple({**routes, **(apple or {})})

        def handler(request: httpx.Request) -> httpx.Response:
            return fake(request)

        class MockedScraper(AppleJSONDocumentationScraper):
            async def __aenter__(self) -> "MockedScraper":
                self.session = httpx.AsyncClient(transport=httpx.MockTransport(handler), follow_redirects=True)
                return self

        class MockedLoader(docc_sites.SiteIndexLoader):
            async def __aenter__(self) -> "MockedLoader":
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
        self.monkeypatch.setattr(docc_sites, "SiteIndexLoader", MockedLoader)
        self.monkeypatch.setattr(sys, "argv", [
            "scrape.py", *(args or ("--sites", "example")), "--yes", "--cleanup-orphans", "--auto-cleanup"])
        with capture_logs() as events:
            code: int = await scrape_all_frameworks.scrape_everything()
        self.events = events
        self.requests = [url for url, _ in fake.requests] + fake.unrouted
        self.conditional = [url for url, if_none_match in fake.requests if if_none_match is not None]
        return code

    def logged(self, event: str) -> List[EventDict]:
        return [e for e in self.events if e["event"] == event]


@pytest.fixture
def site_runs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[SiteRuns]:
    yield SiteRuns(tmp_path, monkeypatch)


def docs() -> Set[Path]:
    return set(Path("documentation").rglob("*.md"))


def without_root(site: DocCSite, root: str) -> DocCSite:
    """The site's config with a root dropped from its allow-list."""
    return DocCSite(**{**site.__dict__, "roots": tuple(r for r in site.roots if r != root)})


class TestPerSiteNaming:
    """page_path, dirmap, doc_link and the canonical id take the site's prefixes, namespace and hash dir."""

    def test_page_path_is_under_the_namespace(self) -> None:
        assert page_path("PackagePlugin", SITE.doc_url("packageplugin"), SITE) == \
            f"{NS}/PackagePlugin/PackagePlugin.md"
        assert page_path("PackagePlugin", SITE.doc_url("packageplugin/path/appending(subpath:)"), SITE) == \
            f"{NS}/PackagePlugin/path/appending(subpath).md"
        # Another site's prefix is no page of the dir
        assert page_path("PackagePlugin", APPLE.doc_url("packageplugin/path"), SITE) is None
        assert page_path("PackagePlugin", SITE.doc_url("packageplugin/path")) is None
        # Apple's is unchanged: top-level
        assert page_path("SwiftUI", APPLE.doc_url("swiftui/view")) == "SwiftUI/view.md"

    def test_links_between_the_sites_pages_are_local_and_to_another_site_absolute(self) -> None:
        dirs = {"guide": "Guide", "kit": "Kit"}
        base = link_base("Guide", SITE.doc_url("guide/intro"), SITE)
        assert base == f"{NS}/Guide"
        assert doc_link(SITE.doc_url("guide/other#section"), base, dirs, SITE) == "./other.md#section"
        assert doc_link(SITE.doc_url("kit/thing"), base, dirs, SITE) == "../Kit/thing.md"
        # Apple's page, an unknown dir of the site: absolute
        apple = "https://developer.apple.com/documentation/swift/array"
        assert doc_link(apple, base, {"swift": "Swift"}, SITE) == apple
        assert doc_link(SITE.doc_url("stdlib/array"), base, dirs, SITE) == SITE.doc_url("stdlib/array")
        # An Apple page's links never take the site's pages local
        assert doc_link(SITE.doc_url("kit/thing"), "SwiftUI", dirs) == SITE.doc_url("kit/thing")
        # A page of no page path of the dir gets the namespaced dir as its base
        assert link_base("Guide", APPLE.doc_url("x"), SITE) == f"{NS}/Guide"

    def test_dirmap_and_the_canonical_id_read_the_sites_hash_dir(self, tmp_path: Path,
                                                                 monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(Config, "CACHE_DIR", tmp_path / ".hashes")
        site_dir = Config.get_hash_dir(NS)
        site_dir.mkdir(parents=True)
        (site_dir / "MigrationGuide_hashes.json").write_text(json.dumps(
            {"metadata": {}, "hashes": {SITE.json_prefix + "migrationguide.json": {"hash": "h"}}}))
        # An Apple-keyed file in the site's dir isn't one of its dirs
        (site_dir / "Other_hashes.json").write_text(json.dumps(
            {"metadata": {}, "hashes": {APPLE.json_prefix + "other.json": {"hash": "h"}}}))
        assert dirmap(site_dir, SITE.json_prefix) == {"migrationguide": "MigrationGuide"}
        assert dirmap(Config.CACHE_DIR) == {}
        canonical = AppleJSONDocumentationScraper._canonical_framework_id
        assert canonical("migrationguide", site_dir) == "MigrationGuide"
        assert canonical("migrationguide") == "migrationguide"
        assert Config.get_hash_file("MigrationGuide", namespace=NS) == site_dir / "MigrationGuide_hashes.json"
        assert Config.get_framework_output_dir("MigrationGuide", namespace=NS) == \
            Config.OUTPUT_DIR / NS / "MigrationGuide"

    def test_the_site_config(self) -> None:
        assert SITE.doc_path == "/documentation/"
        assert APPLE.doc_path == "/documentation/"
        assert SITE.framework_label("PackagePlugin") == "Example-Org/PackagePlugin"
        assert APPLE.framework_label("SwiftUI") == "SwiftUI"
        assert SITE.excluded("stdlib") and SITE.excluded("stdlib/array") and SITE.excluded("kit/proposals/kp-1")
        assert not SITE.excluded("stdlibx") and not SITE.excluded("kit/proposal") and not SITE.excluded("kit")
        assert DocCSite("spi", "s", "d", "j", "b", namespace="SPI/swift-log").framework_label("Logging") == \
            "swift-log/Logging"
        # A page's first 404/410 removes it, as Apple's does (an SPI package waits for a 2nd)
        assert SITE.page_gone_runs == APPLE.page_gone_runs == site_config.SWIFT_ORG.page_gone_runs == 1

    def test_docs_swift_orgs_config(self) -> None:
        swift_org = site_config.SWIFT_ORG
        assert swift_org.namespace == "Swift-Org" and swift_org.index_url
        assert set(swift_org.roots) == {
            "migrationguide", "packagemanagerdocs", "packageplugin", "diagnostics", "embeddedswift", "wasmguide",
            "swiftandroid", "swiftlinux", "swiftlydocs", "userdocs", "swiftjavadocumentation", "cxx", "cxxstdlib",
            "docc", "apiguidelines"}
        assert set(swift_org.excludes) == {
            "swift", "testing", "the-swift-programming-language", "regexbuilder", "synchronization", "distributed",
            "observation", "packagedescription"}
        assert not set(swift_org.roots) & set(swift_org.excludes)

    def test_index_roots_are_the_cased_first_segments_of_its_documentation_references(self) -> None:
        body = json.dumps({"references": {
            "doc://org.swift.migration.6/documentation/MigrationGuide": {"type": "topic",
                                                                        "url": "/documentation/migrationguide"},
            "doc://x/documentation/Cxx/Thing": {"type": "topic", "url": "/documentation/cxx/thing"},
            "doc://t/tutorials/getting-started": {"type": "topic", "url": "/tutorials/getting-started"},
            "https://example.org": {"type": "link", "url": "https://example.org"},
        }})
        assert docc_sites.index_roots(SITE, body) == ["Cxx", "MigrationGuide"]
        for bad in ("not json", json.dumps({"references": {}}), json.dumps([1])):
            with pytest.raises(ValueError):
                docc_sites.index_roots(SITE, bad)


class TestSiteScrape:
    """A DocC site's roots as jobs of the Apple process (--sites)."""

    async def test_the_sites_pages_are_its_own_and_a_second_run_changes_nothing(self, site_runs: SiteRuns) -> None:
        assert await site_runs.scrape(site_routes()) == 0
        assert docs() == {
            site_file("Guide", "Guide"), site_file("Guide/intro", "Guide"),
            site_file("Guide-Concurrency/one", "Guide-Concurrency"),
            site_file("Guide-Concurrency/two", "Guide-Concurrency"),
            site_file("Kit", "Kit"), site_file("Kit/Thing", "Kit"),
            site_file("OtherKit", "OtherKit"), site_file("OtherKit/one", "OtherKit"),
            site_file("OtherKit/Shared", "OtherKit"),
        }
        # Never fetched: the excluded root and path, the private root the index lists, the landing page
        fetched = set(site_runs.requests)
        for path in ("Stdlib/Array", "_Private/Hidden", "Kit/proposals", "Kit/proposals/kp-0001", "Landing"):
            assert site_json(path) not in fetched, path
        # Hash files under the namespace; the module's records its parent
        assert sorted(p.name for p in (Path(".hashes") / NS).iterdir()) == [
            "Guide-Concurrency_hashes.json", "Guide_hashes.json", "Kit_hashes.json", "OtherKit_hashes.json",
            "_site.json"]
        assert not list(Path(".hashes").glob("*_hashes.json"))
        assert metadata_of("Guide-Concurrency")["module"] == {"bundle": GUIDE_B,
                                                              "parents": {"guide": {"unlinked_clean_runs": 0}}}
        assert metadata_of("Guide")["child_modules"] == {"guide-concurrency": {}}
        assert metadata_of("OtherKit")["handoff_from"] == {"kit": {}}
        site_meta = json.loads((Path(".hashes") / NS / "_site.json").read_text())["metadata"]
        assert site_meta["site"] == "example"
        assert site_meta["index_roots"] == ["_Private", "Guide", "Kit", "Landing", "OtherKit", "Stdlib"]

        # The page: front matter, its framework label, local links within the
        # site, absolute ones to Apple and to the excluded root, the site's footer
        thing = site_file("Kit/Thing", "Kit").read_text()
        assert thing.startswith(
            f'---\nurl: "{site_doc("Kit/Thing")}"\nframework: "Example-Org/Kit"\n---\n\n# Thing\n')
        assert "**Framework**: Example-Org/Kit" in thing
        assert "[`Array`](https://developer.apple.com/documentation/swift/array)" in thing
        assert f"[`Array`]({site_doc('Stdlib/Array')})" in thing
        assert "](./Kit.md)" in thing
        assert thing.rstrip().endswith(f"*[View on docs.example.org]({site_doc('Kit/Thing')})*")
        guide = site_file("Guide", "Guide").read_text()
        assert "](./intro.md)" in guide and "](../Guide-Concurrency/one.md)" in guide

        before = sandbox_bytes()
        assert await site_runs.scrape(site_routes()) == 0
        assert sandbox_bytes() == before
        assert not site_runs.logged("file_saved")
        # One unconditional GET per page; a root twice (scrape_page, then its
        # queued copy, which reads its links), the index once
        requests = Counter(site_runs.requests)
        assert site_runs.conditional == []
        assert requests.pop(SITE.index_url) == 1
        assert {url for url, count in requests.items() if count != 1} == {
            site_json(root) for root in ("Guide", "Kit", "OtherKit")}
        assert set(requests.values()) == {1, 2}

    async def test_the_namespace_check(self, site_runs: SiteRuns) -> None:
        # A namespace another scraper's dir, or an Apple hash file's id: the run aborts before scraping
        for namespace in ("MLX", "swift-book"):
            site_runs.configure(DocCSite(**{**SITE.__dict__, "namespace": namespace}))
            assert await site_runs.scrape(site_routes()) == 2
            assert not site_runs.requests
        Path(".hashes").mkdir(exist_ok=True)
        Path(".hashes", "example-org_hashes.json").write_text(json.dumps({"metadata": {}, "hashes": {}}))
        site_runs.configure(SITE)
        assert await site_runs.scrape(site_routes()) == 2
        assert not docs()

    async def test_an_apple_technology_named_like_a_namespace_is_refused(self, site_runs: SiteRuns) -> None:
        code = await site_runs.scrape(site_routes(), "--frameworks", "Example-Org", listed=["Example-Org"])
        assert code == 1
        assert site_runs.logged("namespace_collision")
        assert not site_runs.requests


class TestSiteRemoval:
    """Rule 7 for a DocC site: automatic removals, and what never removes."""

    async def test_a_root_dropped_from_the_allow_list_is_deleted_at_the_next_run(self, site_runs: SiteRuns) -> None:
        assert await site_runs.scrape(site_routes()) == 0
        assert site_file("OtherKit/one", "OtherKit").exists()
        # Dropped while the index root fails (7(f) skips the site's jobs): still deleted (7(a))
        site_runs.configure(without_root(SITE, "otherkit"))
        assert await site_runs.scrape(site_routes(index=[status(503)])) == 1
        assert not Path("documentation", NS, "OtherKit").exists() and not hash_file("OtherKit").exists()
        assert site_runs.requests and set(site_runs.requests) == {SITE.index_url}  # no page fetched
        assert site_runs.logged("root_not_configured")
        # The rest is untouched
        assert site_file("Kit/Thing", "Kit").exists()
        assert site_file("Guide-Concurrency/one", "Guide-Concurrency").exists()

    async def test_a_root_gone_on_two_runs_is_deleted_and_never_recreated(self, site_runs: SiteRuns) -> None:
        assert await site_runs.scrape(site_routes()) == 0
        # OtherKit is gone from the site: its pages 404 and Kit no longer links its page
        pages = {**PAGES, "Kit": (STD_B, [link for link in PAGES["Kit"][1] if link[0] != "OtherKit/Shared"])}
        gone = {site_json(path): [status(404)] for path in PAGES if path.startswith("OtherKit")}
        assert await site_runs.scrape(site_routes(pages, overrides=gone)) == 0
        assert site_file("OtherKit/one", "OtherKit").exists()
        assert metadata_of("OtherKit")["root_gone_runs"] == 1
        assert await site_runs.scrape(site_routes(pages, overrides=gone)) == 0
        assert not Path("documentation", NS, "OtherKit").exists() and not hash_file("OtherKit").exists()
        assert site_runs.logged("framework_removed")
        # Still in the allow-list, its root still 404: nothing is re-created
        assert await site_runs.scrape(site_routes(pages, overrides=gone)) == 0
        assert not Path("documentation", NS, "OtherKit").exists() and not hash_file("OtherKit").exists()

    async def test_a_root_failing_with_a_5xx_keeps_its_pages_and_exits_1(self, site_runs: SiteRuns) -> None:
        assert await site_runs.scrape(site_routes()) == 0
        before = docs()
        assert await site_runs.scrape(site_routes(overrides={site_json("OtherKit"): [status(503)]})) == 1
        assert docs() == before
        assert "root_gone_runs" not in metadata_of("OtherKit")

    async def test_the_index_root_failing_skips_the_site_and_exits_1(self, site_runs: SiteRuns) -> None:
        assert await site_runs.scrape(site_routes()) == 0
        before = sandbox_bytes()
        for failure in ([status(503)], [ok("<html>challenge</html>", "C")], [status(403)]):
            assert await site_runs.scrape(site_routes(index=failure)) == 1
            assert site_runs.logged("index_root_failed")
            assert all(url == SITE.index_url for url in site_runs.requests)
            assert sandbox_bytes() == before

    async def test_the_index_root_gone_uses_the_persisted_index_roots(self, site_runs: SiteRuns) -> None:
        assert await site_runs.scrape(site_routes()) == 0
        before = sandbox_bytes()
        assert await site_runs.scrape(site_routes(index=[status(404)])) == 0
        assert site_runs.logged("index_root_gone")
        # The roots ran normally; the private and excluded roots stay out of the crawl
        assert site_json("Kit/Thing") in site_runs.requests
        for path in ("Stdlib/Array", "_Private/Hidden"):
            assert site_json(path) not in site_runs.requests
        assert sandbox_bytes() == before

    async def test_the_index_root_gone_on_the_first_run_is_a_failure(self, site_runs: SiteRuns) -> None:
        assert await site_runs.scrape(site_routes(index=[status(404)])) == 1
        assert site_runs.logged("index_root_failed")
        assert not docs() and site_runs.requests == [SITE.index_url]

    async def test_a_module_under_the_namespace_is_never_a_7ab_candidate(self, site_runs: SiteRuns) -> None:
        # Its root 404s on every run (as swift-6-concurrency-migration-guide's does) and it
        # isn't in the allow-list: it stays while its parent links it
        for _ in range(3):
            assert await site_runs.scrape(site_routes()) == 0
            assert site_file("Guide-Concurrency/two", "Guide-Concurrency").exists()
            assert "root_gone_runs" not in metadata_of("Guide-Concurrency")
        assert site_json("Guide-Concurrency") in site_runs.requests
        assert not site_runs.logged("root_not_configured")
        # Unlinked by its only parent: removed by the module rules after 2 clean runs
        unlinked = {**PAGES, "Guide": (GUIDE_B, [("Guide/intro", GUIDE_B)])}
        assert await site_runs.scrape(site_routes(unlinked)) == 0
        assert hash_file("Guide-Concurrency").exists()
        assert await site_runs.scrape(site_routes(unlinked)) == 0
        assert not hash_file("Guide-Concurrency").exists()
        assert not Path("documentation", NS, "Guide-Concurrency").exists()
        assert "child_modules" not in metadata_of("Guide")

    async def test_a_site_that_left_the_config_goes_whole(self, site_runs: SiteRuns) -> None:
        assert await site_runs.scrape(site_routes()) == 0
        files = len(docs())
        # A run of only some of the configured sites never removes a site
        other = DocCSite(**{**SITE.__dict__, "name": "other", "namespace": "Other-Org", "roots": ("guide",)})
        site_runs.configure(SITE, other)
        assert await site_runs.scrape(site_routes(), "--sites", "other") == 0
        assert Path("documentation", NS).is_dir() and len(docs()) > files
        # A run of every configured site: the namespace no configured site has goes whole
        site_runs.configure(other)
        assert await site_runs.scrape(site_routes(), "--sites", "other") == 0
        assert not Path("documentation", NS).exists() and not Path(".hashes", NS).exists()
        assert Path("documentation", "Other-Org", "Guide").is_dir() and Path(".hashes", "Other-Org", "_site.json").exists()
        assert site_runs.logged("site_removed")
        # The same with --all (every site, and Apple's frameworks)
        site_runs.configure()
        apple = {"https://developer.apple.com/tutorials/data/documentation/testkit.json": [
            ok(topic_page("testkit", "com.apple.testkit"), "A")]}
        assert await site_runs.scrape({}, "--all", apple=apple, listed=["testkit"]) == 0
        assert not Path("documentation", "Other-Org").exists() and not Path(".hashes", "Other-Org").exists()
        assert Path("documentation", "testkit", "testkit.md").exists()
