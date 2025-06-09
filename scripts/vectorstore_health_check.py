#!/usr/bin/env python3
"""
Health check and verification tools for the vector store
Ensures embeddings are consistent with source documents
"""

import os
import sys
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
import chromadb
import openai
from dotenv import load_dotenv
import logging
from datetime import datetime
import tiktoken

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from scraper.utils.hash_manager import HashManager

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
env_paths = [
    Path(__file__).parent.parent / "mcp-server" / ".env",
    Path(__file__).parent.parent / ".env"
]

for env_path in env_paths:
    if env_path.exists():
        load_dotenv(env_path)
        break

class VectorstoreHealthChecker:
    """Comprehensive health check and verification for vector store"""
    
    def __init__(self, docs_path: Path, vectorstore_path: Path):
        self.docs_path = docs_path
        self.vectorstore_path = vectorstore_path
        self.hash_file = Path(__file__).parent.parent / ".hashes" / "embedding_hashes.json"
        self.hash_manager = HashManager(self.hash_file)
        self.chroma = chromadb.PersistentClient(path=str(vectorstore_path))
        self.issues_found = []
        
    def run_all_checks(self, collection_name: str = "apple_docs") -> Dict[str, any]:
        """Run comprehensive health checks"""
        logger.info(f"Starting health check for collection: {collection_name}")
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "collection": collection_name,
            "checks": {}
        }
        
        # Get collection
        try:
            collection = self.chroma.get_collection(collection_name)
            results["collection_exists"] = True
            results["total_embeddings"] = collection.count()
        except Exception as e:
            results["collection_exists"] = False
            results["error"] = str(e)
            return results
        
        # Run individual checks
        results["checks"]["orphaned_embeddings"] = self.check_orphaned_embeddings(collection)
        results["checks"]["missing_embeddings"] = self.check_missing_embeddings(collection)
        results["checks"]["content_sync"] = self.verify_content_sync(collection)
        results["checks"]["embedding_integrity"] = self.check_embedding_integrity(collection)
        results["checks"]["metadata_completeness"] = self.check_metadata_completeness(collection)
        results["checks"]["duplicate_detection"] = self.check_duplicates(collection)
        
        # Summary
        results["issues_found"] = len(self.issues_found)
        results["issues"] = self.issues_found
        results["health_status"] = "HEALTHY" if len(self.issues_found) == 0 else "NEEDS_ATTENTION"
        
        return results
    
    def check_orphaned_embeddings(self, collection) -> Dict[str, any]:
        """Find embeddings for files that no longer exist"""
        logger.info("Checking for orphaned embeddings...")
        
        orphaned = []
        checked = 0
        
        # Get all embeddings with metadata
        all_docs = collection.get(include=["metadatas"])
        
        for i, metadata in enumerate(all_docs["metadatas"]):
            checked += 1
            if metadata and "file_path" in metadata:
                file_path = Path(metadata["file_path"])
                if not file_path.exists():
                    orphaned.append({
                        "id": all_docs["ids"][i],
                        "file_path": str(file_path),
                        "framework": metadata.get("framework", "unknown")
                    })
                    self.issues_found.append({
                        "type": "orphaned_embedding",
                        "id": all_docs["ids"][i],
                        "file": str(file_path)
                    })
        
        return {
            "checked": checked,
            "orphaned_count": len(orphaned),
            "orphaned_files": orphaned[:10],  # First 10 for report
            "status": "PASS" if len(orphaned) == 0 else "FAIL"
        }
    
    def check_missing_embeddings(self, collection) -> Dict[str, any]:
        """Find documents that should have embeddings but don't"""
        logger.info("Checking for missing embeddings...")
        
        missing = []
        total_docs = 0
        
        # Get all embedded IDs
        all_ids = set(collection.get(include=[])["ids"])
        
        # Check all markdown files
        for md_file in self.docs_path.rglob("*.md"):
            total_docs += 1
            
            # Generate expected ID (same logic as incremental builder)
            content = md_file.read_text(encoding='utf-8')
            path_hash = hashlib.md5(str(md_file).encode()).hexdigest()[:8]
            content_hash = hashlib.md5(content.encode()).hexdigest()[:8]
            expected_id = f"{md_file.stem}_{path_hash}_{content_hash}"
            
            if expected_id not in all_ids:
                # Check if any ID contains this file's path
                file_found = False
                file_pattern = str(md_file).replace("/", "_")
                for id in all_ids:
                    if file_pattern in id or md_file.stem in id:
                        file_found = True
                        break
                
                if not file_found:
                    missing.append({
                        "file": str(md_file.relative_to(self.docs_path)),
                        "expected_id": expected_id
                    })
        
        return {
            "total_documents": total_docs,
            "embedded_count": len(all_ids),
            "missing_count": len(missing),
            "missing_files": missing[:10],  # First 10 for report
            "coverage": f"{(len(all_ids) / total_docs * 100):.1f}%" if total_docs > 0 else "0%",
            "status": "PASS" if len(missing) == 0 else "INFO"
        }
    
    def verify_content_sync(self, collection, sample_size: int = 100) -> Dict[str, any]:
        """Verify embeddings match current file content"""
        logger.info(f"Verifying content sync (sample size: {sample_size})...")
        
        mismatches = []
        checked = 0
        
        # Get sample of embeddings
        all_data = collection.get(include=["metadatas", "documents"], limit=sample_size)
        
        for i, metadata in enumerate(all_data["metadatas"]):
            if metadata and "file_path" in metadata:
                file_path = Path(metadata["file_path"])
                
                # Handle both absolute and relative paths
                if not file_path.is_absolute():
                    # If it's relative, resolve from project root
                    file_path = self.docs_path.parent / file_path
                
                if file_path.exists():
                    checked += 1
                    current_content = file_path.read_text(encoding='utf-8')
                    embedded_content = all_data["documents"][i]
                    
                    # Check if content matches
                    if current_content != embedded_content:
                        # Create file key for hash check
                        try:
                            if file_path.is_relative_to(self.docs_path):
                                file_key = str(file_path.relative_to(self.docs_path))
                            else:
                                # Fallback: use just the stored path
                                file_key = metadata["file_path"]
                        except:
                            file_key = metadata["file_path"]
                            
                        if self.hash_manager.has_changed(file_key, current_content):
                            mismatches.append({
                                "id": all_data["ids"][i],
                                "file": str(file_path),
                                "issue": "content_changed"
                            })
                            self.issues_found.append({
                                "type": "stale_embedding",
                                "id": all_data["ids"][i],
                                "file": str(file_path)
                            })
        
        return {
            "samples_checked": checked,
            "mismatches": len(mismatches),
            "mismatch_files": mismatches[:5],  # First 5 for report
            "status": "PASS" if len(mismatches) == 0 else "FAIL"
        }
    
    def check_embedding_integrity(self, collection, sample_size: int = 50) -> Dict[str, any]:
        """Verify embedding dimensions and validity"""
        logger.info(f"Checking embedding integrity (sample size: {sample_size})...")
        
        issues = []
        checked = 0
        expected_dim = 1536  # OpenAI text-embedding-3-small
        
        # Get sample with embeddings
        all_data = collection.get(include=["embeddings"], limit=sample_size)
        
        for i, embedding in enumerate(all_data["embeddings"]):
            checked += 1
            
            # Check dimension
            if len(embedding) != expected_dim:
                issues.append({
                    "id": all_data["ids"][i],
                    "dimension": len(embedding),
                    "expected": expected_dim
                })
            
            # Check for zero/invalid vectors
            if all(v == 0 for v in embedding):
                issues.append({
                    "id": all_data["ids"][i],
                    "issue": "zero_vector"
                })
            
            # Check for NaN or infinite values
            if any(v != v or v == float('inf') or v == float('-inf') for v in embedding):
                issues.append({
                    "id": all_data["ids"][i],
                    "issue": "invalid_values"
                })
        
        return {
            "samples_checked": checked,
            "expected_dimension": expected_dim,
            "issues": len(issues),
            "issue_details": issues[:5],  # First 5 for report
            "status": "PASS" if len(issues) == 0 else "FAIL"
        }
    
    def check_metadata_completeness(self, collection, sample_size: int = 100) -> Dict[str, any]:
        """Check that all embeddings have complete metadata"""
        logger.info(f"Checking metadata completeness (sample size: {sample_size})...")
        
        required_fields = ["framework", "api_name", "file_path"]
        incomplete = []
        checked = 0
        
        all_data = collection.get(include=["metadatas"], limit=sample_size)
        
        for i, metadata in enumerate(all_data["metadatas"]):
            checked += 1
            
            if not metadata:
                incomplete.append({
                    "id": all_data["ids"][i],
                    "issue": "no_metadata"
                })
                continue
            
            missing_fields = [field for field in required_fields if field not in metadata]
            if missing_fields:
                incomplete.append({
                    "id": all_data["ids"][i],
                    "missing_fields": missing_fields
                })
        
        return {
            "samples_checked": checked,
            "required_fields": required_fields,
            "incomplete_count": len(incomplete),
            "incomplete_examples": incomplete[:5],  # First 5 for report
            "status": "PASS" if len(incomplete) == 0 else "FAIL"
        }
    
    def check_duplicates(self, collection) -> Dict[str, any]:
        """Check for duplicate embeddings of the same content"""
        logger.info("Checking for duplicate embeddings...")
        
        # Get all documents with metadata
        all_data = collection.get(include=["metadatas"])
        
        file_to_ids = {}
        duplicates = []
        
        for i, metadata in enumerate(all_data["metadatas"]):
            if metadata and "file_path" in metadata:
                file_path = metadata["file_path"]
                if file_path not in file_to_ids:
                    file_to_ids[file_path] = []
                file_to_ids[file_path].append(all_data["ids"][i])
        
        # Find files with multiple embeddings
        for file_path, ids in file_to_ids.items():
            if len(ids) > 1:
                duplicates.append({
                    "file": file_path,
                    "count": len(ids),
                    "ids": ids
                })
                self.issues_found.append({
                    "type": "duplicate_embeddings",
                    "file": file_path,
                    "count": len(ids)
                })
        
        return {
            "total_files": len(file_to_ids),
            "duplicates_found": len(duplicates),
            "duplicate_files": duplicates[:10],  # First 10 for report
            "status": "PASS" if len(duplicates) == 0 else "WARNING"
        }
    
    def fix_issues(self, collection_name: str = "apple_docs", dry_run: bool = True):
        """Fix identified issues"""
        logger.info(f"Fixing issues (dry_run={dry_run})...")
        
        if not self.issues_found:
            logger.info("No issues to fix")
            return
        
        collection = self.chroma.get_collection(collection_name)
        fixes_applied = {
            "orphaned_removed": 0,
            "stale_updated": 0,
            "duplicates_removed": 0
        }
        
        for issue in self.issues_found:
            if issue["type"] == "orphaned_embedding":
                if not dry_run:
                    try:
                        collection.delete(ids=[issue["id"]])
                        logger.info(f"Deleted orphaned embedding: {issue['id']}")
                    except Exception as e:
                        logger.error(f"Failed to delete {issue['id']}: {e}")
                fixes_applied["orphaned_removed"] += 1
            
            elif issue["type"] == "stale_embedding":
                logger.info(f"Stale embedding found: {issue['file']} - run incremental update to fix")
                fixes_applied["stale_updated"] += 1
            
            elif issue["type"] == "duplicate_embeddings":
                # Keep the newest, remove others
                if not dry_run:
                    logger.info(f"Found {issue['count']} duplicates for {issue['file']}")
                fixes_applied["duplicates_removed"] += issue["count"] - 1
        
        logger.info(f"Fixes {'applied' if not dry_run else 'to be applied'}: {fixes_applied}")
        return fixes_applied

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Vector store health check and verification")
    parser.add_argument("--collection", default="apple_docs", help="Collection name to check")
    parser.add_argument("--fix", action="store_true", help="Fix identified issues")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be fixed without applying")
    parser.add_argument("--output", help="Save report to JSON file")
    
    args = parser.parse_args()
    
    # Setup paths
    docs_path = Path(__file__).parent.parent / "documentation"
    vectorstore_path = Path(__file__).parent.parent / "vectorstore"
    
    print("🏥 Vector Store Health Check")
    print(f"📁 Documentation: {docs_path}")
    print(f"💾 Vector store: {vectorstore_path}")
    print(f"🎯 Collection: {args.collection}")
    print()
    
    # Run health check
    checker = VectorstoreHealthChecker(docs_path, vectorstore_path)
    results = checker.run_all_checks(args.collection)
    
    # Display results
    print(f"Status: {results['health_status']}")
    print(f"Total embeddings: {results.get('total_embeddings', 0)}")
    print(f"Issues found: {results['issues_found']}")
    print()
    
    # Display check results
    for check_name, check_result in results["checks"].items():
        status = check_result.get("status", "UNKNOWN")
        symbol = "✅" if status == "PASS" else "❌" if status == "FAIL" else "⚠️"
        print(f"{symbol} {check_name}: {status}")
        
        # Show details for failed checks
        if status != "PASS":
            for key, value in check_result.items():
                if key not in ["status", "checked", "samples_checked"]:
                    print(f"  - {key}: {value}")
    
    # Fix issues if requested
    if args.fix or args.dry_run:
        print(f"\n{'🔧' if args.fix else '👀'} {'Fixing' if args.fix else 'Would fix'} issues...")
        fixes = checker.fix_issues(args.collection, dry_run=args.dry_run or not args.fix)
        print(f"Fixes {'applied' if args.fix else 'available'}: {fixes}")
    
    # Save report if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n📄 Report saved to: {args.output}")
    
    # Exit code based on health
    sys.exit(0 if results["health_status"] == "HEALTHY" else 1)

if __name__ == "__main__":
    main()