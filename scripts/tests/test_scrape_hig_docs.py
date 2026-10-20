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
    # It records no render version: every page is rendered again, from unchanged JSON
    assert scraper.exit_code == 0 and scraper.stats["pages_scraped"] == len(ALL)
    data = hash_file()
    assert {url: entry["hash"] for url, entry in data["hashes"].items()} == {
        url: entry["hash"] for url, entry in entries.items()}
    assert data["metadata"]["source"] == "scrape_hig_docs.py"
    assert data["metadata"]["render"] == {"version": scrape_hig_docs.RENDER_VERSION}
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


def test_images_and_videos_use_the_light_variant_under_the_hosting_root() -> None:
    scraper = HIGDocsScraper()
    references: Dict[str, Any] = {
        "intro.png": {"type": "image", "alt": "A sketch.", "variants": [
            {"traits": ["2x", "light"], "url": "/images/com.apple.HIG/intro@2x.png"},
            {"traits": ["2x", "dark"], "url": "/images/com.apple.HIG/intro~dark@2x.png"}]},
        "card.png": {"type": "image", "alt": None, "variants": [
            {"traits": ["1x", "light"], "url": "https://docs-assets.developer.apple.com/published/1/card.png"}]},
        "success.mp4": {"type": "video", "alt": None, "variants": [
            {"traits": ["1x", "light"], "url": "/videos/com.apple.HIG/success.mp4"},
            {"traits": ["1x", "dark"], "url": "/videos/com.apple.HIG/success~dark.mp4"}]},
    }
    root = "https://developer.apple.com/tutorials"
    assert scraper._resolve_image("intro.png", references) == f"![A sketch.]({root}/images/com.apple.HIG/intro@2x.png)"
    # A null alt is no "None"; an absolute URL stays as it is
    assert scraper._resolve_image("card.png", references) == \
        "![](https://docs-assets.developer.apple.com/published/1/card.png)"
    assert scraper._resolve_video("success.mp4", references) == \
        f"[Video: success.mp4]({root}/videos/com.apple.HIG/success.mp4)"
    inline = scraper._extract_text_from_inline_content([{"type": "image", "identifier": "intro.png"}], references)
    assert inline == f"![A sketch.]({root}/images/com.apple.HIG/intro@2x.png)"
    assert scraper._resolve_image("missing.png", references) == ""


def test_a_caption_is_on_the_line_under_its_image_or_video() -> None:
    """An image's or video's caption (its metadata abstract) is on the line
    under it, on one line, in every container (in a table cell, after the
    image on the cell's line); a device frame alone is no caption, and a
    caption whose image can't be resolved is still rendered."""
    scraper = HIGDocsScraper()
    references: Dict[str, Any] = {
        "fig.png": {"type": "image", "alt": "A sketch.", "variants": [
            {"traits": ["2x", "light"], "url": "/images/com.apple.HIG/fig@2x.png"}]},
        "clip.mp4": {"type": "video", "variants": [
            {"traits": ["1x", "light"], "url": "/videos/com.apple.HIG/clip.mp4"}]},
    }
    captioned = {"type": "paragraph", "inlineContent": [{"type": "image", "identifier": "fig.png", "metadata": {
        "abstract": [{"type": "text", "text": "The "},
                     {"type": "strong", "inlineContent": [{"type": "text", "text": "Done"}]},
                     {"type": "text", "text": " button\nin a "}, {"type": "codeVoice", "code": "toolbar"}],
        "deviceFrame": "iPhone16-top-half"}}]}
    content = [
        captioned,
        {"type": "paragraph", "inlineContent": [
            {"type": "image", "identifier": "fig.png", "metadata": {"deviceFrame": "iPhone16-top-half"}}]},
        {"type": "video", "identifier": "clip.mp4", "metadata": {"abstract": [{"type": "text", "text": "Scrolling."}]}},
        paragraph("After."),
        {"type": "aside", "style": "note", "content": [captioned]},
        {"type": "unorderedList", "items": [{"content": [captioned]}]},
        {"type": "table", "header": "row", "rows": [[[paragraph("Example")]], [[captioned]]]},
        {"type": "paragraph", "inlineContent": [
            {"type": "image", "identifier": "gone.png",
             "metadata": {"abstract": [{"type": "text", "text": "Kept."}]}}]},
    ]
    root = "https://developer.apple.com/tutorials"
    image, caption = f"![A sketch.]({root}/images/com.apple.HIG/fig@2x.png)", "The **Done** button in a `toolbar`"
    assert scraper._convert_content_to_markdown(content, references, 2) == (
        f"{image}\n{caption}\n\n{image}\n\n"
        f"[Video: clip.mp4]({root}/videos/com.apple.HIG/clip.mp4)\nScrolling.\n\nAfter.\n\n"
        f"> **Note:** {image}\n> {caption}\n\n"
        f"- {image}\n  {caption}\n\n"
        f"| Example |\n| --- |\n| {image} {caption} |\n\n"
        "Kept.\n\n")


