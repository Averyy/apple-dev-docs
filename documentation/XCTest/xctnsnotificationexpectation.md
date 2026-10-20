# XCTNSNotificationExpectation

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

An expectation that is fulfilled when an expected `NSNotification` is received.

## Declaration

```swift
class XCTNSNotificationExpectation
```

```objc
@interface XCTNSNotificationExpectation : XCTestExpectation
```

## Topics

### Creating NSNotification Expectations
- [convenience init(name: NSNotification.Name)](./xctnsnotificationexpectation/init%28name%29.md)
  Creates an expectation that is fulfilled when an `NSNotification` is posted from the default notification center by any object.
- [convenience init(name: NSNotification.Name, object: Any?)](./xctnsnotificationexpectation/init%28name,object%29.md)
  Creates an expectation that is fulfilled when an `NSNotification` is posted from the default notification center by a specific object.
- [init(name: NSNotification.Name, object: Any?, notificationCenter: NotificationCenter)](./xctnsnotificationexpectation/init%28name,object,notificationcenter%29.md)
  Creates an expectation that is fulfilled when an `NSNotification` is posted from a specific notification center, optionally by a specific object.
### Expectation Properties
- [var notificationName: NSNotification.Name](./xctnsnotificationexpectation/notificationname.md)
  The name of the notification that the expectation is waiting for.
- [var observedObject: Any?](./xctnsnotificationexpectation/observedobject.md)
  The object by which the notification must be posted, or nil if the notification can be posted by any object.
- [var notificationCenter: NotificationCenter](./xctnsnotificationexpectation/notificationcenter.md)
  The notification center from which the notification must be posted.
### Custom Notification Evaluation
- [var handler: XCTNSNotificationExpectation.Handler?](./xctnsnotificationexpectation/handler-swift.property.md)
  An optional handler that performs custom evaluation of matching notifications.
- [XCTNSNotificationExpectation.Handler](./xctnsnotificationexpectation/handler-swift.typealias.md)
  A custom handler to be called when a matching notification is received.

## Relationships

### Inherits From
- [XCTestExpectation](./xctestexpectation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Notification-Based Expectations
- [class XCTDarwinNotificationExpectation](./xctdarwinnotificationexpectation.md)
  An expectation that is fulfilled when an expected Darwin notification is received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnsnotificationexpectation)*