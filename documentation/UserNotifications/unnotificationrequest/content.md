# content

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The content associated with the notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var content: UNNotificationContent { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) UNNotificationContent * content;
```

*macOS*

```objc
@property (atomic, copy, readonly) UNNotificationContent * content;
```

## Discussion

Use this property to access the contents of the notification.

## See Also

### Getting the Request Details
- [var identifier: String](./identifier.md)
  The unique identifier for this notification request.
- [var trigger: UNNotificationTrigger?](./trigger.md)
  The conditions that trigger the delivery of the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationrequest/content)*