# categorySummaryFormat

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

A format string for the summary description used when the system groups the category’s notifications.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var categorySummaryFormat: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * categorySummaryFormat;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * categorySummaryFormat;
```

## See Also

### Getting the Information
- [var identifier: String](./identifier.md)
  The unique string assigned to the category.
- [var actions: [UNNotificationAction]](./actions.md)
  The actions to display when the system delivers notifications of this type.
- [var intentIdentifiers: [String]](./intentidentifiers.md)
  The intents related to notifications of this category.
- [var hiddenPreviewsBodyPlaceholder: String](./hiddenpreviewsbodyplaceholder.md)
  The placeholder text to display when the system disables notification previews for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcategory/categorysummaryformat)*