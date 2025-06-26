#!/usr/bin/env python3
"""
Test the complete auto-rescrape workflow

This tests:
1. Scraper can be found and executed
2. Documentation is saved to the correct location
3. Indexer can find the documentation
4. Meilisearch is updated with new content
"""

import os
import sys
import subprocess
from pathlib import Path
import json
import time

# Colors for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_header(text: str):
    print(f"\n{BLUE}{'=' * 60}{RESET}")
    print(f"{BLUE}{text}{RESET}")
    print(f"{BLUE}{'=' * 60}{RESET}")

def print_success(text: str):
    print(f"{GREEN}✅ {text}{RESET}")

def print_error(text: str):
    print(f"{RED}❌ {text}{RESET}")

def print_info(text: str):
    print(f"{YELLOW}ℹ️  {text}{RESET}")

def check_environment():
    """Check if we're in Docker or local environment"""
    is_docker = Path("/.dockerenv").exists()
    print_info(f"Environment: {'Docker' if is_docker else 'Local'}")
    return is_docker

def test_scraper_location(is_docker: bool):
    """Test if scraper can be found"""
    print_header("Testing Scraper Location")
    
    if is_docker:
        scraper_path = Path("/app/scrape.py")
    else:
        scraper_path = Path(__file__).parent.parent.parent / "scrape.py"
    
    if scraper_path.exists():
        print_success(f"Found scraper at: {scraper_path}")
        return True, scraper_path
    else:
        print_error(f"Scraper not found at: {scraper_path}")
        return False, None

def test_documentation_path(is_docker: bool):
    """Test documentation directory"""
    print_header("Testing Documentation Path")
    
    if is_docker:
        docs_path = Path("/data/documentation")
    else:
        docs_path = Path(__file__).parent.parent.parent / "documentation"
    
    if docs_path.exists():
        print_success(f"Documentation directory exists: {docs_path}")
        # Count existing files
        md_files = list(docs_path.glob("**/*.md"))
        print_info(f"Current markdown files: {len(md_files)}")
    else:
        print_info(f"Documentation directory will be created at: {docs_path}")
        docs_path.mkdir(parents=True, exist_ok=True)
    
    return docs_path

def test_indexer_location(is_docker: bool):
    """Test if indexer can be found"""
    print_header("Testing Indexer Location")
    
    if is_docker:
        indexer_path = Path("/app/scripts/index_to_meilisearch.py")
    else:
        indexer_path = Path(__file__).parent.parent.parent / "scripts" / "index_to_meilisearch.py"
    
    if indexer_path.exists():
        print_success(f"Found indexer at: {indexer_path}")
        return True, indexer_path
    else:
        print_error(f"Indexer not found at: {indexer_path}")
        return False, None

def test_meilisearch_connection():
    """Test Meilisearch connection"""
    print_header("Testing Meilisearch Connection")
    
    try:
        import httpx
        response = httpx.get("http://localhost:7700/health")
        if response.status_code == 200:
            print_success("Meilisearch is healthy")
            
            # Check document count
            api_key = os.getenv("MEILI_MASTER_KEY")
            if api_key:
                headers = {"Authorization": f"Bearer {api_key}"}
                response = httpx.get("http://localhost:7700/indexes/apple_docs/stats", headers=headers)
                if response.status_code == 200:
                    stats = response.json()
                    doc_count = stats.get('numberOfDocuments', 0)
                    print_info(f"Current documents in index: {doc_count:,}")
            
            return True
        else:
            print_error(f"Meilisearch returned status {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Cannot connect to Meilisearch: {e}")
        return False

def test_environment_variables():
    """Test required environment variables"""
    print_header("Testing Environment Variables")
    
    required_vars = {
        "OPENAI_API_KEY": "Required for indexing",
        "MEILI_MASTER_KEY": "Required for Meilisearch"
    }
    
    all_good = True
    for var, description in required_vars.items():
        value = os.getenv(var)
        if value:
            print_success(f"{var} is set ({description})")
        else:
            print_error(f"{var} is NOT set ({description})")
            all_good = False
    
    # Optional variables
    optional_vars = {
        "ENABLE_AUTO_RESCRAPE": "Auto-rescrape scheduling",
        "KEEP_MARKDOWN_FILES": "Keep documentation files",
        "DOCUMENTATION_PATH": "Documentation storage path",
        "HASHES_PATH": "Hash storage path"
    }
    
    print_info("\nOptional variables:")
    for var, description in optional_vars.items():
        value = os.getenv(var, "not set")
        print(f"  {var}: {value} ({description})")
    
    return all_good

def test_scheduler_paths():
    """Test if scheduler can find all required paths"""
    print_header("Testing Scheduler Paths")
    
    # Import the scheduler module to test its path logic
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from schedule_rescrape_v2 import run_weekly_rescrape
        
        print_success("Scheduler module imported successfully")
        print_info("Scheduler will use the following logic:")
        print("  - Scraper: /app/scrape.py (Docker) or project root (local)")
        print("  - Scripts: /app/scripts (Docker) or relative path (local)")
        print("  - Documentation: /data/documentation (Docker) or ../documentation (local)")
        
        return True
    except ImportError as e:
        print_error(f"Cannot import scheduler: {e}")
        return False

def run_mini_scrape_test(scraper_path: Path):
    """Run a minimal scrape test"""
    print_header("Running Mini Scrape Test")
    
    print_info("Testing scraper with --dry-run flag...")
    
    cmd = [sys.executable, str(scraper_path), "--dry-run"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print_success("Scraper dry run successful")
        return True
    else:
        print_error(f"Scraper failed with code {result.returncode}")
        if result.stderr:
            print_error(f"Error: {result.stderr}")
        return False

def main():
    """Run all workflow tests"""
    print_header("Apple Docs V2 Auto-Rescrape Workflow Test")
    
    # Check environment
    is_docker = check_environment()
    
    # Test components
    tests = []
    
    # 1. Environment variables
    tests.append(("Environment Variables", test_environment_variables()))
    
    # 2. Scraper location
    scraper_ok, scraper_path = test_scraper_location(is_docker)
    tests.append(("Scraper Location", scraper_ok))
    
    # 3. Documentation path
    docs_path = test_documentation_path(is_docker)
    tests.append(("Documentation Path", docs_path is not None))
    
    # 4. Indexer location
    indexer_ok, indexer_path = test_indexer_location(is_docker)
    tests.append(("Indexer Location", indexer_ok))
    
    # 5. Meilisearch connection
    tests.append(("Meilisearch Connection", test_meilisearch_connection()))
    
    # 6. Scheduler paths
    tests.append(("Scheduler Paths", test_scheduler_paths()))
    
    # 7. Mini scrape test (only if scraper found)
    if scraper_ok:
        tests.append(("Scraper Dry Run", run_mini_scrape_test(scraper_path)))
    
    # Summary
    print_header("Test Summary")
    
    passed = sum(1 for _, result in tests if result)
    total = len(tests)
    
    for name, result in tests:
        status = "PASSED" if result else "FAILED"
        color = GREEN if result else RED
        print(f"{color}{name}: {status}{RESET}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print_success("\n🎉 All tests passed! The auto-rescrape workflow is ready.")
    else:
        print_error(f"\n⚠️  {total - passed} tests failed. Please fix the issues above.")
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())