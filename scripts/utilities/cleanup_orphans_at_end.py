#!/usr/bin/env python3
"""
Delete orphaned files at the end of scraping.

The scrape (scrape.py --cleanup-orphans) cleans from each framework's result,
computed right after its hash file was saved (cleanup_after_scrape): only the
frameworks scraped this run, never one whose run hit a failure of ours. It
deletes through delete_orphans, presenting them once for approval unless the
cleanup is automatic.

It also removes the D6 modules no longer linked, automatically (rules 1–4 of
todo-4's D6 design): a module's parents are pruned when they are deleted or
gone (rule 3), each clean parent run counts whether it routed the module a
page (rule 2), a module is cleaned only when every parent ran clean (rule 1),
and it is deleted, dir and hash file, once it has no parent left, every
parent's count reached MODULE_UNLINKED_RUNS, or its dir holds no file after
its cleanup (rule 4).

The DocC sites' docs (documentation/<namespace>/) follow the same rules, each
on its own site's paths (.hashes/<namespace>/), with outcomes keyed by (site,
id). Before anything else, the docs that left the config are removed
(rule 7(a)): a top-level hash file whose root the site no longer lists, with
its dir, and a whole namespace whose site left the config, or whose
package's index is gone (row 3).
"""

import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Dict, Final, List, Mapping, Optional, Sequence, Set, Tuple

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scraper.config import Config
from scraper.sink import (
    CHILD_MODULES_KEY, HANDOFF_KEY, HASH_FILE_SUFFIX, MODULE_KEY, metadata_ids, module_metadata, module_parents,
)
from scraper.utils.hash_manager import COUNTER_FIELDS, HashManager, same_name_any_case, valve_trips
from scraper.utils.logger import get_logger

if TYPE_CHECKING:
    from scraper.json_scraper import FrameworkOutcome, ModuleScan, OrphanScan, RunSinks, SiteRemoval

# An outcome's key: (its site's name, its id lowercased)
Key = Tuple[str, str]

logger = get_logger(__name__)

# A framework whose root returned 404/410 on this many consecutive runs is
# removed (its docs dir and hash file); the two runs are the confirmation
ROOT_GONE_REMOVAL_RUNS: Final = 2

# A D6 module is removed once each of its parents ran clean this many runs in
# a row without routing it a page (rule 4)
MODULE_UNLINKED_RUNS: Final = 2

# Why a framework or module is removed (FrameworkCleanup.reason), for the log
# and the summary
ROOT_GONE: Final = "root_gone"
# A DocC root or site that left the config (rule 7(a)); a navigator-index
# site's root its index stopped listing, or the whole package once its index
# is gone (row 3). Each is a SiteRemoval's reason
NOT_CONFIGURED: Final = "not_configured"
UNLISTED: Final = "unlisted"
INDEX_GONE: Final = "index_gone"
SITE_REASONS: Final = {
    NOT_CONFIGURED: "its root left the config",
    UNLISTED: "its package's index hasn't listed it on 2 consecutive loads",
    INDEX_GONE: "its package's index returned 404/410 on 2 consecutive runs",
}
MODULE_REASONS: Final = {
    "module_parentless": "no parent left",
    "module_unlinked": f"unlinked by every parent for {MODULE_UNLINKED_RUNS} clean runs",
    "module_empty": "no file left after its cleanup",
}


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
            hash file: its root returned 404/410 on 2 consecutive runs, a
            DocC root that left the config, or a D6 module rule 4 deletes
        reason: Why it is removed: ROOT_GONE, one of SITE_REASONS, or one of MODULE_REASONS
        drop: The error entries no page links to any more
            (json_scraper.stale_error_entries), dropped from its hash file
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
    reason: str = ROOT_GONE
    drop: List[str] = field(default_factory=list)


