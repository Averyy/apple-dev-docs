# UIUserNotificationType

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants indicating how the app alerts the user when a local or push notification arrives.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIUserNotificationSettings`](./uiusernotificationsettings.md).

## Declaration

```swift
struct UIUserNotificationType
```

```c
enum UIUserNotificationType : NSUInteger;
```

## Topics

### Constants
- [static var badge: UIUserNotificationType](./uiusernotificationtype/badge.md)
  The app badges its icon.
- [static var sound: UIUserNotificationType](./uiusernotificationtype/sound.md)
  The app plays a sound.
- [static var alert: UIUserNotificationType](./uiusernotificationtype/alert.md)
  The app posts an alert.
### Initializers
- [init(rawValue: UInt)](./uiusernotificationtype/init%28rawvalue%29.md)
  Creates a notification type with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationtype)*