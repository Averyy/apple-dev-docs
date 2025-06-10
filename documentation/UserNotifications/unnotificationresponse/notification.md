# notification

**Framework**: User Notifications  
**Kind**: property

The notification to which the user responded.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var notification: UNNotification { get }
```

## See Also

- [var actionIdentifier: String](unnotificationresponse/actionidentifier.md)
  The identifier string of the action that the user selected.
- [var targetScene: UIScene?](unnotificationresponse/targetscene.md)
  The scene where the system reflects the user’s response to a notification.
- [let UNNotificationDefaultActionIdentifier: String](unnotificationdefaultactionidentifier.md)
  An action that indicates the user opened the app from the notification interface.
- [let UNNotificationDismissActionIdentifier: String](unnotificationdismissactionidentifier.md)
  The action that indicates the user explicitly dismissed the notification interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationresponse/notification)*