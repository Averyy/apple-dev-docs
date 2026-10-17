#!/usr/bin/env python3
"""Tests for HashManager content change detection."""

import errno
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any
from unittest import mock

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scraper.utils.hash_manager import HashManager, write_text_atomic


def test_new_url_is_changed():
    """New URLs should always be detected as changed."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        hm = HashManager(Path(f.name))

    assert hm.has_changed("https://example.com/new", "content") is True
    print("PASS: new_url_is_changed")


def test_same_etag_unchanged():
    """Same ETag should be detected as unchanged."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        hm = HashManager(Path(f.name))

    url = "https://example.com/page"
    hm.update_hash(url, "content", etag="W/\"abc123\"")

    assert hm.has_changed(url, "content", etag="W/\"abc123\"") is False
    print("PASS: same_etag_unchanged")


def test_different_etag_different_content_is_changed():
    """Different ETag AND different content should be detected as changed."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        hm = HashManager(Path(f.name))

    url = "https://example.com/page"
    hm.update_hash(url, "old content", etag="W/\"old_etag\"")

    assert hm.has_changed(url, "new content", etag="W/\"new_etag\"") is True
    print("PASS: different_etag_different_content_is_changed")


def test_different_etag_same_content_is_unchanged():
    """Different ETag but same content should be detected as UNCHANGED.

    This is the critical fix: Apple can regenerate ETags during CDN redeployments
    without changing any actual content. The scraper must fall through to hash
    comparison instead of trusting ETag changes blindly.
    """
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        hm = HashManager(Path(f.name))

    url = "https://example.com/page"
    content = '{"identifier":{"url":"/documentation/swiftui/text"}}'

    hm.update_hash(url, content, etag="W/\"old_etag\"")

    # Same content, different ETag (CDN regenerated ETags)
    assert hm.has_changed(url, content, etag="W/\"new_etag\"") is False
    print("PASS: different_etag_same_content_is_unchanged")


def test_no_etag_uses_hash():
    """When no ETag is available, hash comparison should work."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        hm = HashManager(Path(f.name))

    url = "https://example.com/page"
    hm.update_hash(url, "content", etag=None)

    assert hm.has_changed(url, "content", etag=None) is False
    assert hm.has_changed(url, "different content", etag=None) is True
    print("PASS: no_etag_uses_hash")


def test_etag_updated_after_regeneration():
    """After ETag regeneration, the new ETag should be stored via update_hash.

    Simulates the full flow: ETag changes, hash says unchanged, code calls
    update_hash with new ETag. Next check with new ETag should be fast (ETag match).
    """
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        hm = HashManager(Path(f.name))

    url = "https://example.com/page"
    content = "same content throughout"

    # Initial scrape
    hm.update_hash(url, content, etag="W/\"etag_v1\"")

    # Apple regenerates ETags — has_changed falls through to hash, returns False
    assert hm.has_changed(url, content, etag="W/\"etag_v2\"") is False

    # Simulate what json_scraper does on the unchanged path: update_hash with new ETag
    hm.update_hash(url, content, etag="W/\"etag_v2\"")

    # Next run: ETag matches, fast path
    assert hm.has_changed(url, content, etag="W/\"etag_v2\"") is False
    print("PASS: etag_updated_after_regeneration")