def test_an_aside_is_quoted_whole_and_ends_its_quote() -> None:
    """Every line of an aside is quoted, and the paragraph after it isn't."""
    scraper = HIGDocsScraper()
    content = [
        {"type": "aside", "style": "tip", "content": [
            {"type": "paragraph", "inlineContent": [{"type": "text", "text": "First."}]},
            {"type": "paragraph", "inlineContent": [{"type": "text", "text": "Second."}]}]},
        {"type": "paragraph", "inlineContent": [{"type": "text", "text": "After."}]},
    ]
    markdown = scraper._convert_content_to_markdown(content, {}, 2)
    assert "> **Tip:** First.\n>\n> Second.\n\nAfter." in markdown


def test_an_aside_is_labeled_with_its_name_else_its_style() -> None:
    scraper = HIGDocsScraper()
    content = [
        {"type": "aside", "style": "note", "name": "Developer note", "content": [paragraph("Use the API.")]},
        {"type": "aside", "style": "important", "content": [paragraph("Unnamed.")]},
    ]
    assert scraper._convert_content_to_markdown(content, {}, 2).lstrip("\n") == (
        "> **Developer note:** Use the API.\n\n> **Important:** Unnamed.\n\n")


def test_a_reference_reads_as_the_prose_words_it() -> None:
    """An inline reference's link text is its overriding title (its inline
    content, formatted as Apple wrote it, else its plain text) when it carries
    one, else the target's title, never in code voice."""
    scraper = HIGDocsScraper()
    scraper.doc_dirs = {"swiftui": "SwiftUI"}
    references: Dict[str, Any] = {
        "doc://com.apple.HIG/design/Human-Interface-Guidelines/dark-mode": {
            "type": "topic", "title": "Dark Mode", "url": "/design/human-interface-guidelines/dark-mode"},
        "doc://com.apple.HIG/design/Human-Interface-Guidelines/materials": {
            "type": "topic", "title": "Materials", "url": "/design/human-interface-guidelines/materials"},
        "https://developer.apple.com/design/resources/": {
            "type": "link", "title": "Resources", "url": "https://developer.apple.com/design/resources/"},
        "doc://com.apple.documentation/documentation/SwiftUI/Button": {
            "type": "topic", "kind": "symbol", "role": "symbol", "title": "Button",
            "url": "/documentation/SwiftUI/Button"},
    }
    inline = [
        {"type": "text", "text": "Both light and "},
        {"type": "reference", "identifier": "doc://com.apple.HIG/design/Human-Interface-Guidelines/dark-mode",
         "isActive": True, "overridingTitle": "dark",
         "overridingTitleInlineContent": [{"type": "emphasis", "inlineContent": [{"type": "text", "text": "dark"}]}]},
        {"type": "text", "text": " use "},
        {"type": "reference", "identifier": "doc://com.apple.HIG/design/Human-Interface-Guidelines/materials",
         "isActive": True, "overridingTitle": "material"},
        {"type": "text", "text": "; see "},
        {"type": "reference", "identifier": "https://developer.apple.com/design/resources/", "isActive": True,
         "overridingTitle": "Apple Design Resources",
         "overridingTitleInlineContent": [{"type": "text", "text": "Apple Design Resources"}]},
        {"type": "text", "text": ", "},
        {"type": "reference", "identifier": "doc://com.apple.documentation/documentation/SwiftUI/Button",
         "isActive": True},
        {"type": "text", "text": " and "},
        {"type": "reference", "identifier": "doc://missing", "isActive": True, "overridingTitle": "the kit"},
        {"type": "text", "text": "."},
    ]
    assert scraper._extract_text_from_inline_content(inline, references) == (
        "Both light and [*dark*](dark-mode.md) use [material](materials.md); see "
        "[Apple Design Resources](https://developer.apple.com/design/resources/), [Button](../SwiftUI/button.md) "
        "and the kit.")


