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
- [WKBackgroundFetchResult.failed](failed.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkbackgroundfetchresult/failed))
  The download attempt failed.
- [WKBackgroundFetchResult.newData](newdata.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkbackgroundfetchresult/newdata))
  The download attempt succeeded.
- [WKBackgroundFetchResult.noData](nodata.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkbackgroundfetchresult/nodata))
  The notification has no associated content.
### Initializers
- [init?(rawValue: UInt)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkbackgroundfetchresult/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [func didRegisterForRemoteNotifications(withDeviceToken: Data)](didregisterforremotenotifications(withdevicetoken:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/didregisterforremotenotifications(withdevicetoken:)))
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func didFailToRegisterForRemoteNotificationsWithError(any Error)](didfailtoregisterforremotenotificationswitherror(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/didfailtoregisterforremotenotificationswitherror(_:)))
  Tells the delegate that Apple Push Notification service (APNs) can’t successfully complete the registration process.
- [func didReceiveRemoteNotification([AnyHashable : Any], fetchCompletionHandler: (WKBackgroundFetchResult) -> Void)](didreceiveremotenotification(_:fetchcompletionhandler:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/didreceiveremotenotification(_:fetchcompletionhandler:)))
  Tells the delegate that a background notification has arrived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkbackgroundfetchresult)*