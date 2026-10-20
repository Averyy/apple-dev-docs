# isRegisteredForRemoteNotifications

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the app has successfully registered for remote notifications.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
var isRegisteredForRemoteNotifications: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isRegisteredForRemoteNotifications) BOOL registeredForRemoteNotifications;
```

#### Discussion

This method indicates whether your app successfully registered for remote notifications using the [`registerForRemoteNotifications()`](./registerforremotenotifications%28%29.md) method. It also takes into account the notification permissions set by the user. It doesn’t give any indication about whether remote notifications are available.

## See Also

### Registering for remote notifications
- [func registerForRemoteNotifications()](./registerforremotenotifications%28%29.md)
  Register to receive remote notifications from the Apple Push Notification service (APNs).
- [func unregisterForRemoteNotifications()](./unregisterforremotenotifications%28%29.md)
  Unregister for all remote notifications received from Apple Push Notification service (APNs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/isregisteredforremotenotifications)*