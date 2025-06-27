#!/usr/bin/env python3
"""
Enhanced startup check script for Docker container.
Detects content changes using hash timestamps to trigger re-indexing.
"""

import os
import sys
import time
import json
from pathlib import Path
from datetime import datetime
import meilisearch
from rich.console import Console

console = Console()

def wait_for_meilisearch(url: str, api_key: str, max_attempts: int = 30):
    """Wait for Meilisearch to be ready."""
    console.print("⏳ Waiting for Meilisearch to start...", style="yellow")
    
    for attempt in range(max_attempts):
        try:
            client = meilisearch.Client(url, api_key)
            # Try to get health status
            client.health()
            console.print("✅ Meilisearch is ready!", style="green")
            return True
        except Exception as e:
            if attempt < max_attempts - 1:
                time.sleep(2)
            else:
                console.print(f"❌ Meilisearch failed to start after {max_attempts} attempts", style="red")
                return False
    return False

def check_index_status(client: meilisearch.Client, index_name: str = "apple-docs") -> tuple[bool, int]:
    """Check if index exists and has documents."""
    try:
        # Get all indexes to check if ours exists
        indexes = client.get_indexes()
        index_exists = False
        
        for idx in indexes.get('results', []):
            # idx is an Index object
            if idx.uid == index_name:
                index_exists = True
                break
        
        if not index_exists:
            return False, 0
            
        # Index exists, now get document count
        index = client.index(index_name)
        stats = index.get_stats()
        # IMPORTANT: Meilisearch Python client returns an IndexStats OBJECT (not dict)
        # with snake_case attributes. HTTP API returns camelCase but Python client
        # converts to snake_case. Use stats.number_of_documents NOT numberOfDocuments
        doc_count = stats.number_of_documents
        return True, doc_count
    except Exception as e:
        # Log the error for debugging
        console.print(f"[yellow]Warning: Error checking index status: {e}[/yellow]")
        return False, 0

def get_last_index_time() -> datetime | None:
    """Get the last time we indexed to Meilisearch."""
    index_time_file = Path("/data/meilisearch/last_meilisearch_index.txt")
    if index_time_file.exists():
        try:
            timestamp_str = index_time_file.read_text().strip()
            return datetime.fromisoformat(timestamp_str)
        except:
            return None
    return None

def save_index_time():
    """Save the current time as the last index time."""
    index_time_file = Path("/data/meilisearch/last_meilisearch_index.txt")
    index_time_file.parent.mkdir(parents=True, exist_ok=True)
    index_time_file.write_text(datetime.now().isoformat())

def get_most_recent_hash_update() -> datetime | None:
    """Find the most recent update time across all hash files."""
    # In Docker, we don't use hash files anymore - everything is in meilisearch volume
    # This function is kept for compatibility but returns None in Docker
    return None
    
    # Legacy code for local/non-Docker usage
    hashes_dir = Path("/data/hashes")
    if not hashes_dir.exists():
        return None
    
    most_recent = None
    
    # Check all framework hash files
    for hash_file in hashes_dir.glob("*_hashes.json"):
        if hash_file.name == "meilisearch_hashes.json":
            continue  # Skip the index hash file
            
        try:
            with open(hash_file, 'r') as f:
                data = json.load(f)
                if 'metadata' in data and 'last_updated' in data['metadata']:
                    update_time = datetime.fromisoformat(data['metadata']['last_updated'])
                    if most_recent is None or update_time > most_recent:
                        most_recent = update_time
        except:
            continue
    
    return most_recent

def needs_reindexing() -> tuple[bool, str]:
    """Check if we need to re-index based on hash timestamps."""
    last_index = get_last_index_time()
    last_hash_update = get_most_recent_hash_update()
    
    if last_index is None:
        return True, "No previous index timestamp found"
    
    if last_hash_update is None:
        return False, "No hash timestamps found"
    
    if last_hash_update > last_index:
        time_diff = last_hash_update - last_index
        return True, f"Documentation updated {time_diff} after last index"
    
    return False, "Index is up to date with documentation"

