# XCTAssertNil(_:_:file:line:)

**Framework**: XCTest  
**Kind**: func

Asserts that an expression is `nil`.

## Declaration

```swift
func XCTAssertNil(_ expression: @autoclosure () throws -> Any?, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line)
```

#### Discussion

This function generates a failure when `expression != nil`.

## Parameters

- `expression`: An expression of type   to compare against  .
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnil(_:_:file:line:))*