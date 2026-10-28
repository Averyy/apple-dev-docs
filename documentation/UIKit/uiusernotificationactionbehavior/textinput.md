# UIUserNotificationActionBehavior.textInput

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The text input behavior.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIUserNotificationAction`](../uiusernotificationaction.md).

## Declaration

```swift
case textInput
```

```c
UIUserNotificationActionBehaviorTextInput
```

## Discussion

When specified, the system provides a way for the user to enter a text response to be included with the notification. The text response is assigned to the [`UIUserNotificationActionResponseTypedTextKey`](../uiusernotificationactionresponsetypedtextkey.md) of the response information dictionary when the notification is delivered to your app.

## See Also

### Constants
- [UIUserNotificationActionBehavior.default](./default.md)
  The default action behavior. When specified, the action supports no additional behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationactionbehavior/textinput)*