#!/usr/bin/env python3
"""
One-off migration of the Apple docs to the seg_name file names (todo-3 4.1).

The scraper names every page through scraper.utils.naming (seg_name and the
path rule, a function of the URL alone). This script moves each live Apple
page's file to the path the scraper itself now gives it
(AppleJSONDocumentationScraper._get_organized_file_path, imported and called:
any divergence would be an orphan in the next scrape) and records it there,
so the next scrape deletes nothing because of the rename.

1. Every live Apple page, judged by its JSON-URL key as the scraper does
   (_is_previously_good; its doc-URL key follows it), gets its new path.
2. Pages are grouped by their recorded file, case-insensitively. A file
   recorded by one page is that page's. A file several pages record (they
   overwrote each other under the old names) is the page's whose doc URL its
   footer (*[View on Apple Developer](<url>)*) names; the others get no file
   (the next scrape writes theirs). A live page whose file isn't on disk is
   file-less: only its recorded path changes.
3. Nothing is touched unless every check passes: no case-duplicate keys
   left (the D5 normalization drops them); every new path is one page's; a
   moved file's new path is free (not on disk, not another moved file's old
   path); a non-owner's new path is free or the old path of a shared file
   whose owner moves away; a file-less page's new path is free or a file
   that moves away; and a tracked .md in an Apple docs dir that no
   live entry records (a pending removal, deleted by the next scrape's
   cleanup) isn't a live page's file (its footer names no live page).
4. The files are renamed (os.rename; `git add -A` sees the renames), and
   the dirs they leave empty are removed.
5. Every live page's keys record its new path (HashManager.set_file_path:
   hash and counters untouched), metadata.pending_orphans follows the
   renames (matched case-insensitively), and the changed hash files are
   saved.

A second run, once the renames are committed, renames nothing and changes no
hash file; its file-less pages are exactly the first run's non-owners.

Usage (from the repo root, on the merged code, after the D5 normalization of
.hashes, with no scrape run in progress):
    python scripts/utilities/migrate_filenames.py --dry-run [--plan FILE]  # Check and report; change nothing
    python scripts/utilities/migrate_filenames.py [--plan FILE]            # Migrate

--plan writes every rename, non-owner, file-less page and pending removal,
tab-separated (kind, framework, JSON URL, old path, new path).

Exit code: 0, or 1 if a check failed, a hash file failed to load or save, or
a rename failed (a failed check changes nothing).
"""

import argparse
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Final, List, Optional, Set, TextIO, Tuple

# The repo root, for the scraper package
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.hash_manager import HashManager, read_hash_file
from scraper.utils.logger import setup_logging
from scraper.utils.naming import DOC_URL_PREFIX, HASH_FILE_SUFFIX, JSON_URL_PREFIX, dirmap

DOCS_ROOT: Final = Path("documentation")
HASH_DIR: Final = Path(".hashes")
# The last line of every Apple page (metadata_extractor's footer pattern)
FOOTER: Final = re.compile(r'^\*\[View on Apple Developer\]\((https?://\S+)\)\*$')
# How many examples of each failed check are printed
EXAMPLES: Final = 10
COLLISIONS: Final = "new paths of several pages"


@dataclass
class Page:
    """A live Apple page: its JSON-URL key's entry records a file and isn't an error."""

    framework: str
    json_url: str  # its JSON-URL key
    doc_url: str
    keys: List[str]  # its keys: the JSON URL's and the doc URL's
    old: str  # the file its JSON-URL key records
    new: str  # the scraper's path
    on_disk: Optional[str] = None  # the old file as on disk (any casing); None: file-less
    owner: bool = False  # it keeps the file (its only page, or the one its footer names)

    @property
    def identity(self) -> str:
        """URL identity: the lowercased JSON URL (URL space is case-insensitive)."""
        return self.json_url.lower()


