# types

**Framework**: UIKit  
**Kind**: property

A bitmask of the notification types that your app is allowed to use.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var types: UIUserNotificationType { get }
```

#### Discussion

When you create a new settings object, this property contains all of the types you specified. After you register your request with the app, the app provides you with a new settings object that contains only the types that your app is allowed to use.

## See Also

- [class UIUserNotificationSettings](uiusernotificationsettings.md)
  The types of notifications that can be displayed to the user by your app.
- [var categories: Set<UIUserNotificationCategory>?](uiusernotificationsettings/categories.md)
  The app’s registered groups of actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationsettings/types)*