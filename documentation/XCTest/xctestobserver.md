# XCTestObserver

**Framework**: XCTest  
**Kind**: class

An object that observes test activity and events.

## Declaration

```swift
class XCTestObserver
```

## Topics

### Starting and Stopping Test Observation
- [func startObserving()](xctestobserver/startobserving.md)
  Starts observing a test.
- [func stopObserving()](xctestobserver/stopobserving.md)
  Stops observing a test.
### Monitoring Test Activity
- [func testCaseDidFail(XCTestRun!, withDescription: String!, inFile: String!, atLine: Int)](xctestobserver/testcasedidfail(_:withdescription:infile:atline:).md)
  Notifies the observer when a test case fails.
- [func testCaseDidStart(XCTestRun!)](xctestobserver/testcasedidstart(_:).md)
  Notifies the observer when a test case starts.
- [func testCaseDidStop(XCTestRun!)](xctestobserver/testcasedidstop(_:).md)
  Notifies the observer when a test case stops.
- [func testSuiteDidStart(XCTestRun!)](xctestobserver/testsuitedidstart(_:).md)
  Notifies the observer when a test suite starts.
- [func testSuiteDidStop(XCTestRun!)](xctestobserver/testsuitedidstop(_:).md)
  Notifies the observer when a test suite stops.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [XCTestLog](xctestlog.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class XCTestLog](xctestlog.md)
  An object that logs test failures and errors.
- [class XCTestProbe](xctestprobe.md)
  An object that observes test activity status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobserver)*