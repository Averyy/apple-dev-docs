# XCTAssertNotNil(_:_:file:line:)

**Framework**: Xctest  
**Kind**: func

Asserts that an expression is not `nil`.

## Declaration

```swift
func XCTAssertNotNil(_ expression: @autoclosure () throws -> Any?, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line)
```

#### Discussion

This function generates a failure when `expression == nil`.

## Parameters

- `expression`: An expression of type   to compare against  .
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.

## See Also

- [func XCTUnwrap<T>(@autoclosure () throws -> T?, @autoclosure () -> String, file: StaticString, line: UInt) throws -> T](xctunwrap(_:_:file:line:).md)
  Asserts that an expression is not `nil,` and returns the unwrapped value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnotnil(_:_:file:line:))*