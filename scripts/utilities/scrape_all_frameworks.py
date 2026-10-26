#!/usr/bin/env python3
"""
PRODUCTION: Scrape ALL Apple Frameworks
Comprehensive scraper for all 342+ Apple frameworks using JSON API
"""

import ast
import asyncio
import sys
import os
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Final, List, Optional, Sequence, Set, Tuple

# Add parent directories to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper, FrameworkOutcome, RunSinks, finish_run
from scraper.sink import CHILD_MODULES_KEY, HANDOFF_KEY, MODULE_KEY, SinkRegistry, metadata_ids, module_parents
from scraper import site as site_config
from scraper.site import APPLE, DocCSite
from scraper.utils.hash_manager import read_hash_file
from scraper.utils.logger import get_logger
from scraper.utils.naming import dirmap
from scraper.utils.rate_limiter import AdaptiveRateLimiter
from framework_list_scraper import AppleFrameworkListScraper
from cleanup_removed_frameworks import framework_hash_files
import docc_sites

logger = get_logger(__name__)

# The list guard: technologies.json must list at least this share of our Apple
# framework hash files (those not already counted as unlisted), or the run aborts
MIN_LISTED_SHARE: Final = 0.9

# The other scrapers, whose top-level docs dirs no Apple sink may have
# (namespace_collision): their configs are read from their source
OTHER_SCRAPERS: Final = ("scrape_mlx_docs.py", "scrape_swift_docs.py", "scrape_hig_docs.py")
SCRIPTS_DIR: Final = Path(__file__).resolve().parent.parent


def _path_strings(node: ast.AST) -> List[str]:
    """The string literals of a path expression joined with "/" (Path(…) / "a" / "b" -> ["a", "b"])."""
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        return _path_strings(node.left) + _path_strings(node.right)
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return [node.value]
    return []


def _configured_mlx_dirs(scripts_dir: Path) -> Optional[List[str]]:
    """The MLX scraper's configured output dirs (configured_sources()), if it can be imported.

    It needs wafer-py, which the scheduled scrape installs (requirements-scrape.txt)
    but a test environment may lack: None then.
    """
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    try:
        import scrape_mlx_docs
    except ImportError as e:
        logger.info("mlx_scraper_not_importable", error=str(e))
        return None
    return list(scrape_mlx_docs.configured_sources().values())


def _literal_output_dirs(path: Path) -> List[str]:
    """A scraper's docs dirs as its source states them (ast; it isn't imported).

    Each literal output_dir="<dir>[/…]" of a source's config, and each
    OUTPUT_DIR = … / "documentation" / "<dir>" assignment.
    """
    found: List[str] = []
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"), filename=path.name)):
        if (isinstance(node, ast.keyword) and node.arg == "output_dir"
                and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)):
            found.append(node.value.value)
        elif isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == "OUTPUT_DIR" for target in node.targets):
            parts = _path_strings(node.value)
            if "documentation" in parts[:-1]:
                found.append(parts[parts.index("documentation") + 1])
    return found


def other_scraper_dirs(scripts_dir: Path = SCRIPTS_DIR, import_mlx: bool = True) -> Dict[str, str]:
    """The top-level docs dirs the MLX, Swift and HIG scrapers write, {name.lower(): name}.

    From their configs: the MLX scraper's configured sources
    (scrape_mlx_docs.configured_sources(), every source list, so a new source
    is covered by itself), and the Swift and HIG scrapers' OUTPUT_DIR. Where
    the MLX scraper can't be imported (no wafer-py), its source's literal
    output_dirs stand in for configured_sources() (_literal_output_dirs);
    the Swift and HIG scrapers are always read that way.

    Raises:
        OSError: A scraper's source can't be read
        ValueError: A scraper's config names no docs dir (or doesn't parse,
            or configured_sources() rejects it)
    """
    dirs: Dict[str, str] = {}
    for name in OTHER_SCRAPERS:
        found: Optional[List[str]] = None
        if name == "scrape_mlx_docs.py" and import_mlx:
            found = _configured_mlx_dirs(scripts_dir)
        if found is None:
            found = _literal_output_dirs(scripts_dir / name)
        top = {path.strip("/").split("/")[0] for path in found if path.strip("/")}
        if not top:
            raise ValueError(f"{name} names no docs dir (no output_dir or OUTPUT_DIR)")
        for dir_name in sorted(top):
            dirs[dir_name.lower()] = dir_name
    return dirs


