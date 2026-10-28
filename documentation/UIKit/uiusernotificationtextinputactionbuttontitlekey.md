# UIUserNotificationTextInputActionButtonTitleKey

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

The key for specifying the title of the text input button.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIUserNotificationAction`](./uiusernotificationaction.md).

## Declaration

```swift
let UIUserNotificationTextInputActionButtonTitleKey: String
```

```c
extern NSString * const UIUserNotificationTextInputActionButtonTitleKey;
```

## Description

The value of this key is an [`NSString`](../Foundation/nsstring.md) object. When the user chooses to provide a text response to a notification, UIKit displays an interface for entering that response. The value of this key is used on the button that the user taps to accept that text and attach it to the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationtextinputactionbuttontitlekey)*