#!/usr/bin/env python3
"""
Remove the frameworks Apple no longer lists in technologies.json.

Runs before the Apple scrape (scheduled-scrape.yml). The candidates are the
Apple framework hash files (framework_hash_files) whose id technologies.json
doesn't list, compared case-insensitively (Apple flips a framework's URL
casing). technologies.json is read through the scrape's own parser
(framework_list_scraper); no doc folder is scanned and no page is requested.

Each run that finds a framework unlisted counts it in its hash file's
metadata.unlisted_runs. At UNLISTED_REMOVAL_RUNS consecutive runs its docs dir
and hash file are deleted (every casing of each). However many frameworks are
dropped at once, each is removed the same way: there is no cap. A framework
listed again starts over: this script drops the count when the list has it,
and the scrape's save drops it for every framework it scrapes.

A failed technologies.json fetch, or one that lists no frameworks, is our
failure: nothing is counted, reset or deleted, and the exit code is 1. So is a
hash file that can't be read, of a framework the list doesn't have (exit 1 on
that run). Next to a docs dir of its id it is that framework's, and is judged
anyway: its count is lost, so the run counts as the first, and the file is
replaced by one that holds the count (as the scrape replaces a listed
framework's), so the framework is removed if the next run finds it unlisted
too. With no docs
dir of its id it can't be told from another scraper's state file, so it is
never written or deleted; no doc depends on it.

Usage:
    python cleanup_removed_frameworks.py --dry-run  # Preview; changes nothing
    python cleanup_removed_frameworks.py            # Ask before deleting
    python cleanup_removed_frameworks.py --yes      # Automated (CI)

Exit code: 0, or 1 on an error of ours (the above, or a failed write or
deletion).
"""

import asyncio
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Final, List, Optional, Sequence, Set, Tuple

# The repo root, for the scraper package
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from cleanup_orphans_at_end import remove_framework
from framework_list_scraper import AppleFrameworkListScraper
from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.sink import CHILD_MODULES_KEY, MODULE_KEY, metadata_ids
from scraper.utils.hash_manager import HashManager, read_hash_file, same_name_any_case
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

# A framework technologies.json hasn't listed on this many consecutive runs is
# removed (its docs dir and hash file); the runs are the confirmation
UNLISTED_REMOVAL_RUNS: Final = 2

HASH_FILE_SUFFIX: Final = "_hashes.json"

# Every Apple framework hash file has keys under this: its pages' JSON URLs
APPLE_JSON_PREFIX: Final = AppleJSONDocumentationScraper.JSON_BASE_URL + "/"

TECHNOLOGIES_URL: Final = AppleFrameworkListScraper.TECHNOLOGIES_URL


@dataclass(frozen=True)
class FrameworkHashFile:
    """An Apple framework's hash file.

    Attributes:
        path: The hash file
        framework_id: The framework's id, as the file name spells it
        unlisted_runs: Its metadata.unlisted_runs: the consecutive runs
            technologies.json hasn't listed it (0 when absent, or when the
            file can't be read)
        load_error: Why the file can't be read (it is the framework's by its
            docs dir, see framework_hash_files), else None
    """

    path: Path
    framework_id: str
    unlisted_runs: int
    load_error: Optional[str] = None


@dataclass
class HashFiles:
    """The hash files directly in a hash dir, classified.

    Attributes:
        frameworks: The Apple framework hash files
        unreadable: The hash files that can't be read and have no docs dir
            of their id, so can't be classified: file -> why
    """

    frameworks: List[FrameworkHashFile] = field(default_factory=list)
    unreadable: Dict[Path, str] = field(default_factory=dict)


@dataclass
class UnlistedReport:
    """What a run of the unlisted rule did (in a dry run: would do).

    Attributes:
        listed: How many frameworks technologies.json lists
        hash_files: How many Apple framework hash files there are
        counted: framework -> its unlisted_runs now, below the removal count
        removed: framework -> .md files its docs dir held
        declined: Frameworks due for removal whose deletion the user
            declined (interactive); they keep their count, so a later run
            removes them
        reset: Frameworks listed again, whose count was dropped
        failures: Errors of ours for the run (exit 1)
    """

    listed: int = 0
    hash_files: int = 0
    counted: Dict[str, int] = field(default_factory=dict)
    removed: Dict[str, int] = field(default_factory=dict)
    declined: List[str] = field(default_factory=list)
    reset: List[str] = field(default_factory=list)
    failures: List[str] = field(default_factory=list)


def framework_id_of(hash_file: Path) -> str:
    """The framework id a hash file's name spells (<id>_hashes.json)."""
    return hash_file.name[: -len(HASH_FILE_SUFFIX)]


def _docs_dirs(framework_id: str) -> List[Path]:
    """Every casing of a framework's docs dir that exists."""
    return [path for path in same_name_any_case(Config.get_framework_output_dir(framework_id)) if path.is_dir()]


