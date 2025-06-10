# unregisterForRemoteNotifications()

**Framework**: WatchKit  
**Kind**: method

Unregister for all remote notifications received from Apple Push Notification service (APNs).

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
func unregisterForRemoteNotifications()
```

#### Discussion

Use this method to unregister from all remote notifications; for example, unregister to stop receiving notifications when the user logs out of their account.

## See Also

- [@MainActor func registerForRemoteNotifications()](../UIKit/UIApplication/registerForRemoteNotifications.md)
  Registers to receive remote notifications through Apple Push Notification service.
- [func registerForRemoteNotifications()](wkextension/registerforremotenotifications.md)
  Register to receive remote notifications from the Apple Push Notification service (APNs).
- [var isRegisteredForRemoteNotifications: Bool](wkextension/isregisteredforremotenotifications.md)
  A Boolean value that indicates if the app has successfully registered for remote notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/unregisterforremotenotifications())*