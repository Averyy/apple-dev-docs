# categoryIdentifier

**Framework**: User Notifications  
**Kind**: property

The identifier of the notification’s category.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var categoryIdentifier: String { get set }
```

## Mentions

- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md)

#### Discussion

Use notification types to distinguish between the different types of notifications your app supports. You use this support primarily to create actionable notifications with custom action buttons to redirect your notifications through either your notification service app extension or your notification content app extension.

Assign a value to this property that matches the [`identifier`](unnotificationcategory/identifier.md) property of one of the [`UNNotificationCategory`](unnotificationcategory.md) objects you previously registered with your app. If you assign a string that doesn’t match one of your registered categories, the system displays your notification without custom actions and without routing it through your app extensions.

## See Also

- [var threadIdentifier: String](unmutablenotificationcontent/threadidentifier.md)
  The identifier that groups related notifications.
- [var summaryArgument: String](unmutablenotificationcontent/summaryargument.md)
  The text the system adds to the notification summary to provide additional context.
- [var summaryArgumentCount: Int](unmutablenotificationcontent/summaryargumentcount.md)
  The number the system adds to the notification summary when the notification represents multiple items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/categoryidentifier)*