#!/usr/bin/env python3
"""
Self-test script for Apple Docs MCP Server
Runs comprehensive tests to ensure the container is working properly
"""

import sys
import os
import time
import asyncio
import logging
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from server.logger import get_logger
from server.rag import SimpleRAG

logger = get_logger(__name__)


class SelfTester:
    """Comprehensive self-testing for the MCP server"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.results = []
    
    def test(self, name: str, condition: bool, error_msg: str = None):
        """Record a test result"""
        if condition:
            self.passed += 1
            self.results.append(f"✅ {name}")
            logger.info(f"✅ {name}")
        else:
            self.failed += 1
            msg = f"❌ {name}"
            if error_msg:
                msg += f": {error_msg}"
            self.results.append(msg)
            logger.error(msg)
    
    async def run_all_tests(self):
        """Run all self-tests"""
        logger.info("🧪 Starting MCP Server Self-Tests")
        logger.info("=" * 60)
        
        # Test 1: Environment Variables
        logger.info("\n📋 Testing Environment Variables...")
        self.test(
            "OPENAI_API_KEY set",
            bool(os.getenv("OPENAI_API_KEY")),
            "Required for embeddings"
        )
        self.test(
            "MCP_API_KEY set",
            bool(os.getenv("MCP_API_KEY")),
            "Required for authentication"
        )
        
        # Test 2: Directory Structure
        logger.info("\n📁 Testing Directory Structure...")
        dirs_to_check = [
            "/data/vectorstore",
            "/data/hashes",
            "/data/documentation",
            "/data/logs",
            "/app/server",
            "/app/scripts"
        ]
        for dir_path in dirs_to_check:
            self.test(
                f"Directory exists: {dir_path}",
                Path(dir_path).exists()
            )
        
        # Test 3: File Permissions
        logger.info("\n🔐 Testing File Permissions...")
        writable_dirs = ["/data/vectorstore", "/data/hashes", "/data/logs"]
        for dir_path in writable_dirs:
            try:
                test_file = Path(dir_path) / ".write_test"
                test_file.write_text("test")
                test_file.unlink()
                writable = True
            except:
                writable = False
            
            self.test(
                f"Directory writable: {dir_path}",
                writable
            )
        
        # Test 4: ChromaDB Connection
        logger.info("\n🗄️ Testing ChromaDB Connection...")
        try:
            rag = SimpleRAG()
            stats = rag.get_stats()
            self.test(
                "ChromaDB connection successful",
                True
            )
            self.test(
                f"Documents loaded: {stats['total_documents']:,}",
                stats['total_documents'] > 0
            )
        except Exception as e:
            self.test(
                "ChromaDB connection successful",
                False,
                str(e)
            )
        
        # Test 5: API Health Check
        logger.info("\n🌐 Testing API Health Check...")
        try:
            import httpx
            async with httpx.AsyncClient() as client:
                response = await client.get("http://localhost:8080/health")
                self.test(
                    "Health endpoint accessible",
                    response.status_code == 200
                )
                
                health_data = response.json()
                self.test(
                    "Health check returns valid data",
                    health_data.get("status") == "healthy"
                )
        except Exception as e:
            self.test(
                "Health endpoint accessible",
                False,
                str(e)
            )
        
        # Test 6: Search Functionality
        logger.info("\n🔍 Testing Search Functionality...")
        if hasattr(self, 'rag'):
            try:
                rag = SimpleRAG()
                results = await rag.search("SwiftUI Button", limit=1)
                self.test(
                    "Search returns results",
                    len(results) > 0
                )
                
                if results:
                    result = results[0]
                    self.test(
                        "Search result has content",
                        bool(result.get('content'))
                    )
                    self.test(
                        "Search result has metadata",
                        bool(result.get('metadata'))
                    )
            except Exception as e:
                self.test(
                    "Search functionality",
                    False,
                    str(e)
                )
        
        # Test 7: Scraper Availability
        logger.info("\n📥 Testing Scraper Availability...")
        scraper_path = Path("/app/scraper/auto_scrape_and_embed.py")
        self.test(
            "Auto-scraper script exists",
            scraper_path.exists()
        )
        
        if scraper_path.exists():
            self.test(
                "Auto-scraper script executable",
                os.access(str(scraper_path), os.X_OK)
            )
        
        # Test 8: Supervisor Status
        logger.info("\n🎯 Testing Supervisor Status...")
        try:
            import subprocess
            result = subprocess.run(
                ["supervisorctl", "status"],
                capture_output=True,
                text=True
            )
            self.test(
                "Supervisor running",
                result.returncode == 0
            )
            
            if result.returncode == 0:
                output = result.stdout
                self.test(
                    "MCP server process running",
                    "mcp-server" in output and "RUNNING" in output
                )
                self.test(
                    "Scheduler process running",
                    "scheduler" in output and "RUNNING" in output
                )
        except Exception as e:
            self.test(
                "Supervisor running",
                False,
                str(e)
            )
        
        # Test 9: Scheduler Logic
        logger.info("\n⏰ Testing Scheduler Logic...")
        try:
            from scripts.schedule_rescrape import get_next_sunday_1am
            next_run = get_next_sunday_1am()
            self.test(
                "Scheduler calculates next run time",
                isinstance(next_run, datetime)
            )
            logger.info(f"   Next scheduled run: {next_run}")
        except Exception as e:
            self.test(
                "Scheduler logic",
                False,
                str(e)
            )
        
        # Test 10: Memory and Disk Usage
        logger.info("\n💾 Testing Resource Usage...")
        try:
            import shutil
            
            # Check disk space
            total, used, free = shutil.disk_usage("/data")
            free_gb = free / (1024**3)
            self.test(
                f"Sufficient disk space ({free_gb:.1f}GB free)",
                free_gb > 1.0  # At least 1GB free
            )
            
            # Check memory
            with open('/proc/meminfo', 'r') as f:
                meminfo = f.read()
                mem_available = None
                for line in meminfo.split('\n'):
                    if 'MemAvailable' in line:
                        mem_available = int(line.split()[1]) / 1024  # MB
                        break
                
                if mem_available:
                    self.test(
                        f"Sufficient memory ({mem_available:.0f}MB available)",
                        mem_available > 256  # At least 256MB
                    )
        except Exception as e:
            logger.warning(f"Could not check resources: {e}")
        
        # Summary
        logger.info("\n" + "=" * 60)
        logger.info("🏁 Self-Test Summary")
        logger.info("=" * 60)
        logger.info(f"✅ Passed: {self.passed}")
        logger.info(f"❌ Failed: {self.failed}")
        logger.info(f"📊 Total: {self.passed + self.failed}")
        
        if self.failed == 0:
            logger.info("\n🎉 All tests passed! The container is healthy.")
            return 0
        else:
            logger.error(f"\n⚠️  {self.failed} tests failed. Please check the logs.")
            return 1


async def main():
    """Run self-tests"""
    tester = SelfTester()
    return await tester.run_all_tests()


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)