@dataclass
class Plan:
    """What the migration does, or would do."""

    managers: Dict[str, HashManager] = field(default_factory=dict)  # framework -> its hash file
    pages: List[Page] = field(default_factory=list)
    renames: List[Tuple[Page, str]] = field(default_factory=list)  # (owner, its new path), path changes
    staying: int = 0  # owners whose path doesn't change
    shared_files: int = 0
    non_owners: List[Page] = field(default_factory=list)
    vacated_targets: int = 0  # non-owners whose new path is a file its owner moves away from
    file_less: List[Page] = field(default_factory=list)
    orphans: List[Tuple[str, str]] = field(default_factory=list)  # (framework, tracked .md no live entry records)
    keys_to_rewrite: int = 0
    hash_files_to_save: Set[str] = field(default_factory=set)
    failures: Dict[str, List[str]] = field(default_factory=dict)  # check -> examples

    def fail(self, check: str, detail: str) -> None:
        self.failures.setdefault(check, []).append(detail)


def footer_url(path: str) -> Optional[str]:
    """The URL in a page file's footer (its last non-empty line), if it has one."""
    with open(path, 'rb') as f:
        f.seek(0, os.SEEK_END)
        f.seek(max(0, f.tell() - 4096))
        tail = f.read().decode('utf-8', 'replace')
    for line in reversed(tail.splitlines()):
        if line.strip():
            match = FOOTER.match(line.strip())
            return match.group(1) if match else None
    return None


def identity_of(key: str) -> Optional[str]:
    """The URL identity (lowercased JSON URL) of a JSON-URL or doc-URL key; None for any other key."""
    if key.startswith(JSON_URL_PREFIX):
        return key.lower()
    if key.startswith(DOC_URL_PREFIX):
        return f"{JSON_URL_PREFIX}{key[len(DOC_URL_PREFIX):]}.json".lower()
    return None


def tracked_docs() -> List[str]:
    """The files git tracks under documentation/."""
    out = subprocess.run(
        ["git", "ls-files", "-z", "--", str(DOCS_ROOT)], capture_output=True, check=True
    ).stdout
    return [os.fsdecode(path) for path in out.split(b"\0") if path]


def files_on_disk(frameworks: Dict[str, str], plan: Plan) -> Dict[str, str]:
    """Every file under the Apple docs dirs (any casing), lowercased path -> path."""
    found: Dict[str, str] = {}
    if not DOCS_ROOT.is_dir():
        return found
    for entry in sorted(os.listdir(DOCS_ROOT)):
        if entry.lower() not in frameworks:
            continue
        for dirpath, _dirs, files in os.walk(DOCS_ROOT / entry):
            for name in files:
                path = os.path.join(dirpath, name)
                if path.lower() in found:
                    plan.fail("files differing only in case", f"{found[path.lower()]} | {path}")
                found[path.lower()] = path
    return found