def test_links_into_apple_docs_use_the_apple_scrapers_path_rule() -> None:
    """A link to an Apple documentation page is its file under the Apple scraper's
    path rule, relative to the HIG file (quoted, its fragment kept), when its framework
    is a docs dir we have; else its Apple URL. HIG's own links stay as they are."""
    scraper = HIGDocsScraper()
    scraper.doc_dirs = {"swiftui": "SwiftUI", "xctest": "XCTest", "swift": "Swift"}
    scraper.current_url = f"{scrape_hig_docs.JSON_BASE_URL}/human-interface-guidelines/buttons.json"
    cases = {
        "/documentation/SwiftUI/View/padding(_:_:)": "../SwiftUI/view/padding%28_,_%29.md",
        "/documentation/swiftui/view#Overview": "../SwiftUI/view.md#Overview",
        "/documentation/xctest/xctest": "../XCTest/xctest-page.md",
        "/documentation/swift/comparable/'..<(_:_:)": "../Swift/comparable/dot._%28_,_%29.md",
        "/documentation/swiftui": "../SwiftUI/SwiftUI.md",
        "/documentation/otherkit/thing": "https://developer.apple.com/documentation/otherkit/thing",
        "/design/human-interface-guidelines/color#Best-practices": "color.md#Best-practices",
        "https://developer.apple.com/documentation/swiftui/view": "https://developer.apple.com/documentation/swiftui/view",
    }
    for link_url, link in cases.items():
        assert scraper._convert_url_to_local_path(link_url) == link, link_url


async def test_the_known_dirs_are_the_apple_hash_files(site: FakeUpstream) -> None:
    """The dirmap comes from the hash files next to HIG's: an Apple framework's name, never HIG's own file."""
    hashes = scrape_hig_docs.HASH_FILE.parent
    hashes.mkdir(parents=True, exist_ok=True)
    (hashes / "SwiftUI_hashes.json").write_text(json.dumps({"metadata": {}, "hashes": {
        "https://developer.apple.com/tutorials/data/documentation/swiftui/view.json": {"hash": "h"}}}))
    await run()
    scraper = HIGDocsScraper()
    assert scraper._link_dirs() == {"swiftui": "SwiftUI"}


async def test_a_new_render_version_renders_every_page_once(site: FakeUpstream,
                                                             monkeypatch: pytest.MonkeyPatch) -> None:
    await run()
    assert hash_file()["metadata"]["render"] == {"version": scrape_hig_docs.RENDER_VERSION}
    (scrape_hig_docs.OUTPUT_DIR / "a.md").write_text("# an older rendering\n")
    monkeypatch.setattr(scrape_hig_docs, "RENDER_VERSION", 2)
    scraper = await run()
    assert scraper.exit_code == 0 and scraper.stats["pages_scraped"] == len(ALL)
    assert "an older rendering" not in (scrape_hig_docs.OUTPUT_DIR / "a.md").read_text()
    assert hash_file()["metadata"]["render"] == {"version": 2}
    before = scrape_hig_docs.HASH_FILE.read_text()
    scraper = await run()
    assert scraper.stats["pages_scraped"] == 0 and scrape_hig_docs.HASH_FILE.read_text() == before


