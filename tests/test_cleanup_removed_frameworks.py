"""The pre-scrape removal of frameworks technologies.json no longer lists (2.5).

cleanup_removed_frameworks.py judges the Apple framework hash files only (no
doc folder scan, no request but technologies.json): each run that finds a
framework unlisted counts it in metadata.unlisted_runs, and the 2nd
consecutive one deletes its docs dir and hash file, however many frameworks
go at once. A framework listed again starts over (reset by this script and
by the scrape's save). A failed or empty fetch counts nothing and exits 1.
An unlisted framework's hash file that can't be read (judged by its docs dir)
is replaced by one counting the run (exit 1), so it is still removed a run
later. Also the scrape's list guard (check_framework_list), which leaves out the
frameworks already counted as unlisted. Runs in a sandbox (cwd = tmp_path).
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any, Callable, Dict, Iterator, List, Optional, Sequence, Type

import httpx
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts', 'utilities')))

import cleanup_removed_frameworks
import framework_list_scraper
import scrape_all_frameworks
from cleanup_removed_frameworks import UNLISTED_REMOVAL_RUNS, framework_hash_files
from scrape_all_frameworks import ScrapeAborted, check_framework_list
from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.hash_manager import HashManager
from tests.test_failure_policy import FW, SITE, Apple, Runs, file_of, routes_for, sandbox_runs, seeded
from tests.test_fetch_results import doc_url, json_url


@pytest.fixture
def runs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Runs]:
    yield sandbox_runs(tmp_path, monkeypatch)


def make_framework(fw: str, pages: int = 2, docs_dir: Optional[str] = None,
                   hash_file: Optional[Path] = None, **metadata: Any) -> Path:
    """An Apple framework as a scrape leaves it: its docs and its hash file (JSON-URL and doc-URL keys)."""
    docs = Config.OUTPUT_DIR / (docs_dir or fw)
    hash_file = hash_file or Config.get_hash_file(fw)
    manager = HashManager(hash_file)
    for i in range(pages):
        path = docs / f"page{i}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# {fw} page {i}\n")
        for url in (json_url(f"{fw.lower()}/page{i}"), doc_url(f"{fw.lower()}/page{i}")):
            manager.update_hash(url, path.read_text(), f"E-{i}", path)
    for key, value in metadata.items():
        manager.set_metadata(key, value)
    assert manager.save()
    return hash_file


def listing(ids: Sequence[str]) -> Type[Any]:
    """Stands in for AppleFrameworkListScraper: technologies.json lists these ids."""

    class Listing:
        async def __aenter__(self) -> "Listing":
            return self

        async def __aexit__(self, *exc: Any) -> None:
            return None

        async def fetch_all_frameworks(self) -> List[Dict[str, str]]:
            return frameworks(ids)

    return Listing


def frameworks(ids: Sequence[str]) -> List[Dict[str, str]]:
    """The shared parser's output for a technologies.json listing these ids."""
    return [{"id": fw, "title": fw.title(), "url": f"/documentation/{fw}"} for fw in ids]


def prescrape(monkeypatch: pytest.MonkeyPatch, listed: Optional[Sequence[str]],
              flags: Sequence[str] = ("--yes",)) -> int:
    """One run of cleanup_removed_frameworks.py with these flags (CI's --yes by default); its exit code.

    listed: The ids technologies.json lists (None: the real parser, which the test serves)
    """
    if listed is not None:
        monkeypatch.setattr(cleanup_removed_frameworks, "AppleFrameworkListScraper", listing(listed))
    monkeypatch.setattr(sys, "argv", ["cleanup_removed_frameworks.py", *flags])
    code: int = cleanup_removed_frameworks.main()
    return code


