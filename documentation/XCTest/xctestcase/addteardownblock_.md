# addTeardownBlock:

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Registers a block of teardown code to run after the current test method ends.

## Declaration

```objc
- (void) addTeardownBlock:(void (^)()) block;
```

#### Discussion

Call [`addTeardownBlock:`](./addteardownblock_.md) during a test method’s execution to register a block of code to be called when the test method ends.

Registered teardown blocks are called before the [`tearDown()`](../xctest-page/teardown%28%29.md), [`tearDownWithError()`](../xctest-page/teardownwitherror%28%29.md), or [`tearDown(completion:)`](../xctest-page/teardown%28completion%29.md) instance methods for their associated test case are executed. Teardown blocks are run on the main thread, but can be registered from any thread. Each registered block is run once, in last-in, first-out order, executed serially.

> **Note**:  You can register a teardown block within a test case’s [`setUp()`](../xctest-page/setup%28%29.md), [`setUpWithError()`](../xctest-page/setupwitherror%28%29.md), or [`setUp(completion:)`](../xctest-page/setup%28completion%29.md) instance methods, but not from within its [`tearDown()`](../xctest-page/teardown%28%29.md), [`tearDownWithError()`](../xctest-page/teardownwitherror%28%29.md), or [`tearDown(completion:)`](../xctest-page/teardown%28completion%29.md) instance methods, or from within another teardown block. Teardown blocks always execute before the test system calls the [`tearDown()`](../xctest-page/teardown%28%29.md), [`tearDownWithError()`](../xctest-page/teardownwitherror%28%29.md), or [`tearDown(completion:)`](../xctest-page/teardown%28completion%29.md) instance methods.

Use teardown blocks to write test-specific teardown code alongside associated setup code. For example, if a test method needs to create a resource that must be deleted when the test completes, write the code to create the resource, followed immediately by code that registers a teardown block to delete the resource.

Listing 1. Example test case to write and read a string to and from a file on disk, using a teardown block to delete the file after the test completes

```swift
class ReadAndWriteTests: XCTestCase {
    
    /**
    Creates a URL for a temporary file on disk. Registers a teardown block to
    delete a file at that URL (if one exists) during test teardown.
    */
    func temporaryFileURL() -> URL {
        
        // Create a URL for an unique file in the system's temporary directory.
        let directory = NSTemporaryDirectory()
        let filename = UUID().uuidString
        let fileURL = URL(fileURLWithPath: directory).appendingPathComponent(filename)
        
        // Add a teardown block to delete any file at `fileURL`.
        addTeardownBlock {
            do {
                let fileManager = FileManager.default
                // Check that the file exists before trying to delete it.
                if fileManager.fileExists(atPath: fileURL.path) {
                    // Perform the deletion.
                    try fileManager.removeItem(at: fileURL)
                    // Verify that the file no longer exists after the deletion.
                    XCTAssertFalse(fileManager.fileExists(atPath: fileURL.path))
                }
            } catch {
                // Treat any errors during file deletion as a test failure.
                XCTFail("Error while deleting temporary file: \(error)")
            }
        }
        
        // Return the temporary file URL for use in a test method.
        return fileURL
        
    }
    
    /**
    Tests that a string can be written to a temporary file and read back in
    again from that file without error.
    */
    func testReadAndWriteDataToTemporaryFile() throws {  
      
        // Obtain a temporary file URL for this test to write to.
        let fileURL = temporaryFileURL()
        
        /// A string to be written to the temporary file location.
        let originalString = "Hello there"
        
        // Write the string to the temporary file URL.
        try originalString.write(to: fileURL, atomically: true, encoding: .utf8)
        // Read the same file's contents into a new string.
        let readString = try String(contentsOf: fileURL, encoding: .utf8)
        // Verify that the string is the same after writing and reading.
        XCTAssertEqual(readString, originalString)

    }

}
```

Listing 1 tests that a string can be written to a temporary file on disk and read back into a new string from the same file. The temporary file is deleted as part of the test’s teardown process.

The sole test method in this test case, `testReadAndWriteDataToTemporaryFile()`, calls a convenience method named `temporaryFileURL()` to construct a URL to a temporary file location on disk. In addition to constructing the URL, the `temporaryFileURL()` method also registers a teardown block that deletes the temporary file during test teardown. You can call the `temporaryFileURL()` method multiple times from the same test method, or from multiple different test methods, and it will always clean up any temporary file at the returned URL when the test method completes. Registering a teardown block at the point that the URL is constructed keeps the setup and teardown code closely coupled, and removes the need to track file state in an instance variable on the test case subclass.

> **Note**:  The teardown block in this example needs to call a method that can throw errors, indicated by the `try` keyword. Teardown blocks cannot rethrow errors that occur during their execution, and so they must catch and handle any errors within their own implementation. In the example above, the teardown block wraps the call to the throwing method in a `do`-`catch` block, and treats any caught errors as a test failure.

## Parameters

- `block`: A block of teardown code.

## See Also

### Customizing Test Setup and Teardown
- [Set Up and Tear Down State in Your Tests](../set-up-and-tear-down-state-in-your-tests.md)
  Prepare initial state before tests run, and clean up resources after tests complete.
- [class func setUp()](./setup%28%29.md)
  Provides an opportunity to customize initial state before a test case begins.
- [- addAsyncTeardownBlock:](./addasyncteardownblock_.md)
  Registers a block of asynchronous teardown code to run after the current test method ends.
- [class func tearDown()](./teardown%28%29.md)
  Provides an opportunity to perform cleanup after a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/addteardownblock:)*