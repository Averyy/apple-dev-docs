# XCTAssertEqualWithAccuracy(_:_:accuracy:_:file:line:)

**Framework**: XCTest  
**Kind**: func

Asserts that two values are equal within a certain accuracy.

## Declaration

```swift
func XCTAssertEqualWithAccuracy<T>(_ expression1: @autoclosure () throws -> T, _ expression2: @autoclosure () throws -> T, accuracy: T, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line) where T : FloatingPoint
```

#### Discussion

`expression1`, `expression2`, and `accuracy` must all be of the same type `T` that conforms to [`FloatingPoint`](https://developer.apple.com/documentation/Swift/FloatingPoint).

## Parameters

- `expression1`: An expression of type `T`, where `T` conforms to [`FloatingPoint`](https://developer.apple.com/documentation/Swift/FloatingPoint).
- `expression2`: An expression of type `T`, where `T` conforms to [`FloatingPoint`](https://developer.apple.com/documentation/Swift/FloatingPoint).
- `accuracy`: An expression of type `T`, where `T` conforms to [`FloatingPoint`](https://developer.apple.com/documentation/Swift/FloatingPoint). Describes the maximum difference between `expression1` and `expression2` for these values to be considered equal.
- `message`: An optional description of the failure.
- `file`: The file in which failure occurred. Defaults to the file name of the test case in which this function was called.
- `line`: The line number on which failure occurred. Defaults to the line number on which this function was called.

## See Also

- [func XCTSelfTestMain() -> Int32](xctselftestmain().md)
- [func XCTAssertNotEqualWithAccuracy<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertnotequalwithaccuracy(_:_:_:_:file:line:).md)
  Asserts that two values are not equal within a certain accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertequalwithaccuracy(_:_:accuracy:_:file:line:))*