@dataclass
class HashDirScan:
    """What the run needs from the hash files at its start, read once.

    Attributes:
        page_counts: id (lowercased) -> its hash file's entries, plus its
            modules' (rule 5: a parent crawls its modules)
        module_files: The D6 module hash files (metadata.module)
        handoff_files: The hash files with metadata.handoff_from
        child_modules: Module id (lowercased) -> the hash files whose
            metadata.child_modules lists it
        top_level: The ids (lowercased) of the Apple hash files that aren't
            D6 modules', and of those that can't be read (never taken for a
            module): sink.apple_top_level's, for the scope rule
    """

    page_counts: Dict[str, int] = field(default_factory=dict)
    module_files: List[Path] = field(default_factory=list)
    handoff_files: List[Path] = field(default_factory=list)
    child_modules: Dict[str, List[Path]] = field(default_factory=dict)
    top_level: Set[str] = field(default_factory=set)


def scan_hash_dir(hash_dir: Path, site: DocCSite = APPLE) -> HashDirScan:
    """Read every hash file of the dir once: sizes for the sort, and the D6 metadata.

    A file that can't be read counts as a top-level technology's and is
    otherwise left out (its framework's scrape reports it). hash_dir is the
    site's (.hashes/<namespace>/ for a DocC site's).
    """
    scan = HashDirScan()
    module_sizes: List[Tuple[Dict[str, int], int]] = []
    for path in sorted(hash_dir.glob("*_hashes.json")):
        stem = path.name[:-len("_hashes.json")].lower()
        try:
            hashes, metadata = read_hash_file(path)
        except (OSError, ValueError):
            scan.top_level.add(stem)
            continue
        scan.page_counts[stem] = len(hashes)
        module = metadata.get(MODULE_KEY)
        if module:
            scan.module_files.append(path)
            module_sizes.append((module_parents(module), len(hashes)))
        elif any(url.startswith(site.json_prefix) for url in hashes):
            scan.top_level.add(stem)
        if metadata_ids(metadata.get(HANDOFF_KEY)):
            scan.handoff_files.append(path)
        for child in metadata_ids(metadata.get(CHILD_MODULES_KEY)):
            scan.child_modules.setdefault(str(child).lower(), []).append(path)
    for parents, size in module_sizes:
        for parent in parents:
            scan.page_counts[parent] = scan.page_counts.get(parent, 0) + size
    return scan


class ScrapeAborted(Exception):
    """The run stopped before scraping anything (exit code 2)."""


def check_framework_list(frameworks: Sequence[Dict[str, str]]) -> None:
    """The list guard: abort on a failed or short technologies.json fetch.

    The list must not be empty, and must hold at least MIN_LISTED_SHARE of
    the Apple framework hash files we have (cleanup_removed_frameworks'
    framework_hash_files: not the other scrapers' files or D6 modules), not
    counting those whose unlisted_runs is 1 or more: the pre-scrape, which
    runs first, is already removing those, so a real removal of many
    frameworks never stops the scrape.

    Raises:
        ScrapeAborted: The list is empty or short; nothing is scraped or cleaned
    """
    expected = sum(1 for hash_file in framework_hash_files(Config.CACHE_DIR).frameworks
                   if hash_file.unlisted_runs < 1)
    if not frameworks or len(frameworks) < MIN_LISTED_SHARE * expected:
        raise ScrapeAborted(
            f"technologies.json listed {len(frameworks)} frameworks, below {MIN_LISTED_SHARE:.0%} of the "
            f"{expected} Apple framework hash files here (not counting those already unlisted): "
            "a failed or short fetch"
        )


async def fetch_framework_list() -> List[Dict[str, str]]:
    """Every framework technologies.json lists, through the list guard (check_framework_list)."""
    async with AppleFrameworkListScraper() as framework_scraper:
        frameworks: List[Dict[str, str]] = await framework_scraper.fetch_all_frameworks()
    check_framework_list(frameworks)
    return frameworks


def names_framework(framework: Dict[str, str], name: str) -> bool:
    """Whether a name given on the command line is the framework's id or title, in any casing.

    Framework identity is case-insensitive: Apple flips a framework's URL casing.
    """
    return name.lower() in (framework['id'].lower(), framework['title'].lower())


def select_frameworks(frameworks: Sequence[Dict[str, str]], names: Sequence[str]) -> Tuple[List[Dict[str, str]], List[str]]:
    """The frameworks the --frameworks names pick (names_framework), and the names that pick none."""
    selected = [fw for fw in frameworks if any(names_framework(fw, name) for name in names)]
    unknown = [name for name in names if not any(names_framework(fw, name) for fw in selected)]
    return selected, unknown


def framework_errors(outcomes: Sequence[FrameworkOutcome]) -> List[str]:
    """The frameworks whose run hit an error of ours, each with why: the run exits 1.

    That is a framework that raised, one whose cleanup was blocked (a failed
    request or local error, its root, a hash file that couldn't be loaded,
    zero entries touched), one with a page whose fetch failure or local
    error reached PERSISTENT_FAILURE_RUNS (it no longer blocks, but still
    flags the run), and one with a filename clash (two pages named alike:
    the newcomer was written under a hashed stem; it never blocks). A root
    that returned 404/410 and a mass removal the valve holds for
    confirmation aren't errors.
    """
    errors = []
    for outcome in outcomes:
        reasons = [f"raised: {outcome.raised}"] if outcome.raised is not None else []
        reasons += [f"{reason} x{len(details)}" for reason, details in outcome.blocks.items()]
        if outcome.persistent_fetch_failures:
            reasons.append(f"persistent_fetch_failure x{len(outcome.persistent_fetch_failures)}")
        if outcome.persistent_local_errors:
            reasons.append(f"persistent_local_error x{len(outcome.persistent_local_errors)}")
        if outcome.filename_clashes:
            reasons.append(f"filename_clash x{len(outcome.filename_clashes)}")
        if reasons:
            errors.append(f"{outcome.name}: {', '.join(reasons)}")
    return errors


def known_dirs(frameworks: Sequence[Dict[str, str]]) -> Dict[str, str]:
    """The docs dirs whose pages this run links locally, {name.lower(): name}.

    Every Apple framework dir with a hash file (naming.dirmap) and every
    framework this run scrapes, by its id after _canonical_framework_id (its
    dir name): a framework scraped for the first time links to itself, and
    is linked to, locally in its first run.
    """
    dirs = dirmap(Config.CACHE_DIR)
    for fw in frameworks:
        dir_name = AppleJSONDocumentationScraper._canonical_framework_id(fw['id'])
        dirs[dir_name.lower()] = dir_name
    return dirs


def site_job_outcome(fw: Dict[str, str], site: DocCSite, **fields: Any) -> FrameworkOutcome:
    """The outcome of a job that didn't run its scraper: an Apple framework's, or a DocC site root's."""
    return FrameworkOutcome(framework_id=fw['id'], site=site.name, namespace=site.namespace, **fields)


async def load_sites(sites: Sequence[DocCSite]) -> Tuple[List["docc_sites.SiteRun"], Dict[str, AdaptiveRateLimiter]]:
    """Each DocC site's share of the run (docc_sites.load_site), and the rate limiter its jobs share.

    A site whose index root fails (7(f)), or whose load raises, runs no job
    this run; its error is the run's.
    """
    runs = []
    limiters: Dict[str, AdaptiveRateLimiter] = {}
    for site in sites:
        limiter = limiters[site.name] = AdaptiveRateLimiter(initial_delay=Config.RATE_LIMIT_DELAY)
        try:
            site_run = await docc_sites.load_site(site, limiter)
        except Exception as e:
            logger.error("site_load_failed", site=site.name, error=str(e))
            site_run = docc_sites.SiteRun(site=site, error=f"{site.name}: load failed: {e}")
        runs.append(site_run)
    return runs, limiters


async def scrape_frameworks(
    framework_list: Optional[List[Dict[str, str]]] = None,
    resume_from: Optional[str] = None,
    max_concurrent: int = 20,
    cleanup_orphans: bool = False,
    all_frameworks: Optional[Sequence[Dict[str, str]]] = None,
    sites: Sequence[DocCSite] = (),
) -> Dict[str, Any]:
    """Scrape specified frameworks or all frameworks with proper rolling concurrency

    Args:
        all_frameworks: technologies.json's full list, when framework_list is
            a selection of it (--frameworks): the scope rule's top-level set
            is the full list's, so a selected framework never crawls a
            bundle sibling's pages as its modules
        sites: The DocC sites to scrape too (site.DOCC_SITES): each root of
            a site's allow-list is a job of this run, with the Apple ones
            (docc_sites). With cleanup_orphans, their roots and sites that
            left the config are removed (rule 7(a)); a site whose index
            root fails runs no job (7(f))

    After every job: the multi-writer sinks' failure policy, render versions
    and save (finish_run), with or without cleanup_orphans.

    Raises:
        ScrapeAborted: The fetched list failed the list guard, the
            --resume framework isn't in the list, or a DocC namespace
            collides with another top-level dir
    """

    # Get list of frameworks to scrape
    if framework_list is not None:
        # Use provided list (an empty one scrapes nothing, never everything)
        frameworks = framework_list
    else:
        # Fetch all frameworks
        print("📋 Fetching complete framework list from Apple...")
        frameworks = await fetch_framework_list()
    listed = list(all_frameworks) if all_frameworks is not None else list(frameworks)

    # Filter if resuming
    if resume_from:
        found = False
        filtered = []
        for fw in frameworks:
            if names_framework(fw, resume_from):
                found = True
            if found:
                filtered.append(fw)
        frameworks = filtered
        if not frameworks:
            raise ScrapeAborted(f"Could not find framework '{resume_from}' to resume from")

    hash_scan = scan_hash_dir(Config.CACHE_DIR) if Config.CACHE_DIR.exists() else HashDirScan()
    page_counts: Dict[Tuple[str, str], int] = {(APPLE.name, fw): count for fw, count in hash_scan.page_counts.items()}

    # The other scrapers' top-level docs dirs, which no Apple sink may have.
    # Without them the run stops: an Apple page written into one of those
    # dirs would be deleted by that scraper's own orphan scan
    run_errors: List[str] = []
    try:
        reserved = other_scraper_dirs()
    except (OSError, ValueError, SyntaxError) as e:
        logger.error("other_scraper_dirs_unreadable", error=str(e))
        raise ScrapeAborted(f"namespace check: the other scrapers' docs dirs can't be read: {e}") from e
    # The DocC namespaces: none may be another scraper's dir or an Apple
    # framework's (checked from the config, before anything is scraped),
    # and no Apple sink may have one
    try:
        docc_sites.check_namespaces(
            site_config.DOCC_SITES, reserved, set(hash_scan.page_counts) | hash_scan.top_level)
    except ValueError as e:
        logger.error("namespace_collision", error=str(e))
        raise ScrapeAborted(f"namespace check: {e}") from e
    apple_reserved = {
        **reserved, **{site.namespace_top.lower(): site.namespace_top for site in site_config.DOCC_SITES}}

    # The run's sinks. Local links reach every framework dir we have and
    # every one this run scrapes. The scope rule's top-level technologies
    # are technologies.json's full list and our Apple hash files that
    # aren't D6 modules'
    sinks = SinkRegistry(
        known_dirs(frameworks),
        top_level={APPLE.name: {fw['id'] for fw in listed} | hash_scan.top_level},
        titles={fw['id']: fw['title'] for fw in listed},
        reserved=apple_reserved,
    )

    # The DocC sites: each site's index root (7(f)), its share of the
    # sinks, and its roots as jobs
    run_sinks = RunSinks(
        listed={(APPLE.name, fw['id'].lower()) for fw in listed},
        module_files=list(hash_scan.module_files),
        handoff_files=list(hash_scan.handoff_files),
        child_modules={(APPLE.name, module): files for module, files in hash_scan.child_modules.items()},
    )
    site_runs, limiters = await load_sites(sites)
    jobs: List[Dict[str, str]] = list(frameworks)
    for site_run in site_runs:
        site = site_run.site
        hash_dir = Config.get_hash_dir(site.namespace)
        run_sinks.hash_dirs[str(hash_dir).lower()] = (site.name, site.namespace)
        run_sinks.listed |= {(site.name, root) for root in site.roots}
        if cleanup_orphans:
            run_sinks.removals += docc_sites.config_removals(site)
        if hash_dir.exists():
            site_scan = scan_hash_dir(hash_dir, site)
            page_counts.update({(site.name, dir_id): count for dir_id, count in site_scan.page_counts.items()})
            run_sinks.module_files += site_scan.module_files
            run_sinks.handoff_files += site_scan.handoff_files
            run_sinks.child_modules.update(
                {(site.name, module): files for module, files in site_scan.child_modules.items()})
        if site_run.error is not None:
            run_errors.append(site_run.error)
            print(f"❌ {site.name}: its jobs are skipped this run ({site_run.error})")
            continue
        sinks.add_site(site, site_run.known_dirs, site_run.top_level, site.roots)
        jobs += [{'id': dir_name, 'title': site.framework_label(dir_name), 'site': site.name, 'root': root}
                 for root, dir_name in site_run.jobs]
    if cleanup_orphans and {site.name for site in sites} == {site.name for site in site_config.DOCC_SITES}:
        # A site that left the config goes whole (only a run that covers every site knows)
        run_sinks.removals += docc_sites.gone_sites(site_config.DOCC_SITES)

    # Sort the jobs by page count (largest first) for optimal scheduling.
    # Longest jobs start first so they don't become the tail when running
    # concurrently. A parent's count includes its D6 modules' (rule 5)
    def count(fw: Dict[str, str]) -> int:
        return page_counts.get((fw.get('site', APPLE.name), fw['id'].lower()), 0)

    if page_counts:
        jobs.sort(key=count, reverse=True)
        top3 = [(fw['title'], count(fw)) for fw in jobs[:3]]
        print(f"📐 Sorted by page count (largest first): {', '.join(f'{n} ({c:,})' for n, c in top3)}, ...")

    print(f"\n📊 Will scrape {len(jobs)} frameworks"
          + (f" ({len(jobs) - len(frameworks)} of them DocC site roots)" if len(jobs) > len(frameworks) else ""))

    # Track progress
    site_of_job = {site.name: site for site in (APPLE, *sites)}
    total = len(jobs)
    completed = 0
    failed = []
    outcomes = []
    
    # Use semaphore for proper rolling concurrency
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def scrape_with_semaphore(fw, index):
        async with semaphore:
            site = site_of_job[fw.get('site', APPLE.name)]
            print(f"\n[{index}/{total}] 🚀 Starting: {fw['title']} ({fw['id']})")
            if sinks.refuses(fw['id'], site):
                # Another scraper's top-level dir, or a DocC namespace: never scraped into
                logger.error("namespace_collision", framework=fw['title'], dir=fw['id'])
                print(f"❌ {fw['title']} ({fw['id']}): its dir is another scraper's (namespace_collision); not scraped")
                return fw, site_job_outcome(fw, site, blocks={"namespace_collision": [fw['id']]})
            try:
                scraper = AppleJSONDocumentationScraper(
                    framework_id=fw['id'],
                    framework_name=fw['title'],
                    sinks=sinks,
                    site=site,
                    root_id=fw.get('root'),
                    rate_limiter=limiters.get(site.name),
                )
                outcome = await scrape_single_framework(scraper, fw, index, total, cleanup_orphans)
                return fw, outcome
            except Exception as e:
                # A framework-level exception: its cleanup is blocked this run
                return fw, site_job_outcome(fw, site, raised=str(e) or type(e).__name__)
    
    # Create all tasks at once
    tasks = []
    for i, fw in enumerate(jobs, 1):
        task = scrape_with_semaphore(fw, i)
        tasks.append(task)
    
    # Run all tasks with rolling concurrency
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Process results
    for result in results:
        if isinstance(result, tuple):
            outcomes.append(result[1])
        elif isinstance(result, Exception):
            print(f"❌ Unexpected error: {result}")

    # D6: the multi-writer sinks' failure policy (its blocks go to the jobs'
    # outcomes), their render versions, then every sink saved
    run_sinks.modules = finish_run(sinks, outcomes, cleanup_orphans)
    for result in results:
        if isinstance(result, tuple):
            fw, outcome = result
            if outcome.raised is not None:
                failed.append((fw, outcome.raised))
                print(f"❌ Failed: {fw['title']} - {outcome.raised}")
    
    # Collect comprehensive stats
    total_pages_scraped = 0
    total_pages_skipped = 0
    total_pages_added = 0
    total_pages_updated = 0
    
    # Summary
    print("\n" + "="*70)
    print("📊 SCRAPING COMPLETE")
    print(f"✅ Successful: {total - len(failed)}")
    print(f"❌ Failed: {len(failed)}")
    
    if failed:
        print("\nFailed frameworks:")
        for fw, error in failed:
            print(f"  - {fw['title']} ({fw['id']}): {error}")
    
    # Return stats for final summary, with each framework's outcome (cleanup
    # skips, persistent failures) for the orphan cleanup and the exit code
    return {
        'total_frameworks': total,
        'successful_frameworks': total - len(failed),
        'failed_frameworks': len(failed),
        'total_pages_scraped': total_pages_scraped,
        'total_pages_skipped': total_pages_skipped,
        'framework_outcomes': outcomes,
        'run_sinks': run_sinks,
        'errors': run_errors,
    }

