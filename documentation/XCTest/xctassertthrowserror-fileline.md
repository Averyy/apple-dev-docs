# XCTAssertThrowsError(_:_:file:line:_:)

**Framework**: XCTest  
**Kind**: func

Asserts that an expression throws an error.

## Declaration

```swift
func XCTAssertThrowsError<T>(_ expression: @autoclosure () throws -> T, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line, _ errorHandler: (any Error) -> Void = { _ in })
```

## Parameters

- `expression`: An expression that can throw an error.
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.
- `errorHandler`: An optional handler for errors that   throws.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertthrowserror(_:_:file:line:_:))*