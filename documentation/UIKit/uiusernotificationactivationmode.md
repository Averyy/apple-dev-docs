# UIUserNotificationActivationMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating whether the app should activate to the foreground or background.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIUserNotificationAction`](./uiusernotificationaction.md).

## Declaration

```swift
enum UIUserNotificationActivationMode
```

```c
enum UIUserNotificationActivationMode : NSUInteger;
```

## Topics

### Constants
- [UIUserNotificationActivationMode.foreground](./uiusernotificationactivationmode/foreground.md)
  Activate the app and put it in the foreground.
- [UIUserNotificationActivationMode.background](./uiusernotificationactivationmode/background.md)
  Activate the app and put it in the background. If the app is already in the foreground, it remains in the foreground.
### Initializers
- [init?(rawValue: UInt)](./uiusernotificationactivationmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum UIUserNotificationActionBehavior](./uiusernotificationactionbehavior.md)
  Constants indicating additional behavior that the action supports.
- [Action Parameter Key](./action-parameter-key.md)
  Key to include among the parameters of the action.
- [Behavior Key](./behavior-key.md)
  Key related to action-related behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationactivationmode)*