# XCTAssertFalse(_:_:file:line:)

**Framework**: XCTest  
**Kind**: func

Asserts that an expression is false.

## Declaration

```swift
func XCTAssertFalse(_ expression: @autoclosure () throws -> Bool, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line)
```

#### Discussion

This function generates a failure when `expression == true`.

## Parameters

- `expression`: An expression of Boolean type.
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertfalse(_:_:file:line:))*