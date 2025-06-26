#!/usr/bin/env python3
"""Check failed Meilisearch tasks to understand why documents didn't index."""

import os
import meilisearch
from dotenv import load_dotenv
from rich.console import Console
from collections import defaultdict

load_dotenv()

console = Console()

def check_failed_tasks():
    """Check Meilisearch task history for failures."""
    client = meilisearch.Client(
        os.getenv('MEILI_HTTP_ADDR', 'http://localhost:7700'),
        os.getenv('MEILI_MASTER_KEY', '')
    )
    
    console.print("🔍 Checking Meilisearch task history for failures...\n")
    
    # Get recent tasks with failures
    tasks = client.get_tasks({
        'statuses': ['failed'],
        'limit': 100  # Get last 100 failed tasks
    })
    
    # Analyze failure reasons
    error_types = defaultdict(list)
    
    for task in tasks.results:
        if hasattr(task, 'error') and task.error:
            error_code = task.error.get('code', 'unknown')
            error_msg = task.error.get('message', 'No message')
            error_types[error_code].append({
                'task_id': task.uid,
                'type': task.type,
                'message': error_msg,
                'details': task.details if hasattr(task, 'details') else None
            })
    
    # Print summary
    console.print(f"[red]Found {len(tasks.results)} failed tasks[/red]\n")
    
    for error_code, errors in error_types.items():
        console.print(f"[bold]Error Code: {error_code}[/bold] ({len(errors)} occurrences)")
        
        # Show first few examples
        for error in errors[:3]:
            console.print(f"  Task {error['task_id']}: {error['message']}")
            if error['details']:
                console.print(f"    Details: {error['details']}")
        
        if len(errors) > 3:
            console.print(f"  ... and {len(errors) - 3} more\n")
        else:
            console.print()
    
    # Get successful document addition tasks
    console.print("📊 Checking successful indexing tasks...")
    success_tasks = client.get_tasks({
        'statuses': ['succeeded'],
        'types': ['documentAdditionOrUpdate'],
        'limit': 10
    })
    
    total_indexed = 0
    for task in success_tasks.results:
        if hasattr(task, 'details') and 'indexedDocuments' in task.details:
            indexed = task.details['indexedDocuments']
            total = task.details.get('receivedDocuments', 0)
            console.print(f"  Task {task.uid}: Indexed {indexed}/{total} documents")
            total_indexed += indexed

if __name__ == "__main__":
    check_failed_tasks()