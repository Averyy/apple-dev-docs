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
    """Nested metadata survives load and save; total_pages is rewritten and the legacy keys are dropped."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        cache.write_text(json.dumps({
            "metadata": {
                "last_updated": "old", "total_pages": 99, "session_id": "old", "partial_session": "old",
                "root_gone_runs": 1, "failure_storm_runs": 2, "pending_orphans": ["a.md"],
                "module": {"parent": "other"},
            },
            "hashes": {"u": {"hash": "h", "file_path": "documentation/fw/u.md"}},
        }))
        hm = HashManager(cache)
        assert hm.metadata == {
            "root_gone_runs": 1, "failure_storm_runs": 2, "pending_orphans": ["a.md"], "module": {"parent": "other"},
        }
        hm.set_counter("u", "consecutive_failures", 1)
        hm.save()
        metadata = json.loads(cache.read_text())["metadata"]
        assert list(metadata) == ["failure_storm_runs", "module", "pending_orphans", "root_gone_runs", "total_pages"]
        assert metadata["total_pages"] == 1
        assert HashManager(cache).metadata == hm.metadata
    print("PASS: metadata_is_preserved_across_save_and_load")


def test_legacy_fields_are_dropped_on_load() -> None:
    """The fields no longer written are dropped on load, and leave the file at its next save.

    Per entry: last_checked, session_id, a status other than "error", and an
    error entry's hash. Counters and every content field stay.
    """
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        legacy = json.dumps({
            "metadata": {"last_updated": "t", "total_pages": 4, "session_id": "s", "partial_session": "s"},
            "hashes": {
                "live": {"hash": "h", "last_checked": "t", "status": "unchanged", "session_id": "s",
                         "etag": "E", "file_path": "documentation/fw/live.md"},
                "new": {"hash": "h2", "last_checked": "t", "status": "new", "session_id": "s",
                        "file_path": "documentation/fw/new.md", "consecutive_local_errors": 1},
                "gone": {"hash": "", "last_checked": "t", "status": "error", "error": "HTTP 404",
                         "consecutive_failures": 2},
                "kept": {"hash": "", "status": "unchanged", "session_id": "s", "file_path": "documentation/fw/kept.md"},
            },
        }, indent=2)
        cache.write_text(legacy)
        hm = HashManager(cache)
        assert hm.hashes == {
            "live": {"hash": "h", "etag": "E", "file_path": "documentation/fw/live.md"},
            "new": {"hash": "h2", "file_path": "documentation/fw/new.md", "consecutive_local_errors": 1},
            "gone": {"status": "error", "error": "HTTP 404", "consecutive_failures": 2},
            "kept": {"hash": "", "file_path": "documentation/fw/kept.md"},
        }
        assert hm.metadata == {}
        # Loading changes nothing on disk: an unmodified manager writes nothing
        assert hm.save() is True and cache.read_text() == legacy
        # Any change writes the whole file without them
        hm.set_counter("gone", "consecutive_failures", 3)
        assert hm.save() is True
        saved = json.loads(cache.read_text())
        assert saved["metadata"] == {"total_pages": 4}
        assert saved["hashes"] == hm.hashes
        assert saved["hashes"]["gone"] == {"status": "error", "error": "HTTP 404", "consecutive_failures": 3}
    print("PASS: legacy_fields_are_dropped_on_load")


def test_a_second_save_of_the_same_entries_is_byte_identical() -> None:
    """Sorted keys and no timestamps: a run that rewrites what a file holds writes the same bytes.

    E.g. a page re-marked as a 404 every run (mark_error always marks the
    manager modified), or an unchanged page whose hash and etag are written again.
    """
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        hm = HashManager(cache)
        hm.update_hash("b", "content", etag="E", file_path=Path("documentation/fw/b.md"))
        hm.update_hash("a", "content", etag="E", file_path=Path("documentation/fw/a.md"))
        hm.mark_error("c", "HTTP 404")
        hm.set_counter("a", "consecutive_failures", 1)
        hm.set_metadata("pending_orphans", ["documentation/fw/x.md"])
        assert hm.save() is True
        first = cache.read_bytes()
        assert first == json.dumps(json.loads(first), indent=2, sort_keys=True).encode()
        for rewrite in ("mark_error", "update_hash"):
            again = HashManager(cache)
            if rewrite == "mark_error":
                again.mark_error("c", "HTTP 404")
            else:
                again.update_hash("b", "content", etag="E", file_path=Path("documentation/fw/b.md"))
            assert again.save() is True
            assert cache.read_bytes() == first, rewrite
    print("PASS: a_second_save_of_the_same_entries_is_byte_identical")


def test_a_stale_render_version_refetches_and_renders_every_page() -> None:
    """While the stored render version isn't the manager's: no etag is sent and every page has changed."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        url = "https://example.com/page"
        hm = HashManager(cache, render_version=2)
        hm.update_hash(url, "content", etag="E1")
        assert (hm.stale, hm.stored_render_version) == (True, None)
        assert hm.get_etag(url) is None
        assert hm.has_changed(url, "content", etag="E1") is True
        hm.mark_rendered()
        assert (hm.stale, hm.stored_render_version) == (False, 2)
        assert hm.get_etag(url) == "E1"
        assert hm.has_changed(url, "content", etag="E1") is False
        assert hm.save()
        assert json.loads(cache.read_text())["metadata"]["render"] == {"version": 2}

        # A version bump makes the location stale again; an equal one doesn't
        assert HashManager(cache, render_version=3).stale
        assert not HashManager(cache, render_version=2).stale
        # A malformed value is stale
        data = json.loads(cache.read_text())
        data["metadata"]["render"] = 2
        cache.write_text(json.dumps(data))
        assert HashManager(cache, render_version=2).stale
    print("PASS: a_stale_render_version_refetches_and_renders_every_page")


