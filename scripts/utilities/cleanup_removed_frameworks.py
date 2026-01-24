#!/usr/bin/env python3
"""
Clean up frameworks that Apple has removed from technologies.json.

This handles the case where an entire framework is removed (not just pages within it).
The existing orphan cleanup only handles pages within active frameworks.

Usage:
    python cleanup_removed_frameworks.py --dry-run  # Preview what would be deleted
    python cleanup_removed_frameworks.py            # Actually delete
"""

import functools
import shutil
import sys
from pathlib import Path

import httpx

TECHNOLOGIES_URL = "https://developer.apple.com/tutorials/data/documentation/technologies.json"
HASH_DIR = Path(__file__).parent.parent.parent / ".hashes"
DOC_DIR = Path(__file__).parent.parent.parent / "documentation"

# Frameworks to never delete (not from Apple's API)
# Static list for docs that don't have a scraper config to import
PROTECTED_FRAMEWORKS = {"Swift-Book", "HIG"}

# Hash files that are not framework hashes (different structure/purpose)
# These use different naming than their output folders
NON_FRAMEWORK_HASHES = {"meilisearch", "swift_docs", "mlx_docs", "hig_docs"}


@functools.lru_cache(maxsize=1)
def get_mlx_protected_frameworks() -> frozenset[str]:
    """Get protected frameworks from MLX scraper config dynamically."""
    try:
        # Import MLX scraper sources
        scripts_dir = Path(__file__).parent.parent
        if str(scripts_dir) not in sys.path:
            sys.path.insert(0, str(scripts_dir))

        from scrape_mlx_docs import SPHINX_SOURCES, GITHUB_SOURCES

        # Extract top-level output directories
        protected: set[str] = set()
        for source in SPHINX_SOURCES:
            top_dir = source.output_dir.split("/")[0]
            protected.add(top_dir.lower())
        for source in GITHUB_SOURCES:
            top_dir = source.output_dir.split("/")[0]
            protected.add(top_dir.lower())

        return frozenset(protected)
    except ImportError as e:
        print(f"Warning: Could not import MLX scraper config: {e}")
        # Fallback to known values if import fails
        return frozenset({"mlx", "mlx-swift", "coremltools", "ml-stable-diffusion"})


def check_apple_site_available() -> tuple[bool, str]:
    """Verify Apple's documentation site is responding before trusting 404s.

    Returns:
        Tuple of (is_available, message)
    """
    # Check a framework that should always exist
    test_urls = [
        "https://developer.apple.com/documentation/foundation",
        "https://developer.apple.com/documentation/swift",
    ]

    for url in test_urls:
        try:
            response = httpx.head(url, follow_redirects=True, timeout=10)
            if response.status_code == 200:
                return True, f"Apple site responding ({url})"
        except Exception:
            continue

    return False, "Apple documentation site not responding - aborting for safety"


def verify_framework_removed(framework: str) -> tuple[bool, str]:
    """Verify a framework is truly removed by checking Apple's website.

    Returns:
        Tuple of (is_removed, reason)
    """
    url = f"https://developer.apple.com/documentation/{framework}"
    try:
        # Don't follow redirects - we want to see the actual response
        response = httpx.head(url, follow_redirects=False, timeout=10)

        if response.status_code == 404:
            return True, "404"
        elif response.status_code == 301 or response.status_code == 302:
            location = response.headers.get("location", "")
            return True, f"redirects to {location}"
        elif response.status_code == 200:
            return False, "still exists (200)"
        else:
            return False, f"unknown status {response.status_code}"
    except Exception as e:
        return False, f"error: {e}"


def get_apple_frameworks() -> set:
    """Fetch current framework list from Apple's API."""
    response = httpx.get(TECHNOLOGIES_URL, follow_redirects=True, timeout=30)
    response.raise_for_status()
    data = response.json()

    frameworks = set()
    for section in data.get("sections", []):
        for group in section.get("groups", []):
            for tech in group.get("technologies", []):
                # Extract framework ID from destination identifier
                dest = tech.get("destination", {})
                identifier = dest.get("identifier", "")
                if identifier.startswith("doc://"):
                    # doc://com.apple.documentation/documentation/SwiftUI
                    parts = identifier.split("/documentation/")
                    if len(parts) > 1:
                        framework_id = parts[1].split("/")[0]
                        frameworks.add(framework_id.lower())

    return frameworks


def get_local_frameworks() -> dict:
    """Get frameworks we have locally (from hash files).

    Returns:
        Dict mapping lowercase framework name to actual hash file path
    """
    if not HASH_DIR.exists():
        return {}

    frameworks = {}
    for hash_file in HASH_DIR.glob("*_hashes.json"):
        framework = hash_file.stem.replace("_hashes", "")
        # Skip non-framework hash files
        if framework.lower() in NON_FRAMEWORK_HASHES:
            continue
        frameworks[framework.lower()] = hash_file

    return frameworks


def get_local_doc_folders() -> dict:
    """Get documentation folders we have locally.

    Returns:
        Dict mapping lowercase folder name to actual folder path
    """
    if not DOC_DIR.exists():
        return {}

    folders = {}
    for folder in DOC_DIR.iterdir():
        if folder.is_dir():
            folders[folder.name.lower()] = folder

    return folders


