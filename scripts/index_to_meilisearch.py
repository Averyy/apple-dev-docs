#!/usr/bin/env python3
"""
Index Apple Developer Documentation to Meilisearch

This script reads all markdown files from the documentation directory,
processes them with metadata extraction and document chunking,
and indexes them into Meilisearch with incremental update support.
"""

import os
import sys
import json
import hashlib
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import time

import meilisearch
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn
from rich.table import Table
from dotenv import load_dotenv
from collections import defaultdict

# Add parent directory to path to import local modules
sys.path.append(str(Path(__file__).parent.parent))

from scripts.metadata_extractor import MetadataExtractor
from scripts.document_processor import DocumentProcessor

# Load environment variables
load_dotenv()

console = Console()

class MeilisearchIndexer:
    """Handles indexing of Apple documentation to Meilisearch"""
    
    def __init__(self, 
                 meilisearch_url: str,
                 api_key: str,
                 docs_path: str = "../documentation",
                 index_name: str = "apple-docs",
                 batch_size: int = 50,
                 hash_file: str = "../.hashes/meilisearch_hashes.json"):
        """
        Initialize the indexer
        
        Args:
            meilisearch_url: URL of Meilisearch instance
            api_key: Master key or API key for Meilisearch
            docs_path: Path to documentation directory
            index_name: Name of the Meilisearch index
            batch_size: Number of documents to upload in each batch
            hash_file: Path to store file hashes for incremental updates
        """
        self.client = meilisearch.Client(meilisearch_url, api_key)
        self.docs_path = Path(docs_path).resolve()
        self.index_name = index_name
        self.batch_size = batch_size
        self.hash_file = Path(hash_file)
        
        self.metadata_extractor = MetadataExtractor()
        self.document_processor = DocumentProcessor()
        
        # Statistics
        self.stats = {
            "total_files": 0,
            "processed": 0,
            "skipped": 0,
            "errors": 0,
            "chunks_created": 0,
            "start_time": time.time()
        }
        
    def load_hashes(self) -> Dict[str, str]:
        """Load stored file hashes for incremental updates"""
        if self.hash_file.exists():
            try:
                with open(self.hash_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                console.print(f"[yellow]Warning: Could not load hash file: {e}[/yellow]")
        return {}
    
    def save_hashes(self, hashes: Dict[str, str]):
        """Save file hashes for next run"""
        try:
            with open(self.hash_file, 'w') as f:
                json.dump(hashes, f, indent=2)
        except Exception as e:
            console.print(f"[red]Error saving hash file: {e}[/red]")
    
    def compute_file_hash(self, file_path: Path) -> str:
        """Compute SHA-256 hash of a file"""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    def discover_markdown_files(self) -> List[Path]:
        """Find all markdown files in documentation directory"""
        return list(self.docs_path.rglob("*.md"))
    
    def ensure_index_exists(self, force_rebuild: bool = False):
        """Create index if it doesn't exist and configure it"""
        try:
            index = self.client.index(self.index_name)
            if force_rebuild:
                # Delete existing index to ensure clean rebuild
                console.print(f"[yellow]Deleting existing index '{self.index_name}' for clean rebuild...[/yellow]")
                task = self.client.delete_index(self.index_name)
                # Wait a moment for deletion to complete
                time.sleep(2)
                # Create fresh index
                task = self.client.create_index(self.index_name, {'primaryKey': 'id'})
                console.print(f"[green]Created fresh index '{self.index_name}'[/green]")
                # Wait for creation to complete
                self.client.wait_for_task(task.task_uid)
                # Get the new index and configure it
                index = self.client.index(self.index_name)
                self.configure_index_settings(index)
            else:
                console.print(f"[green]Using existing index '{self.index_name}'[/green]")
                # Configure index settings in case they were lost
                self.configure_index_settings(index)
        except Exception:
            # Index doesn't exist, create it
            task = self.client.create_index(self.index_name, {'primaryKey': 'id'})
            console.print(f"[green]Created new index '{self.index_name}'[/green]")
            # Wait for task to complete
            self.client.wait_for_task(task.task_uid)
            # Configure the new index
            index = self.client.index(self.index_name)
            self.configure_index_settings(index)
    
    def configure_index_settings(self, index):
        """Configure index settings for filtering and searching"""
        console.print("🔧 Configuring index settings...")
        
        # Configure filterable attributes
        task = index.update_filterable_attributes([
            'framework',
            'platforms',
            'kind',
            'is_framework_main',
            'file_path',
            'api_name',
            'is_chunk'
        ])
        self.client.wait_for_task(task.task_uid)
        
        # Configure sortable attributes
        task = index.update_sortable_attributes([
            'last_modified',
            'file_size'
        ])
        self.client.wait_for_task(task.task_uid)
        
        # Configure searchable attributes with priority
        task = index.update_searchable_attributes([
            'title',
            'api_name',
            'overview',
            'content',
            'content_cleaned'
        ])
        self.client.wait_for_task(task.task_uid)
        
        # Configure faceting settings to show all frameworks
        task = index.update_settings({
            'faceting': {
                'maxValuesPerFacet': 500  # Allow up to 500 framework values
            }
        })
        self.client.wait_for_task(task.task_uid)
        
        console.print("✅ Index settings configured")
    
    def process_file(self, file_path: Path) -> List[Dict]:
        """Process a single markdown file into documents"""
        try:
            # Process with document processor (it reads the file internally)
            documents = self.document_processor.process_document(str(file_path))
            return documents
                
        except Exception as e:
            console.print(f"[red]Error processing {file_path}: {e}[/red]")
            self.stats['errors'] += 1
            return []
    
    def index_documents(self, documents: List[Dict], show_progress: bool = True):
        """Index documents to Meilisearch in batches"""
        if not documents:
            return
            
        total_batches = (len(documents) + self.batch_size - 1) // self.batch_size
        
        if show_progress:
            progress = Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeRemainingColumn(),
                console=console
            )
            
            with progress:
                task = progress.add_task(
                    f"Indexing {len(documents)} documents...", 
                    total=total_batches
                )
                
                for i in range(0, len(documents), self.batch_size):
                    batch = documents[i:i + self.batch_size]
                    try:
                        response = self.client.index(self.index_name).add_documents(batch)
                        # For large indexing jobs, wait for tasks to complete periodically
                        if (i // self.batch_size) % 100 == 0 and i > 0:
                            # Every 100 batches, wait for tasks to complete
                            time.sleep(1)  # Give Meilisearch a breather
                    except Exception as e:
                        console.print(f"[red]Error indexing batch: {e}[/red]")
                        self.stats['errors'] += 1
                    
                    progress.update(task, advance=1)
        else:
            # Index without progress bar
            for i in range(0, len(documents), self.batch_size):
                batch = documents[i:i + self.batch_size]
                try:
                    self.client.index(self.index_name).add_documents(batch)
                except Exception as e:
                    console.print(f"[red]Error indexing batch: {e}[/red]")
                    self.stats['errors'] += 1
    
    def run(self, limit: Optional[int] = None, dry_run: bool = False, force: bool = False):
        """
        Run the indexing process
        
        Args:
            limit: Maximum number of files to process (for testing)
            dry_run: If True, don't actually index documents
            force: If True, reindex all files regardless of hash
        """
        if force:
            console.print("\n[bold]Apple Documentation Meilisearch Indexer - Full Rebuild Mode[/bold]\n")
            console.print("[yellow]⚠️  This will delete and rebuild the entire index from scratch[/yellow]")
            print("\n🔄 Full index rebuild initiated")
        else:
            console.print("\n[bold]Apple Documentation Meilisearch Indexer[/bold]\n")
            print("\n🔍 Checking for documentation updates...")
        
        # Only rebuild if forced
        if not dry_run:
            self.ensure_index_exists(force_rebuild=force)
        
        # Load existing hashes unless force rebuild
        if force:
            existing_hashes = {}
        else:
            existing_hashes = self.load_hashes()
        new_hashes = {}
        
        # Discover files
        console.print("🔍 Discovering markdown files...")
        all_files = self.discover_markdown_files()
        self.stats['total_files'] = len(all_files)
        
        # Count files by framework
        framework_counts = defaultdict(int)
        for file_path in all_files:
            parts = file_path.relative_to(self.docs_path).parts
            if parts:
                framework = parts[0]
                framework_counts[framework] += 1
        
        console.print(f"📁 Found {len(all_files)} markdown files across {len(framework_counts)} frameworks")
        console.print(f"   Top frameworks: {', '.join(f'{k}:{v}' for k, v in sorted(framework_counts.items(), key=lambda x: x[1], reverse=True)[:5])}")
        
        if limit:
            all_files = all_files[:limit]
            console.print(f"[yellow]Limited to {limit} files[/yellow]")
        
        if force:
            console.print(f"\n🔄 Full rebuild mode - processing all {len(all_files)} files")
        else:
            console.print(f"\n📋 Processing {len(all_files)} files (checking for changes)...")
        
        console.print(f"\n📋 Existing hashes: {len(existing_hashes)} files")
        
        # Process files
        documents_to_index = []
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TextColumn("{task.completed}/{task.total}"),
            TimeRemainingColumn(),
            console=console
        ) as progress:
            
            task = progress.add_task("Processing files...", total=len(all_files))
            
            for file_path in all_files:
                # Compute hash
                file_hash = self.compute_file_hash(file_path)
                relative_path = file_path.relative_to(self.docs_path)
                
                # Check if file needs processing
                if not force and str(relative_path) in existing_hashes:
                    if existing_hashes[str(relative_path)] == file_hash:
                        self.stats['skipped'] += 1
                        progress.update(task, advance=1)
                        continue
                
                # Process file
                documents = self.process_file(file_path)
                if documents:
                    documents_to_index.extend(documents)
                    new_hashes[str(relative_path)] = file_hash
                    self.stats['processed'] += 1
                    self.stats['chunks_created'] += len(documents)
                    
                    # Log progress for debugging
                    if self.stats['processed'] % 1000 == 0:
                        console.print(f"[dim]Processed {self.stats['processed']} files, created {self.stats['chunks_created']} documents[/dim]")
                
                progress.update(task, advance=1)
        
        # Index documents
        if documents_to_index and not dry_run:
            console.print(f"\n📤 Indexing {len(documents_to_index)} documents to Meilisearch...")
            self.index_documents(documents_to_index)
        elif dry_run:
            console.print(f"\n[yellow]Dry run: Would index {len(documents_to_index)} documents[/yellow]")
        else:
            console.print("\n[green]No new or changed documents to index[/green]")
        
        # Save hashes for next run
        if not dry_run and (new_hashes or force):
            # Merge with existing hashes unless force mode
            if force:
                all_hashes = new_hashes
            else:
                all_hashes = {**existing_hashes, **new_hashes}
            
            # Ensure hash directory exists
            self.hash_file.parent.mkdir(parents=True, exist_ok=True)
            self.save_hashes(all_hashes)
            console.print(f"\n💾 Saved {len(all_hashes)} file hashes")
        
        # Print summary
        self.print_summary()
    
    def print_summary(self):
        """Print indexing summary"""
        duration = time.time() - self.stats['start_time']
        
        table = Table(title="Indexing Summary", show_header=False)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Total Files", str(self.stats['total_files']))
        table.add_row("Files Processed", str(self.stats['processed']))
        table.add_row("Files Skipped", str(self.stats['skipped']))
        table.add_row("Documents Created", str(self.stats['chunks_created']))
        table.add_row("Errors", str(self.stats['errors']) if self.stats['errors'] == 0 else f"[red]{self.stats['errors']}[/red]")
        table.add_row("Duration", f"{duration:.2f} seconds")
        
        if self.stats['processed'] > 0:
            rate = self.stats['processed'] / duration
            table.add_row("Processing Rate", f"{rate:.1f} files/second")
        
        console.print("\n")
        console.print(table)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Index Apple Developer Documentation to Meilisearch"
    )
    parser.add_argument(
        "--url",
        default=os.getenv("MEILI_HTTP_ADDR", "http://localhost:7700"),
        help="Meilisearch URL (default: http://localhost:7700 or MEILI_HTTP_ADDR env)"
    )
    parser.add_argument(
        "--api-key",
        default=os.getenv("MEILI_MASTER_KEY", ""),
        help="Meilisearch API key (default: MEILI_MASTER_KEY env)"
    )
    parser.add_argument(
        "--docs-path",
        default="../documentation",
        help="Path to documentation directory (default: ../documentation)"
    )
    parser.add_argument(
        "--index",
        default="apple-docs",
        help="Meilisearch index name (default: apple-docs)"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=50,
        help="Batch size for indexing (default: 50)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of files to process (for testing)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Process files but don't index to Meilisearch"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force reindex all files, ignoring hash cache"
    )
    
    args = parser.parse_args()
    
    # Validate Meilisearch connection
    if not args.dry_run:
        try:
            client = meilisearch.Client(args.url, args.api_key)
            health = client.health()
            console.print(f"[green]✓ Connected to Meilisearch at {args.url}[/green]")
        except Exception as e:
            console.print(f"[red]✗ Could not connect to Meilisearch at {args.url}: {e}[/red]")
            console.print("[yellow]Make sure Meilisearch is running and accessible[/yellow]")
            sys.exit(1)
    
    # Run indexer
    indexer = MeilisearchIndexer(
        meilisearch_url=args.url,
        api_key=args.api_key,
        docs_path=args.docs_path,
        index_name=args.index,
        batch_size=args.batch_size
    )
    
    indexer.run(limit=args.limit, dry_run=args.dry_run, force=args.force)


if __name__ == "__main__":
    main()