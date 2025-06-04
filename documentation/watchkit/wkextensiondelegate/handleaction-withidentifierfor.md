# handleAction(withIdentifier:for:)

**Framework**: WatchKit  
**Kind**: method

Delivers a local notification payload and a user-selected action to the app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
optional func handleAction(withIdentifier identifier: String?, for localNotification: UILocalNotification)
```

#### Discussion

Use this method to handle actions selected by users from your notification interfaces. If your containing iOS app supports interactive notifications, the `identifier` parameter may contain the action identifier for the button that was tapped. Use that value to perform the requested action. If the `identifier` parameter contains an empty string, that means the user launched your Watch app from the notification interface without choosing a specific action.

The system calls this method on your WatchKit extension’s main thread. The `super` implementation of this method does nothing.

For information about how to support interactive notifications in your iOS app, see [`Local and Remote Notification Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194). For information about how to display a custom interface for notifications, see [`App Programming Guide for watchOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969).

## Parameters

- `identifier`: The action selected by the user. The string is the identifier for an action that was registered by the companion iOS app; it identifies which button was tapped by the user. Use the identifier to perform the associated action. This parameter is set to the empty string when the user launches the app without tapping one of the action buttons.
- `localNotification`: The local notification object that triggered the notification.

## See Also

- [func didReceiveRemoteNotification([AnyHashable : Any])](didreceiveremotenotification(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceiveremotenotification(_:)))
  Tells the delegate that a remote notification arrived.
- [func didReceive(UILocalNotification)](didreceive(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceive(_:)))
  Tells the delegate that a local notification was triggered.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any])](handleaction(withidentifier:forremotenotification:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:forremotenotification:)))
  Delivers a remote notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any], withResponseInfo: [AnyHashable : Any])](handleaction(withidentifier:forremotenotification:withresponseinfo:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:forremotenotification:withresponseinfo:)))
  Delivers a remote notification payload and user response information to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification, withResponseInfo: [AnyHashable : Any])](handleaction(withidentifier:for:withresponseinfo:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:for:withresponseinfo:)))
  Delivers a local notification payload and user response information to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:for:))*