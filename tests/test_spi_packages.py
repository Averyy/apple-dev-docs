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
  proposals collection and the proposals only it lists are never fetched,
  and a second run changes nothing.
- Removal, all automatic (D6 rule 7, row 3): a root answering 404 on 2
  consecutive runs; a target its index stops listing while its JSON still
  answers 200 (deleted on the 2nd load without it); the index answering 404
  on 2 consecutive runs (the package goes whole; a 3rd such run, the package
  still configured, exits 0 and re-creates nothing); an index failure of
  ours counts nothing.
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
    """The fake host answers without an ETag (SPI's), so every page is fetched in full each run."""

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
        assert {package.namespace: package for package in packages}["SPI/CareKit"].framework_label(
            "CareKitStore") == "CareKit/CareKitStore"
        for package in packages:
            assert package.roots_from_index and not package.roots and package.namespace_top == "SPI"
            assert package.label == "Swift Package Index"
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
        # SPI's 503s last ~10 s on their URL: its retries wait past that; its jobs share the limiter, 4 at a time
        spi = site_config.SPI_PACKAGES[0]
        assert (spi.max_retries, spi.retry_backoff, spi.max_jobs) == (4, 6.0, 4)
        assert all((package.max_retries, package.retry_backoff, package.max_jobs) == (4, 6.0, 4)
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
        # OD3: the excluded collection and the proposal only it lists; OD5: no tutorial
        for path in ("KitCore/proposals", "KitCore/KP-0001"):
            assert pkg_json(path) not in fetched, path
        assert not [url for url in fetched if "/tutorials/" in url]
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
        packages = [fake_package(f"kit-{n}") for n in range(3)]
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
        assert len(docs()) == 3 * len(ALL)
        assert peak == 4  # 6 jobs on one host whose cap is 4


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
