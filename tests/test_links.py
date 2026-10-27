"""Local links (4.10): every link to an Apple documentation page goes through
the scraper's own path rule (naming.page_path), relative to the linking file.

- links.doc_link: the target file relative to the linking file's folder,
  "./" unless it starts with "../", quoted (safe "/,"), the #fragment after
  ".md"; the Apple URL for a dir that isn't known;
- the Apple converter: inline references (the page being converted) and the
  Topics/See Also/Relationships/Mentions links (its source_url) agree;
- the known dirs: naming.dirmap over the hash files and the run's frameworks
  (scrape_all_frameworks.known_dirs), so a framework scraped for the first
  time links, and is linked to, locally;
- links.markdown_url: a page's footer URL as a link holds it (an unclosed "("
  of a URL the site cut is encoded, any other URL is as it is), and
  unquote gives the page's URL back.
"""

import json
import os
import posixpath
import sys
from pathlib import Path
from typing import Any, Dict, Iterator, List
from urllib.parse import unquote

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts', 'utilities')))

import scrape_all_frameworks
from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.sink import SinkRegistry
from scraper.site import spi_package
from scraper.utils.links import doc_link, link_base, markdown_url
from scraper.utils.markdown_converter import AppleDocMarkdownConverter
from scraper.utils.naming import page_path
from tests.test_exit_codes import CI, scrape
from tests.test_failure_policy import Runs, sandbox_runs
from tests.test_fetch_results import Spec, json_url, ok

DOC = "https://developer.apple.com/documentation"
DIRS = {"swiftui": "SwiftUI", "swift": "Swift", "xctest": "XCTest", "testkit": "TestKit"}
# A page two folders down: its links are relative to TestKit/widget/
PAGE = f"{DOC}/testkit/widget/size"


def resolves(link: str, page_file: str, target_file: str) -> bool:
    """The link, read as the MCP server does (unquoted, from the page's folder), names the target."""
    path = unquote(link.partition('#')[0])
    return posixpath.normpath(posixpath.join(posixpath.dirname(page_file), path)) == target_file


class TestDocLink:
    base = link_base("TestKit", PAGE)

    def test_the_base_is_the_page_files_folder(self) -> None:
        assert self.base == "TestKit/widget"
        assert link_base("TestKit", f"{DOC}/testkit") == "TestKit"
        assert link_base("TestKit", f"{DOC}/testkit/widget") == "TestKit"
        # A URL of no page of the dir: its files are under the dir
        assert link_base("TestKit", "") == "TestKit"
        assert link_base("TestKit", f"{DOC}/otherkit/x") == "TestKit"

    @pytest.mark.parametrize("url, link", [
        # Same folder, a parent folder, another branch, the framework root
        (f"{DOC}/testkit/widget/color", "./color.md"),
        (f"{DOC}/testkit/widget", "../widget.md"),
        (f"{DOC}/testkit/gauge/value", "../gauge/value.md"),
        (f"{DOC}/testkit", "../TestKit.md"),
        (f"{DOC}/TestKit/Widget/Color", "./color.md"),
        # A page named like its framework: -page, in the folder position too
        (f"{DOC}/xctest/xctest", "../../XCTest/xctest-page.md"),
        (f"{DOC}/xctest/xctest/run()", "../../XCTest/xctest-page/run%28%29.md"),
        # Another framework, through the dirmap's casing
        (f"{DOC}/swiftui/view", "../../SwiftUI/view.md"),
        # An operator's name, with parentheses (quoted) and its label commas
        (f"{DOC}/swift/comparable/'...(_:_:)", "../../Swift/comparable/dotdotdot%28_,_%29.md"),
        (f"{DOC}/swift/equatable/==(_:_:)-3axv1", "../../Swift/equatable/eqeq%28_,_%29-3axv1.md"),
        (f"{DOC}/swiftui/view/frame(width:height:alignment:)",
         "../../SwiftUI/view/frame%28width,height,alignment%29.md"),
        # A name starting with a digit, a space
        (f"{DOC}/testkit/3180904-merge", "../api-3180904-merge.md"),
        (f"{DOC}/testkit/Editor Integration", "../editor-integration.md"),
        # The fragment is split off before the path rule, kept after ".md"
        (f"{DOC}/testkit/guide#Configure-the-widget", "../guide.md#Configure-the-widget"),
        (f"{DOC}/swiftui/view/padding(_:_:)#Discussion", "../../SwiftUI/view/padding%28_,_%29.md#Discussion"),
        # A query names no other file; a trailing slash is the same page
        (f"{DOC}/testkit/guide?language=objc", "../guide.md"),
        (f"{DOC}/swiftui/", "../../SwiftUI/SwiftUI.md"),
    ])
    def test_a_known_dirs_page_is_its_file_relative_to_the_page(self, url: str, link: str) -> None:
        assert doc_link(url, self.base, DIRS) == link
        assert link.startswith(("./", "../"))
        target = page_path(DIRS[url[len(DOC) + 1:].split('/')[0].lower()], url.partition('#')[0].partition('?')[0].rstrip('/'))
        assert target is not None and resolves(link, page_path("TestKit", PAGE) or "", target)

    @pytest.mark.parametrize("url", [
        f"{DOC}/otherkit/thing",            # a dir we don't have
        f"{DOC}/otherkit/thing#Overview",
        f"{DOC}/",                          # no framework
        "https://www.usb.org/",             # not a documentation page
        "https://developer.apple.com/design/human-interface-guidelines/color",
        "https://developer.apple.com/tutorials/swiftui",
    ])
    def test_anything_else_keeps_its_url(self, url: str) -> None:
        assert doc_link(url, self.base, DIRS) == url


