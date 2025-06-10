# request

**Framework**: User Notifications  
**Kind**: property

The notification request containing the payload and trigger condition for the notification.

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
var request: UNNotificationRequest { get }
```

#### Discussion

For local notifications, the request object is a copy of the one you originally configured. For remote notifications, the system synthesizes the request object from information received from Apple Push Notification service.

## See Also

- [var date: Date](unnotification/date.md)
  The delivery date of the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotification/request)*