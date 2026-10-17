#!/usr/bin/env python3
"""Swift scraper: configured-directory rules, failure policy and cleanup, over consecutive runs.

Each test runs the real scraper (aiohttp included) against a local fake
GitHub (fake_upstream.py: raw files and contents-API listings), in a
temporary docs dir and hash file. The config: org/book's Book/Guide (3 files,
one in a subdirectory) and Book/Reference (2), and org/site's docs/interop (2).
"""

import errno
import json
from pathlib import Path
from typing import Any, AsyncIterator, Dict, Set

import pytest

import scrape_swift_docs
import utilities.source_policy as source_policy
from fake_upstream import DROP, FakeUpstream, case_sensitive
from scrape_swift_docs import DocSource

FILES = {
    ("org/book", "Book/Guide/Basics.md"): "Guide/Basics.md",
    ("org/book", "Book/Guide/Closures.md"): "Guide/Closures.md",
    ("org/book", "Book/Guide/sub/Deep.md"): "Guide/sub/Deep.md",
    ("org/book", "Book/Reference/Types.md"): "Reference/Types.md",
    ("org/book", "Book/Reference/Statements.md"): "Reference/Statements.md",
    ("org/site", "docs/interop/A.md"): "Interop/A.md",
    ("org/site", "docs/interop/B.md"): "Interop/B.md",
}
ALL = set(FILES.values())
SOURCES = [
    DocSource(repo="org/book", branch="main", path="Book/Guide", output_subdir="Guide"),
    DocSource(repo="org/book", branch="main", path="Book/Reference", output_subdir="Reference"),
    DocSource(repo="org/site", branch="main", path="docs/interop", output_subdir="Interop"),
]


