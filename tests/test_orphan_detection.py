#!/usr/bin/env python3
"""
Test orphan detection and the end-of-run orphan cleanup.

- Detection: the files no entry the run touched records (the in-memory
  touched set), with case-insensitive path matching.
- The mass-removal valve and confirm-then-delete (pending_orphans).
- delete_orphans, the one deletion path: empty dirs, pruning that keeps the
  metadata, interactive approval, whole-framework removal.
- scrape.py's end-of-run cleanup over consecutive framework runs (the
  test_failure_policy harness): results-based, the zero-touched guard, the
  root-gone x2 removal and the run summary.
"""

import gc
import json
import os
import sys
import weakref
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Type

import httpx
import pytest
from structlog.testing import capture_logs

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts', 'utilities')))

import scrape_all_frameworks
from cleanup_orphans_at_end import FrameworkCleanup, delete_orphans, plan_cleanup
from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper, OrphanScan
from scraper.utils.hash_manager import HashManager, valve_trips
from tests.test_failure_policy import (
    FW, ROOT, SITE, Apple, FrameworkList, Runs, Site, file_of, routes_for, sandbox_runs, seeded,
)
from tests.test_fetch_results import json_url, status


def case_sensitive(path: Path) -> bool:
    """Whether the filesystem holding path tells names apart by case."""
    probe = path / "CaseProbe"
    probe.write_text("")
    try:
        return not (path / "caseprobe").exists()
    finally:
        probe.unlink()


def write(path: Path, text: str = "# page\n") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


# --- Detection -------------------------------------------------------------


def test_every_touch_site_keeps_its_file(tmp_path: Path) -> None:
    """update_hash, touch and keep_file touch; an entry an error replaced after its touch records no file."""
    hash_file = tmp_path / "fw_hashes.json"
    docs = tmp_path / "docs"
    files = {name: write(docs / f"{name}.md") for name in ("updated", "touched", "kept", "d8", "unrecorded")}
    old = HashManager(hash_file)
    for name in ("updated", "touched", "d8"):
        old.update_hash(name, name, "E", files[name])
    old.save()

    hm = HashManager(hash_file)
    hm.update_hash("updated", "new content", "E2", files["updated"])
    hm.touch("touched")
    hm.mark_error("kept", "local error: x")
    assert hm.keep_file("kept", files["kept"])
    hm.touch("d8")
    hm.mark_error("d8", "HTTP 502")  # D8 at its third failed run
    assert hm.touched == {"updated", "touched", "kept", "d8"}
    assert hm.get_untouched_files(docs) == [files["d8"], files["unrecorded"]]


def test_a_recorded_path_in_another_casing_keeps_its_file(tmp_path: Path) -> None:
    """Matched by name against the listing, never by stat (on macOS a stat finds any casing)."""
    hash_file = tmp_path / "fw_hashes.json"
    docs = tmp_path / "docs"
    page = write(docs / "Page.md")
    hm = HashManager(hash_file)
    hm.update_hash("u", "content", None, docs / "page.md")
    assert hm.get_untouched_files(docs) == []
    assert page.exists()

    if case_sensitive(tmp_path):
        # Two files that differ only in case (Linux): the exact match is kept,
        # the other is an orphan; a path matching neither exactly keeps both
        other = write(docs / "page.md")
        assert hm.get_untouched_files(docs) == [page]
        hm2 = HashManager(hash_file)
        hm2.update_hash("u", "content", None, docs / "PAGE.md")
        assert hm2.get_untouched_files(docs) == []
        assert other.exists()


def test_a_fresh_manager_touched_nothing(tmp_path: Path) -> None:
    """Valid only in the process that scraped: a later manager sees every file untouched."""
    hash_file = tmp_path / "fw_hashes.json"
    page = write(tmp_path / "docs" / "page.md")
    hm = HashManager(hash_file)
    hm.update_hash("u", "content", None, page)
    hm.save()
    later = HashManager(hash_file)
    assert later.touched == set()
    assert later.get_untouched_files(page.parent) == [page]


# --- The valve and confirm-then-delete --------------------------------------


