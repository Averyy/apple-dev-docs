#!/usr/bin/env python3
"""Get Meilisearch API keys for configuration."""

import os
import sys
import meilisearch
from dotenv import load_dotenv

load_dotenv()

# Connect with master key
client = meilisearch.Client(
    os.getenv('MEILI_HTTP_ADDR', 'http://localhost:7700'),
    os.getenv('MEILI_MASTER_KEY')
)

try:
    # Get all keys
    keys = client.get_keys()
    
    print("🔑 Meilisearch API Keys:\n")
    
    # Handle the response properly
    if hasattr(keys, 'results'):
        key_list = keys.results
    else:
        key_list = keys
    
    for key in key_list:
        key_data = key if isinstance(key, dict) else key.__dict__
        
        if 'Default Search API Key' in key_data.get('name', '') or 'Default Search API Key' in str(key_data.get('description', '')):
            print(f"Search API Key (for MCP server / read-only access):")
            print(f"  {key_data.get('key', 'N/A')}")
            print(f"  Actions: {', '.join(key_data.get('actions', []))}")
            print(f"  Use this in your MCP server configuration\n")
        elif 'Default Admin API Key' in key_data.get('name', '') or 'Default Admin API Key' in str(key_data.get('description', '')):
            print(f"Admin API Key (for indexing / write access):")
            print(f"  {key_data.get('key', 'N/A')}")
            print(f"  Actions: {', '.join(key_data.get('actions', []))}\n")
    
    print("\n💡 For development, you can also run Meilisearch without auth:")
    print("   meilisearch --no-analytics")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nDebug info:")
    import traceback
    traceback.print_exc()
    print("\nMake sure Meilisearch is running with the master key from .env")
    sys.exit(1)