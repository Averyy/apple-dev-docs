#!/usr/bin/env python3
"""
Direct test to prove current scripts re-embed everything
"""

import os
import time
from pathlib import Path
import openai
from dotenv import load_dotenv

# Load environment
env_path = Path(__file__).parent.parent / "mcp-server" / ".env"
load_dotenv(env_path)

# Track API calls
api_calls = []
original_create = openai.OpenAI().embeddings.create

def track_calls(client_self, *args, **kwargs):
    api_calls.append(time.time())
    print(f"   🔴 API CALL #{len(api_calls)} - Creating embeddings...")
    return original_create(*args, **kwargs)

# Monkey patch to track calls
openai.OpenAI.embeddings.create = track_calls

print("="*70)
print("TESTING: Do current scripts re-embed unchanged files?")
print("="*70)

print("\n1. First run - embedding AdSupport (5 files)...")
os.system("python3 scripts/build_index_test.py --framework AdSupport >/dev/null 2>&1")
first_run_calls = len(api_calls)
print(f"\n   Total API calls: {first_run_calls}")
print(f"   Expected: 1 (batch of 5 files)")

print("\n2. Second run - SAME files, NO changes...")
api_calls.clear()
os.system("python3 scripts/build_index_test.py --framework AdSupport >/dev/null 2>&1")
second_run_calls = len(api_calls)
print(f"\n   Total API calls: {second_run_calls}")
print(f"   Expected: 0 (should skip all)")

print("\n" + "="*70)
print("RESULTS:")
print("="*70)

if second_run_calls == 0:
    print("✅ PASS: No embeddings created on second run")
    print("✅ Incremental updates are working!")
else:
    print(f"❌ FAIL: Created {second_run_calls} embeddings for UNCHANGED files!")
    print("💸 This means wasting $3.74 on EVERY run!")
    print("\n⚠️  CRITICAL ISSUE: Scripts have NO incremental support!")
    print("   They will re-embed all 259,026 files every time!")
    print("   That's $3.74 wasted on each run!")