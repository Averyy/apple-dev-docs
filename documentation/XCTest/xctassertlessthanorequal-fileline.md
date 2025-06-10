# XCTAssertLessThanOrEqual(_:_:_:file:line:)

**Framework**: XCTest  
**Kind**: func

Asserts that the value of the first expression is less than or equal to the value of the second expression.

## Declaration

```swift
func XCTAssertLessThanOrEqual<T>(_ expression1: @autoclosure () throws -> T, _ expression2: @autoclosure () throws -> T, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line) where T : Comparable
```

## Parameters

- `expression1`: An expression of type  , where   is  .
- `expression2`: A second expression of type  , where   is  .
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.

## See Also

- [func XCTAssertGreaterThan<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertgreaterthan(_:_:_:file:line:).md)
  Asserts that the value of the first expression is greater than the value of the second expression.
- [func XCTAssertGreaterThanOrEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertgreaterthanorequal(_:_:_:file:line:).md)
  Asserts that the value of the first expression is greater than or equal to the value of the second expression.
- [func XCTAssertLessThan<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertlessthan(_:_:_:file:line:).md)
  Asserts that the value of the first expression is less than the value of the second expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertlessthanorequal(_:_:_:file:line:))*