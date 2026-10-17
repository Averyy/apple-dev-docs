#!/usr/bin/env python3
"""
Delete orphaned files at the end of scraping.

The scrape (scrape.py --cleanup-orphans) cleans from each framework's result,
computed right after its hash file was saved (cleanup_after_scrape): only the
frameworks scraped this run, never one whose run hit a failure of ours. The
standalone main() collects every framework's orphans from its persisted
session instead, skipping a framework whose last save came from a scrape that
didn't finish it or hit a failure of ours. Both delete through delete_orphans,
presenting them once for approval unless the cleanup is automatic.
"""

import os
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Dict, Final, Iterable, List, Optional, Sequence, Tuple

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from analysis.check_orphans import HashManager
from scraper.config import Config
from scraper.utils.hash_manager import same_name_any_case, valve_trips
from scraper.utils.logger import get_logger

if TYPE_CHECKING:
    from scraper.json_scraper import FrameworkOutcome, OrphanScan

logger = get_logger(__name__)

# A framework whose root returned 404/410 on this many consecutive runs is
# removed (its docs dir and hash file); the two runs are the confirmation
ROOT_GONE_REMOVAL_RUNS: Final = 2


@dataclass
class FrameworkCleanup:
    """One framework's share of an orphan cleanup.

    Attributes:
        framework: The framework's id
        framework_dir: Its docs dir
        hash_file: Its hash file
        files: How many .md files its docs dir held when its orphans were found
        delete: The orphaned files to delete
        confirmed: How many of them an earlier clean run held in
            pending_orphans (confirm-then-delete)
        held: How many orphans the valve holds this run, in pending_orphans
        pending_orphans: The framework's new metadata.pending_orphans if it
            changes ([] drops it), else None
        remove: Remove the whole framework, every casing of its docs dir and
            hash file: its root returned 404/410 on 2 consecutive runs
    """

    framework: str
    framework_dir: Path
    hash_file: Path
    files: int = 0
    delete: List[Path] = field(default_factory=list)
    confirmed: int = 0
    held: int = 0
    pending_orphans: Optional[List[str]] = None
    remove: bool = False


@dataclass
class CleanupReport:
    """What an orphan cleanup did, for the end-of-run summary and the exit code.

    Attributes:
        deleted: framework -> orphaned files deleted
        confirmed: framework -> of those, files confirmed from pending_orphans
        held: framework -> (orphans the valve holds in pending_orphans, the
            framework's files once the confirmed ones are deleted)
        removed: framework -> .md files in the removed framework's docs dir
        pruned: Hash entries pruned for deleted files
        cancelled: The user declined the deletion (interactive cleanup)
        failures: What failed (a deletion, or a hash-file write that lost a
            prune or a pending_orphans change): errors for the run
    """

    deleted: Dict[str, int] = field(default_factory=dict)
    confirmed: Dict[str, int] = field(default_factory=dict)
    held: Dict[str, Tuple[int, int]] = field(default_factory=dict)
    removed: Dict[str, int] = field(default_factory=dict)
    pruned: int = 0
    cancelled: bool = False
    failures: List[str] = field(default_factory=list)


