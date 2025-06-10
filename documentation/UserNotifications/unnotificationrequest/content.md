# content

**Framework**: User Notifications  
**Kind**: property

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

#### Discussion

Use this property to access the contents of the notification.

## See Also

- [var identifier: String](unnotificationrequest/identifier.md)
  The unique identifier for this notification request.
- [var trigger: UNNotificationTrigger?](unnotificationrequest/trigger.md)
  The conditions that trigger the delivery of the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationrequest/content)*