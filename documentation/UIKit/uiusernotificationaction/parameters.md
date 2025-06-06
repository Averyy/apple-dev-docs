# parameters

**Framework**: UIKit  
**Kind**: property

A dictionary of additional parameters to include with the action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var parameters: [AnyHashable : Any] { get }
```

#### Discussion

Use this dictionary to specify any behavior-specific data for the action. For example, the [`UIUserNotificationActionBehavior.textInput`](uiusernotificationactionbehavior/textinput.md) behavior supports the [`UIUserNotificationTextInputActionButtonTitleKey`](uiusernotificationtextinputactionbuttontitlekey.md) key, which lets you customize the title of the button displayed by the text input interface.

## See Also

- [var activationMode: UIUserNotificationActivationMode](uiusernotificationaction/activationmode.md)
  The mode in which to run the app when the action is performed.
- [var isAuthenticationRequired: Bool](uiusernotificationaction/isauthenticationrequired.md)
  A Boolean value indicating whether the user must unlock the device before the action is performed.
- [var isDestructive: Bool](uiusernotificationaction/isdestructive.md)
  A Boolean value indicating whether the action is destructive.
- [var behavior: UIUserNotificationActionBehavior](uiusernotificationaction/behavior.md)
  The custom behavior (if any) that the action supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationaction/parameters)*