# didReceiveRemoteNotification(_:fetchCompletionHandler:)

**Framework**: WatchKit  
**Kind**: method

Tells the delegate that a background notification has arrived.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
optional func didReceiveRemoteNotification(_ userInfo: [AnyHashable : Any]) async -> WKBackgroundFetchResult
```

#### Discussion

Implement this method to process incoming background notifications. The system launches your app or wakes it from the suspended state when the notification arrives, and your app receives a brief amount of time to run in the background.

Use the background execution time to process the notification and download its associated content. As soon as you finish processing the notification, you must call its fetch completion handler. Your app has up to 30 seconds of wall-clock time to process the notification and call the handler or the system terminates your app. Always call the handler as quickly as possible, because the system tracks the elapsed time, power usage, and data costs for your app’s background notifications.

Background notifications are low priority, and the system limits these notifications based on the power considerations of the target device. APNs doesn’t guarantee that a device will receive push notifications, and apps that use significant amounts of power or time when processing background notifications may not receive background time to process future notifications.

For more information, see [`Pushing background updates to your App`](https://developer.apple.com/documentation/UserNotifications/pushing-background-updates-to-your-app).

## Parameters

- `userInfo`: A dictionary that contains data from the notification payload. The notification originates as a JSON-defined dictionary that WatchKit converts to a dictionary type; the dictionary may contain only property-list objects plus  . For more information about the contents of the notification payload, see  .
- `completionHandler`: The block to execute after the download operation completes. When calling this block, pass the fetch result that best describes your download operation. For a list of possible values, see the   type.

## See Also

- [func didRegisterForRemoteNotifications(withDeviceToken: Data)](wkapplicationdelegate/didregisterforremotenotifications(withdevicetoken:).md)
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func didFailToRegisterForRemoteNotificationsWithError(any Error)](wkapplicationdelegate/didfailtoregisterforremotenotificationswitherror(_:).md)
  Tells the delegate that Apple Push Notification service (APNs) can’t successfully complete the registration process.
- [enum WKBackgroundFetchResult](wkbackgroundfetchresult.md)
  The result of an attempt to download the content associated with a remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/didreceiveremotenotification(_:fetchcompletionhandler:))*