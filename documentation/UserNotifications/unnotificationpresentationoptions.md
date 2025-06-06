# UNNotificationPresentationOptions

**Framework**: Usernotifications  
**Kind**: struct

Constants indicating how to present a notification in a foreground app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct UNNotificationPresentationOptions
```

## Topics

### Constants
- [static var badge: UNNotificationPresentationOptions](unnotificationpresentationoptions/badge.md)
  Apply the notification’s badge value to the app’s icon.
- [static var banner: UNNotificationPresentationOptions](unnotificationpresentationoptions/banner.md)
  Present the notification as a banner.
- [static var list: UNNotificationPresentationOptions](unnotificationpresentationoptions/list.md)
  Show the notification in Notification Center.
- [static var sound: UNNotificationPresentationOptions](unnotificationpresentationoptions/sound.md)
  Play the sound associated with the notification.
- [static var alert: UNNotificationPresentationOptions](unnotificationpresentationoptions/alert.md)
  Display the alert using the content provided by the notification.
### Initializers
- [init(rawValue: UInt)](unnotificationpresentationoptions/init(rawvalue:).md)
  Initializes a notification presentation options object using the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func userNotificationCenter(UNUserNotificationCenter, willPresent: UNNotification, withCompletionHandler: (UNNotificationPresentationOptions) -> Void)](unusernotificationcenterdelegate/usernotificationcenter(_:willpresent:withcompletionhandler:).md)
  Asks the delegate how to handle a notification that arrived while the app was running in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptions)*