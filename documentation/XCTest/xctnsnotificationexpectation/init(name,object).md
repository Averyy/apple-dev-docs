# init(name:object:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an expectation that is fulfilled when an `NSNotification` is posted from the default notification center by a specific object.

## Declaration

```swift
convenience init(name notificationName: NSNotification.Name, object: Any?)
```

```objc
- (instancetype) initWithName:(NSNotificationName) notificationName object:(id) object;
```

## Parameters

- `notificationName`: The notification name to watch for.
- `object`: The object by which the notification must be posted.

## See Also

### Creating NSNotification Expectations
- [convenience init(name: NSNotification.Name)](./init%28name%29.md)
  Creates an expectation that is fulfilled when an `NSNotification` is posted from the default notification center by any object.
- [init(name: NSNotification.Name, object: Any?, notificationCenter: NotificationCenter)](./init%28name,object,notificationcenter%29.md)
  Creates an expectation that is fulfilled when an `NSNotification` is posted from a specific notification center, optionally by a specific object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnsnotificationexpectation/init(name:object:))*