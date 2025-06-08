#!/usr/bin/env python3
"""
Quick test script to verify environment setup
"""

import os
import sys
from pathlib import Path

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

print("Apple Docs MCP Server - Setup Test")
print("==================================\n")

# Test imports
print("1. Testing imports...")
try:
    import chromadb
    print("✓ chromadb imported successfully")
except ImportError as e:
    print(f"✗ Failed to import chromadb: {e}")

try:
    import requests
    print("✓ requests imported successfully")
except ImportError as e:
    print(f"✗ Failed to import requests: {e}")

try:
    import fastapi
    print("✓ fastapi imported successfully")
except ImportError as e:
    print(f"✗ Failed to import fastapi: {e}")

# Test environment variables
print("\n2. Testing environment variables...")
tei_url = os.getenv("TEI_URL")
mcp_api_key = os.getenv("MCP_API_KEY")
docs_path = os.getenv("DOCS_PATH", "../documentation")

if tei_url:
    print(f"✓ TEI_URL configured: {tei_url}")
else:
    print("✗ TEI_URL not configured")

if mcp_api_key:
    print(f"✓ MCP_API_KEY configured: {mcp_api_key[:8]}...")
else:
    print("✗ MCP_API_KEY not configured")

# Test TEI connection
print("\n3. Testing TEI server connection...")
if tei_url:
    try:
        import requests
        response = requests.post(
            tei_url, 
            json={"inputs": ["test"]},
            timeout=5
        )
        if response.status_code == 200:
            print(f"✓ TEI server accessible at {tei_url}")
            print(f"  Response shape: {len(response.json())} embeddings")
        else:
            print(f"✗ TEI server returned status {response.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"✗ Cannot connect to TEI server at {tei_url}")
    except Exception as e:
        print(f"✗ Error testing TEI server: {e}")

# Test documentation directory
print("\n4. Testing documentation directory...")
docs_full_path = Path(docs_path).resolve()
if docs_full_path.exists():
    # Count frameworks
    framework_count = len([d for d in docs_full_path.iterdir() if d.is_dir()])
    print(f"✓ Documentation directory found: {docs_full_path}")
    print(f"  Contains {framework_count} framework directories")
else:
    print(f"✗ Documentation directory not found: {docs_full_path}")

print("\n✓ All imports working!" if all([
    'chromadb' in sys.modules,
    'requests' in sys.modules,
    'fastapi' in sys.modules,
    tei_url,
    mcp_api_key
]) else "\n⚠ Some components need attention")