#!/usr/bin/env python3
"""
Startup check script for Docker container.
Always runs the indexer on startup - the indexer handles incremental updates.
Monthly force rebuild to clean up deleted files.
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime
import meilisearch
from rich.console import Console

console = Console()

# How often to force a full rebuild (cleans up deleted files)
FORCE_REBUILD_DAYS = 30


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


def should_force_rebuild(current_doc_count: int, file_count: int) -> tuple[bool, str]:
    """Check if we should do a full rebuild (monthly cleanup of deleted files)."""
    force_file = Path("/data/logs/last_force_rebuild.txt")

    # Index is "healthy" if doc count is at least 90% of file count
    # (each file produces ~1 doc on average, some produce more for sections)
    min_expected = int(file_count * 0.9)
    index_is_healthy = current_doc_count >= min_expected

    if index_is_healthy:
        if not force_file.exists():
            # Create the file so future checks work, but don't force rebuild
            save_force_rebuild_time()
            return False, f"Index healthy ({current_doc_count:,} docs) - skipping rebuild"

        try:
            last_force = datetime.fromisoformat(force_file.read_text().strip())
            days_since = (datetime.now() - last_force).days

            if days_since >= FORCE_REBUILD_DAYS:
                return True, f"Monthly cleanup ({days_since} days since last rebuild)"
            else:
                return False, f"Incremental update ({days_since} days since last rebuild)"
        except Exception:
            return False, f"Index healthy ({current_doc_count:,} docs) - skipping rebuild"

    # Index is empty or incomplete - needs full build
    return True, f"Index incomplete ({current_doc_count:,} docs, expected {min_expected:,}+) - full build needed"


def save_force_rebuild_time():
    """Save the current time as the last force rebuild time."""
    force_file = Path("/data/logs/last_force_rebuild.txt")
    force_file.parent.mkdir(parents=True, exist_ok=True)
    force_file.write_text(datetime.now().isoformat())


def run_indexing(force_rebuild: bool = False) -> bool:
    """Run the indexing script."""
    import subprocess

    mode = "full rebuild" if force_rebuild else "incremental"
    msg = f"Starting indexing ({mode})..."
    console.print(msg, style="blue")
    print(msg)

    # Build command
    cmd = [
        sys.executable,
        "/app/scripts/index_to_meilisearch.py",
        "--docs-path", "/data/documentation"
    ]

    if force_rebuild:
        cmd.append("--force")

    # Run the indexing script
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        console.print("Indexing completed successfully!", style="green")
        # Log last few lines of output
        if result.stdout:
            for line in result.stdout.strip().split('\n')[-5:]:
                if line.strip():
                    console.print(f"   {line}", style="dim")
        return True
    else:
        console.print(f"Indexing failed with return code {result.returncode}", style="red")
        if result.stderr:
            for line in result.stderr.strip().split('\n')[-10:]:
                console.print(f"   {line}", style="red")
        if result.stdout:
            for line in result.stdout.strip().split('\n')[-10:]:
                console.print(f"   {line}", style="yellow")
        return False


def main():
    """Main startup check - always run indexer, monthly force rebuild."""
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

    # Determine if we need force rebuild (compare doc count to file count)
    force_rebuild, reason = should_force_rebuild(doc_count, len(doc_files))
    console.print(f"Mode: {reason}", style="cyan")
    print(f"Mode: {reason}")

    # Always run the indexer - it handles incremental updates
    if run_indexing(force_rebuild=force_rebuild):
        # Save force rebuild time if we did a force rebuild
        if force_rebuild:
            save_force_rebuild_time()

        # Verify final state
        time.sleep(2)
        new_count = get_index_doc_count(client)
        msg = f"Index ready with {new_count:,} documents"
        console.print(msg, style="green")
        print(msg)
    else:
        console.print("Failed to index documents!", style="red")
        sys.exit(1)

    # Signal that startup is complete - MCP server waits for this
    ready_file = Path("/data/logs/startup_complete")
    ready_file.touch()

    print("\nStartup check complete - services can start\n")


if __name__ == "__main__":
    main()
