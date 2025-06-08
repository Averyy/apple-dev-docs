#!/usr/bin/env python3
"""
Monitor performance metrics during vector index building.
Run this in a separate terminal while build_index.py is running.
"""
import json
import os
import psutil
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from server.config import VECTORSTORE_PATH
from server.logger import get_logger

logger = get_logger(__name__)


class IndexingMonitor:
    """Monitor system resources and indexing progress"""
    
    def __init__(self, interval: int = 10):
        self.interval = interval
        self.metrics: List[Dict] = []
        self.start_time = time.time()
        self.hash_file = VECTORSTORE_PATH / "file_hashes.json"
        self.metrics_file = VECTORSTORE_PATH / "indexing_metrics.json"
        
    def get_process_stats(self) -> Dict:
        """Get current process statistics"""
        process = psutil.Process()
        
        # Find python processes running build_index.py
        build_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'] and 'python' in proc.info['name'].lower():
                    cmdline = proc.info.get('cmdline', [])
                    if any('build_index.py' in arg for arg in cmdline):
                        build_processes.append(proc)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        # Aggregate stats from all build processes
        total_memory = 0
        total_cpu = 0
        for proc in build_processes:
            try:
                total_memory += proc.memory_info().rss / 1024 / 1024  # MB
                total_cpu += proc.cpu_percent(interval=0.1)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        return {
            "memory_mb": total_memory,
            "cpu_percent": total_cpu,
            "num_processes": len(build_processes)
        }
    
    def get_indexing_progress(self) -> Dict:
        """Get current indexing progress from hash file"""
        if not self.hash_file.exists():
            return {"indexed_files": 0, "hash_count": 0}
        
        try:
            with open(self.hash_file, 'r') as f:
                hashes = json.load(f)
                return {
                    "indexed_files": len(hashes),
                    "hash_count": len(hashes)
                }
        except Exception:
            return {"indexed_files": 0, "hash_count": 0}
    
    def get_vectorstore_size(self) -> float:
        """Get size of vectorstore directory in MB"""
        total_size = 0
        if VECTORSTORE_PATH.exists():
            for path in VECTORSTORE_PATH.rglob('*'):
                if path.is_file():
                    total_size += path.stat().st_size
        return total_size / 1024 / 1024  # MB
    
    def collect_metrics(self) -> Dict:
        """Collect all metrics"""
        elapsed = time.time() - self.start_time
        process_stats = self.get_process_stats()
        progress = self.get_indexing_progress()
        
        metrics = {
            "timestamp": datetime.now().isoformat(),
            "elapsed_seconds": elapsed,
            "elapsed_readable": f"{int(elapsed//3600)}h {int((elapsed%3600)//60)}m {int(elapsed%60)}s",
            **process_stats,
            **progress,
            "vectorstore_size_mb": self.get_vectorstore_size(),
            "docs_per_second": progress["indexed_files"] / elapsed if elapsed > 0 else 0
        }
        
        # Estimate time remaining
        if metrics["docs_per_second"] > 0:
            # Assuming ~278K total documents
            estimated_total = 278778
            remaining = estimated_total - progress["indexed_files"]
            eta_seconds = remaining / metrics["docs_per_second"]
            metrics["eta_readable"] = f"{int(eta_seconds//3600)}h {int((eta_seconds%3600)//60)}m"
            metrics["estimated_total_time"] = f"{int((elapsed + eta_seconds)//3600)}h {int(((elapsed + eta_seconds)%3600)//60)}m"
        
        return metrics
    
    def save_metrics(self):
        """Save metrics to file"""
        try:
            with open(self.metrics_file, 'w') as f:
                json.dump(self.metrics, f, indent=2)
        except Exception as e:
            logger.warning(f"Failed to save metrics: {e}")
    
    def display_metrics(self, metrics: Dict):
        """Display metrics in a nice format"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("=" * 60)
        print("Vector Index Building Monitor")
        print("=" * 60)
        print(f"Elapsed Time: {metrics['elapsed_readable']}")
        print(f"Documents Indexed: {metrics['indexed_files']:,}")
        print(f"Speed: {metrics['docs_per_second']:.1f} docs/sec")
        
        if 'eta_readable' in metrics:
            print(f"ETA: {metrics['eta_readable']} (Total: {metrics['estimated_total_time']})")
        
        print("\nResource Usage:")
        print(f"  Memory: {metrics['memory_mb']:.1f} MB")
        print(f"  CPU: {metrics['cpu_percent']:.1f}%")
        print(f"  Processes: {metrics['num_processes']}")
        print(f"  Vectorstore Size: {metrics['vectorstore_size_mb']:.1f} MB")
        
        # Performance warnings
        if metrics['memory_mb'] > 2000:
            print("\n⚠️  High memory usage detected!")
        if metrics['cpu_percent'] < 10 and metrics['num_processes'] > 0:
            print("\n⚠️  Low CPU usage - might be I/O bound")
        if metrics['docs_per_second'] < 10 and metrics['indexed_files'] > 100:
            print("\n⚠️  Slow indexing speed detected")
    
    def run(self):
        """Run the monitoring loop"""
        logger.info("Starting indexing monitor...")
        print("Monitoring vector index building. Press Ctrl+C to stop.")
        
        try:
            while True:
                metrics = self.collect_metrics()
                self.metrics.append(metrics)
                self.display_metrics(metrics)
                self.save_metrics()
                
                # Check if indexing might be complete
                if len(self.metrics) > 2:
                    if (self.metrics[-1]['indexed_files'] == self.metrics[-2]['indexed_files'] and 
                        metrics['num_processes'] == 0):
                        print("\n✅ Indexing appears to be complete!")
                        break
                
                time.sleep(self.interval)
                
        except KeyboardInterrupt:
            print("\n\nMonitoring stopped.")
            self.generate_summary()
    
    def generate_summary(self):
        """Generate a summary of the indexing run"""
        if not self.metrics:
            return
        
        print("\n" + "=" * 60)
        print("Indexing Summary")
        print("=" * 60)
        
        final = self.metrics[-1]
        peak_memory = max(m['memory_mb'] for m in self.metrics)
        avg_speed = sum(m['docs_per_second'] for m in self.metrics) / len(self.metrics)
        
        print(f"Total Time: {final['elapsed_readable']}")
        print(f"Documents Indexed: {final['indexed_files']:,}")
        print(f"Average Speed: {avg_speed:.1f} docs/sec")
        print(f"Peak Memory: {peak_memory:.1f} MB")
        print(f"Final Vectorstore Size: {final['vectorstore_size_mb']:.1f} MB")
        
        # Save summary
        summary = {
            "total_time": final['elapsed_readable'],
            "total_seconds": final['elapsed_seconds'],
            "documents_indexed": final['indexed_files'],
            "average_speed": avg_speed,
            "peak_memory_mb": peak_memory,
            "final_size_mb": final['vectorstore_size_mb'],
            "metrics_count": len(self.metrics)
        }
        
        summary_file = VECTORSTORE_PATH / "indexing_summary.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"\nSummary saved to: {summary_file}")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Monitor vector index building")
    parser.add_argument("--interval", type=int, default=10, 
                       help="Update interval in seconds (default: 10)")
    args = parser.parse_args()
    
    monitor = IndexingMonitor(interval=args.interval)
    monitor.run()


if __name__ == "__main__":
    main()