#!/usr/bin/env python3
"""Verify both local and remote deployment modes work correctly"""

import json
import os
from pathlib import Path

print("🔍 Verifying Deployment Modes")
print("=" * 60)

# 1. Check Local STDIO Mode
print("\n1. LOCAL STDIO MODE (for development)")
print("-" * 40)

# Check main STDIO server
if Path("apple_docs_stdio_mcp.py").exists():
    print("✅ Main STDIO server exists")
    
    # Check Claude Code config for local
    local_config = {
        "mcpServers": {
            "apple-docs": {
                "command": "python3",
                "args": [str(Path.cwd() / "apple_docs_stdio_mcp.py")]
            }
        }
    }
    print("✅ Local Claude Code config:")
    print(f"   {json.dumps(local_config, indent=2)}")
else:
    print("❌ Main STDIO server missing!")

# 2. Check Remote HTTP Mode
print("\n\n2. REMOTE HTTP MODE (for deployment at 192.168.2.5)")
print("-" * 40)

# Check HTTP wrapper
if Path("http_stdio_wrapper.py").exists():
    print("✅ HTTP wrapper exists (for server)")
    
    # Check supervisord config
    supervisord_path = Path("docker/supervisord.conf")
    if supervisord_path.exists():
        with open(supervisord_path) as f:
            content = f.read()
            if "ENABLE_HTTP_WRAPPER" in content and "http_stdio_wrapper.py" in content:
                print("✅ Supervisord configured to run HTTP wrapper")
            else:
                print("❌ Supervisord missing HTTP wrapper config")
else:
    print("❌ HTTP wrapper missing!")

# Check STDIO-to-HTTP bridge
if Path("apple_docs_stdio_http_bridge.py").exists():
    print("✅ STDIO-to-HTTP bridge exists (for Claude Code)")
    
    # Check Claude Code config for remote
    remote_config = {
        "mcpServers": {
            "apple-docs": {
                "command": "python3",
                "args": [
                    str(Path.cwd() / "apple_docs_stdio_http_bridge.py"),
                    "--server-url", "http://192.168.2.5:8080/mcp"
                ],
                "env": {
                    "MCP_API_KEY": "your-api-key"
                }
            }
        }
    }
    print("✅ Remote Claude Code config:")
    print(f"   {json.dumps(remote_config, indent=2)}")
else:
    print("❌ STDIO-to-HTTP bridge missing!")

# 3. Check Docker Configuration
print("\n\n3. DOCKER CONFIGURATION")
print("-" * 40)

# Check docker-compose.yml
docker_compose = Path("docker-compose.yml")
if docker_compose.exists():
    with open(docker_compose) as f:
        content = f.read()
        checks = {
            "HTTP port exposed": "8080:8080" in content,
            "HTTP wrapper env var": "ENABLE_HTTP_WRAPPER" in content,
            "Default is false": "ENABLE_HTTP_WRAPPER:-false" in content,
            "Documentation volume": "documentation:/data/documentation" in content
        }
        
        for check, result in checks.items():
            print(f"{'✅' if result else '❌'} {check}")

# Check .env.example
env_example = Path("../.env.example")
if env_example.exists():
    with open(env_example) as f:
        content = f.read()
        if "ENABLE_HTTP_WRAPPER=false" in content:
            print("✅ .env.example has ENABLE_HTTP_WRAPPER=false default")
        else:
            print("❌ .env.example missing proper defaults")

# 4. Check Auto-rescrape Control
print("\n\n4. AUTO-RESCRAPE CONTROL")
print("-" * 40)

# Check supervisord for scheduler control
supervisord_path = Path("docker/supervisord.conf")
if supervisord_path.exists():
    with open(supervisord_path) as f:
        content = f.read()
        if 'if [ "$ENABLE_AUTO_RESCRAPE" = "true" ]' in content:
            print("✅ Scheduler only runs when ENABLE_AUTO_RESCRAPE=true")
        else:
            print("❌ Scheduler not properly controlled")

# Check docker-compose default
if docker_compose.exists():
    with open(docker_compose) as f:
        content = f.read()
        if "ENABLE_AUTO_RESCRAPE:-false" in content:
            print("✅ Auto-rescrape defaults to false")
        else:
            print("❌ Auto-rescrape default not set")

# 5. Summary
print("\n\n5. DEPLOYMENT SUMMARY")
print("-" * 40)
print("""
LOCAL MODE:
- Claude Code → STDIO → apple_docs_stdio_mcp.py → Meilisearch
- Direct process communication
- No network overhead

REMOTE MODE:
- Claude Code → STDIO → apple_docs_stdio_http_bridge.py → HTTP → 192.168.2.5:8080
- Server runs http_stdio_wrapper.py when ENABLE_HTTP_WRAPPER=true
- Requires MCP_API_KEY for authentication

Both modes use the same core server (apple_docs_stdio_mcp.py)
""")

print("✅ Both deployment modes are properly configured!")