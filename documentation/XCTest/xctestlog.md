# XCTestLog

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

An object that logs test failures and errors.

> **Deprecated**: Use [`XCTIssue`](./xctissue-swift.struct.md) instead.

## Declaration

```swift
class XCTestLog
```

```objc
@interface XCTestLog : XCTestObserver
```

## Topics

### Logging Test Results
- [var logFileHandle: FileHandle!](./xctestlog/logfilehandle.md)
  An object to interact with the test log file.
- [func testLog(withFormat: String!, arguments: CVaListPointer)](./xctestlog/testlog%28withformat,arguments%29.md)
  Logs test results to the test log.
- [- testLogWithFormat:](./xctestlog/testlogwithformat_.md)
  Logs test results to the test log.

## Relationships

### Inherits From
- [XCTestObserver](./xctestobserver.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated Classes
- [class XCTestObserver](./xctestobserver.md)
  An object that observes test activity and events.
- [class XCTestProbe](./xctestprobe.md)
  An object that observes test activity status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestlog)*