#!/usr/bin/env python3
"""
Test MCP infrastructure without requiring a full vectorstore.
This tests the code structure and imports.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
# Also add server directory for direct imports
sys.path.insert(0, str(Path(__file__).parent.parent / "server"))

def test_imports():
    """Test that all modules can be imported"""
    print("🧪 Testing module imports...")
    
    modules_to_test = [
        ("Build Index Script", "scripts.build_index", ["IncrementalEmbeddingBuilder"]),
        ("Config Module", "server.config", ["VECTORSTORE_PATH", "COLLECTION_NAME", "MCP_API_KEY"]),
        ("MCP Server", "server.mcp_server", ["app", "search_apple_docs", "list_frameworks"]),
        ("Logger", "server.logger", ["get_logger"]),
    ]
    
    passed = 0
    failed = 0
    
    for module_name, import_path, expected_attrs in modules_to_test:
        try:
            module = __import__(import_path, fromlist=expected_attrs)
            
            # Check expected attributes
            missing = []
            for attr in expected_attrs:
                if not hasattr(module, attr):
                    missing.append(attr)
            
            if missing:
                print(f"❌ {module_name}: Missing attributes {missing}")
                failed += 1
            else:
                print(f"✅ {module_name}: All imports successful")
                passed += 1
                
        except Exception as e:
            print(f"❌ {module_name}: Import failed - {e}")
            failed += 1
    
    return passed, failed


def test_platform_extraction():
    """Test platform extraction logic standalone"""
    print("\n🧪 Testing platform extraction logic...")
    
    from scripts.build_index import IncrementalEmbeddingBuilder
    from pathlib import Path
    # Create dummy paths for the builder
    docs_path = Path("/tmp/docs")
    vectorstore_path = Path("/tmp/vectorstore")
    builder = IncrementalEmbeddingBuilder(docs_path, vectorstore_path)
    
    test_cases = [
        # (content, expected_platforms)
        ("**Availability**: iOS 13.0+, macOS 10.15+", ['ios', 'macos']),
        ("**Availability**: iOS 13.0–17.4 Deprecated, iPadOS 13.0–17.4 Deprecated", ['ios', 'ipados']),
        ("iOS 15.0+, macOS 12.0+, tvOS 15.0+, watchOS 8.0+", ['ios', 'macos', 'tvos', 'watchos']),
        ("visionOS 1.0+", ['visionos']),
        ("Mac Catalyst 13.0+", ['catalyst']),
    ]
    
    passed = 0
    failed = 0
    
    for content, expected in test_cases:
        platforms = builder._extract_platforms(content)
        if set(platforms) == set(expected):
            print(f"✅ Extracted {platforms} from '{content[:50]}...'")
            passed += 1
        else:
            print(f"❌ Expected {expected}, got {platforms} from '{content[:50]}...'")
            failed += 1
    
    return passed, failed


def test_summary_extraction():
    """Test summary extraction logic standalone"""
    print("\n🧪 Testing summary extraction logic...")
    
    from scripts.build_index import IncrementalEmbeddingBuilder
    from pathlib import Path
    # Create dummy paths for the builder
    docs_path = Path("/tmp/docs")
    vectorstore_path = Path("/tmp/vectorstore")
    builder = IncrementalEmbeddingBuilder(docs_path, vectorstore_path)
    
    test_cases = [
        # (content, expected_summary_start)
        ("# Title\n\n## Overview\n\nThis is a test summary. It has multiple sentences.", "This is a test summary."),
        ("# API\n\n## Overview\n\nThe quick brown fox jumps over the lazy dog. More text here.", "The quick brown fox jumps over the lazy dog."),
        ("# Framework\n\nNo overview section here. This is the first line.", None),
    ]
    
    passed = 0
    failed = 0
    
    for content, expected_start in test_cases:
        summary = builder._extract_summary(content)
        if expected_start is None:
            if summary is None:
                print(f"✅ Correctly returned None for content without Overview")
                passed += 1
            else:
                print(f"❌ Expected None, got '{summary}' for content without Overview")
                failed += 1
        else:
            if summary and summary.startswith(expected_start):
                print(f"✅ Extracted summary: '{summary[:50]}...'")
                passed += 1
            else:
                print(f"❌ Expected summary starting with '{expected_start}', got '{summary}'")
                failed += 1
    
    return passed, failed


def test_mcp_endpoints():
    """Test MCP endpoint definitions"""
    print("\n🧪 Testing MCP endpoint definitions...")
    
    try:
        from server.mcp_server import app
        
        # Get all routes
        routes = []
        for route in app.routes:
            if hasattr(route, 'path') and hasattr(route, 'methods'):
                routes.append((route.path, list(route.methods)))
        
        expected_routes = [
            ("/", ["GET"]),
            ("/health", ["GET"]),
            ("/mcp/tools/list", ["GET"]),
            ("/mcp/tools/call", ["POST"]),
        ]
        
        passed = 0
        failed = 0
        
        for path, methods in expected_routes:
            found = False
            for route_path, route_methods in routes:
                if route_path == path and any(m in route_methods for m in methods):
                    print(f"✅ Found endpoint: {methods[0]} {path}")
                    passed += 1
                    found = True
                    break
            
            if not found:
                print(f"❌ Missing endpoint: {methods[0]} {path}")
                failed += 1
        
        return passed, failed
        
    except Exception as e:
        print(f"❌ Failed to test endpoints: {e}")
        return 0, 1


def main():
    """Run all infrastructure tests"""
    print("🔍 MCP Infrastructure Tests")
    print("=" * 50)
    print("These tests verify the code structure without requiring a vectorstore.\n")
    
    all_tests = [
        test_imports,
        test_platform_extraction,
        test_summary_extraction,
        test_mcp_endpoints,
    ]
    
    total_passed = 0
    total_failed = 0
    
    for test_func in all_tests:
        passed, failed = test_func()
        total_passed += passed
        total_failed += failed
    
    print("\n" + "=" * 50)
    print(f"📊 Total Results: {total_passed} passed, {total_failed} failed")
    
    if total_failed == 0:
        print("\n✅ All infrastructure tests passed!")
        print("\n📝 Note: These tests verify code structure only.")
        print("To test with real data, you need to:")
        print("1. Build the vectorstore: cd mcp-server && python scripts/build_index.py")
        print("2. Start the server: cd mcp-server && make server")
        print("3. Run full tests: cd mcp-server && python tests/test_mcp_server.py")
    else:
        print("\n❌ Some infrastructure tests failed.")
        print("Please fix the issues before proceeding.")
    
    return total_failed == 0


if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)