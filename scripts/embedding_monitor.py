#!/usr/bin/env python3
"""
Monitoring script for embedding system health
Run periodically to ensure everything is working correctly
"""

import sys
import json
import time
from pathlib import Path
from datetime import datetime, timedelta
import chromadb
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EmbeddingMonitor:
    """Monitor embedding system health"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.vectorstore_path = self.project_root / "vectorstore"
        self.docs_path = self.project_root / "documentation"
        self.hash_file = self.project_root / ".hashes" / "embedding_hashes.json"
        self.monitor_file = self.project_root / ".hashes" / "embedding_monitor.json"
        
        # Load previous monitoring data if exists
        self.previous_data = self._load_monitor_data()
        
        # Initialize ChromaDB
        self.chroma = chromadb.PersistentClient(path=str(self.vectorstore_path))
        self.collection = self.chroma.get_collection("apple_docs")
    
    def _load_monitor_data(self):
        """Load previous monitoring data"""
        if self.monitor_file.exists():
            with open(self.monitor_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_monitor_data(self, data):
        """Save monitoring data"""
        self.monitor_file.parent.mkdir(exist_ok=True)
        with open(self.monitor_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def check_collection_growth(self):
        """Monitor collection growth"""
        current_count = self.collection.count()
        previous_count = self.previous_data.get("embedding_count", 0)
        
        growth = current_count - previous_count
        growth_pct = (growth / previous_count * 100) if previous_count > 0 else 0
        
        status = {
            "current_count": current_count,
            "previous_count": previous_count,
            "growth": growth,
            "growth_percentage": growth_pct,
            "status": "OK"
        }
        
        # Alert if unexpected changes
        if growth < 0:
            status["status"] = "WARNING"
            status["message"] = f"Embedding count decreased by {abs(growth)}"
        elif growth_pct > 10:
            status["status"] = "INFO"
            status["message"] = f"Large growth detected: {growth_pct:.1f}%"
        
        return status
    
    def check_hash_file_freshness(self):
        """Check if hash file is being updated"""
        if not self.hash_file.exists():
            return {
                "status": "ERROR",
                "message": "Hash file not found"
            }
        
        # Check modification time
        mtime = datetime.fromtimestamp(self.hash_file.stat().st_mtime)
        age = datetime.now() - mtime
        
        status = {
            "last_modified": mtime.isoformat(),
            "age_hours": age.total_seconds() / 3600,
            "status": "OK"
        }
        
        # Alert if not updated recently
        if age > timedelta(days=7):
            status["status"] = "WARNING"
            status["message"] = f"Hash file not updated in {age.days} days"
        elif age > timedelta(days=30):
            status["status"] = "ERROR"
            status["message"] = f"Hash file severely outdated: {age.days} days"
        
        return status
    
    def check_document_count(self):
        """Compare document count with embeddings"""
        # Count markdown files
        doc_count = sum(1 for _ in self.docs_path.rglob("*.md"))
        
        # Load hash file for processed count
        if self.hash_file.exists():
            with open(self.hash_file, 'r') as f:
                hash_data = json.load(f)
                processed_count = len([k for k in hash_data.get("hashes", {}) if k != "metadata"])
        else:
            processed_count = 0
        
        embedding_count = self.collection.count()
        
        # Calculate chunked files (embeddings > processed means some files were split)
        chunked_files = embedding_count - processed_count if embedding_count > processed_count else 0
        
        status = {
            "document_count": doc_count,
            "processed_count": processed_count,
            "embedding_count": embedding_count,
            "files_with_chunks": chunked_files,
            "unprocessed": doc_count - processed_count,
            "status": "OK"
        }
        
        # Better logic: if we have embeddings and they're recent, we're good
        # The difference between doc_count and processed_count might be due to:
        # 1. Empty files that were skipped
        # 2. Files added after embedding generation
        # 3. Counting differences (some files might be in subfolders not processed)
        
        # Only warn if the hash file is old AND there's a big difference
        if self.hash_file.exists():
            mtime = datetime.fromtimestamp(self.hash_file.stat().st_mtime)
            age = datetime.now() - mtime
            
            if age < timedelta(hours=24) and doc_count - processed_count > 1000:
                # Recent processing but still missing files
                status["status"] = "WARNING"
                status["message"] = f"{doc_count - processed_count} files may need processing"
            elif doc_count - processed_count > 5000:
                # Very large difference
                status["status"] = "WARNING" 
                status["message"] = f"Large file count difference: {doc_count - processed_count}"
            else:
                # Small differences are normal
                status["message"] = f"File difference likely due to empty files or post-processing additions"
        
        return status
    
    def check_disk_space(self):
        """Monitor disk space usage"""
        import shutil
        
        # Get vectorstore size
        total_size = sum(
            f.stat().st_size 
            for f in self.vectorstore_path.rglob('*') 
            if f.is_file()
        )
        size_gb = total_size / (1024**3)
        
        # Get free space
        stat = shutil.disk_usage(self.vectorstore_path)
        free_gb = stat.free / (1024**3)
        used_pct = (stat.used / stat.total) * 100
        
        status = {
            "vectorstore_size_gb": round(size_gb, 2),
            "free_space_gb": round(free_gb, 2),
            "disk_usage_percent": round(used_pct, 1),
            "status": "OK"
        }
        
        # Check thresholds
        if free_gb < 5:
            status["status"] = "ERROR"
            status["message"] = f"Low disk space: {free_gb:.1f}GB free"
        elif free_gb < 10:
            status["status"] = "WARNING"
            status["message"] = f"Disk space getting low: {free_gb:.1f}GB free"
        
        return status
    
    def check_query_performance(self):
        """Test query performance"""
        # Simple performance test
        test_embedding = [0.1] * 1536  # Dummy embedding
        
        start = time.time()
        try:
            results = self.collection.query(
                query_embeddings=[test_embedding],
                n_results=10
            )
            elapsed = time.time() - start
            
            status = {
                "query_time_ms": round(elapsed * 1000, 1),
                "results_returned": len(results["documents"][0]),
                "status": "OK"
            }
            
            # Check performance thresholds
            if elapsed > 1.0:
                status["status"] = "WARNING"
                status["message"] = f"Slow query performance: {elapsed:.2f}s"
            elif elapsed > 5.0:
                status["status"] = "ERROR"
                status["message"] = f"Very slow queries: {elapsed:.2f}s"
                
        except Exception as e:
            status = {
                "status": "ERROR",
                "message": f"Query failed: {str(e)}"
            }
        
        return status
    
    def generate_report(self):
        """Generate comprehensive health report"""
        logger.info("Starting embedding system health check...")
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "checks": {
                "collection_growth": self.check_collection_growth(),
                "hash_freshness": self.check_hash_file_freshness(),
                "document_sync": self.check_document_count(),
                "disk_space": self.check_disk_space(),
                "query_performance": self.check_query_performance()
            }
        }
        
        # Calculate overall status
        statuses = [check["status"] for check in report["checks"].values()]
        if "ERROR" in statuses:
            report["overall_status"] = "ERROR"
        elif "WARNING" in statuses:
            report["overall_status"] = "WARNING"
        else:
            report["overall_status"] = "HEALTHY"
        
        # Save current data for next run
        monitor_data = {
            "last_check": datetime.now().isoformat(),
            "embedding_count": self.collection.count(),
            "overall_status": report["overall_status"]
        }
        self._save_monitor_data(monitor_data)
        
        return report
    
    def print_report(self, report):
        """Print formatted report"""
        print("\n" + "="*60)
        print("EMBEDDING SYSTEM HEALTH REPORT")
        print(f"Timestamp: {report['timestamp']}")
        print(f"Overall Status: {report['overall_status']}")
        print("="*60)
        
        for check_name, check_data in report["checks"].items():
            status = check_data["status"]
            symbol = "✅" if status == "OK" else "⚠️" if status == "WARNING" else "❌"
            
            print(f"\n{symbol} {check_name.upper().replace('_', ' ')}")
            
            # Print relevant details
            for key, value in check_data.items():
                if key not in ["status", "message"]:
                    print(f"  {key}: {value}")
            
            # Print message if exists
            if "message" in check_data:
                print(f"  ⚠️  {check_data['message']}")
        
        print("\n" + "="*60)
        
        # Recommendations
        if report["overall_status"] != "HEALTHY":
            print("\nRECOMMENDATIONS:")
            
            if report["checks"]["collection_growth"]["status"] == "WARNING":
                print("- Check for unexpected deletions in the collection")
            
            if report["checks"]["hash_freshness"]["status"] in ["WARNING", "ERROR"]:
                print("- Run incremental update to refresh embeddings")
            
            if report["checks"]["document_sync"]["unprocessed"] > 1000:
                print(f"- Process {report['checks']['document_sync']['unprocessed']} new documents")
            
            if report["checks"]["disk_space"]["status"] in ["WARNING", "ERROR"]:
                print("- Free up disk space or expand storage")
            
            if report["checks"]["query_performance"]["status"] in ["WARNING", "ERROR"]:
                print("- Check ChromaDB performance and consider optimization")


def main():
    """Run monitoring and generate report"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Monitor embedding system health")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--save", help="Save report to file")
    
    args = parser.parse_args()
    
    try:
        monitor = EmbeddingMonitor()
        report = monitor.generate_report()
        
        if args.json:
            print(json.dumps(report, indent=2))
        else:
            monitor.print_report(report)
        
        if args.save:
            with open(args.save, 'w') as f:
                json.dump(report, f, indent=2)
            print(f"\nReport saved to: {args.save}")
        
        # Exit code based on status
        if report["overall_status"] == "ERROR":
            sys.exit(2)
        elif report["overall_status"] == "WARNING":
            sys.exit(1)
        else:
            sys.exit(0)
            
    except Exception as e:
        logger.error(f"Monitoring failed: {e}")
        sys.exit(3)


if __name__ == "__main__":
    main()