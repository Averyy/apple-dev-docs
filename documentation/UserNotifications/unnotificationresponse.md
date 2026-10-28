# UNNotificationResponse

**Framework**: User Notifications  
**Kind**: class  
**Role**: Class

The user’s response to an actionable notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class UNNotificationResponse
```

```objc
@interface UNNotificationResponse : NSObject
```

## Overview

When the user interacts with a delivered notification, the system delivers a [`UNNotificationResponse`](./unnotificationresponse.md) object to your app so that you can process the response. Users can interact with delivered notifications in many ways. If the notification’s category had associated action buttons, they can select one of those buttons. Users can also dismiss the notification without selecting one of your actions and they can open your app. A response object tells you which option the user selected.

You don’t create [`UNNotificationResponse`](./unnotificationresponse.md) objects yourself. Instead, the shared user notification center object creates them and delivers them to the [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](./unusernotificationcenterdelegate/usernotificationcenter%28_,didreceive,withcompletionhandler%29.md) method of its delegate object. Use that method to extract any needed information from the response object and take appropriate action.

For more information about responding to actions, see [Handling notifications and notification-related actions](./handling-notifications-and-notification-related-actions.md).

## Topics

### Getting the Response Information
- [var actionIdentifier: String](./unnotificationresponse/actionidentifier.md)
  The identifier string of the action that the user selected.
- [var notification: UNNotification](./unnotificationresponse/notification.md)
  The notification to which the user responded.
- [var targetScene: UIScene?](./unnotificationresponse/targetscene.md)
  The scene where the system reflects the user’s response to a notification.
- [let UNNotificationDefaultActionIdentifier: String](./unnotificationdefaultactionidentifier.md)
  An action that indicates the user opened the app from the notification interface.
- [let UNNotificationDismissActionIdentifier: String](./unnotificationdismissactionidentifier.md)
  The action that indicates the user explicitly dismissed the notification interface.
### Initializers
- [init?(coder: NSCoder)](./unnotificationresponse/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UNTextInputNotificationResponse](./untextinputnotificationresponse.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Notification responses
- [Handling notifications and notification-related actions](./handling-notifications-and-notification-related-actions.md)
  Respond to user interactions with the system’s notification interfaces, including handling your app’s custom actions.
- [class UNTextInputNotificationResponse](./untextinputnotificationresponse.md)
  The user’s response to an actionable notification, including any custom text that the user typed or dictated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationresponse)*