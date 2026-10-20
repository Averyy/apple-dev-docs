#!/usr/bin/env python3
"""
PRODUCTION: Scrape ALL Apple Frameworks
Comprehensive scraper for all 342+ Apple frameworks using JSON API
"""

import asyncio
import sys
import os
import json
from pathlib import Path
from typing import Dict, Final, List, Sequence, Tuple

# Add parent directories to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper, FrameworkOutcome
from scraper.utils.naming import dirmap
from framework_list_scraper import AppleFrameworkListScraper
from cleanup_removed_frameworks import framework_hash_files

# The list guard: technologies.json must list at least this share of our Apple
# framework hash files (those not already counted as unlisted), or the run aborts
MIN_LISTED_SHARE: Final = 0.9


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
            errors.append(f"{outcome.framework_id}: {', '.join(reasons)}")
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


async def scrape_frameworks(framework_list=None, resume_from=None, max_concurrent=20, cleanup_orphans=False):
    """Scrape specified frameworks or all frameworks with proper rolling concurrency

    Raises:
        ScrapeAborted: The fetched list failed the list guard, or the
            --resume framework isn't in the list
    """

    # Get list of frameworks to scrape
    if framework_list is not None:
        # Use provided list (an empty one scrapes nothing, never everything)
        frameworks = framework_list
    else:
        # Fetch all frameworks
        print("📋 Fetching complete framework list from Apple...")
        frameworks = await fetch_framework_list()

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

    # Sort frameworks by page count (largest first) for optimal scheduling.
    # Longest jobs start first so they don't become the tail when running concurrently.
    hashes_dir = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))).joinpath('.hashes')
    if hashes_dir.exists():
        page_counts = {}
        for hf in hashes_dir.glob('*_hashes.json'):
            try:
                data = json.loads(hf.read_text())
                fw_name = hf.stem.replace('_hashes', '')
                page_counts[fw_name.lower()] = len(data.get('hashes', {}))
            except Exception:
                pass
        if page_counts:
            frameworks.sort(key=lambda fw: page_counts.get(fw['id'].lower(), 0), reverse=True)
            top3 = [(fw['title'], page_counts.get(fw['id'].lower(), 0)) for fw in frameworks[:3]]
            print(f"📐 Sorted by page count (largest first): {', '.join(f'{n} ({c:,})' for n, c in top3)}, ...")

    print(f"\n📊 Will scrape {len(frameworks)} frameworks")

    # Local links reach every framework dir we have and every one this run scrapes
    link_dirs = known_dirs(frameworks)

    # Track progress
    total = len(frameworks)
    completed = 0
    failed = []
    outcomes = []
    
    # Use semaphore for proper rolling concurrency
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def scrape_with_semaphore(fw, index):
        async with semaphore:
            print(f"\n[{index}/{total}] 🚀 Starting: {fw['title']} ({fw['id']})")
            try:
                scraper = AppleJSONDocumentationScraper(
                    framework_id=fw['id'],
                    framework_name=fw['title'],
                    known_dirs=link_dirs,
                )
                outcome = await scrape_single_framework(scraper, fw, index, total, cleanup_orphans)
                return fw, outcome
            except Exception as e:
                # A framework-level exception: its cleanup is blocked this run
                return fw, FrameworkOutcome(framework_id=fw['id'], raised=str(e) or type(e).__name__)
    
    # Create all tasks at once
    tasks = []
    for i, fw in enumerate(frameworks, 1):
        task = scrape_with_semaphore(fw, i)
        tasks.append(task)
    
    # Run all tasks with rolling concurrency
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Process results
    for result in results:
        if isinstance(result, tuple):
            fw, outcome = result
            outcomes.append(outcome)
            if outcome.raised is not None:
                failed.append((fw, outcome.raised))
                print(f"❌ Failed: {fw['title']} - {outcome.raised}")
        elif isinstance(result, Exception):
            print(f"❌ Unexpected error: {result}")
    
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
        'framework_outcomes': outcomes
    }

async def scrape_single_framework(scraper, framework, current, total, cleanup_orphans=False):
    """Scrape a single framework and return its FrameworkOutcome

    With cleanup_orphans, the outcome also carries the framework's orphan
    candidates, found right after its hash file was saved, so the end-of-run
    cleanup keeps neither the scraper nor its hash manager (every entry of
    the framework) in memory.
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

    if cleanup_orphans:
        scraper.scan_orphans()

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
      --frameworks name that is no framework's id or title, or a --resume
      framework that isn't in the list.
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
        framework_list = None
        if specific_frameworks:
            framework_list, unknown = select_frameworks(await fetch_framework_list(), specific_frameworks)
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
            cleanup_orphans=cleanup_orphans
        )
        outcomes = scrape_stats['framework_outcomes']
        errors = framework_errors(outcomes)
        
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
    print()
    
    try:
        sys.exit(asyncio.run(scrape_everything()))
    except KeyboardInterrupt:
        print("\n⏹️  Scraping interrupted by user")
        sys.exit(130)