@pytest.fixture
async def site(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> AsyncIterator[FakeUpstream]:
    upstream = FakeUpstream()
    base = await upstream.start()
    monkeypatch.setattr(scrape_swift_docs, "OUTPUT_DIR", tmp_path / "documentation" / "Swift-Book")
    monkeypatch.setattr(scrape_swift_docs, "HASH_FILE", tmp_path / ".hashes" / "swift_docs_hashes.json")
    monkeypatch.setattr(scrape_swift_docs, "REQUEST_DELAY", 0)
    monkeypatch.setattr(scrape_swift_docs, "SOURCES", list(SOURCES))
    monkeypatch.setattr(source_policy, "GITHUB_RAW", f"{base}/raw")
    monkeypatch.setattr(source_policy, "GITHUB_API", f"{base}/api")
    monkeypatch.setattr(source_policy, "RETRY_BASE_DELAY", 0)
    for (repo, path), _ in FILES.items():
        upstream.github_file(repo, path, f"# {Path(path).stem}\n\nAbout {path}.\n")
    yield upstream
    await upstream.stop()


async def run(**kwargs: Any) -> int:
    stats = await scrape_swift_docs.scrape_all(**kwargs)
    return int(stats["exit_code"])


def docs() -> Set[str]:
    out = scrape_swift_docs.OUTPUT_DIR
    return {p.relative_to(out).as_posix() for p in out.rglob("*.md") if p.is_file()}


def hash_file() -> Dict[str, Any]:
    data: Dict[str, Any] = json.loads(scrape_swift_docs.HASH_FILE.read_text())
    return data


def metadata() -> Dict[str, Any]:
    result: Dict[str, Any] = hash_file()["metadata"]
    return result


def remove_upstream(site: FakeUpstream, repo: str, path: str) -> None:
    site.files.pop(site.raw_path(repo, path))


async def test_full_scrape(site: FakeUpstream) -> None:
    assert await run() == 0
    assert docs() == ALL
    assert set(hash_file()["hashes"]) == {f"{repo}:{path}" for repo, path in FILES}
    assert "failure_counts" not in metadata() and "pending_orphans" not in metadata()


async def test_configured_dir_404_x2_is_removed_while_other_removals_run(site: FakeUpstream) -> None:
    assert await run() == 0
    remove_upstream(site, "org/site", "docs/interop/A.md")
    remove_upstream(site, "org/site", "docs/interop/B.md")  # the listing now 404s
    remove_upstream(site, "org/book", "Book/Guide/Closures.md")  # a real removal elsewhere
    assert await run() == 0  # source_gone_pending: not an error
    assert docs() == ALL - {"Guide/Closures.md"}
    assert metadata()["failure_counts"] == {"org/site:docs/interop/": {"gone": 1}}
    assert "org/site:docs/interop/A.md" in hash_file()["hashes"]
    assert await run() == 0  # source_gone: deleted, keys pruned
    assert docs() == ALL - {"Guide/Closures.md", "Interop/A.md", "Interop/B.md"}
    assert not (scrape_swift_docs.OUTPUT_DIR / "Interop").exists()
    assert not any(key.startswith("org/site:") for key in hash_file()["hashes"])
    assert metadata()["failure_counts"] == {"org/site:docs/interop/": {"gone": 2}}
    before = scrape_swift_docs.HASH_FILE.read_text()
    assert await run() == 0  # still configured and gone: no churn
    assert scrape_swift_docs.HASH_FILE.read_text() == before


async def test_configured_dir_5xx_keeps_its_files_every_run(site: FakeUpstream) -> None:
    assert await run() == 0
    site.faults[site.api_path("org/site", "docs/interop")] = 503
    remove_upstream(site, "org/book", "Book/Guide/Closures.md")
    for run_number in range(4):
        assert await run() == 1, run_number  # source_fetch_failed
        assert docs() == ALL - {"Guide/Closures.md"}  # others still cleaned
    assert "org/site:docs/interop/A.md" in hash_file()["hashes"]
    site.faults.clear()
    assert await run() == 0


async def test_listed_subdirectory_failures(site: FakeUpstream) -> None:
    assert await run() == 0
    site.faults[site.api_path("org/book", "Book/Guide/sub")] = 502
    remove_upstream(site, "org/book", "Book/Reference/Statements.md")
    assert await run() == 1  # directory_fetch_failed: its files kept, the rest cleaned
    assert docs() == ALL - {"Reference/Statements.md"}
    site.faults[site.api_path("org/book", "Book/Guide/sub")] = 404  # gone: removed at once
    assert await run() == 0
    assert docs() == ALL - {"Reference/Statements.md", "Guide/sub/Deep.md"}


async def test_a_file_moved_into_a_new_subdirectory_that_fails_to_list(site: FakeUpstream) -> None:
    """The new subdirectory has nothing of ours to keep: its failure blocks the
    cleanup (never-good rule), so the moved file isn't deleted at its old path."""
    assert await run() == 0
    site.files[site.raw_path("org/book", "Book/Guide/newsub/Basics.md")] = site.files.pop(
        site.raw_path("org/book", "Book/Guide/Basics.md"))
    site.faults[site.api_path("org/book", "Book/Guide/newsub")] = 502
    for run_number in (1, 2):
        assert await run() == 1 and docs() == ALL
        assert metadata()["failure_counts"] == {"org/book:Book/Guide/newsub/": {"fail": run_number}}
    assert await run() == 1  # lifted at 3 (persistent_fetch_failure): the old path goes
    assert docs() == ALL - {"Guide/Basics.md"}
    site.faults.clear()
    assert await run() == 0
    assert docs() == (ALL - {"Guide/Basics.md"}) | {"Guide/newsub/Basics.md"}
    assert "failure_counts" not in metadata()


async def test_a_listed_file_404_is_removed_at_once(site: FakeUpstream) -> None:
    assert await run() == 0
    site.faults[site.raw_path("org/book", "Book/Guide/Basics.md")] = 404
    assert await run() == 0
    assert docs() == ALL - {"Guide/Basics.md"}
    assert "org/book:Book/Guide/Basics.md" not in hash_file()["hashes"]


@pytest.mark.parametrize("name", ["New.md", "basics.md"])
async def test_a_new_file_4xx_does_not_block(site: FakeUpstream, name: str) -> None:
    """A newly listed file answering 403 is one we never had (no key, no file
    under exactly its name): it doesn't block, and a real removal in the same
    run is deleted. basics.md is Basics.md's case twin, whose file a
    case-insensitive filesystem also reports under basics.md's name."""
    assert await run() == 0
    site.github_file("org/book", f"Book/Guide/{name}", "# New\n")
    site.faults[site.raw_path("org/book", f"Book/Guide/{name}")] = 403
    remove_upstream(site, "org/book", "Book/Reference/Types.md")
    assert await run() == 0
    assert docs() == ALL - {"Reference/Types.md"}
    assert f"org/book:Book/Guide/{name}" not in hash_file()["hashes"] and "failure_counts" not in metadata()


async def test_a_case_only_rename_upstream(site: FakeUpstream, tmp_path: Path) -> None:
    assert await run() == 0
    site.files[site.raw_path("org/book", "Book/Guide/basics.md")] = site.files.pop(
        site.raw_path("org/book", "Book/Guide/Basics.md"))
    assert await run() == 0
    keys = set(hash_file()["hashes"])
    assert "org/book:Book/Guide/basics.md" in keys
    if case_sensitive(tmp_path):
        # Written next to the old file (CI): the old one is deleted, its key pruned
        assert docs() == ALL - {"Guide/Basics.md"} | {"Guide/basics.md"}
        assert "org/book:Book/Guide/Basics.md" not in keys
    else:
        # Written into the old file, which keeps its name (macOS)
        assert docs() == ALL
    before = scrape_swift_docs.HASH_FILE.read_text()
    assert await run() == 0 and scrape_swift_docs.HASH_FILE.read_text() == before


async def test_a_good_file_failing_3_runs_is_removed_at_run_3(site: FakeUpstream) -> None:
    assert await run() == 0
    site.faults[site.raw_path("org/book", "Book/Guide/Basics.md")] = 502
    remove_upstream(site, "org/book", "Book/Reference/Types.md")
    for run_number in (1, 2):
        assert await run() == 1
        assert docs() == ALL  # blocked
        assert metadata()["failure_counts"] == {"org/book:Book/Guide/Basics.md": {"fail": run_number}}
    assert await run() == 1  # D8
    assert docs() == ALL - {"Guide/Basics.md", "Reference/Types.md"}
    site.faults.clear()
    assert await run() == 0
    assert docs() == ALL - {"Reference/Types.md"} and "failure_counts" not in metadata()


@pytest.mark.parametrize("loss", ["deleted", "unreadable"])
async def test_a_file_we_have_is_protected_after_the_hash_file_is_lost(site: FakeUpstream, loss: str) -> None:
    """A lost hash file loses keys, not files: a 403 on a file on disk still
    takes D8's 3 runs, as Apple's lost entries do."""
    assert await run() == 0
    if loss == "deleted":
        scrape_swift_docs.HASH_FILE.unlink()
    else:
        scrape_swift_docs.HASH_FILE.write_text("{not json")
    site.faults[site.raw_path("org/book", "Book/Guide/Basics.md")] = 403
    for run_number in (1, 2):
        assert await run() == 1 and docs() == ALL, run_number  # kept and blocking
        assert metadata()["failure_counts"] == {"org/book:Book/Guide/Basics.md": {"fail": run_number}}
    assert await run() == 1  # D8
    assert docs() == ALL - {"Guide/Basics.md"}
    site.faults.clear()
    assert await run() == 0 and docs() == ALL and "failure_counts" not in metadata()


async def test_a_write_failing_part_way_keeps_the_old_doc_whole(site: FakeUpstream,
                                                                monkeypatch: pytest.MonkeyPatch) -> None:
    """Doc writes are atomic: a write that fails part way (disk full) leaves
    the old doc as it was (kept as a local error), and no temp file."""
    assert await run() == 0
    doc = scrape_swift_docs.OUTPUT_DIR / "Guide/Basics.md"
    original = doc.read_text()
    site.github_file("org/book", "Book/Guide/Basics.md", "# Basics\n\nChanged.\n")
    write_text = Path.write_text

    def disk_full(self: Path, data: str, *args: Any, **kwargs: Any) -> int:
        if self.name.startswith("Basics.md"):
            write_text(self, data[:10], *args, **kwargs)
            raise OSError(errno.ENOSPC, "No space left on device")
        return write_text(self, data, *args, **kwargs)

    monkeypatch.setattr(Path, "write_text", disk_full)
    assert await run() == 1 and docs() == ALL
    assert doc.read_text() == original
    assert not list(scrape_swift_docs.OUTPUT_DIR.rglob("*.tmp"))
    assert metadata()["failure_counts"] == {"org/book:Book/Guide/Basics.md": {"local": 1}}
    monkeypatch.setattr(Path, "write_text", write_text)
    assert await run() == 0 and "Changed" in doc.read_text()


async def test_d8_needs_3_failed_fetches_in_a_row(site: FakeUpstream) -> None:
    """Basics fails on odd runs, and its configured dir on even runs, when
    Basics isn't fetched: it never fails 2 runs in a row, so D8 never removes it."""
    assert await run() == 0
    basics = site.raw_path("org/book", "Book/Guide/Basics.md")
    for run_number in range(1, 8):
        site.faults.clear()
        site.faults[basics if run_number % 2 else site.api_path("org/book", "Book/Guide")] = 502
        assert await run() == 1 and docs() == ALL, run_number
        expected = {"org/book:Book/Guide/Basics.md": {"fail": 1}} if run_number % 2 else {}
        assert metadata().get("failure_counts", {}) == expected, run_number
    site.faults.clear()
    assert await run() == 0 and docs() == ALL and "failure_counts" not in metadata()


async def test_network_errors_are_retried_then_block(site: FakeUpstream) -> None:
    assert await run() == 0
    site.flaky[site.api_path("org/book", "Book/Guide")] = [502, DROP, 503]
    assert await run() == 0 and docs() == ALL
    site.faults[site.raw_path("org/book", "Book/Guide/Basics.md")] = DROP
    remove_upstream(site, "org/book", "Book/Reference/Types.md")
    assert await run() == 1 and docs() == ALL


async def test_a_convert_error_x3_keeps_the_file(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    assert await run() == 0
    site.github_file("org/book", "Book/Guide/Basics.md", "# Basics\n\nChanged.\n")
    remove_upstream(site, "org/book", "Book/Reference/Types.md")
    clean = scrape_swift_docs.clean_docc_content

    def failing_clean(content: str, filename: str) -> str:
        if filename == "Basics.md":
            raise RuntimeError("converter bug")
        return clean(content, filename)

    monkeypatch.setattr(scrape_swift_docs, "clean_docc_content", failing_clean)
    for run_number in (1, 2):
        assert await run() == 1 and docs() == ALL
        assert metadata()["failure_counts"] == {"org/book:Book/Guide/Basics.md": {"local": run_number}}
    assert await run() == 1  # persistent_local_error: no longer blocking, the file kept
    assert docs() == ALL - {"Reference/Types.md"}
    assert "Changed" not in (scrape_swift_docs.OUTPUT_DIR / "Guide/Basics.md").read_text()
    monkeypatch.setattr(scrape_swift_docs, "clean_docc_content", clean)
    assert await run() == 0
    assert "Changed" in (scrape_swift_docs.OUTPUT_DIR / "Guide/Basics.md").read_text()
    assert "failure_counts" not in metadata()


async def test_a_local_count_waits_while_blocked_and_goes_with_its_file(site: FakeUpstream,
                                                                        monkeypatch: pytest.MonkeyPatch) -> None:
    """A file that failed to convert is then removed upstream: a blocked run
    that doesn't list it neither counts nor ends its local errors (its file is
    kept too); the next clean run deletes the file, and the count goes with it."""
    assert await run() == 0
    site.github_file("org/book", "Book/Guide/Basics.md", "# Basics\n\nChanged.\n")
    clean = scrape_swift_docs.clean_docc_content

    def failing_clean(content: str, filename: str) -> str:
        if filename == "Basics.md":
            raise RuntimeError("converter bug")
        return clean(content, filename)

    monkeypatch.setattr(scrape_swift_docs, "clean_docc_content", failing_clean)
    assert await run() == 1
    remove_upstream(site, "org/book", "Book/Guide/Basics.md")
    site.faults[site.raw_path("org/book", "Book/Reference/Types.md")] = 502  # blocks the cleanup
    assert await run() == 1 and docs() == ALL
    assert metadata()["failure_counts"] == {"org/book:Book/Guide/Basics.md": {"local": 1},
                                            "org/book:Book/Reference/Types.md": {"fail": 1}}
    site.faults.clear()
    assert await run() == 0 and docs() == ALL - {"Guide/Basics.md"}
    assert "org/book:Book/Guide/Basics.md" not in hash_file()["hashes"] and "failure_counts" not in metadata()


async def test_mass_removal_and_quiet_runs(site: FakeUpstream) -> None:
    assert await run() == 0
    # 4 of 7 gone from the listings (every configured dir keeps a file, so no listing 404s)
    gone = [("org/book", "Book/Guide/Basics.md"), ("org/book", "Book/Guide/Closures.md"),
            ("org/book", "Book/Reference/Types.md"), ("org/site", "docs/interop/A.md")]
    for repo, path in gone:
        remove_upstream(site, repo, path)
    assert await run() == 0  # held; nothing downloaded or deleted, the list still saved
    assert docs() == ALL
    assert metadata()["pending_orphans"] == sorted(f"Swift-Book/{FILES[key]}" for key in gone)
    site.faults[site.raw_path("org/site", "docs/interop/B.md")] = 500  # a blocked quiet run keeps the list
    assert await run() == 1
    assert len(metadata()["pending_orphans"]) == 4
    site.faults.clear()
    assert await run() == 0  # confirmed
    assert docs() == ALL - {FILES[key] for key in gone}
    assert "pending_orphans" not in metadata()


async def test_two_configured_dirs_gone_go_through_the_valve(site: FakeUpstream) -> None:
    assert await run() == 0
    for repo, path in list(FILES)[:5]:  # Guide and Reference gone: 5 of 7
        remove_upstream(site, repo, path)
    assert await run() == 0 and docs() == ALL  # source_gone_pending x2
    assert await run() == 0 and docs() == ALL  # source_gone x2: held by the valve
    assert len(metadata()["pending_orphans"]) == 5
    assert await run() == 0  # confirmed
    assert docs() == {"Interop/A.md", "Interop/B.md"}


async def test_a_source_removed_from_the_config_is_cleaned(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    assert await run() == 0
    monkeypatch.setattr(scrape_swift_docs, "SOURCES", SOURCES[:2])
    assert await run() == 0
    assert docs() == ALL - {"Interop/A.md", "Interop/B.md"}
    assert not any(key.startswith("org/site:") for key in hash_file()["hashes"])


def test_main_exit_codes(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("sys.argv", ["scrape_swift_docs.py"])

    async def returns(code: int) -> Dict[str, Any]:
        return {"exit_code": code}

    for code in (0, 1):
        monkeypatch.setattr(scrape_swift_docs, "scrape_all", lambda code=code, **_: returns(code))
        assert scrape_swift_docs.main() == code

    async def raises(error: BaseException) -> Dict[str, Any]:
        raise error

    monkeypatch.setattr(scrape_swift_docs, "scrape_all", lambda **_: raises(KeyboardInterrupt()))
    assert scrape_swift_docs.main() == 130
    monkeypatch.setattr(scrape_swift_docs, "scrape_all", lambda **_: raises(RuntimeError("bug")))
    assert scrape_swift_docs.main() == 1
