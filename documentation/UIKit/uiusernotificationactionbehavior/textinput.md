# UIUserNotificationActionBehavior.textInput

**Framework**: UIKit  
**Kind**: case

The text input behavior.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case textInput
```

#### Discussion

When specified, the system provides a way for the user to enter a text response to be included with the notification. The text response is assigned to the [`UIUserNotificationActionResponseTypedTextKey`](uiusernotificationactionresponsetypedtextkey.md) of the response information dictionary when the notification is delivered to your app.

## See Also

- [UIUserNotificationActionBehavior.default](uiusernotificationactionbehavior/default.md)
  The default action behavior. When specified, the action supports no additional behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationactionbehavior/textinput)*