# actions

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSArray<UNNotificationAction *> * actions;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSArray<UNNotificationAction *> * actions;
```

#### Discussion

When displaying a notification assigned to this category, the system adds a button to the notification interface for each action in this property. The system displays these buttons after the notification’s content but before the Dismiss button.

When displaying banner notifications, the system displays only the first two actions.

## See Also

### Getting the Information
- [var identifier: String](./identifier.md)
  The unique string assigned to the category.
- [var intentIdentifiers: [String]](./intentidentifiers.md)
  The intents related to notifications of this category.
- [var hiddenPreviewsBodyPlaceholder: String](./hiddenpreviewsbodyplaceholder.md)
  The placeholder text to display when the system disables notification previews for the app.
- [var categorySummaryFormat: String](./categorysummaryformat.md)
  A format string for the summary description used when the system groups the category’s notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcategory/actions)*