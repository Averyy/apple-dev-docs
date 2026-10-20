# WKBackgroundFetchResult

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

The result of an attempt to download the content associated with a remote notification.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
enum WKBackgroundFetchResult
```

```c
enum WKBackgroundFetchResult : NSUInteger;
```

## Topics

### Fetch Results
- [WKBackgroundFetchResult.failed](./wkbackgroundfetchresult/failed.md)
  The download attempt failed.
- [WKBackgroundFetchResult.newData](./wkbackgroundfetchresult/newdata.md)
  The download attempt succeeded.
- [WKBackgroundFetchResult.noData](./wkbackgroundfetchresult/nodata.md)
  The notification has no associated content.
### Initializers
- [init?(rawValue: UInt)](./wkbackgroundfetchresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing remote notifications
- [func didRegisterForRemoteNotifications(withDeviceToken: Data)](./wkapplicationdelegate/didregisterforremotenotifications%28withdevicetoken%29.md)
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func didFailToRegisterForRemoteNotificationsWithError(any Error)](./wkapplicationdelegate/didfailtoregisterforremotenotificationswitherror%28_%29.md)
  Tells the delegate that Apple Push Notification service (APNs) can’t successfully complete the registration process.
- [func didReceiveRemoteNotification([AnyHashable : Any], fetchCompletionHandler: (WKBackgroundFetchResult) -> Void)](./wkapplicationdelegate/didreceiveremotenotification%28_,fetchcompletionhandler%29.md)
  Tells the delegate that a background notification has arrived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkbackgroundfetchresult)*