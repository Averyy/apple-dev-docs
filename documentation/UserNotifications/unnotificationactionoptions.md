# UNNotificationActionOptions

**Framework**: User Notifications  
**Kind**: struct

The behaviors you can apply to an action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct UNNotificationActionOptions
```

## Topics

### Initializers
- [init(rawValue: UInt)](unnotificationactionoptions/init(rawvalue:).md)
  Initializes an action options object using the specified raw value.
### Constants
- [static var authenticationRequired: UNNotificationActionOptions](unnotificationactionoptions/authenticationrequired.md)
  The action can be performed only on an unlocked device.
- [static var destructive: UNNotificationActionOptions](unnotificationactionoptions/destructive.md)
  The action performs a destructive task.
- [static var foreground: UNNotificationActionOptions](unnotificationactionoptions/foreground.md)
  The action causes the app to launch in the foreground.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var options: UNNotificationActionOptions](unnotificationaction/options.md)
  The behaviors associated with the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions)*