def load(plan: Plan) -> Dict[str, str]:
    """Steps 1-2: every live Apple page with its new path, and who keeps each shared file.

    Returns:
        The files under the Apple docs dirs, lowercased path -> path
    """
    frameworks = dirmap(HASH_DIR)
    # A hash file dirmap couldn't read might be a framework's: never guess
    for path in sorted(HASH_DIR.glob(f"*{HASH_FILE_SUFFIX}")):
        if path.name[:-len(HASH_FILE_SUFFIX)].lower() not in frameworks:
            try:
                read_hash_file(path)
            except (OSError, ValueError) as e:
                plan.fail("hash files that can't be read", f"{path}: {e}")

    seen: Dict[str, str] = {}  # identity -> framework, across hash files
    for name in sorted(frameworks.values()):
        scraper = AppleJSONDocumentationScraper(name)
        manager = scraper.hash_manager
        if scraper.framework_id != name or manager.load_error is not None:
            plan.fail("hash files that can't be loaded", f"{name}: {manager.load_error or scraper.framework_id}")
            continue
        plan.managers[name] = manager
        keys: Dict[str, List[str]] = defaultdict(list)
        for key in manager.hashes:
            identity = identity_of(key)
            if identity is not None:
                keys[identity].append(key)
        for identity, its_keys in keys.items():
            if identity in seen and seen[identity] != name:
                plan.fail("pages in two hash files", f"{identity}: {seen[identity]}, {name}")
            seen[identity] = name
            json_keys = [key for key in its_keys if key.startswith(JSON_URL_PREFIX)]
            if len(json_keys) > 1 or len(its_keys) - len(json_keys) > 1:
                plan.fail("case-duplicate keys (the D5 normalization drops them)", ", ".join(sorted(its_keys)))
            json_url = next((key for key in json_keys if key == identity), json_keys[0] if json_keys else None)
            if json_url is None or not scraper._is_previously_good(manager.hashes[json_url]):
                continue
            doc_url = scraper._convert_json_url_to_doc_url(json_url)
            plan.pages.append(Page(
                framework=name,
                json_url=json_url,
                doc_url=doc_url,
                keys=its_keys,
                old=os.path.normpath(manager.hashes[json_url]['file_path']),
                new=str(scraper._get_organized_file_path(scraper.sink, doc_url, {})),
            ))

    disk = files_on_disk(frameworks, plan)
    groups: Dict[str, List[Page]] = defaultdict(list)
    for page in plan.pages:
        page.on_disk = disk.get(page.old.lower())
        if page.on_disk is None:
            plan.file_less.append(page)
        else:
            groups[page.old.lower()].append(page)
    for pages in groups.values():
        if len(pages) == 1:
            pages[0].owner = True
            continue
        plan.shared_files += 1
        on_disk = pages[0].on_disk
        assert on_disk is not None
        footer = footer_url(on_disk)
        owners = [page for page in pages if footer is not None and page.doc_url.lower() == footer.lower()]
        if len(owners) != 1:
            plan.fail(
                "shared files whose footer names no single page",
                f"{on_disk}: footer {footer}, {len(owners)} of {len(pages)} pages",
            )
            continue
        owners[0].owner = True
        plan.non_owners += [page for page in pages if page is not owners[0]]
    return disk


def check(plan: Plan, disk: Dict[str, str]) -> None:
    """Step 3: the checks, before anything is touched; and the renames and rewrites they allow."""
    by_new: Dict[str, Set[str]] = defaultdict(set)
    for page in plan.pages:
        by_new[page.new.lower()].add(page.identity)
    for new, identities in sorted(by_new.items()):
        if len(identities) > 1:
            plan.fail(COLLISIONS, f"{new}: {', '.join(sorted(identities))}")

    owners = [page for page in plan.pages if page.owner]
    # The files that move away (a case-only rename keeps its path)
    moving_old = {page.old.lower() for page in owners if page.new.lower() != page.old.lower()}
    for page in owners:
        if page.on_disk == page.new:
            plan.staying += 1
            continue
        assert page.on_disk is not None
        target = page.new.lower()
        if target in moving_old:
            plan.fail("renames onto another moved file (a chain)", f"{page.on_disk} -> {page.new}")
        elif target in disk and target != page.old.lower():
            plan.fail("renames onto a file that stays", f"{page.on_disk} -> {page.new} ({disk[target]})")
        else:
            plan.renames.append((page, page.new))

    # Shared files whose owner moves away: a non-owner may take over the path
    shared = {page.old.lower() for page in plan.non_owners}
    vacated = moving_old & shared
    for page in plan.non_owners:
        target = page.new.lower()
        if target in disk:
            if target in vacated:
                plan.vacated_targets += 1
            elif target in moving_old:
                plan.fail(
                    "non-owners whose new path is a single page's file that moves away (not a shared file's)",
                    f"{page.json_url}: {page.new}",
                )
            else:
                plan.fail("non-owners whose new path is a file that stays", f"{page.json_url}: {page.new}")
    # A file-less page records its new path: a file there must move away, or
    # the page would take it as its own (an unchanged page keeps that content)
    for page in plan.file_less:
        target = page.new.lower()
        if target in disk and target not in moving_old:
            plan.fail("file-less pages whose new path is a file that stays", f"{page.json_url}: {page.new}")

    live_old = {page.old.lower() for page in plan.pages}
    live_docs = {page.doc_url.lower() for page in plan.pages}
    frameworks = {name.lower(): name for name in plan.managers}
    for path in tracked_docs():
        parts = path.split('/')
        if len(parts) < 3 or parts[1].lower() not in frameworks or not path.endswith('.md'):
            continue
        if path.lower() in live_old:
            continue
        plan.orphans.append((frameworks[parts[1].lower()], path))
        footer = footer_url(path) if os.path.exists(path) else None
        if footer is not None and footer.lower() in live_docs:
            plan.fail("files no live entry records whose footer names a live page", f"{path}: {footer}")

    for page in plan.pages:
        manager = plan.managers[page.framework]
        for key in page.keys:
            if stale_path(manager, key, page.new):
                plan.keys_to_rewrite += 1
                plan.hash_files_to_save.add(page.framework)
    renamed = renamed_paths(plan)
    for name, manager in plan.managers.items():
        if renamed_pending(manager, renamed) is not None:
            plan.hash_files_to_save.add(name)


