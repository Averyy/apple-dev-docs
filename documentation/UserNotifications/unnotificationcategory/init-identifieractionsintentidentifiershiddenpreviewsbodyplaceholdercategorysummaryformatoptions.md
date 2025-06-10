# init(identifier:actions:intentIdentifiers:hiddenPreviewsBodyPlaceholder:categorySummaryFormat:options:)

**Framework**: User Notifications  
**Kind**: init

Creates a category object containing the specified actions, options, placeholder text used when previews aren’t shown, and summary format string.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
convenience init(identifier: String, actions: [UNNotificationAction], intentIdentifiers: [String], hiddenPreviewsBodyPlaceholder: String?, categorySummaryFormat: String?, options: UNNotificationCategoryOptions = [])
```

## Parameters

- `identifier`: The unique identifier for the category. Each category that your app uses must have a unique identifier. Don’t specify an empty string.
- `actions`: The actions to display when the system delivers notifications of this type. When minimal space is available, the system displays only the first two actions in the array. You may specify an empty array for this parameter if you don’t want to display custom actions.
- `intentIdentifiers`: The intent identifier strings that you want to associate with notifications of this type. The Intents framework defines constants for each type of intent that you can associate with your notifications.
- `hiddenPreviewsBodyPlaceholder`: To specify different strings for the singular and plural cases, use the   method of   to specify the value for this parameter. The key passed to that method contains the identifier of an entry in a   property list of your project. A strings dictionary lets you specify different formatted strings based on the language rules, and is as described in  .
- `categorySummaryFormat`: A format string for the summary description used when the system groups the category’s notifications.
- `options`: Additional options for handling notifications of this type. For a list of possible values, see  .

## See Also

- [convenience init(identifier: String, actions: [UNNotificationAction], intentIdentifiers: [String], options: UNNotificationCategoryOptions)](unnotificationcategory/init(identifier:actions:intentidentifiers:options:).md)
  Creates a category object containing the specified actions and options.
- [convenience init(identifier: String, actions: [UNNotificationAction], intentIdentifiers: [String], hiddenPreviewsBodyPlaceholder: String, options: UNNotificationCategoryOptions)](unnotificationcategory/init(identifier:actions:intentidentifiers:hiddenpreviewsbodyplaceholder:options:).md)
  Creates a category object containing the specified actions, options, and placeholder text used when previews aren’t shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcategory/init(identifier:actions:intentidentifiers:hiddenpreviewsbodyplaceholder:categorysummaryformat:options:))*