@pytest.mark.parametrize("orphans, files, trips", [
    (0, 0, False), (0, 10, False),
    (5, 12, False), (6, 12, True),  # exactly half trips (the old strict > let 6 of 12 through)
    (5, 10, True), (4, 10, False), (1, 1, True), (1, 2, True), (1, 3, False),
    (1000, 100_000, False), (1001, 100_000, True),
])
def test_the_valve_trips_at_half_or_over_1000(orphans: int, files: int, trips: bool) -> None:
    assert valve_trips(orphans, files) is trips


def scan(files: int, orphans: List[str], pending: Optional[List[str]] = None) -> OrphanScan:
    return OrphanScan(
        framework_dir=Path("documentation/fw"),
        hash_file=Path(".hashes/fw_hashes.json"),
        files=files,
        orphans=[Path(f"documentation/fw/{name}.md") for name in orphans],
        pending_orphans=[f"documentation/fw/{name}.md" for name in (pending or [])],
    )


def names(paths: List[Path]) -> List[str]:
    return [path.stem for path in paths]


@pytest.mark.parametrize("files, orphans, pending, delete, confirmed, held, new_pending", [
    # No pending_orphans: deleted below the valve; at the valve, held and kept
    (10, ["a"], None, ["a"], 0, 0, None),
    (10, ["a", "b", "c", "d", "e"], None, [], 0, 5, ["a", "b", "c", "d", "e"]),
    (10, [], None, [], 0, 0, None),
    # Confirmed: the held files are orphaned again, D = P ∩ O2 is deleted, P dropped
    (10, ["a", "b", "c", "d", "e"], ["a", "b", "c", "d", "e"], ["a", "b", "c", "d", "e"], 5, 0, []),
    # The remainder O2 − D is deleted too when it doesn't trip the valve on its own (1 of the 5 left)
    (10, ["a", "b", "c", "d", "e", "f"], ["a", "b", "c", "d", "e"], ["a", "b", "c", "d", "e", "f"], 5, 0, []),
    # A remainder that trips the valve itself (3 of the 5 left) waits, replacing P; D still goes
    (10, ["a", "b", "c", "d", "e", "f", "g", "h"], ["a", "b", "c", "d", "e"], ["a", "b", "c", "d", "e"], 5, 3,
     ["f", "g", "h"]),
    # A one-off glitch: nothing orphaned again, P dropped and nothing deleted
    (10, [], ["a", "b", "c", "d", "e"], [], 0, 0, []),
    # Partly confirmed: only the files orphaned again are deleted
    (10, ["a", "b"], ["a", "b", "c", "d", "e"], ["a", "b"], 2, 0, []),
    # A different mass of candidates: none confirmed, the new set replaces P
    (10, ["v", "w", "x", "y", "z"], ["a", "b", "c", "d", "e"], [], 0, 5, ["v", "w", "x", "y", "z"]),
])
def test_confirm_then_delete(
    files: int, orphans: List[str], pending: Optional[List[str]], delete: List[str], confirmed: int, held: int,
    new_pending: Optional[List[str]],
) -> None:
    cleanup = plan_cleanup("fw", scan(files, orphans, pending))
    assert sorted(names(cleanup.delete)) == delete
    assert cleanup.confirmed == confirmed and cleanup.held == held
    expected = None if new_pending is None else [f"documentation/fw/{name}.md" for name in new_pending]
    assert cleanup.pending_orphans == expected


def test_pending_orphans_match_in_any_casing() -> None:
    held = OrphanScan(Path("documentation/fw"), Path(".hashes/fw_hashes.json"), 4,
                      [Path("documentation/fw/Sub/Page.md"), Path("documentation/fw/b.md")],
                      ["documentation/FW/sub/page.md", "documentation/fw/B.md"])
    cleanup = plan_cleanup("fw", held)
    assert cleanup.confirmed == 2 and cleanup.delete == held.orphans and cleanup.pending_orphans == []


# --- delete_orphans ---------------------------------------------------------


@pytest.fixture
def sandbox(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Path]:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(Config, "OUTPUT_DIR", Path("documentation"))
    monkeypatch.setattr(Config, "CACHE_DIR", Path(".hashes"))
    yield tmp_path