async def scrape_single_framework(scraper, framework, current, total, cleanup_orphans=False):
    """Scrape a single framework and return its FrameworkOutcome

    With cleanup_orphans, the outcome also carries the framework's orphan
    candidates, found right after its hash file was saved, so the end-of-run
    cleanup keeps neither the scraper nor its hash manager (every entry of
    the framework) in memory (a multi-writer sink's are found at the end of
    the run instead, finish_run). Either way, the job then leaves the sinks
    it used, which release their hash managers once nothing in flight uses
    them (SinkRegistry.job_done).
    """
    try:
        async with scraper:
            print(f"[{current}/{total}] 📝 Starting scrape for {framework['title']}...")
            
            # Use the streaming scrape_framework method
            stats = await scraper.scrape_framework()
            print(f"[{current}/{total}] ✅ Completed: {framework['title']} - {stats['pages_scraped']} scraped, {stats['pages_skipped']} skipped")
                
    except Exception as e:
        print(f"[{current}/{total}] ❌ Error scraping {framework['title']}: {e}")
        # A framework-level exception (or a failed hash save): its cleanup is blocked this run
        scraper.outcome.raised = str(e) or type(e).__name__

    try:
        if cleanup_orphans:
            scraper.scan_orphans(scraper.sink)
    finally:
        scraper.sinks.job_done(scraper.job_id)

    # Return the outcome (with its stats) for aggregation
    return scraper.outcome

