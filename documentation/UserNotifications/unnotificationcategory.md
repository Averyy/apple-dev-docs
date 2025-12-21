# UNNotificationCategory

**Framework**: User Notifications  
**Kind**: class

A type of notification your app supports and the custom actions that the system displays.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class UNNotificationCategory
```

## Mentions

- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md)
- [Generating a remote notification](generating-a-remote-notification.md)

#### Overview

A [`UNNotificationCategory`](unnotificationcategory.md) object defines a type of notification that your executable can receive. You create category objects to define your app’s  — notifications that have action buttons the user can select in response to the notification. Each category object you create stores the actions and other behaviors associated with a specific type of notification. Register your category objects using the [`setNotificationCategories(_:)`](unusernotificationcenter/setnotificationcategories(_:).md) method of [`UNUserNotificationCenter`](unusernotificationcenter.md). You can register as many category objects as you need.

> **Note**:  When someone performs a Double Tap gesture while viewing a notification on Apple Watch Series 9 or Apple Watch Ultra 2, the system invokes the first nondestructive action. A nondestructive action doesn’t include the [`destructive`](unnotificationactionoptions/destructive.md) option, and won’t delete user data or change the app irrevocably.

To apply category objects to your notifications, include the category’s identifier string in the payload of any notifications you create. For local notifications, put this string in the [`categoryIdentifier`](unmutablenotificationcontent/categoryidentifier.md) property of the [`UNMutableNotificationContent`](unmutablenotificationcontent.md) object that you use to specify the notification’s content. For remote notifications, use this string as the value of the `category` key in the `aps` dictionary of your payload.

Categories can have associated actions, which define custom buttons the system displays for notifications of that category. When the system has unlimited space, the system displays up to 10 actions. When the system has limited space, the system displays at most two actions.

## Topics

### Essentials
- [convenience init(identifier: String, actions: [UNNotificationAction], intentIdentifiers: [String], options: UNNotificationCategoryOptions)](unnotificationcategory/init(identifier:actions:intentidentifiers:options:).md)
  Creates a category object containing the specified actions and options.
- [convenience init(identifier: String, actions: [UNNotificationAction], intentIdentifiers: [String], hiddenPreviewsBodyPlaceholder: String, options: UNNotificationCategoryOptions)](unnotificationcategory/init(identifier:actions:intentidentifiers:hiddenpreviewsbodyplaceholder:options:).md)
  Creates a category object containing the specified actions, options, and placeholder text used when previews aren’t shown.
- [convenience init(identifier: String, actions: [UNNotificationAction], intentIdentifiers: [String], hiddenPreviewsBodyPlaceholder: String?, categorySummaryFormat: String?, options: UNNotificationCategoryOptions)](unnotificationcategory/init(identifier:actions:intentidentifiers:hiddenpreviewsbodyplaceholder:categorysummaryformat:options:).md)
  Creates a category object containing the specified actions, options, placeholder text used when previews aren’t shown, and summary format string.
### Getting the Information
- [var identifier: String](unnotificationcategory/identifier.md)
  The unique string assigned to the category.
- [var actions: [UNNotificationAction]](unnotificationcategory/actions.md)
  The actions to display when the system delivers notifications of this type.
- [var intentIdentifiers: [String]](unnotificationcategory/intentidentifiers.md)
  The intents related to notifications of this category.
- [var hiddenPreviewsBodyPlaceholder: String](unnotificationcategory/hiddenpreviewsbodyplaceholder.md)
  The placeholder text to display when the system disables notification previews for the app.
- [var categorySummaryFormat: String](unnotificationcategory/categorysummaryformat.md)
  A format string for the summary description used when the system groups the category’s notifications.
### Getting the Options
- [var options: UNNotificationCategoryOptions](unnotificationcategory/options.md)
  Options for how to handle notifications of this type.
- [struct UNNotificationCategoryOptions](unnotificationcategoryoptions.md)
  Constants indicating how to handle notifications associated with this category.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md)
  Differentiate your notifications and add action buttons to the notification interface.
- [class UNNotificationAction](unnotificationaction.md)
  A task your app performs in response to a notification that the system delivers.
- [class UNTextInputNotificationAction](untextinputnotificationaction.md)
  An action that accepts user-typed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcategory)*