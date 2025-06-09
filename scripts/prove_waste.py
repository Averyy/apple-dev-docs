#!/usr/bin/env python3
"""
Prove that current scripts waste money by re-embedding unchanged files
"""

import subprocess
import re

print("💸 MONEY WASTE TEST")
print("="*70)
print("Running the SAME embedding job twice to prove it wastes money...\n")

# Run 1
print("RUN 1:")
result1 = subprocess.run(
    ["python3", "scripts/build_index_test.py", "--framework", "AdSupport"],
    capture_output=True, text=True
)

# Extract key info from both stdout and stderr
full_output_1 = result1.stdout + result1.stderr
api_calls_1 = len(re.findall(r"HTTP Request: POST.*embeddings", full_output_1))
cost_match_1 = re.search(r"Estimated cost: \$(\d+\.\d+)", full_output_1)
docs_match_1 = re.search(r"Found (\d+) documents", full_output_1)

print(f"  Documents found: {docs_match_1.group(1) if docs_match_1 else '?'}")
print(f"  API calls made: {api_calls_1}")
print(f"  Estimated cost: {cost_match_1.group(0) if cost_match_1 else '?'}")

# Run 2 - EXACT SAME COMMAND
print("\nRUN 2 (identical command, no changes):")
result2 = subprocess.run(
    ["python3", "scripts/build_index_test.py", "--framework", "AdSupport"],
    capture_output=True, text=True
)

full_output_2 = result2.stdout + result2.stderr
api_calls_2 = len(re.findall(r"HTTP Request: POST.*embeddings", full_output_2))
cost_match_2 = re.search(r"Estimated cost: \$(\d+\.\d+)", full_output_2)
docs_match_2 = re.search(r"Found (\d+) documents", full_output_2)

print(f"  Documents found: {docs_match_2.group(1) if docs_match_2 else '?'}")
print(f"  API calls made: {api_calls_2}")
print(f"  Estimated cost: {cost_match_2.group(0) if cost_match_2 else '?'}")

print("\n" + "="*70)
print("ANALYSIS:")
print("="*70)

if api_calls_2 > 0:
    print("❌ CRITICAL ISSUE CONFIRMED!")
    print(f"❌ Made {api_calls_2} API calls for UNCHANGED files!")
    print("❌ This script has NO incremental support!")
    print("\n💸 COST IMPLICATIONS:")
    print("   - Every run costs money, even with no changes")
    print("   - Full run (259,026 files) = $3.74 EVERY TIME")
    print("   - Run it 10 times = $37.40 wasted!")
    print("\n⚠️  DO NOT USE THESE SCRIPTS IN PRODUCTION!")
    print("   Use build_index_incremental.py instead")
else:
    print("✅ No API calls on second run")
    print("✅ Incremental support is working")

# Show the problematic code
print("\n" + "="*70)
print("THE PROBLEM:")
print("="*70)
print("Current scripts blindly embed everything they find:")
print('  for doc in documents:')
print('      embeddings = embed_batch(...)  # NO CHECK IF ALREADY EXISTS!')
print('      collection.add(...)')
print("\nThey SHOULD check:")
print('  if document_already_embedded_and_unchanged:')
print('      skip')
print('  else:')
print('      embed_and_store')