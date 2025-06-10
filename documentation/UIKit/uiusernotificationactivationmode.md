# UIUserNotificationActivationMode

**Framework**: UIKit  
**Kind**: enum

Constants indicating whether the app should activate to the foreground or background.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum UIUserNotificationActivationMode
```

## Topics

### Constants
- [UIUserNotificationActivationMode.foreground](uiusernotificationactivationmode/foreground.md)
  Activate the app and put it in the foreground.
- [UIUserNotificationActivationMode.background](uiusernotificationactivationmode/background.md)
  Activate the app and put it in the background. If the app is already in the foreground, it remains in the foreground.
### Initializers
- [init?(rawValue: UInt)](uiusernotificationactivationmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum UIUserNotificationActionBehavior](uiusernotificationactionbehavior.md)
  Constants indicating additional behavior that the action supports.
- [Action Parameter Key](action-parameter-key.md)
  Key to include among the parameters of the action.
- [Behavior Key](behavior-key.md)
  Key related to action-related behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationactivationmode)*