# A symbol's URL Apple cut inside its argument list (as its JSON names it)
CUT = f"{DOC}/accelerate/bnns/fusedconvolutionnormalizationlayer/init(input:output:filter-30cwy"


class TestMarkdownUrl:
    @pytest.mark.parametrize("url", [
        f"{DOC}/swiftui/view/frame(width:height:alignment:)",
        f"{DOC}/swift/comparable/'...(_:_:)",
        f"{DOC}/swift/array/init()",
        f"{DOC}/testkit/guide#Setup",
        "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/x/init(from:)",
        "https://docs.swift.org/swiftpm/documentation/packagedescription",
    ])
    def test_a_url_whose_parentheses_pair_up_is_as_it_is(self, url: str) -> None:
        assert markdown_url(url) == url

    def test_unpaired_parentheses_are_encoded(self) -> None:
        assert markdown_url(CUT) == CUT.replace("init(", "init%28")
        assert markdown_url("https://h.test/a)b(c") == "https://h.test/a%29b%28c"
        assert markdown_url("https://h.test/(a)(b") == "https://h.test/%28a%29%28b"
        # Characters a link can't hold, as the MCP server's link_url encodes them
        assert markdown_url("https://h.test/caf\u00e9 <x>") == "https://h.test/caf%C3%A9%20%3Cx%3E"

    def test_an_encoded_url_is_not_encoded_again(self) -> None:
        once = markdown_url(CUT)
        assert markdown_url(once) == once
        assert markdown_url(f"{DOC}/x/a%28b%29") == f"{DOC}/x/a%28b%29"
        assert unquote(once) == CUT

    @pytest.mark.parametrize("site,url,label", [
        (None, CUT, "Apple Developer"),
        (spi_package("ml-explore", "mlx-swift-lm"),
         "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/smollm3configuration/"
         "init(modeltype:hiddensize:noropelayerinterval:-614q5", "Swift Package Index"),
    ])
    def test_the_footer_of_a_cut_url_is_a_valid_link(self, tmp_path: Path, site: Any, url: str, label: str) -> None:
        converter = (AppleDocMarkdownConverter(tmp_path / "Accelerate") if site is None
                     else AppleDocMarkdownConverter(tmp_path / "SPI" / "mlx-swift-lm" / "MLXLLM", site=site))
        md = converter.convert_page({"title": "init", "source_url": url})
        assert md.endswith(f"\n---\n\n*[View on {label}]({url.replace('init(', 'init%28')})*")
        # A namespaced site's front matter keeps the URL as scraped (a YAML string)
        assert (f'url: "{url}"' in md) == (site is not None)

    def test_the_footer_of_any_other_url_is_as_before(self, tmp_path: Path) -> None:
        url = f"{DOC}/swiftui/view/frame(width:height:alignment:)"
        md = AppleDocMarkdownConverter(tmp_path / "SwiftUI").convert_page({"title": "frame", "source_url": url})
        assert md.endswith(f"\n---\n\n*[View on Apple Developer]({url})*")


@pytest.fixture
def runs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Runs]:
    yield sandbox_runs(tmp_path, monkeypatch)


def ref(identifier: str) -> Dict[str, Any]:
    return {"type": "reference", "identifier": identifier, "isActive": True}


