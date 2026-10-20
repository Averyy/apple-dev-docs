# authorizationStatus

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) UNAuthorizationStatus authorizationStatus;
```

*macOS*

```objc
@property (atomic, readonly) UNAuthorizationStatus authorizationStatus;
```

#### Discussion

When the value of this property is [`UNAuthorizationStatus.authorized`](../unauthorizationstatus/authorized.md), your app is allowed to schedule and receive local and remote notifications. When authorized, use the [`alertSetting`](./alertsetting.md), [`badgeSetting`](./badgesetting.md), and [`soundSetting`](./soundsetting.md) properties to specify which types of interactions are allowed. When the value of the property is [`UNAuthorizationStatus.denied`](../unauthorizationstatus/denied.md), the system doesn’t deliver notifications to your app, and the system ignores any attempts to schedule local notifications.

The value of this property is [`UNAuthorizationStatus.notDetermined`](../unauthorizationstatus/notdetermined.md) if your app has never requested authorization using the [`requestAuthorization(options:completionHandler:)`](../unusernotificationcenter/requestauthorization%28options,completionhandler%29.md) method.

## See Also

### Getting the Authorization Status
- [enum UNAuthorizationStatus](../unauthorizationstatus.md)
  Constants indicating whether the app is allowed to schedule notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsettings/authorizationstatus)*