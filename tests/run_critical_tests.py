#!/usr/bin/env python3
"""Run critical tests without pytest dependency."""

import sys
import subprocess
from pathlib import Path

def main():
    """Run critical tests."""
    test_dir = Path(__file__).parent
    test_file = test_dir / "test_critical_sync.py"
    
    print("🧪 Running critical scraping tests...")
    print("=" * 50)
    
    try:
        result = subprocess.run(
            [sys.executable, str(test_file)],
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        
        if result.stderr:
            print("Errors:", result.stderr)
        
        if result.returncode == 0:
            print("\n✅ All critical tests passed successfully!")
            return 0
        else:
            print("\n❌ Some tests failed!")
            return 1
            
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())