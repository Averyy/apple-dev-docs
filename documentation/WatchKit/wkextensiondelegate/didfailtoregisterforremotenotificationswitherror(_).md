# didFailToRegisterForRemoteNotificationsWithError(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that Apple Push Notification service (APNs) cannot successfully complete the registration process.

**Availability**:
- watchOS 6.0+ - Deprecated in 9.2

## Declaration

```swift
optional func didFailToRegisterForRemoteNotificationsWithError(_ error: any Error)
```

```objc
- (void) didFailToRegisterForRemoteNotificationsWithError:(NSError *) error;
```

#### Discussion

WatchKit calls this method if it was unable to register your app with APNs or if your app is not properly configured for remote notifications. For example, WatchKit might call this method if you didn’t enable your WatchKit extension’s Push Notification capability.** **For more information about how to set up and send remote notifications in your app, see [Setting up a remote notification server](../../UserNotifications/setting-up-a-remote-notification-server.md) and [Registering your app with APNs](../../UserNotifications/registering-your-app-with-apns.md).

In your implementation, you can check the error type, and try to register again later.

## Parameters

- `error`: An error object that contains information about why the registration failed. The app can choose to display this information to the user.

## See Also

### Managing remote notifications
- [func didRegisterForRemoteNotifications(withDeviceToken: Data)](./didregisterforremotenotifications%28withdevicetoken%29.md)
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func didReceiveRemoteNotification([AnyHashable : Any], fetchCompletionHandler: (WKBackgroundFetchResult) -> Void)](./didreceiveremotenotification%28_,fetchcompletionhandler%29.md)
  Tells the delegate that a background notification has arrived.
- [enum WKBackgroundFetchResult](../wkbackgroundfetchresult.md)
  The result of an attempt to download the content associated with a remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didfailtoregisterforremotenotificationswitherror(_:))*