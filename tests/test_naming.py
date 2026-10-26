"""The page naming (scraper.utils.naming): seg_name, the path rule, the dirmap.

The injectivity test checks that no two pages get the same file, over every
key of the repo's Apple hash files, plus a navigator-path fixture when
NAVIGATOR_FIXTURE names one (built at window-gate time by
scripts/utilities/build_navigator_fixture.py). No workflow runs it: run it in
a scratch copy that holds .hashes (or NAMING_HASH_DIR), whenever naming.py
changes. With no Apple hash file it skips, or fails when either variable is
set (a gate run).
"""

import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set

import pytest
from structlog.testing import capture_logs

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import site as site_config
from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils import naming
from scraper.utils.hash_manager import read_hash_file
from scraper.utils.naming import (
    DOC_URL_PREFIX, JSON_URL_PREFIX, SEGMENT_MAX, clash_suffix, dirmap, page_path, seg_name,
)

REPO = Path(__file__).resolve().parent.parent
# The configured DocC sites, as imported (tests run with none: conftest)
CONFIGURED_SITES = site_config.DOCC_SITES
ALPHABET = re.compile(r'[a-z0-9._(),-]+')


class TestSegName:
    @pytest.mark.parametrize("segment, name", [
        # The spec's examples
        ("setNeedsDisplay()", "setneedsdisplay()"),
        ("setNeedsDisplay(_:)", "setneedsdisplay(_)"),
        ("init(_:count:)", "init(_,count)"),
        ("'...(_:_:)", "dotdotdot(_,_)"),
        ("'.==(_:_:)-8szzf", "doteqeq(_,_)-8szzf"),
        ("3180904-merge", "api-3180904-merge"),
        ("$state", "dollarstate"),
        ("Editor Integration", "editor-integration"),
        # Overloads that differ in arity or only in "_" labels stay apart
        ("abGroupRemoveMember(_:_:)", "abgroupremovemember(_,_)"),
        ("abGroupRemoveMember(_:_:_:)", "abgroupremovemember(_,_,_)"),
        # Operators: only when everything before "(" is operator characters
        ("+(_:_:)", "plus(_,_)"),
        ("!=(_:_:)", "noteq(_,_)"),
        ("&&(_:_:)", "ampamp(_,_)"),
        ("~=(_:_:)", "tildeeq(_,_)"),
        ("_(_:_:)", "op(_,_)"),
        ("'.._(_:_:)", "dotdotop(_,_)"),
        ("*=(_:_:)-3kxzh", "stareq(_,_)-3kxzh"),
        ("subscript(_:)", "subscript(_)"),
        # A list that isn't only labels is kept verbatim (then cleaned)
        ("foo(bar)", "foo(bar)"),
        ("init?(rawValue: Int)", "init_(rawvalue_-int)"),
        # The remaining specials
        ("a:b", "a_b"),
        ("@MainActor", "atmainactor"),
        ("it's", "its"),
        ("Font.Weight", "font.weight"),
        ("reason-swift.struct", "reason-swift.struct"),
        ("com.apple.developer.aps-environment", "com.apple.developer.aps-environment"),
        # Only one leading "'" is dropped
        ("''x", "x"),
    ])
    def test_names(self, segment: str, name: str) -> None:
        assert seg_name(segment) == name

    @pytest.mark.parametrize("segment, name", [
        ("  spaced\tout  ", "spaced-out"),
        ("-dashes-", "dashes"),
        ("organization.", "organization"),
        ("x..", "x"),
        ("-.hidden", "dothidden"),
        ("..", "unnamed"),
        ("", "unnamed"),
        ("-", "unnamed"),
        ("2fa", "api-2fa"),
    ])
    def test_closure(self, segment: str, name: str) -> None:
        assert seg_name(segment) == name

    def test_characters_outside_the_alphabet_become_underscores_logged_once_each(self) -> None:
        naming._warned_chars.clear()
        with capture_logs() as events:
            assert seg_name("über") == "_ber"
            assert seg_name("x%y") == "x_y"
            assert seg_name("ü%") == "__"
        warned = [e["char"] for e in events if e["event"] == "seg_name_unmapped_char"]
        assert warned == ["ü", "%"]

    @pytest.mark.parametrize("segment", [
        "setNeedsDisplay(_:)", "'..<(_:_:)", "über alles", "a/b", "x?y", "<>|^%", "''.''", "Ω(_:)",
    ])
    def test_output_alphabet(self, segment: str) -> None:
        name = seg_name(segment)
        assert ALPHABET.fullmatch(name), name
        assert not name.startswith('.') and not name.endswith('.')

    def test_cap(self) -> None:
        longest = "a" * (SEGMENT_MAX - len(".md"))
        assert seg_name(longest) == longest
        raw = "A" * (SEGMENT_MAX - len(".md") + 1)
        capped = seg_name(raw)
        digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:8]
        assert capped == "a" * 218 + "-" + digest
        assert len(capped.encode()) + len(".md") <= SEGMENT_MAX
        # Room for the tripwire's suffix and an atomic write's .tmp under NAME_MAX
        assert len(capped) + len(clash_suffix("x")) + len(".md.tmp") <= 255


