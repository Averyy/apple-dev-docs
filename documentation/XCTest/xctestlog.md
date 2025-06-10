# XCTestLog

**Framework**: XCTest  
**Kind**: class

An object that logs test failures and errors.

**Availability**:
- Unknown ?+ - Deprecated

## Declaration

```swift
class XCTestLog
```

## Topics

### Logging Test Results
- [var logFileHandle: FileHandle!](xctestlog/logfilehandle.md)
  An object to interact with the test log file.
- [func testLog(withFormat: String!, arguments: CVaListPointer)](xctestlog/testlog(withformat:arguments:).md)
  Logs test results to the test log.

## Relationships

### Inherits From
- [XCTestObserver](xctestobserver.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class XCTestObserver](xctestobserver.md)
  An object that observes test activity and events.
- [class XCTestProbe](xctestprobe.md)
  An object that observes test activity status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestlog)*