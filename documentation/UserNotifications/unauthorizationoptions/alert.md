# alert

**Framework**: User Notifications  
**Kind**: property  
**Role**: Type Property

The ability to display alerts.

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
static var alert: UNAuthorizationOptions { get }
```

```c
UNAuthorizationOptionAlert
```

## See Also

### Options
- [static var badge: UNAuthorizationOptions](./badge.md)
  The ability to update the app’s badge.
- [static var sound: UNAuthorizationOptions](./sound.md)
  The ability to play sounds.
- [static var carPlay: UNAuthorizationOptions](./carplay.md)
  The ability to display notifications in a CarPlay environment.
- [static var criticalAlert: UNAuthorizationOptions](./criticalalert.md)
  The ability to play sounds for critical alerts.
- [static var providesAppNotificationSettings: UNAuthorizationOptions](./providesappnotificationsettings.md)
  An option indicating the system should display a button for in-app notification settings.
- [static var provisional: UNAuthorizationOptions](./provisional.md)
  The ability to post noninterrupting notifications provisionally to the Notification Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unauthorizationoptions/alert)*