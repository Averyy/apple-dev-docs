# XCTSkipUnless(_:_:file:line:)

**Framework**: XCTest  
**Kind**: func

Skips remaining tests in a test method unless the specified condition is met.

## Declaration

```swift
func XCTSkipUnless(_ expression: @autoclosure () throws -> Bool, _ message: @autoclosure () -> String? = nil, file: StaticString = #filePath, line: UInt = #line) throws
```

#### Discussion

Call this method to skip any remaining code and assertions in the test method when `expression` evaluates to `false`, and mark the test method as skipped. If a test failure occurs in the test method before the skip, the test runner marks the test method as failed.

## Parameters

- `expression`: A Boolean expression.
- `message`: An optional description of the skip.
- `file`: The file where the skip occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the skip occurs. The default is the line number where you call this function.

## See Also

- [func XCTSkipIf(@autoclosure () throws -> Bool, @autoclosure () -> String?, file: StaticString, line: UInt) throws](xctskipif(_:_:file:line:).md)
  Skips remaining tests in a test method if the specified condition is met.
- [struct XCTSkip](xctskip-swift.struct.md)
  An error that causes the current test to cease executing and the test runner to mark the test as skipped when the test throws the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctskipunless(_:_:file:line:))*