def test_a_manager_without_a_render_version_keeps_the_stored_one() -> None:
    """A manager loaded only to prune or count is never stale, never writes render, and keeps it on save."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        cache.write_text(json.dumps({
            "metadata": {"render": {"version": 1}},
            "hashes": {"u": {"hash": "h", "etag": "E", "file_path": str(Path(d) / "gone.md")},
                       "v": {"hash": "h", "etag": "E2", "file_path": str(cache)}},
        }))
        hm = HashManager(cache)
        assert (hm.stale, hm.get_etag("v")) == (False, "E2")
        hm.mark_rendered()
        assert hm.metadata == {"render": {"version": 1}}
        assert hm.prune_missing_files() == 1 and hm.save()
        assert json.loads(cache.read_text())["metadata"]["render"] == {"version": 1}
        # The scraper's own manager of another version is stale, and stores it only through mark_rendered
        own = HashManager(cache, render_version=2)
        own.set_counter("v", "consecutive_failures", 1)
        assert own.stale and own.save()
        assert json.loads(cache.read_text())["metadata"]["render"] == {"version": 1}
    print("PASS: a_manager_without_a_render_version_keeps_the_stored_one")


def test_forget_untouched_renderings_drops_only_their_hash_and_etag() -> None:
    """Untouched live entries lose hash and etag, keeping file_path and counters; touched and
    error entries, and a value that isn't an entry, stay; a second call changes nothing."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        cache.write_text(json.dumps({"metadata": {}, "hashes": {
            "held": {"hash": "h", "etag": "E", "file_path": "a.md", "consecutive_local_errors": 1},
            "seen": {"hash": "h", "etag": "E", "file_path": "b.md"},
            "gone": {"status": "error", "error": "HTTP 404"},
            "digest": "d",
        }}))
        hm = HashManager(cache, render_version=2)
        hm.touch("seen")
        assert hm.forget_untouched_renderings() == 1 and hm.save()
        assert json.loads(cache.read_text())["hashes"] == {
            "held": {"hash": "", "file_path": "a.md", "consecutive_local_errors": 1},
            "seen": {"hash": "h", "etag": "E", "file_path": "b.md"},
            "gone": {"status": "error", "error": "HTTP 404"},
            "digest": "d",
        }
        assert hm.forget_untouched_renderings() == 0 and not hm._modified
    print("PASS: forget_untouched_renderings_drops_only_their_hash_and_etag")


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