def test_metadata_is_preserved_across_save_and_load() -> None:
    """Nested metadata survives load and save; the per-run keys are rewritten."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        cache.write_text(json.dumps({
            "metadata": {
                "last_updated": "old", "total_pages": 99, "session_id": "old",
                "root_gone_runs": 1, "failure_storm_runs": 2, "pending_orphans": ["a.md"],
            },
            "hashes": {"u": {"hash": "h", "file_path": "documentation/fw/u.md"}},
        }))
        hm = HashManager(cache)
        assert hm.metadata == {"root_gone_runs": 1, "failure_storm_runs": 2, "pending_orphans": ["a.md"]}
        hm.touch("u")
        hm.save()
        metadata = json.loads(cache.read_text())["metadata"]
        assert list(metadata) == [
            "last_updated", "total_pages", "session_id", "root_gone_runs", "failure_storm_runs", "pending_orphans",
        ]
        assert metadata["session_id"] == hm.session_id
        assert metadata["total_pages"] == 1
        assert HashManager(cache).metadata == hm.metadata
    print("PASS: metadata_is_preserved_across_save_and_load")


def test_set_metadata_marks_modified_and_drops_falsy() -> None:
    """Every metadata change is saved, even on a run that changed nothing else."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        hm = HashManager(cache)
        hm.hashes["u"] = {"hash": "h", "file_path": "documentation/fw/u.md"}
        hm.save()  # not modified: nothing written
        assert not cache.exists()
        hm.set_metadata("failure_storm_runs", 1)
        hm.save()
        assert json.loads(cache.read_text())["metadata"]["failure_storm_runs"] == 1
        saved = cache.read_text()
        reloaded = HashManager(cache)
        reloaded.set_metadata("failure_storm_runs", 1)  # unchanged: not modified, not rewritten
        reloaded.save()
        assert cache.read_text() == saved
        reloaded.set_metadata("failure_storm_runs", 0)
        reloaded.save()
        assert "failure_storm_runs" not in json.loads(cache.read_text())["metadata"]
    print("PASS: set_metadata_marks_modified_and_drops_falsy")


