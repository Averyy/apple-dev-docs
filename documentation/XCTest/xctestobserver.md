# XCTestObserver

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

An object that observes test activity and events.

> **Deprecated**: Use [`XCTestObservationCenter`](./xctestobservationcenter.md) instead.

## Declaration

```swift
class XCTestObserver
```

```objc
@interface XCTestObserver : NSObject
```

## Topics

### Starting and Stopping Test Observation
- [func startObserving()](./xctestobserver/startobserving%28%29.md)
  Starts observing a test.
- [func stopObserving()](./xctestobserver/stopobserving%28%29.md)
  Stops observing a test.
### Monitoring Test Activity
- [func testCaseDidFail(XCTestRun!, withDescription: String!, inFile: String!, atLine: Int)](./xctestobserver/testcasedidfail%28_,withdescription,infile,atline%29.md)
  Notifies the observer when a test case fails.
- [func testCaseDidStart(XCTestRun!)](./xctestobserver/testcasedidstart%28_%29.md)
  Notifies the observer when a test case starts.
- [func testCaseDidStop(XCTestRun!)](./xctestobserver/testcasedidstop%28_%29.md)
  Notifies the observer when a test case stops.
- [func testSuiteDidStart(XCTestRun!)](./xctestobserver/testsuitedidstart%28_%29.md)
  Notifies the observer when a test suite starts.
- [func testSuiteDidStop(XCTestRun!)](./xctestobserver/testsuitedidstop%28_%29.md)
  Notifies the observer when a test suite stops.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [XCTestLog](./xctestlog.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated Classes
- [class XCTestLog](./xctestlog.md)
  An object that logs test failures and errors.
- [class XCTestProbe](./xctestprobe.md)
  An object that observes test activity status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobserver)*