def test_touch_only_records_the_url() -> None:
    """touch adds the URL to the touched set, leaving its entry alone; nothing is saved for it."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        hm = HashManager(cache)
        hm.update_hash("u", "content", etag="E", file_path=Path("documentation/fw/u.md"))
        assert hm.save() is True
        later = HashManager(cache)
        before = dict(later.hashes["u"])
        later.touch("u")
        assert later.touched == {"u"} and later.hashes["u"] == before
        cache.unlink()
        assert later.save() is True and not cache.exists()  # not modified: nothing written
    print("PASS: touch_only_records_the_url")


def test_set_file_path_sets_only_the_path() -> None:
    """set_file_path leaves hash, etag and counters alone, and marks the manager modified only on a change."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        hm = HashManager(cache)
        hm.update_hash("u", "content", etag="E", file_path=Path("documentation/fw/old.md"))
        hm.set_counter("u", "consecutive_failures", 2)
        assert hm.save() is True
        saved = cache.read_text()
        same = HashManager(cache)
        same.set_file_path("u", "documentation/fw/old.md")  # unchanged: not modified, not rewritten
        cache.unlink()
        assert same.save() is True and not cache.exists()
        cache.write_text(saved)
        renamed = HashManager(cache)
        renamed.set_file_path("u", Path("documentation/fw/new.md"))
        assert renamed.touched == set()
        assert renamed.save() is True
        assert json.loads(cache.read_text())["hashes"]["u"] == {
            "hash": renamed.get_content_hash("content"), "etag": "E", "file_path": "documentation/fw/new.md",
            "consecutive_failures": 2,
        }
        try:
            renamed.set_file_path("missing", "documentation/fw/x.md")
        except KeyError:
            pass
        else:
            raise AssertionError("set_file_path created an entry")
        assert "missing" not in renamed.hashes
    print("PASS: set_file_path_sets_only_the_path")


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
        assert entry == {"hash": "", "file_path": str(page), "consecutive_failures": 3}
        assert hm.hashes["v"] == {"hash": "", "file_path": str(page.with_name("page.md"))}
        assert hm.touched == {"u", "v"}
        # The next run refetches it without an etag and converts it again
        assert hm.has_changed("u", "content") is True and hm.get_etag("u") is None
        del hm.hashes["v"]
        assert hm.get_untouched_files(page.parent) == []
        assert hm.save() is True and json.loads(hm.cache_file.read_text())["hashes"]["u"] == entry
    print("PASS: keep_file_records_a_file_on_disk_only")


def test_keep_file_alone_is_saved() -> None:
    """keep_file marks the manager modified: e.g. a lost hash file, then the root fails with its file on disk."""
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d) / "fw_hashes.json"
        page = Path(d) / "fw" / "fw.md"
        page.parent.mkdir()
        page.write_text("# fw\n")
        hm = HashManager(cache)
        assert hm.keep_file("root", page) is True
        assert hm.save() is True and cache.exists()
        assert json.loads(cache.read_text())["hashes"] == {"root": {"hash": "", "file_path": str(page)}}
    print("PASS: keep_file_alone_is_saved")


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
        hm.hashes["v"] = {"hash": "h", "etag": "E", "file_path": str(page)}
        assert hm.get_etag("v") is None
        assert hm.has_changed("v", "content", etag="E") is True
        assert hm.prune_missing_files() == 1 and "v" not in hm.hashes
        # Orphan detection checks a touched entry's path without raising
        hm.hashes["w"] = {"hash": "h", "file_path": str(page)}
        hm.touch("w")
        assert hm.get_untouched_files(page.parent) == [page.parent / "other.md"]
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
        hm.hashes["u"] = {"hash": hm.get_content_hash("content"), "etag": "E", "file_path": str(page),
                          "consecutive_local_errors": 2}
        hm.touch("u")
        hm.mark_error("v", "HTTP 502")
        locked.chmod(0)
        try:
            assert hm.get_etag("u") == "E"
            assert hm.has_changed("u", "content", etag="E") is False
            assert hm.prune_missing_files() == 0 and hm.hashes["u"]["consecutive_local_errors"] == 2
            before = dict(hm.hashes["v"])
            assert hm.keep_file("v", page) is False and hm.hashes["v"] == before
            assert hm.get_untouched_files(Path(d) / "fw") == []
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


def main():
    tests = [
        test_new_url_is_changed,
        test_same_etag_unchanged,
        test_different_etag_different_content_is_changed,
        test_different_etag_same_content_is_unchanged,
        test_no_etag_uses_hash,
        test_etag_updated_after_regeneration,
        test_metadata_is_preserved_across_save_and_load,
        test_a_stale_render_version_refetches_and_renders_every_page,
        test_a_manager_without_a_render_version_keeps_the_stored_one,
        test_forget_untouched_renderings_drops_only_their_hash_and_etag,
        test_set_metadata_marks_modified_and_drops_falsy,
        test_legacy_fields_are_dropped_on_load,
        test_a_second_save_of_the_same_entries_is_byte_identical,
        test_counters_survive_update_hash_mark_error_and_save,
        test_touch_only_records_the_url,
        test_set_file_path_sets_only_the_path,
        test_keep_file_records_a_file_on_disk_only,
        test_keep_file_alone_is_saved,
        test_a_path_that_cant_be_checked_counts_as_missing,
        test_a_dir_that_cant_be_listed_keeps_its_entries,
        test_save_skips_a_manager_with_nothing_to_keep,
        test_nothing_worth_saving_is_written_while_the_file_or_dir_exists,
        test_a_failed_save_is_reported_and_keeps_the_previous_file,
        test_a_file_that_fails_to_load_is_replaced_by_the_next_save,
        test_write_text_atomic_writes_whole_or_not_at_all,
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
