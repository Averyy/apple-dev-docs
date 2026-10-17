#!/usr/bin/env python3
"""The failure policy shared by the MLX, HIG and Swift scrapers (utilities/source_policy.py)."""

import asyncio
from pathlib import Path
from typing import List, Optional, Tuple

import pytest

import utilities.source_policy as source_policy
from fake_upstream import case_sensitive
from scraper.utils.hash_manager import HashManager
from scraper.utils.hash_manager import valve_trips as apple_valve_trips
from utilities.source_policy import (
    PERSISTENT_FAILURE_RUNS,
    FailureCounts,
    FetchFailed,
    KeptLocation,
    ScrapeRun,
    fetch_with_retry,
    has_file_named,
    status_failure,
    unmatched,
    valve_trips,
)

GONE = FetchFailed(status=404, error="HTTP 404", transient=False)
GONE_410 = FetchFailed(status=410, error="HTTP 410", transient=False)
SERVER = FetchFailed(status=502, error="HTTP 502", transient=True)
FORBIDDEN = FetchFailed(status=403, error="HTTP 403", transient=False)
TIMEOUT = FetchFailed(status=None, error="TimeoutError", transient=True)


def new_run(base: Path, metadata: Optional[dict] = None, load_error: Optional[str] = None) -> ScrapeRun:
    return ScrapeRun("Test", base, metadata or {}, load_error)


def write(base: Path, *paths: str) -> List[Path]:
    files = []
    for rel in paths:
        path = base / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rel)
        files.append(path)
    return files


# -- fetching ---------------------------------------------------------------

def test_status_failure() -> None:
    assert status_failure(404).gone and status_failure(410).gone
    assert not status_failure(404).transient and not status_failure(403).transient
    assert status_failure(500).transient and status_failure(429).transient and status_failure(505).transient
    assert not status_failure(500).gone


async def fake_attempts(responses: List[object], monkeypatch: pytest.MonkeyPatch) -> Tuple[object, int]:
    monkeypatch.setattr(source_policy, "RETRY_BASE_DELAY", 0)
    calls = 0

    async def attempt() -> Tuple[int, Optional[str], str]:
        nonlocal calls
        response = responses[calls]
        calls += 1
        if isinstance(response, BaseException):
            raise response
        assert isinstance(response, tuple)
        return response

    result = await fetch_with_retry(attempt, "http://x", (ConnectionError,))
    return result, calls


async def test_fetch_with_retry(monkeypatch: pytest.MonkeyPatch) -> None:
    assert await fake_attempts([(200, None, "ok")], monkeypatch) == ("ok", 1)
    assert await fake_attempts([(502, None, ""), (503, None, ""), (200, None, "ok")], monkeypatch) == ("ok", 3)
    assert await fake_attempts([ConnectionError("reset"), (200, None, "ok")], monkeypatch) == ("ok", 2)
    result, calls = await fake_attempts([(404, None, "")], monkeypatch)
    assert result == status_failure(404) and calls == 1  # not retried
    result, calls = await fake_attempts([(403, None, "")], monkeypatch)
    assert result == status_failure(403) and calls == 1
    result, calls = await fake_attempts([(502, None, "")] * 4, monkeypatch)
    assert result == status_failure(502) and calls == source_policy.MAX_ATTEMPTS
    result, calls = await fake_attempts([ConnectionError("reset")] * 4, monkeypatch)
    assert isinstance(result, FetchFailed) and result.status is None and result.transient


async def test_retry_after_is_honored_and_capped(monkeypatch: pytest.MonkeyPatch) -> None:
    sleeps: List[float] = []

    async def fake_sleep(delay: float) -> None:
        sleeps.append(delay)

    monkeypatch.setattr(asyncio, "sleep", fake_sleep)
    responses = iter([(429, "30", ""), (429, "9999", ""), (200, None, "ok")])

    async def attempt() -> Tuple[int, Optional[str], str]:
        return next(responses)

    assert await fetch_with_retry(attempt, "http://x", ()) == "ok"
    assert sleeps == [30.0, source_policy.RETRY_AFTER_CAP]