async def test_pages_the_storing_run_didnt_render_are_rendered_when_back(site: FakeUpstream,
                                                                         monkeypatch: pytest.MonkeyPatch) -> None:
    """The run that stores a new render version drops the hash of the pages it didn't produce
    (here files the valve holds), so they are rendered when they're linked again unchanged."""
    await run()
    for name in ALL:
        (scrape_hig_docs.OUTPUT_DIR / name).write_text("# an older rendering\n")
    monkeypatch.setattr(scrape_hig_docs, "RENDER_VERSION", 2)
    site.hig_page("", ROOT_TITLE, ("a",))  # 5 of 7 unlinked: held
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == ALL and len(hash_file()["metadata"]["pending_orphans"]) == 5
    assert hash_file()["metadata"]["render"] == {"version": 2}
    held = urls(site, ("b", "c", "c1", "d", "e"))
    entries = hash_file()["hashes"]
    assert {u for u, entry in entries.items() if entry["hash"] == ""} == held
    assert all(entries[u]["file_path"] for u in held)
    site.hig_page("", ROOT_TITLE, ROOT_LINKS)  # linked again, unchanged
    scraper = await run()
    assert scraper.exit_code == 0 and docs() == ALL and "pending_orphans" not in hash_file()["metadata"]
    assert not any("an older rendering" in (scrape_hig_docs.OUTPUT_DIR / name).read_text() for name in ALL)
    before = scrape_hig_docs.HASH_FILE.read_text()
    scraper = await run()
    assert scraper.stats["pages_scraped"] == 0 and scrape_hig_docs.HASH_FILE.read_text() == before


async def test_a_run_that_isnt_clean_keeps_the_stored_render_version(site: FakeUpstream,
                                                                     monkeypatch: pytest.MonkeyPatch) -> None:
    """A blocked run, and an interrupted one (its save keeps the stored metadata), store nothing;
    the next clean run renders every page and stores the version."""
    await run()
    monkeypatch.setattr(scrape_hig_docs, "RENDER_VERSION", 2)
    site.faults[site.hig_path("a")] = 502
    scraper = await run()
    assert scraper.exit_code == 1 and hash_file()["metadata"]["render"] == {"version": 1}
    del site.faults[site.hig_path("a")]

    def interrupted(self: HIGDocsScraper) -> None:
        raise RuntimeError("interrupted")

    log_unknown_content = HIGDocsScraper._log_unknown_content
    monkeypatch.setattr(HIGDocsScraper, "_log_unknown_content", interrupted)
    with pytest.raises(RuntimeError, match="interrupted"):
        await run()
    assert hash_file()["metadata"]["render"] == {"version": 1}
    monkeypatch.setattr(HIGDocsScraper, "_log_unknown_content", log_unknown_content)
    scraper = await run()
    assert scraper.stats["pages_scraped"] == len(ALL) and hash_file()["metadata"]["render"] == {"version": 2}


def paragraph(value: str) -> Dict[str, Any]:
    return {"type": "paragraph", "inlineContent": [{"type": "text", "text": value}]}


def test_paragraphs_stay_apart_in_every_container() -> None:
    """Each paragraph is a Markdown paragraph of its own (a blank line between
    them): at the top level, in a list item (indented under its marker), after
    a list, in a term's definition, and in a table cell on one line."""
    scraper = HIGDocsScraper()
    content = [
        paragraph("One."), paragraph("Two."),
        {"type": "unorderedList", "items": [{"content": [paragraph("Item."), paragraph("More.")]},
                                            {"content": [paragraph("Last.")]}]},
        paragraph("After the list."),
        {"type": "orderedList", "items": [{"content": [paragraph("First."), paragraph("Also.")]}]},
        {"type": "table", "header": "row", "rows": [
            [[paragraph("Name")], [paragraph("Use")]],
            [[paragraph("Cell.")], [paragraph("Line one."), paragraph("Line two.")]]]},
        {"type": "termList", "items": [
            {"term": {"inlineContent": [{"type": "text", "text": "A"}]},
             "definition": {"content": [paragraph("Def."), paragraph("Rest.")]}},
            {"term": {"inlineContent": [{"type": "text", "text": "B"}]},
             "definition": {"content": [paragraph("Other.")]}}]},
    ]
    assert scraper._convert_content_to_markdown(content, {}, 2) == (
        "One.\n\nTwo.\n\n"
        "- Item.\n\n  More.\n- Last.\n\n"
        "After the list.\n\n"
        "1. First.\n\n   Also.\n\n"
        "| Name | Use |\n| --- | --- |\n| Cell. | Line one. Line two. |\n\n"
        "**A**: Def.\n\nRest.\n\n**B**: Other.\n\n")


