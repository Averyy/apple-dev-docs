# XCTUnwrap(_:_:file:line:)

**Framework**: Xctest  
**Kind**: func

Asserts that an expression is not `nil,` and returns the unwrapped value.

## Declaration

```swift
func XCTUnwrap<T>(_ expression: @autoclosure () throws -> T?, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line) throws -> T
```

#### Return Value

The result of evaluating and unwrapping the `expression`, which is of type `T`. `XCTUnwrap()` only returns a value if `expression` is not `nil`.

#### Discussion

This function generates a failure when `expression` is `nil`. Otherwise, it returns the unwrapped value of `expression` for subsequent use in the test.

## Parameters

- `expression`: An expression of type  . The expression’s type determines the type of the return value.
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.

## See Also

- [func XCTAssertNotNil(@autoclosure () throws -> Any?, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertnotnil(_:_:file:line:).md)
  Asserts that an expression is not `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctunwrap(_:_:file:line:))*