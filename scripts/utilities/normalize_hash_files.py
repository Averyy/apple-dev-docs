#!/usr/bin/env python3
"""
One-off normalization of the Apple framework hash files (D5 switch).

HashManager now writes only content fields (hash, etag, file_path; status and
error on an error entry; the run counters while > 0) with sorted keys, and
drops the legacy fields on load (last_checked, session_id, a status other
than "error", an error entry's hash; metadata last_updated, session_id,
partial_session). save() writes only a modified manager, and a run whose
pages all answer 304 modifies nothing, so no scrape would ever rewrite a
file in the new format: this script loads every Apple framework hash file
(one with a key under the JSON data URL) through HashManager, marks it
modified and saves it.

It also drops the root keys whose casing doesn't match the framework id (the
hash file's name), both of each (JSON URL and doc URL), when the root in the
id's casing is there too: Apple flipped a framework's URL casing once, and
the scrape only ever writes the id's casing, so the other pair is stale.

The other scrapers' hash files (HIG, Swift, MLX) are hash_utils' and are left
alone. A second run writes the same bytes.

Usage (from the repo root, with the D5 switch's code applied on an
up-to-date origin/main and no scrape run queued or in progress; with the old
HashManager, which drops no legacy field, it refuses to run):
    python scripts/utilities/normalize_hash_files.py --dry-run  # Report; changes nothing
    python scripts/utilities/normalize_hash_files.py            # Normalize .hashes

Exit code: 0, or 1 if a hash file failed to load or save (left as it was)
or the HashManager is the old one (nothing changed).
"""

import argparse
import shutil
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Final, List

# The repo root, for the scraper package
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.hash_manager import HashManager, read_hash_file

HASH_FILE_SUFFIX: Final = "_hashes.json"
APPLE_JSON_PREFIX: Final = AppleJSONDocumentationScraper.JSON_BASE_URL + "/"


@dataclass
class Report:
    """What the normalization did (or, on a dry run, would do)."""

    files: int = 0
    other_files: int = 0
    entries_before: int = 0
    entries_after: int = 0
    entries_cleaned: int = 0
    metadata_keys_dropped: int = 0
    bytes_before: int = 0
    bytes_after: int = 0
    changed_files: int = 0
    dropped_keys: List[str] = field(default_factory=list)
    failures: List[str] = field(default_factory=list)


def case_duplicate_roots(framework_id: str, manager: HashManager) -> List[str]:
    """The root keys in another casing than framework_id's, if the id-cased root is there too."""
    json_root = f"{APPLE_JSON_PREFIX}{framework_id}.json"
    doc_root = f"{Config.DOCUMENTATION_URL}/{framework_id}"
    if json_root not in manager.hashes:
        return []
    return sorted(
        url for url in manager.hashes
        if url.lower() in (json_root.lower(), doc_root.lower()) and url not in (json_root, doc_root)
    )


def normalize(path: Path, raw_hashes: Dict[str, Any], raw_metadata: Dict[str, Any], report: Report) -> None:
    """Load one Apple hash file through HashManager, drop its case-duplicate roots and save it.

    raw_hashes and raw_metadata are the file as read_hash_file reads it, for the report.
    """
    framework_id = path.name[: -len(HASH_FILE_SUFFIX)]
    before = path.read_bytes()
    manager = HashManager(path)
    if manager.load_error is not None:
        report.failures.append(f"{path}: failed to load: {manager.load_error}")
        return
    report.files += 1
    report.entries_before += len(raw_hashes)
    report.entries_cleaned += sum(
        1 for url, entry in manager.hashes.items() if entry != raw_hashes[url]
    )
    report.metadata_keys_dropped += sum(
        1 for key in raw_metadata if key != "total_pages" and key not in manager.metadata
    )
    for url in case_duplicate_roots(framework_id, manager):
        manager.remove(url)
        report.dropped_keys.append(url)
    # save() writes only a modified manager
    manager._modified = True
    if not manager.save():
        report.failures.append(f"{path}: save failed")
        return
    after = path.read_bytes()
    report.entries_after += len(manager.hashes)
    report.bytes_before += len(before)
    report.bytes_after += len(after)
    report.changed_files += after != before


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="Normalize copies and report; change nothing")
    args = parser.parse_args()
    if not hasattr(HashManager, "set_file_path"):
        # The old HashManager would rewrite every file in the old format
        print("❌ This HashManager predates the D5 switch: apply its code first; nothing changed")
        return 1

    report = Report()
    paths = sorted(Config.CACHE_DIR.glob(f"*{HASH_FILE_SUFFIX}"))
    with tempfile.TemporaryDirectory() as scratch:
        for path in paths:
            try:
                hashes, metadata = read_hash_file(path)
            except (OSError, ValueError) as e:
                report.failures.append(f"{path}: failed to load: {e}")
                continue
            if not any(url.startswith(APPLE_JSON_PREFIX) for url in hashes):
                report.other_files += 1
                continue
            if args.dry_run:
                copy = Path(scratch) / path.name
                shutil.copy2(path, copy)
                normalize(copy, hashes, metadata, report)
                copy.unlink()
            else:
                normalize(path, hashes, metadata, report)

    mode = "Would normalize" if args.dry_run else "Normalized"
    print(f"{mode} {report.files} Apple hash files ({report.other_files} other hash files left alone)")
    print(f"  entries: {report.entries_before:,} -> {report.entries_after:,} "
          f"({report.entries_cleaned:,} lose legacy fields)")
    print(f"  legacy metadata keys dropped: {report.metadata_keys_dropped:,}")
    print(f"  case-duplicate root keys dropped: {len(report.dropped_keys)}")
    for url in report.dropped_keys:
        print(f"    - {url}")
    print(f"  size: {report.bytes_before:,} -> {report.bytes_after:,} bytes; "
          f"{report.changed_files} files {'would change' if args.dry_run else 'changed'}")
    for failure in report.failures:
        print(f"❌ {failure}")
    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
