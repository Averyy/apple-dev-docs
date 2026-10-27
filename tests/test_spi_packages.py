"""The Swift Package Index packages (Batch 4 item 5: CareKit and the SPI packages, Phase 5 rows 2-3).

- The config: one DocC site per package, all on swiftpackageindex.com, each
  its own namespace (SPI/<repo>), with its roots from its navigator index
  (index/index.json) and its design proposals excluded (OD3).
- The navigator index parser: the roots are the first segments of its
  documentation paths, cased as their root nodes' titles.
- The host: its packages share one rate limiter and run at most max_jobs
  jobs at once, waiting outside the run's job slots; its requests are
  retried 4 times, 6, 12, 18 and 24 s apart (a 503 lasts ~10 s on its URL).
- Whole scrape.py runs (--sites) against a fake package on a host that sends
  no ETag: its index's roots are jobs under the namespace, an excluded
  proposals collection is read once at the site's load and the proposals it
  lists are never fetched, and a second run changes nothing.
- The pages only the excluded collection lists (Batch 7 B7,
  DocCSite.excluded_pages): never fetched, linked by URL; one in-scope
  curation reaches is crawled as ever and linked locally; a failed or empty
  fetch of the collection uses what it last listed (persisted in
  _site.json), and a new set renders the package's pages again (their
  sinks' metadata.render records it).
- Removal, all automatic (D6 rule 7, row 3): a root answering 404 on 2
  consecutive runs; a target its index stops listing while its JSON still
  answers 200 (deleted on the 2nd load without it); the index answering 404
  on 2 consecutive runs (the package goes whole; a 3rd such run, the package
  still configured, exits 0 and re-creates nothing); an index failure of
  ours counts nothing.
- A page we have answering 404/410 (Batch 6 item 2: SPI does while it
  rebuilds a package's docs): kept on the 1st run, with the pages only it
  links (its target's cleanup skipped, no error), removed on the 2nd in a
  row; any other answer starts the count again. A page we never had, and a
  module's page, follow the same rules as ever.
"""

import asyncio
import dataclasses
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Sequence, Tuple

import httpx
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts', 'utilities')))

import docc_sites
import scrape_all_frameworks
from scraper import site as site_config
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.site import DocCSite, spi_package
from scraper.utils.naming import page_path
from tests import test_docc_sites
from tests.test_docc_sites import SiteRuns, docs
from tests.test_failure_policy import Apple
from tests.test_fetch_results import Spec, ok, status
from tests.test_sink import sandbox_bytes, topic_page

def fake_package(repo: str) -> DocCSite:
    """An SPI package's config for a fake package (its retries don't wait)."""
    return dataclasses.replace(spi_package("example", repo, excludes=("kitcore/proposals",)), retry_backoff=0.0)


PKG = fake_package("fake-kit")
NS = PKG.namespace
CORE_B = "KitCore"
UI_B = "KitUI"

# cased documentation path -> (its bundle, its links (cased path, bundle)).
# Each target is its own bundle, as SPI builds them: KitCore links KitUI's
# page across bundles (never followed, linked locally), and its proposals
# collection, excluded with the proposal only it lists
Pages = Dict[str, Tuple[str, List[Tuple[str, str]]]]
PAGES: Pages = {
    "KitCore": (CORE_B, [("KitCore/Thing", CORE_B), ("KitUI/View", UI_B), ("KitCore/proposals", CORE_B)]),
    "KitCore/Thing": (CORE_B, [("KitCore", CORE_B)]),
    "KitCore/proposals": (CORE_B, [("KitCore/KP-0001", CORE_B)]),
    "KitCore/KP-0001": (CORE_B, []),
    "KitUI": (UI_B, [("KitUI/View", UI_B), ("KitCore/Thing", CORE_B)]),
    "KitUI/View": (UI_B, []),
}
ROOTS = ("KitCore", "KitUI")


def pkg_json(path: str) -> str:
    return f"{PKG.json_prefix}{path.lower()}.json"


def pkg_doc(path: str) -> str:
    return PKG.doc_url(path.lower())


def navigator(roots: Sequence[str] = ROOTS) -> str:
    """The package's index/index.json: each root's node (titled as cased) with its pages, and a tutorial."""
    def node(path: str) -> Dict[str, Any]:
        return {"path": f"/documentation/{path.lower()}", "title": path.split("/")[-1], "type": "symbol"}

    children = {root: [node(path) for path in PAGES if path.startswith(f"{root}/")] for root in roots}
    return json.dumps({
        "includedArchiveIdentifiers": list(roots),
        "interfaceLanguages": {"swift": [
            *({"path": f"/documentation/{root.lower()}", "title": root, "type": "module",
               "children": [{"title": "Topics", "type": "groupMarker"}, *children[root]]} for root in roots),
            {"path": "/tutorials/kitcore", "title": "Working with KitCore", "type": "overview",
             "children": [{"path": "/tutorials/kitcore/first", "title": "First", "type": "project"}]},
        ]},
        "schemaVersion": {"major": 0, "minor": 1, "patch": 0},
    })


