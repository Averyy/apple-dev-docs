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

Use this array to dynamically update the list of actions associated with a notification. You can only change this property during the [`didReceive(_:)`](wkusernotificationinterfacecontroller/didreceive(_:).md) method.

## See Also

- [func didReceive(UNNotification)](wkusernotificationinterfacecontroller/didreceive(_:).md)
  Delivers a notification object to your interface controller for processing.
- [func performNotificationDefaultAction()](wkusernotificationinterfacecontroller/performnotificationdefaultaction.md)
  Launches the watchOS app and performs the current notification’s default action.
- [func performDismissAction()](wkusernotificationinterfacecontroller/performdismissaction.md)
  Dismisses the notification interface controller.
- [func dismiss()](wkusernotificationinterfacecontroller/dismiss.md)
  Dismisses the notification interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/notificationactions)*