@dataclass
class CleanupReport:
    """What an orphan cleanup did, for the end-of-run summary and the exit code.

    Attributes:
        deleted: framework -> orphaned files deleted
        confirmed: framework -> of those, files confirmed from pending_orphans
        held: framework -> (orphans the valve holds in pending_orphans, the
            framework's files once the confirmed ones are deleted)
        removed: framework -> .md files in the removed framework's docs dir
        unconfigured: DocC root or whole site that left the config, or its
            package's index (rule 7(a)) -> .md files its removed docs dir held
        removed_modules: D6 module -> (.md files its docs dir held, why: a
            MODULE_REASONS key)
        parents_pruned: D6 module -> the parents pruned from it (rule 3)
        pruned: Hash entries pruned for deleted files
        dropped: Error entries dropped that no page links to any more
        cancelled: The user declined the deletion (interactive cleanup)
        failures: What failed (a deletion, or a hash-file write that lost a
            prune or a pending_orphans change): errors for the run
    """

    deleted: Dict[str, int] = field(default_factory=dict)
    confirmed: Dict[str, int] = field(default_factory=dict)
    held: Dict[str, Tuple[int, int]] = field(default_factory=dict)
    removed: Dict[str, int] = field(default_factory=dict)
    unconfigured: Dict[str, int] = field(default_factory=dict)
    removed_modules: Dict[str, Tuple[int, str]] = field(default_factory=dict)
    parents_pruned: Dict[str, List[str]] = field(default_factory=dict)
    pruned: int = 0
    dropped: int = 0
    cancelled: bool = False
    failures: List[str] = field(default_factory=list)

    def merge(self, other: "CleanupReport") -> None:
        """Add another part of the same cleanup's report to this one."""
        self.deleted.update(other.deleted)
        self.confirmed.update(other.confirmed)
        self.held.update(other.held)
        self.removed.update(other.removed)
        self.unconfigured.update(other.unconfigured)
        self.removed_modules.update(other.removed_modules)
        self.parents_pruned.update(other.parents_pruned)
        self.pruned += other.pruned
        self.dropped += other.dropped
        self.cancelled = self.cancelled or other.cancelled
        self.failures.extend(other.failures)


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
    cleanup.drop = list(scan.stale_errors)
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
    """Remove a framework whose root returned 404/410 on 2 consecutive runs, or a D6 module rule 4 deletes."""
    try:
        files = remove_framework(cleanup.framework, cleanup.framework_dir, cleanup.hash_file, reason=cleanup.reason)
    except OSError as e:
        report.failures.append(f"{cleanup.framework}: removal failed: {e}")
        return
    if cleanup.reason == ROOT_GONE:
        report.removed[cleanup.framework] = files
    elif cleanup.reason in SITE_REASONS:
        report.unconfigured[cleanup.framework] = files
    else:
        report.removed_modules[cleanup.framework] = (files, cleanup.reason)


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

    Reloads the framework's hash file and saves once; a pending_orphans
    change is saved even when nothing else changed. Also drops the error
    entries no page links to any more (cleanup.drop).

    Returns:
        False if the write failed (reported in report.failures)
    """
    hash_manager = HashManager(cleanup.hash_file, cleanup.framework_dir)
    if hash_manager.load_error is not None:
        # Never replace a hash file we can't read with what this write holds
        report.failures.append(f"{cleanup.framework}: hash file failed to load: {hash_manager.load_error}")
        return False
    pruned = hash_manager.prune_missing_files() if prune else 0
    if cleanup.pending_orphans is not None:
        hash_manager.set_metadata("pending_orphans", cleanup.pending_orphans)
    dropped = 0
    for url in cleanup.drop:
        # Still an error entry no run counter keeps (the save left it so)
        entry = hash_manager.hashes.get(url)
        if (isinstance(entry, dict) and entry.get("status") == "error" and not entry.get("file_path")
                and not any(counter in entry for counter in COUNTER_FIELDS)):
            hash_manager.remove(url)
            dropped += 1
    if not hash_manager.save():
        # Lost: a prune, or a pending_orphans change (a hold confirmed one
        # run later, or a list that should be dropped)
        report.failures.append(f"{cleanup.framework}: hash file save failed ({cleanup.hash_file})")
        return False
    report.pruned += pruned
    report.dropped += dropped
    if pruned:
        logger.info("pruned_hash_entries", framework=cleanup.framework, pruned=pruned)
    if dropped:
        logger.info("dropped_stale_error_entries", framework=cleanup.framework, dropped=dropped)
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
            why = (f"its root returned 404/410 on {ROOT_GONE_REMOVAL_RUNS} runs" if cleanup.reason == ROOT_GONE
                   else SITE_REASONS[cleanup.reason] if cleanup.reason in SITE_REASONS
                   else f"a module with {MODULE_REASONS[cleanup.reason]}")
            print(f"\n📁 {cleanup.framework}: {why}; its docs dir and hash file will be removed")
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
    what each deletes is decided by the caller (cleanup_after_scrape).

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
        if deleted or cleanup.pending_orphans is not None or cleanup.drop:
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


def _print_summary(report: CleanupReport, skipped: Sequence["FrameworkOutcome"],
                   root_pending: Sequence["FrameworkOutcome"], root_gone: Sequence["FrameworkOutcome"],
                   waiting: Sequence[Tuple[str, str]] = ()) -> None:
    """The end-of-run summary of the orphan cleanup.

    root_pending: frameworks whose root returned 404/410 this run, removed if
    it does again on the next run; root_gone: those with no docs dir or hash
    file left to remove (e.g. still listed after their removal), which
    nothing in the cleanup can change; waiting: the sinks rule 1 leaves
    alone this run, with why (a writer that didn't run clean).
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
    if report.dropped:
        print(f"🧹 Dropped {report.dropped} error entries no page links to any more")
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
    if report.unconfigured:
        print(f"🗑️  Removed {len(report.unconfigured)} DocC roots or sites that left the config or their package's "
              f"index (docs and hash files): "
              + ", ".join(f"{name} ({files} files)" for name, files in sorted(report.unconfigured.items())))
    if report.removed_modules:
        print(f"🗑️  Removed {len(report.removed_modules)} modules (docs dir and hash file): "
              + ", ".join(f"{module} ({files} files, {MODULE_REASONS[reason]})"
                          for module, (files, reason) in sorted(report.removed_modules.items())))
    if report.parents_pruned:
        print("✂️  Parents pruned from modules (deleted or gone): "
              + ", ".join(f"{module} ({', '.join(parents)})" for module, parents in sorted(report.parents_pruned.items())))
    if root_pending:
        print("⏳ Root returned 404/410 (removed if it does again next run): "
              + ", ".join(f"{outcome.name} (run {outcome.root_gone_runs})" for outcome in root_pending))
    if root_gone:
        print("ℹ️  Root returned 404/410, with no docs dir or hash file left to remove: "
              + ", ".join(outcome.name for outcome in root_gone))
    if skipped:
        print(f"⏸️  Cleanup skipped this run for {len(skipped)} frameworks: "
              + ", ".join(f"{outcome.name} ({describe_skip(outcome)})" for outcome in skipped))
    if waiting:
        print(f"⏸️  Not cleaned this run (rule 1) ({len(waiting)}): "
              + ", ".join(f"{name} ({why})" for name, why in waiting))
    for failure in report.failures:
        print(f"❌ {failure}")
    if not (report.deleted or report.held or report.removed or report.unconfigured or report.removed_modules
            or report.cancelled or report.failures):
        if skipped or root_pending or waiting:
            print("✅ No orphaned files found in the frameworks cleaned this run")
        else:
            print("✅ No orphaned files found!")


def _ran_clean(outcomes: Mapping[Key, "FrameworkOutcome"], key: Key) -> bool:
    """The job ran this run and ran clean: its cleanup isn't skipped (rule 1)."""
    outcome = outcomes.get(key)
    return outcome is not None and not outcome.skip_cleanup


def _gone(key: Key, namespace: str, outcomes: Mapping[Key, "FrameworkOutcome"], removed: Set[Key]) -> bool:
    """Rule 3: a parent (or handoff writer) is pruned once deleted, or gone.

    Deleted by this run's cleanup (root gone, or left the config), or didn't
    run this run and has no hash file left at its own site's path
    (.hashes/[<namespace>/]<id>_hashes.json, any casing): the pre-scrape's
    unlisted removal deletes it, and a renamed parent's old id goes that
    way. Never for "not in technologies.json" (or the config's roots)
    alone: a parent unlisted for one run still has its hash file and keeps
    its modules.
    """
    if key in removed:
        return True
    if key in outcomes:
        return False
    hash_file = Config.get_hash_file(key[1], namespace=namespace)
    return not any(path.is_file() for path in same_name_any_case(hash_file))


def _save(hash_manager: HashManager, name: str, report: CleanupReport) -> bool:
    """Save a reloaded hash file; a failure is an error for the run."""
    if hash_manager.save():
        return True
    report.failures.append(f"{name}: hash file save failed ({hash_manager.cache_file})")
    return False


def _unique(paths: Sequence[Path]) -> List[Path]:
    """The paths, each once in any casing, in order."""
    seen: Set[str] = set()
    unique = []
    for path in paths:
        if str(path).lower() not in seen:
            seen.add(str(path).lower())
            unique.append(path)
    return unique


def prune_handoff_writers(run: "RunSinks", outcomes: Mapping[Key, "FrameworkOutcome"], removed: Set[Key],
                          report: CleanupReport) -> Dict[Key, Set[str]]:
    """Rule 3 for the handoff writers a top-level hash file records (metadata.handoff_from).

    Returns:
        (Its site, hash file id lowercased) -> the writers pruned from it
    """
    pruned: Dict[Key, Set[str]] = {}
    for path in _unique(run.handoff_files):
        if not path.is_file():
            continue
        site, namespace = run.site_of(path)
        name = path.name[: -len(HASH_FILE_SUFFIX)]
        hash_manager = HashManager(path)
        if hash_manager.load_error is not None:
            report.failures.append(f"{name}: hash file failed to load: {hash_manager.load_error}")
            continue
        writers = metadata_ids(hash_manager.get_metadata(HANDOFF_KEY))
        gone = {writer for writer in writers if _gone((site, writer), namespace, outcomes, removed)}
        if not gone:
            continue
        hash_manager.set_metadata(HANDOFF_KEY, {writer: value for writer, value in writers.items() if writer not in gone})
        if _save(hash_manager, name, report):
            logger.info("handoff_writers_pruned", framework=name, pruned=sorted(gone))
            pruned[(site, name.lower())] = gone
    return pruned


def _prune_child_module(module: str, parent_files: Sequence[Path], report: CleanupReport) -> None:
    """Drop a module from its parents' metadata.child_modules (deleted, or promoted)."""
    for path in _unique(parent_files):
        for found in same_name_any_case(path):
            if not found.is_file():
                continue
            hash_manager = HashManager(found)
            children = metadata_ids(hash_manager.get_metadata(CHILD_MODULES_KEY))
            if hash_manager.load_error is not None or module.lower() not in children:
                continue
            del children[module.lower()]
            hash_manager.set_metadata(CHILD_MODULES_KEY, children)
            _save(hash_manager, found.name[: -len(HASH_FILE_SUFFIX)], report)


@dataclass
class ModuleState:
    """A D6 module's state in this run's end-of-run cleanup.

    Attributes:
        name: Its id, as its hash file spells it
        output_dir: Its docs dir
        hash_file: Its hash file
        parent_files: Its parents' hash files (to drop it from their child_modules)
        eligible: Every remaining parent ran this run and ran clean (rule 1)
        routed: A parent routed it a page this run (it has a sink)
        display: Its name for the console and the report: its id, under its
            site's namespace
    """

    name: str
    output_dir: Path
    hash_file: Path
    parent_files: List[Path]
    eligible: bool
    routed: bool = False
    display: str = ""

    def __post_init__(self) -> None:
        self.display = self.display or self.name


def apply_module_rules(run: "RunSinks", outcomes: Mapping[Key, "FrameworkOutcome"], removed: Set[Key],
                       report: CleanupReport) -> Tuple[List[FrameworkCleanup], List[ModuleState]]:
    """Rules 3, 2 and 1 for every D6 module hash file, and what rule 4 removes at once.

    Over the module files on disk at run start and the run's module sinks,
    so a module no parent linked this run is counted too (it has no sink).
    Each is judged on its own site: its parents are jobs of that site, and
    their hash files are at its namespace's path. A module whose id this
    run's technologies.json (or its site's allow-list) lists is promoted: rules
    2–4 skip it (its own job dropped its module key) and its parents' hash
    files no longer list it in child_modules. For each other module, in
    this order:
    - rule 3: its deleted or gone parents are pruned (_gone);
    - rule 2: each parent that ran clean resets its counter if it routed
      the module a page this run (at the routing decision), else counts on;
    - rule 1: it is eligible when every remaining parent ran this run and
      ran clean;
    - rule 4: removed when no parent is left (not gated by rule 1, since
      its parents no longer run), or when eligible and every counter reached
      MODULE_UNLINKED_RUNS; otherwise an eligible module with a sink this
      run gets its orphan pass (valve, confirm-then-delete), even with an
      empty touched set. The empty-dir branch runs after that pass
      (remove_empty_modules).

    Returns:
        The orphan cleanups and removals to run (delete_orphans), and the
        modules' states (for the empty-dir branch)
    """
    scans: Dict[str, "ModuleScan"] = {str(module.hash_file).lower(): module for module in run.modules}
    cleanups: List[FrameworkCleanup] = []
    states: List[ModuleState] = []
    for path in _unique([*run.module_files, *(module.hash_file for module in run.modules)]):
        site, namespace = run.site_of(path)
        name = path.name[: -len(HASH_FILE_SUFFIX)]
        display = f"{namespace}/{name}" if namespace else name
        children = run.child_modules.get((site, name.lower()), [])
        if (site, name.lower()) in run.listed:
            _prune_child_module(name, children, report)
            continue
        if not path.is_file():
            continue
        hash_manager = HashManager(path)
        if hash_manager.load_error is not None:
            report.failures.append(f"{name}: hash file failed to load: {hash_manager.load_error}")
            continue
        module = hash_manager.get_metadata(MODULE_KEY)
        if not module:
            continue
        scan = scans.get(str(path).lower())
        routed = scan.routed_by if scan is not None else set()
        parents = module_parents(module)
        parent_files = [Config.get_hash_file(parent, namespace=namespace) for parent in parents] + children
        gone = sorted(parent for parent in parents if _gone((site, parent), namespace, outcomes, removed))
        for parent in gone:
            del parents[parent]
        for parent in parents:
            if _ran_clean(outcomes, (site, parent)):
                parents[parent] = 0 if parent in routed else parents[parent] + 1
        updated = module_metadata(module.get("bundle") if isinstance(module, dict) else None, parents)
        if updated != module:
            hash_manager.set_metadata(MODULE_KEY, updated)
            if not _save(hash_manager, name, report):
                continue
        if gone:
            logger.info("module_parents_pruned", module=display, pruned=gone)
            report.parents_pruned[display] = gone
        output_dir = (scan.output_dir if scan is not None
                      else Config.get_framework_output_dir(name, namespace=namespace))
        eligible = bool(parents) and all(_ran_clean(outcomes, (site, parent)) for parent in parents)
        state = ModuleState(name, output_dir, path, parent_files, eligible, routed=scan is not None, display=display)
        if not parents or (eligible and all(runs >= MODULE_UNLINKED_RUNS for runs in parents.values())):
            reason = "module_parentless" if not parents else "module_unlinked"
            logger.warning("module_removal", module=display, reason=reason, parents=parents)
            cleanups.append(FrameworkCleanup(display, output_dir, path, remove=True, reason=reason))
            states.append(state)
            continue
        states.append(state)
        if eligible and scan is not None and scan.orphan_scan is not None:
            cleanups.append(plan_cleanup(display, scan.orphan_scan))
    return cleanups, states


def remove_empty_modules(states: Sequence[ModuleState], report: CleanupReport) -> None:
    """Rule 4's last branch: an eligible module whose dir holds no file after its orphan pass is removed.

    E.g. every page answers 404/410 while still linked: the pages left
    through confirm-then-delete first, and the module goes with its hash
    file now.
    """
    for state in states:
        if not state.eligible or state.display in report.removed_modules or not state.hash_file.is_file():
            continue
        dirs = [path for path in same_name_any_case(state.output_dir) if path.is_dir()]
        if any(HashManager.framework_files(path) for path in dirs):
            continue
        logger.warning("module_removal", module=state.display, reason="module_empty")
        _remove_framework(FrameworkCleanup(state.display, state.output_dir, state.hash_file, remove=True,
                                           reason="module_empty"), report)


def remove_namespace(removal: "SiteRemoval", report: CleanupReport) -> None:
    """Rule 7(a) for a DocC site that left the config, or a package whose index is gone: its
    whole namespace goes, docs dir and hash dir (every top-level and module hash file, and _site.json)."""
    files = len(HashManager.framework_files(removal.output_dir)) if removal.output_dir.is_dir() else 0
    try:
        for path in (removal.output_dir, removal.hash_file):
            if path.is_dir():
                shutil.rmtree(path)
    except OSError as e:
        logger.error("site_removal_failed", site=removal.name, error=str(e))
        report.failures.append(f"{removal.name}: removal failed: {e}")
        return
    logger.warning("site_removed", site=removal.name, reason=removal.reason, files=files,
                   dirs=[str(removal.output_dir), str(removal.hash_file)])
    report.unconfigured[removal.name] = files


def cleanup_after_scrape(outcomes: Sequence["FrameworkOutcome"], interactive: bool,
                         run: Optional["RunSinks"] = None) -> CleanupReport:
    """The scrape's end-of-run orphan cleanup, from each framework's result.

    Only frameworks scraped this run are cleaned (others have no result),
    each from the orphan candidates found right after its hash file was
    saved (FrameworkOutcome.orphan_scan; a multi-writer sink's at the end of
    the run), with confirm-then-delete for mass removals (plan_cleanup). A
    framework blocked by a failure of ours, or that raised, is never
    cleaned; neither is one whose root returned 404/410 this run, until it
    has on 2 consecutive runs: it is then removed outright (docs dir and
    hash file, its own sink's: FrameworkOutcome.paths), bypassing the
    zero-touched guard and the valve. With neither left (a still-listed
    framework after its removal), its root_gone_runs isn't saved
    (HashManager.save), so it stays at 1 and the summary says there is
    nothing left to remove.

    With the run's sinks (run), the D6 rules, in this order: the
    framework deletions first (rule 7(a): the DocC docs that left the
    config; root gone ×2, rule 7(b) for a DocC root), then rule 3's prunes
    of deleted or gone parents and handoff writers, then rule 2's counters,
    rule 1's eligibility, the eligible sinks' orphan pass, and rule 4's
    module removals (apply_module_rules, remove_empty_modules). A top-level
    framework with handoff writers is cleaned only if each of them ran
    clean too (rule 1). Outcomes are keyed by (site, id).

    Args:
        outcomes: The run's framework outcomes
        interactive: Ask before deleting (delete_orphans)
        run: The run's sinks (scrape_frameworks' run_sinks)

    Returns:
        The report; its failures are errors for the run
    """
    by_key: Dict[Key, "FrameworkOutcome"] = {outcome.key: outcome for outcome in outcomes}
    removals: List[FrameworkCleanup] = []
    removal_keys: Dict[str, Set[Key]] = {}
    report = CleanupReport()
    for removal in (run.removals if run is not None else []):
        if removal.framework_id:
            removals.append(FrameworkCleanup(removal.name, removal.output_dir, removal.hash_file,
                                             remove=True, reason=removal.reason))
            removal_keys.setdefault(removal.name, set()).add((removal.site, removal.framework_id.lower()))
        else:
            # A whole site: every top-level id of its namespace is removed with it
            ids = {path.name[: -len(HASH_FILE_SUFFIX)].lower()
                   for path in removal.hash_file.glob(f"*{HASH_FILE_SUFFIX}")} if removal.hash_file.is_dir() else set()
            if interactive and not _approved([FrameworkCleanup(removal.name, removal.output_dir, removal.hash_file,
                                                               remove=True, reason=removal.reason)]):
                report.cancelled = True
                continue
            remove_namespace(removal, report)
            if removal.name in report.unconfigured:
                removal_keys[removal.name] = {(removal.site, framework) for framework in ids}
    for outcome in outcomes:
        if outcome.root_gone_runs >= ROOT_GONE_REMOVAL_RUNS and not outcome.blocked:
            output_dir, hash_file = outcome.paths
            removals.append(FrameworkCleanup(outcome.name, output_dir, hash_file, remove=True))
            removal_keys.setdefault(outcome.name, set()).add(outcome.key)
    if removals:
        report.merge(delete_orphans(removals, interactive))
    removed = {key for name, keys in removal_keys.items()
               if name in report.removed or name in report.unconfigured for key in keys}

    pruned_writers: Dict[Key, Set[str]] = {}
    module_cleanups: List[FrameworkCleanup] = []
    states: List[ModuleState] = []
    if run is not None:
        pruned_writers = prune_handoff_writers(run, by_key, removed, report)
        module_cleanups, states = apply_module_rules(run, by_key, removed, report)

    cleanups: List[FrameworkCleanup] = []
    skipped: List["FrameworkOutcome"] = []
    root_pending: List["FrameworkOutcome"] = []
    root_gone: List["FrameworkOutcome"] = []
    waiting: List[Tuple[str, str]] = []
    for outcome in outcomes:
        if outcome.key in removed:
            continue
        if outcome.root_gone_runs >= ROOT_GONE_REMOVAL_RUNS and not outcome.blocked:
            continue
        if outcome.root_gone_runs and not outcome.blocked:
            dirs, hash_files = _framework_on_disk(*outcome.paths)
            # While either exists, the framework's save kept the count for the next run
            (root_pending if dirs or hash_files else root_gone).append(outcome)
        elif outcome.skip_cleanup:
            skipped.append(outcome)
        elif outcome.orphan_scan is not None:
            pruned = pruned_writers.get(outcome.key, set())
            unclean = [writer for writer in outcome.handoff_writers
                       if writer not in pruned and not _ran_clean(by_key, (outcome.site, writer))]
            if unclean:
                logger.info("cleanup_waits_for_writers", framework=outcome.name, writers=unclean)
                waiting.append((outcome.name,
                                f"handoff writer {', '.join(unclean)} didn't run, or didn't run clean"))
                continue
            cleanups.append(plan_cleanup(outcome.name, outcome.orphan_scan))
    report.merge(delete_orphans(cleanups + module_cleanups, interactive))
    removing = {cleanup.framework for cleanup in module_cleanups if cleanup.remove}
    for state in states:
        if state.routed and not state.eligible and state.display not in removing:
            waiting.append((state.display, "a parent didn't run, or didn't run clean"))
    for state in states:
        if state.display in removing and state.display in report.removed_modules:
            _prune_child_module(state.name, state.parent_files, report)
    if run is not None and not report.cancelled:
        removed_before = set(report.removed_modules)
        remove_empty_modules(states, report)
        for state in states:
            if state.display in report.removed_modules and state.display not in removed_before:
                _prune_child_module(state.name, state.parent_files, report)
    _print_summary(report, skipped, root_pending, root_gone, waiting)
    return report
