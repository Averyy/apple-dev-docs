#!/usr/bin/env python3
"""
Test the build_index.py script with a small subset of documentation
"""
import json
import os
import shutil
import sys
import time
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from scripts.build_index import VectorIndexBuilder
from server.config import VECTORSTORE_PATH
from server.logger import get_logger

logger = get_logger(__name__)


def create_test_docs(test_docs_path: Path):
    """Create a small set of test documentation files"""
    # Create test directory structure
    test_docs_path.mkdir(parents=True, exist_ok=True)
    
    # Sample documentation content
    test_files = [
        {
            "path": "SwiftUI/Text.md",
            "content": """# Text

**Framework**: SwiftUI  
**Availability**: iOS 13.0+, macOS 10.15+, tvOS 13.0+, watchOS 6.0+  
**Import**: `import SwiftUI`

A view that displays one or more lines of read-only text.

## Declaration
```swift
struct Text : View
```

## Overview
A text view draws a string in your app's user interface using a font, color, and text layout that you specify.

## Code Examples
```swift
Text("Hello, World!")
Text("Multiline\\ntext\\nstring")
Text("Styled Text").font(.title).foregroundColor(.blue)
```

## See Also
- [Label](Label.md)
- [TextField](TextField.md)

[Apple Documentation](https://developer.apple.com/documentation/swiftui/text)
"""
        },
        {
            "path": "SwiftUI/Button.md", 
            "content": """# Button

**Framework**: SwiftUI  
**Availability**: iOS 13.0+, macOS 10.15+, tvOS 13.0+, watchOS 6.0+  
**Import**: `import SwiftUI`

A control that initiates an action.

## Declaration
```swift
struct Button<Label> : View where Label : View
```

## Overview
You create a button by providing an action and a label. The action is a closure that executes when someone taps the button.

## Code Examples
```swift
Button("Sign In") {
    login()
}

Button(action: signIn) {
    Text("Sign In")
}
```

## See Also
- [Text](Text.md)
- [NavigationLink](NavigationLink.md)

[Apple Documentation](https://developer.apple.com/documentation/swiftui/button)
"""
        },
        {
            "path": "UIKit/UIViewController.md",
            "content": """# UIViewController

**Framework**: UIKit  
**Availability**: iOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+  
**Import**: `import UIKit`

An object that manages a view hierarchy for your UIKit app.

## Declaration
```swift
class UIViewController : UIResponder
```

## Overview
The UIViewController class defines the shared behavior that's common to all view controllers.

## Code Examples
```swift
class MyViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        // Configure the view
    }
}
```

## See Also
- [UIView](UIView.md)
- [UINavigationController](UINavigationController.md)

[Apple Documentation](https://developer.apple.com/documentation/uikit/uiviewcontroller)
"""
        }
    ]
    
    # Write test files
    for file_info in test_files:
        file_path = test_docs_path / file_info["path"]
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(file_info["content"])
    
    return len(test_files)


def test_initial_indexing():
    """Test initial indexing of documentation"""
    print("\n1. Testing initial indexing...")
    
    # Create test environment
    test_docs_path = Path("temp_test_docs")
    test_vectorstore = Path("temp_test_vectorstore")
    
    try:
        # Clean up any existing test data
        shutil.rmtree(test_docs_path, ignore_errors=True)
        shutil.rmtree(test_vectorstore, ignore_errors=True)
        
        # Create test documents
        num_docs = create_test_docs(test_docs_path)
        print(f"✓ Created {num_docs} test documents")
        
        # Override vectorstore path for testing
        original_path = VECTORSTORE_PATH
        import server.config
        server.config.VECTORSTORE_PATH = test_vectorstore
        
        # Build index
        builder = VectorIndexBuilder(docs_path=test_docs_path)
        builder.build_index()
        
        # Verify results
        if builder.collection:
            count = builder.collection.count()
            print(f"✓ Indexed {count} documents successfully")
            
            # Verify hash file was created
            hash_file = test_vectorstore / "file_hashes.json"
            if hash_file.exists():
                hashes = json.loads(hash_file.read_text())
                print(f"✓ Hash file created with {len(hashes)} entries")
            
            success = count == num_docs
        else:
            success = False
            
        # Restore original path
        server.config.VECTORSTORE_PATH = original_path
        
        return success, test_docs_path, test_vectorstore
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False, test_docs_path, test_vectorstore


