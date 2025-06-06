# XCTAssertEqual(_:_:_:file:line:)

**Framework**: Xctest  
**Kind**: func

Asserts that two values are equal.

## Declaration

```swift
func XCTAssertEqual<T>(_ expression1: @autoclosure () throws -> T, _ expression2: @autoclosure () throws -> T, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line) where T : Equatable
```

#### Discussion

Use this function to compare two non-optional values of the same type.

Listing 1. Comparing Non-Optional Values Of The Same Type

```objc
class FrameSizeTests: XCTestCase {
    func testInitialFrameSize() {
        let view = CustomView()
        let expectedSize = CGSize(width: 640.0, height: 480.0)
        XCTAssertEqual(view.frame.size, expectedSize, "Unexpected frame size.")
    }
}
```

Listing 1 creates a new instance of a custom class called `CustomView`, and checks that its size is equal to `CGSize(width: 640.0, height: 480.0)`.

## Parameters

- `expression1`: An expression of type  , where   is  .
- `expression2`: A second expression of type  , where   is  .
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.

## See Also

- [func XCTAssertNotEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertnotequal(_:_:_:file:line:).md)
  Asserts that two values are not equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertequal(_:_:_:file:line:))*