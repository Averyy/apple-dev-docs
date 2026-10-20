# UIUserNotificationActionBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating additional behavior that the action supports.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIUserNotificationAction`](./uiusernotificationaction.md).

## Declaration

```swift
enum UIUserNotificationActionBehavior
```

```c
enum UIUserNotificationActionBehavior : NSUInteger;
```

## Topics

### Constants
- [UIUserNotificationActionBehavior.default](./uiusernotificationactionbehavior/default.md)
  The default action behavior. When specified, the action supports no additional behaviors.
- [UIUserNotificationActionBehavior.textInput](./uiusernotificationactionbehavior/textinput.md)
  The text input behavior.
### Initializers
- [init?(rawValue: UInt)](./uiusernotificationactionbehavior/init%28rawvalue%29.md)

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
- [enum UIUserNotificationActivationMode](./uiusernotificationactivationmode.md)
  Constants indicating whether the app should activate to the foreground or background.
- [Action Parameter Key](./action-parameter-key.md)
  Key to include among the parameters of the action.
- [Behavior Key](./behavior-key.md)
  Key related to action-related behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationactionbehavior)*