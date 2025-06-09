#!/usr/bin/env python3
"""
Production monitoring system for Apple docs vectorstore.
Health checks, alerts, and operational metrics.
"""

import os
import json
import time
import psutil
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional
import chromadb
import logging
from dataclasses import dataclass, asdict

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class HealthMetric:
    """Health check metric with status and details."""
    name: str
    status: str  # "healthy", "warning", "critical"
    value: Any
    threshold: Optional[Any] = None
    message: str = ""
    timestamp: str = ""
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now(timezone.utc).isoformat()

class ProductionMonitor:
    """Comprehensive production monitoring for the Apple docs system."""
    
    def __init__(self, vectorstore_path: str = "vectorstore", alerts_enabled: bool = True):
        self.vectorstore_path = Path(vectorstore_path)
        self.hashes_path = Path(".hashes")
        self.alerts_enabled = alerts_enabled
        self.metrics_history = []
        
        # Health check thresholds
        self.thresholds = {
            "disk_usage_percent": 85,
            "memory_usage_percent": 90,
            "vectorstore_size_mb": 5000,  # 5GB max
            "embedding_files_count": 300000,
            "hash_files_age_hours": 168,  # 7 days
            "collection_count_min": 1,
            "collection_count_max": 50
        }
    
    def run_health_check(self) -> Dict[str, HealthMetric]:
        """Run comprehensive health check and return metrics."""
        
        logger.info("🔍 Running production health check...")
        
        metrics = {}
        
        # System resource checks
        metrics.update(self._check_system_resources())
        
        # ChromaDB health checks
        metrics.update(self._check_chromadb_health())
        
        # Data integrity checks
        metrics.update(self._check_data_integrity())
        
        # File system checks
        metrics.update(self._check_file_system())
        
        # Performance checks
        metrics.update(self._check_performance())
        
        # Store metrics for trend analysis
        self.metrics_history.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "metrics": {name: asdict(metric) for name, metric in metrics.items()}
        })
        
        # Keep only last 100 checks
        if len(self.metrics_history) > 100:
            self.metrics_history = self.metrics_history[-100:]
        
        # Check for alerts
        if self.alerts_enabled:
            self._process_alerts(metrics)
        
        return metrics
    
    def _check_system_resources(self) -> Dict[str, HealthMetric]:
        """Check system resource usage."""
        
        metrics = {}
        
        # Disk usage
        disk_usage = psutil.disk_usage('.')
        disk_percent = (disk_usage.used / disk_usage.total) * 100
        
        disk_status = "healthy"
        if disk_percent > self.thresholds["disk_usage_percent"]:
            disk_status = "critical"
        elif disk_percent > self.thresholds["disk_usage_percent"] - 10:
            disk_status = "warning"
        
        metrics["disk_usage"] = HealthMetric(
            name="Disk Usage",
            status=disk_status,
            value=f"{disk_percent:.1f}%",
            threshold=f"{self.thresholds['disk_usage_percent']}%",
            message=f"Used: {disk_usage.used / (1024**3):.1f}GB / {disk_usage.total / (1024**3):.1f}GB"
        )
        
        # Memory usage
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        
        memory_status = "healthy"
        if memory_percent > self.thresholds["memory_usage_percent"]:
            memory_status = "critical"
        elif memory_percent > self.thresholds["memory_usage_percent"] - 10:
            memory_status = "warning"
        
        metrics["memory_usage"] = HealthMetric(
            name="Memory Usage",
            status=memory_status,
            value=f"{memory_percent:.1f}%",
            threshold=f"{self.thresholds['memory_usage_percent']}%",
            message=f"Used: {memory.used / (1024**3):.1f}GB / {memory.total / (1024**3):.1f}GB"
        )
        
        return metrics
    
    def _check_chromadb_health(self) -> Dict[str, HealthMetric]:
        """Check ChromaDB vectorstore health."""
        
        metrics = {}
        
        try:
            # Check if vectorstore exists
            if not self.vectorstore_path.exists():
                metrics["chromadb_existence"] = HealthMetric(
                    name="ChromaDB Existence",
                    status="critical",
                    value="missing",
                    message="Vectorstore directory not found"
                )
                return metrics
            
            # Check vectorstore size
            vectorstore_size = self._get_directory_size(self.vectorstore_path)
            vectorstore_size_mb = vectorstore_size / (1024 * 1024)
            
            size_status = "healthy"
            if vectorstore_size_mb > self.thresholds["vectorstore_size_mb"]:
                size_status = "warning"
            elif vectorstore_size_mb < 1:  # Less than 1MB is suspicious
                size_status = "critical"
            
            metrics["vectorstore_size"] = HealthMetric(
                name="Vectorstore Size",
                status=size_status,
                value=f"{vectorstore_size_mb:.1f}MB",
                threshold=f"{self.thresholds['vectorstore_size_mb']}MB",
                message=f"Total size: {vectorstore_size_mb:.1f}MB"
            )
            
            # Check ChromaDB connectivity
            try:
                client = chromadb.PersistentClient(path=str(self.vectorstore_path))
                collections = client.list_collections()
                
                collection_count = len(collections)
                
                count_status = "healthy"
                if collection_count < self.thresholds["collection_count_min"]:
                    count_status = "warning"
                elif collection_count > self.thresholds["collection_count_max"]:
                    count_status = "warning"
                
                metrics["collection_count"] = HealthMetric(
                    name="Collection Count",
                    status=count_status,
                    value=collection_count,
                    threshold=f"{self.thresholds['collection_count_min']}-{self.thresholds['collection_count_max']}",
                    message=f"Collections: {[c.name for c in collections]}"
                )
                
                # Check individual collection health
                total_documents = 0
                for collection in collections:
                    try:
                        doc_count = collection.count()
                        total_documents += doc_count
                        
                        if doc_count == 0:
                            metrics[f"collection_{collection.name}"] = HealthMetric(
                                name=f"Collection {collection.name}",
                                status="warning",
                                value=doc_count,
                                message="Empty collection"
                            )
                        
                    except Exception as e:
                        metrics[f"collection_{collection.name}"] = HealthMetric(
                            name=f"Collection {collection.name}",
                            status="critical",
                            value="error",
                            message=f"Collection access failed: {e}"
                        )
                
                metrics["total_documents"] = HealthMetric(
                    name="Total Documents",
                    status="healthy",
                    value=total_documents,
                    message=f"Total embedded documents across all collections"
                )
                
            except Exception as e:
                metrics["chromadb_connectivity"] = HealthMetric(
                    name="ChromaDB Connectivity",
                    status="critical",
                    value="failed",
                    message=f"Cannot connect to ChromaDB: {e}"
                )
        
        except Exception as e:
            metrics["chromadb_health"] = HealthMetric(
                name="ChromaDB Health",
                status="critical",
                value="error",
                message=f"Health check failed: {e}"
            )
        
        return metrics
    
    def _check_data_integrity(self) -> Dict[str, HealthMetric]:
        """Check data integrity and consistency."""
        
        metrics = {}
        
        # Check hash files
        if self.hashes_path.exists():
            hash_files = list(self.hashes_path.glob("*.json"))
            
            metrics["hash_files_count"] = HealthMetric(
                name="Hash Files Count",
                status="healthy",
                value=len(hash_files),
                message=f"Hash files: {[f.name for f in hash_files[:5]]}" + (f" and {len(hash_files)-5} more" if len(hash_files) > 5 else "")
            )
            
            # Check hash file freshness
            if hash_files:
                newest_hash_file = max(hash_files, key=lambda f: f.stat().st_mtime)
                age_hours = (time.time() - newest_hash_file.stat().st_mtime) / 3600
                
                age_status = "healthy"
                if age_hours > self.thresholds["hash_files_age_hours"]:
                    age_status = "warning"
                
                metrics["hash_files_age"] = HealthMetric(
                    name="Hash Files Age",
                    status=age_status,
                    value=f"{age_hours:.1f} hours",
                    threshold=f"{self.thresholds['hash_files_age_hours']} hours",
                    message=f"Newest: {newest_hash_file.name}"
                )
        else:
            metrics["hash_files_existence"] = HealthMetric(
                name="Hash Files Existence",
                status="warning",
                value="missing",
                message="Hash files directory not found"
            )
        
        return metrics
    
    def _check_file_system(self) -> Dict[str, HealthMetric]:
        """Check file system health."""
        
        metrics = {}
        
        # Check documentation directory
        docs_path = Path("documentation")
        if docs_path.exists():
            doc_files = list(docs_path.rglob("*.md"))
            
            docs_status = "healthy"
            if len(doc_files) < 1000:  # Expect significant number of docs
                docs_status = "warning"
            
            metrics["documentation_files"] = HealthMetric(
                name="Documentation Files",
                status=docs_status,
                value=len(doc_files),
                threshold="1000+",
                message=f"Total .md files in documentation directory"
            )
        else:
            metrics["documentation_existence"] = HealthMetric(
                name="Documentation Existence",
                status="critical",
                value="missing",
                message="Documentation directory not found"
            )
        
        return metrics
    
    def _check_performance(self) -> Dict[str, HealthMetric]:
        """Check system performance metrics."""
        
        metrics = {}
        
        # Check ChromaDB query performance
        if self.vectorstore_path.exists():
            try:
                start_time = time.time()
                
                client = chromadb.PersistentClient(path=str(self.vectorstore_path))
                collections = client.list_collections()
                
                if collections:
                    # Test query performance on first collection
                    test_collection = collections[0]
                    sample_docs = test_collection.get(limit=1, include=["documents"])
                    
                    query_time = (time.time() - start_time) * 1000  # Convert to ms
                    
                    perf_status = "healthy"
                    if query_time > 5000:  # 5 seconds
                        perf_status = "critical"
                    elif query_time > 1000:  # 1 second
                        perf_status = "warning"
                    
                    metrics["query_performance"] = HealthMetric(
                        name="Query Performance",
                        status=perf_status,
                        value=f"{query_time:.0f}ms",
                        threshold="1000ms",
                        message=f"Collection access and sample query time"
                    )
                
            except Exception as e:
                metrics["performance_test"] = HealthMetric(
                    name="Performance Test",
                    status="warning",
                    value="failed",
                    message=f"Performance test failed: {e}"
                )
        
        return metrics
    
    def _get_directory_size(self, path: Path) -> int:
        """Calculate total size of directory in bytes."""
        
        total_size = 0
        for file_path in path.rglob("*"):
            if file_path.is_file():
                total_size += file_path.stat().st_size
        return total_size
    
    def _process_alerts(self, metrics: Dict[str, HealthMetric]):
        """Process alerts for critical issues."""
        
        critical_issues = [m for m in metrics.values() if m.status == "critical"]
        warning_issues = [m for m in metrics.values() if m.status == "warning"]
        
        if critical_issues:
            logger.error(f"🚨 CRITICAL ALERTS ({len(critical_issues)}):")
            for issue in critical_issues:
                logger.error(f"   ❌ {issue.name}: {issue.message}")
        
        if warning_issues:
            logger.warning(f"⚠️  WARNINGS ({len(warning_issues)}):")
            for issue in warning_issues:
                logger.warning(f"   ⚠️  {issue.name}: {issue.message}")
        
        if not critical_issues and not warning_issues:
            logger.info("✅ All health checks passed!")
    
    def generate_report(self, metrics: Dict[str, HealthMetric]) -> str:
        """Generate formatted health report."""
        
        report = []
        report.append("🏥 APPLE DOCS SYSTEM HEALTH REPORT")
        report.append("=" * 50)
        report.append(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
        report.append("")
        
        # Summary
        healthy_count = sum(1 for m in metrics.values() if m.status == "healthy")
        warning_count = sum(1 for m in metrics.values() if m.status == "warning")
        critical_count = sum(1 for m in metrics.values() if m.status == "critical")
        
        report.append(f"📊 SUMMARY:")
        report.append(f"   ✅ Healthy: {healthy_count}")
        report.append(f"   ⚠️  Warnings: {warning_count}")
        report.append(f"   ❌ Critical: {critical_count}")
        report.append("")
        
        # Detailed metrics
        report.append("📋 DETAILED METRICS:")
        report.append("")
        
        categories = {
            "System Resources": ["disk_usage", "memory_usage"],
            "ChromaDB Health": ["chromadb_existence", "vectorstore_size", "collection_count", "total_documents", "chromadb_connectivity"],
            "Data Integrity": ["hash_files_count", "hash_files_age", "hash_files_existence"],
            "File System": ["documentation_files", "documentation_existence"],
            "Performance": ["query_performance", "performance_test"]
        }
        
        for category, metric_keys in categories.items():
            report.append(f"🔍 {category}:")
            
            for key in metric_keys:
                if key in metrics:
                    metric = metrics[key]
                    status_icon = {"healthy": "✅", "warning": "⚠️", "critical": "❌"}.get(metric.status, "❓")
                    report.append(f"   {status_icon} {metric.name}: {metric.value}")
                    if metric.message:
                        report.append(f"      {metric.message}")
            
            report.append("")
        
        return "\n".join(report)
    
    def save_metrics(self, output_path: str = "health_metrics.json"):
        """Save metrics history to file."""
        
        with open(output_path, "w") as f:
            json.dump(self.metrics_history, f, indent=2)
        
        logger.info(f"📊 Metrics saved to {output_path}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Apple Docs Production Monitor")
    parser.add_argument("--vectorstore", type=str, default="vectorstore", help="Vectorstore path")
    parser.add_argument("--output", type=str, help="Save report to file")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--continuous", type=int, help="Run continuously with interval in seconds")
    parser.add_argument("--no-alerts", action="store_true", help="Disable alert processing")
    
    args = parser.parse_args()
    
    monitor = ProductionMonitor(
        vectorstore_path=args.vectorstore,
        alerts_enabled=not args.no_alerts
    )
    
    def run_check():
        metrics = monitor.run_health_check()
        
        if args.json:
            output = json.dumps({name: asdict(metric) for name, metric in metrics.items()}, indent=2)
        else:
            output = monitor.generate_report(metrics)
        
        if args.output:
            with open(args.output, "w") as f:
                f.write(output)
            logger.info(f"Report saved to {args.output}")
        else:
            print(output)
        
        return metrics
    
    if args.continuous:
        logger.info(f"Running continuous monitoring every {args.continuous} seconds...")
        try:
            while True:
                run_check()
                time.sleep(args.continuous)
        except KeyboardInterrupt:
            logger.info("Monitoring stopped")
    else:
        run_check()

if __name__ == "__main__":
    main()