# XCTFail(_:file:line:)

**Framework**: Xctest  
**Kind**: func

This function generates a failure immediately and unconditionally.

## Declaration

```swift
func XCTFail(_ message: String = "", file: StaticString = #filePath, line: UInt = #line)
```

## Parameters

- `message`: An optional description of the assertion, for inclusion in test results.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctfail(_:file:line:))*