def plan_cleanup(framework: str, scan: "OrphanScan") -> FrameworkCleanup:
    """Confirm-then-delete: what to do with a framework's orphan candidates O.

    - With no pending_orphans P, O is deleted unless it trips the valve
      (valve_trips): then nothing is deleted and P = O is kept.
    - With a P an earlier clean run held, D = P ∩ O (case-insensitive) is
      deleted: two clean runs found those files orphaned. The remainder O − D
      waits only if it trips the valve itself, against the files left once D
      is gone: it then replaces P. Otherwise it is deleted too and P is
      dropped.

    Every change to P is returned, to be written even on a run that deletes
    nothing.
    """
    pending = {path.lower() for path in scan.pending_orphans}
    confirmed = [path for path in scan.orphans if str(path).lower() in pending]
    remainder = [path for path in scan.orphans if str(path).lower() not in pending]
    cleanup = FrameworkCleanup(framework, scan.framework_dir, scan.hash_file, files=scan.files)
    cleanup.confirmed = len(confirmed)
    if valve_trips(len(remainder), scan.files - len(confirmed)):
        cleanup.delete = confirmed
        cleanup.held = len(remainder)
        new_pending = sorted(str(path) for path in remainder)
        logger.warning(
            "orphan_valve_held",
            framework=framework,
            held=len(remainder),
            files=scan.files - len(confirmed),
            confirmed=len(confirmed),
        )
    else:
        cleanup.delete = confirmed + remainder
        new_pending = []
    if new_pending != scan.pending_orphans:
        cleanup.pending_orphans = new_pending
    return cleanup


def _framework_on_disk(framework_dir: Path, hash_file: Path) -> Tuple[List[Path], List[Path]]:
    """Every casing of a framework's docs dir and hash file that exists: what its removal deletes."""
    dirs = [path for path in same_name_any_case(framework_dir) if path.is_dir()]
    hash_files = [path for path in same_name_any_case(hash_file) if path.is_file()]
    return dirs, hash_files


def remove_framework(framework: str, framework_dir: Path, hash_file: Path, reason: str) -> int:
    """Delete every casing of a framework's docs dir and hash file.

    Both of Apple's framework removals go through this: a root gone
    (404/410) on 2 consecutive runs, and a framework technologies.json
    hasn't listed on 2 consecutive runs (cleanup_removed_frameworks.py).

    Args:
        framework: The framework's id, for the log
        framework_dir: Its docs dir
        hash_file: Its hash file
        reason: Why it is removed, for the log ("root_gone", "unlisted")

    Returns:
        How many .md files its docs dir held

    Raises:
        OSError: A deletion failed (logged)
    """
    dirs, hash_files = _framework_on_disk(framework_dir, hash_file)
    files = sum(len(HashManager.framework_files(path)) for path in dirs)
    try:
        for path in dirs:
            shutil.rmtree(path)
        for path in hash_files:
            path.unlink()
    except OSError as e:
        logger.error("framework_removal_failed", framework=framework, reason=reason, error=str(e))
        raise
    logger.warning(
        "framework_removed",
        framework=framework,
        reason=reason,
        files=files,
        dirs=[str(path) for path in dirs],
        hash_files=[str(path) for path in hash_files],
    )
    return files


def _remove_framework(cleanup: FrameworkCleanup, report: CleanupReport) -> None:
    """Remove a framework whose root returned 404/410 on 2 consecutive runs."""
    try:
        files = remove_framework(cleanup.framework, cleanup.framework_dir, cleanup.hash_file, reason="root_gone")
    except OSError as e:
        report.failures.append(f"{cleanup.framework}: removal failed: {e}")
        return
    report.removed[cleanup.framework] = files


def _remove_empty_dirs(path: Path, framework_dir: Path) -> None:
    """Remove the dirs a deleted file leaves empty, up to the framework's dir."""
    parent = path.parent
    while parent != framework_dir and framework_dir in parent.parents:
        try:
            parent.rmdir()  # only an empty dir
        except OSError:
            break
        parent = parent.parent