def pkg_routes(pages: Pages = PAGES, index: Optional[List[Spec]] = None,
               overrides: Optional[Dict[str, List[Spec]]] = None) -> Dict[str, List[Spec]]:
    """The fake package: each page 200 (no ETag, as SPI sends none), its index listing both targets."""
    routes: Dict[str, List[Spec]] = {pkg_json(path): [ok(topic_page(path, bundle, links), "")]
                                     for path, (bundle, links) in pages.items()}
    routes[PKG.index_url or ""] = index or [ok(navigator(), "")]
    for url, specs in (overrides or {}).items():
        routes[url] = specs
    return routes


class NoETag(Apple):
    """The fake host answers without an ETag, as SPI's does."""

    def __call__(self, request: httpx.Request) -> httpx.Response:
        response = super().__call__(request)
        if response.status_code != 200:
            return response
        return httpx.Response(200, content=response.content, request=request)


def pkg_file(path: str, root: str) -> Path:
    relative = page_path(root, pkg_doc(path), PKG)
    assert relative is not None
    return Path("documentation") / relative


def hash_file(name: str) -> Path:
    return Path(".hashes") / NS / f"{name}_hashes.json"


def metadata_of(path: Path) -> Dict[str, Any]:
    data: Dict[str, Any] = json.loads(path.read_text())
    return dict(data["metadata"])


def site_metadata() -> Dict[str, Any]:
    return metadata_of(Path(".hashes") / NS / "_site.json")


@pytest.fixture
def pkg_runs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[SiteRuns]:
    monkeypatch.setattr(test_docc_sites, "Apple", NoETag)
    runs = SiteRuns(tmp_path, monkeypatch)
    runs.configure(PKG)
    yield runs


async def scrape(runs: SiteRuns, routes: Dict[str, List[Spec]]) -> int:
    return await runs.scrape(routes, "--sites", PKG.name)


ALL = {pkg_file("KitCore", "KitCore"), pkg_file("KitCore/Thing", "KitCore"),
       pkg_file("KitUI", "KitUI"), pkg_file("KitUI/View", "KitUI")}


class TestConfig:
    def test_the_packages(self) -> None:
        packages = site_config.SPI_PACKAGES
        assert [package.namespace for package in packages] == [
            "SPI/CareKit", "SPI/mlx-swift", "SPI/swift-argument-parser", "SPI/swift-log",
            "SPI/swift-async-algorithms", "SPI/swift-openapi-generator", "SPI/swift-configuration",
            "SPI/mlx-swift-lm"]
        # (tests/conftest.py empties DOCC_SITES for every test: its module source lists them)
        assert "DOCC_SITES: Final[Tuple[DocCSite, ...]] = (SWIFT_ORG, *SPI_PACKAGES)" in \
            Path(site_config.__file__).read_text()
        sites = (site_config.SWIFT_ORG, *packages)
        assert len({site.name for site in sites}) == len({site.namespace.lower() for site in sites}) == len(sites)
        log = {package.namespace: package for package in packages}["SPI/swift-log"]
        assert log.index_url == "https://swiftpackageindex.com/apple/swift-log/main/index/index.json"
        assert log.json_prefix == "https://swiftpackageindex.com/apple/swift-log/main/data/documentation/"
        assert log.doc_url("logging/logger") == "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger"
        assert log.doc_path == "/documentation/"
        assert log.framework_label("Logging") == "swift-log/Logging"
        assert log.page_gone_runs == 2
        assert {package.namespace: package for package in packages}["SPI/CareKit"].framework_label(
            "CareKitStore") == "CareKit/CareKitStore"
        for package in packages:
            assert package.roots_from_index and not package.roots and package.namespace_top == "SPI"
            assert package.label == "Swift Package Index" and package.page_gone_runs == 2
        # OD3: the design proposals are no documentation
        assert {package.namespace: package.excludes for package in packages if package.excludes} == {
            "SPI/swift-log": ("logging/proposals",),
            "SPI/swift-openapi-generator": ("swift-openapi-generator/proposals",),
            "SPI/swift-configuration": ("configuration/proposals",)}
        assert not site_config.SWIFT_ORG.roots_from_index

    def test_the_namespaces_pass_the_startup_assertion(self) -> None:
        # Under SPI/, so SPI's mlx-swift is never the MLX scraper's MLX-Swift dir
        reserved = scrape_all_frameworks.other_scraper_dirs()
        assert "spi" not in reserved and "mlx-swift" in reserved
        docc_sites.check_namespaces(site_config.DOCC_SITES, reserved, set())

    async def test_the_packages_share_one_limiter(self, monkeypatch: pytest.MonkeyPatch) -> None:
        other = spi_package("example", "other-kit")

        async def load(site: DocCSite, limiter: Any) -> docc_sites.SiteRun:
            return docc_sites.SiteRun(site=site)

        monkeypatch.setattr(docc_sites, "load_site", load)
        _, limiters = await scrape_all_frameworks.load_sites([PKG, other, site_config.SWIFT_ORG])
        assert limiters[PKG.name] is limiters[other.name]
        assert limiters[site_config.SWIFT_ORG.name] is not limiters[PKG.name]
        # SPI's 503s last ~10 s on their URL: its retries wait past that; its jobs share the limiter, 8 at a time
        spi = site_config.SPI_PACKAGES[0]
        assert (spi.max_retries, spi.retry_backoff, spi.max_jobs) == (4, 6.0, 8)
        assert all((package.max_retries, package.retry_backoff, package.max_jobs) == (4, 6.0, 8)
                   for package in site_config.SPI_PACKAGES)
        assert (site_config.SWIFT_ORG.max_retries, site_config.SWIFT_ORG.retry_backoff,
                site_config.SWIFT_ORG.max_jobs) == (None, None, 0)
        # Its jobs' scrapers take them (Apple's keep Config's)
        scraper = AppleJSONDocumentationScraper("Logging", site=spi)
        assert (scraper.max_retries, scraper.retry_backoff) == (4, 6.0)
        assert (AppleJSONDocumentationScraper("Kit").max_retries, AppleJSONDocumentationScraper("Kit").retry_backoff) \
            == (None, None)