def test_a_page_has_one_blank_line_between_blocks() -> None:
    """Where blocks and the page's sections meet, one blank line, never more;
    a code listing's own blank lines stay."""
    scraper = HIGDocsScraper()
    data: Dict[str, Any] = {
        "metadata": {"title": "Buttons"},
        "abstract": [{"type": "text", "text": "Buttons start actions."}],
        "primaryContentSections": [{"kind": "content", "content": [
            {"type": "heading", "level": 2, "text": "Best practices"}, paragraph("Text."),
            {"type": "aside", "style": "note", "content": [paragraph("Aside.")]},
            {"type": "heading", "level": 2, "text": "Lists"},
            {"type": "unorderedList", "items": [{"content": [paragraph("Item.")]}]},
            {"type": "video", "identifier": "v.mp4"}, paragraph("Caption.")]}],
        "topicSections": [{"title": "Related", "identifiers": ["doc://t"]}],
        "references": {"doc://t": {"title": "Toggles", "url": "/design/human-interface-guidelines/toggles"},
                       "v.mp4": {"type": "video", "variants": [{"traits": ["1x", "light"], "url": "/videos/v.mp4"}]}},
    }
    md = scraper._extract_to_markdown(data, f"{scrape_hig_docs.JSON_BASE_URL}/human-interface-guidelines/buttons.json")
    assert "\n\n\n" not in md
    assert ("Buttons start actions.\n\n## Best practices\nText.\n\n> **Note:** Aside.\n\n## Lists\n- Item.\n\n"
            "[Video: v.mp4](https://developer.apple.com/tutorials/videos/v.mp4)\n\nCaption.\n\n## Topics\n\n"
            "### Related\n\n- [Toggles](toggles.md)\n\n---\n") in md
    listing = "\n```swift\na\n\n\nb\n```\n"
    assert scrape_hig_docs.join_parts(["Text.\n\n", listing, "\n## Next\n"]) == f"Text.\n{listing}\n## Next\n"


def test_a_tab_navigator_renders_every_tab_under_its_title() -> None:
    """Each tab: its title as a bold label, then its content (a heading, a
    table and the small print under it included); small print outside a tab
    is a paragraph too. Links in a tab are discovered."""
    scraper = HIGDocsScraper()
    small = {"type": "small", "inlineContent": [{"type": "text", "text": "Sizes in points."}]}
    content = [
        paragraph("Before."),
        {"type": "tabNavigator", "tabs": [
            {"title": "iOS", "content": [
                paragraph("Phone."), {"type": "heading", "level": 4, "text": "Sizes"},
                {"type": "table", "header": "row", "rows": [[[paragraph("Style")], [paragraph("Size")]],
                                                            [[paragraph("Body")], [paragraph("17")]]]},
                small]},
            {"title": "macOS", "content": [
                {"type": "row", "numberOfColumns": 1, "columns": [{"size": 1, "content": [paragraph("Mac.")]}]},
                {"type": "links", "style": "list", "items": ["doc://com.apple.HIG/design/Human-Interface-Guidelines/x"]}]},
            {"title": "Empty", "content": []}]},
        small, paragraph("After."),
    ]
    assert scraper._convert_content_to_markdown(content, {}, 2) == (
        "Before.\n\n**iOS**:\n\nPhone.\n\n#### Sizes\n"
        "| Style | Size |\n| --- | --- |\n| Body | 17 |\n\nSizes in points.\n\n"
        "**macOS**:\n\nMac.\n\nSizes in points.\n\nAfter.\n\n")
    data: Dict[str, Any] = {"primaryContentSections": [{"kind": "content", "content": content}]}
    assert scraper._extract_urls_from_json(data) == [f"{scrape_hig_docs.JSON_BASE_URL}/human-interface-guidelines/x.json"]
    assert not scraper.unknown_content


