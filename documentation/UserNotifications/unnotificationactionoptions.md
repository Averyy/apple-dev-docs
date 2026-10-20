# UNNotificationActionOptions

**Framework**: User Notifications  
**Kind**: struct  
**Role**: Structure

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

```c
enum UNNotificationActionOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./unnotificationactionoptions/init%28rawvalue%29.md)
  Initializes an action options object using the specified raw value.
### Constants
- [static var authenticationRequired: UNNotificationActionOptions](./unnotificationactionoptions/authenticationrequired.md)
  The action can be performed only on an unlocked device.
- [static var destructive: UNNotificationActionOptions](./unnotificationactionoptions/destructive.md)
  The action performs a destructive task.
- [static var foreground: UNNotificationActionOptions](./unnotificationactionoptions/foreground.md)
  The action causes the app to launch in the foreground.

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

## See Also

### Getting Options
- [var options: UNNotificationActionOptions](./unnotificationaction/options.md)
  The behaviors associated with the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions)*