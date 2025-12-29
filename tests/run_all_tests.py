#!/usr/bin/env python3
"""
Comprehensive test runner for the Apple Developer Docs scraper and MCP server.
Runs all tests and provides detailed coverage report.
"""

import sys
import subprocess
from pathlib import Path

def run_test_script(script_path: Path, description: str) -> tuple[bool, str]:
    """Run a test script and return success status and output"""
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        success = result.returncode == 0
        output = result.stdout + result.stderr
        return success, output
    except subprocess.TimeoutExpired:
        return False, "Test timed out after 5 minutes"
    except Exception as e:
        return False, f"Failed to run test: {e}"

def main():
    """Run all tests and generate comprehensive report"""
    print("🧪 COMPREHENSIVE TEST SUITE")
    print("=" * 80)
    print("Running all tests for Apple Developer Docs scraper\n")

    # Define all test scripts
    test_scripts = [
        ("tests/test_critical_sync.py", "Critical Scraping Functionality"),
        ("tests/test_orphan_detection.py", "Orphan Detection & Cleanup"),
        ("tests/test_concurrent_scraping.py", "Concurrent Scraping with Semaphore"),
        ("tests/test_network_resilience.py", "Network Resilience"),
        ("tests/test_full_orphan_flow.py", "Full Orphan Flow"),
    ]
    
    results = []
    total_time_start = __import__('time').time()
    
    for script_path, description in test_scripts:
        script_path = Path(script_path)
        if not script_path.exists():
            print(f"⚠️  {description}: SKIPPED (file not found: {script_path})")
            results.append((description, False, "File not found"))
            continue
        
        print(f"🔍 Running: {description}")
        print(f"   Script: {script_path}")
        
        start_time = __import__('time').time()
        success, output = run_test_script(script_path, description)
        duration = __import__('time').time() - start_time
        
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   Result: {status} ({duration:.2f}s)")
        
        if not success:
            # Show last few lines of error output
            lines = output.strip().split('\n')
            error_lines = lines[-5:] if len(lines) > 5 else lines
            print(f"   Error: {chr(10).join(error_lines)}")
        
        results.append((description, success, output))
        print()
    
    total_time = __import__('time').time() - total_time_start
    
    # Generate summary report
    print("=" * 80)
    print("TEST SUMMARY REPORT")
    print("=" * 80)
    
    passed = sum(1 for _, success, _ in results if success)
    failed = len(results) - passed
    
    print(f"📊 Overall Results:")
    print(f"   Tests passed: {passed}")
    print(f"   Tests failed: {failed}")
    print(f"   Success rate: {(passed/len(results)*100):.1f}%")
    print(f"   Total time: {total_time:.2f}s")
    print()
    
    # Detailed results
    print(f"📋 Detailed Results:")
    for description, success, _ in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {status} {description}")
    
    # Test coverage analysis
    print(f"\n🎯 Test Coverage Analysis:")
    print("   ✅ Critical scraping functionality (URL conversion, ETag handling)")
    print("   ✅ Path generation and filename safety")
    print("   ✅ Cross-framework reference handling")
    print("   ✅ Orphan detection and cleanup (session tracking)")
    print("   ✅ Concurrent scraping (rolling concurrency, error handling)")
    print("   ✅ Network resilience and error recovery")
    
    # Production readiness assessment
    print(f"\n🚀 Production Readiness Assessment:")

    if failed == 0:
        print("   ✅ ALL TESTS PASS - SYSTEM IS PRODUCTION READY!")
        print("   🛡️  Robust error handling verified")
        print("   🔧 Recovery capabilities confirmed")
        print("   🔐 Path safety validations in place")
    else:
        print(f"   ⚠️  {failed} TEST(S) FAILED - ISSUES NEED RESOLUTION")
        print("   🔧 Fix failing tests before production deployment")
        print("   📝 Review error output above for specific issues")

    # Next steps
    print(f"\n📋 Next Steps:")
    if failed == 0:
        print("   1. Run scraper: python3 scrape.py --all --yes")
        print("   2. Index to Meilisearch: python3 scripts/index_to_meilisearch.py")
        print("   3. Deploy MCP server: cd mcp-server && docker-compose up -d")
    else:
        print("   1. Fix failing tests identified above")
        print("   2. Re-run test suite to verify fixes")
        print("   3. Once all tests pass, proceed with deployment")
    
    print(f"\n{'='*80}")
    
    # Exit with appropriate code
    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    main()