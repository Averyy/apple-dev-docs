# trigger

**Framework**: User Notifications  
**Kind**: property

The conditions that trigger the delivery of the notification.

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
var trigger: UNNotificationTrigger? { get }
```

#### Discussion

For notifications that the system has delivered, use this property to determine what caused the delivery to occur. For remote notifications, this property contains a [`UNPushNotificationTrigger`](unpushnotificationtrigger.md) object. For other notifications, the system sets this type using the trigger condition specified in the original request.

## See Also

- [var identifier: String](unnotificationrequest/identifier.md)
  The unique identifier for this notification request.
- [var content: UNNotificationContent](unnotificationrequest/content.md)
  The content associated with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationrequest/trigger)*