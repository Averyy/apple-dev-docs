#!/usr/bin/env python3
"""
Run self-tests when supervisor starts the services.
This script listens for supervisor events and runs tests when all services are running.
"""

import sys
import time
import subprocess
from pathlib import Path

def write_stdout(s):
    """Write to stdout for supervisor"""
    sys.stdout.write(s)
    sys.stdout.flush()

def write_stderr(s):
    """Write to stderr for supervisor"""
    sys.stderr.write(s)
    sys.stderr.flush()

def main():
    """Main event listener loop"""
    # Wait for supervisor to be ready
    write_stdout('READY\n')
    
    # Read header line from stdin
    line = sys.stdin.readline()
    
    # Parse the header
    headers = dict([x.split(':') for x in line.split()])
    
    # Check if this is a state change event
    if headers.get('eventname') == 'SUPERVISOR_STATE_CHANGE_RUNNING':
        # Wait a bit for services to stabilize
        time.sleep(10)
        
        # Check if both services are running
        result = subprocess.run(['supervisorctl', 'status'], capture_output=True, text=True)
        
        if 'mcp-server' in result.stdout and 'RUNNING' in result.stdout:
            if 'scheduler' in result.stdout and 'RUNNING' in result.stdout:
                write_stderr("All services running, executing self-tests...\n")
                
                # Run the self-test
                test_result = subprocess.run(
                    [sys.executable, '/app/scripts/self_test.py'],
                    capture_output=True,
                    text=True
                )
                
                # Log the output
                write_stderr(test_result.stdout)
                if test_result.stderr:
                    write_stderr(test_result.stderr)
                
                if test_result.returncode == 0:
                    write_stderr("✅ Self-tests passed!\n")
                    # Mark self-test as completed
                    Path('/data/hashes/.self_test_completed').touch()
                else:
                    write_stderr("❌ Self-tests failed!\n")
    
    # Acknowledge the event
    write_stdout('RESULT 2\nOK')
    
    # Exit after running once
    sys.exit(0)

if __name__ == '__main__':
    main()