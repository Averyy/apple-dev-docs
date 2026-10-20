# observedObject

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The object by which the notification must be posted, or nil if the notification can be posted by any object.

## Declaration

```swift
var observedObject: Any? { get }
```

```objc
@property (strong, readonly, nullable) id observedObject;
```

## See Also

### Expectation Properties
- [var notificationName: NSNotification.Name](./notificationname.md)
  The name of the notification that the expectation is waiting for.
- [var notificationCenter: NotificationCenter](./notificationcenter.md)
  The notification center from which the notification must be posted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnsnotificationexpectation/observedobject)*