async def scrape_everything() -> int:
    """Production script to scrape all Apple frameworks

    Returns the process exit code:
    - 0: a clean run. A framework whose root returned 404/410 (removed on
      the second such run) and a mass removal the valve holds for
      confirmation aren't errors.
    - 1: an error of ours (framework_errors: a framework raised, its cleanup
      was blocked, a page failed on PERSISTENT_FAILURE_RUNS runs, or two
      pages' file names clashed), the orphan cleanup failed to delete a file
      or write a hash file, or the re-indexing failed.
    - 2: aborted before scraping: the list guard (check_framework_list), a
      --frameworks name that is no framework's id or title, a --sites name
      that is no DocC site's, a --resume framework that isn't in the list,
      or a DocC namespace that collides with another top-level dir.

    The DocC sites (site.DOCC_SITES, e.g. docs.swift.org) are scraped with
    --all, or with no --frameworks; --sites picks some (alone, it scrapes
    no Apple framework). A --frameworks run scrapes none of them.
    - 130: interrupted.
    """
    
    print("🍎 APPLE DOCUMENTATION COMPREHENSIVE SCRAPER - PRODUCTION")
    print("=" * 70)
    print("This will scrape ALL 342+ Apple frameworks from technologies.json")
    print("Estimated time: 3-6 hours (using JSON API)")
    print("Uses incremental scraping - won't re-scrape unchanged content")
    print()
    
    # Parse command line arguments
    resume_from = None
    max_concurrent = 20
    specific_frameworks = []
    site_names: List[str] = []
    
    if '--resume' in sys.argv:
        idx = sys.argv.index('--resume')
        if idx + 1 < len(sys.argv) and not sys.argv[idx + 1].startswith('--'):
            resume_from = sys.argv[idx + 1]
            print(f"📍 Resuming from framework: {resume_from}")
        else:
            print("❌ --resume needs the framework to resume from: --resume SwiftUI. Nothing scraped.")
            return 2
    
    if '--concurrent' in sys.argv:
        idx = sys.argv.index('--concurrent')
        if idx + 1 < len(sys.argv):
            max_concurrent = int(sys.argv[idx + 1])
            print(f"🔧 Using {max_concurrent} concurrent scrapers")
    
    if '--frameworks' in sys.argv:
        idx = sys.argv.index('--frameworks')
        # Collect all arguments until next flag or end
        idx += 1
        while idx < len(sys.argv) and not sys.argv[idx].startswith('--'):
            specific_frameworks.append(sys.argv[idx])
            idx += 1
        if not specific_frameworks and '--all' not in sys.argv:
            # No names must never mean every framework
            print("❌ --frameworks needs at least one framework name. Nothing scraped.")
            return 2
        print(f"📌 Scraping specific frameworks: {', '.join(specific_frameworks)}")

    if '--sites' in sys.argv:
        idx = sys.argv.index('--sites') + 1
        while idx < len(sys.argv) and not sys.argv[idx].startswith('--'):
            site_names.append(sys.argv[idx])
            idx += 1
        configured = {site.name: site for site in site_config.DOCC_SITES}
        unknown_sites = [name for name in site_names if name not in configured]
        if not site_names or unknown_sites:
            print(f"❌ --sites needs DocC site names ({', '.join(configured) or 'none configured'}): "
                  f"{', '.join(unknown_sites) or 'none given'}. Nothing scraped.")
            return 2
        print(f"📌 Scraping DocC sites: {', '.join(site_names)}")
    if site_names:
        sites = [site for site in site_config.DOCC_SITES if site.name in site_names]
    elif specific_frameworks:
        sites = []
    else:
        sites = list(site_config.DOCC_SITES)
    
    # Check for orphan cleanup flag
    cleanup_orphans = False
    if '--cleanup-orphans' in sys.argv:
        cleanup_orphans = True
        print("🧹 Orphan cleanup enabled - will check for orphaned pages after all scraping completes")
    
    if '--dry-run' in sys.argv:
        print("🧪 DRY RUN MODE - Will show what would be scraped")
        
        # Just show the framework list
        async with AppleFrameworkListScraper() as framework_scraper:
            frameworks = await framework_scraper.fetch_all_frameworks()
        
        if specific_frameworks:
            frameworks, unknown = select_frameworks(frameworks, specific_frameworks)
            if unknown:
                print(f"⚠️  Not a framework id or title in technologies.json: {', '.join(unknown)}")
        elif site_names and '--all' not in sys.argv:
            frameworks = []
        for site in sites:
            print(f"🌐 Would scrape {site.name} ({site.doc_base}): {len(site.roots)} roots under "
                  f"documentation/{site.namespace}/")
        
        print(f"\n📋 Would scrape {len(frameworks)} frameworks:")
        for i, fw in enumerate(frameworks[:20], 1):
            print(f"{i:3d}. {fw['title']} ({fw['id']})")
        
        if len(frameworks) > 20:
            print(f"    ... and {len(frameworks) - 20} more frameworks")
        
        return 0
    
    # Handle --all flag
    if '--all' in sys.argv:
        specific_frameworks = []  # Clear to scrape all
    
    # Confirm before starting
    if '--yes' not in sys.argv:
        if specific_frameworks:
            response = input(f"\n🚀 Ready to scrape {len(specific_frameworks)} frameworks? Continue? (y/N): ")
        else:
            response = input("\n🚀 Ready to scrape all Apple frameworks? This will take several hours. Continue? (y/N): ")
        
        if response.lower() not in ['y', 'yes']:
            print("❌ Aborted by user")
            return 0
    
    print("\n🚀 Starting Apple framework scraping...")
    
    try:
        # If specific frameworks requested, fetch their info
        framework_list: Optional[List[Dict[str, str]]] = None
        all_frameworks = None
        if site_names and not specific_frameworks and '--all' not in sys.argv:
            # Only the DocC sites
            framework_list = []
        if specific_frameworks:
            all_frameworks = await fetch_framework_list()
            framework_list, unknown = select_frameworks(all_frameworks, specific_frameworks)
            if unknown:
                # Every name must pick a framework (e.g. "SwiftUI UIKit"
                # passed as one argument picks none): never a partial run
                print(f"❌ Not a framework id or title in technologies.json: {', '.join(unknown)}. Nothing scraped.")
                print("💡 Pass each name as its own argument: --frameworks SwiftUI UIKit")
                return 2
        
        scrape_stats = await scrape_frameworks(
            framework_list=framework_list,
            resume_from=resume_from,
            max_concurrent=max_concurrent,
            cleanup_orphans=cleanup_orphans,
            all_frameworks=all_frameworks,
            sites=sites,
        )
        outcomes = scrape_stats['framework_outcomes']
        errors = framework_errors(outcomes) + scrape_stats.get('errors', [])
        
        if errors:
            print("\n⚠️  SCRAPING COMPLETED, WITH ERRORS (listed at the end)")
        else:
            print("\n🎉 SCRAPING COMPLETED SUCCESSFULLY!")
        
        # Handle orphan cleanup at the end
        if cleanup_orphans:
            print("\n" + "="*70)
            print("🔍 Checking for orphaned files...")
            
            # Import and run the cleanup
            from cleanup_orphans_at_end import cleanup_after_scrape

            # From each framework's result: only the frameworks scraped this
            # run, never one whose run hit a failure of ours (it keeps every
            # file until a clean run); --auto-cleanup deletes without asking.
            # The report's failures are errors for the run.
            report = cleanup_after_scrape(
                outcomes,
                interactive='--auto-cleanup' not in sys.argv,
                run=scrape_stats.get('run_sinks'),
            )
            errors.extend(f"cleanup: {failure}" for failure in report.failures)
        
        # Trigger re-indexing if requested
        if '--trigger-reindex' in sys.argv:
            print("\n" + "="*70)
            print("🔍 Triggering Meilisearch re-indexing...")
            
            try:
                # Check if we're in Docker environment
                if os.path.exists("/data/documentation"):
                    docs_path = "/data/documentation"
                    index_script = "/app/scripts/index_to_meilisearch.py"
                else:
                    docs_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "documentation")
                    index_script = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "index_to_meilisearch.py")
                
                if os.path.exists(index_script):
                    import subprocess
                    # Force full rebuild after scraping to ensure orphans are removed
                    cmd = [sys.executable, index_script, "--docs-path", docs_path, "--force"]
                    print(f"Running: {' '.join(cmd)}")

                    # The indexer's output goes straight to this run's stdout and stderr, all
                    # of it as it happens: each file left out of the index and why, and the
                    # cause of a failed run (its last lines, on stdout)
                    sys.stdout.flush()
                    result = subprocess.run(cmd)

                    if result.returncode == 0:
                        print("✅ Re-indexing completed successfully!")
                    else:
                        print(f"❌ Re-indexing failed with return code {result.returncode}")
                        errors.append(f"re-indexing failed with return code {result.returncode}")
                else:
                    print(f"❌ Index script not found at {index_script}")
                    print("💡 Re-indexing skipped - run manually with: cd scripts && python3 index_to_meilisearch.py")
                    errors.append(f"re-indexing skipped: no index script at {index_script}")
            except Exception as e:
                print(f"❌ Failed to trigger re-indexing: {e}")
                print("💡 You can manually re-index with: cd scripts && python3 index_to_meilisearch.py")
                errors.append(f"re-indexing failed: {e}")
        
        if errors:
            print(f"\n❌ Errors of ours this run ({len(errors)}), exit code 1:")
            for error in errors:
                print(f"   - {error}")
            return 1
        return 0
        
    except ScrapeAborted as e:
        print(f"\n❌ {e}. Nothing scraped.")
        return 2
    
    except (KeyboardInterrupt, asyncio.CancelledError):
        # Under asyncio.run, Ctrl-C arrives as a cancellation of this task
        print("\n⏹️  Scraping interrupted by user")
        print(f"💡 To resume, run: python3 {sys.argv[0]} --resume [last_framework]")
        return 130
        
    except Exception as e:
        print(f"\n❌ Scraping failed: {e}")
        print(f"💡 To resume, run: python3 {sys.argv[0]} --resume [last_framework]")
        return 1

