#!/usr/bin/env python3
"""HIG scraper: failure policy, orphan cleanup and hash file, over consecutive runs.

Each test runs the real scraper (httpx included) against a local fake HIG
(fake_upstream.py), in a temporary docs dir and hash file. The site: the root
links to a, b, c, d and e; c links to c1 (7 pages, so one or two removals
stay under the mass-removal valve).
"""

import errno
import json
from pathlib import Path
from typing import Any, AsyncIterator, Dict, Set, Tuple

import pytest

import scrape_hig_docs
import utilities.source_policy as source_policy
from fake_upstream import BAD_JSON, DROP, FakeUpstream
from scrape_hig_docs import HIGDocsScraper

ROOT_TITLE = "Human Interface Guidelines"
ROOT_LINKS = ("a", "b", "c", "d", "e")
ALL = {"index.md", "a.md", "b.md", "c.md", "c1.md", "d.md", "e.md"}
NAMES = ("", "a", "b", "c", "c1", "d", "e")


@pytest.fixture
async def site(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> AsyncIterator[FakeUpstream]:
    upstream = FakeUpstream()
    await upstream.start()
    monkeypatch.setattr(scrape_hig_docs, "OUTPUT_DIR", tmp_path / "documentation" / "HIG")
    monkeypatch.setattr(scrape_hig_docs, "HASH_FILE", tmp_path / ".hashes" / "hig_docs_hashes.json")
    monkeypatch.setattr(scrape_hig_docs, "JSON_BASE_URL", upstream.hig_base())
    monkeypatch.setattr(scrape_hig_docs, "REQUEST_DELAY", 0)
    monkeypatch.setattr(source_policy, "RETRY_BASE_DELAY", 0)
    upstream.hig_page("", ROOT_TITLE, ROOT_LINKS)
    for name in ("a", "b", "d", "e"):
        upstream.hig_page(name, name.upper())
    upstream.hig_page("c", "C", ("c1",))
    upstream.hig_page("c1", "C1")
    yield upstream
    await upstream.stop()


async def run(**kwargs: Any) -> HIGDocsScraper:
    async with HIGDocsScraper(**kwargs) as scraper:
        await scraper.scrape_all()
    return scraper


def docs() -> Set[str]:
    return {p.relative_to(scrape_hig_docs.OUTPUT_DIR).as_posix() for p in scrape_hig_docs.OUTPUT_DIR.rglob("*.md")
            if p.is_file()}


def hash_file() -> Dict[str, Any]:
    data: Dict[str, Any] = json.loads(scrape_hig_docs.HASH_FILE.read_text())
    return data


def counts() -> Dict[str, Any]:
    result: Dict[str, Any] = hash_file()["metadata"].get("failure_counts", {})
    return result


def url(upstream: FakeUpstream, name: str) -> str:
    return f"{upstream.base_url}{upstream.hig_path(name)}"


def urls(upstream: FakeUpstream, names: Tuple[str, ...]) -> Set[str]:
    return {url(upstream, name) for name in names}


def without(*names: str) -> Tuple[str, ...]:
    """The root's links without these pages."""
    return tuple(name for name in ROOT_LINKS if name not in names)


async def test_full_scrape_writes_the_shared_hash_format(site: FakeUpstream) -> None:
    scraper = await run()
    assert scraper.exit_code == 0
    assert docs() == ALL
    data = hash_file()
    assert data["metadata"]["source"] == "scrape_hig_docs.py"
    assert data["metadata"]["total_files"] == 7
    assert "failure_counts" not in data["metadata"] and "pending_orphans" not in data["metadata"]
    assert set(data["hashes"]) == urls(site, NAMES)


async def test_flat_hash_file_is_converted_on_a_quiet_run(site: FakeUpstream) -> None:
    await run()
    entries = hash_file()["hashes"]
    scrape_hig_docs.HASH_FILE.write_text(json.dumps(entries))  # the old flat format
    scraper = await run()
    assert scraper.exit_code == 0 and scraper.stats["pages_scraped"] == 0
    data = hash_file()
    assert data["hashes"] == entries and data["metadata"]["source"] == "scrape_hig_docs.py"
    # And nothing is rewritten on the next quiet run
    before = scrape_hig_docs.HASH_FILE.read_text()
    await run()
    assert scrape_hig_docs.HASH_FILE.read_text() == before


async def test_a_page_404_is_removed_in_the_same_run(site: FakeUpstream) -> None:
    await run()
    site.faults[site.hig_path("b")] = 404  # still linked from the root
    scraper = await run()
    assert scraper.exit_code == 0
    assert docs() == ALL - {"b.md"}
    assert url(site, "b") not in hash_file()["hashes"]
    assert "failure_counts" not in hash_file()["metadata"]


async def test_an_unlinked_page_and_its_subtree_are_removed(site: FakeUpstream) -> None:
    await run()
    site.hig_page("", ROOT_TITLE, without("c"))
    scraper = await run()
    assert scraper.exit_code == 0
    assert docs() == ALL - {"c.md", "c1.md"}
    assert set(hash_file()["hashes"]) == urls(site, NAMES) - urls(site, ("c", "c1"))


async def test_a_good_page_failing_3_runs_is_removed_at_run_3(site: FakeUpstream) -> None:
    await run()
    site.faults[site.hig_path("c")] = 502
    site.hig_page("", ROOT_TITLE, without("a"))  # a is a real removal meanwhile
    for run_number in (1, 2):
        scraper = await run()
        assert scraper.exit_code == 1, run_number
        assert docs() == ALL, run_number  # blocked: nothing deleted, c and its subtree kept
        assert counts() == {url(site, "c"): {"fail": run_number}}
    scraper = await run()  # run 3: D8, c and its unreachable subtree go with a
    assert scraper.exit_code == 1
    assert docs() == ALL - {"a.md", "c.md", "c1.md"}
    assert counts() == {url(site, "c"): {"fail": 3}}
    assert url(site, "c") not in hash_file()["hashes"]
    scraper = await run()  # run 4, still linked and failing: not blocked again
    assert scraper.exit_code == 1 and docs() == ALL - {"a.md", "c.md", "c1.md"}
    site.faults.clear()
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == ALL - {"a.md"}
    assert "failure_counts" not in hash_file()["metadata"]


async def test_a_new_page_502_protects_the_page_moved_under_it(site: FakeUpstream) -> None:
    await run()
    # c1 moves under a new page n, which fails; c no longer links to c1
    site.hig_page("", ROOT_TITLE, (*ROOT_LINKS, "n"))
    site.hig_page("c", "C")
    site.hig_page("n", "N", ("c1",))
    site.faults[site.hig_path("n")] = 502
    for run_number in (1, 2):
        scraper = await run()
        assert scraper.exit_code == 1
        assert docs() == ALL  # blocked, the moved page kept
        assert counts() == {url(site, "n"): {"fail": run_number}}
    scraper = await run()  # lifted at 3: the page no fetched page links to goes
    assert scraper.exit_code == 1
    assert docs() == ALL - {"c1.md"}
    site.faults.clear()
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == ALL | {"n.md"}
    assert "failure_counts" not in hash_file()["metadata"]


async def test_a_new_page_4xx_does_not_block(site: FakeUpstream) -> None:
    await run()
    site.hig_page("", ROOT_TITLE, (*ROOT_LINKS, "n"))
    site.hig_page("c", "C")
    site.hig_page("n", "N", ("c1",))
    site.faults[site.hig_path("n")] = 403
    scraper = await run()
    assert scraper.exit_code == 0
    assert docs() == ALL - {"c1.md"}
    assert "failure_counts" not in hash_file()["metadata"]


async def test_a_good_page_403_and_invalid_json_block(site: FakeUpstream) -> None:
    await run()
    site.faults[site.hig_path("a")] = 403
    site.faults[site.hig_path("b")] = BAD_JSON
    site.hig_page("c", "C")  # c1 unlinked: a removal the block holds
    scraper = await run()
    assert scraper.exit_code == 1
    assert docs() == ALL
    assert counts() == {url(site, "a"): {"fail": 1}, url(site, "b"): {"fail": 1}}


async def test_transient_failures_are_retried(site: FakeUpstream) -> None:
    await run()
    site.flaky[site.hig_path("a")] = [503, DROP, 502]
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == ALL
    assert site.count(site.hig_path("a")) == 5  # 2 runs; 4 attempts in the 2nd
    assert "failure_counts" not in hash_file()["metadata"]


async def test_a_convert_error_x3_keeps_the_file(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    await run()
    original = (scrape_hig_docs.OUTPUT_DIR / "a.md").read_text()
    site.hig_page("a", "A changed")
    site.hig_page("", ROOT_TITLE, without("b"))  # b removed meanwhile
    convert = HIGDocsScraper._extract_to_markdown

    def failing_convert(self: HIGDocsScraper, data: Dict[str, Any], json_url: str) -> str:
        if json_url.endswith("/a.json"):
            raise ValueError("converter bug")
        return convert(self, data, json_url)

    monkeypatch.setattr(HIGDocsScraper, "_extract_to_markdown", failing_convert)
    for run_number in (1, 2):
        scraper = await run()
        assert scraper.exit_code == 1 and docs() == ALL
        assert counts() == {url(site, "a"): {"local": run_number}}
    scraper = await run()  # 3: persistent_local_error, no longer blocking; a kept
    assert scraper.exit_code == 1
    assert docs() == ALL - {"b.md"}
    assert (scrape_hig_docs.OUTPUT_DIR / "a.md").read_text() == original
    assert counts() == {url(site, "a"): {"local": 3}}
    monkeypatch.setattr(HIGDocsScraper, "_extract_to_markdown", convert)
    scraper = await run()
    assert scraper.exit_code == 0
    assert "A changed" in (scrape_hig_docs.OUTPUT_DIR / "a.md").read_text()
    assert "failure_counts" not in hash_file()["metadata"]


async def test_a_convert_error_count_survives_runs_that_dont_reach_the_page(site: FakeUpstream,
                                                                            monkeypatch: pytest.MonkeyPatch) -> None:
    """c1's converter fails every run, and its only parent c fails every other
    run: a run that doesn't reach c1 neither counts nor ends its local errors,
    so the block still lifts at its 3rd error; the count goes with the page."""
    await run()
    site.hig_page("c1", "C1 changed")
    site.hig_page("", ROOT_TITLE, without("b"))  # b removed meanwhile
    convert = HIGDocsScraper._extract_to_markdown

    def failing_convert(self: HIGDocsScraper, data: Dict[str, Any], json_url: str) -> str:
        if json_url.endswith("/c1.json"):
            raise ValueError("converter bug")
        return convert(self, data, json_url)

    monkeypatch.setattr(HIGDocsScraper, "_extract_to_markdown", failing_convert)
    c, c1 = url(site, "c"), url(site, "c1")
    for run_number in range(1, 5):
        site.faults.pop(site.hig_path("c"), None)
        if run_number % 2 == 0:
            site.faults[site.hig_path("c")] = 502
        scraper = await run()
        assert scraper.exit_code == 1 and docs() == ALL, run_number  # blocked by c1, or by c
        local = {c1: {"local": (run_number + 1) // 2}}
        assert counts() == (local | {c: {"fail": 1}} if run_number % 2 == 0 else local), run_number
    site.faults.clear()
    scraper = await run()  # c1's 3rd error: kept, no longer blocking
    assert scraper.exit_code == 1 and docs() == ALL - {"b.md"}
    assert counts() == {c1: {"local": 3}}
    site.hig_page("c", "C")  # c1 removed upstream: its file, entry and count go
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == ALL - {"b.md", "c1.md"}
    assert c1 not in hash_file()["hashes"] and "failure_counts" not in hash_file()["metadata"]


async def test_a_save_error_blocks_and_its_children_are_still_reached(site: FakeUpstream) -> None:
    await run()
    # c can't be written (a dir in its place); c1 must still be reached through it
    site.hig_page("c", "C changed", ("c1",))
    (scrape_hig_docs.OUTPUT_DIR / "c.md").unlink()
    (scrape_hig_docs.OUTPUT_DIR / "c.md").mkdir()
    site.hig_page("", ROOT_TITLE, without("b"))
    scraper = await run()
    assert scraper.exit_code == 1
    assert docs() == ALL - {"c.md"}  # b's removal blocked
    assert counts() == {url(site, "c"): {"local": 1}}
    assert site.count(site.hig_path("c1")) == 2
    assert not list(scrape_hig_docs.OUTPUT_DIR.rglob("*.tmp"))


async def test_a_write_failing_part_way_keeps_the_old_doc_whole(site: FakeUpstream,
                                                                monkeypatch: pytest.MonkeyPatch) -> None:
    """Doc writes are atomic: a write that fails part way (disk full) leaves
    the old doc as it was (kept as a local error), and no temp file."""
    await run()
    original = (scrape_hig_docs.OUTPUT_DIR / "a.md").read_text()
    site.hig_page("a", "A changed")
    write_text = Path.write_text

    def disk_full(self: Path, data: str, *args: Any, **kwargs: Any) -> int:
        if self.name.startswith("a.md"):
            write_text(self, data[:10], *args, **kwargs)
            raise OSError(errno.ENOSPC, "No space left on device")
        return write_text(self, data, *args, **kwargs)

    monkeypatch.setattr(Path, "write_text", disk_full)
    scraper = await run()
    assert scraper.exit_code == 1 and docs() == ALL
    assert (scrape_hig_docs.OUTPUT_DIR / "a.md").read_text() == original
    assert not list(scrape_hig_docs.OUTPUT_DIR.rglob("*.tmp"))
    assert counts() == {url(site, "a"): {"local": 1}}
    monkeypatch.setattr(Path, "write_text", write_text)
    scraper = await run()
    assert scraper.exit_code == 0 and "A changed" in (scrape_hig_docs.OUTPUT_DIR / "a.md").read_text()


@pytest.mark.parametrize("loss", ["deleted", "unreadable"])
async def test_a_page_we_have_is_protected_after_the_hash_file_is_lost(site: FakeUpstream, loss: str) -> None:
    """A hash file that was deleted, or couldn't be read (that run blocks, and
    its save keeps only the pages it fetched), loses keys, not files: a 403 on
    a page whose file is on disk still takes D8's 3 runs, as Apple's lost
    entries do, and its subtree is kept until then."""
    await run()
    if loss == "deleted":
        scrape_hig_docs.HASH_FILE.unlink()
    else:
        scrape_hig_docs.HASH_FILE.write_text("{not json")
    site.faults[site.hig_path("c")] = 403  # c links to c1
    for run_number in (1, 2):
        scraper = await run()
        assert scraper.exit_code == 1 and docs() == ALL, run_number  # kept and blocking
        assert counts() == {url(site, "c"): {"fail": run_number}}
        assert url(site, "c") not in hash_file()["hashes"]  # still unrecorded: its file is what tells
    scraper = await run()  # D8: c and its unreachable subtree go
    assert scraper.exit_code == 1 and docs() == ALL - {"c.md", "c1.md"}
    site.faults.clear()
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == ALL and "failure_counts" not in hash_file()["metadata"]


async def test_root_404_x2_removes_hig_through_confirm_then_delete(site: FakeUpstream) -> None:
    await run()
    site.faults[site.hig_path("")] = 404
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == ALL  # source_gone_pending
    assert counts() == {url(site, ""): {"gone": 1}}
    scraper = await run()  # source_gone: every file orphaned, held by the valve
    assert scraper.exit_code == 0 and docs() == ALL
    assert hash_file()["metadata"]["pending_orphans"] == sorted(f"HIG/{name}" for name in ALL)
    scraper = await run()  # confirmed
    assert scraper.exit_code == 0 and docs() == set()
    metadata = hash_file()["metadata"]
    assert "pending_orphans" not in metadata and hash_file()["hashes"] == {}
    assert metadata["failure_counts"] == {url(site, ""): {"gone": 2}}
    before = scrape_hig_docs.HASH_FILE.read_text()
    scraper = await run()  # still gone: nothing changes, no churn
    assert scraper.exit_code == 0 and scrape_hig_docs.HASH_FILE.read_text() == before


async def test_root_5xx_keeps_everything_every_run(site: FakeUpstream) -> None:
    await run()
    site.faults[site.hig_path("c")] = 502
    await run()
    assert counts() == {url(site, "c"): {"fail": 1}}
    site.faults[site.hig_path("")] = 503
    for _ in range(4):
        scraper = await run()
        assert scraper.exit_code == 1 and docs() == ALL
        assert counts() == {}  # c isn't fetched: its streak ends (as an Apple root failure ends it)
    site.faults.clear()
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == ALL and "failure_counts" not in hash_file()["metadata"]


async def test_d8_needs_3_failed_fetches_in_a_row(site: FakeUpstream) -> None:
    """a fails on odd runs and the root on even runs, when a isn't fetched:
    a never fails 2 runs in a row, so D8 never treats it as removed."""
    await run()
    a = url(site, "a")
    for run_number in range(1, 8):
        site.faults.clear()
        site.faults[site.hig_path("a" if run_number % 2 else "")] = 502
        scraper = await run()
        assert scraper.exit_code == 1 and docs() == ALL, run_number
        assert counts() == ({a: {"fail": 1}} if run_number % 2 else {}), run_number
    site.faults.clear()
    assert (await run()).exit_code == 0 and docs() == ALL and counts() == {}


async def test_root_404_then_recovery_restarts_the_count(site: FakeUpstream) -> None:
    await run()
    site.faults[site.hig_path("")] = 404
    await run()
    site.faults.clear()
    scraper = await run()
    assert scraper.exit_code == 0 and "failure_counts" not in hash_file()["metadata"]
    site.faults[site.hig_path("")] = 404
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == ALL and counts() == {url(site, ""): {"gone": 1}}


async def test_mass_removal_is_confirmed_on_the_next_clean_run(site: FakeUpstream) -> None:
    await run()
    site.hig_page("", ROOT_TITLE, ("a",))  # b, c, c1, d, e unlinked: 5 of 7
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == ALL  # held
    assert hash_file()["metadata"]["pending_orphans"] == ["HIG/b.md", "HIG/c.md", "HIG/c1.md", "HIG/d.md", "HIG/e.md"]
    site.hig_page("", ROOT_TITLE, ("a", "b"))  # b is back: only the others are confirmed
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == {"index.md", "a.md", "b.md"}
    assert "pending_orphans" not in hash_file()["metadata"]


async def test_pending_orphans_and_counts_survive_quiet_runs(site: FakeUpstream) -> None:
    await run()
    site.hig_page("", ROOT_TITLE, ("a",))  # 5 of 7 unlinked: held
    await run()
    pending = hash_file()["metadata"]["pending_orphans"]
    # A blocked, quiet run (nothing downloaded or deleted): the list stays, the count is saved
    site.faults[site.hig_path("a")] = 502
    scraper = await run()
    assert scraper.exit_code == 1 and scraper.stats["pages_scraped"] == 0 and docs() == ALL
    assert hash_file()["metadata"]["pending_orphans"] == pending
    assert counts() == {url(site, "a"): {"fail": 1}}
    scraper = await run()  # quiet again: the count still moves
    assert scraper.exit_code == 1 and counts() == {url(site, "a"): {"fail": 2}}
    site.faults.clear()
    scraper = await run()  # the next clean run confirms the held removal
    assert scraper.exit_code == 0 and docs() == {"index.md", "a.md"}
    assert "pending_orphans" not in hash_file()["metadata"] and "failure_counts" not in hash_file()["metadata"]


async def test_a_root_failure_leaves_a_held_removal_waiting(site: FakeUpstream) -> None:
    await run()
    site.hig_page("", ROOT_TITLE, ("a",))  # 5 of 7 unlinked: held
    await run()
    pending = hash_file()["metadata"]["pending_orphans"]
    # The root fails: nothing of HIG was scraped, so the held list stays as it is
    site.faults[site.hig_path("")] = 503
    scraper = await run()
    assert scraper.exit_code == 1 and docs() == ALL
    assert hash_file()["metadata"]["pending_orphans"] == pending
    site.faults.clear()
    scraper = await run()  # the next run that scrapes HIG confirms it
    assert scraper.exit_code == 0 and docs() == {"index.md", "a.md"}
    assert "pending_orphans" not in hash_file()["metadata"]


async def test_a_deleted_file_is_rewritten(site: FakeUpstream) -> None:
    await run()
    (scrape_hig_docs.OUTPUT_DIR / "a.md").unlink()
    scraper = await run()
    assert scraper.stats["pages_scraped"] == 1 and docs() == ALL


async def test_an_unreadable_hash_file_blocks_once_and_is_replaced(site: FakeUpstream) -> None:
    await run()
    site.hig_page("c", "C")  # c1 unlinked
    scrape_hig_docs.HASH_FILE.write_bytes(b"\xff\xfe not utf-8")
    scraper = await run()
    assert scraper.exit_code == 1 and docs() == ALL  # blocked: hash_load_failed
    assert set(hash_file()["hashes"]) == urls(site, NAMES) - {url(site, "c1")}
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == ALL - {"c1.md"}


async def test_dry_run_writes_nothing(site: FakeUpstream) -> None:
    await run()
    before = scrape_hig_docs.HASH_FILE.read_text()
    site.hig_page("c", "C")
    site.faults[site.hig_path("a")] = 404
    scraper = await run(dry_run=True)
    assert scraper.exit_code == 0 and docs() == ALL
    assert scrape_hig_docs.HASH_FILE.read_text() == before
