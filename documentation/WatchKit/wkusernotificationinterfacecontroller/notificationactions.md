# notificationActions

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The actions associated with the current notification.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
var notificationActions: [UNNotificationAction] { get set }
```

```objc
@property (nonatomic, copy) NSArray<UNNotificationAction *> * notificationActions;
```

## Discussion

Use this array to dynamically update the list of actions associated with a notification. You can only change this property during the [`didReceive(_:)`](./didreceive%28_%29.md) method.

## See Also

### Related Documentation
- [func didReceive(UNNotification)](./didreceive%28_%29.md)
  Delivers a notification object to your interface controller for processing.
### Working with Actions
- [func performNotificationDefaultAction()](./performnotificationdefaultaction%28%29.md)
  Launches the watchOS app and performs the current notification’s default action.
- [func performDismissAction()](./performdismissaction%28%29.md)
  Dismisses the notification interface controller.
- [func dismiss()](./dismiss%28%29.md)
  Dismisses the notification interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/notificationactions)*