# -- counters ---------------------------------------------------------------

def test_failure_counts_keep_only_met_keys() -> None:
    stored = {"a": {"fail": 2}, "b": {"local": 1, "gone": 1}, "c": {"fail": 1}, "d": {"local": 2, "fail": 1},
              "e": {"local": 1, "fail": 1}, "f": {"local": 2}, "junk": {"fail": "x"}, "neg": {"fail": -1},
              "flag": {"fail": True}}
    counts = FailureCounts(stored)
    assert counts.get("a", "fail") == 2 and counts.get("junk", "fail") == 0
    assert counts.bump("a", "fail") == 3
    assert counts.bump("a", "fail") == 3  # once per run
    counts.reset("b", "local")
    assert counts.bump("new", "gone", cap=2) == 1
    assert counts.bump("e", "fail") == 2
    assert counts.bump("f", "local") == 3
    # c and d were not met this run: a fetch count is dropped, a local count
    # is kept while its page is present
    assert counts.to_metadata(kept=lambda key: False, present=lambda key: True) == {
        "a": {"fail": 3}, "b": {"gone": 1}, "d": {"local": 2}, "e": {"fail": 2, "local": 1}, "f": {"local": 3},
        "new": {"gone": 1}}
    # A local count goes with its page, unless the page failed locally this run
    assert counts.to_metadata(kept=lambda key: False, present=lambda key: False) == {
        "a": {"fail": 3}, "b": {"gone": 1}, "e": {"fail": 2}, "f": {"local": 3}, "new": {"gone": 1}}
    # Under a location this run kept, the page (and its file) wasn't reached:
    # its local count stays, while its fetch count ends as for any unmet key
    kept = counts.to_metadata(kept=lambda key: key in ("c", "d"), present=lambda key: False)
    assert "c" not in kept and kept["d"] == {"local": 2}


def test_gone_count_is_capped() -> None:
    counts = FailureCounts({"root": {"gone": 2}})
    assert counts.bump("root", "gone", cap=2) == 2


# -- page and source rules --------------------------------------------------

def test_page_rules(tmp_path: Path) -> None:
    run = new_run(tmp_path)
    assert run.page_failed("gone", GONE, previously_good=True) is False
    assert run.page_failed("gone410", GONE_410, previously_good=True) is False
    assert run.page_failed("new4xx", FORBIDDEN, previously_good=False) is False
    assert (run.blocked, run.exit_code()) == (False, 0)
    assert run.page_failed("good403", FORBIDDEN, previously_good=True) is True
    assert run.page_failed("new5xx", SERVER, previously_good=False) is False  # no file, but blocks
    assert run.page_failed("goodtimeout", TIMEOUT, previously_good=True) is True
    assert run.blocked and run.exit_code() == 1
    assert run.metadata(hash_keys=())["failure_counts"] == {"good403": {"fail": 1}, "goodtimeout": {"fail": 1},
                                                "new5xx": {"fail": 1}}


def test_d8_at_the_third_run(tmp_path: Path) -> None:
    run = new_run(tmp_path, {"failure_counts": {"good": {"fail": 2}, "new": {"fail": 2}, "gone": {"fail": 2}}})
    assert run.page_failed("good", SERVER, previously_good=True) is False  # treated as removed
    assert run.page_failed("new", SERVER, previously_good=False) is False
    assert run.page_failed("gone", GONE, previously_good=True) is False
    assert not run.blocked and run.exit_code() == 1  # persistent_fetch_failure x2
    assert run.metadata(hash_keys=())["failure_counts"] == {"good": {"fail": 3}, "new": {"fail": 3}}


