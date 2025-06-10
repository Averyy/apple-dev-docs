# criticalAlert

**Framework**: User Notifications  
**Kind**: property

The ability to play sounds for critical alerts.

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
static var criticalAlert: UNAuthorizationOptions { get }
```

#### Discussion

Critical alerts ignore the mute switch and Do Not Disturb; the system plays a critical alert’s sound regardless of the device’s mute or Do Not Disturb settings. You can specify a custom sound and volume.

Critical alerts require a special entitlement issued by Apple.

## See Also

- [static var badge: UNAuthorizationOptions](unauthorizationoptions/badge.md)
  The ability to update the app’s badge.
- [static var sound: UNAuthorizationOptions](unauthorizationoptions/sound.md)
  The ability to play sounds.
- [static var alert: UNAuthorizationOptions](unauthorizationoptions/alert.md)
  The ability to display alerts.
- [static var carPlay: UNAuthorizationOptions](unauthorizationoptions/carplay.md)
  The ability to display notifications in a CarPlay environment.
- [static var providesAppNotificationSettings: UNAuthorizationOptions](unauthorizationoptions/providesappnotificationsettings.md)
  An option indicating the system should display a button for in-app notification settings.
- [static var provisional: UNAuthorizationOptions](unauthorizationoptions/provisional.md)
  The ability to post noninterrupting notifications provisionally to the Notification Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unauthorizationoptions/criticalalert)*