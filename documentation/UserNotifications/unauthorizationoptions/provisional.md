# provisional

**Framework**: User Notifications  
**Kind**: property  
**Role**: Type Property

The ability to post noninterrupting notifications provisionally to the Notification Center.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
static var provisional: UNAuthorizationOptions { get }
```

```c
UNAuthorizationOptionProvisional
```

## Mentions

- [Asking permission to use notifications](../asking-permission-to-use-notifications.md)

## See Also

### Options
- [static var badge: UNAuthorizationOptions](./badge.md)
  The ability to update the app’s badge.
- [static var sound: UNAuthorizationOptions](./sound.md)
  The ability to play sounds.
- [static var alert: UNAuthorizationOptions](./alert.md)
  The ability to display alerts.
- [static var carPlay: UNAuthorizationOptions](./carplay.md)
  The ability to display notifications in a CarPlay environment.
- [static var criticalAlert: UNAuthorizationOptions](./criticalalert.md)
  The ability to play sounds for critical alerts.
- [static var providesAppNotificationSettings: UNAuthorizationOptions](./providesappnotificationsettings.md)
  An option indicating the system should display a button for in-app notification settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unauthorizationoptions/provisional)*