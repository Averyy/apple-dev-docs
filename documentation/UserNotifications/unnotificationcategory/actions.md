# actions

**Framework**: User Notifications  
**Kind**: property

The actions to display when the system delivers notifications of this type.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var actions: [UNNotificationAction] { get }
```

#### Discussion

When displaying a notification assigned to this category, the system adds a button to the notification interface for each action in this property. The system displays these buttons after the notification’s content but before the Dismiss button.

When displaying banner notifications, the system displays only the first two actions.

## See Also

- [var identifier: String](unnotificationcategory/identifier.md)
  The unique string assigned to the category.
- [var intentIdentifiers: [String]](unnotificationcategory/intentidentifiers.md)
  The intents related to notifications of this category.
- [var hiddenPreviewsBodyPlaceholder: String](unnotificationcategory/hiddenpreviewsbodyplaceholder.md)
  The placeholder text to display when the system disables notification previews for the app.
- [var categorySummaryFormat: String](unnotificationcategory/categorysummaryformat.md)
  A format string for the summary description used when the system groups the category’s notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcategory/actions)*