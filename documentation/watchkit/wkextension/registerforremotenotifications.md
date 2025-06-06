# registerForRemoteNotifications()

**Framework**: Watchkit  
**Kind**: method

Register to receive remote notifications from the Apple Push Notification service (APNs).

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
func registerForRemoteNotifications()
```

#### Discussion

Before calling this method, you must enable your WatchKit extension’s Push Notification capability, as described in [`Enable push notifications`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devdfd3d04a1).

Call this method to register a device with APNs. If registration succeeds, the system calls your extension delegate’s [`didRegisterForRemoteNotifications(withDeviceToken:)`](wkextensiondelegate/didregisterforremotenotifications(withdevicetoken:).md) method and passes it a device token. Pass this token to the provider server you use to generate remote notifications for this device. If registration fails, the system calls your extension delegate’s [`didFailToRegisterForRemoteNotificationsWithError(_:)`](wkextensiondelegate/didfailtoregisterforremotenotificationswitherror(_:).md) method instead.

> ❗ **Important**:  Device tokens may change, so don’t cache the device token on the device. Instead, register for remote notifications every time your app launches. If the device token hasn’t changed, registration happens quickly.

 Device tokens may change, so don’t cache the device token on the device. Instead, register for remote notifications every time your app launches. If the device token hasn’t changed, registration happens quickly.

To display alerts, play sounds, or perform other user-facing actions, you must also request authorization using the [`UNUserNotificationCenter`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenter) class’s [`requestAuthorization(options:completionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenter/requestAuthorization(options:completionHandler:)) method. If you do not request and receive authorization for your app’s interactions, the system delivers all remote notifications to your app silently.

If your watchOS app has an iOS companion, always send notifications to both watchOS and the paired iOS device. As long as the payloads are identical, the system recognizes the duplicates, and only displays one notification to the user.

For more information on setting up remote notifications, see [`Setting up a remote notification server`](https://developer.apple.com/documentation/UserNotifications/setting-up-a-remote-notification-server) and [`Registering your app with APNs`](https://developer.apple.com/documentation/UserNotifications/registering-your-app-with-apns).

## See Also

- [func unregisterForRemoteNotifications()](wkextension/unregisterforremotenotifications.md)
  Unregister for all remote notifications received from Apple Push Notification service (APNs).
- [var isRegisteredForRemoteNotifications: Bool](wkextension/isregisteredforremotenotifications.md)
  A Boolean value that indicates if the app has successfully registered for remote notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/registerforremotenotifications())*