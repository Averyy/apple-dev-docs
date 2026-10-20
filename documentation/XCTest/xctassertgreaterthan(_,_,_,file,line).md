# XCTAssertGreaterThan(_:_:_:file:line:)

**Framework**: XCTest  
**Kind**: func  
**Role**: Function

Asserts that the value of the first expression is greater than the value of the second expression.

## Declaration

```swift
func XCTAssertGreaterThan<T>(_ expression1: @autoclosure () throws -> T, _ expression2: @autoclosure () throws -> T, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line) where T : Comparable
```

## Parameters

- `expression1`: An expression of type `T`, where `T` is [`Comparable`](../Swift/comparable.md).
- `expression2`: A second expression of type `T`, where `T` is [`Comparable`](../Swift/comparable.md).
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.

## See Also

### Tests for Comparable Values
- [func XCTAssertGreaterThanOrEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertgreaterthanorequal%28_,_,_,file,line%29.md)
  Asserts that the value of the first expression is greater than or equal to the value of the second expression.
- [func XCTAssertLessThanOrEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertlessthanorequal%28_,_,_,file,line%29.md)
  Asserts that the value of the first expression is less than or equal to the value of the second expression.
- [func XCTAssertLessThan<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertlessthan%28_,_,_,file,line%29.md)
  Asserts that the value of the first expression is less than the value of the second expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertgreaterthan(_:_:_:file:line:))*