@pytest.mark.parametrize("kept_by", ["source", "directory"])
def test_d8_needs_failed_fetches_in_a_row(tmp_path: Path, kept_by: str) -> None:
    """A run whose source (or listed directory) failed doesn't fetch the pages
    under it: it ends their fetch counts, as the Apple scraper's root failure
    does, so pages failing only on the other runs never reach D8."""
    location = KeptLocation(tmp_path / "src", reason="")
    write(tmp_path, "src/page.md", "src/new.md")
    metadata: dict = {}
    for run_number in range(1, 2 * PERSISTENT_FAILURE_RUNS + 2):
        run = new_run(tmp_path, metadata)
        if run_number % 2:  # the pages fail
            assert run.page_failed("dir/page.md", SERVER, previously_good=True) is True
            assert run.page_failed("dir/new.md", TIMEOUT, previously_good=False) is False
            assert run.blocked, run_number
            expected = {"dir/page.md": {"fail": 1}, "dir/new.md": {"fail": 1}}
        else:  # their location fails: not fetched, kept
            failed = run.source_failed if kept_by == "source" else run.directory_failed
            assert failed("dir/", SERVER, location, key_prefix="dir/") is True
            assert not run.blocked and run.keeps_key("dir/page.md"), run_number
            expected = {}
        metadata = run.metadata(hash_keys={"dir/page.md"})
        assert metadata.get("failure_counts", {}) == expected, run_number


def test_local_errors_never_delete(tmp_path: Path) -> None:
    run = new_run(tmp_path, {"failure_counts": {"p": {"local": 2}}})
    run.local_error("q", tmp_path / "q.md", "boom")
    assert run.blocked
    run2 = new_run(tmp_path, {"failure_counts": {"p": {"local": 2}}})
    run2.local_error("p", tmp_path / "p.md", "boom")
    assert not run2.blocked and run2.exit_code() == 1  # persistent_local_error
    assert run2.is_expected(tmp_path / "p.md") and "p" in run2.produced
    run3 = new_run(tmp_path, {"failure_counts": {"p": {"local": 2}}})
    run3.page_ok("p", tmp_path / "p.md")
    run3.page_saved("p")
    assert run3.metadata(hash_keys=()) == {}


def test_a_local_count_lasts_until_the_page_saves_or_goes(tmp_path: Path) -> None:
    """A run that doesn't reach a page neither counts nor ends its local
    errors (as Apple's consecutive_local_errors, reset only by a save), so a
    parent failing every other run can't keep its block from lifting; the
    count goes with the page, once a run whose cleanup ran saves no key for it."""
    stored = {"failure_counts": {"had": {"local": 2, "fail": 1}, "new": {"local": 1}}}
    # Blocked (their parent failed): nothing is removed, every local count stays
    run = new_run(tmp_path, stored)
    run.page_failed("parent", SERVER, previously_good=True)
    assert run.metadata(hash_keys=set())["failure_counts"] == {"had": {"local": 2}, "new": {"local": 1},
                                                                "parent": {"fail": 1}}
    # Not blocked: the page whose key is saved stays (its file wasn't deleted),
    # the never-good one went with its parent (nothing reaches it)
    run2 = new_run(tmp_path, stored)
    metadata = run2.metadata(hash_keys={"had"})
    assert metadata["failure_counts"] == {"had": {"local": 2}}
    # The next run that reaches it counts on: the 3rd lifts the block
    run3 = new_run(tmp_path, metadata)
    run3.local_error("had", tmp_path / "had.md", "boom")
    assert not run3.blocked and run3.exit_code() == 1
    # A never-good page still failing locally keeps its count on a clean run
    run4 = new_run(tmp_path, {"failure_counts": {"new": {"local": 2}}})
    run4.local_error("new", tmp_path / "new.md", "boom")
    assert run4.metadata(hash_keys=set())["failure_counts"] == {"new": {"local": 3}}
    # A page removed upstream (404) or whose file the cleanup deleted (key pruned): its count goes
    run5 = new_run(tmp_path, stored)
    assert run5.page_failed("had", GONE, previously_good=True) is False
    assert run5.metadata(hash_keys=set()) == {}
    # A kept location keeps its pages' local counts (their files are kept),
    # never their fetch counts (this run didn't fetch them)
    run6 = new_run(tmp_path, stored)
    run6.source_failed("root", SERVER, KeptLocation(tmp_path, reason=""), key_prefix="")
    assert run6.metadata(hash_keys=set())["failure_counts"] == {"had": {"local": 2}, "new": {"local": 1}}


