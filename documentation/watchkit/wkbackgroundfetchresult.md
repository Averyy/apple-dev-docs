# WKBackgroundFetchResult

**Framework**: WatchKit  
**Kind**: enum

The result of an attempt to download the content associated with a remote notification.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
enum WKBackgroundFetchResult
```

## Topics

### Fetch Results
- [WKBackgroundFetchResult.failed](wkbackgroundfetchresult/failed.md)
  The download attempt failed.
- [WKBackgroundFetchResult.newData](wkbackgroundfetchresult/newdata.md)
  The download attempt succeeded.
- [WKBackgroundFetchResult.noData](wkbackgroundfetchresult/nodata.md)
  The notification has no associated content.
### Initializers
- [init?(rawValue: UInt)](wkbackgroundfetchresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func didRegisterForRemoteNotifications(withDeviceToken: Data)](wkapplicationdelegate/didregisterforremotenotifications(withdevicetoken:).md)
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func didFailToRegisterForRemoteNotificationsWithError(any Error)](wkapplicationdelegate/didfailtoregisterforremotenotificationswitherror(_:).md)
  Tells the delegate that Apple Push Notification service (APNs) can’t successfully complete the registration process.
- [func didReceiveRemoteNotification([AnyHashable : Any], fetchCompletionHandler: (WKBackgroundFetchResult) -> Void)](wkapplicationdelegate/didreceiveremotenotification(_:fetchcompletionhandler:).md)
  Tells the delegate that a background notification has arrived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkbackgroundfetchresult)*