def framework_on_disk(pages: List[str]) -> HashManager:
    """A framework 'fw' whose hash file records each page."""
    hm = HashManager(Config.get_hash_file("fw"))
    for name in pages:
        hm.update_hash(name, name, "E", write(Config.get_framework_output_dir("fw") / f"{name}.md"))
    hm.set_metadata("failure_storm_runs", 1)
    hm.save()
    return hm


def test_delete_orphans_removes_emptied_dirs_and_prunes(sandbox: Path) -> None:
    hm = framework_on_disk(["root", "keep/one", "gone/deep/two", "gone/three"])
    fw_dir = Config.get_framework_output_dir("fw")
    orphans = [fw_dir / "gone/deep/two.md", fw_dir / "gone/three.md", fw_dir / "keep/one.md"]
    report = delete_orphans([FrameworkCleanup("fw", fw_dir, hm.cache_file, files=4, delete=orphans)], interactive=False)
    assert report.deleted == {"fw": 3} and report.pruned == 3 and report.failures == []
    # The dirs the deletions emptied are gone; the framework's dir stays
    assert sorted(str(p.relative_to(fw_dir)) for p in fw_dir.rglob("*")) == ["root.md"]
    saved = json.loads(hm.cache_file.read_text())
    assert set(saved["hashes"]) == {"root"}
    # The prune kept the metadata
    assert saved["metadata"]["failure_storm_runs"] == 1


def test_interactive_cleanup_asks_once(sandbox: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """On no: nothing deleted, the deleting framework's pending_orphans untouched; a hold-only one still writes."""
    hm = framework_on_disk(["root", "a", "b"])
    fw_dir = Config.get_framework_output_dir("fw")
    hm.set_metadata("pending_orphans", [str(fw_dir / "a.md")])
    hm.save()
    other = HashManager(Config.get_hash_file("other"))
    other.update_hash("x", "x", "E", write(Config.get_framework_output_dir("other") / "x.md"))
    other.save()
    cleanups = [
        FrameworkCleanup("fw", fw_dir, hm.cache_file, files=3, delete=[fw_dir / "a.md"], confirmed=1,
                         pending_orphans=[]),
        FrameworkCleanup("other", Config.get_framework_output_dir("other"), other.cache_file, files=1, held=1,
                         pending_orphans=["documentation/other/x.md"]),
    ]
    answers = iter(["n", "y"])
    prompts: List[str] = []

    def answer(prompt: str) -> str:
        prompts.append(prompt)
        return next(answers)

    monkeypatch.setattr("builtins.input", answer)
    report = delete_orphans(cleanups, interactive=True)
    assert len(prompts) == 1 and report.cancelled and report.deleted == {}
    assert (fw_dir / "a.md").exists()
    assert HashManager(hm.cache_file).get_metadata("pending_orphans") == [str(fw_dir / "a.md")]
    assert HashManager(other.cache_file).get_metadata("pending_orphans") == ["documentation/other/x.md"]
    assert report.held == {"other": (1, 1)}

    report = delete_orphans(cleanups, interactive=True)
    assert report.deleted == {"fw": 1} and not (fw_dir / "a.md").exists()
    assert HashManager(hm.cache_file).get_metadata("pending_orphans") is None


def test_removal_takes_every_casing_of_the_dir_and_hash_file(sandbox: Path) -> None:
    hm = framework_on_disk(["root", "sub/page"])
    fw_dir = Config.get_framework_output_dir("fw")
    renamed = fw_dir.with_name("FW")
    fw_dir.rename(renamed)
    hm.cache_file.rename(hm.cache_file.with_name("FW_hashes.json"))
    report = delete_orphans([FrameworkCleanup("fw", fw_dir, hm.cache_file, remove=True)], interactive=False)
    assert report.removed == {"fw": 2} and report.failures == []
    assert list(Path("documentation").iterdir()) == [] and list(Path(".hashes").iterdir()) == []

    if case_sensitive(sandbox):
        # Both casings side by side (Linux): all of them go
        for name in ("fw", "FW"):
            write(Path("documentation", name, "page.md"))
            write(Path(".hashes", f"{name}_hashes.json"), "{}")
        report = delete_orphans([FrameworkCleanup("fw", fw_dir, hm.cache_file, remove=True)], interactive=False)
        assert report.removed == {"fw": 2}
        assert list(Path("documentation").iterdir()) == [] and list(Path(".hashes").iterdir()) == []


# --- scrape.py's end-of-run cleanup, over consecutive runs -------------------


@pytest.fixture
def runs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Runs]:
    yield sandbox_runs(tmp_path, monkeypatch)