def snapshot() -> Dict[str, bytes]:
    """Every file under the sandbox's docs and hash dirs."""
    return {
        str(path): path.read_bytes()
        for root in (Config.OUTPUT_DIR, Config.CACHE_DIR)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def saved(fw: str) -> Dict[str, Any]:
    data: Dict[str, Any] = json.loads(Config.get_hash_file(fw).read_text())
    return data


def on_disk(fw: str, docs_dir: Optional[str] = None) -> bool:
    """Whether the framework's docs dir or hash file is still there."""
    return (Config.OUTPUT_DIR / (docs_dir or fw)).exists() or Config.get_hash_file(fw).exists()


def case_sensitive(path: Path) -> bool:
    """Whether the filesystem holding path tells names apart by case."""
    probe = path / "CaseProbe"
    probe.write_text("")
    try:
        return not (path / "caseprobe").exists()
    finally:
        probe.unlink()


KITS = [f"kit{i:02d}" for i in range(20)]


class TestUnlistedFrameworks:
    def test_counted_on_run_1_then_removed_on_run_2(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """technologies.json misses 3 of 20 frameworks (15%)."""
        rendered = {"kit00": {"version": 0}}  # metadata.render, kept as it is by the count's write
        for kit in KITS:
            make_framework(kit, **({"render": rendered[kit]} if kit in rendered else {}))
        dropped, listed = KITS[:3], KITS[3:]
        before = snapshot()
        # The scrape's list guard alone would stop the run: 17 of 20 is below 90%
        with pytest.raises(ScrapeAborted):
            check_framework_list(frameworks(listed))

        # Run 1: counted, nothing deleted; only their hash files change, by the count alone
        capsys.readouterr()
        assert prescrape(monkeypatch, listed) == 0
        after = snapshot()
        assert set(after) == set(before)
        assert {path for path in after if after[path] != before[path]} == {
            str(Config.get_hash_file(kit)) for kit in dropped
        }
        for kit in dropped:
            data = json.loads(after[str(Config.get_hash_file(kit))])
            assert data["metadata"].pop("unlisted_runs") == 1
            assert data["metadata"].get("render") == rendered.get(kit), kit  # present stays, absent stays absent
            assert data == json.loads(before[str(Config.get_hash_file(kit))])
        out = capsys.readouterr().out
        assert "removed if still unlisted on the next run: kit00 (run 1), kit01 (run 1), kit02 (run 1)" in out
        assert "Removed" not in out
        # The list guard leaves them out now, so the scrape runs
        check_framework_list(frameworks(listed))
        assert [f.unlisted_runs for f in framework_hash_files(Config.CACHE_DIR).frameworks] == [1] * 3 + [0] * 17

        # Run 2: still unlisted, removed (docs dir and hash file); nothing else changes
        assert prescrape(monkeypatch, listed) == 0
        for kit in dropped:
            assert not on_disk(kit)
        assert snapshot() == {
            path: data for path, data in after.items()
            if not any(f"/{kit}/" in path or path.endswith(f"/{kit}_hashes.json") for kit in dropped)
        }
        assert ("Removed 3 frameworks technologies.json hasn't listed on 2 consecutive runs "
                "(docs dir and hash file): kit00 (2 files), kit01 (2 files), kit02 (2 files)") in capsys.readouterr().out

        # Run 3: nothing left to do
        assert prescrape(monkeypatch, listed) == 0
        assert "✅ No removed frameworks detected" in capsys.readouterr().out

    def test_many_frameworks_dropped_at_once_are_removed_like_one(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        """No count guard, candidate guard or cap: 12 of 20 dropped are all removed on run 2."""
        for kit in KITS:
            make_framework(kit)
        listed = KITS[12:]
        assert prescrape(monkeypatch, listed) == 0
        assert all(on_disk(kit) for kit in KITS)
        assert prescrape(monkeypatch, listed) == 0
        assert [kit for kit in KITS if on_disk(kit)] == listed
        check_framework_list(frameworks(listed))  # the scrape runs: no stale hash file counts

    def test_listed_again_starts_over(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                      capsys: pytest.CaptureFixture[str]) -> None:
        make_framework("kit00")
        make_framework("kit01")
        original = Config.get_hash_file("kit00").read_bytes()
        assert prescrape(monkeypatch, ["kit01"]) == 0
        assert saved("kit00")["metadata"]["unlisted_runs"] == 1
        # Listed again: the count is dropped, and the file is as it was
        capsys.readouterr()
        assert prescrape(monkeypatch, ["kit00", "kit01"]) == 0
        assert Config.get_hash_file("kit00").read_bytes() == original
        assert "Listed again, unlisted_runs reset: kit00" in capsys.readouterr().out
        # Unlisted once more: run 1 again, not a removal
        assert prescrape(monkeypatch, ["kit01"]) == 0
        assert saved("kit00")["metadata"]["unlisted_runs"] == 1 and on_disk("kit00")

    async def test_the_scrape_resets_the_count(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        """A pre-scrape whose fetch failed resets nothing: the scrape's save of a listed framework does.

        Otherwise the stale 1 left on a framework the scrape found listed
        would make a single later unlisted run delete it.
        """
        await seeded(runs)
        make_framework("otherkit")
        assert await asyncio.to_thread(prescrape, monkeypatch, ["otherkit"]) == 0
        assert saved(FW)["metadata"]["unlisted_runs"] == 1
        # The next run: the pre-scrape's fetch fails, the scrape's succeeds and lists testkit
        assert await asyncio.to_thread(prescrape, monkeypatch, []) == 1
        assert saved(FW)["metadata"]["unlisted_runs"] == 1
        scraper = await runs.run(routes_for(SITE))
        assert not scraper.outcome.blocked
        assert "unlisted_runs" not in saved(FW)["metadata"]
        # Unlisted on the run after: run 1 again, so it is kept
        assert await asyncio.to_thread(prescrape, monkeypatch, ["otherkit"]) == 0
        assert saved(FW)["metadata"]["unlisted_runs"] == 1
        assert all(file_of(path).exists() for path in SITE)

    @pytest.mark.parametrize("fetch", ["empty-list", "http-500", "invalid-json", "no-references"])
    def test_a_failed_or_empty_fetch_counts_nothing(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str], fetch: str
    ) -> None:
        """Our failure: no count, no reset, nothing deleted (not even a framework due at 2), exit 1."""
        make_framework("kit00", unlisted_runs=1)  # unlisted last run: due for removal
        make_framework("kit01", unlisted_runs=1)  # would be reset if listed
        make_framework("kit02")
        before = snapshot()
        if fetch == "empty-list":
            code = prescrape(monkeypatch, [])
        else:
            def handler(request: httpx.Request) -> httpx.Response:
                if fetch == "http-500":
                    return httpx.Response(500, text="error", request=request)
                if fetch == "invalid-json":
                    return httpx.Response(200, text="<html>", request=request)
                return httpx.Response(200, json={"sections": []}, request=request)

            requests = serve_technologies(monkeypatch, handler)
            code = prescrape(monkeypatch, None)
            assert requests == [framework_list_scraper.AppleFrameworkListScraper.TECHNOLOGIES_URL]
        assert code == 1
        assert snapshot() == before
        assert "technologies.json couldn't be fetched, or listed no frameworks" in capsys.readouterr().out

    def test_the_shared_parser_and_no_other_request(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        """technologies.json's references, top-level only (the scrape's parser), is the only request."""
        for kit in ("kit00", "kit01", "technologies"):
            make_framework(kit)
        references = {
            f"doc://com.apple.documentation/documentation/{fw}": {"url": f"/documentation/{fw}", "title": fw, "type": "topic"}
            for fw in ("kit00", "technologies")
        }
        # A sub-path is no framework: kit01 isn't listed through it
        references["doc://com.apple.documentation/documentation/kit00/kit01"] = {
            "url": "/documentation/kit00/kit01", "title": "kit01", "type": "topic"}
        requests = serve_technologies(
            monkeypatch, lambda request: httpx.Response(200, json={"references": references}, request=request)
        )
        assert prescrape(monkeypatch, None) == 0
        assert requests == [framework_list_scraper.AppleFrameworkListScraper.TECHNOLOGIES_URL]
        assert [f.framework_id for f in framework_hash_files(Config.CACHE_DIR).frameworks if f.unlisted_runs] == ["kit01"]

    def test_modules_namespaces_and_other_scrapers_files_are_never_judged(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        make_framework("kit00")
        make_framework("modkit", module={"parent": "kit00"})  # a D6 module's file
        make_framework("nskit", hash_file=Config.CACHE_DIR / "ns" / "nskit_hashes.json")  # .hashes/<namespace>/
        hig = Config.OUTPUT_DIR / "HIG" / "buttons.md"
        hig.parent.mkdir(parents=True)
        hig.write_text("# Buttons\n")
        other_files = {
            "hig_docs": {"https://developer.apple.com/tutorials/data/design/human-interface-guidelines/buttons.json":
                         {"hash": "h", "file_path": str(hig)}},
            "mlx_docs": {"metadata": {"source": "mlx"}, "hashes": {"MLX:https://ml-explore.github.io/mlx/x.html": "d"}},
            "swift_docs": {"metadata": {}, "hashes": {"swiftlang/swift-book:TSPL.docc/A.md": "d"}},
            "meilisearch": {"StoreKit/a.md": "d"},
        }
        for name, data in other_files.items():
            (Config.CACHE_DIR / f"{name}_hashes.json").write_text(json.dumps(data))
        before = snapshot()
        for run in (1, 2, 3):
            assert prescrape(monkeypatch, ["kit00"]) == 0
            assert snapshot() == before, run
        assert [f.framework_id for f in framework_hash_files(Config.CACHE_DIR).frameworks] == ["kit00"]
        check_framework_list(frameworks(["kit00"]))  # 1 of 1

    def test_matching_is_case_insensitive(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        """Apple flips a framework's URL casing: a listed framework in any casing is listed."""
        make_framework("CryptoKit")
        make_framework("visionkit")
        before = snapshot()
        for listed in (["cryptokit", "VisionKit"], ["CRYPTOKIT", "visionkit"]):
            assert prescrape(monkeypatch, listed) == 0
            assert snapshot() == before

    def test_a_removal_takes_every_casing_of_the_docs_dir(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        make_framework("CryptoKit", docs_dir="cryptokit")  # docs in another casing than the hash file
        make_framework("kit00")
        if case_sensitive(Config.OUTPUT_DIR):
            (Config.OUTPUT_DIR / "CryptoKit").mkdir()
            (Config.OUTPUT_DIR / "CryptoKit" / "page.md").write_text("# page\n")
        for run in (1, 2):
            assert prescrape(monkeypatch, ["kit00"]) == 0
            assert on_disk("CryptoKit", docs_dir="cryptokit") is (run == 1)
        assert sorted(p.name for p in Config.OUTPUT_DIR.iterdir()) == ["kit00"]
        assert sorted(p.name for p in Config.CACHE_DIR.iterdir()) == ["kit00_hashes.json"]

    def test_an_unlisted_framework_whose_hash_file_cant_be_read_is_still_removed(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Its docs dir makes it the framework's: run 1 counts (exit 1) and replaces the file, run 2 removes.

        The count is lost with the file, so the removal waits one run at
        most; it never waits for good, keeping the docs dir in the corpus and
        exiting 1 on every run.
        """
        make_framework("kit00")
        broken = make_framework("BrokenKit", docs_dir="brokenkit")  # docs in another casing, as Apple flips it
        broken.write_text(broken.read_text()[:100])  # cut off mid-JSON
        before = snapshot()
        [unreadable] = [f for f in framework_hash_files(Config.CACHE_DIR).frameworks if f.load_error]
        assert (unreadable.framework_id, unreadable.unlisted_runs) == ("BrokenKit", 0)
        with pytest.raises(ScrapeAborted):  # it counts in the list guard like any framework hash file
            check_framework_list(frameworks(["kit00"]))

        # A dry run changes nothing, but says what a run would do
        capsys.readouterr()
        assert prescrape(monkeypatch, ["kit00"], ["--dry-run"]) == 1
        assert snapshot() == before
        assert "the file would be replaced by one holding that count" in capsys.readouterr().out

        # Run 1: an error of ours (exit 1); counted, and only the unreadable file changes
        assert prescrape(monkeypatch, ["kit00"]) == 1
        after = snapshot()
        assert {path for path in after if after.get(path) != before.get(path)} == {str(broken)}
        data = json.loads(broken.read_text())
        assert data["hashes"] == {} and data["metadata"]["unlisted_runs"] == 1
        out = capsys.readouterr().out
        assert f"{broken} can't be read (" in out
        assert ("its unlisted_runs is lost, so this run counts as run 1, "
                "and the file is replaced by one holding that count") in out
        assert "removed if still unlisted on the next run: BrokenKit (run 1)" in out
        check_framework_list(frameworks(["kit00"]))  # left out of the list guard now, like any counted one

        # Run 2: still unlisted, removed (every casing of its docs dir, and its hash file)
        assert prescrape(monkeypatch, ["kit00"]) == 0
        assert not on_disk("BrokenKit", docs_dir="brokenkit")
        assert sorted(p.name for p in Config.OUTPUT_DIR.iterdir()) == ["kit00"]
        assert sorted(p.name for p in Config.CACHE_DIR.iterdir()) == ["kit00_hashes.json"]
        assert "Removed 1 frameworks" in capsys.readouterr().out

    def test_a_replaced_hash_file_listed_again_starts_over(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        """Listed again, the count is dropped; the file holds no entries yet, but is still judged by its docs dir."""
        make_framework("kit00")
        broken = make_framework("kit01")
        broken.write_text("{")
        assert prescrape(monkeypatch, ["kit00"]) == 1
        assert saved("kit01")["metadata"]["unlisted_runs"] == 1
        assert prescrape(monkeypatch, ["kit00", "kit01"]) == 0
        data = saved("kit01")
        assert data["hashes"] == {} and set(data["metadata"]) == {"total_pages"}
        assert [(f.framework_id, f.unlisted_runs) for f in framework_hash_files(Config.CACHE_DIR).frameworks] == [
            ("kit00", 0), ("kit01", 0)]
        # Unlisted once more: run 1 again, then removed on run 2
        assert prescrape(monkeypatch, ["kit00"]) == 0
        assert saved("kit01")["metadata"]["unlisted_runs"] == 1 and on_disk("kit01")
        assert prescrape(monkeypatch, ["kit00"]) == 0
        assert not on_disk("kit01") and on_disk("kit00")

    async def test_the_scrape_fills_a_replaced_hash_file(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        """Listed on the scrape's run, its save writes every page's entry back and drops the count."""
        await seeded(runs)
        make_framework("otherkit")
        Config.get_hash_file(FW).write_text(Config.get_hash_file(FW).read_text()[:50])
        assert await asyncio.to_thread(prescrape, monkeypatch, ["otherkit"]) == 1
        assert saved(FW)["metadata"]["unlisted_runs"] == 1 and saved(FW)["hashes"] == {}
        # The pre-scrape's fetch fails on the next run (no reset), the scrape's lists testkit
        assert await asyncio.to_thread(prescrape, monkeypatch, []) == 1
        scraper = await runs.run(routes_for(SITE))
        assert not scraper.outcome.blocked
        assert "unlisted_runs" not in saved(FW)["metadata"]
        assert {json_url(path) for path in SITE} <= set(saved(FW)["hashes"])
        assert all(file_of(path).exists() for path in SITE)
        # Unlisted on the run after: run 1, kept
        assert await asyncio.to_thread(prescrape, monkeypatch, ["otherkit"]) == 0
        assert saved(FW)["metadata"]["unlisted_runs"] == 1
        assert all(file_of(path).exists() for path in SITE)

    def test_an_unreadable_hash_file_of_a_listed_framework_is_left_to_the_scrape(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """The scrape replaces it (hash_load_failed blocks that framework's cleanup once)."""
        make_framework("kit00")
        broken = make_framework("kit01")
        broken.write_text(broken.read_text()[:100])
        before = snapshot()
        for run in (1, 2):
            assert prescrape(monkeypatch, ["kit00", "KIT01"]) == 0
            assert snapshot() == before, run

    def test_an_unreadable_module_hash_file_its_parent_lists_is_never_judged(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """A D6 module's file its parent lists in child_modules: never counted as unlisted (its next save
        replaces it); unlisted ×2 would delete a module its parent still links."""
        make_framework("kit00", child_modules={"modkit": {}})
        broken = make_framework("ModKit", module={"parents": {"kit00": {"unlinked_clean_runs": 0}}})
        broken.write_text(broken.read_text()[:100])
        before = snapshot()
        assert [f.framework_id for f in framework_hash_files(Config.CACHE_DIR).frameworks] == ["kit00"]
        assert framework_hash_files(Config.CACHE_DIR).unreadable == {}
        check_framework_list(frameworks(["kit00"]))  # 1 of 1
        for run in (1, 2, 3):
            assert prescrape(monkeypatch, ["kit00"]) == 0
            assert snapshot() == before, run
        # Without its parent's listing it is judged by its docs dir, as before
        parent = json.loads(Config.get_hash_file("kit00").read_text())
        del parent["metadata"]["child_modules"]
        Config.get_hash_file("kit00").write_text(json.dumps(parent))
        assert [f.framework_id for f in framework_hash_files(Config.CACHE_DIR).frameworks] == ["ModKit", "kit00"]

    @pytest.mark.parametrize("listed", [False, True])
    def test_an_unreadable_hash_file_with_no_docs_dir_is_never_touched(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str], listed: bool
    ) -> None:
        """Another scraper's state file looks the same (its scraper replaces it); no doc depends on it.

        Unlisted: an error every run while it can't be read. Listed: left to the scrape.
        """
        make_framework("kit00")
        (Config.OUTPUT_DIR / "MLX").mkdir()
        (Config.OUTPUT_DIR / "MLX" / "index.md").write_text("# MLX\n")
        broken = Config.CACHE_DIR / "mlx_docs_hashes.json"
        broken.write_text('{"metadata": {"source": "mlx"}, "hashes": {"MLX:https://ml-explore.git')
        before = snapshot()
        for run in (1, 2):
            capsys.readouterr()
            assert prescrape(monkeypatch, ["kit00", "mlx_docs"] if listed else ["kit00"]) == (0 if listed else 1)
            assert snapshot() == before, run
            assert (f"{broken} can't be read and has no docs dir of its id, so it can't be judged"
                    in capsys.readouterr().out) is not listed
        assert [f.framework_id for f in framework_hash_files(Config.CACHE_DIR).frameworks] == ["kit00"]

    def test_dry_run_changes_nothing(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                     capsys: pytest.CaptureFixture[str]) -> None:
        make_framework("kit00", unlisted_runs=1)  # due for removal
        make_framework("kit01")  # newly unlisted
        make_framework("kit02", unlisted_runs=1)  # listed again
        before = snapshot()

        def no_prompt(prompt: str = "") -> str:
            raise AssertionError("a dry run asks nothing")

        monkeypatch.setattr("builtins.input", no_prompt)
        capsys.readouterr()
        assert prescrape(monkeypatch, ["kit02"], ["--dry-run"]) == 0
        assert snapshot() == before
        out = capsys.readouterr().out
        assert "[DRY RUN] Nothing is written or deleted" in out
        assert "Would remove 1 frameworks" in out and "kit00 (2 files)" in out
        assert "(would be counted in unlisted_runs)" in out and "kit01 (run 1)" in out
        assert "unlisted_runs would be reset: kit02" in out

    def test_interactive_asks_once_and_a_no_keeps_the_count(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        make_framework("kit00", unlisted_runs=1)
        make_framework("kit01", unlisted_runs=1)
        make_framework("kit02")
        answers = iter(["n", "y"])
        prompts: List[str] = []

        def answer(prompt: str = "") -> str:
            prompts.append(prompt)
            return next(answers)

        monkeypatch.setattr("builtins.input", answer)
        capsys.readouterr()
        assert prescrape(monkeypatch, ["kit02"], []) == 0
        assert len(prompts) == 1
        assert on_disk("kit00") and on_disk("kit01")
        assert saved("kit00")["metadata"]["unlisted_runs"] == UNLISTED_REMOVAL_RUNS
        assert "Not removed (declined); a later run removes them: kit00, kit01" in capsys.readouterr().out
        assert prescrape(monkeypatch, ["kit02"], []) == 0
        assert len(prompts) == 2
        assert not on_disk("kit00") and not on_disk("kit01") and on_disk("kit02")

    @pytest.mark.skipif(hasattr(os, "geteuid") and os.geteuid() == 0, reason="root ignores file permissions")
    def test_a_failed_count_write_is_an_error(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                              capsys: pytest.CaptureFixture[str]) -> None:
        make_framework("kit00")
        make_framework("kit01")
        before = snapshot()
        Config.CACHE_DIR.chmod(0o555)
        try:
            capsys.readouterr()
            assert prescrape(monkeypatch, ["kit01"]) == 1
        finally:
            Config.CACHE_DIR.chmod(0o755)
        assert snapshot() == before
        assert f"kit00: hash file save failed ({Config.get_hash_file('kit00')})" in capsys.readouterr().out
        # Not counted: the next run is run 1 again
        assert prescrape(monkeypatch, ["kit01"]) == 0
        assert saved("kit00")["metadata"]["unlisted_runs"] == 1

    @pytest.mark.skipif(hasattr(os, "geteuid") and os.geteuid() == 0, reason="root ignores file permissions")
    def test_a_failed_removal_is_an_error_and_retried(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                                      capsys: pytest.CaptureFixture[str]) -> None:
        make_framework("kit00", unlisted_runs=1)
        make_framework("kit01")
        Config.OUTPUT_DIR.chmod(0o555)  # the docs dir can't be removed from it
        try:
            capsys.readouterr()
            assert prescrape(monkeypatch, ["kit01"]) == 1
        finally:
            Config.OUTPUT_DIR.chmod(0o755)
        assert "kit00: removal failed" in capsys.readouterr().out
        assert Config.get_hash_file("kit00").exists()  # the dir goes first, so the count survives
        assert prescrape(monkeypatch, ["kit01"]) == 0
        assert not on_disk("kit00") and on_disk("kit01")


def serve_technologies(monkeypatch: pytest.MonkeyPatch,
                       handler: Callable[[httpx.Request], httpx.Response]) -> List[str]:
    """Serve the list scraper's requests from handler (the real parser); returns the requested URLs."""
    requests: List[str] = []
    real_client = httpx.AsyncClient

    def record(request: httpx.Request) -> httpx.Response:
        requests.append(str(request.url))
        return handler(request)

    def client(*args: Any, **kwargs: Any) -> httpx.AsyncClient:
        return real_client(*args, transport=httpx.MockTransport(record), **kwargs)

    monkeypatch.setattr(framework_list_scraper.httpx, "AsyncClient", client)
    return requests


class TestListGuard:
    """The scrape's guard against a failed or short technologies.json fetch (exit 2)."""

    def test_an_empty_list_aborts_even_with_no_hash_files(self, runs: Runs) -> None:
        with pytest.raises(ScrapeAborted, match="listed 0 frameworks"):
            check_framework_list([])

    def test_below_90_percent_of_the_framework_hash_files_aborts(self, runs: Runs) -> None:
        for kit in KITS[:10]:
            make_framework(kit)
        check_framework_list(frameworks(KITS[:9]))
        with pytest.raises(ScrapeAborted, match="listed 8 frameworks, below 90% of the 10 Apple framework hash files"):
            check_framework_list(frameworks(KITS[:8]))

    def test_frameworks_already_unlisted_dont_count(self, runs: Runs) -> None:
        """2.5 is already removing them, so a real removal of many frameworks never stops the scrape."""
        for kit in KITS[:6]:
            make_framework(kit)
        for kit in KITS[6:10]:
            make_framework(kit, unlisted_runs=1)
        check_framework_list(frameworks(KITS[:6]))
        with pytest.raises(ScrapeAborted, match="of the 6 Apple framework hash files"):
            check_framework_list(frameworks(KITS[:5]))

    async def test_a_short_list_scrapes_and_cleans_nothing(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """scrape.py --all: exit 2 before any scrape or cleanup; once 2.5 counted the missing ones, it runs."""
        await seeded(runs)
        for kit in ("otherkit", "thirdkit"):
            make_framework(kit)
        stray = Config.OUTPUT_DIR / FW / "stray.md"
        stray.write_text("# stray\n")
        before = snapshot()
        apple = Apple(routes_for(SITE))

        class MockedScraper(AppleJSONDocumentationScraper):
            async def __aenter__(self) -> "MockedScraper":
                self.session = httpx.AsyncClient(transport=httpx.MockTransport(apple), follow_redirects=True)
                return self

        monkeypatch.setattr(scrape_all_frameworks, "AppleJSONDocumentationScraper", MockedScraper)
        monkeypatch.setattr(scrape_all_frameworks, "AppleFrameworkListScraper", listing([FW]))
        ci = ["scrape.py", "--all", "--yes", "--cleanup-orphans", "--auto-cleanup"]
        monkeypatch.setattr(sys, "argv", ci)
        capsys.readouterr()
        assert await scrape_all_frameworks.scrape_everything() == 2
        assert snapshot() == before
        assert ("technologies.json listed 1 frameworks, below 90% of the 3 Apple framework hash files here "
                "(not counting those already unlisted): a failed or short fetch. Nothing scraped.") in capsys.readouterr().out

        # The pre-scrape counts otherkit and thirdkit: the scrape runs, and cleans testkit
        assert await asyncio.to_thread(prescrape, monkeypatch, [FW]) == 0
        monkeypatch.setattr(sys, "argv", ci)
        assert await scrape_all_frameworks.scrape_everything() == 0
        assert not stray.exists()
        assert on_disk("otherkit") and on_disk("thirdkit")