def _write_hash_file(cleanup: FrameworkCleanup, prune: bool, report: CleanupReport) -> bool:
    """Prune the entries of deleted files and write a changed pending_orphans.

    Reloads the framework's hash file with the scrape's session (so old-way
    orphan detection still compares against it) and saves once; a
    pending_orphans change is saved even when nothing else changed.

    Returns:
        False if the write failed (reported in report.failures)
    """
    hash_manager = HashManager(cleanup.hash_file, cleanup.framework_dir, resume_session=True)
    if hash_manager.load_error is not None:
        # Never replace a hash file we can't read with what this write holds
        report.failures.append(f"{cleanup.framework}: hash file failed to load: {hash_manager.load_error}")
        return False
    pruned = hash_manager.prune_missing_files() if prune else 0
    if cleanup.pending_orphans is not None:
        hash_manager.set_metadata("pending_orphans", cleanup.pending_orphans)
    if not hash_manager.save():
        # Lost: a prune, or a pending_orphans change (a hold confirmed one
        # run later, or a list that should be dropped)
        report.failures.append(f"{cleanup.framework}: hash file save failed ({cleanup.hash_file})")
        return False
    report.pruned += pruned
    if pruned:
        logger.info("pruned_hash_entries", framework=cleanup.framework, pruned=pruned)
    return True


def _approved(cleanups: Sequence[FrameworkCleanup]) -> bool:
    """Show what would be deleted and ask once."""
    total = sum(len(cleanup.delete) for cleanup in cleanups)
    removals = [cleanup for cleanup in cleanups if cleanup.remove]
    print("\n" + "=" * 70)
    print(f"🗑️  Detected that Apple has removed {total} pages across "
          f"{len([c for c in cleanups if c.delete])} frameworks:")
    print("=" * 70)

    # Group by framework for display
    for cleanup in sorted(cleanups, key=lambda c: c.framework):
        if cleanup.remove:
            print(f"\n📁 {cleanup.framework}: its root returned 404/410 on {ROOT_GONE_REMOVAL_RUNS} runs; "
                  "its docs dir and hash file will be removed")
            continue
        print(f"\n📁 {cleanup.framework} ({len(cleanup.delete)} files):")
        for orphan in cleanup.delete[:5]:  # Show first 5 per framework
            print(f"   • {orphan.name}")
        if len(cleanup.delete) > 5:
            print(f"   ... and {len(cleanup.delete) - 5} more files")
    if removals:
        print(f"\n🗑️  {len(removals)} frameworks will be removed entirely")

    print("\n" + "=" * 70)
    response = input("\n⚠️  These markdown files will be removed if you approve. Continue? (y/N): ")
    return response.lower() in ['y', 'yes']


def delete_orphans(cleanups: Sequence[FrameworkCleanup], interactive: bool) -> CleanupReport:
    """Delete orphaned files: the one deletion path, automatic or interactive.

    For each framework, delete its files and the dirs they leave empty (up to
    the framework's dir), or remove the whole framework, every casing of its
    docs dir and hash file. Then write its hash file once: the entries of
    deleted files are pruned and a changed pending_orphans is written, even
    on a run that deletes nothing.

    Which frameworks are cleaned (never one blocked by a failure of ours) and
    what each deletes is decided by the caller (cleanup_after_scrape, or
    collect_all_orphans for the standalone check).

    Args:
        cleanups: Each framework's deletions and pending_orphans change
        interactive: Show the deletions and ask once. On no, nothing is
            deleted, and a framework that would have deleted something keeps
            its pending_orphans as they are; one that only holds still
            writes its list.
    """
    report = CleanupReport()
    deleting = [cleanup for cleanup in cleanups if cleanup.delete or cleanup.remove]
    if interactive and deleting and not _approved(deleting):
        print("❌ Deletion cancelled by user")
        report.cancelled = True
        cleanups = [cleanup for cleanup in cleanups if not (cleanup.delete or cleanup.remove)]

    for cleanup in cleanups:
        if cleanup.remove:
            _remove_framework(cleanup, report)
            continue
        deleted = 0
        for orphan in cleanup.delete:
            try:
                orphan.unlink()
            except FileNotFoundError:
                continue
            except OSError as e:
                logger.error("orphan_delete_failed", file=str(orphan), error=str(e))
                report.failures.append(f"{cleanup.framework}: failed to delete {orphan}: {e}")
                continue
            deleted += 1
            _remove_empty_dirs(orphan, cleanup.framework_dir)
        if deleted:
            report.deleted[cleanup.framework] = deleted
            if cleanup.confirmed:
                report.confirmed[cleanup.framework] = cleanup.confirmed
            logger.info("orphans_deleted", framework=cleanup.framework, deleted=deleted, confirmed=cleanup.confirmed)
        written = True
        if deleted or cleanup.pending_orphans is not None:
            written = _write_hash_file(cleanup, prune=deleted > 0, report=report)
        if cleanup.held and written:
            # Against the files the valve weighed them with (those left once the confirmed ones go)
            report.held[cleanup.framework] = (cleanup.held, cleanup.files - cleanup.confirmed)
    return report