LEAVES = [f"{FW}/leaf{i}" for i in range(10)]
WIDE: Site = {ROOT: LEAVES, **{leaf: [] for leaf in LEAVES}}  # 11 files


def linking(*leaves: str) -> Site:
    """WIDE, with the root linking only these leaves (Apple stopped linking the rest)."""
    return {**WIDE, ROOT: list(leaves)}


def pending(fw: str = FW) -> Optional[List[str]]:
    value: Optional[List[str]] = Runs.saved(fw)["metadata"].get("pending_orphans")
    return value


def on_disk(*paths: str) -> List[bool]:
    return [file_of(path).exists() for path in paths]


async def test_a_mass_removal_is_held_then_confirmed_on_the_next_clean_run(
    runs: Runs, capsys: pytest.CaptureFixture[str]
) -> None:
    """60% of a framework unlinked: run 1 keeps pending_orphans and deletes nothing, run 2 deletes them."""
    await seeded(runs, WIDE)
    site = linking(*LEAVES[:4])  # 6 of 11 files unlinked
    scraper = await runs.run(routes_for(site))
    capsys.readouterr()
    report = runs.cleanup(scraper)
    out = capsys.readouterr().out
    assert report.deleted == {} and report.held == {FW: (6, 11)} and report.failures == []
    assert all(on_disk(*WIDE))
    # Written after the framework's own save, on a run that changed nothing else
    assert pending() == sorted(str(file_of(leaf)) for leaf in LEAVES[4:])
    assert f"   - {FW}: 6 of 11 files" in out and "pending_orphans set" in out
    assert "No orphaned files found" not in out

    scraper = await runs.run(routes_for(site))
    capsys.readouterr()
    report = runs.cleanup(scraper)
    out = capsys.readouterr().out
    assert report.deleted == {FW: 6} and report.confirmed == {FW: 6} and report.held == {}
    assert on_disk(*LEAVES[4:]) == [False] * 6 and all(on_disk(ROOT, *LEAVES[:4]))
    assert pending() is None
    assert all(json_url(leaf) not in runs.saved()["hashes"] for leaf in LEAVES[4:])
    assert f"Deleted 6 orphaned files in 1 frameworks: {FW} 6 (6 confirmed from pending_orphans)" in out
    # Nothing live looks orphaned
    assert runs.orphans() == set()


async def test_a_remainder_that_trips_the_valve_replaces_pending_orphans(runs: Runs) -> None:
    await seeded(runs, WIDE)
    runs.cleanup(await runs.run(routes_for(linking(*LEAVES[:4]))))
    assert pending() == sorted(str(file_of(leaf)) for leaf in LEAVES[4:])
    # Run 2: the 6 held are confirmed; 3 more are unlinked, 3 of the 5 files left: held themselves
    report = runs.cleanup(await runs.run(routes_for(linking(LEAVES[0]))))
    assert report.deleted == {FW: 6} and report.held == {FW: (3, 5)}
    assert pending() == sorted(str(file_of(leaf)) for leaf in LEAVES[1:4])
    assert all(on_disk(*LEAVES[1:4]))
    # Run 3 confirms those
    report = runs.cleanup(await runs.run(routes_for(linking(LEAVES[0]))))
    assert report.deleted == {FW: 3} and report.held == {} and pending() is None
    assert on_disk(ROOT, *LEAVES) == [True, True] + [False] * 9


async def test_a_one_off_glitch_drops_pending_orphans(runs: Runs) -> None:
    """Held on run 1, linked again on run 2: nothing deleted, and the list is dropped on a run that deletes nothing."""
    await seeded(runs, WIDE)
    runs.cleanup(await runs.run(routes_for(linking(*LEAVES[:4]))))
    assert pending() is not None
    report = runs.cleanup(await runs.run(routes_for(WIDE)))
    assert report.deleted == {} and report.held == {} and pending() is None
    assert all(on_disk(*WIDE))


