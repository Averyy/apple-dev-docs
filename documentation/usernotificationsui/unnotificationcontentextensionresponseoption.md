# UNNotificationContentExtensionResponseOption

**Framework**: User Notifications UI  
**Kind**: enum

Constants indicating the preferred response to a notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum UNNotificationContentExtensionResponseOption
```

## Topics

### Response Options
- [UNNotificationContentExtensionResponseOption.doNotDismiss](unnotificationcontentextensionresponseoption/donotdismiss.md)
  Don’t dismiss the notification interface.
- [UNNotificationContentExtensionResponseOption.dismiss](unnotificationcontentextensionresponseoption/dismiss.md)
  Dismiss the notification interface.
- [UNNotificationContentExtensionResponseOption.dismissAndForwardAction](unnotificationcontentextensionresponseoption/dismissandforwardaction.md)
  Dismiss the notification interface and forward the notification to the app.
### Initializers
- [init?(rawValue: UInt)](unnotificationcontentextensionresponseoption/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func didReceive(UNNotificationResponse, completionHandler: (UNNotificationContentExtensionResponseOption) -> Void)](unnotificationcontentextension/didreceive(_:completionhandler:).md)
  Handles a notification action selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextensionresponseoption)*