if __name__ == "__main__":
    # Usage examples:
    print("Usage examples:")
    print(f"  python3 {sys.argv[0]} --dry-run                    # Show what would be scraped")
    print(f"  python3 {sys.argv[0]} --all --yes                  # Scrape all frameworks")
    print(f"  python3 {sys.argv[0]} --frameworks SwiftUI UIKit   # Scrape specific frameworks")
    print(f"  python3 {sys.argv[0]} --resume SwiftUI             # Resume from SwiftUI")
    print(f"  python3 {sys.argv[0]} --all --yes --cleanup-orphans # Scrape and check for orphans at end")
    print(f"  python3 {sys.argv[0]} --all --yes --cleanup-orphans --auto-cleanup # Auto-delete orphans")
    print(f"  python3 {sys.argv[0]} --all --yes --trigger-reindex # Scrape and re-index Meilisearch")
    print(f"  python3 {sys.argv[0]} --concurrent 5               # Use 5 concurrent scrapers")
    print(f"  python3 {sys.argv[0]} --sites swift-org --yes      # Scrape only a DocC site (docs.swift.org)")
    print()
    
    try:
        sys.exit(asyncio.run(scrape_everything()))
    except KeyboardInterrupt:
        print("\n⏹️  Scraping interrupted by user")
        sys.exit(130)
