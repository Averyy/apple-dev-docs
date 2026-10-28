# XCTAssertNotNil(_:_:file:line:)

**Framework**: XCTest  
**Kind**: func  
**Role**: Function

Asserts that an expression is not `nil`.

## Declaration

```swift
func XCTAssertNotNil(_ expression: @autoclosure () throws -> Any?, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line)
```

## Discussion

This function generates a failure when `expression == nil`.

## Parameters

- `expression`: An expression of type `Any?` to compare against `nil`.
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.

## See Also

### Tests for a Non-Nil Condition
- [func XCTUnwrap<T>(@autoclosure () throws -> T?, @autoclosure () -> String, file: StaticString, line: UInt) throws -> T](./xctunwrap%28_,_,file,line%29.md)
  Asserts that an expression is not `nil,` and returns the unwrapped value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnotnil(_:_:file:line:))*