# didRegisterForRemoteNotifications(withDeviceToken:)

**Framework**: Watchkit  
**Kind**: method

Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor optional func didRegisterForRemoteNotifications(withDeviceToken deviceToken: Data)
```

## Overview

WatchKit calls this method after it successfully registers your app with APNs. In your implementation, send the contents of the `deviceToken` parameter to the server you use to generate remote notifications. Never cache the device token locally on the user’s device. Device tokens can change periodically, so caching the value risks sending an invalid token to your server.

Typically, the system calls this method only after you call your [`WKExtension`](https://developer.apple.com/documentation/watchkit/wkextension) object’s [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/watchkit/wkextension/registerforremotenotifications()) method, but WatchKit may call it under other rare circumstances. For example, WatchKit calls the method when the user launches an app after setting up the watch using a different device’s backup. In this case, the app doesn’t know the new device’s token until the user launches it.

## Parameters

- `deviceToken`: The length of APNs device tokens can vary. Do not hardcode the token’s size in your app.

## See Also

- @MainActor optional func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: any Error) ([Apple Docs](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didFailToRegisterForRemoteNotificationsWithError:)))
- @MainActor optional func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any]) ([Apple Docs](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didReceiveRemoteNotification:)))
- @MainActor func registerForRemoteNotifications() ([Apple Docs](https://developer.apple.com/documentation/UIKit/UIApplication/registerForRemoteNotifications()))
- [func didFailToRegisterForRemoteNotificationsWithError(any Error)](didfailtoregisterforremotenotificationswitherror(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didfailtoregisterforremotenotificationswitherror(_:)))
- [func didReceiveRemoteNotification([AnyHashable : Any], fetchCompletionHandler: (WKBackgroundFetchResult) -> Void)](didreceiveremotenotification(_:fetchcompletionhandler:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceiveremotenotification(_:fetchcompletionhandler:)))
- [enum WKBackgroundFetchResult](wkbackgroundfetchresult.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkbackgroundfetchresult))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didregisterforremotenotifications(withdevicetoken:))*