# didRegisterForRemoteNotifications(withDeviceToken:)

**Framework**: WatchKit  
**Kind**: method

Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
optional func didRegisterForRemoteNotifications(withDeviceToken deviceToken: Data)
```

#### Discussion

WatchKit calls this method after it successfully registers your app with APNs. In your implementation, send the contents of the `deviceToken` parameter to the server you use to generate remote notifications. Never cache the device token locally on the user’s device. Device tokens can change periodically, so caching the value risks sending an invalid token to your server.

Typically, the system calls this method only after you call your [`WKExtension`](wkextension.md) object’s [`registerForRemoteNotifications()`](wkextension/registerforremotenotifications().md) method, but WatchKit may call it under other rare circumstances. For example, WatchKit calls the method when the user launches an app after setting up the watch using a different device’s backup. In this case, the app doesn’t know the new device’s token until the user launches it.

## Parameters

- `deviceToken`: The length of APNs device tokens can vary. Do not hardcode the token’s size in your app.

## See Also

- [@MainActor optional func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: any Error)](../UIKit/UIApplicationDelegate/application(_:didFailToRegisterForRemoteNotificationsWithError:).md)
  Tells the delegate when Apple Push Notification service cannot successfully complete the registration process.
- [@MainActor optional func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any])](../UIKit/UIApplicationDelegate/application(_:didReceiveRemoteNotification:).md)
  Called when your app has received a remote notification.
- [@MainActor func registerForRemoteNotifications()](../UIKit/UIApplication/registerForRemoteNotifications.md)
  Registers to receive remote notifications through Apple Push Notification service.
- [func didFailToRegisterForRemoteNotificationsWithError(any Error)](wkextensiondelegate/didfailtoregisterforremotenotificationswitherror(_:).md)
  Tells the delegate that Apple Push Notification service (APNs) cannot successfully complete the registration process.
- [func didReceiveRemoteNotification([AnyHashable : Any], fetchCompletionHandler: (WKBackgroundFetchResult) -> Void)](wkextensiondelegate/didreceiveremotenotification(_:fetchcompletionhandler:).md)
  Tells the delegate that a background notification has arrived.
- [enum WKBackgroundFetchResult](wkbackgroundfetchresult.md)
  The result of an attempt to download the content associated with a remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didregisterforremotenotifications(withdevicetoken:))*