def stale_path(manager: HashManager, key: str, new: str) -> bool:
    """Whether the key records a file, at another path than new."""
    recorded = manager.hashes[key].get('file_path')
    return recorded is not None and recorded != new


def renamed_paths(plan: Plan) -> Dict[str, str]:
    """The renames, lowercased old path -> new path."""
    return {page.old.lower(): new for page, new in plan.renames}


def renamed_pending(manager: HashManager, renamed: Dict[str, str]) -> Optional[List[str]]:
    """metadata.pending_orphans with the renamed paths' new paths (matched in any casing), if any changes."""
    pending = manager.get_metadata("pending_orphans")
    if not isinstance(pending, list):
        return None
    updated = [renamed.get(path.lower(), path) if isinstance(path, str) else path for path in pending]
    return sorted(updated) if updated != pending else None


def write_plan(plan: Plan, out: TextIO) -> None:
    """Every rename, non-owner, file-less page and pending removal, tab-separated."""
    for page, new in plan.renames:
        out.write(f"rename\t{page.framework}\t{page.json_url}\t{page.on_disk}\t{new}\n")
    for page in plan.non_owners:
        out.write(f"non-owner\t{page.framework}\t{page.json_url}\t{page.old}\t{page.new}\n")
    for page in plan.file_less:
        out.write(f"file-less\t{page.framework}\t{page.json_url}\t{page.old}\t{page.new}\n")
    for framework, path in plan.orphans:
        out.write(f"orphan\t{framework}\t\t{path}\t\n")


def rename(plan: Plan) -> int:
    """Step 4: move the files, then remove the dirs they leave empty (never a docs dir).

    Returns:
        How many dirs were removed
    """
    left: Set[str] = set()
    for page, new in plan.renames:
        assert page.on_disk is not None
        if os.path.exists(new) and new.lower() != page.on_disk.lower():
            # Checked before: os.rename would replace that file
            raise FileExistsError(f"{new} exists (renaming {page.on_disk})")
        os.makedirs(os.path.dirname(new), exist_ok=True)
        os.rename(page.on_disk, new)
        left.add(os.path.dirname(page.on_disk))
    removed = 0
    for directory in sorted(left, key=lambda d: -d.count(os.sep)):
        while len(Path(directory).parts) > 2:  # documentation/<Dir>/…
            try:
                os.rmdir(directory)
            except OSError:  # not empty (or already removed)
                break
            removed += 1
            directory = os.path.dirname(directory)
    return removed