def cleanup_removed_frameworks(dry_run: bool = False) -> int:
    """Remove frameworks that Apple has removed.

    Returns:
        Number of frameworks removed
    """
    # Safety check - ensure Apple's site is responding before trusting 404s
    print("Checking Apple documentation site availability...")
    site_available, site_msg = check_apple_site_available()
    if not site_available:
        print(f"ABORT: {site_msg}")
        return 0
    print(f"   {site_msg}")

    print("Fetching current framework list from Apple...")
    try:
        apple_frameworks = get_apple_frameworks()
    except Exception as e:
        print(f"Error fetching Apple frameworks: {e}")
        return 0

    print(f"Apple lists {len(apple_frameworks)} frameworks")

    local_hash_frameworks = get_local_frameworks()
    local_doc_folders = get_local_doc_folders()

    print(f"Local hash files: {len(local_hash_frameworks)}")
    print(f"Local doc folders: {len(local_doc_folders)}")

    # Find frameworks we have locally but Apple doesn't list anymore
    protected_lower = {f.lower() for f in PROTECTED_FRAMEWORKS} | get_mlx_protected_frameworks()

    orphaned_hashes = set(local_hash_frameworks.keys()) - apple_frameworks - protected_lower
    orphaned_docs = set(local_doc_folders.keys()) - apple_frameworks - protected_lower

    all_orphans = orphaned_hashes | orphaned_docs

    if not all_orphans:
        print("No removed frameworks detected")
        return 0

    print(f"\nFound {len(all_orphans)} candidate(s) not in technologies.json")
    print("Verifying against Apple's website...")

    # Verify each orphan is truly removed (404 or redirect)
    verified_orphans = {}
    skipped_count = 0
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    for fw in sorted(all_orphans):
        is_removed, reason = verify_framework_removed(fw)
        has_hash = fw in orphaned_hashes
        has_docs = fw in orphaned_docs
        markers = []
        if has_hash:
            markers.append("hash")
        if has_docs:
            markers.append("docs")

        if is_removed:
            verified_orphans[fw] = (reason, markers)
        else:
            skipped_count += 1
            if verbose:
                print(f"   [SKIP] {fw} - {reason}")

    if skipped_count > 0 and not verbose:
        print(f"   Skipped {skipped_count} (still exist on Apple's site)")

    if not verified_orphans:
        print("\nNo removed frameworks found")
        return 0

    print(f"\nConfirmed {len(verified_orphans)} removed framework(s):")
    for fw, (reason, markers) in sorted(verified_orphans.items()):
        print(f"   - {fw} ({', '.join(markers)}) - {reason}")

    if dry_run:
        print("\n[DRY RUN] Would delete the above frameworks")
        return len(verified_orphans)

    # Confirm before deletion
    print(f"\nAbout to delete {len(verified_orphans)} framework(s). Continue? [y/N] ", end="")
    response = input().strip().lower()
    if response != 'y':
        print("Aborted.")
        return 0

    deleted = 0
    for fw in verified_orphans:
        # Delete hash file
        if fw in local_hash_frameworks:
            hash_file = local_hash_frameworks[fw]
            if hash_file.exists():
                hash_file.unlink()
                print(f"   Deleted: {hash_file}")

        # Delete documentation folder
        if fw in local_doc_folders:
            doc_folder = local_doc_folders[fw]
            if doc_folder.exists():
                shutil.rmtree(doc_folder)
                print(f"   Deleted: {doc_folder}")

        deleted += 1

    print(f"\nCleaned up {deleted} removed framework(s)")
    return deleted


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    auto_yes = "--yes" in sys.argv

    if auto_yes and not dry_run:
        # For automation: skip confirmation prompt but still verify
        # Safety check first
        print("Checking Apple documentation site availability...")
        site_available, site_msg = check_apple_site_available()
        if not site_available:
            print(f"ABORT: {site_msg}")
            sys.exit(1)
        print(f"   {site_msg}")

        print("Fetching current framework list from Apple...")
        try:
            apple_frameworks = get_apple_frameworks()
        except Exception as e:
            print(f"Error fetching Apple frameworks: {e}")
            sys.exit(1)

        print(f"Apple lists {len(apple_frameworks)} frameworks")

        local_hash_frameworks = get_local_frameworks()
        local_doc_folders = get_local_doc_folders()

        protected_lower = {f.lower() for f in PROTECTED_FRAMEWORKS} | get_mlx_protected_frameworks()
        orphaned_hashes = set(local_hash_frameworks.keys()) - apple_frameworks - protected_lower
        orphaned_docs = set(local_doc_folders.keys()) - apple_frameworks - protected_lower
        all_orphans = orphaned_hashes | orphaned_docs

        if not all_orphans:
            print("No removed frameworks detected")
            sys.exit(0)

        print(f"\nFound {len(all_orphans)} candidate(s), verifying...")

        # Verify each orphan before deletion
        deleted = 0
        skipped = 0
        for fw in sorted(all_orphans):
            is_removed, reason = verify_framework_removed(fw)

            if not is_removed:
                print(f"   [SKIP] {fw} - {reason}")
                skipped += 1
                continue

            print(f"   [DELETE] {fw} - {reason}")
            if fw in local_hash_frameworks:
                hash_file = local_hash_frameworks[fw]
                if hash_file.exists():
                    hash_file.unlink()
            if fw in local_doc_folders:
                doc_folder = local_doc_folders[fw]
                if doc_folder.exists():
                    shutil.rmtree(doc_folder)
            deleted += 1

        print(f"\nCleaned up {deleted} framework(s), skipped {skipped}")
    else:
        cleanup_removed_frameworks(dry_run=dry_run)