def test_a_page_whose_links_cant_be_read_blocks_uncounted(tmp_path: Path) -> None:
    stored = {"failure_counts": {"p": {"fail": 1}}}
    for _ in range(PERSISTENT_FAILURE_RUNS + 1):  # never lifted: its live children are unknown
        run = new_run(tmp_path, stored)
        run.unprocessed("p", tmp_path / "D" / "p.md", "ValueError: bad link")
        run.unprocessed("unsafe", None, "ValueError: bad link")  # no safe path: no file, still blocks
        assert run.blocked and run.exit_code() == 1
        assert run.is_expected(tmp_path / "D" / "p.md") and {"p", "unsafe"} <= run.produced
        assert run.metadata(hash_keys=()) == stored  # carried, not counted
    write(tmp_path, "D/p.md", "D/orphan.md")
    assert run.cleanup([tmp_path / "D"]).skipped and (tmp_path / "D/orphan.md").exists()


def test_configured_source_rules(tmp_path: Path) -> None:
    location = KeptLocation(tmp_path / "src", reason="")
    run = new_run(tmp_path)
    assert run.source_failed("dir/", GONE, location, key_prefix="dir/") is True  # pending
    assert run.exit_code() == 0 and run.keeps_key("dir/file.md")
    assert run.is_kept(tmp_path / "src" / "a" / "b.md") and not run.is_kept(tmp_path / "other.md")
    run2 = new_run(tmp_path, run.metadata(hash_keys=()))
    assert run2.source_failed("dir/", GONE, location, key_prefix="dir/") is False  # source_gone
    assert run2.exit_code() == 0 and not run2.is_kept(tmp_path / "src" / "b.md")
    assert run2.metadata(hash_keys=())["failure_counts"] == {"dir/": {"gone": 2}}
    # Any other failure keeps it (exit 1) and never counts toward removal; its
    # own gone count stays, while a page under it, not fetched, loses its fetch count
    run3 = new_run(tmp_path, {"failure_counts": {"dir/": {"gone": 1}, "dir/x.md": {"fail": 1}}})
    assert run3.source_failed("dir/", SERVER, location, key_prefix="dir/") is True
    assert run3.exit_code() == 1 and not run3.blocked
    assert run3.metadata(hash_keys=())["failure_counts"] == {"dir/": {"gone": 1}}
    # A 404 after the 5xx is the 2nd consecutive 404 run (only an answer resets it)
    run4 = new_run(tmp_path, run3.metadata(hash_keys=()))
    assert run4.source_failed("dir/", GONE, location, key_prefix="dir/") is False
    run5 = new_run(tmp_path, run3.metadata(hash_keys=()))
    run5.source_ok("dir/")
    assert "dir/" not in run5.metadata(hash_keys=()).get("failure_counts", {})


