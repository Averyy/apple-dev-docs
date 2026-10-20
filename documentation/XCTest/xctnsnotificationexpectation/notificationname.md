# notificationName

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The name of the notification that the expectation is waiting for.

## Declaration

```swift
var notificationName: NSNotification.Name { get }
```

```objc
@property (copy, readonly) NSNotificationName notificationName;
```

## See Also

### Expectation Properties
- [var observedObject: Any?](./observedobject.md)
  The object by which the notification must be posted, or nil if the notification can be posted by any object.
- [var notificationCenter: NotificationCenter](./notificationcenter.md)
  The notification center from which the notification must be posted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnsnotificationexpectation/notificationname)*