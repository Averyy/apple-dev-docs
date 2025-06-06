# XCTAssertNotEqual(_:_:_:file:line:)

**Framework**: Xctest  
**Kind**: func

Asserts that two values are not equal.

## Declaration

```swift
func XCTAssertNotEqual<T>(_ expression1: @autoclosure () throws -> T, _ expression2: @autoclosure () throws -> T, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line) where T : Equatable
```

## Parameters

- `expression1`: An expression of type  , where   is  .
- `expression2`: A second expression of type  , where   is  .
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.

## See Also

- [func XCTAssertEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertequal(_:_:_:file:line:).md)
  Asserts that two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnotequal(_:_:_:file:line:))*