# notificationActions

**Framework**: WatchKit  
**Kind**: property

The actions associated with the current notification.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
@MainActor
var notificationActions: [UNNotificationAction] { get set }
```

#### Discussion

Use this array to dynamically update the list of actions associated with a notification. You can only change this property during the [`didReceive(_:)`](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/didreceive(_:)) method.

## See Also

- [func didReceive(UNNotification)](didreceive(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/didreceive(_:)))
  Delivers a notification object to your interface controller for processing.
- [func performNotificationDefaultAction()](performnotificationdefaultaction().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/performnotificationdefaultaction()))
  Launches the watchOS app and performs the current notification’s default action.
- [func performDismissAction()](performdismissaction().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/performdismissaction()))
  Dismisses the notification interface controller.
- [func dismiss()](dismiss().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/dismiss()))
  Dismisses the notification interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/notificationactions)*