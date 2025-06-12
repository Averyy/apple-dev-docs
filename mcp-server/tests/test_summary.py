#!/usr/bin/env python3
"""
Summary test script to verify all MCP server components.
"""

import os
import sys
import subprocess
from pathlib import Path

# Colors for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def run_test(name, command, cwd=None):
    """Run a test and return success status"""
    print(f"\n{BLUE}Running: {name}{RESET}")
    print(f"Command: {command}")
    print("-" * 60)
    
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"{GREEN}✅ PASSED{RESET}")
            # Show key results
            if "passed" in result.stdout:
                lines = result.stdout.split('\n')
                for line in lines:
                    if "passed" in line and "failed" in line:
                        print(f"   {line.strip()}")
            return True
        else:
            print(f"{RED}❌ FAILED{RESET}")
            if result.stderr:
                print(f"Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"{RED}❌ ERROR: {e}{RESET}")
        return False


def check_environment():
    """Check environment setup"""
    print(f"\n{BLUE}Checking Environment{RESET}")
    print("-" * 60)
    
    checks = []
    
    # Check Python version
    py_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    if sys.version_info >= (3, 11):
        print(f"{GREEN}✅ Python {py_version}{RESET}")
        checks.append(True)
    else:
        print(f"{RED}❌ Python {py_version} (need 3.11+){RESET}")
        checks.append(False)
    
    # Check environment variables
    env_vars = ['OPENAI_API_KEY', 'MCP_API_KEY']
    for var in env_vars:
        if os.getenv(var):
            print(f"{GREEN}✅ {var} is set{RESET}")
            checks.append(True)
        else:
            print(f"{YELLOW}⚠️  {var} not set (required for full tests){RESET}")
            checks.append(False)
    
    # Check vectorstore
    vectorstore_path = Path.cwd() / "vectorstore"
    if vectorstore_path.exists() and any(vectorstore_path.iterdir()):
        print(f"{GREEN}✅ Vectorstore exists{RESET}")
        checks.append(True)
    else:
        print(f"{YELLOW}⚠️  Vectorstore not found (run build_index.py){RESET}")
        checks.append(False)
    
    return all(checks)


def main():
    """Run all tests and provide summary"""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}MCP Server Test Summary{RESET}")
    print(f"{BLUE}{'='*60}{RESET}")
    
    # Change to mcp-server directory
    mcp_dir = Path(__file__).parent.parent
    os.chdir(mcp_dir)
    
    # Check environment
    env_ok = check_environment()
    
    # Define tests to run
    tests = [
        ("Infrastructure Tests", "./venv/bin/python tests/test_mcp_infrastructure.py"),
        ("Embedding Feature Tests", "./venv/bin/python tests/test_embedding_features.py"),
    ]
    
    # Add comprehensive tests only if vectorstore exists
    if Path("vectorstore").exists():
        tests.append(("Comprehensive Verification", "./venv/bin/python tests/test_comprehensive_verification.py"))
    
    # Run tests
    results = []
    for test_name, command in tests:
        success = run_test(test_name, command)
        results.append((test_name, success))
    
    # Summary
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Test Results Summary{RESET}")
    print(f"{BLUE}{'='*60}{RESET}")
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for test_name, success in results:
        status = f"{GREEN}PASSED{RESET}" if success else f"{RED}FAILED{RESET}"
        print(f"{test_name:.<40} {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    # Recommendations
    print(f"\n{BLUE}Recommendations:{RESET}")
    
    if not env_ok:
        print(f"{YELLOW}1. Set up environment variables:{RESET}")
        print("   - Create .env file from .env.example")
        print("   - Set OPENAI_API_KEY and MCP_API_KEY")
    
    if not Path("vectorstore").exists():
        print(f"{YELLOW}2. Build the vectorstore:{RESET}")
        print("   python scripts/build_index.py")
        print("   (This requires sample Apple documentation in ../documentation/)")
    
    if passed == total:
        print(f"{GREEN}✅ All tests passed! The MCP server is ready to use.{RESET}")
        print("\nTo run the server:")
        print("   make server")
        print("\nTo test with a running server:")
        print("   python tests/test_mcp_server.py")
    else:
        print(f"{RED}❌ Some tests failed. Please fix the issues above.{RESET}")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)