async def test_a_blocked_or_unscraped_run_leaves_pending_orphans_untouched(runs: Runs) -> None:
    await seeded(runs, WIDE)
    other: Site = {"otherkit": ["otherkit/one"], "otherkit/one": []}
    await runs.run(routes_for(other), fw="otherkit")
    site = linking(*LEAVES[:4])
    runs.cleanup(await runs.run(routes_for(site)))
    held = pending()
    assert held is not None
    hash_file = Config.get_hash_file(FW)

    # Blocked: a page's 502 (our failed request) keeps everything, P included
    report = runs.cleanup(await runs.run(routes_for(site, {LEAVES[0]: [status(502)]})))
    assert report.deleted == {} and pending() == held and all(on_disk(*WIDE))
    # Unscraped this run: only otherkit is scraped, testkit's hash file isn't even read
    before = hash_file.read_text()
    report = runs.cleanup(await runs.run(routes_for(other), fw="otherkit"))
    assert report.deleted == {} and hash_file.read_text() == before
    # The next clean run confirms
    report = runs.cleanup(await runs.run(routes_for(site)))
    assert report.deleted == {FW: 6} and pending() is None


async def test_root_gone_twice_removes_the_framework(runs: Runs, capsys: pytest.CaptureFixture[str]) -> None:
    await seeded(runs)
    gone = routes_for(SITE, {ROOT: [status(404)]})
    scraper = await runs.run(gone)
    report = runs.cleanup(scraper)
    assert not scraper.outcome.blocked and scraper.outcome.root_gone_runs == 1
    assert scraper.outcome.orphan_scan is None
    assert report.deleted == {} and report.removed == {}
    assert all(on_disk(*SITE)) and "pending_orphans" not in runs.saved()["metadata"]
    assert f"(removed if it does again next run): {FW} (run 1)" in capsys.readouterr().out

    # Run 2: the dir and the hash file go, bypassing the valve (100% of the files); not an error
    scraper = await runs.run(gone)
    report = runs.cleanup(scraper)
    assert not scraper.outcome.blocked and scraper.outcome.root_gone_runs == 2
    assert report.removed == {FW: 5} and report.failures == []
    assert not Path("documentation", FW).exists() and not Config.get_hash_file(FW).exists()
    assert f"Removed 1 frameworks whose root returned 404/410 on 2 runs (docs dir and hash file): {FW} (5 files)" \
        in capsys.readouterr().out

    # Still listed, still gone, on every later run: nothing is written again, and
    # the summary doesn't announce a removal that can't come (the count stays at 1)
    for _ in range(2):
        scraper = await runs.run(gone)
        report = runs.cleanup(scraper)
        out = capsys.readouterr().out
        assert scraper.outcome.root_gone_runs == 1 and report.removed == {}
        assert not Path("documentation", FW).exists() and not Config.get_hash_file(FW).exists()
        assert "removed if it does again next run" not in out
        assert f"with no docs dir or hash file left to remove: {FW}" in out
        assert "No orphaned files found!" in out


async def test_root_gone_removal_after_a_lost_hash_file_in_another_casing(
    runs: Runs, capsys: pytest.CaptureFixture[str]
) -> None:
    """The docs dir is TestKit while the run's id is testkit (no hash file to adopt its casing from)."""
    await seeded(runs)
    Path("documentation", FW).rename(Path("documentation", "TestKit"))
    Config.get_hash_file(FW).unlink()
    gone = routes_for(SITE, {ROOT: [status(404)]})
    capsys.readouterr()
    runs.cleanup(await runs.run(gone))
    assert runs.saved()["metadata"]["root_gone_runs"] == 1
    # Only the docs dir was left: the count was saved, so the removal does come next run
    assert f"(removed if it does again next run): {FW} (run 1)" in capsys.readouterr().out
    report = runs.cleanup(await runs.run(gone))
    assert report.removed == {FW: 5}
    assert list(Path("documentation").iterdir()) == [] and list(Path(".hashes").iterdir()) == []