def test_counters_survive_update_hash_mark_error_and_save() -> None:
    """Run counters are carried over by update_hash and mark_error, and persisted."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        hm = HashManager(cache)
        hm.update_hash("u", "content", etag="E1", file_path=Path("documentation/fw/u.md"))
        hm.set_counter("u", "consecutive_failures", 2)
        hm.set_counter("u", "consecutive_local_errors", 1)
        hm.update_hash("u", "new content", etag="E2", file_path=Path("documentation/fw/u.md"))
        assert hm.hashes["u"]["consecutive_failures"] == 2
        assert hm.hashes["u"]["consecutive_local_errors"] == 1
        hm.mark_error("u", "HTTP 502")
        entry = hm.hashes["u"]
        assert entry["status"] == "error" and "file_path" not in entry and "etag" not in entry
        assert entry["consecutive_failures"] == 2 and entry["consecutive_local_errors"] == 1
        hm.save()
        reloaded = HashManager(cache)
        assert reloaded.get_counter("u", "consecutive_failures") == 2
        assert reloaded.get_counter("missing", "consecutive_failures") == 0
        reloaded.set_counter("u", "consecutive_failures", 0)
        assert "consecutive_failures" not in reloaded.hashes["u"]
        reloaded.set_counter("missing", "consecutive_failures", 0)  # no entry, nothing to drop
        assert "missing" not in reloaded.hashes
    print("PASS: counters_survive_update_hash_mark_error_and_save")


def test_touch_refreshes_only_the_session() -> None:
    """touch keeps hash, etag and file_path, refreshing session_id and last_checked."""
    with tempfile.TemporaryDirectory() as d:
        hm = HashManager(Path(d) / "fw_hashes.json")
        hm.hashes["u"] = {
            "hash": "h", "last_checked": "old", "status": "unchanged", "session_id": "old",
            "etag": "E", "file_path": "documentation/fw/u.md",
        }
        hm.touch("u")
        assert hm.hashes["u"]["session_id"] == hm.session_id
        assert hm.hashes["u"]["last_checked"] != "old"
        assert {k: hm.hashes["u"][k] for k in ("hash", "status", "etag", "file_path")} == {
            "hash": "h", "status": "unchanged", "etag": "E", "file_path": "documentation/fw/u.md",
        }
        hm.save()
        assert json.loads(hm.cache_file.read_text())["hashes"]["u"]["session_id"] == hm.session_id
    print("PASS: touch_refreshes_only_the_session")


def test_keep_file_records_a_file_on_disk_only() -> None:
    """keep_file re-records a file on disk on an error entry, keeping its counters."""
    with tempfile.TemporaryDirectory() as d:
        hm = HashManager(Path(d) / "fw_hashes.json")
        page = Path(d) / "fw" / "Page.md"
        hm.mark_error("u", "HTTP 502")
        hm.set_counter("u", "consecutive_failures", 3)
        before = dict(hm.hashes["u"])
        assert hm.keep_file("u", page) is False  # not on disk: nothing changes
        assert hm.hashes["u"] == before
        page.parent.mkdir()
        page.write_text("# page\n")
        # A recorded casing that drifted from the disk's is found too
        assert hm.keep_file("v", page.with_name("page.md")) is True
        assert hm.keep_file("u", page) is True
        entry = hm.hashes["u"]
        assert entry["file_path"] == str(page)
        assert entry["status"] == "unchanged" and entry["hash"] == "" and "etag" not in entry
        assert entry["session_id"] == hm.session_id and entry["consecutive_failures"] == 3
        assert hm.hashes["v"]["status"] == "new"
        # The next run refetches it without an etag and converts it again
        assert hm.has_changed("u", "content") is True and hm.get_etag("u") is None
        del hm.hashes["v"]
        hm.save()
        assert hm.get_orphaned_files(page.parent) == []
    print("PASS: keep_file_records_a_file_on_disk_only")


def test_a_path_that_cant_be_checked_counts_as_missing() -> None:
    """A file name over the filesystem's limit (255 bytes) makes stat raise: missing, and nothing raises."""
    with tempfile.TemporaryDirectory() as d:
        hm = HashManager(Path(d) / "fw_hashes.json")
        page = Path(d) / "fw" / ("a" * 300 + ".md")
        page.parent.mkdir()
        (page.parent / "other.md").write_text("# other\n")
        hm.mark_error("u", "local error: File name too long")
        hm.set_counter("u", "consecutive_local_errors", 1)
        before = dict(hm.hashes["u"])
        assert hm.keep_file("u", page) is False  # nothing changes: the URL keeps its counted error entry
        assert hm.hashes["u"] == before
        # An entry that records such a path: refetched without an etag and converted again
        hm.hashes["v"] = {"hash": "h", "status": "unchanged", "etag": "E", "file_path": str(page)}
        assert hm.get_etag("v") is None
        assert hm.has_changed("v", "content", etag="E") is True
        assert hm.prune_missing_files() == 1 and "v" not in hm.hashes
        # Orphan detection checks a touched entry's path without raising
        hm.hashes["w"] = {"hash": "h", "status": "unchanged", "session_id": hm.session_id, "file_path": str(page)}
        assert hm.get_orphaned_files(page.parent) == [page.parent / "other.md"]
    print("PASS: a_path_that_cant_be_checked_counts_as_missing")


def test_a_dir_that_cant_be_listed_keeps_its_entries() -> None:
    """No permission on a page's dir: whether its file exists can't be told, and nothing raises.

    keep_file doesn't vouch for it, but its entry isn't missing: the etag is
    still sent and prune keeps the entry (and its counters).
    """
    if hasattr(os, "geteuid") and os.geteuid() == 0:
        print("SKIP: a_dir_that_cant_be_listed_keeps_its_entries (root ignores file permissions)")
        return
    with tempfile.TemporaryDirectory() as d:
        hm = HashManager(Path(d) / "fw_hashes.json")
        locked = Path(d) / "fw" / "page"
        locked.mkdir(parents=True)
        page = locked / "child.md"
        page.write_text("# child\n")
        hm.hashes["u"] = {"hash": hm.get_content_hash("content"), "status": "unchanged", "etag": "E",
                          "session_id": hm.session_id, "file_path": str(page), "consecutive_local_errors": 2}
        hm.mark_error("v", "HTTP 502")
        locked.chmod(0)
        try:
            assert hm.get_etag("u") == "E"
            assert hm.has_changed("u", "content", etag="E") is False
            assert hm.prune_missing_files() == 0 and hm.hashes["u"]["consecutive_local_errors"] == 2
            before = dict(hm.hashes["v"])
            assert hm.keep_file("v", page) is False and hm.hashes["v"] == before
            hm.save()
            assert hm.get_orphaned_files(Path(d) / "fw") == []
        finally:
            locked.chmod(0o755)
    print("PASS: a_dir_that_cant_be_listed_keeps_its_entries")


