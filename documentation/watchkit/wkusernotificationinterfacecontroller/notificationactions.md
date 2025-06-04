# notificationActions

**Framework**: Watchkit  
**Kind**: property

The actions associated with the current notification.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
@MainActor var notificationActions: [UNNotificationAction] { get set }
```

## Overview

Use this array to dynamically update the list of actions associated with a notification. You can only change this property during the [`didReceive(_:)`](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/didreceive(_:)) method.

## See Also

- [func didReceive(UNNotification)](didreceive(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/didreceive(_:)))
- [func performNotificationDefaultAction()](performnotificationdefaultaction().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/performnotificationdefaultaction()))
- [func performDismissAction()](performdismissaction().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/performdismissaction()))
- [func dismiss()](dismiss().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/dismiss()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/notificationactions)*