def test_configured_file_rules(tmp_path: Path) -> None:
    """A configured file is a source: 404/410 x2 removes it; any other failure
    keeps it every run (source_fetch_failed, exit 1), never counted toward
    D8, and blocks nothing."""
    path = write(tmp_path, "src/README.md")[0]
    run = new_run(tmp_path)
    assert run.configured_file_failed("f", GONE, path) is True
    assert run.exit_code() == 0 and run.is_kept(path)
    run2 = new_run(tmp_path, run.metadata(hash_keys=()))
    assert run2.configured_file_failed("f", GONE, path) is False
    metadata: dict = {}
    for failure in (SERVER, FORBIDDEN, TIMEOUT, SERVER):  # past PERSISTENT_FAILURE_RUNS
        run3 = new_run(tmp_path, metadata)
        assert run3.configured_file_failed("f", failure, path) is True
        assert run3.exit_code() == 1 and not run3.blocked and run3.is_kept(path)
        assert run3.errors == [f"source_fetch_failed: f ({failure.error})"]
        metadata = run3.metadata(hash_keys=("f",))
        assert "failure_counts" not in metadata


def test_has_file_named_is_exact(tmp_path: Path) -> None:
    """Only a file under exactly that name: never one in another casing
    (which Path.exists() accepts on macOS), a directory or a missing parent."""
    write(tmp_path, "d/Page.md")
    assert has_file_named(tmp_path / "d" / "Page.md")
    assert not has_file_named(tmp_path / "d" / "page.md")
    assert not has_file_named(tmp_path / "d")
    assert not has_file_named(tmp_path / "missing" / "x.md")


def test_directory_found_by_a_listing(tmp_path: Path) -> None:
    location = KeptLocation(tmp_path / "src" / "sub", reason="")
    write(tmp_path, "src/sub/x.md")
    run = new_run(tmp_path)
    assert run.directory_failed("sub/", GONE, location, key_prefix="sub/") is False
    assert run.exit_code() == 0
    assert run.directory_failed("sub/", SERVER, location, key_prefix="sub/") is True
    assert run.exit_code() == 1 and not run.blocked and run.is_kept(tmp_path / "src" / "sub" / "x.md")
    assert "failure_counts" not in run.metadata(hash_keys=())


def test_a_new_directory_failing_follows_the_never_good_rule(tmp_path: Path) -> None:
    """A listed directory we have no files under: keeping it would protect
    nothing, so a transient failure blocks (a file moved into it would
    otherwise be deleted), counted and lifted at 3; a 4xx doesn't block."""
    write(tmp_path, "src/a.md", "src/other/y.txt")
    for name in ("new", "other"):  # missing, or holding no .md file
        location = KeptLocation(tmp_path / "src" / name, reason="")
        metadata: dict = {}
        for run_number in (1, 2):
            run = new_run(tmp_path, metadata)
            assert run.directory_failed(f"{name}/", SERVER, location, key_prefix=f"{name}/") is False
            assert run.blocked and run.exit_code() == 1 and not run.kept
            metadata = run.metadata(hash_keys=())
            assert metadata["failure_counts"] == {f"{name}/": {"fail": run_number}}
        run3 = new_run(tmp_path, metadata)
        assert run3.directory_failed(f"{name}/", TIMEOUT, location, key_prefix=f"{name}/") is False
        assert not run3.blocked and run3.exit_code() == 1  # persistent_fetch_failure
        assert run3.metadata(hash_keys=())["failure_counts"] == {f"{name}/": {"fail": 3}}
        run4 = new_run(tmp_path)
        assert run4.directory_failed(f"{name}/", FORBIDDEN, location, key_prefix=f"{name}/") is False
        assert not run4.blocked and run4.exit_code() == 0 and run4.metadata(hash_keys=()) == {}
    # A file moved into a new directory whose listing failed is not deleted
    run5 = new_run(tmp_path)
    run5.directory_failed("new/", SERVER, KeptLocation(tmp_path / "src" / "new", reason=""), key_prefix="new/")
    assert run5.cleanup([tmp_path / "src"]).skipped and (tmp_path / "src/a.md").exists()


def test_kept_location_excludes_nested_sources(tmp_path: Path) -> None:
    location = KeptLocation(tmp_path / "MLX", reason="", excluded=(tmp_path / "MLX" / "mlx-data",))
    assert location.holds(tmp_path / "MLX" / "a.md") and location.holds(tmp_path / "mlx" / "b" / "c.md")
    assert not location.holds(tmp_path / "MLX" / "mlx-data" / "x.md")
    assert not location.holds(tmp_path / "MLX-Swift" / "x.md")


