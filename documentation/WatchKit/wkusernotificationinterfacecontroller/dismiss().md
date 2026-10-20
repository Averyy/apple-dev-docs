# dismiss()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the notification interface controller.

**Availability**:
- watchOS 2.0+ - Deprecated in 5.0

> **Deprecated**: Use [`performDismissAction()`](./performdismissaction%28%29.md) instead.

## Declaration

```swift
func dismiss()
```

```objc
- (void) dismissController;
```

## See Also

### Working with Actions
- [var notificationActions: [UNNotificationAction]](./notificationactions.md)
  The actions associated with the current notification.
- [func performNotificationDefaultAction()](./performnotificationdefaultaction%28%29.md)
  Launches the watchOS app and performs the current notification’s default action.
- [func performDismissAction()](./performdismissaction%28%29.md)
  Dismisses the notification interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/dismiss())*