def rewrite(plan: Plan) -> Tuple[int, int, List[str]]:
    """Step 5: record every live page's new path, follow the renames in pending_orphans, save.

    Returns:
        (keys rewritten, hash files saved, failed saves)
    """
    rewritten = 0
    for page in plan.pages:
        manager = plan.managers[page.framework]
        for key in page.keys:
            if stale_path(manager, key, page.new):
                manager.set_file_path(key, page.new)
                rewritten += 1
    renamed = renamed_paths(plan)
    saved = 0
    failed: List[str] = []
    for name in sorted(plan.hash_files_to_save):
        manager = plan.managers[name]
        pending = renamed_pending(manager, renamed)
        if pending is not None:
            manager.set_metadata("pending_orphans", pending)
        if manager.save():
            saved += 1
        else:
            failed.append(str(manager.cache_file))
    return rewritten, saved, failed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="Check and report; change nothing")
    parser.add_argument("--plan", type=Path, help="Write the plan (tab-separated) to this file")
    args = parser.parse_args()
    setup_logging(log_level="WARNING")

    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if top.returncode != 0 or Path(top.stdout.strip()).resolve() != Path.cwd().resolve():
        print("❌ Run it from the repo root; nothing changed")
        return 1
    if Config.OUTPUT_DIR != DOCS_ROOT or Config.CACHE_DIR != HASH_DIR:
        print(f"❌ OUTPUT_DIR/CACHE_DIR must be the repo's {DOCS_ROOT}/ and {HASH_DIR}/; nothing changed")
        return 1

    started = time.time()
    plan = Plan()
    disk = load(plan)
    check(plan, disk)
    planned = time.time()

    within = sum(1 for page, new in plan.renames if os.path.dirname(new) == os.path.dirname(page.on_disk or ""))
    mode = "Would migrate" if args.dry_run else "Migrating"
    print(f"{mode}: {len(plan.managers)} Apple hash files, {len(plan.pages):,} live pages "
          f"(planned in {planned - started:.1f}s)")
    print(f"  files: {len(plan.pages) - len(plan.file_less) - len(plan.non_owners):,} "
          f"({plan.shared_files:,} shared by {plan.shared_files + len(plan.non_owners):,} pages)")
    print(f"  renames: {len(plan.renames):,} ({within:,} within their dir); staying: {plan.staying:,}")
    collisions = len(plan.failures.get(COLLISIONS, []))
    print(f"  new paths shared by several pages (case-insensitive): {collisions}")
    print(f"  non-owners (no file; the next scrape writes it): {len(plan.non_owners):,} "
          f"({plan.vacated_targets} take over a path their file's owner leaves)")
    print(f"  file-less live pages (only the recorded path changes): {len(plan.file_less):,}")
    for page in plan.file_less[:EXAMPLES]:
        print(f"    - {page.old} -> {page.new}")
    print(f"  tracked .md no live entry records (the next scrape's cleanup removes them): {len(plan.orphans):,}")
    for _framework, path in plan.orphans[:EXAMPLES]:
        print(f"    - {path}")
    print(f"  hash keys to rewrite: {plan.keys_to_rewrite:,} in {len(plan.hash_files_to_save)} hash files")
    if args.plan:
        with open(args.plan, 'w', encoding='utf-8') as out:
            write_plan(plan, out)
        print(f"  plan written to {args.plan}")
    if plan.failures:
        for check_name, details in plan.failures.items():
            print(f"❌ {check_name}: {len(details)}")
            for detail in details[:EXAMPLES]:
                print(f"    - {detail}")
        print("❌ Nothing changed")
        return 1
    if args.dry_run:
        print("✓ All checks passed; nothing changed (dry run)")
        return 0

    try:
        removed = rename(plan)
    except OSError as e:
        print(f"❌ Rename failed: {e}. Hash files unchanged; discard the renames (git checkout/clean) and fix")
        return 1
    renamed = time.time()
    print(f"  renamed {len(plan.renames):,} files in {renamed - planned:.1f}s; removed {removed:,} empty dirs")
    rewritten, saved, failed = rewrite(plan)
    print(f"  rewrote {rewritten:,} hash keys; saved {saved} hash files in {time.time() - renamed:.1f}s")
    for path in failed:
        print(f"❌ Failed to save {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
