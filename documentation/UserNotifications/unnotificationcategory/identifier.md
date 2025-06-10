# identifier

**Framework**: User Notifications  
**Kind**: property

The unique string assigned to the category.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var identifier: String { get }
```

## Mentions

- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md)
- [Generating a remote notification](generating-a-remote-notification.md)

#### Discussion

Use this string to differentiate the different types of notifications that your app can send. To assign a category to a local notification, assign this string to the [`categoryIdentifier`](unmutablenotificationcontent/categoryidentifier.md) property of the content object. To assign a category to a remote notification, use the string as the value of the `category` key in the notification payload `aps` dictionary.

## See Also

- [var actions: [UNNotificationAction]](unnotificationcategory/actions.md)
  The actions to display when the system delivers notifications of this type.
- [var intentIdentifiers: [String]](unnotificationcategory/intentidentifiers.md)
  The intents related to notifications of this category.
- [var hiddenPreviewsBodyPlaceholder: String](unnotificationcategory/hiddenpreviewsbodyplaceholder.md)
  The placeholder text to display when the system disables notification previews for the app.
- [var categorySummaryFormat: String](unnotificationcategory/categorysummaryformat.md)
  A format string for the summary description used when the system groups the category’s notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcategory/identifier)*