# XCTestObservationCenter

**Framework**: XCTest  
**Kind**: class

Provides information about the progress of test runs to registered observers.

## Declaration

```swift
class XCTestObservationCenter
```

#### Overview

Observers can be any object that conforms to the [`XCTestObservation`](xctestobservation.md) protocol. Register new observers with the [`addTestObserver(_:)`](xctestobservationcenter/addtestobserver(_:).md) method and remove them with the [`removeTestObserver(_:)`](xctestobservationcenter/removetestobserver(_:).md) method.

If an [`NSPrincipalClass`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/NSPrincipalClass) key is declared in the test bundle’s Info.plist file, XCTest automatically creates a single instance of that class when the test bundle is loaded. You can use this instance as a place to register observers or do other pretesting global setup before testing for that bundle begins.

> ❗ **Important**:  Observers must be registered manually. The NSPrincipalClass instance is not automatically registered as an observer even if the class conforms to [`XCTestObservation`](xctestobservation.md).

## Topics

### Accessing the Shared Observation Center
- [class var shared: XCTestObservationCenter](xctestobservationcenter/shared.md)
  The shared [`XCTestObservationCenter`](xctestobservationcenter.md) singleton instance.
### Managing Observers
- [func addTestObserver(any XCTestObservation)](xctestobservationcenter/addtestobserver(_:).md)
  Registers an object conforming to [`XCTestObservation`](xctestobservation.md) as an observer for the current test session.
- [func removeTestObserver(any XCTestObservation)](xctestobservationcenter/removetestobserver(_:).md)
  Unregisters an object conforming to [`XCTestObservation`](xctestobservation.md) as an observer for the current test session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol XCTestObservation](xctestobservation.md)
  A protocol that defines methods the test runner calls in response to significant events during test runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobservationcenter)*