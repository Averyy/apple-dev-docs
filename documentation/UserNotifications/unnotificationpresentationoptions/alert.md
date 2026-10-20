# alert

**Framework**: User Notifications  
**Kind**: property  
**Role**: Type Property

Display the alert using the content provided by the notification.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0
- iPadOS 10.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.14+ - Deprecated in 11.0
- tvOS 10.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

> **Deprecated**: Use [`list`](./list.md) and [`banner`](./banner.md) instead.

## Declaration

```swift
static var alert: UNNotificationPresentationOptions { get }
```

```c
UNNotificationPresentationOptionAlert
```

## See Also

### Constants
- [static var badge: UNNotificationPresentationOptions](./badge.md)
  Apply the notification’s badge value to the app’s icon.
- [static var banner: UNNotificationPresentationOptions](./banner.md)
  Present the notification as a banner.
- [static var list: UNNotificationPresentationOptions](./list.md)
  Show the notification in Notification Center.
- [static var sound: UNNotificationPresentationOptions](./sound.md)
  Play the sound associated with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptions/alert)*