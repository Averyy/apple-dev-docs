#!/usr/bin/env python3
"""Test script to verify indexing completeness and find missing documents."""

import os
import sys
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set

# Add parent directory to path to import local modules
sys.path.append(str(Path(__file__).parent.parent))

from scripts.metadata_extractor import MetadataExtractor
from scripts.document_processor import DocumentProcessor

def count_markdown_files_by_framework(docs_path: Path) -> Dict[str, int]:
    """Count markdown files per framework directory."""
    framework_counts = defaultdict(int)
    
    # Get all top-level directories (frameworks)
    for framework_dir in docs_path.iterdir():
        if framework_dir.is_dir() and not framework_dir.name.startswith('.'):
            # Count all .md files in this framework
            md_files = list(framework_dir.rglob("*.md"))
            framework_counts[framework_dir.name] = len(md_files)
    
    return dict(framework_counts)

def analyze_indexing_process(docs_path: Path, sample_frameworks: List[str] = None) -> Dict:
    """Analyze what would be indexed by the current process."""
    metadata_extractor = MetadataExtractor()
    document_processor = DocumentProcessor()
    
    results = {
        'total_files': 0,
        'by_framework': defaultdict(lambda: {
            'files_found': 0,
            'documents_created': 0,
            'files_with_errors': 0,
            'sample_ids': [],
            'error_samples': []
        }),
        'framework_mismatches': [],
        'processing_errors': []
    }
    
    # Process all or sample frameworks
    if sample_frameworks:
        framework_dirs = [docs_path / fw for fw in sample_frameworks if (docs_path / fw).exists()]
    else:
        framework_dirs = [d for d in docs_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    for framework_dir in framework_dirs:
        framework_name = framework_dir.name
        md_files = list(framework_dir.rglob("*.md"))
        
        results['total_files'] += len(md_files)
        results['by_framework'][framework_name]['files_found'] = len(md_files)
        
        # Sample processing to check for issues
        sample_size = min(50, len(md_files))  # Process up to 50 files per framework
        
        for i, file_path in enumerate(md_files[:sample_size]):
            try:
                # Process document
                documents = document_processor.process_document(str(file_path))
                results['by_framework'][framework_name]['documents_created'] += len(documents)
                
                # Check framework assignment
                for doc in documents:
                    extracted_framework = doc.get('framework', 'Unknown')
                    if extracted_framework != framework_name:
                        results['framework_mismatches'].append({
                            'file': str(file_path),
                            'expected': framework_name,
                            'extracted': extracted_framework
                        })
                    
                    # Collect sample IDs
                    if len(results['by_framework'][framework_name]['sample_ids']) < 5:
                        results['by_framework'][framework_name]['sample_ids'].append(doc['id'])
                        
            except Exception as e:
                results['by_framework'][framework_name]['files_with_errors'] += 1
                error_info = {
                    'file': str(file_path),
                    'error': str(e)
                }
                results['processing_errors'].append(error_info)
                if len(results['by_framework'][framework_name]['error_samples']) < 3:
                    results['by_framework'][framework_name]['error_samples'].append(error_info)
        
        # Extrapolate document count based on sample
        if sample_size < len(md_files) and sample_size > 0:
            avg_docs_per_file = results['by_framework'][framework_name]['documents_created'] / sample_size
            estimated_total_docs = int(avg_docs_per_file * len(md_files))
            results['by_framework'][framework_name]['estimated_documents'] = estimated_total_docs
    
    return results

def check_hash_file_coverage(hash_file_path: Path, docs_path: Path) -> Dict:
    """Check which files are covered by the hash file."""
    if not hash_file_path.exists():
        return {'error': 'Hash file not found'}
    
    with open(hash_file_path, 'r') as f:
        hashes = json.load(f)
    
    # Count files per framework in hash file
    framework_counts = defaultdict(int)
    for file_path in hashes.keys():
        parts = Path(file_path).parts
        if len(parts) > 0:
            framework = parts[0]
            framework_counts[framework] += 1
    
    return dict(framework_counts)

def main():
    """Run comprehensive indexing analysis."""
    docs_path = Path("../documentation")
    hash_file = Path("../.hashes/meilisearch_hashes.json")
    
    print("🔍 Apple Documentation Indexing Analysis\n")
    
    # Count actual files
    print("📁 Counting markdown files by framework...")
    actual_counts = count_markdown_files_by_framework(docs_path)
    
    # Sort by count descending
    sorted_frameworks = sorted(actual_counts.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\nTop 20 frameworks by file count:")
    total_files = 0
    for framework, count in sorted_frameworks[:20]:
        print(f"  {framework:20s}: {count:6,} files")
        total_files += count
    
    total_all = sum(actual_counts.values())
    print(f"\nTotal files: {total_all:,}")
    
    # Check hash file coverage
    print("\n📋 Checking hash file coverage...")
    hash_coverage = check_hash_file_coverage(hash_file, docs_path)
    
    if 'error' not in hash_coverage:
        print(f"\nFrameworks in hash file: {len(hash_coverage)}")
        missing_frameworks = set(actual_counts.keys()) - set(hash_coverage.keys())
        if missing_frameworks:
            print(f"Frameworks missing from hash file: {', '.join(sorted(missing_frameworks))}")
        
        # Compare counts
        print("\n📊 Comparing file counts (actual vs hashed):")
        discrepancies = []
        for framework in sorted_frameworks[:10]:
            fw_name = framework[0]
            actual = actual_counts.get(fw_name, 0)
            hashed = hash_coverage.get(fw_name, 0)
            diff = actual - hashed
            if abs(diff) > 10:  # Only show significant differences
                discrepancies.append((fw_name, actual, hashed, diff))
                print(f"  {fw_name:20s}: {actual:6,} actual, {hashed:6,} hashed, {diff:+7,} difference")
    
    # Analyze indexing process for problematic frameworks
    print("\n🔬 Analyzing indexing process for problematic frameworks...")
    problematic_frameworks = ['UIKit', 'Foundation', 'AppKit', 'Swift', 'SwiftUI']
    
    analysis = analyze_indexing_process(docs_path, problematic_frameworks)
    
    print("\nFramework Analysis Results:")
    for framework in problematic_frameworks:
        if framework in analysis['by_framework']:
            data = analysis['by_framework'][framework]
            print(f"\n{framework}:")
            print(f"  Files found: {data['files_found']:,}")
            print(f"  Documents created (sample): {data['documents_created']}")
            if 'estimated_documents' in data:
                print(f"  Estimated total documents: {data['estimated_documents']:,}")
            print(f"  Files with errors: {data['files_with_errors']}")
            if data['sample_ids']:
                print(f"  Sample document IDs: {', '.join(data['sample_ids'][:3])}")
            if data['error_samples']:
                print(f"  Sample errors:")
                for err in data['error_samples'][:2]:
                    print(f"    - {Path(err['file']).name}: {err['error']}")
    
    if analysis['framework_mismatches']:
        print(f"\n⚠️  Framework mismatches found: {len(analysis['framework_mismatches'])}")
        for mismatch in analysis['framework_mismatches'][:5]:
            print(f"  {Path(mismatch['file']).relative_to(docs_path)}")
            print(f"    Expected: {mismatch['expected']}, Got: {mismatch['extracted']}")
    
    # Create verification script
    print("\n📝 Creating verification script...")
    create_verification_script(actual_counts)
    print("Created scripts/verify_indexed_counts.py")

def create_verification_script(expected_counts: Dict[str, int]):
    """Create a script to verify indexed document counts."""
    script_content = '''#!/usr/bin/env python3
"""Verify that all documents are properly indexed in Meilisearch."""

import os
import sys
import meilisearch
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

load_dotenv()

console = Console()

# Expected counts
EXPECTED_COUNTS = ''' + json.dumps(expected_counts, indent=4) + '''

def verify_index_counts():
    """Verify document counts in Meilisearch index."""
    client = meilisearch.Client(
        os.getenv('MEILI_HTTP_ADDR', 'http://localhost:7700'),
        os.getenv('MEILI_MASTER_KEY', '')
    )
    
    try:
        # Get index stats
        stats = client.index('apple-docs').get_stats()
        total_indexed = stats.get('numberOfDocuments', 0)
        
        console.print(f"\\nTotal documents in index: {total_indexed:,}")
        
        # Check counts by framework
        console.print("\\nChecking document counts by framework...")
        
        table = Table(title="Framework Document Counts")
        table.add_column("Framework", style="cyan")
        table.add_column("Expected", style="green")
        table.add_column("Indexed", style="yellow")
        table.add_column("Difference", style="red")
        table.add_column("Status", style="blue")
        
        total_expected = sum(EXPECTED_COUNTS.values())
        total_found = 0
        missing_total = 0
        
        for framework, expected in sorted(EXPECTED_COUNTS.items(), key=lambda x: x[1], reverse=True)[:20]:
            # Search for documents with this framework
            result = client.index('apple-docs').search('', {
                'filter': f'framework = "{framework}"',
                'limit': 1
            })
            
            indexed = result.get('estimatedTotalHits', 0)
            total_found += indexed
            diff = indexed - expected
            missing_total += max(0, -diff)
            
            status = "✓" if abs(diff) < 10 else "✗"
            
            table.add_row(
                framework,
                f"{expected:,}",
                f"{indexed:,}",
                f"{diff:+,}",
                status
            )
        
        console.print(table)
        
        console.print(f"\\nTotal expected: {total_expected:,}")
        console.print(f"Total found by framework filter: {total_found:,}")
        console.print(f"Total missing: {missing_total:,}")
        
        return total_indexed, total_expected, missing_total
        
    except Exception as e:
        console.print(f"[red]Error connecting to Meilisearch: {e}[/red]")
        return 0, sum(EXPECTED_COUNTS.values()), sum(EXPECTED_COUNTS.values())

if __name__ == "__main__":
    indexed, expected, missing = verify_index_counts()
    
    if missing > 0:
        console.print(f"\\n[red]⚠️  Missing {missing:,} documents![/red]")
        sys.exit(1)
    else:
        console.print(f"\\n[green]✓ All documents indexed successfully![/green]")
'''
    
    with open('verify_indexed_counts.py', 'w') as f:
        f.write(script_content)
    os.chmod('verify_indexed_counts.py', 0o755)

if __name__ == "__main__":
    main()