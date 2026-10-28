# UNNotificationDefaultActionIdentifier

**Framework**: User Notifications  
**Kind**: var  
**Role**: Global Variable

An action that indicates the user opened the app from the notification interface.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let UNNotificationDefaultActionIdentifier: String
```

```c
extern NSString * const UNNotificationDefaultActionIdentifier;
```

## Discussion

The delivery of this action doesn’t require any special configuration of notification categories. Use the [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](./unusernotificationcenterdelegate/usernotificationcenter%28_,didreceive,withcompletionhandler%29.md) method of your delegate object to receive this action.

## See Also

### Getting the Response Information
- [var actionIdentifier: String](./unnotificationresponse/actionidentifier.md)
  The identifier string of the action that the user selected.
- [var notification: UNNotification](./unnotificationresponse/notification.md)
  The notification to which the user responded.
- [var targetScene: UIScene?](./unnotificationresponse/targetscene.md)
  The scene where the system reflects the user’s response to a notification.
- [let UNNotificationDismissActionIdentifier: String](./unnotificationdismissactionidentifier.md)
  The action that indicates the user explicitly dismissed the notification interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationdefaultactionidentifier)*