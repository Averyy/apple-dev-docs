# categories

**Framework**: UIKit  
**Kind**: property

The app’s registered groups of actions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var categories: Set<UIUserNotificationCategory>? { get }
```

#### Discussion

This property contains the [`UIUserNotificationCategory`](uiusernotificationcategory.md) objects that you specified when creating the settings object. Each object corresponds to a group of actions that may be displayed in conjunction with a push notification. After registration, this property contains the set of actions you specified in your initial request.

## See Also

- [convenience init(types: UIUserNotificationType, categories: Set<UIUserNotificationCategory>?)](uiusernotificationsettings/init(types:categories:).md)
  Creates and returns a settings object that you can use to register your requested notification and action types.
- [var types: UIUserNotificationType](uiusernotificationsettings/types.md)
  A bitmask of the notification types that your app is allowed to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationsettings/categories)*