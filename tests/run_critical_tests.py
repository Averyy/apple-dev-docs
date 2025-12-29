#!/usr/bin/env python3
"""Run critical tests without pytest dependency."""

import sys
import subprocess
from pathlib import Path

def main():
    """Run critical tests."""
    test_dir = Path(__file__).parent
    tests = [
        ("test_critical_sync.py", "critical scraping"),
    ]
    
    all_passed = True
    
    for test_file, description in tests:
        test_path = test_dir / test_file
        
        print(f"🧪 Running {description} tests...")
        print("=" * 50)
        
        try:
            result = subprocess.run(
                [sys.executable, str(test_path)],
                capture_output=True,
                text=True
            )
            
            print(result.stdout)
            
            if result.stderr:
                print("Errors:", result.stderr)
            
            if result.returncode != 0:
                all_passed = False
                print(f"\n❌ {description} tests failed!")
            else:
                print(f"\n✅ {description} tests passed!")
                
        except Exception as e:
            print(f"❌ Error running {description} tests: {e}")
            all_passed = False
    
    if all_passed:
        print("\n✅ All critical tests passed successfully!")
        return 0
    else:
        print("\n❌ Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())