# didReceive(_:)

**Framework**: Watchkit  
**Kind**: method

Tells the delegate that a local notification was triggered.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor optional func didReceive(_ notification: UILocalNotification)
```

## Overview

If a local notification arrives while your app is active, WatchKit calls this method to deliver the notification payload. Use this method to respond to the notification. For example, you might use this method to update your app’s interface or display a message to the user.

WatchKit may call this method multiple times. If a new local notification with the same category arrives while your app is active, WatchKit calls the method again with the new payload.

## Parameters

- `notification`: The local notification object corresponding to the event that was triggered.

## See Also

- [func didReceiveRemoteNotification([AnyHashable : Any])](didreceiveremotenotification(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceiveremotenotification(_:)))
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any])](handleaction(withidentifier:forremotenotification:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:forremotenotification:)))
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any], withResponseInfo: [AnyHashable : Any])](handleaction(withidentifier:forremotenotification:withresponseinfo:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:forremotenotification:withresponseinfo:)))
- [func handleAction(withIdentifier: String?, for: UILocalNotification)](handleaction(withidentifier:for:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:for:)))
- [func handleAction(withIdentifier: String?, for: UILocalNotification, withResponseInfo: [AnyHashable : Any])](handleaction(withidentifier:for:withresponseinfo:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:for:withresponseinfo:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceive(_:))*