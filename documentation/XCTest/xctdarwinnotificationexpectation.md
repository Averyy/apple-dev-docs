# XCTDarwinNotificationExpectation

**Framework**: Xctest  
**Kind**: class

An expectation that is fulfilled when an expected Darwin notification is received.

## Declaration

```swift
class XCTDarwinNotificationExpectation
```

#### Overview

If a custom [`handler`](xctdarwinnotificationexpectation/handler-swift.property.md) value is not provided, the expectation will be fulfilled as soon as a matching Darwin notification is received from any process.

## Topics

### Creating Darwin Notification Expectations
- [init(notificationName: String)](xctdarwinnotificationexpectation/init(notificationname:).md)
  Creates an expectation that waits for a Darwin notification with the specified name to be posted.
### Expectation Properties
- [var notificationName: String](xctdarwinnotificationexpectation/notificationname.md)
  The name of the notification that the expectation is waiting for.
### Custom Notification Evaluation
- [var handler: XCTDarwinNotificationExpectation.Handler?](xctdarwinnotificationexpectation/handler-swift.property.md)
  An optional handler that performs custom evaluation of matching notifications.
- [XCTDarwinNotificationExpectation.Handler](xctdarwinnotificationexpectation/handler-swift.typealias.md)
  A custom handler to be called when a matching notification is received.

## Relationships

### Inherits From
- [XCTestExpectation](xctestexpectation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class XCTNSNotificationExpectation](xctnsnotificationexpectation.md)
  An expectation that is fulfilled when an expected `NSNotification` is received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctdarwinnotificationexpectation)*