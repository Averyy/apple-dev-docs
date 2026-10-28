# XCTAssertEqualWithAccuracy(_:_:accuracy:_:file:line:)

**Framework**: XCTest  
**Kind**: func  
**Role**: Function

Asserts that two values are equal within a certain accuracy.

> **Deprecated**: Use [`XCTAssertEqual(_:_:accuracy:_:file:line:)`](./xctassertequal%28_,_,accuracy,_,file,line%29-6frfw.md) instead.

## Declaration

```swift
func XCTAssertEqualWithAccuracy<T>(_ expression1: @autoclosure () throws -> T, _ expression2: @autoclosure () throws -> T, accuracy: T, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line) where T : FloatingPoint
```

## Discussion

`expression1`, `expression2`, and `accuracy` must all be of the same type `T` that conforms to [`FloatingPoint`](../Swift/floatingpoint.md).

## Parameters

- `expression1`: An expression of type `T`, where `T` conforms to [`FloatingPoint`](../Swift/floatingpoint.md).
- `expression2`: An expression of type `T`, where `T` conforms to [`FloatingPoint`](../Swift/floatingpoint.md).
- `accuracy`: An expression of type `T`, where `T` conforms to [`FloatingPoint`](../Swift/floatingpoint.md). Describes the maximum difference between `expression1` and `expression2` for these values to be considered equal.
- `message`: An optional description of the failure.
- `file`: The file in which failure occurred. Defaults to the file name of the test case in which this function was called.
- `line`: The line number on which failure occurred. Defaults to the line number on which this function was called.

## See Also

### Deprecated Functions
- [func XCTSelfTestMain() -> Int32](./xctselftestmain%28%29.md)
- [func XCTAssertNotEqualWithAccuracy<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, T, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertnotequalwithaccuracy%28_,_,_,_,file,line%29.md)
  Asserts that two values are not equal within a certain accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertequalwithaccuracy(_:_:accuracy:_:file:line:))*