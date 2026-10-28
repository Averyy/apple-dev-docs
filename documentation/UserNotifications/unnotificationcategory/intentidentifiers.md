# intentIdentifiers

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The intents related to notifications of this category.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var intentIdentifiers: [String] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSArray<NSString *> * intentIdentifiers;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSArray<NSString *> * intentIdentifiers;
```

## Discussion

When the system delivers a notification, the presence of an intent identifier lets the system know that the notification is potentially related to the handling of a request made through Siri.

## See Also

### Getting the Information
- [var identifier: String](./identifier.md)
  The unique string assigned to the category.
- [var actions: [UNNotificationAction]](./actions.md)
  The actions to display when the system delivers notifications of this type.
- [var hiddenPreviewsBodyPlaceholder: String](./hiddenpreviewsbodyplaceholder.md)
  The placeholder text to display when the system disables notification previews for the app.
- [var categorySummaryFormat: String](./categorysummaryformat.md)
  A format string for the summary description used when the system groups the category’s notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcategory/intentidentifiers)*