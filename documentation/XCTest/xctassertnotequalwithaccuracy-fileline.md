# XCTAssertNotEqualWithAccuracy(_:_:_:_:file:line:)

**Framework**: Xctest  
**Kind**: func

Asserts that two values are not equal within a certain accuracy.

**Availability**:
- Unknown ?+ - Deprecated

## Declaration

```swift
func XCTAssertNotEqualWithAccuracy<T>(_ expression1: @autoclosure () throws -> T, _ expression2: @autoclosure () throws -> T, _ accuracy: T, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line) where T : FloatingPoint
```

#### Discussion

`expression1`, `expression2`, and `accuracy` must all be of the same type `T` that conforms to [`FloatingPoint`](https://developer.apple.com/documentation/Swift/FloatingPoint).

## Parameters

- `expression1`: An expression of type  , where   conforms to  .
- `expression2`: An expression of type  , where   conforms to  .
- `accuracy`: An expression of type  , where   conforms to  . Describes the maximum difference between   and   for these values to be considered not equal.
- `message`: An optional description of the failure.
- `file`: The file in which failure occurred. Defaults to the file name of the test case in which this function was called.
- `line`: The line number on which failure occurred. Defaults to the line number on which this function was called.

## See Also

- [func XCTSelfTestMain() -> Int32](xctselftestmain().md)
- [func XCTAssertEqualWithAccuracy<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, accuracy: T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertequalwithaccuracy(_:_:accuracy:_:file:line:).md)
  Asserts that two values are equal within a certain accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnotequalwithaccuracy(_:_:_:_:file:line:))*