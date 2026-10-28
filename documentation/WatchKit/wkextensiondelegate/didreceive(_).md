# didReceive(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a local notification was triggered.

**Availability**:
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Instead of using this method, create a delegate object that adopts the [`UNUserNotificationCenterDelegate`](../../UserNotifications/unusernotificationcenterdelegate.md) protocol and implement the `userNotificationCenter:willPresentNotification:withCompletionHandler:` and `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` methods. Assign this object to the `delegate` property of the singleton [`UNUserNotificationCenter`](../../UserNotifications/unusernotificationcenter.md) object.

## Declaration

```swift
optional func didReceive(_ notification: UILocalNotification)
```

```objc
- (void) didReceiveLocalNotification:(UILocalNotification *) notification;
```

## Discussion

If a local notification arrives while your app is active, WatchKit calls this method to deliver the notification payload. Use this method to respond to the notification. For example, you might use this method to update your app’s interface or display a message to the user.

WatchKit may call this method multiple times. If a new local notification with the same category arrives while your app is active, WatchKit calls the method again with the new payload.

## Parameters

- `notification`: The local notification object corresponding to the event that was triggered.

## See Also

### Deprecated Methods
- [func didReceiveRemoteNotification([AnyHashable : Any])](./didreceiveremotenotification%28_%29.md)
  Tells the delegate that a remote notification arrived.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any])](./handleaction%28withidentifier,forremotenotification%29.md)
  Delivers a remote notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any], withResponseInfo: [AnyHashable : Any])](./handleaction%28withidentifier,forremotenotification,withresponseinfo%29.md)
  Delivers a remote notification payload and user response information to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification)](./handleaction%28withidentifier,for%29.md)
  Delivers a local notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification, withResponseInfo: [AnyHashable : Any])](./handleaction%28withidentifier,for,withresponseinfo%29.md)
  Delivers a local notification payload and user response information to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceive(_:))*