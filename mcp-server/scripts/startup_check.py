#!/usr/bin/env python3
"""
Startup check script for Docker container.
Always runs the indexer on startup. The indexer updates the live index (new and changed
docs added, removed docs deleted), or rebuilds it beside the live index and swaps it in
when a rebuild is due (no index yet, a new processor version, a hash file that belongs to
another index, an older indexer has run on it (a rollback), a week since the last rebuild,
or more than 25% of the files changed). Either way the live index keeps serving; a due
rebuild that fails is followed by the update and retried on the next start.
"""

import os
import sys
import time
from pathlib import Path
import meilisearch
from rich.console import Console

console = Console()

# Written by older versions of this script for their weekly in-place rebuild. The live
# index's createdAt is the rebuild time now; an older image started on this volume (a
# rollback) treats a missing file as a rebuild just done instead of rebuilding in place.
RETIRED_FORCE_REBUILD_FILE = Path("/data/logs/last_force_rebuild.txt")


def wait_for_meilisearch(url: str, api_key: str, max_attempts: int = 30) -> bool:
    """Wait for Meilisearch to be ready."""
    console.print("Waiting for Meilisearch to start...", style="yellow")

    for attempt in range(max_attempts):
        try:
            client = meilisearch.Client(url, api_key)
            client.health()
            console.print("Meilisearch is ready!", style="green")
            return True
        except Exception:
            if attempt < max_attempts - 1:
                time.sleep(2)
            else:
                console.print(f"Meilisearch failed to start after {max_attempts} attempts", style="red")
                return False
    return False


def get_index_doc_count(client: meilisearch.Client, index_name: str = "apple-docs") -> int:
    """Get document count from index, or 0 if index doesn't exist."""
    try:
        index = client.index(index_name)
        stats = index.get_stats()
        return stats.number_of_documents
    except Exception:
        return 0


def run_indexing() -> bool:
    """Run the indexing script (it prints its mode: incremental update or rebuild by swap)."""
    import subprocess

    msg = "Starting indexing..."
    console.print(msg, style="blue")
    print(msg)

    # Build command
    cmd = [
        sys.executable,
        "/app/scripts/index_to_meilisearch.py",
        "--docs-path", "/data/documentation"
    ]

    # Run the indexing script. Its output goes straight to this script's stdout and stderr
    # (/data/logs/startup-check.log under supervisord), so the log keeps all of it as it
    # happens: each file left out of the index and why, and the cause of a failed run
    sys.stdout.flush()
    result = subprocess.run(cmd)

    if result.returncode == 0:
        console.print("Indexing completed successfully!", style="green")
        return True
    else:
        console.print(f"Indexing failed with return code {result.returncode}", style="red")
        return False


def main() -> None:
    """Main startup check - always run the indexer (it decides when to rebuild)."""
    print("\n" + "=" * 50)
    print("Apple Docs MCP Server - Startup Check")
    print("=" * 50)

    # Remove ready marker so MCP server waits for us
    ready_file = Path("/data/logs/startup_complete")
    if ready_file.exists():
        ready_file.unlink()

    # Get environment variables
    meilisearch_url = os.getenv("MEILI_HTTP_ADDR", "http://localhost:7700")
    meilisearch_key = os.getenv("MEILI_MASTER_KEY", "")

    # Wait for Meilisearch to be ready
    if not wait_for_meilisearch(meilisearch_url, meilisearch_key):
        sys.exit(1)

    # Check current index status
    client = meilisearch.Client(meilisearch_url, meilisearch_key)
    doc_count = get_index_doc_count(client)

    if doc_count > 0:
        msg = f"Current index: {doc_count:,} documents"
        console.print(msg, style="cyan")
        print(msg)
    else:
        console.print("No existing index found", style="yellow")

    # Check if documentation exists
    docs_path = Path("/data/documentation")
    if not docs_path.exists() or not any(docs_path.rglob("*.md")):
        console.print("No documentation found in /data/documentation!", style="red")
        sys.exit(1)

    doc_files = list(docs_path.rglob("*.md"))
    console.print(f"Documentation: {len(doc_files):,} markdown files", style="cyan")

    RETIRED_FORCE_REBUILD_FILE.unlink(missing_ok=True)

    # Always run the indexer - it updates the live index or rebuilds it by swap
    if run_indexing():
        # Verify final state
        time.sleep(2)
        new_count = get_index_doc_count(client)
        msg = f"Index ready with {new_count:,} documents"
        console.print(msg, style="green")
        print(msg)
    else:
        console.print("Failed to index documents!", style="red")
        sys.exit(1)

    # Note: startup_complete file is no longer used - MCP server now starts
    # when Meilisearch health check passes (see supervisord.conf)

    print("\nStartup check complete - services can start\n")


if __name__ == "__main__":
    main()
