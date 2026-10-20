# XCTAssertEqual(_:_:accuracy:_:file:line:)

**Framework**: XCTest  
**Kind**: func

Asserts that two numeric values are equal within a specified accuracy.

## Declaration

```swift
func XCTAssertEqual<T>(_ expression1: @autoclosure () throws -> T, _ expression2: @autoclosure () throws -> T, accuracy: T, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line) where T : Numeric
```

#### Discussion

`expression1`, `expression2`, and `accuracy` must all be of the same type `T`, and type `T` must conform to [`Numeric`](https://developer.apple.com/documentation/swift/numeric).

## Parameters

- `expression1`: An expression of type `T`, where `T` conforms to [`Numeric`](https://developer.apple.com/documentation/swift/numeric).
- `expression2`: A second expression of type `T`, where `T` conforms to [`Numeric`](https://developer.apple.com/documentation/swift/numeric).
- `accuracy`: An expression of type `T`, where `T` conforms to [`Numeric`](https://developer.apple.com/documentation/swift/numeric). This parameter describes the maximum difference between `expression1` and `expression2` for these values to be considered equal.
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.

## See Also

- [func XCTAssertEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, accuracy: T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertequal(_:_:accuracy:_:file:line:)-6frfw.md)
  Asserts that two floating-point values are equal within a specified accuracy.
- [func XCTAssertNotEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, accuracy: T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertnotequal(_:_:accuracy:_:file:line:)-7jcd6.md)
  Asserts that two floating-point values aren’t equal within a specified accuracy.
- [func XCTAssertNotEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, accuracy: T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertnotequal(_:_:accuracy:_:file:line:)-326vc.md)
  Asserts that two numeric values aren’t equal within a specified accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertequal(_:_:accuracy:_:file:line:)-4epu5)*