def describe_skip(outcome: "FrameworkOutcome") -> str:
    """Why orphan cleanup skips a framework this run, for the console."""
    if outcome.raised is not None:
        return "raised"
    if outcome.blocks:
        return ", ".join(f"{reason} x{len(details)}" for reason, details in outcome.blocks.items())
    return f"root gone, run {outcome.root_gone_runs}"


def _shadow_summary(outcomes: Sequence["FrameworkOutcome"]) -> None:
    """D5 shadow mode: log how often the two ways of finding orphans disagreed.

    compared: frameworks whose orphans were found both ways (orphan_shadow);
    mismatched: those whose two sets differ, blocked ones excluded; blocked:
    frameworks blocked by a failure of ours or that raised (logged, never in
    mismatched), so a run with blocked frameworks isn't taken for full
    coverage. Also appended to the GitHub Actions step summary.
    """
    compared = [outcome for outcome in outcomes if outcome.shadow_mismatch is not None]
    mismatched = [outcome for outcome in compared if outcome.shadow_mismatch and not outcome.blocked]
    blocked = [outcome for outcome in outcomes if outcome.blocked]
    log = logger.warning if mismatched else logger.info
    log(
        "orphan_shadow_summary",
        compared=len(compared),
        mismatched=len(mismatched),
        blocked=len(blocked),
        mismatched_frameworks=[outcome.framework_id for outcome in mismatched],
    )
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        try:
            with open(step_summary, "a") as f:
                f.write(f"orphan_shadow_summary compared={len(compared)} mismatched={len(mismatched)} "
                        f"blocked={len(blocked)}\n")
        except OSError as e:
            logger.warning("step_summary_write_failed", file=step_summary, error=str(e))


def _print_summary(report: CleanupReport, skipped: Sequence["FrameworkOutcome"],
                   root_pending: Sequence["FrameworkOutcome"], root_gone: Sequence["FrameworkOutcome"]) -> None:
    """The end-of-run summary of the orphan cleanup.

    root_pending: frameworks whose root returned 404/410 this run, removed if
    it does again on the next run; root_gone: those with no docs dir or hash
    file left to remove (e.g. still listed after their removal), which
    nothing in the cleanup can change.
    """
    if report.deleted:
        details = []
        for framework, count in sorted(report.deleted.items()):
            confirmed = report.confirmed.get(framework)
            details.append(f"{framework} {count}" + (f" ({confirmed} confirmed from pending_orphans)" if confirmed else ""))
        print(f"✅ Deleted {sum(report.deleted.values())} orphaned files in {len(report.deleted)} frameworks: "
              + ", ".join(details))
    if report.pruned:
        print(f"🧹 Pruned {report.pruned} hash entries for deleted files")
    if report.held:
        print(f"⏸️  Held by the valve (at least half of a framework's files, or over 1,000) in "
              f"{len(report.held)} frameworks, pending_orphans set; deleted on the next clean run "
              "if still orphaned:")
        for framework, (held, files) in sorted(report.held.items()):
            print(f"   - {framework}: {held} of {files} files")
    if report.removed:
        print(f"🗑️  Removed {len(report.removed)} frameworks whose root returned 404/410 on "
              f"{ROOT_GONE_REMOVAL_RUNS} runs (docs dir and hash file): "
              + ", ".join(f"{framework} ({files} files)" for framework, files in sorted(report.removed.items())))
    if root_pending:
        print("⏳ Root returned 404/410 (removed if it does again next run): "
              + ", ".join(f"{outcome.framework_id} (run {outcome.root_gone_runs})" for outcome in root_pending))
    if root_gone:
        print("ℹ️  Root returned 404/410, with no docs dir or hash file left to remove: "
              + ", ".join(outcome.framework_id for outcome in root_gone))
    if skipped:
        print(f"⏸️  Cleanup skipped this run for {len(skipped)} frameworks: "
              + ", ".join(f"{outcome.framework_id} ({describe_skip(outcome)})" for outcome in skipped))
    for failure in report.failures:
        print(f"❌ {failure}")
    if not (report.deleted or report.held or report.removed or report.cancelled or report.failures):
        if skipped or root_pending:
            print("✅ No orphaned files found in the frameworks cleaned this run")
        else:
            print("✅ No orphaned files found!")


