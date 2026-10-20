# UNNotificationContentExtensionResponseOption

**Framework**: User Notifications UI  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UNNotificationContentExtensionResponseOption : NSUInteger;
```

## Topics

### Response Options
- [UNNotificationContentExtensionResponseOption.doNotDismiss](./unnotificationcontentextensionresponseoption/donotdismiss.md)
  Don’t dismiss the notification interface.
- [UNNotificationContentExtensionResponseOption.dismiss](./unnotificationcontentextensionresponseoption/dismiss.md)
  Dismiss the notification interface.
- [UNNotificationContentExtensionResponseOption.dismissAndForwardAction](./unnotificationcontentextensionresponseoption/dismissandforwardaction.md)
  Dismiss the notification interface and forward the notification to the app.
### Initializers
- [init?(rawValue: UInt)](./unnotificationcontentextensionresponseoption/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling Custom Actions
- [func didReceive(UNNotificationResponse, completionHandler: (UNNotificationContentExtensionResponseOption) -> Void)](./unnotificationcontentextension/didreceive%28_,completionhandler%29.md)
  Handles a notification action selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextensionresponseoption)*