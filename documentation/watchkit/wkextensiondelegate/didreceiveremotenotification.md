# didReceiveRemoteNotification(_:)

**Framework**: WatchKit  
**Kind**: method

Tells the delegate that a remote notification arrived.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
optional func didReceiveRemoteNotification(_ userInfo: [AnyHashable : Any])
```

#### Discussion

If a remote notification arrives while your app is active, WatchKit calls this method to deliver the notification payload. Use this method to respond to the notification. For example, you might use this method to update your app’s interface or display a message to the user.

WatchKit may call this method multiple times. If a new remote notification with the same category arrives while your app is active, WatchKit calls the method again with the new payload.

## Parameters

- `userInfo`: The remote notification dictionary. The contents of the dictionary correspond to the contents of the notification payload and are organized in the same way. For information about the contents of the remote notification payload, see  .

## See Also

- [func didReceive(UILocalNotification)](didreceive(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceive(_:)))
  Tells the delegate that a local notification was triggered.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any])](handleaction(withidentifier:forremotenotification:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:forremotenotification:)))
  Delivers a remote notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any], withResponseInfo: [AnyHashable : Any])](handleaction(withidentifier:forremotenotification:withresponseinfo:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:forremotenotification:withresponseinfo:)))
  Delivers a remote notification payload and user response information to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification)](handleaction(withidentifier:for:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:for:)))
  Delivers a local notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification, withResponseInfo: [AnyHashable : Any])](handleaction(withidentifier:for:withresponseinfo:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:for:withresponseinfo:)))
  Delivers a local notification payload and user response information to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceiveremotenotification(_:))*