def test_unreadable_hash_file_blocks(tmp_path: Path) -> None:
    run = new_run(tmp_path, load_error="bad json")
    assert run.blocked and run.exit_code() == 1
    write(tmp_path, "D/a.md")
    assert run.cleanup([tmp_path / "D"]).skipped and (tmp_path / "D/a.md").exists()


# -- confirm-then-delete ----------------------------------------------------

def test_valve_matches_the_apple_scraper() -> None:
    for files in range(0, 2200, 7):
        for orphans in (0, 1, files // 2 - 1, files // 2, files // 2 + 1, 1000, 1001, files):
            if 0 <= orphans <= files:
                assert valve_trips(orphans, files) == apple_valve_trips(orphans, files), (orphans, files)


def test_cleanup_deletes_under_the_valve(tmp_path: Path) -> None:
    files = write(tmp_path, "D/a.md", "D/b.md", "D/sub/c.md", "D/d.md", "D/e.txt")
    run = new_run(tmp_path)
    for path in files[:3]:
        run.expect(path)
    result = run.cleanup([tmp_path / "D"])
    assert result.deleted == ["D/d.md"] and (tmp_path / "D/e.txt").exists()
    assert run.metadata(hash_keys=()) == {}


def test_cleanup_holds_then_confirms(tmp_path: Path) -> None:
    files = write(tmp_path, "D/a.md", "D/b.md", "D/c.md", "D/d.md")
    run = new_run(tmp_path)
    run.expect(files[0])
    run.expect(files[1])  # 2 of 4 orphaned: held
    result = run.cleanup([tmp_path / "D"])
    assert result.deleted == [] and result.held == {"D": (2, 4)}
    assert run.metadata(hash_keys=()) == {"pending_orphans": ["D/c.md", "D/d.md"]}
    # Next clean run: c still orphaned (confirmed), d is back
    run2 = new_run(tmp_path, run.metadata(hash_keys=()))
    for path in (files[0], files[1], files[3]):
        run2.expect(path)
    result2 = run2.cleanup([tmp_path / "D"])
    assert result2.deleted == ["D/c.md"] and result2.confirmed == 1
    assert run2.metadata(hash_keys=()) == {}


def test_confirmation_is_case_insensitive_and_a_big_remainder_waits(tmp_path: Path) -> None:
    files = write(tmp_path, *(f"D/f{i}.md" for i in range(10)))
    run = new_run(tmp_path, {"pending_orphans": ["d/F0.md", "D/f1.md"]})
    run.expect(files[9])  # 9 orphans: f0, f1 confirmed; 7 of the 8 left trip the valve
    result = run.cleanup([tmp_path / "D"])
    assert sorted(result.deleted) == ["D/f0.md", "D/f1.md"]
    assert run.pending_orphans == [f"D/f{i}.md" for i in range(2, 9)]


def test_blocked_cleanup_leaves_pending_untouched(tmp_path: Path) -> None:
    write(tmp_path, "D/a.md", "D/b.md")
    run = new_run(tmp_path, {"pending_orphans": ["D/a.md"]})
    run.page_failed("x", SERVER, previously_good=True)
    result = run.cleanup([tmp_path / "D"])
    assert result.skipped and (tmp_path / "D/a.md").exists()
    assert run.metadata(hash_keys=())["pending_orphans"] == ["D/a.md"]


def test_nested_scan_dirs_weigh_each_file_once(tmp_path: Path) -> None:
    files = write(tmp_path, *(f"Top/f{i}.md" for i in range(6)), "Top/dropped/x.md", "Top/dropped/y/z.md")
    run = new_run(tmp_path)
    for path in files[:6]:
        run.expect(path)
    result = run.cleanup([tmp_path / "Top", tmp_path / "Top" / "dropped"],
                         removable_dirs=[tmp_path / "Top" / "dropped"])
    # The dropped dir is weighed alone (2 of 2: held), not as 2 of 8 in Top
    assert result.held == {"Top/dropped": (2, 2)} and result.deleted == []
    run2 = new_run(tmp_path, run.metadata(hash_keys=()))
    for path in files[:6]:
        run2.expect(path)
    run2.cleanup([tmp_path / "Top", tmp_path / "Top" / "dropped"], removable_dirs=[tmp_path / "Top" / "dropped"])
    assert not (tmp_path / "Top" / "dropped").exists() and (tmp_path / "Top").is_dir()


def test_kept_files_are_never_orphans(tmp_path: Path) -> None:
    write(tmp_path, "D/a.md", "D/keep/b.md", "D/keep/c.md")
    run = new_run(tmp_path)
    run.expect(tmp_path / "D/a.md")
    run.source_failed("k/", SERVER, KeptLocation(tmp_path / "D" / "keep", reason=""), key_prefix="k/")
    result = run.cleanup([tmp_path / "D"])
    assert result.deleted == [] and (tmp_path / "D/keep/b.md").exists()


def test_a_kept_location_leaves_its_pending_orphans_waiting(tmp_path: Path) -> None:
    files = write(tmp_path, *(f"D/f{i}.md" for i in range(10)))
    run = new_run(tmp_path)
    for path in files[:4]:
        run.expect(path)
    run.cleanup([tmp_path / "D"])  # 6 of 10 orphaned: held
    held = run.metadata(hash_keys=())["pending_orphans"]
    assert len(held) == 6
    # The source fails: nothing under it was scraped, so its held files wait
    run2 = new_run(tmp_path, run.metadata(hash_keys=()))
    run2.source_failed("root", SERVER, KeptLocation(tmp_path / "D", reason=""), key_prefix="")
    assert run2.cleanup([tmp_path / "D"]).deleted == []
    assert run2.metadata(hash_keys=())["pending_orphans"] == held
    # The next run that scrapes it confirms them
    run3 = new_run(tmp_path, run2.metadata(hash_keys=()))
    for path in files[:4]:
        run3.expect(path)
    result = run3.cleanup([tmp_path / "D"])
    assert sorted(result.deleted) == held and result.confirmed == 6
    assert "pending_orphans" not in run3.metadata(hash_keys=())


def test_only_a_kept_locations_pending_orphans_are_carried(tmp_path: Path) -> None:
    files = write(tmp_path, "D/a.md", "D/b.md", "D/c.md", "D/keep/x.md")
    run = new_run(tmp_path, {"pending_orphans": ["D/b.md", "D/gone.md", "D/keep/x.md"]})
    run.expect(files[0])
    run.expect(files[1])  # b is back
    run.directory_failed("keep/", SERVER, KeptLocation(tmp_path / "D" / "keep", reason=""), key_prefix="keep/")
    result = run.cleanup([tmp_path / "D"])
    assert result.deleted == ["D/c.md"]  # 1 of 4: under the valve
    assert run.metadata(hash_keys=())["pending_orphans"] == ["D/keep/x.md"]


def test_expected_files_match_like_the_apple_scraper() -> None:
    names = ["D/Basics.md", "D/basics.md", "D/BASICS.md", "D/Other.md"]
    candidates = [*names, "D/other.md", "D/Gone.md"]
    for existing_mask in range(1, 2 ** len(names)):
        existing = {name for i, name in enumerate(names) if existing_mask >> i & 1}
        for expected_mask in range(2 ** len(candidates)):
            expected = [name for i, name in enumerate(candidates) if expected_mask >> i & 1]
            apple = HashManager._unrecorded({Path(name) for name in existing}, expected)
            assert unmatched(existing, expected) == {str(path) for path in apple}, (existing, expected)


def test_a_case_only_rename_leaves_the_old_file_an_orphan(tmp_path: Path) -> None:
    files = write(tmp_path, *(f"D/p{i}.md" for i in range(4)), "D/Basics.md")
    run = new_run(tmp_path)
    for path in files[:4]:
        run.expect(path)
    renamed = write(tmp_path, "D/basics.md")[0]  # upstream now spells it basics.md
    run.expect(renamed)
    result = run.cleanup([tmp_path / "D"])
    if case_sensitive(tmp_path):
        # Written next to the old file (CI): the old one is stale
        assert result.deleted == ["D/Basics.md"]
        assert sorted(path.name for path in (tmp_path / "D").iterdir()) == ["basics.md", "p0.md", "p1.md",
                                                                            "p2.md", "p3.md"]
    else:
        # Written into the old file, which keeps its name (macOS): kept
        assert result.deleted == [] and "Basics.md" in {path.name for path in (tmp_path / "D").iterdir()}


def test_a_file_named_only_in_another_casing_is_kept(tmp_path: Path) -> None:
    files = write(tmp_path, "D/Basics.md", "D/a.md")
    run = new_run(tmp_path)
    run.expect(tmp_path / "D" / "basics.md")  # no file has this exact name
    run.expect(files[1])
    assert run.cleanup([tmp_path / "D"]).deleted == [] and files[0].exists()


def test_nested_scan_dirs_list_each_file_once_in_any_casing(tmp_path: Path) -> None:
    files = write(tmp_path, *(f"Top/f{i}.md" for i in range(4)), "Top/sub/x.md")
    run = new_run(tmp_path)
    for path in files[:4]:
        run.expect(path)
    if case_sensitive(tmp_path):
        # A twin of the deeper scanned dir in another casing is a separate dir
        # (CI): weighed in Top, its stale file is an orphan
        write(tmp_path, "Top/SUB/x.md")
        run.expect(files[4])
        result = run.cleanup([tmp_path / "Top", tmp_path / "Top" / "sub"])
        assert result.deleted == ["Top/SUB/x.md"] and files[4].exists()
    else:
        # The deeper scanned dir spelled in another casing (macOS) lists the
        # same file that Top lists: weighed once, in it, and expected there
        run.expect(tmp_path / "Top" / "SUB" / "x.md")
        result = run.cleanup([tmp_path / "Top", tmp_path / "Top" / "SUB"])
        assert result.deleted == [] and files[4].exists()


def test_a_dir_named_like_a_doc_is_not_deleted(tmp_path: Path) -> None:
    write(tmp_path, "D/a.md", "D/b.md", "D/c.md")
    (tmp_path / "D" / "x.md").mkdir()
    run = new_run(tmp_path)
    for name in ("a", "b", "c"):
        run.expect(tmp_path / "D" / f"{name}.md")
    result = run.cleanup([tmp_path / "D"])
    assert result.deleted == [] and result.failures == []


def test_dry_run_deletes_nothing(tmp_path: Path) -> None:
    write(tmp_path, "D/a.md", "D/b.md", "D/c.md")
    run = new_run(tmp_path)
    run.expect(tmp_path / "D/a.md")
    run.expect(tmp_path / "D/b.md")
    result = run.cleanup([tmp_path / "D"], dry_run=True)
    assert result.deleted == ["D/c.md"] and (tmp_path / "D/c.md").exists()


def test_a_failed_deletion_is_an_error(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    write(tmp_path, "D/a.md", "D/b.md", "D/c.md")
    run = new_run(tmp_path)
    run.expect(tmp_path / "D/a.md")
    run.expect(tmp_path / "D/b.md")

    def refuse(self: Path, missing_ok: bool = False) -> None:
        raise PermissionError("read-only")

    monkeypatch.setattr(Path, "unlink", refuse)
    result = run.cleanup([tmp_path / "D"])
    assert result.failures and run.exit_code() == 1
