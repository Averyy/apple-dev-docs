# isRegisteredForRemoteNotifications

**Framework**: Watchkit  
**Kind**: property

A Boolean value that indicates if the app has successfully registered for remote notifications.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
var isRegisteredForRemoteNotifications: Bool { get }
```

#### Discussion

This method indicates whether your app successfully registered for remote notifications using the [`registerForRemoteNotifications()`](wkextension/registerforremotenotifications().md) method. It also takes into account the notification permissions set by the user. It does not give any indication about whether remote notifications are available.

## See Also

- [func registerForRemoteNotifications()](wkextension/registerforremotenotifications.md)
  Register to receive remote notifications from the Apple Push Notification service (APNs).
- [func unregisterForRemoteNotifications()](wkextension/unregisterforremotenotifications.md)
  Unregister for all remote notifications received from Apple Push Notification service (APNs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/isregisteredforremotenotifications)*