async def test_root_5xx_four_runs_deletes_nothing(runs: Runs) -> None:
    await seeded(runs)
    for _ in range(4):
        scraper = await runs.run(routes_for(SITE, {ROOT: [status(503)]}))
        report = runs.cleanup(scraper)
        assert scraper.outcome.blocked and report.deleted == {} and report.removed == {}
        assert all(on_disk(*SITE))


async def test_a_zero_touched_framework_is_never_cleaned(runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
    """A touch-tracking bug: this run touched no entry (here every page answers 304)."""
    await seeded(runs)
    monkeypatch.setattr(HashManager, "touch", lambda self, url: None)
    scraper = await runs.run(routes_for(SITE))
    saved_before = Runs.saved()
    with capture_logs() as events:
        report = runs.cleanup(scraper)
    assert scraper.outcome.blocks == {"zero_touched": [FW]} and scraper.outcome.blocked
    assert scraper.outcome.orphan_scan is None
    assert [e["event"] for e in events if e["event"] == "framework_zero_touched"] == ["framework_zero_touched"]
    assert report.deleted == {} and report.held == {} and all(on_disk(*SITE))
    assert Runs.saved() == saved_before  # no pending_orphans written


def mocked(apple: Apple) -> Type[AppleJSONDocumentationScraper]:
    class MockedScraper(AppleJSONDocumentationScraper):
        async def __aenter__(self) -> "MockedScraper":
            self.session = httpx.AsyncClient(transport=httpx.MockTransport(apple), follow_redirects=True)
            return self

    return MockedScraper


async def test_scrape_py_holds_then_confirms(
    runs: Runs, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """scrape.py --frameworks testkit --yes --cleanup-orphans --auto-cleanup, twice: the summary names the hold."""
    await seeded(runs, WIDE)
    monkeypatch.setattr(scrape_all_frameworks, "AppleFrameworkListScraper", FrameworkList)
    monkeypatch.setattr(sys, "argv", ["scrape.py", "--frameworks", FW, "--yes", "--cleanup-orphans", "--auto-cleanup"])
    site = linking(*LEAVES[:4])
    for run in (1, 2):
        monkeypatch.setattr(scrape_all_frameworks, "AppleJSONDocumentationScraper", mocked(Apple(routes_for(site))))
        capsys.readouterr()
        await scrape_all_frameworks.scrape_everything()
        out = capsys.readouterr().out
        if run == 1:
            assert f"   - {FW}: 6 of 11 files" in out and "No orphaned files found" not in out
            assert all(on_disk(*WIDE))
        else:
            assert f"{FW} 6 (6 confirmed from pending_orphans)" in out
            assert on_disk(*LEAVES[4:]) == [False] * 6


async def test_finished_frameworks_drop_their_hash_managers(runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
    """Results-based cleanup: once scraped, a framework's scraper and hash manager are freed."""
    kits = [f"kit{i}" for i in range(6)]
    routes: Dict[str, Any] = {}
    for kit in kits:
        site: Site = {kit: [f"{kit}/a", f"{kit}/b"], f"{kit}/a": [], f"{kit}/b": []}
        routes.update(routes_for(site))
    managers: "weakref.WeakSet[HashManager]" = weakref.WeakSet()
    created: List[Path] = []
    real_init = HashManager.__init__

    def init(self: HashManager, *args: Any, **kwargs: Any) -> None:
        real_init(self, *args, **kwargs)
        managers.add(self)
        created.append(self.cache_file)

    monkeypatch.setattr(HashManager, "__init__", init)
    monkeypatch.setattr(scrape_all_frameworks, "AppleJSONDocumentationScraper", mocked(Apple(routes)))
    stats = await scrape_all_frameworks.scrape_frameworks(
        framework_list=[{"id": kit, "title": kit} for kit in kits], max_concurrent=2, cleanup_orphans=True
    )
    assert stats is not None
    outcomes = stats["framework_outcomes"]
    assert len(created) == len(kits)  # one per framework, none reloaded
    gc.collect()
    assert len(managers) == 0
    assert all(o.orphan_scan is not None and o.orphan_scan.files == 3 for o in outcomes)
