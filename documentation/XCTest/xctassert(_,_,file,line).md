# XCTAssert(_:_:file:line:)

**Framework**: XCTest  
**Kind**: func  
**Role**: Function

Asserts that an expression is true.

## Declaration

```swift
func XCTAssert(_ expression: @autoclosure () throws -> Bool, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line)
```

## Discussion

This function generates a failure when `expression == false` and is equivalent to [`XCTAssertTrue(_:_:file:line:)`](./xctasserttrue%28_,_,file,line%29.md).

## Parameters

- `expression`: An expression of Boolean type.
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.

## See Also

### Tests for True Conditions
- [func XCTAssertTrue(@autoclosure () throws -> Bool, @autoclosure () -> String, file: StaticString, line: UInt)](./xctasserttrue%28_,_,file,line%29.md)
  Asserts that an expression is true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassert(_:_:file:line:))*