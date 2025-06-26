#!/usr/bin/env python3
"""
Startup check script for Docker container.
Ensures Meilisearch is indexed before starting other services.
"""

import os
import sys
import time
import json
from pathlib import Path
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
        index = client.index(index_name)
        stats = index.get_stats()
        doc_count = stats.get('numberOfDocuments', 0)
        return True, doc_count
    except Exception:
        return False, 0

def run_indexing():
    """Run the indexing script."""
    console.print("🔨 Starting indexing process...", style="blue")
    
    # Run the indexing script
    import subprocess
    result = subprocess.run([
        sys.executable, 
        "/app/scripts/index_to_meilisearch.py",
        "--docs-path", "/data/documentation"
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        console.print("✅ Indexing completed successfully!", style="green")
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
    
    if not index_exists or doc_count < 300000:
        console.print(f"⚠️  Index needs initialization (current docs: {doc_count})", style="yellow")
        
        # Check if documentation exists
        docs_path = Path("/data/documentation")
        if not docs_path.exists() or not any(docs_path.rglob("*.md")):
            console.print("❌ No documentation found in /data/documentation!", style="red")
            console.print("Please ensure documentation is included in the Docker image.", style="red")
            sys.exit(1)
        
        # Run indexing
        if run_indexing():
            # Verify indexing worked
            _, new_count = check_index_status(client)
            if new_count >= 300000:
                console.print(f"✅ Index ready with {new_count:,} documents!", style="green")
            else:
                console.print(f"⚠️  Index has {new_count:,} documents (expected >300,000)", style="yellow")
        else:
            console.print("❌ Failed to index documents!", style="red")
            sys.exit(1)
    else:
        console.print(f"✅ Index already initialized with {doc_count:,} documents!", style="green")
    
    console.print("\n✨ Startup check complete! Services can start.\n", style="bold green")

if __name__ == "__main__":
    main()