class TestConverterLinks:
    def test_inline_references_and_topics_agree(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """A page two folders down links each reference the same way in its prose and in its Topics."""
        monkeypatch.setattr(Config, "OUTPUT_DIR", tmp_path / "documentation")
        monkeypatch.setattr(Config, "CACHE_DIR", tmp_path / ".hashes")
        scraper = AppleJSONDocumentationScraper("TestKit", sinks=SinkRegistry({"swiftui": "SwiftUI", "swift": "Swift"}))
        targets = {
            "doc://t/documentation/TestKit/Widget/Color": ("Color", "/documentation/testkit/widget/color", "./color.md"),
            "doc://t/documentation/TestKit/TestKit": ("TestKit", "/documentation/testkit/testkit", "../testkit-page.md"),
            "doc://t/documentation/SwiftUI/View": ("View", "/documentation/swiftui/view", "../../SwiftUI/view.md"),
            "doc://t/documentation/Swift/Comparable/...(_:_:)": (
                "...(_:_:)", "/documentation/swift/comparable/'...(_:_:)", "../../Swift/comparable/dotdotdot%28_,_%29.md"),
            "doc://t/documentation/TestKit/guide#Setup": ("Setup", "/documentation/testkit/guide#Setup", "../guide.md#Setup"),
            # Another bundle's page of a dir no hash file has: its URL
            "doc://o/documentation/OtherKit/Thing": ("Thing", "/documentation/otherkit/thing", f"{DOC}/otherkit/thing"),
            # A module of the page's bundle (D6): local from its first run, the
            # dir its identifier cases (_module_link_dirs)
            "doc://t/documentation/ModKit/Part": ("Part", "/documentation/modkit/part", "../../ModKit/part.md"),
        }
        references = {identifier: {"type": "topic", "kind": "article", "role": "article", "title": title, "url": url}
                      for identifier, (title, url, _) in targets.items()}
        json_page = {
            "identifier": {"url": "doc://t/documentation/TestKit/Widget/size", "interfaceLanguage": "swift"},
            "kind": "article", "metadata": {"title": "size"}, "references": references,
            "primaryContentSections": [{"kind": "content", "content": [
                {"type": "paragraph", "inlineContent": [ref(identifier) for identifier in targets]}]}],
            "topicSections": [{"title": "Links", "identifiers": list(targets)}],
        }
        md = scraper.markdown_converter.convert_page(scraper._extract_from_json(scraper.sink, json_page, PAGE, None))
        for title, _, link in targets.values():
            assert f"[{title}]({link})" in md.split("## Topics")[0], title
            assert f"- [{title}]({link})" in md.split("## Topics")[1], title

    def test_known_dirs_are_the_dirmap_and_the_runs_frameworks(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """A framework without a hash file yet (its first scrape) is known by its id, a framework
        with one by the hash file's casing; the other scrapers' hash files name no dir."""
        hashes = tmp_path / ".hashes"
        hashes.mkdir()
        monkeypatch.setattr(Config, "CACHE_DIR", hashes)
        (hashes / "SwiftUI_hashes.json").write_text(json.dumps(
            {"metadata": {}, "hashes": {f"{AppleJSONDocumentationScraper.JSON_BASE_URL}/swiftui.json": {}}}))
        (hashes / "hig_docs_hashes.json").write_text(json.dumps(
            {"metadata": {}, "hashes": {"https://developer.apple.com/tutorials/data/design/x.json": {}}}))
        frameworks = [{"id": "NewKit", "title": "New Kit"}, {"id": "swiftui", "title": "SwiftUI"}]
        assert scrape_all_frameworks.known_dirs(frameworks) == {"swiftui": "SwiftUI", "newkit": "NewKit"}


def linking_page(fw: str, path: str, links: List[str]) -> str:
    """An Apple JSON page whose Topics link to these pages (doc URL paths), in any framework."""
    return json.dumps({
        "identifier": {"url": f"doc://com.apple.{fw}/documentation/{path}", "interfaceLanguage": "swift"},
        "metadata": {"title": path.split("/")[-1], "symbolKind": "class", "roleHeading": "Class"},
        "topicSections": [{"title": "Topics", "identifiers": [
            f"doc://com.apple.{link.split('/')[0]}/documentation/{link}" for link in links]}],
    })


async def test_first_scraped_frameworks_link_to_each_other_locally(
    runs: Runs, monkeypatch: pytest.MonkeyPatch
) -> None:
    """scrape.py --frameworks testkit otherkit, with neither scraped before: each links to itself
    and to the other locally (the run's frameworks are known), and every link resolves."""
    pages = {
        "testkit": ["testkit/alpha", "otherkit/one"],
        "testkit/alpha": ["testkit", "otherkit"],
        "otherkit": ["otherkit/one"],
        "otherkit/one": ["testkit/alpha", "elsewhere/page"],
    }
    routes: Dict[str, List[Spec]] = {
        json_url(path): [ok(linking_page(path.split('/')[0], path, links), f"E-{path}")]
        for path, links in pages.items()
    }
    assert await scrape(monkeypatch, routes, "--frameworks", "testkit", "otherkit", *CI) == 0
    expected = {
        "documentation/testkit/testkit.md": {"alpha": "./alpha.md", "one": "../otherkit/one.md"},
        "documentation/testkit/alpha.md": {"testkit": "./testkit.md", "otherkit": "../otherkit/otherkit.md"},
        "documentation/otherkit/otherkit.md": {"one": "./one.md"},
        "documentation/otherkit/one.md": {"alpha": "../testkit/alpha.md",
                                          "page": f"{DOC}/elsewhere/page"},
    }
    for file, links in expected.items():
        text = Path(file).read_text(encoding="utf-8")
        for title, link in links.items():
            assert f"- [{title}]({link})" in text, (file, title)
            if not link.startswith("https://"):
                assert Path(posixpath.normpath(posixpath.join(posixpath.dirname(file), link))).is_file()
