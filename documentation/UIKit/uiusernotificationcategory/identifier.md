# identifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The name of the action group.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIUserNotificationCategory`](../uiusernotificationcategory.md).

## Declaration

```swift
var identifier: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * identifier;
```

#### Discussion

When generating a notification that includes these custom actions, you must use this string to initialize the notification. For local notifications, assign the string to the [`category`](../uilocalnotification/category.md) property of the [`UILocalNotification`](../uilocalnotification.md) object. For push notifications, use the string as the value of the `category` key in the push notification’s payload.

## See Also

### Getting the group configuration
- [func actions(for: UIUserNotificationActionContext) -> [UIUserNotificationAction]?](./actions%28for%29.md)
  Returns the actions to be displayed for the given notification context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/identifier)*