class TestRelativeLinks:
    def test_a_relative_link_reference_resolves_against_its_page(self) -> None:
        """A link reference's relative URL is resolved as a browser does from the
        page: SPI's mlx-swift writes [MLX](mlx) on …/documentation/mlxnn, and
        Apple pages carry "#section" links and URLs with a byte-order mark."""
        scraper = AppleJSONDocumentationScraper("KitCore", site=PKG)
        scraper._current_scraping_url = pkg_doc("KitUI")
        assert scraper._reference_url("kitcore") == pkg_doc("KitCore")
        assert scraper._reference_url("#topics") == f"{pkg_doc('KitUI')}#topics"
        assert scraper._reference_url("/documentation/kitcore/thing") == pkg_doc("KitCore/Thing")
        assert scraper._reference_url("\ufeff\ufeffhttps://example.org/x ") == "https://example.org/x"
        assert scraper._reference_url("") == "" and scraper._reference_url("\ufeff") == ""
        apple = AppleJSONDocumentationScraper("Xcode")
        apple._current_scraping_url = "https://developer.apple.com/documentation/xcode/page"
        assert apple._reference_url("#Creating-a-resampler") == \
            "https://developer.apple.com/documentation/xcode/page#Creating-a-resampler"
        assert apple._reference_url("/documentation/xcode") == "https://developer.apple.com/documentation/xcode"


    async def test_a_relative_link_on_a_page_links_its_sibling(self, pkg_runs: SiteRuns) -> None:
        body = json.loads(topic_page("KitCore", CORE_B, PAGES["KitCore"][1]))
        body["abstract"] = [{"type": "text", "text": "See "}, {"type": "reference", "identifier": "kitui",
                                                               "isActive": True}]
        body["references"]["kitui"] = {"type": "link", "identifier": "kitui", "title": "KitUI", "url": "kitui"}
        assert await scrape(pkg_runs, pkg_routes(overrides={pkg_json("KitCore"): [ok(json.dumps(body), "")]})) == 0
        page = pkg_file("KitCore", "KitCore").read_text()
        assert "See [KitUI](../KitUI/KitUI.md)" in page and "mainkitui" not in page


class TestNavigatorRoots:
    def test_the_roots_are_the_cased_first_segments_of_its_documentation_paths(self) -> None:
        assert docc_sites.navigator_roots(PKG, navigator()) == ["KitCore", "KitUI"]
        body = json.dumps({"interfaceLanguages": {"swift": [
            {"path": "/documentation/swift-openapi-generator", "title": "Swift OpenAPI Generator", "type": "module",
             "children": [{"path": "/documentation/swift-openapi-generator/proposals", "title": "Proposals"}]},
            {"path": "/documentation/swift_openapi_generator/outputformat", "title": "OutputFormat"},
            {"path": "/tutorials/swift-openapi-generator", "title": "Tutorials", "type": "overview"},
        ], "occ": [{"path": "/documentation/carekitstore", "title": "CareKitStore", "type": "module"}]}})
        # A root whose title isn't its segment keeps the path's casing; a tutorial is no root (OD5)
        assert docc_sites.navigator_roots(PKG, body) == [
            "CareKitStore", "swift-openapi-generator", "swift_openapi_generator"]
        for bad in ("not json", json.dumps([1]), json.dumps({"references": {}}),
                    json.dumps({"interfaceLanguages": {"swift": [{"path": "/tutorials/x", "title": "X"}]}})):
            with pytest.raises(ValueError):
                docc_sites.navigator_roots(PKG, bad)


