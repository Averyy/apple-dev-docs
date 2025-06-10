# XCTAssertNotIdentical(_:_:_:file:line:)

**Framework**: XCTest  
**Kind**: func

Asserts that two values aren’t identical.

## Declaration

```swift
func XCTAssertNotIdentical(_ expression1: @autoclosure () throws -> AnyObject?, _ expression2: @autoclosure () throws -> AnyObject?, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line)
```

#### Discussion

Compare two optional values of types that conform to `AnyObject`. The values aren’t identical if they’re not the same instance.

## Parameters

- `expression1`: An optional expression of type  .
- `expression2`: A second optional expression of type  .
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.

## See Also

- [func XCTAssertIdentical(@autoclosure () throws -> AnyObject?, @autoclosure () throws -> AnyObject?, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertidentical(_:_:_:file:line:).md)
  Asserts that two values are identical.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnotidentical(_:_:_:file:line:))*