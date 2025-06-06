# XCTAssertTrue(_:_:file:line:)

**Framework**: Xctest  
**Kind**: func

Asserts that an expression is true.

## Declaration

```swift
func XCTAssertTrue(_ expression: @autoclosure () throws -> Bool, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line)
```

#### Discussion

This function generates a failure when `expression == false` and is equivalent to [`XCTAssert(_:_:file:line:)`](xctassert(_:_:file:line:).md).

## Parameters

- `expression`: An expression of Boolean type.
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.

## See Also

- [func XCTAssert(@autoclosure () throws -> Bool, @autoclosure () -> String, file: StaticString, line: UInt)](xctassert(_:_:file:line:).md)
  Asserts that an expression is true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctasserttrue(_:_:file:line:))*