class TestPackageScrape:
    async def test_the_index_roots_are_jobs_and_a_second_run_changes_nothing(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes()) == 0
        assert docs() == ALL
        fetched = set(pkg_runs.requests)
        # OD3: the proposal its excluded collection lists is never fetched;
        # the collection is read once, at the site's load; OD5: no tutorial
        assert pkg_json("KitCore/KP-0001") not in fetched
        assert pkg_runs.requests.count(pkg_json("KitCore/proposals")) == 1
        assert not [url for url in fetched if "/tutorials/" in url]
        assert site_metadata()["excluded_pages"] == {"kitcore/proposals": ["kitcore/kp-0001"]}
        assert sorted(p.name for p in (Path(".hashes") / NS).iterdir()) == [
            "KitCore_hashes.json", "KitUI_hashes.json", "_site.json"]
        assert site_metadata()["index_roots"] == ["KitCore", "KitUI"]
        assert site_metadata()["site"] == PKG.name
        page = pkg_file("KitCore", "KitCore").read_text()
        assert page.startswith(f'---\nurl: "{pkg_doc("KitCore")}"\nframework: "fake-kit/KitCore"\n---\n')
        # Within the package, local across its targets; the excluded collection stays absolute
        assert "](./thing.md)" in page and "](../KitUI/view.md)" in page
        assert f"]({pkg_doc('KitCore/proposals')})" in page
        assert page.rstrip().endswith(f"*[View on Swift Package Index]({pkg_doc('KitCore')})*")

        before = sandbox_bytes()
        assert await scrape(pkg_runs, pkg_routes()) == 0
        assert sandbox_bytes() == before
        assert not pkg_runs.logged("file_saved")

    async def test_a_page_answering_503_for_4_tries_is_fetched(self, pkg_runs: SiteRuns) -> None:
        flaky = {pkg_json("KitCore/Thing"): [status(503)] * 4 + [ok(topic_page("KitCore/Thing", CORE_B,
                                                                                [("KitCore", CORE_B)]), "")]}
        assert await scrape(pkg_runs, pkg_routes(overrides=flaky)) == 0
        assert docs() == ALL
        assert pkg_runs.requests.count(pkg_json("KitCore/Thing")) == 5


    async def test_a_capped_host_runs_at_most_max_jobs_jobs(self, pkg_runs: SiteRuns,
                                                             monkeypatch: pytest.MonkeyPatch) -> None:
        packages = [fake_package(f"kit-{n}") for n in range(5)]
        pkg_runs.configure(*packages)
        active = peak = 0
        original = scrape_all_frameworks.scrape_single_framework

        async def tracked(*args: Any, **kwargs: Any) -> Any:
            nonlocal active, peak
            active += 1
            peak = max(peak, active)
            await asyncio.sleep(0.01)
            try:
                return await original(*args, **kwargs)
            finally:
                active -= 1

        monkeypatch.setattr(scrape_all_frameworks, "scrape_single_framework", tracked)
        routes: Dict[str, List[Spec]] = {}
        for package in packages:
            routes[package.index_url or ""] = [ok(navigator(), "")]
            for path, (bundle, links) in PAGES.items():
                routes[f"{package.json_prefix}{path.lower()}.json"] = [ok(topic_page(path, bundle, links), "")]
        assert await pkg_runs.scrape(routes, "--sites", *(package.name for package in packages)) == 0
        assert len(docs()) == len(packages) * len(ALL)
        assert peak == PKG.max_jobs == 8  # 10 jobs on one host whose cap is 8


