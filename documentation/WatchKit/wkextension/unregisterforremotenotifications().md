# unregisterForRemoteNotifications()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Unregister for all remote notifications received from Apple Push Notification service (APNs).

**Availability**:
- watchOS 6.0+ - Deprecated in 9.2

## Declaration

```swift
func unregisterForRemoteNotifications()
```

```objc
- (void) unregisterForRemoteNotifications;
```

#### Discussion

Use this method to unregister from all remote notifications; for example, unregister to stop receiving notifications when the user logs out of their account.

## See Also

### Related Documentation
- [func registerForRemoteNotifications()](../../UIKit/uiapplication/registerforremotenotifications%28%29.md)
  Registers to receive remote notifications through Apple Push Notification service.
### Registering for remote notifications
- [func registerForRemoteNotifications()](./registerforremotenotifications%28%29.md)
  Register to receive remote notifications from the Apple Push Notification service (APNs).
- [var isRegisteredForRemoteNotifications: Bool](./isregisteredforremotenotifications.md)
  A Boolean value that indicates if the app has successfully registered for remote notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/unregisterforremotenotifications())*