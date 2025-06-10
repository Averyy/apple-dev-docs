# identifier

**Framework**: User Notifications  
**Kind**: property

The unique string that your app uses to identify the action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var identifier: String { get }
```

#### Discussion

When the user selects an action, the system reports the value of this string to your app. Because your app handles all actions by using a single delegate method, the identifier strings for all of your app’s actions must be unique.

## See Also

- [var title: String](unnotificationaction/title.md)
  The localized string to use as the title of the action.
- [var icon: UNNotificationActionIcon?](unnotificationaction/icon.md)
  The icon associated with the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationaction/identifier)*