class TestPackageRemoval:
    async def test_a_root_gone_on_two_runs_is_deleted_and_never_recreated(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes()) == 0
        pages = {**PAGES, "KitCore": (CORE_B, [link for link in PAGES["KitCore"][1] if link[0] != "KitUI/View"])}
        gone = {pkg_json(path): [status(404)] for path in PAGES if path.startswith("KitUI")}
        assert await scrape(pkg_runs, pkg_routes(pages, overrides=gone)) == 0
        assert metadata_of(hash_file("KitUI"))["root_gone_runs"] == 1
        assert pkg_file("KitUI/View", "KitUI").exists()
        assert await scrape(pkg_runs, pkg_routes(pages, overrides=gone)) == 0
        assert not Path("documentation", NS, "KitUI").exists() and not hash_file("KitUI").exists()
        assert pkg_runs.logged("framework_removed")
        assert await scrape(pkg_runs, pkg_routes(pages, overrides=gone)) == 0
        assert not Path("documentation", NS, "KitUI").exists() and not hash_file("KitUI").exists()
        assert pkg_file("KitCore/Thing", "KitCore").exists()

    async def test_a_target_its_index_drops_is_deleted_on_the_second_load(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes()) == 0
        # Dropped from the index; its JSON still answers 200 (SPI keeps serving it)
        dropped = pkg_routes(index=[ok(navigator(("KitCore",)), "")])
        assert await scrape(pkg_runs, dropped) == 0
        assert pkg_file("KitUI/View", "KitUI").exists()
        assert metadata_of(hash_file("KitUI"))["unlisted_runs"] == 1
        assert pkg_json("KitUI") not in pkg_runs.requests  # no job
        assert pkg_runs.logged("root_unlisted_pending")
        assert await scrape(pkg_runs, dropped) == 0
        assert not Path("documentation", NS, "KitUI").exists() and not hash_file("KitUI").exists()
        assert [e["reason"] for e in pkg_runs.logged("framework_removed")] == ["unlisted"]
        assert docs() == {pkg_file("KitCore", "KitCore"), pkg_file("KitCore/Thing", "KitCore")}
        assert "unlisted_runs" not in metadata_of(hash_file("KitCore"))
        assert site_metadata()["index_roots"] == ["KitCore"]
        # Listed again: crawled again
        assert await scrape(pkg_runs, pkg_routes()) == 0
        assert docs() == ALL

    async def test_a_target_listed_again_resets_its_count(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes()) == 0
        assert await scrape(pkg_runs, pkg_routes(index=[ok(navigator(("KitCore",)), "")])) == 0
        assert metadata_of(hash_file("KitUI"))["unlisted_runs"] == 1
        assert await scrape(pkg_runs, pkg_routes()) == 0
        assert "unlisted_runs" not in metadata_of(hash_file("KitUI"))
        assert await scrape(pkg_runs, pkg_routes(index=[ok(navigator(("KitCore",)), "")])) == 0
        assert docs() == ALL and metadata_of(hash_file("KitUI"))["unlisted_runs"] == 1

    async def test_an_index_failure_of_ours_counts_nothing(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes()) == 0
        assert await scrape(pkg_runs, pkg_routes(index=[ok(navigator(("KitCore",)), "")])) == 0
        before = sandbox_bytes()
        for failure in ([status(503)], [ok("<html>challenge</html>", "")], [status(403)], [status(500)]):
            assert await scrape(pkg_runs, pkg_routes(index=failure)) == 1
            assert pkg_runs.logged("index_root_failed")
            assert pkg_runs.requests == [PKG.index_url] * len(pkg_runs.requests)
            assert sandbox_bytes() == before  # neither unlisted_runs nor root_gone_runs counted

    async def test_an_index_gone_on_two_runs_removes_the_package(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes()) == 0
        gone = pkg_routes(index=[status(404)])  # every target's JSON still answers 200
        # 1st run: the persisted roots run normally
        assert await scrape(pkg_runs, gone) == 0
        assert pkg_runs.logged("index_gone_pending")
        assert pkg_json("KitUI/View") in pkg_runs.requests
        assert docs() == ALL and site_metadata()["root_gone_runs"] == 1
        # 2nd: the package goes whole (dirs, hash files, _site.json), nothing fetched
        assert await scrape(pkg_runs, gone) == 0
        assert not Path("documentation", NS).exists() and not Path(".hashes", NS).exists()
        assert pkg_runs.requests == [PKG.index_url]
        assert [e["reason"] for e in pkg_runs.logged("site_removed")] == ["index_gone"]
        assert not docs()
        # 3rd, the package still configured: exits 0, re-creates nothing
        assert await scrape(pkg_runs, gone) == 0
        assert pkg_runs.requests == [PKG.index_url]
        assert not Path("documentation", NS).exists() and not Path(".hashes", NS).exists()

    async def test_an_index_back_after_one_404_resets_the_count(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes()) == 0
        assert await scrape(pkg_runs, pkg_routes(index=[status(410)])) == 0
        assert site_metadata()["root_gone_runs"] == 1
        assert await scrape(pkg_runs, pkg_routes()) == 0
        assert "root_gone_runs" not in site_metadata()
        assert await scrape(pkg_runs, pkg_routes(index=[status(404)])) == 0
        assert docs() == ALL and site_metadata()["root_gone_runs"] == 1

    async def test_an_index_404_on_the_first_run_runs_nothing_and_writes_nothing(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes(index=[status(404)])) == 0
        assert pkg_runs.requests == [PKG.index_url]
        assert not Path("documentation", NS).exists() and not Path(".hashes", NS).exists()

    async def test_a_package_dropped_from_the_config_goes_whole(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes()) == 0
        other = fake_package("other-kit")
        pkg_runs.configure(other)
        routes = {other.index_url or "": [status(503)]}
        assert await pkg_runs.scrape(routes, "--sites", other.name) == 1  # its own index fails
        assert not Path("documentation", NS).exists() and not Path(".hashes", NS).exists()
        assert [e["reason"] for e in pkg_runs.logged("site_removed")] == ["not_configured"]
        assert Path(".hashes", "SPI").is_dir()


