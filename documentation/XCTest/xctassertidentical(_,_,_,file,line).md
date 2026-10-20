# XCTAssertIdentical(_:_:_:file:line:)

**Framework**: XCTest  
**Kind**: func  
**Role**: Function

Asserts that two values are identical.

## Declaration

```swift
func XCTAssertIdentical(_ expression1: @autoclosure () throws -> AnyObject?, _ expression2: @autoclosure () throws -> AnyObject?, _ message: @autoclosure () -> String = "", file: StaticString = #filePath, line: UInt = #line)
```

#### Discussion

Compare two optional values of types that conform to `AnyObject`. The values are identical if they’re the same instance.

## Parameters

- `expression1`: An optional expression of type [`AnyObject`](../Swift/anyobject.md).
- `expression2`: A second optional expression of type [`AnyObject`](../Swift/anyobject.md).
- `message`: An optional description of a failure.
- `file`: The file where the failure occurs. The default is the filename of the test case where you call this function.
- `line`: The line number where the failure occurs. The default is the line number where you call this function.

## See Also

### Tests for Identical Objects
- [func XCTAssertNotIdentical(@autoclosure () throws -> AnyObject?, @autoclosure () throws -> AnyObject?, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertnotidentical%28_,_,_,file,line%29.md)
  Asserts that two values aren’t identical.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertidentical(_:_:_:file:line:))*