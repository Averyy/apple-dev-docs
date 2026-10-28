# actions(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the actions to be displayed for the given notification context.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIUserNotificationCategory`](../uiusernotificationcategory.md).

## Declaration

```swift
func actions(for context: UIUserNotificationActionContext) -> [UIUserNotificationAction]?
```

```objc
- (NSArray<UIUserNotificationAction *> *) actionsForContext:(UIUserNotificationActionContext) context;
```

## Return Value

An array of [`UIUserNotificationAction`](../uiusernotificationaction.md) objects to be displayed in the specified context. The order of the objects in the array represents the order that they are displayed in the resulting notification.

## Discussion

This method returns the actions associated with the specified display context. To set the actions for a given context, you must create a [`UIMutableUserNotificationCategory`](../uimutableusernotificationcategory.md) object and use its setActions:forContext: method to specify your actions.

## Parameters

- `context`: The context in which the notification is displayed. Notifications can have a default context or a minimal context depending on whether the notification was just delivered or the user is looking at it in more detail.

## See Also

### Getting the group configuration
- [var identifier: String?](./identifier.md)
  The name of the action group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/actions(for:))*