def test_save_skips_a_manager_with_nothing_to_keep() -> None:
    """No file_path, no counter and no metadata beyond root_gone_runs: nothing is written."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        hm = HashManager(cache)
        hm.mark_error("root", "HTTP 404")
        hm.set_metadata("root_gone_runs", 1)
        hm.save()
        assert not cache.exists()

        # Any of these is worth saving
        for keep in ("file_path", "counter", "metadata"):
            hm = HashManager(cache)
            hm.mark_error("root", "HTTP 404")
            hm.set_metadata("root_gone_runs", 1)
            if keep == "file_path":
                hm.update_hash("page", "content", file_path=Path("documentation/fw/page.md"))
            elif keep == "counter":
                hm.set_counter("root", "consecutive_failures", 1)
            else:
                hm.set_metadata("index_roots", ["x"])
            hm.save()
            assert cache.exists(), keep
            cache.unlink()
    print("PASS: save_skips_a_manager_with_nothing_to_keep")


def test_nothing_worth_saving_is_written_while_the_file_or_dir_exists() -> None:
    """The skip only stops a hash file being created; one on disk, or the output dir, gets every change."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        output_dir = Path(d) / "documentation" / "fw"

        # Neither exists (e.g. after a root-gone removal): nothing is written
        hm = HashManager(cache, output_dir)
        hm.mark_error("root", "HTTP 404")
        hm.set_metadata("root_gone_runs", 1)
        assert hm.save() is True
        assert not cache.exists()

        # The output dir exists, in any casing, e.g. a hash file lost next to its docs
        (Path(d) / "documentation" / "FW").mkdir(parents=True)
        hm = HashManager(cache, output_dir)
        hm.mark_error("root", "HTTP 404")
        hm.set_metadata("root_gone_runs", 1)
        assert hm.save() is True
        assert json.loads(cache.read_text())["metadata"]["root_gone_runs"] == 1
        (Path(d) / "documentation" / "FW").rmdir()

        # The cache file exists: each run's count is written, though no entry has a file_path
        for runs in (2, 3):
            hm = HashManager(cache, output_dir)
            assert set(hm.hashes) == {"root"} and "file_path" not in hm.hashes["root"]
            hm.set_metadata("root_gone_runs", hm.get_metadata("root_gone_runs") + 1)
            assert hm.save() is True
            assert json.loads(cache.read_text())["metadata"]["root_gone_runs"] == runs

        # A prune of the last files is written too
        hm = HashManager(cache)
        hm.update_hash("page", "content", file_path=Path(d) / "gone.md")
        hm.save()
        hm = HashManager(cache)
        assert hm.prune_missing_files() == 1
        assert hm.save() is True
        assert "page" not in json.loads(cache.read_text())["hashes"]
    print("PASS: nothing_worth_saving_is_written_while_the_file_or_dir_exists")


