# targetScene

**Framework**: User Notifications  
**Kind**: property

The scene where the system reflects the user’s response to a notification.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var targetScene: UIScene? { get }
```

## See Also

- [var actionIdentifier: String](unnotificationresponse/actionidentifier.md)
  The identifier string of the action that the user selected.
- [var notification: UNNotification](unnotificationresponse/notification.md)
  The notification to which the user responded.
- [let UNNotificationDefaultActionIdentifier: String](unnotificationdefaultactionidentifier.md)
  An action that indicates the user opened the app from the notification interface.
- [let UNNotificationDismissActionIdentifier: String](unnotificationdismissactionidentifier.md)
  The action that indicates the user explicitly dismissed the notification interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationresponse/targetscene)*