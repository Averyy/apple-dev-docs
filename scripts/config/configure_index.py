#!/usr/bin/env python3
"""Configure Meilisearch index settings."""

import os
import meilisearch
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()

console = Console()

def configure_index():
    """Configure the apple-docs index settings."""
    client = meilisearch.Client(
        os.getenv('MEILI_HTTP_ADDR', 'http://localhost:7700'),
        os.getenv('MEILI_MASTER_KEY', '')
    )
    
    index = client.index('apple-docs')
    
    console.print("🔧 Configuring index settings...")
    
    # Configure filterable attributes
    console.print("  Setting filterable attributes...")
    task = index.update_filterable_attributes([
        'framework',
        'platforms',
        'kind',
        'is_framework_main',
        'file_path',
        'api_name',
        'is_chunk'
    ])
    console.print(f"    Task submitted: {task.task_uid}")
    
    # Configure sortable attributes
    console.print("  Setting sortable attributes...")
    task = index.update_sortable_attributes([
        'last_modified',
        'file_size'
    ])
    console.print(f"    Task submitted: {task.task_uid}")
    
    # Configure searchable attributes with priority
    console.print("  Setting searchable attributes...")
    task = index.update_searchable_attributes([
        'title',
        'api_name',
        'overview',
        'content',
        'content_cleaned'
    ])
    console.print(f"    Task submitted: {task.task_uid}")
    
    # Configure faceting settings to show all frameworks
    console.print("  Setting faceting settings...")
    task = index.update_settings({
        'faceting': {
            'maxValuesPerFacet': 500  # Allow up to 500 framework values
        }
    })
    console.print(f"    Task submitted: {task.task_uid}")
    
    console.print("✅ Index settings configured successfully!")
    
    # Verify settings
    settings = index.get_settings()
    console.print(f"\nFilterable attributes: {settings['filterableAttributes']}")
    console.print(f"Faceting settings: {settings['faceting']}")

if __name__ == "__main__":
    configure_index()