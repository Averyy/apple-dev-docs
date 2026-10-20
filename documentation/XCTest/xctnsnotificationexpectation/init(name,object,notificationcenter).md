# init(name:object:notificationCenter:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an expectation that is fulfilled when an `NSNotification` is posted from a specific notification center, optionally by a specific object.

## Declaration

```swift
init(name notificationName: NSNotification.Name, object: Any?, notificationCenter: NotificationCenter)
```

```objc
- (instancetype) initWithName:(NSNotificationName) notificationName object:(id) object notificationCenter:(NSNotificationCenter *) notificationCenter;
```

## Parameters

- `notificationName`: The notification name to watch for.
- `object`: The object by which the notification must be posted, or nil if the notification can be posted by any object.
- `notificationCenter`: The [`NotificationCenter`](../../Foundation/notificationcenter.md) from which the notification must be posted.

## See Also

### Creating NSNotification Expectations
- [convenience init(name: NSNotification.Name)](./init%28name%29.md)
  Creates an expectation that is fulfilled when an `NSNotification` is posted from the default notification center by any object.
- [convenience init(name: NSNotification.Name, object: Any?)](./init%28name,object%29.md)
  Creates an expectation that is fulfilled when an `NSNotification` is posted from the default notification center by a specific object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnsnotificationexpectation/init(name:object:notificationcenter:))*