# didReceiveRemoteNotification(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a remote notification arrived.

**Availability**:
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Instead of using this method, create a delegate object that adopts the [`UNUserNotificationCenterDelegate`](../../UserNotifications/unusernotificationcenterdelegate.md) protocol and implement the `userNotificationCenter:willPresentNotification:withCompletionHandler:` and `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` methods. Assign this object to the `delegate` property of the singleton [`UNUserNotificationCenter`](../../UserNotifications/unusernotificationcenter.md) object.

## Declaration

```swift
optional func didReceiveRemoteNotification(_ userInfo: [AnyHashable : Any])
```

```objc
- (void) didReceiveRemoteNotification:(NSDictionary *) userInfo;
```

## Discussion

If a remote notification arrives while your app is active, WatchKit calls this method to deliver the notification payload. Use this method to respond to the notification. For example, you might use this method to update your app’s interface or display a message to the user.

WatchKit may call this method multiple times. If a new remote notification with the same category arrives while your app is active, WatchKit calls the method again with the new payload.

## Parameters

- `userInfo`: The remote notification dictionary. The contents of the dictionary correspond to the contents of the notification payload and are organized in the same way. For information about the contents of the remote notification payload, see [Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194).

## See Also

### Deprecated Methods
- [func didReceive(UILocalNotification)](./didreceive%28_%29.md)
  Tells the delegate that a local notification was triggered.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any])](./handleaction%28withidentifier,forremotenotification%29.md)
  Delivers a remote notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any], withResponseInfo: [AnyHashable : Any])](./handleaction%28withidentifier,forremotenotification,withresponseinfo%29.md)
  Delivers a remote notification payload and user response information to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification)](./handleaction%28withidentifier,for%29.md)
  Delivers a local notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification, withResponseInfo: [AnyHashable : Any])](./handleaction%28withidentifier,for,withresponseinfo%29.md)
  Delivers a local notification payload and user response information to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceiveremotenotification(_:))*