# KitCore's Group page lists 5 children only it links (the 2026-10-26 incident's
# actor-implementations); 7 other pages keep its 6 orphans under the valve
GROUP = "KitCore/Group"
GROUP_CHILDREN = [f"KitCore/Group/Child{n}" for n in range(1, 6)]
OTHERS = [f"KitCore/Other{n}" for n in range(1, 8)]
GROUPED: Pages = {
    **PAGES,
    "KitCore": (CORE_B, [*PAGES["KitCore"][1], (GROUP, CORE_B), *((path, CORE_B) for path in OTHERS)]),
    GROUP: (CORE_B, [(path, CORE_B) for path in GROUP_CHILDREN]),
    **{path: (CORE_B, []) for path in [*GROUP_CHILDREN, *OTHERS]},
}
SUBTREE = {pkg_file(path, "KitCore") for path in [GROUP, *GROUP_CHILDREN]}


def linking_proposal() -> Dict[str, List[Spec]]:
    """KitCore/Thing links the proposal only its excluded collection lists, inline (its abstract):
    a link, never a crawl link."""
    body = json.loads(topic_page("KitCore/Thing", CORE_B, [("KitCore", CORE_B)]))
    proposal = f"doc://{CORE_B}/documentation/KitCore/KP-0001"
    body["abstract"] = [{"type": "text", "text": "See "}, {"type": "reference", "identifier": proposal,
                                                           "isActive": True}]
    body["references"][proposal] = {"type": "topic", "url": "/documentation/kitcore/kp-0001", "title": "KP-0001",
                                    "identifier": proposal, "kind": "article", "role": "article"}
    return {pkg_json("KitCore/Thing"): [ok(json.dumps(body), "")]}


def collection(*paths: str) -> Dict[str, List[Spec]]:
    """The proposals collection, listing these pages."""
    return {pkg_json("KitCore/proposals"): [ok(topic_page("KitCore/proposals", CORE_B,
                                                          [(path, CORE_B) for path in paths]), "")]}


PROPOSAL_LINK = f"See [KP-0001]({pkg_doc('KitCore/KP-0001')})"


class TestExcludedCollection:
    """B7: the pages only an excluded collection lists (DocCSite.excluded_pages) are linked by URL."""

    def test_the_pages_a_collection_curates(self) -> None:
        body = json.loads(topic_page("KitCore/proposals", CORE_B, [
            ("KitCore/KP-0001", CORE_B), ("KitCore/KP-NNNN", CORE_B), ("KitCore", CORE_B),
            ("KitCore/proposals", CORE_B)]))
        body["topicSections"].append({"title": "Elsewhere", "identifiers": ["https://example.org/process"]})
        body["references"]["https://example.org/process"] = {"type": "link", "url": "https://example.org/process"}
        # Not the collection itself, nor a root (a top-level page is never excluded this way)
        assert docc_sites.collection_pages(PKG, "kitcore/proposals", json.dumps(body)) == [
            "kitcore/kp-0001", "kitcore/kp-nnnn"]
        for bad in ("not json", json.dumps([1])):
            with pytest.raises(ValueError):
                docc_sites.collection_pages(PKG, "kitcore/proposals", bad)

    def test_a_listed_page_is_linked_by_url_and_never_a_crawl_rule(self) -> None:
        site = dataclasses.replace(PKG, excluded_pages=frozenset({"kitcore/kp-0001"}))
        # Exactly the listed page; the excluded path and the pages under it as ever
        assert site.linked_by_url("kitcore/kp-0001") and not site.linked_by_url("kitcore/kp-0001/part")
        assert site.linked_by_url("kitcore/proposals") and site.linked_by_url("kitcore/proposals/x")
        assert not site.linked_by_url("kitcore/kp-00011") and not site.linked_by_url("kitcore")
        # The crawl's rule is the excluded paths alone
        assert not site.excluded("kitcore/kp-0001") and site.excluded("kitcore/proposals/x")

    async def test_a_page_only_it_lists_is_never_fetched_and_linked_by_url(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes(overrides=linking_proposal())) == 0
        assert docs() == ALL
        assert pkg_json("KitCore/KP-0001") not in pkg_runs.requests
        thing = pkg_file("KitCore/Thing", "KitCore").read_text()
        # Linked by its URL, as the collection is (a local link would point at no file)
        assert PROPOSAL_LINK in thing and "kp-0001.md" not in thing

    async def test_a_page_in_scope_curation_reaches_is_crawled_and_linked_locally(self, pkg_runs: SiteRuns) -> None:
        """A package author's collection lists an API page (KitCore/Thing): it is crawled as ever,
        never removed, and linked locally once a crawl has reached it."""
        routes = pkg_routes(overrides=collection("KitCore/KP-0001", "KitCore/Thing"))
        assert await scrape(pkg_runs, routes) == 0
        assert docs() == ALL
        assert site_metadata()["excluded_pages"] == {"kitcore/proposals": ["kitcore/kp-0001", "kitcore/thing"]}
        assert await scrape(pkg_runs, routes) == 0
        assert docs() == ALL and not pkg_runs.logged("orphans_deleted")
        # Recorded live, it is no excluded page: the sinks render again and link it locally
        assert "](./thing.md)" in pkg_file("KitCore", "KitCore").read_text()
        for root in ROOTS:
            assert metadata_of(hash_file(root))["render"] == {
                "version": AppleJSONDocumentationScraper.RENDER_VERSION, "excluded_pages": ["kitcore/kp-0001"]}
        before = sandbox_bytes()
        assert await scrape(pkg_runs, routes) == 0
        assert sandbox_bytes() == before

    async def test_a_failed_or_empty_collection_fetch_uses_what_it_last_listed(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes(overrides=linking_proposal())) == 0
        before = sandbox_bytes()
        # Its fetch fails (a 404 too: SPI answers one while it rebuilds), or it lists
        # nothing (served empty while it rebuilds): no error, nothing changes
        for answer in (status(404), status(500), ok(topic_page("KitCore/proposals", CORE_B, []), "")):
            overrides = {**linking_proposal(), pkg_json("KitCore/proposals"): [answer]}
            assert await scrape(pkg_runs, pkg_routes(overrides=overrides)) == 0
            assert [e["url"] for e in pkg_runs.logged("excluded_collection_failed")] == [
                pkg_json("KitCore/proposals")]
            assert pkg_json("KitCore/KP-0001") not in pkg_runs.requests
            assert sandbox_bytes() == before

    async def test_a_first_run_whose_collection_fetch_fails_links_it_locally_until_one_reads_it(
        self, pkg_runs: SiteRuns
    ) -> None:
        overrides = {**linking_proposal(), pkg_json("KitCore/proposals"): [status(500)]}
        assert await scrape(pkg_runs, pkg_routes(overrides=overrides)) == 0
        assert "excluded_pages" not in site_metadata()
        assert "](./kp-0001.md)" in pkg_file("KitCore/Thing", "KitCore").read_text()
        assert await scrape(pkg_runs, pkg_routes(overrides=linking_proposal())) == 0
        assert docs() == ALL
        # Its sinks' renderings record the excluded pages: the new set renders
        # every page again, Thing too (its JSON didn't change)
        assert PROPOSAL_LINK in pkg_file("KitCore/Thing", "KitCore").read_text()
        for root in ROOTS:
            assert metadata_of(hash_file(root))["render"] == {
                "version": AppleJSONDocumentationScraper.RENDER_VERSION, "excluded_pages": ["kitcore/kp-0001"]}


