# WKUserNotificationInterfaceType

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

The type of notification interface to display.

**Availability**:
- watchOS

## Declaration

```swift
enum WKUserNotificationInterfaceType
```

```c
enum WKUserNotificationInterfaceType : NSInteger;
```

## Topics

### Constants
- [WKUserNotificationInterfaceType.default](./wkusernotificationinterfacetype/default.md)
  A constant indicating that the system should display the corresponding static interface instead. When you return this value, the system takes responsibility for displaying the notification’s content.
- [WKUserNotificationInterfaceType.custom](./wkusernotificationinterfacetype/custom.md)
  A constant indicating that the system should display your dynamic notification interface.
### Initializers
- [init?(rawValue: Int)](./wkusernotificationinterfacetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacetype)*