def test_a_links_abstract_stays_on_its_item_line() -> None:
    """A links abstract's line breaks (Apple's text has paragraphs) are spaces:
    its later lines can't continue the item or end the list."""
    scraper = HIGDocsScraper()
    references: Dict[str, Any] = {
        "doc://v1": {"title": "Session one", "url": "https://developer.apple.com/videos/play/wwdc2025/1",
                     "abstract": [{"type": "text", "text": "Explore it.\n\nTo get the most out of it, watch "},
                                  {"type": "emphasis", "inlineContent": [{"type": "text", "text": "Basics"}]},
                                  {"type": "text", "text": " first.\n"}]},
        "doc://v2": {"title": "Session two", "url": "https://developer.apple.com/videos/play/wwdc2025/2",
                     "abstract": [{"type": "text", "text": "Learn more."}]},
    }
    content = [{"type": "links", "style": "list", "items": ["doc://v1", "doc://v2"]}, paragraph("After.")]
    assert scraper._convert_content_to_markdown(content, references, 2) == (
        "- [Session one](https://developer.apple.com/videos/play/wwdc2025/1) - Explore it. To get the most out of it, "
        "watch *Basics* first.\n"
        "- [Session two](https://developer.apple.com/videos/play/wwdc2025/2) - Learn more.\n\nAfter.\n\n")


def test_unknown_content_is_rendered_as_its_text_and_warned(caplog: pytest.LogCaptureFixture) -> None:
    """A block or inline type or section kind the converter doesn't know is
    rendered as its text (its blocks as blocks, inline on one line), never
    dropped, and counted: one WARN per type at the end of the run, with the
    page it was first seen on. Strikethrough and a thematic break are known."""
    scraper = HIGDocsScraper()
    data: Dict[str, Any] = {
        "metadata": {"title": "Mystery"},
        "primaryContentSections": [
            {"kind": "content", "content": [
                {"type": "step", "content": [paragraph("Step text.")], "caption": [paragraph("Caption.")],
                 "media": "step.png", "code": ["let a = 1", "", "print(a)"]},
                {"type": "paragraph", "inlineContent": [
                    {"type": "text", "text": "A "},
                    {"type": "mystery", "inlineContent": [{"type": "text", "text": "term "}],
                     "content": [{"type": "unorderedList", "items": [{"content": [paragraph("x")]}]}]},
                    {"type": "strikethrough", "inlineContent": [{"type": "text", "text": "old"}]},
                    {"type": "text", "text": " and more."}]},
                {"type": "thematicBreak"},
                {"type": "step", "content": [paragraph("Again.")]}]},
            {"kind": "discussion", "content": [paragraph("Section text.")]}],
        "references": {},
    }
    url = f"{scrape_hig_docs.JSON_BASE_URL}/human-interface-guidelines/mystery.json"
    md = scraper._extract_to_markdown(data, url)
    assert ("Step text.\n\nCaption.\n\n```\nlet a = 1\n\nprint(a)\n```\n\n"
            "A term  - x ~~old~~ and more.\n\n---\n\nAgain.\n\nSection text.\n\n") in md
    assert dict(scraper.unknown_content) == {
        ("block type", "step"): 2, ("inline type", "mystery"): 1, ("section kind", "discussion"): 1}
    with caplog.at_level("WARNING", logger=scrape_hig_docs.logger.name):
        scraper._log_unknown_content()
    assert [r.getMessage() for r in caplog.records] == [
        f"unknown_content: block type 'step' x2, rendered as its text (e.g. {url})",
        f"unknown_content: inline type 'mystery' x1, rendered as its text (e.g. {url})",
        f"unknown_content: section kind 'discussion' x1, rendered as its text (e.g. {url})"]


def test_a_video_is_named_by_its_alt_text() -> None:
    scraper = HIGDocsScraper()
    references: Dict[str, Any] = {"clip.mp4": {"type": "video", "alt": "A person taps\nthe button.", "variants": [
        {"traits": ["1x", "light"], "url": "/videos/com.apple.HIG/clip.mp4"}]}}
    assert scraper._resolve_video("clip.mp4", references) == \
        "[Video: A person taps the button.](https://developer.apple.com/tutorials/videos/com.apple.HIG/clip.mp4)"
