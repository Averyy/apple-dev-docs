# didFailToRegisterForRemoteNotificationsWithError(_:)

**Framework**: WatchKit  
**Kind**: method

Tells the delegate that Apple Push Notification service (APNs) cannot successfully complete the registration process.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
optional func didFailToRegisterForRemoteNotificationsWithError(_ error: any Error)
```

#### Discussion

WatchKit calls this method if it was unable to register your app with APNs or if your app is not properly configured for remote notifications. For example, WatchKit might call this method if you didn’t enable your WatchKit extension’s Push Notification capability.** **For more information about how to set up and send remote notifications in your app, see [`Setting up a remote notification server`](https://developer.apple.com/documentation/UserNotifications/setting-up-a-remote-notification-server) and [`Registering your app with APNs`](https://developer.apple.com/documentation/UserNotifications/registering-your-app-with-apns).

In your implementation, you can check the error type, and try to register again later.

## Parameters

- `error`: An error object that contains information about why the registration failed. The app can choose to display this information to the user.

## See Also

- [func didRegisterForRemoteNotifications(withDeviceToken: Data)](didregisterforremotenotifications(withdevicetoken:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didregisterforremotenotifications(withdevicetoken:)))
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func didReceiveRemoteNotification([AnyHashable : Any], fetchCompletionHandler: (WKBackgroundFetchResult) -> Void)](didreceiveremotenotification(_:fetchcompletionhandler:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceiveremotenotification(_:fetchcompletionhandler:)))
  Tells the delegate that a background notification has arrived.
- [enum WKBackgroundFetchResult](wkbackgroundfetchresult.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkbackgroundfetchresult))
  The result of an attempt to download the content associated with a remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didfailtoregisterforremotenotificationswitherror(_:))*