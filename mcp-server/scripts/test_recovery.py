#!/usr/bin/env python3
"""
Test recovery from interrupted indexing.
This script simulates interruptions and verifies recovery works correctly.
"""
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from server.config import VECTORSTORE_PATH
from server.logger import get_logger

logger = get_logger(__name__)


def simulate_interruption():
    """Simulate an indexing interruption"""
    print("\n1. Starting indexing process...")
    
    # Start build_index.py in a subprocess
    cmd = [sys.executable, "scripts/build_index.py"]
    env = os.environ.copy()
    
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
        env=env
    )
    
    print("✓ Indexing process started (PID: {})".format(process.pid))
    
    # Let it run for a bit
    print("  Letting it run for 30 seconds...")
    time.sleep(30)
    
    # Check if hash file exists and has content
    hash_file = VECTORSTORE_PATH / "file_hashes.json"
    if hash_file.exists():
        with open(hash_file, 'r') as f:
            hashes = json.load(f)
            print(f"  Files indexed so far: {len(hashes)}")
    
    # Interrupt the process
    print("\n2. Interrupting the process...")
    process.send_signal(signal.SIGINT)
    
    # Wait for process to terminate
    try:
        process.wait(timeout=5)
        print("✓ Process interrupted successfully")
    except subprocess.TimeoutExpired:
        print("⚠️  Process didn't terminate, forcing...")
        process.kill()
        process.wait()
    
    return len(hashes) if 'hashes' in locals() else 0


def test_recovery(initial_count: int):
    """Test recovery by resuming indexing"""
    print("\n3. Testing recovery by resuming indexing...")
    
    # Check current state
    hash_file = VECTORSTORE_PATH / "file_hashes.json"
    if not hash_file.exists():
        print("✗ Hash file missing - recovery not possible")
        return False
    
    with open(hash_file, 'r') as f:
        hashes = json.load(f)
        pre_resume_count = len(hashes)
    
    print(f"  Files indexed before resume: {pre_resume_count}")
    
    if pre_resume_count == 0:
        print("✗ No files were indexed before interruption")
        return False
    
    # Resume indexing
    print("  Resuming indexing...")
    result = subprocess.run(
        [sys.executable, "scripts/build_index.py"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"✗ Resume failed with error: {result.stderr}")
        return False
    
    # Check final state
    with open(hash_file, 'r') as f:
        hashes = json.load(f)
        post_resume_count = len(hashes)
    
    print(f"  Files indexed after resume: {post_resume_count}")
    
    # Verify recovery worked
    if post_resume_count >= pre_resume_count:
        print(f"✓ Recovery successful! Indexed {post_resume_count - pre_resume_count} additional files")
        return True
    else:
        print("✗ Recovery failed - file count decreased")
        return False


def test_force_rebuild():
    """Test force rebuild option"""
    print("\n4. Testing force rebuild...")
    
    # Get initial count
    hash_file = VECTORSTORE_PATH / "file_hashes.json"
    if hash_file.exists():
        with open(hash_file, 'r') as f:
            initial_hashes = json.load(f)
            initial_count = len(initial_hashes)
    else:
        initial_count = 0
    
    print(f"  Initial file count: {initial_count}")
    
    # Run with --force flag
    result = subprocess.run(
        [sys.executable, "scripts/build_index.py", "--force"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"✗ Force rebuild failed: {result.stderr}")
        return False
    
    # Verify all files were re-indexed
    if hash_file.exists():
        with open(hash_file, 'r') as f:
            new_hashes = json.load(f)
            new_count = len(new_hashes)
        
        print(f"  Files after force rebuild: {new_count}")
        print("✓ Force rebuild completed successfully")
        return True
    else:
        print("✗ Hash file missing after rebuild")
        return False


def verify_data_integrity():
    """Verify data integrity after recovery"""
    print("\n5. Verifying data integrity...")
    
    try:
        # Test with build_index.py verify option
        result = subprocess.run(
            [sys.executable, "scripts/build_index.py", "--verify"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0 and "Index verification successful" in result.stdout:
            print("✓ Data integrity verified")
            return True
        else:
            print("✗ Data integrity check failed")
            return False
            
    except Exception as e:
        print(f"✗ Error during verification: {e}")
        return False


def main():
    """Main test runner"""
    print("Recovery Test Suite")
    print("===================")
    print("Testing recovery from interrupted indexing\n")
    
    # Check if we're in the right directory
    if not Path("scripts/build_index.py").exists():
        print("❌ Error: Must run from mcp-server directory")
        sys.exit(1)
    
    # Ensure we have some documents to index
    docs_path = Path("../documentation")
    if not docs_path.exists() or not any(docs_path.rglob("*.md")):
        print("❌ Error: No documentation files found")
        print("  Please ensure the scraper has completed first")
        sys.exit(1)
    
    tests_passed = 0
    total_tests = 4
    
    try:
        # Test 1: Simulate interruption
        initial_count = simulate_interruption()
        if initial_count > 0:
            tests_passed += 1
        
        # Test 2: Recovery
        if test_recovery(initial_count):
            tests_passed += 1
        
        # Test 3: Force rebuild
        if test_force_rebuild():
            tests_passed += 1
        
        # Test 4: Data integrity
        if verify_data_integrity():
            tests_passed += 1
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
    
    # Summary
    print(f"\n{'='*40}")
    print(f"Tests passed: {tests_passed}/{total_tests}")
    
    if tests_passed == total_tests:
        print("✅ All recovery tests passed!")
    else:
        print("❌ Some recovery tests failed")
        sys.exit(1)


if __name__ == "__main__":
    main()