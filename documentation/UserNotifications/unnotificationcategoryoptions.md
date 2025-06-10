# UNNotificationCategoryOptions

**Framework**: User Notifications  
**Kind**: struct

Constants indicating how to handle notifications associated with this category.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct UNNotificationCategoryOptions
```

## Topics

### Creating an option
- [init(rawValue: UInt)](unnotificationcategoryoptions/init(rawvalue:).md)
  Initializes a notification category options object using the specified raw value.
### Customizing a category
- [static var allowInCarPlay: UNNotificationCategoryOptions](unnotificationcategoryoptions/allowincarplay.md)
  Allow CarPlay to display notifications of this type.
- [static var allowAnnouncement: UNNotificationCategoryOptions](unnotificationcategoryoptions/allowannouncement.md)
  An option that grants Siri permission to read incoming messages out loud when the user has a compatible audio output device connected.
### Managing hidden preview behavior
- [static var hiddenPreviewsShowTitle: UNNotificationCategoryOptions](unnotificationcategoryoptions/hiddenpreviewsshowtitle.md)
  Show the notification’s title, even if the user has disabled notification previews for the app.
- [static var hiddenPreviewsShowSubtitle: UNNotificationCategoryOptions](unnotificationcategoryoptions/hiddenpreviewsshowsubtitle.md)
  Show the notification’s subtitle, even if the user has disabled notification previews for the app.
### Managing action handling behavior
- [static var customDismissAction: UNNotificationCategoryOptions](unnotificationcategoryoptions/customdismissaction.md)
  Send dismiss actions to the `UNUserNotificationCenter` object’s delegate for handling.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var options: UNNotificationCategoryOptions](unnotificationcategory/options.md)
  Options for how to handle notifications of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcategoryoptions)*