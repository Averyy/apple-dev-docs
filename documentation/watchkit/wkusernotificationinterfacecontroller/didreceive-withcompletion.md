# didReceive(_:withCompletion:)

**Framework**: Watchkit  
**Kind**: method

Delivers a notification object to your interface controller for processing.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
@MainActor
func didReceive(_ notification: UNNotification, withCompletion completionHandler: @escaping (WKUserNotificationInterfaceType) -> Void)
```

#### Discussion

Before displaying your notification interface, WatchKit calls this method to deliver the payload of the incoming remote notification. Implement this method and use it to store the notification dictionary, configure your custom notification interface, and execute the `completionHandler` block as quickly as possible. Failure to execute the completion handler in a timely manner will cause the system to display the corresponding static notification interface.

WatchKit may call this method multiple times while your interface controller is active. If a new remote notification with the same category arrives while your notification interface is active, WatchKit calls the method again with the new remote notification payload.

## Parameters

- `notification`: The notification object that triggered this event.
- `completionHandler`: The completion handler for telling the system what interface to display. Execute this completion handler at the end of your method implementation. If you do not execute this block in a timely manner, the system displays your app’s static notification interface. This block has no return value and takes the following parameter:

## See Also

- [func didReceive(UNNotification)](wkusernotificationinterfacecontroller/didreceive(_:).md)
  Delivers a notification object to your interface controller for processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/didreceive(_:withcompletion:))*