def cleanup_after_scrape(outcomes: Sequence["FrameworkOutcome"], interactive: bool) -> CleanupReport:
    """The scrape's end-of-run orphan cleanup, from each framework's result.

    Only frameworks scraped this run are cleaned (others have no result),
    each from the orphan candidates found right after its hash file was
    saved (FrameworkOutcome.orphan_scan), with confirm-then-delete for mass
    removals (plan_cleanup). A framework blocked by a failure of ours, or
    that raised, is never cleaned; neither is one whose root returned
    404/410 this run, until it has on 2 consecutive runs: it is then removed
    outright (docs dir and hash file), bypassing the zero-touched guard and
    the valve. With neither left (a still-listed framework after its
    removal), its root_gone_runs isn't saved (HashManager.save), so it stays
    at 1 and the summary says there is nothing left to remove.

    Args:
        outcomes: The run's framework outcomes
        interactive: Ask before deleting (delete_orphans)

    Returns:
        The report; its failures are errors for the run
    """
    _shadow_summary(outcomes)
    cleanups: List[FrameworkCleanup] = []
    skipped: List["FrameworkOutcome"] = []
    root_pending: List["FrameworkOutcome"] = []
    root_gone: List["FrameworkOutcome"] = []
    for outcome in outcomes:
        if outcome.root_gone_runs >= ROOT_GONE_REMOVAL_RUNS and not outcome.blocked:
            cleanups.append(FrameworkCleanup(
                outcome.framework_id,
                Config.get_framework_output_dir(outcome.framework_id),
                Config.get_hash_file(outcome.framework_id),
                remove=True,
            ))
        elif outcome.root_gone_runs and not outcome.blocked:
            dirs, hash_files = _framework_on_disk(Config.get_framework_output_dir(outcome.framework_id),
                                                  Config.get_hash_file(outcome.framework_id))
            # While either exists, the framework's save kept the count for the next run
            (root_pending if dirs or hash_files else root_gone).append(outcome)
        elif outcome.skip_cleanup:
            skipped.append(outcome)
        elif outcome.orphan_scan is not None:
            cleanups.append(plan_cleanup(outcome.framework_id, outcome.orphan_scan))
    report = delete_orphans(cleanups, interactive)
    _print_summary(report, skipped, root_pending, root_gone)
    return report


def collect_all_orphans(skip_frameworks: Iterable[str] = ()) -> Dict[str, List[Path]]:
    """Collect orphaned files from all frameworks, from each one's persisted session.

    For the standalone check (main), outside a scrape. A framework whose
    orphans trip the valve is skipped: confirm-then-delete belongs to the
    scrape, whose two clean runs confirm a mass removal. So is a framework
    whose hash file's last save came from a scrape that didn't finish its
    discovery or whose cleanup was blocked (HashManager.partial): only the
    pages that scrape reached carry its session, so every other live page
    would look orphaned.

    Args:
        skip_frameworks: Framework ids (any casing) whose cleanup is blocked
            this run, e.g. by a failed request of ours; none of their files
            are collected.
    """
    cleanups, _, _ = _collect(skip_frameworks)
    return {cleanup.framework: cleanup.delete for cleanup in cleanups}