def framework_hash_files(hash_dir: Path) -> HashFiles:
    """The Apple framework hash files directly in hash_dir.

    An Apple framework hash file has a key under the Apple JSON URL prefix
    (Apple's files also hold doc-URL keys, so not every key does) and no
    metadata.module (a D6 module's file, which the scrape's end-of-run rules
    remove). The other scrapers' files (HIG, MLX, Swift) and a local
    meilisearch_hashes.json have no such key. Files in .hashes/<namespace>/
    aren't looked at.

    A file with no entry to tell by (one that can't be read, or has no
    'hashes' entries) is a framework's when a docs dir of its id exists, in
    any casing: a framework's hash file and docs dir share its id, and the
    other scrapers' files have no docs dir of theirs. So the unlisted rule
    still judges a framework whose hash file can't be read, and the file it
    writes in its place, which has no entries until a scrape fills it.

    A file that can't be read whose id a readable file's
    metadata.child_modules lists is a D6 module's (its parent's scrape
    routes it pages): it is never judged, and its module's next save
    replaces it. A readable module file is judged by its metadata.module,
    so a promoted module, whose own scrape dropped the key, is a framework's.

    The unlisted rule judges these, and the scrape's list guard counts them
    (scrape_all_frameworks.check_framework_list).
    """
    found = HashFiles()
    failed: List[Tuple[Path, str]] = []
    modules: Set[str] = set()
    for path in sorted(hash_dir.glob(f"*{HASH_FILE_SUFFIX}")):
        framework_id = framework_id_of(path)
        try:
            hashes, metadata = read_hash_file(path)
        except (OSError, ValueError) as e:  # ValueError: not UTF-8, JSON or a hash file
            failed.append((path, str(e)))
            continue
        modules.update(str(module).lower() for module in metadata_ids(metadata.get(CHILD_MODULES_KEY)))
        if metadata.get(MODULE_KEY):
            continue
        has_apple_key = any(url.startswith(APPLE_JSON_PREFIX) for url in hashes)
        if not has_apple_key and (hashes or not _docs_dirs(framework_id)):
            continue
        runs = metadata.get("unlisted_runs", 0)
        found.frameworks.append(FrameworkHashFile(path, framework_id, runs if isinstance(runs, int) else 0))
    for path, error in failed:
        framework_id = framework_id_of(path)
        if framework_id.lower() in modules:
            continue
        if _docs_dirs(framework_id):
            found.frameworks.append(FrameworkHashFile(path, framework_id, 0, load_error=error))
        else:
            found.unreadable[path] = error
    found.frameworks.sort(key=lambda hash_file: hash_file.path)
    return found


def _write_count(hash_file: FrameworkHashFile, runs: int, report: UnlistedReport) -> bool:
    """Write a framework's unlisted_runs (0 drops it); False, a failure for the run, if that failed.

    The hash file is reloaded and saved with only the count changed;
    set_metadata marks the manager modified, so a metadata-only change is
    saved. A file that couldn't be read when it was classified
    (hash_file.load_error) is replaced by one holding only the count, as
    HashManager's save replaces any file that failed to load.
    """
    manager = HashManager(hash_file.path)
    if manager.load_error is not None and hash_file.load_error is None:
        report.failures.append(f"{hash_file.framework_id}: hash file can't be loaded ({manager.load_error})")
        return False
    manager.set_metadata("unlisted_runs", runs)
    if not manager.save():
        report.failures.append(f"{hash_file.framework_id}: hash file save failed ({hash_file.path})")
        return False
    if manager.load_error is not None:
        logger.warning("unreadable_hash_file_replaced", framework=hash_file.framework_id,
                       file=str(hash_file.path), unlisted_runs=runs)
    return True


def _doc_files(framework_id: str) -> int:
    """How many .md files a framework's docs dir holds, every casing of it."""
    return sum(len(HashManager.framework_files(path)) for path in _docs_dirs(framework_id))


def _approved(due: Sequence[FrameworkHashFile]) -> bool:
    """Show the frameworks due for removal and ask once."""
    print(f"\nAbout to remove {len(due)} frameworks technologies.json hasn't listed on "
          f"{UNLISTED_REMOVAL_RUNS} consecutive runs (docs dir and hash file):")
    for hash_file in due:
        print(f"   - {hash_file.framework_id} ({_doc_files(hash_file.framework_id)} files)")
    response = input("Continue? [y/N] ")
    return response.strip().lower() in ("y", "yes")