def entry_of(path: str, root: str = "KitCore") -> Dict[str, Any]:
    entry: Dict[str, Any] = json.loads(hash_file(root).read_text())["hashes"][pkg_json(path)]
    return entry


def gone_urls(runs: SiteRuns, event: str) -> List[str]:
    return [e["url"] for e in runs.logged(event)]


class TestPageGone:
    async def test_a_parent_404_keeps_its_subtree_one_run_then_removes_it(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes(GROUPED)) == 0
        files = docs()
        assert SUBTREE <= files and len(files) == 4 + 6 + 7
        gone = pkg_routes(GROUPED, overrides={pkg_json(GROUP): [status(404)]})
        # 1st run: the page and the 5 children only it links are kept; no error
        assert await scrape(pkg_runs, gone) == 0
        assert docs() == files
        assert gone_urls(pkg_runs, "page_gone_pending") == [pkg_json(GROUP)]
        assert pkg_json(GROUP) not in gone_urls(pkg_runs, "page_gone")
        assert not any(pkg_json(path) in pkg_runs.requests for path in GROUP_CHILDREN)
        entry = entry_of(GROUP)
        assert entry["consecutive_gone"] == 1 and entry["file_path"] == str(pkg_file(GROUP, "KitCore"))
        # 2nd in a row: removed with them
        assert await scrape(pkg_runs, gone) == 0
        assert docs() == files - SUBTREE
        assert gone_urls(pkg_runs, "page_gone") == [pkg_json(GROUP)] and not pkg_runs.logged("page_gone_pending")
        assert entry_of(GROUP) == {"status": "error", "error": "HTTP 404"}

    async def test_a_200_between_two_404s_resets_the_count(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes()) == 0
        gone = pkg_routes(overrides={pkg_json("KitCore/Thing"): [status(404)]})
        assert await scrape(pkg_runs, gone) == 0
        assert entry_of("KitCore/Thing")["consecutive_gone"] == 1
        assert await scrape(pkg_runs, pkg_routes()) == 0
        assert "consecutive_gone" not in entry_of("KitCore/Thing")
        assert await scrape(pkg_runs, gone) == 0
        assert docs() == ALL and entry_of("KitCore/Thing")["consecutive_gone"] == 1
        assert gone_urls(pkg_runs, "page_gone_pending") == [pkg_json("KitCore/Thing")]

    async def test_404_503_404_is_pending_then_blocked_then_pending(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes()) == 0
        thing = pkg_json("KitCore/Thing")
        gone = pkg_routes(overrides={thing: [status(404)]})
        assert await scrape(pkg_runs, gone) == 0
        assert entry_of("KitCore/Thing")["consecutive_gone"] == 1
        # A 503 that outlasts the retries: our failure (blocks, exits 1), and it ends the 404 count
        assert await scrape(pkg_runs, pkg_routes(overrides={thing: [status(503)]})) == 1
        entry = entry_of("KitCore/Thing")
        assert entry["consecutive_failures"] == 1 and "consecutive_gone" not in entry
        assert await scrape(pkg_runs, gone) == 0
        entry = entry_of("KitCore/Thing")
        assert entry["consecutive_gone"] == 1 and "consecutive_failures" not in entry
        assert docs() == ALL

    async def test_a_page_we_never_had_is_removed_at_once(self, pkg_runs: SiteRuns) -> None:
        assert await scrape(pkg_runs, pkg_routes(GROUPED)) == 0
        files = docs()
        # Newly linked and 404 (no route); Other1 unlinked in the same run, which the cleanup still removes
        pages: Pages = {**GROUPED, "KitCore": (CORE_B, [*(link for link in GROUPED["KitCore"][1]
                                                         if link[0] != "KitCore/Other1"),
                                                       ("KitCore/New", CORE_B)])}
        assert await scrape(pkg_runs, pkg_routes(pages)) == 0
        assert pkg_json("KitCore/New") in gone_urls(pkg_runs, "page_gone")
        assert not pkg_runs.logged("page_gone_pending")
        assert entry_of("KitCore/New") == {"status": "error", "error": "HTTP 404"}
        assert docs() == files - {pkg_file("KitCore/Other1", "KitCore")}

    async def test_a_module_page_waits_too(self, pkg_runs: SiteRuns) -> None:
        """A page of a module under the namespace (D6): its parent's cleanup is skipped, so the module isn't cleaned."""
        extras = [f"KitExtras/Leaf{n}" for n in range(1, 5)]
        pages: Pages = {
            **PAGES,
            "KitCore": (CORE_B, [*PAGES["KitCore"][1], ("KitExtras/One", CORE_B), *((p, CORE_B) for p in extras)]),
            "KitExtras/One": (CORE_B, [("KitExtras/One/Two", CORE_B)]),
            "KitExtras/One/Two": (CORE_B, []),
            **{path: (CORE_B, []) for path in extras},
        }
        assert await scrape(pkg_runs, pkg_routes(pages)) == 0
        one, two = pkg_file("KitExtras/One", "KitExtras"), pkg_file("KitExtras/One/Two", "KitExtras")
        files = docs()
        assert {one, two} <= files and hash_file("KitExtras").exists()
        gone = pkg_routes(pages, overrides={pkg_json("KitExtras/One"): [status(404)]})
        assert await scrape(pkg_runs, gone) == 0
        assert docs() == files
        assert gone_urls(pkg_runs, "page_gone_pending") == [pkg_json("KitExtras/One")]
        assert entry_of("KitExtras/One", "KitExtras")["consecutive_gone"] == 1
        assert await scrape(pkg_runs, gone) == 0
        assert docs() == files - {one, two}
        assert entry_of("KitExtras/One", "KitExtras") == {"status": "error", "error": "HTTP 404"}

    async def test_a_module_run_that_reaches_no_page_of_it_resets_the_count(self, pkg_runs: SiteRuns) -> None:
        """Its parent's page linking it fails, so the module has no sink that run: its pages' counts end too."""
        pages: Pages = {
            **PAGES,
            "KitCore": (CORE_B, [*PAGES["KitCore"][1], ("KitCore/Hub", CORE_B)]),
            "KitCore/Hub": (CORE_B, [("KitExtras/One", CORE_B)]),
            "KitExtras/One": (CORE_B, [("KitExtras/One/Two", CORE_B)]),
            "KitExtras/One/Two": (CORE_B, []),
        }
        assert await scrape(pkg_runs, pkg_routes(pages)) == 0
        one = pkg_file("KitExtras/One", "KitExtras")
        files = docs()
        gone = pkg_routes(pages, overrides={pkg_json("KitExtras/One"): [status(404)]})
        assert await scrape(pkg_runs, gone) == 0
        assert entry_of("KitExtras/One", "KitExtras")["consecutive_gone"] == 1
        # The hub fails (ours: exit 1): no page of the module is reached
        assert await scrape(pkg_runs, pkg_routes(pages, overrides={pkg_json("KitCore/Hub"): [status(503)]})) == 1
        assert not any("/kitextras/" in url for url in pkg_runs.requests)
        assert "consecutive_gone" not in entry_of("KitExtras/One", "KitExtras")
        assert [e["module"] for e in pkg_runs.logged("unreached_module_counts_reset")] == ["KitExtras"]
        # A single 404 after it is a first one again
        assert await scrape(pkg_runs, gone) == 0
        assert gone_urls(pkg_runs, "page_gone_pending") == [pkg_json("KitExtras/One")]
        assert one.exists() and docs() == files