def test_a_failed_save_is_reported_and_keeps_the_previous_file() -> None:
    """A save that fails returns False and leaves the previous file whole, with no temp file.

    The manager stays modified, so a later save still writes the changes.
    """
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        hm = HashManager(cache)
        assert hm.save() is True  # nothing to save
        hm.update_hash("u", "content", file_path=Path("documentation/fw/u.md"))
        assert hm.save() is True
        saved = cache.read_text()
        hm.update_hash("v", "content", file_path=Path("documentation/fw/v.md"))

        def dump_until_the_disk_is_full(obj: Any, f: Any, **kwargs: Any) -> None:
            f.write(json.dumps(obj, **kwargs)[:100])
            raise OSError(errno.ENOSPC, "No space left on device")

        # The disk fills up part way through the write
        with mock.patch.object(json, "dump", dump_until_the_disk_is_full):
            assert hm.save() is False
        assert cache.read_text() == saved
        assert sorted(p.name for p in Path(d).iterdir()) == [cache.name]

        # No permission to create the temp file in the hash dir
        if not (hasattr(os, "geteuid") and os.geteuid() == 0):
            Path(d).chmod(0o555)
            try:
                assert hm.save() is False
            finally:
                Path(d).chmod(0o755)
            assert cache.read_text() == saved

        assert hm.save() is True
        assert set(json.loads(cache.read_text())["hashes"]) == {"u", "v"}
        assert sorted(p.name for p in Path(d).iterdir()) == [cache.name]
    print("PASS: a_failed_save_is_reported_and_keeps_the_previous_file")


