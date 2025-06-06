# actions(for:)

**Framework**: UIKit  
**Kind**: method

Returns the actions to be displayed for the given notification context.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func actions(for context: UIUserNotificationActionContext) -> [UIUserNotificationAction]?
```

#### Return Value

An array of [`UIUserNotificationAction`](uiusernotificationaction.md) objects to be displayed in the specified context. The order of the objects in the array represents the order that they are displayed in the resulting notification.

#### Discussion

This method returns the actions associated with the specified display context. To set the actions for a given context, you must create a [`UIMutableUserNotificationCategory`](uimutableusernotificationcategory.md) object and use its setActions:forContext: method to specify your actions.

## Parameters

- `context`: The context in which the notification is displayed. Notifications can have a default context or a minimal context depending on whether the notification was just delivered or the user is looking at it in more detail.

## See Also

- [var identifier: String?](uiusernotificationcategory/identifier.md)
  The name of the action group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/actions(for:))*