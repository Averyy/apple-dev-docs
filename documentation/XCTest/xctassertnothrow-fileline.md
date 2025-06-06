# XCTAssertNoThrow(_:_:file:line:)

**Framework**: Xctest  
**Kind**: func

Asserts that an expression doesn’t throw an error.

## Declaration

```swift
func XCTAssertNoThrow<T>(_ expression: @autoclosure () throws -> T, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line)
```

## Parameters

- `expression`: An expression that can throw an error.
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnothrow(_:_:file:line:))*