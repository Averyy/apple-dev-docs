# didReceive(_:)

**Framework**: WatchKit  
**Kind**: method

Tells the delegate that a local notification was triggered.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
optional func didReceive(_ notification: UILocalNotification)
```

#### Discussion

If a local notification arrives while your app is active, WatchKit calls this method to deliver the notification payload. Use this method to respond to the notification. For example, you might use this method to update your app’s interface or display a message to the user.

WatchKit may call this method multiple times. If a new local notification with the same category arrives while your app is active, WatchKit calls the method again with the new payload.

## Parameters

- `notification`: The local notification object corresponding to the event that was triggered.

## See Also

- [func didReceiveRemoteNotification([AnyHashable : Any])](wkextensiondelegate/didreceiveremotenotification(_:).md)
  Tells the delegate that a remote notification arrived.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any])](wkextensiondelegate/handleaction(withidentifier:forremotenotification:).md)
  Delivers a remote notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any], withResponseInfo: [AnyHashable : Any])](wkextensiondelegate/handleaction(withidentifier:forremotenotification:withresponseinfo:).md)
  Delivers a remote notification payload and user response information to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification)](wkextensiondelegate/handleaction(withidentifier:for:).md)
  Delivers a local notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification, withResponseInfo: [AnyHashable : Any])](wkextensiondelegate/handleaction(withidentifier:for:withresponseinfo:).md)
  Delivers a local notification payload and user response information to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceive(_:))*