def apply_unlisted_rule(frameworks: Sequence[Dict[str, str]], dry_run: bool = False,
                        interactive: bool = False) -> UnlistedReport:
    """Count, reset and remove the frameworks technologies.json doesn't list.

    Args:
        frameworks: The frameworks a successful technologies.json fetch lists
            (the shared parser's output); never empty, which is a failed fetch
        dry_run: Write and delete nothing; report what a run would do
        interactive: Ask once before deleting; on no, nothing is deleted and
            each framework keeps its count, so a later run removes it
    """
    listed = {fw['id'].lower() for fw in frameworks}
    found = framework_hash_files(Config.CACHE_DIR)
    report = UnlistedReport(listed=len(listed), hash_files=len(found.frameworks))
    for path, error in found.unreadable.items():
        if framework_id_of(path).lower() in listed:
            continue  # its framework's scrape replaces the file (hash_load_failed)
        logger.error("unlisted_hash_file_unreadable", file=str(path), error=error, docs_dir=False)
        report.failures.append(f"{path} can't be read and has no docs dir of its id, so it can't be judged: {error}")

    due: List[FrameworkHashFile] = []
    for hash_file in found.frameworks:
        framework = hash_file.framework_id
        if framework.lower() in listed:
            # One that can't be read has no count to drop: the scrape replaces it (hash_load_failed)
            if hash_file.unlisted_runs and (dry_run or _write_count(hash_file, 0, report)):
                logger.info("framework_listed_again", framework=framework,
                            unlisted_runs=hash_file.unlisted_runs)
                report.reset.append(framework)
            continue
        if hash_file.load_error is not None:
            # An error of ours that loses the count: this run counts as the
            # first, so the removal waits one run at most, and the count
            # write replaces the file, so the next run can judge it
            logger.error("unlisted_hash_file_unreadable", framework=framework, file=str(hash_file.path),
                         error=hash_file.load_error, docs_dir=True)
            report.failures.append(
                f"{hash_file.path} can't be read ({hash_file.load_error}): its unlisted_runs is lost, so this run "
                f"counts as run 1, and the file {'would be' if dry_run else 'is'} replaced by one holding that count"
            )
        runs = hash_file.unlisted_runs + 1
        if runs >= UNLISTED_REMOVAL_RUNS:
            due.append(hash_file)
        elif dry_run or _write_count(hash_file, runs, report):
            logger.warning("framework_unlisted_pending", framework=framework, unlisted_runs=runs)
            report.counted[framework] = runs

    if due and interactive and not dry_run and not _approved(due):
        for hash_file in due:
            if _write_count(hash_file, hash_file.unlisted_runs + 1, report):
                report.declined.append(hash_file.framework_id)
        return report
    for hash_file in due:
        framework = hash_file.framework_id
        if dry_run:
            report.removed[framework] = _doc_files(framework)
            continue
        try:
            report.removed[framework] = remove_framework(
                framework, Config.get_framework_output_dir(framework), hash_file.path, reason="unlisted"
            )
        except OSError as e:
            report.failures.append(f"{framework}: removal failed: {e}")
    return report


def _print_summary(report: UnlistedReport, dry_run: bool) -> None:
    """The run's summary for the console."""
    if dry_run:
        print("\n[DRY RUN] Nothing is written or deleted; a run would do this:")
    print(f"Apple lists {report.listed} frameworks; {report.hash_files} Apple framework hash files here")
    if report.counted:
        print(f"⏳ Not in technologies.json ({'would be ' if dry_run else ''}counted in unlisted_runs), "
              "removed if still unlisted on the next run: "
              + ", ".join(f"{framework} (run {runs})" for framework, runs in sorted(report.counted.items())))
    if report.removed:
        print(f"🗑️  {'Would remove' if dry_run else 'Removed'} {len(report.removed)} frameworks "
              f"technologies.json hasn't listed on {UNLISTED_REMOVAL_RUNS} consecutive runs "
              "(docs dir and hash file): "
              + ", ".join(f"{framework} ({files} files)" for framework, files in sorted(report.removed.items())))
    if report.declined:
        print("⏸️  Not removed (declined); a later run removes them: " + ", ".join(sorted(report.declined)))
    if report.reset:
        print(f"🔁 Listed again, unlisted_runs {'would be ' if dry_run else ''}reset: "
              + ", ".join(sorted(report.reset)))
    for failure in report.failures:
        print(f"❌ {failure}")
    if not (report.counted or report.removed or report.declined or report.failures):
        print("✅ No removed frameworks detected")


async def fetch_frameworks() -> List[Dict[str, str]]:
    """technologies.json's frameworks, through the scrape's parser ([] if the fetch failed)."""
    async with AppleFrameworkListScraper() as framework_scraper:
        frameworks: List[Dict[str, str]] = await framework_scraper.fetch_all_frameworks()
    return frameworks


def main() -> int:
    """Apply the unlisted rule once; returns the process exit code."""
    dry_run = "--dry-run" in sys.argv
    interactive = "--yes" not in sys.argv
    print("Fetching current framework list from Apple...")
    frameworks = asyncio.run(fetch_frameworks())
    if not frameworks:
        logger.error("framework_list_unavailable", url=TECHNOLOGIES_URL)
        print("❌ technologies.json couldn't be fetched, or listed no frameworks: nothing counted, reset or removed")
        return 1
    report = apply_unlisted_rule(frameworks, dry_run=dry_run, interactive=interactive)
    _print_summary(report, dry_run)
    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