class TestPagePath:
    @pytest.mark.parametrize("url, path", [
        ("https://developer.apple.com/documentation/XCTest", "XCTest/XCTest.md"),
        ("https://developer.apple.com/documentation/xctest", "XCTest/XCTest.md"),
        ("https://developer.apple.com/documentation/xctest/xctestcase", "XCTest/xctestcase.md"),
        ("https://developer.apple.com/documentation/xctest/xctestcase/wait(for:timeout:)",
         "XCTest/xctestcase/wait(for,timeout).md"),
        # Named like its framework: "-page" in the file and the folder position
        ("https://developer.apple.com/documentation/xctest/xctest", "XCTest/xctest-page.md"),
        ("https://developer.apple.com/documentation/xctest/xctest/init()", "XCTest/xctest-page/init().md"),
        # Only the first segment
        ("https://developer.apple.com/documentation/xctest/xctestcase/xctest", "XCTest/xctestcase/xctest.md"),
    ])
    def test_paths(self, url: str, path: str) -> None:
        assert page_path("XCTest", url) == path

    def test_folders_equal_their_file_stems(self) -> None:
        parent = page_path("UIKit", "https://developer.apple.com/documentation/uikit/uiview/reason-swift.struct")
        child = page_path("UIKit", "https://developer.apple.com/documentation/uikit/uiview/reason-swift.struct/x")
        assert parent is not None and child is not None
        assert Path(child).parent == Path(parent).with_suffix("")

    @pytest.mark.parametrize("url", [
        "https://developer.apple.com/documentation/uikitx/uiview",
        "https://developer.apple.com/documentation/swiftui/view",
        "https://example.com/documentation/uikit/uiview",
    ])
    def test_another_frameworks_url_has_none(self, url: str) -> None:
        assert page_path("UIKit", url) is None

    def test_the_scraper_uses_it(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(Config, "OUTPUT_DIR", tmp_path / "docs")
        monkeypatch.setattr(Config, "CACHE_DIR", tmp_path / ".hashes")
        scraper = AppleJSONDocumentationScraper("XCTest")
        url = "https://developer.apple.com/documentation/xctest/xctest/init()"
        sink = scraper.sink
        assert scraper._get_organized_file_path(sink, url, {}) == tmp_path / "docs" / "XCTest/xctest-page/init().md"
        # The path depends on the URL alone
        assert scraper._get_organized_file_path(sink, url, {"symbol_kind": "class"}) == scraper._get_organized_file_path(sink, url, {})

    def test_the_doc_url_and_json_url_give_the_same_path(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(Config, "CACHE_DIR", tmp_path / ".hashes")
        scraper = AppleJSONDocumentationScraper("swift")
        json_url = f"{JSON_URL_PREFIX}swift/comparable/'...(_:_:).json"
        doc_url = scraper._convert_json_url_to_doc_url(json_url)
        assert page_path("swift", doc_url) == "swift/comparable/dotdotdot(_,_).md"


def test_clash_suffix_is_the_lowercased_json_urls_digest() -> None:
    url = f"{JSON_URL_PREFIX}UIKit/UIView.json"
    assert clash_suffix(url) == "-" + hashlib.sha256(url.lower().encode()).hexdigest()[:8]
    assert clash_suffix(url) == clash_suffix(url.lower())


def test_dirmap(tmp_path: Path) -> None:
    def write(name: str, keys: List[str]) -> None:
        data = {"metadata": {"total_pages": len(keys)}, "hashes": {key: {"hash": "h"} for key in keys}}
        (tmp_path / f"{name}_hashes.json").write_text(json.dumps(data))

    write("XCTest", [f"{DOC_URL_PREFIX}XCTest", f"{JSON_URL_PREFIX}XCTest.json"])
    write("AppStoreConnectAPI", [f"{JSON_URL_PREFIX}appstoreconnectapi/app.json"])
    write("hig_docs", ["https://developer.apple.com/tutorials/data/design/human-interface-guidelines/color.json"])
    write("docless", [f"{DOC_URL_PREFIX}docless/x"])
    (tmp_path / "broken_hashes.json").write_text("{")
    assert dirmap(tmp_path) == {"xctest": "XCTest", "appstoreconnectapi": "AppStoreConnectAPI"}


def navigator_paths(fixture: Path) -> Set[str]:
    """The fixture's paths: /documentation/<…>, lowercased, dot segments '-escaped."""
    return {line.strip() for line in fixture.read_text(encoding="utf-8").splitlines() if line.strip()}


def test_page_path_is_injective() -> None:
    """No two pages share a file (case-insensitively): over every hash key, and the navigator fixture.

    A page's identity is its lowercased JSON URL with dot segments '-escaped
    as the crawler does (_escape_dot_path_segments: an old error entry's
    unescaped URL is the same page); its JSON-URL and doc-URL keys must give
    the same path. Every name is within the cap and the alphabet. The
    configured DocC sites' hash files (.hashes/<namespace>/) are read too:
    their pages are under their namespace, which no Apple dir may be.
    """
    escape = AppleJSONDocumentationScraper._escape_dot_path_segments
    hash_dir = Path(os.environ.get("NAMING_HASH_DIR", REPO / ".hashes"))
    dirs = dirmap(hash_dir) if hash_dir.is_dir() else {}
    if not dirs:
        if os.environ.get("NAVIGATOR_FIXTURE") or os.environ.get("NAMING_HASH_DIR"):
            # A gate run: a skip would look like a pass
            pytest.fail(f"no Apple hash file in {hash_dir} (NAVIGATOR_FIXTURE or NAMING_HASH_DIR is set)")
        pytest.skip(f"no Apple hash file in {hash_dir}")
    by_path: Dict[str, Set[str]] = defaultdict(set)
    paths_of: Dict[str, Set[str]] = defaultdict(set)
    foreign: List[str] = []
    for name in sorted(dirs.values()):
        hashes, _ = read_hash_file(hash_dir / f"{name}{naming.HASH_FILE_SUFFIX}")
        for key in hashes:
            if key.startswith(JSON_URL_PREFIX) and key.endswith(".json"):
                rest = key[len(JSON_URL_PREFIX):-len(".json")]
            elif key.startswith(DOC_URL_PREFIX):
                rest = key[len(DOC_URL_PREFIX):]
            else:
                continue
            identity = f"{JSON_URL_PREFIX}{escape(rest.lower())}.json"
            path = page_path(name, DOC_URL_PREFIX + rest)
            if path is None:
                foreign.append(key)
                continue
            by_path[path.lower()].add(identity)
            paths_of[identity].add(path)
    # The DocC sites' pages: <namespace>/<Dir>/…
    site_dirs: Dict[str, str] = {}
    for docc_site in CONFIGURED_SITES:
        site_hash_dir = hash_dir / docc_site.namespace
        found = dirmap(site_hash_dir, docc_site.json_prefix) if site_hash_dir.is_dir() else {}
        assert docc_site.namespace_top.lower() not in dirs, docc_site.namespace
        for name in sorted(found.values()):
            site_dirs[f"{docc_site.namespace}/{name}"] = name
            hashes, _ = read_hash_file(site_hash_dir / f"{name}{naming.HASH_FILE_SUFFIX}")
            for key in hashes:
                if key.startswith(docc_site.json_prefix) and key.endswith(".json"):
                    rest = key[len(docc_site.json_prefix):-len(".json")]
                elif key.startswith(docc_site.doc_prefix):
                    rest = key[len(docc_site.doc_prefix):]
                else:
                    continue
                identity = f"{docc_site.json_prefix}{escape(rest.lower())}.json"
                path = page_path(name, docc_site.doc_prefix + rest, docc_site)
                if path is None:
                    foreign.append(key)
                    continue
                by_path[path.lower()].add(identity)
                paths_of[identity].add(path)
    keys = len(paths_of)

    fixture = os.environ.get("NAVIGATOR_FIXTURE")
    unknown = 0
    if fixture:
        for nav_path in navigator_paths(Path(fixture)):
            rest = nav_path[len("/documentation/"):]
            dir_name = dirs.get(rest.split("/")[0])
            if dir_name is None:
                unknown += 1
                continue
            path = page_path(dir_name, DOC_URL_PREFIX + rest)
            assert path is not None
            identity = f"{JSON_URL_PREFIX}{rest}.json".lower()
            by_path[path.lower()].add(identity)
            paths_of[identity].add(path)

    collisions = {path: sorted(ids) for path, ids in by_path.items() if len(ids) > 1}
    split = {identity: sorted(paths) for identity, paths in paths_of.items() if len(paths) > 1}
    # Every name seg_name gave (a root page, <Dir>/<Dir>.md, is named by its dir)
    roots = {f"{dir_name}/{dir_name}.md" for dir_name in dirs.values()}
    roots |= {f"{base}/{dir_name}.md" for base, dir_name in site_dirs.items()}

    def page_names(path: str) -> List[str]:
        """The names after a page's dir (a DocC site's dir is <namespace>/<Dir>)."""
        for base in site_dirs:
            if path.startswith(f"{base}/"):
                return path[len(base) + 1:].split("/")
        return path.split("/")[1:]

    names = {part for paths in paths_of.values() for path in paths if path not in roots for part in page_names(path)}
    print(f"\n{len(dirs)} dirs + {len(site_dirs)} DocC site dirs, {keys:,} pages from hash keys, "
          f"{len(paths_of) - keys:,} more from "
          f"the navigator fixture ({unknown:,} paths of unknown dirs), {len(by_path):,} paths")
    assert foreign == []
    assert collisions == {}, list(collisions.items())[:10]
    assert split == {}, list(split.items())[:10]
    assert max(len(part.encode()) for part in names) <= SEGMENT_MAX
    assert all(ALPHABET.fullmatch(part[:-len(".md")] if part.endswith(".md") else part) for part in names)