def test_a_file_that_fails_to_load_is_replaced_by_the_next_save() -> None:
    """A cache file that exists but loads nothing sets load_error, and the next save replaces it.

    Even a manager holding nothing worth saving writes, or the file would fail
    to load on every run.
    """
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        hm = HashManager(cache)
        hm.update_hash("u", "content", file_path=Path("documentation/fw/u.md"))
        hm.set_metadata("failure_storm_runs", 1)
        hm.save()
        text = cache.read_text()
        broken = {
            "truncated": text[: len(text) // 2].encode(),
            "conflict marker": b"<<<<<<< HEAD\n" + text.encode(),
            "not utf-8": b"\xff" + text.encode(),
            "not an object": b"[]",
            "hashes not an object": b'{"hashes": []}',
            "metadata not an object": b'{"metadata": null, "hashes": {}}',
        }
        for how, content in broken.items():
            cache.write_bytes(content)
            hm = HashManager(cache)
            assert hm.load_error, how
            assert hm.hashes == {} and hm.metadata == {}, how
            hm.mark_error("root", "HTTP 404")
            hm.set_metadata("root_gone_runs", 1)
            assert hm.save() is True, how
            reloaded = HashManager(cache)
            assert reloaded.load_error is None, how
            assert reloaded.metadata == {"root_gone_runs": 1}, how
            assert set(reloaded.hashes) == {"root"}, how

        # A run that changes nothing still replaces it
        cache.write_bytes(broken["truncated"])
        assert HashManager(cache).save() is True
        assert HashManager(cache).load_error is None

        # A file we may not read (root can read it anyway)
        if not (hasattr(os, "geteuid") and os.geteuid() == 0):
            cache.chmod(0o000)
            try:
                hm = HashManager(cache)
                assert hm.load_error and hm.hashes == {}
                assert hm.save() is True
            finally:
                cache.chmod(0o644)
            assert HashManager(cache).load_error is None

        # No file, or the other hash files the cleanup scripts read: no error
        cache.unlink()
        hm = HashManager(cache)
        assert hm.load_error is None
        hm.save()
        assert not cache.exists()
        for other in (
            {"metadata": {"source": "x"}, "hashes": {"docs/a.md": "digest"}},  # MLX / Swift
            {"https://developer.apple.com/tutorials/data/design/a.json": {"hash": "h"}},  # HIG
        ):
            cache.write_text(json.dumps(other))
            assert HashManager(cache).load_error is None
    print("PASS: a_file_that_fails_to_load_is_replaced_by_the_next_save")


def test_write_text_atomic_writes_whole_or_not_at_all() -> None:
    """A doc write that fails part way (disk full) keeps the old file, with no temp file left."""
    with tempfile.TemporaryDirectory() as d:
        doc = Path(d) / "page.md"
        write_text_atomic(doc, "# old\n")
        write_text_atomic(doc, "# new ü\n")
        assert doc.read_text(encoding="utf-8") == "# new ü\n"
        write_text = Path.write_text

        def disk_full(path: Path, data: str, *args: Any, **kwargs: Any) -> int:
            write_text(path, data[:3], *args, **kwargs)
            raise OSError(errno.ENOSPC, "No space left on device")

        with mock.patch.object(Path, "write_text", disk_full):
            try:
                write_text_atomic(doc, "# newer\n")
            except OSError:
                pass
            else:
                raise AssertionError("the failed write didn't raise")
        assert doc.read_text(encoding="utf-8") == "# new ü\n"
        assert sorted(p.name for p in Path(d).iterdir()) == ["page.md"]
        # A name with no room for the ".tmp" suffix gets a short temp name
        long_doc = Path(d) / ("a" * 250 + ".md")
        write_text_atomic(long_doc, "# long\n")
        assert long_doc.read_text() == "# long\n"
        assert sorted(p.name for p in Path(d).iterdir()) == sorted([long_doc.name, "page.md"])
    print("PASS: write_text_atomic_writes_whole_or_not_at_all")


def test_a_partial_run_marks_its_save_only_when_it_writes() -> None:
    """mark_partial sets metadata.partial_session only on a manager whose save writes anyway."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        hm = HashManager(cache)
        hm.update_hash("u", "content", file_path=Path("documentation/fw/u.md"))
        assert hm.save() is True
        before = cache.read_text()
        quiet = HashManager(cache)
        quiet.mark_partial()  # nothing changed: nothing to write
        assert quiet.save() is True and cache.read_text() == before
        assert not HashManager(cache).partial
        busy = HashManager(cache)
        busy.touch("u")
        busy.mark_partial()
        assert busy.save() is True
        reloaded = HashManager(cache)
        assert reloaded.partial and reloaded.get_metadata("partial_session") == busy.session_id
        reloaded.set_metadata("partial_session", None)  # a run that finishes unblocked drops it
        assert reloaded.save() is True and not HashManager(cache).partial

        # The mark never makes a manager worth saving: a removed framework
        # (no hash file, no docs dir) still writes nothing
        gone = HashManager(Path(d) / "gone_hashes.json", Path(d) / "gone")
        gone.mark_error("root", "HTTP 404")
        gone.mark_partial()
        assert gone.save() is True and not (Path(d) / "gone_hashes.json").exists()
    print("PASS: a_partial_run_marks_its_save_only_when_it_writes")


def main():
    tests = [
        test_new_url_is_changed,
        test_same_etag_unchanged,
        test_different_etag_different_content_is_changed,
        test_different_etag_same_content_is_unchanged,
        test_no_etag_uses_hash,
        test_etag_updated_after_regeneration,
        test_metadata_is_preserved_across_save_and_load,
        test_set_metadata_marks_modified_and_drops_falsy,
        test_counters_survive_update_hash_mark_error_and_save,
        test_touch_refreshes_only_the_session,
        test_keep_file_records_a_file_on_disk_only,
        test_a_path_that_cant_be_checked_counts_as_missing,
        test_a_dir_that_cant_be_listed_keeps_its_entries,
        test_save_skips_a_manager_with_nothing_to_keep,
        test_nothing_worth_saving_is_written_while_the_file_or_dir_exists,
        test_a_failed_save_is_reported_and_keeps_the_previous_file,
        test_a_file_that_fails_to_load_is_replaced_by_the_next_save,
        test_write_text_atomic_writes_whole_or_not_at_all,
        test_a_partial_run_marks_its_save_only_when_it_writes,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"FAIL: {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"ERROR: {test.__name__}: {e}")
            failed += 1

    print(f"\n{passed}/{passed + failed} tests passed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
