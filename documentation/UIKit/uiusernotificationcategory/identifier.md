# identifier

**Framework**: UIKit  
**Kind**: property

The name of the action group.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var identifier: String? { get }
```

#### Discussion

When generating a notification that includes these custom actions, you must use this string to initialize the notification. For local notifications, assign the string to the [`category`](uilocalnotification/category.md) property of the [`UILocalNotification`](uilocalnotification.md) object. For push notifications, use the string as the value of the `category` key in the push notification’s payload.

## See Also

- [func actions(for: UIUserNotificationActionContext) -> [UIUserNotificationAction]?](uiusernotificationcategory/actions(for:).md)
  Returns the actions to be displayed for the given notification context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/identifier)*