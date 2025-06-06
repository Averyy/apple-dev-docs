# UNTextInputNotificationResponse

**Framework**: Usernotifications  
**Kind**: class

The user’s response to an actionable notification, including any custom text that the user typed or dictated.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class UNTextInputNotificationResponse
```

#### Overview

The system delivers a [`UNTextInputNotificationResponse`](untextinputnotificationresponse.md) object to your app so that you can process user-provided text content. When defining your categories, you can specify an [`UNTextInputNotificationAction`](untextinputnotificationaction.md) object instead of an [`UNNotificationAction`](unnotificationaction.md) object for your action. If you do, the system creates an [`UNTextInputNotificationResponse`](untextinputnotificationresponse.md) object when the user selects the accompanying action, and it fills the [`userText`](untextinputnotificationresponse/usertext.md) property with any user-entered text.

You don’t create [`UNTextInputNotificationResponse`](untextinputnotificationresponse.md) objects yourself. Instead, the shared user notification center object creates them and delivers them to the [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](unusernotificationcenterdelegate/usernotificationcenter(_:didreceive:withcompletionhandler:).md) method of its delegate object. Use that method to extract any needed information from the response object and take appropriate action.

For more information about responding to actions, see [`Handling notifications and notification-related actions`](handling-notifications-and-notification-related-actions.md).

## Topics

### Getting the Text Response
- [var userText: String](untextinputnotificationresponse/usertext.md)
  The text response provided by the user.

## Relationships

### Inherits From
- [UNNotificationResponse](unnotificationresponse.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Handling notifications and notification-related actions](handling-notifications-and-notification-related-actions.md)
  Respond to user interactions with the system’s notification interfaces, including handling your app’s custom actions.
- [class UNNotificationResponse](unnotificationresponse.md)
  The user’s response to an actionable notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/untextinputnotificationresponse)*