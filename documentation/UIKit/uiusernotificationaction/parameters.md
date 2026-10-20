# parameters

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A dictionary of additional parameters to include with the action.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
var parameters: [AnyHashable : Any] { get }
```

```objc
@property (nonatomic, copy, readonly) NSDictionary * parameters;
```

#### Discussion

Use this dictionary to specify any behavior-specific data for the action. For example, the [`UIUserNotificationActionBehavior.textInput`](../uiusernotificationactionbehavior/textinput.md) behavior supports the [`UIUserNotificationTextInputActionButtonTitleKey`](../uiusernotificationtextinputactionbuttontitlekey.md) key, which lets you customize the title of the button displayed by the text input interface.

## See Also

### Getting the action’s configuration
- [var activationMode: UIUserNotificationActivationMode](./activationmode.md)
  The mode in which to run the app when the action is performed.
- [var isAuthenticationRequired: Bool](./isauthenticationrequired.md)
  A Boolean value indicating whether the user must unlock the device before the action is performed.
- [var isDestructive: Bool](./isdestructive.md)
  A Boolean value indicating whether the action is destructive.
- [var behavior: UIUserNotificationActionBehavior](./behavior.md)
  The custom behavior (if any) that the action supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationaction/parameters)*