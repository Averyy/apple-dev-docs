# actionIdentifier

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The identifier string of the action that the user selected.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var actionIdentifier: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * actionIdentifier;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * actionIdentifier;
```

## Mentions

- [Declaring your actionable notification types](../declaring-your-actionable-notification-types.md)
- [Handling notifications and notification-related actions](../handling-notifications-and-notification-related-actions.md)

#### Discussion

This parameter may contain one the identifier of one of your [`UNNotificationAction`](../unnotificationaction.md) objects or it may contain a system-defined identifier. The system defined identifiers are [`UNNotificationDefaultActionIdentifier`](../unnotificationdefaultactionidentifier.md) and [`UNNotificationDismissActionIdentifier`](../unnotificationdismissactionidentifier.md), which indicate that the user opened the app or dismissed the notification without any further actions.

For more information about defining custom actions, see [Declaring your actionable notification types](../declaring-your-actionable-notification-types.md).

## See Also

### Getting the Response Information
- [var notification: UNNotification](./notification.md)
  The notification to which the user responded.
- [var targetScene: UIScene?](./targetscene.md)
  The scene where the system reflects the user’s response to a notification.
- [let UNNotificationDefaultActionIdentifier: String](../unnotificationdefaultactionidentifier.md)
  An action that indicates the user opened the app from the notification interface.
- [let UNNotificationDismissActionIdentifier: String](../unnotificationdismissactionidentifier.md)
  The action that indicates the user explicitly dismissed the notification interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationresponse/actionidentifier)*