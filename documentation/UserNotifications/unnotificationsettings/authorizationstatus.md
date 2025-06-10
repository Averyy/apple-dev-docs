# authorizationStatus

**Framework**: User Notifications  
**Kind**: property

The app’s ability to schedule and receive local and remote notifications.

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
var authorizationStatus: UNAuthorizationStatus { get }
```

#### Discussion

When the value of this property is [`UNAuthorizationStatus.authorized`](unauthorizationstatus/authorized.md), your app is allowed to schedule and receive local and remote notifications. When authorized, use the [`alertSetting`](unnotificationsettings/alertsetting.md), [`badgeSetting`](unnotificationsettings/badgesetting.md), and [`soundSetting`](unnotificationsettings/soundsetting.md) properties to specify which types of interactions are allowed. When the value of the property is [`UNAuthorizationStatus.denied`](unauthorizationstatus/denied.md), the system doesn’t deliver notifications to your app, and the system ignores any attempts to schedule local notifications.

The value of this property is [`UNAuthorizationStatus.notDetermined`](unauthorizationstatus/notdetermined.md) if your app has never requested authorization using the [`requestAuthorization(options:completionHandler:)`](unusernotificationcenter/requestauthorization(options:completionhandler:).md) method.

## See Also

- [enum UNAuthorizationStatus](unauthorizationstatus.md)
  Constants indicating whether the app is allowed to schedule notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsettings/authorizationstatus)*