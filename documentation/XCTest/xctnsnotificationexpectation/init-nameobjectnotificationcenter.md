# init(name:object:notificationCenter:)

**Framework**: XCTest  
**Kind**: init

Creates an expectation that is fulfilled when an `NSNotification` is posted from a specific notification center, optionally by a specific object.

## Declaration

```swift
init(name notificationName: NSNotification.Name, object: Any?, notificationCenter: NotificationCenter)
```

## Parameters

- `notificationName`: The notification name to watch for.
- `object`: The object by which the notification must be posted, or nil if the notification can be posted by any object.
- `notificationCenter`: The   from which the notification must be posted.

## See Also

- [convenience init(name: NSNotification.Name)](xctnsnotificationexpectation/init(name:).md)
  Creates an expectation that is fulfilled when an `NSNotification` is posted from the default notification center by any object.
- [convenience init(name: NSNotification.Name, object: Any?)](xctnsnotificationexpectation/init(name:object:).md)
  Creates an expectation that is fulfilled when an `NSNotification` is posted from the default notification center by a specific object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnsnotificationexpectation/init(name:object:notificationcenter:))*