def run_indexing(force_rebuild=False):
    """Run the indexing script."""
    msg = "🔨 Starting indexing process..."
    console.print(msg, style="blue")
    print(msg)  # Also to stdout for Docker logs
    
    # Build command
    cmd = [
        sys.executable, 
        "/app/scripts/index_to_meilisearch.py",
        "--docs-path", "/data/documentation"
    ]
    
    # Add force flag if documentation has changed
    if force_rebuild:
        cmd.append("--force")
        msg = "🔄 Full rebuild due to documentation changes"
        console.print(f"[yellow]{msg}[/yellow]")
        print(msg)  # Also to stdout for Docker logs
    
    # Run the indexing script
    import subprocess
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        console.print("✅ Indexing completed successfully!", style="green")
        # Save the index timestamp
        save_index_time()
        # Log stdout for debugging
        if result.stdout:
            for line in result.stdout.strip().split('\n')[-5:]:
                if line.strip():
                    console.print(f"   {line}", style="dim")
        return True
    else:
        console.print(f"❌ Indexing failed with return code {result.returncode}", style="red")
        if result.stderr:
            console.print("Error output:", style="red")
            for line in result.stderr.strip().split('\n'):
                console.print(f"   {line}", style="red")
        if result.stdout:
            console.print("Standard output:", style="yellow")
            for line in result.stdout.strip().split('\n')[-10:]:
                console.print(f"   {line}", style="yellow")
        return False

def main():
    """Main startup check."""
    # Always print to both console and stdout for Docker logs
    print("\n🚀 Apple Docs MCP Server - Startup Check")
    print("=" * 50)
    console.print("\n🚀 Apple Docs MCP Server - Startup Check", style="bold blue")
    console.print("=" * 50)
    
    # Get environment variables
    meilisearch_url = os.getenv("MEILI_HTTP_ADDR", "http://localhost:7700")
    meilisearch_key = os.getenv("MEILI_MASTER_KEY", "")
    
    # Wait for Meilisearch to be ready
    if not wait_for_meilisearch(meilisearch_url, meilisearch_key):
        sys.exit(1)
    
    # Check index status
    client = meilisearch.Client(meilisearch_url, meilisearch_key)
    index_exists, doc_count = check_index_status(client)
    
    # Check if we need to re-index based on hash timestamps
    needs_index, reason = needs_reindexing()
    
    # Important status logging (always visible in Docker logs)
    if index_exists:
        msg = f"📦 Index status: {doc_count:,} documents indexed"
        console.print(msg)
        print(msg)  # Also to stdout for Docker logs
    if needs_index:
        msg = f"⚠️  Re-indexing needed: {reason}"
        console.print(msg)
        print(msg)  # Also to stdout for Docker logs
    elif index_exists:
        msg = f"✅ {reason}"
        console.print(msg)
        print(msg)  # Also to stdout for Docker logs
    
    if not index_exists or doc_count < 300000 or needs_index:
        if not index_exists:
            console.print("⚠️  Index does not exist", style="yellow")
        elif doc_count < 300000:
            console.print(f"⚠️  Index has insufficient documents ({doc_count:,})", style="yellow")
        # else case removed - reason already shown above
        
        # Check if documentation exists
        docs_path = Path("/data/documentation")
        if not docs_path.exists() or not any(docs_path.rglob("*.md")):
            console.print("❌ No documentation found in /data/documentation!", style="red")
            console.print("Please ensure documentation is included in the Docker image.", style="red")
            sys.exit(1)
        
        # Run indexing (force rebuild if docs changed)
        if run_indexing(force_rebuild=needs_index):
            # Wait a bit for Meilisearch to update stats
            time.sleep(2)
            
            # Verify indexing worked with retries
            new_count = 0  # Initialize in case loop doesn't run properly
            for retry in range(10):  # More retries
                index_exists, new_count = check_index_status(client)
                if index_exists and new_count >= 300000:
                    msg = f"✅ Index ready with {new_count:,} documents!"
                    console.print(msg, style="green")
                    print(msg)  # Also to stdout
                    break
                elif retry < 9:
                    if retry == 0:
                        console.print("⏳ Waiting for Meilisearch to finish indexing...", style="dim")
                    time.sleep(3)  # Longer wait between retries
            
            # Only show error messages if we didn't succeed
            if not (index_exists and new_count >= 300000):
                if not index_exists:
                    console.print(f"❌ Index creation may have failed", style="red")
                elif new_count == 0:
                    msg = f"⚠️  Index created but stats not updated yet (Meilisearch may still be processing)"
                    console.print(msg, style="yellow")
                    print(msg)  # Also to stdout
                else:
                    msg = f"✅ Index ready with {new_count:,} documents!"
                    console.print(msg, style="green")
                    print(msg)  # Also to stdout
        else:
            console.print("❌ Failed to index documents!", style="red")
            sys.exit(1)
    else:
        msg = f"✅ Index already initialized with {doc_count:,} documents!"
        console.print(msg, style="green")
        print(msg)  # Also to stdout for Docker logs
        console.print(f"   {reason}", style="dim")
    
    final_msg = "\n✨ Startup check complete! Services can start.\n"
    console.print(final_msg, style="bold green")
    print(final_msg)  # Also to stdout

if __name__ == "__main__":
    main()