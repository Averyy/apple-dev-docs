# XCTSkip

**Framework**: XCTest  
**Kind**: struct  
**Role**: Structure

An error that causes the current test to cease executing and the test runner to mark the test as skipped when the test throws the error.

## Declaration

```swift
struct XCTSkip
```

## Topics

### Skipping a Test
- [init(String?, file: StaticString, line: UInt)](./xctskip-swift.struct/init%28_,file,line%29.md)
  Intitializes an error to skip a test.
### Describing a Skipped Test
- [var message: String?](./xctskip-swift.struct/message.md)
  An optional description of the skipped test, displayed in the Test navigator.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/customnserror.md)
- [Error](../Swift/error.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Methods for Skipping Tests
- [func XCTSkipIf(@autoclosure () throws -> Bool, @autoclosure () -> String?, file: StaticString, line: UInt) throws](./xctskipif%28_,_,file,line%29.md)
  Skips remaining tests in a test method if the specified condition is met.
- [func XCTSkipUnless(@autoclosure () throws -> Bool, @autoclosure () -> String?, file: StaticString, line: UInt) throws](./xctskipunless%28_,_,file,line%29.md)
  Skips remaining tests in a test method unless the specified condition is met.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctskip-swift.struct)*