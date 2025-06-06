# UNAuthorizationOptions

**Framework**: Usernotifications  
**Kind**: struct

Options that determine the authorized features of local and remote notifications.

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
struct UNAuthorizationOptions
```

## Topics

### Options
- [static var badge: UNAuthorizationOptions](unauthorizationoptions/badge.md)
  The ability to update the app’s badge.
- [static var sound: UNAuthorizationOptions](unauthorizationoptions/sound.md)
  The ability to play sounds.
- [static var alert: UNAuthorizationOptions](unauthorizationoptions/alert.md)
  The ability to display alerts.
- [static var carPlay: UNAuthorizationOptions](unauthorizationoptions/carplay.md)
  The ability to display notifications in a CarPlay environment.
- [static var criticalAlert: UNAuthorizationOptions](unauthorizationoptions/criticalalert.md)
  The ability to play sounds for critical alerts.
- [static var providesAppNotificationSettings: UNAuthorizationOptions](unauthorizationoptions/providesappnotificationsettings.md)
  An option indicating the system should display a button for in-app notification settings.
- [static var provisional: UNAuthorizationOptions](unauthorizationoptions/provisional.md)
  The ability to post noninterrupting notifications provisionally to the Notification Center.
### Initializers
- [init(rawValue: UInt)](unauthorizationoptions/init(rawvalue:).md)
  Initializes an authorization options constant using the specified raw value.
### Deprecated
- [static var announcement: UNAuthorizationOptions](unauthorizationoptions/announcement.md)
  The ability for Siri to automatically read out messages over AirPods.
- [static var timeSensitive: UNAuthorizationOptions](unauthorizationoptions/timesensitive.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func requestAuthorization(options: UNAuthorizationOptions, completionHandler: (Bool, (any Error)?) -> Void)](unusernotificationcenter/requestauthorization(options:completionhandler:).md)
  Requests a person’s authorization to allow local and remote notifications for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unauthorizationoptions)*