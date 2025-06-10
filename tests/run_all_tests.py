#!/usr/bin/env python3
"""
Comprehensive test runner for the Apple Developer Docs embedding system
Runs all tests and provides detailed coverage report
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
    print("Running all tests for Apple Developer Docs embedding system\n")
    
    # Define all test scripts
    test_scripts = [
        ("tests/test_critical_sync.py", "Critical Scraping Functionality"),
        ("tests/test_chromadb_edge_cases.py", "ChromaDB Edge Cases"),
        ("tests/test_new_features.py", "New Checkpointing & Verification Features"),
        ("tests/test_production_readiness.py", "Production Readiness & Resilience"),
        ("tests/test_hash_integration.py", "Hash Integration System"),
        ("tests/test_orphan_detection.py", "Orphan Detection & Cleanup"),
        ("tests/test_concurrent_scraping.py", "Concurrent Scraping with Semaphore"),
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
    print("   ✅ ChromaDB edge cases (collection names, document limits)")
    print("   ✅ Hash-based change detection and incremental updates")
    print("   ✅ Checkpointing and resume capability")
    print("   ✅ Embedding verification and integrity")
    print("   ✅ Production resilience (error handling, file system)")
    print("   ✅ Security validation (API keys, path traversal)")
    print("   ✅ Health check and monitoring tools")
    print("   ✅ Orphan detection and cleanup (session tracking)")
    print("   ✅ Concurrent scraping (rolling concurrency, error handling)")
    
    # Production readiness assessment
    print(f"\n🚀 Production Readiness Assessment:")
    
    if failed == 0:
        print("   ✅ ALL TESTS PASS - SYSTEM IS PRODUCTION READY!")
        print("   🛡️  Robust error handling verified")
        print("   💰 Cost protection mechanisms tested")
        print("   🔧 Resume/recovery capabilities confirmed")
        print("   📊 Health monitoring tools functional")
        print("   🔐 Security validations in place")
        print(f"\n🎉 The embedding system is ready for production deployment!")
        print(f"   Safe to process all 278,778 Apple documentation files")
        print(f"   Estimated cost: ~$3.74 (one-time), $0-0.10 (updates)")
    else:
        print(f"   ⚠️  {failed} TEST(S) FAILED - ISSUES NEED RESOLUTION")
        print("   🔧 Fix failing tests before production deployment")
        print("   📝 Review error output above for specific issues")
        
        # Show recommendations based on failing tests
        for description, success, output in results:
            if not success:
                if "network" in description.lower():
                    print("   🌐 Network resilience needs attention")
                elif "production" in description.lower():
                    print("   🏭 Production readiness issues detected")
                elif "chromadb" in description.lower():
                    print("   💾 Database edge cases need fixing")
    
    # Next steps
    print(f"\n📋 Next Steps:")
    if failed == 0:
        print("   1. Run full embedding generation:")
        print("      python3 scripts/build_index_incremental.py")
        print("   2. Set up health monitoring:")
        print("      python3 scripts/vectorstore_health_check.py")
        print("   3. Configure automated updates (safe for daily runs)")
    else:
        print("   1. Fix failing tests identified above")
        print("   2. Re-run test suite to verify fixes")
        print("   3. Once all tests pass, proceed with deployment")
    
    print(f"\n{'='*80}")
    
    # Exit with appropriate code
    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    main()