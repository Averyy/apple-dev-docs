# categories

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The app’s registered groups of actions.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIUserNotificationSettings`](../uiusernotificationsettings.md).

## Declaration

```swift
var categories: Set<UIUserNotificationCategory>? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSSet<UIUserNotificationCategory *> * categories;
```

## Discussion

This property contains the [`UIUserNotificationCategory`](../uiusernotificationcategory.md) objects that you specified when creating the settings object. Each object corresponds to a group of actions that may be displayed in conjunction with a push notification. After registration, this property contains the set of actions you specified in your initial request.

## See Also

### Related Documentation
- [convenience init(types: UIUserNotificationType, categories: Set<UIUserNotificationCategory>?)](./init%28types,categories%29.md)
  Creates and returns a settings object that you can use to register your requested notification and action types.
### Getting the configured settings
- [var types: UIUserNotificationType](./types.md)
  A bitmask of the notification types that your app is allowed to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationsettings/categories)*