def test_incremental_update(test_docs_path: Path, test_vectorstore: Path):
    """Test incremental update functionality"""
    print("\n2. Testing incremental updates...")
    
    try:
        # Override vectorstore path
        import server.config
        original_path = VECTORSTORE_PATH
        server.config.VECTORSTORE_PATH = test_vectorstore
        
        # Add a new document
        new_file = test_docs_path / "SwiftUI" / "List.md"
        new_file.write_text("""# List

**Framework**: SwiftUI  
**Availability**: iOS 13.0+, macOS 10.15+, tvOS 13.0+, watchOS 6.0+  
**Import**: `import SwiftUI`

A container that presents rows of data arranged in a single column.

## Declaration
```swift
struct List<SelectionValue, Content> : View
```

[Apple Documentation](https://developer.apple.com/documentation/swiftui/list)
""")
        print("✓ Added new document: SwiftUI/List.md")
        
        # Modify existing document
        button_file = test_docs_path / "SwiftUI" / "Button.md"
        content = button_file.read_text()
        button_file.write_text(content + "\n\n## Additional Information\nButtons are interactive elements.")
        print("✓ Modified existing document: SwiftUI/Button.md")
        
        # Run incremental update
        builder = VectorIndexBuilder(docs_path=test_docs_path)
        builder.build_index()
        
        # Verify only changed files were processed
        if builder.collection:
            count = builder.collection.count()
            print(f"✓ Total documents after update: {count}")
            success = count == 4  # 3 original + 1 new
        else:
            success = False
            
        # Restore original path
        server.config.VECTORSTORE_PATH = original_path
        
        return success
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_search_functionality(test_vectorstore: Path):
    """Test searching the indexed documents"""
    print("\n3. Testing search functionality...")
    
    try:
        # Override vectorstore path
        import server.config
        original_path = VECTORSTORE_PATH
        server.config.VECTORSTORE_PATH = test_vectorstore
        
        # Create builder and verify index
        builder = VectorIndexBuilder()
        builder.collection = builder.client.get_collection("apple_docs")
        
        # Test search
        test_query = "SwiftUI button action"
        embeddings = builder._embed_texts([test_query])
        
        results = builder.collection.query(
            query_embeddings=embeddings,
            n_results=3
        )
        
        if results and results['documents'][0]:
            print(f"✓ Search successful for: '{test_query}'")
            print(f"  Found {len(results['documents'][0])} results")
            
            # Check top result
            top_metadata = results['metadatas'][0][0]
            print(f"  Top result: {top_metadata['api_name']} ({top_metadata['framework']})")
            
            success = top_metadata['api_name'] == 'Button'  # Should find Button.md
        else:
            print("✗ No search results found")
            success = False
            
        # Restore original path
        server.config.VECTORSTORE_PATH = original_path
        
        return success
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def cleanup_test_data(test_docs_path: Path, test_vectorstore: Path):
    """Clean up test data"""
    print("\n4. Cleaning up test data...")
    shutil.rmtree(test_docs_path, ignore_errors=True)
    shutil.rmtree(test_vectorstore, ignore_errors=True)
    print("✓ Test data cleaned up")


if __name__ == "__main__":
    print("Build Index Tests")
    print("=================")
    print("Testing the vector index builder with sample documentation")
    
    # Run tests
    success1, test_docs_path, test_vectorstore = test_initial_indexing()
    
    if success1:
        success2 = test_incremental_update(test_docs_path, test_vectorstore)
        success3 = test_search_functionality(test_vectorstore)
    else:
        success2 = success3 = False
    
    # Cleanup
    cleanup_test_data(test_docs_path, test_vectorstore)
    
    # Summary
    tests_passed = sum([success1, success2, success3])
    total_tests = 3
    
    print(f"\n{'='*40}")
    print(f"Tests passed: {tests_passed}/{total_tests}")
    
    if tests_passed == total_tests:
        print("✅ All tests passed! Ready for full indexing.")
    else:
        print("❌ Some tests failed. Please fix issues before proceeding.")
        sys.exit(1)