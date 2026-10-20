# registerForRemoteNotifications()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Register to receive remote notifications from the Apple Push Notification service (APNs).

**Availability**:
- watchOS 7.0+

## Declaration

```swift
func registerForRemoteNotifications()
```

```objc
- (void) registerForRemoteNotifications;
```

#### Discussion

Before calling this method, you must enable your WatchKit extension’s Push Notification capability, as described in [Enable push notifications](https://help.apple.com/xcode/mac/current/#/devdfd3d04a1).

Call this method to register a device with APNs. If registration succeeds, the system calls your app delegate’s [`didRegisterForRemoteNotifications(withDeviceToken:)`](../wkapplicationdelegate/didregisterforremotenotifications%28withdevicetoken%29.md) method and passes it a device token. Pass this token to the provider server you use to generate remote notifications for this device. If registration fails, the system calls your app delegate’s [`didFailToRegisterForRemoteNotificationsWithError(_:)`](../wkapplicationdelegate/didfailtoregisterforremotenotificationswitherror%28_%29.md) method instead.

> ❗ **Important**:  Device tokens may change, so don’t cache the device token on the device. Instead, register for remote notifications every time your app launches. If the device token hasn’t changed, registration happens quickly.

To display alerts, play sounds, or perform other user-facing actions, you must also request authorization using the [`UNUserNotificationCenter`](../../UserNotifications/unusernotificationcenter.md) class’s [`requestAuthorization(options:completionHandler:)`](../../UserNotifications/unusernotificationcenter/requestauthorization%28options,completionhandler%29.md) method. If you don’t request and receive authorization for your app’s interactions, the system delivers all remote notifications to your app silently.

If your watchOS app has an iOS companion, always send notifications to both watchOS and the paired iOS device. As long as the payloads are identical, the system recognizes the duplicates, and only displays one notification to the user.

For more information on setting up remote notifications, see [Setting up a remote notification server](../../UserNotifications/setting-up-a-remote-notification-server.md) and [Registering your app with APNs](../../UserNotifications/registering-your-app-with-apns.md).

## See Also

### Registering for remote notifications
- [func unregisterForRemoteNotifications()](./unregisterforremotenotifications%28%29.md)
  Unregister for all remote notifications received from Apple Push Notification service (APNs).
- [var isRegisteredForRemoteNotifications: Bool](./isregisteredforremotenotifications.md)
  A Boolean value that indicates if the app has successfully registered for remote notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/registerforremotenotifications())*