def _collect(
    skip_frameworks: Iterable[str] = (),
) -> Tuple[List[FrameworkCleanup], Dict[str, Tuple[int, int]], List[str]]:
    """Each framework's orphans from its persisted session (see collect_all_orphans).

    Returns:
        The frameworks' cleanups; framework -> (orphans, files) for each
        framework the valve skips; and the frameworks skipped because their
        last save came from an interrupted or blocked scrape (nothing of
        either kind of skipped framework is deleted or written)
    """
    hash_dir = Path(".hashes")
    doc_dir = Path("documentation")

    if not hash_dir.exists() or not doc_dir.exists():
        return [], {}, []

    cleanups = []
    held: Dict[str, Tuple[int, int]] = {}
    partial: List[str] = []
    skip = {framework.lower() for framework in skip_frameworks}

    # Get all hash files
    hash_files = list(hash_dir.glob("*_hashes.json"))

    for hash_file in hash_files:
        framework_name = hash_file.stem.replace("_hashes", "")
        if framework_name.lower() in skip:
            logger.info("orphan_cleanup_skipped", framework=framework_name)
            continue

        # Load hash manager
        hash_manager = HashManager(hash_file)
        if hash_manager.partial:
            logger.warning("orphan_cleanup_skipped_partial", framework=framework_name)
            partial.append(framework_name)
            continue

        # Get framework directory, in any casing
        framework_dirs = [path for path in same_name_any_case(doc_dir / framework_name) if path.is_dir()]
        if not framework_dirs:
            continue
        framework_dir = framework_dirs[0]

        # Find orphaned files
        all_files = HashManager.framework_files(framework_dir)
        orphaned_files = hash_manager.get_orphaned_files(framework_dir, all_files)

        if orphaned_files:
            # Safety check
            if valve_trips(len(orphaned_files), len(all_files)):
                logger.warning(f"Skipping {framework_name}: too many orphans ({len(orphaned_files)}/{len(all_files)})")
                held[framework_name] = (len(orphaned_files), len(all_files))
                continue

            cleanups.append(FrameworkCleanup(
                framework_name, framework_dir, hash_file, files=len(all_files), delete=orphaned_files
            ))

    return cleanups, held, partial


def main() -> None:
    """Main entry point."""
    print("🔍 Collecting orphaned files across all frameworks...")

    cleanups, held, partial = _collect()

    if held:
        print(f"⏸️  Not deleted, held by the valve (at least half of a framework's files, or over 1,000) in "
              f"{len(held)} frameworks; the scrape's cleanup deletes them once two clean runs find them "
              "orphaned (pending_orphans):")
        for framework, (orphans, files) in sorted(held.items()):
            print(f"   - {framework}: {orphans} of {files} files")
    if partial:
        print(f"⏸️  Skipped {len(partial)} frameworks whose hash file was last saved by a scrape that didn't "
              "reach all their pages (interrupted, or blocked by a failure: partial_session): every page it "
              "didn't reach would look orphaned. The next scrape that finishes each one unblocked clears this: "
              + ", ".join(sorted(partial)))

    if not cleanups:
        print("✅ No other orphaned files found" if held or partial else "✅ No orphaned files found!")
        return

    report = delete_orphans(cleanups, interactive=True)
    if report.deleted:
        print(f"\n✅ Deleted {sum(report.deleted.values())} orphaned files")
    if report.pruned:
        print(f"🧹 Pruned {report.pruned} hash entries for deleted files")
    for failure in report.failures:
        print(f"❌ {failure}")


if __name__ == "__main__":
    main()
