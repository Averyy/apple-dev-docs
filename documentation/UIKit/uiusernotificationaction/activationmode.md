# activationMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The mode in which to run the app when the action is performed.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIUserNotificationAction`](../uiusernotificationaction.md).

## Declaration

```swift
var activationMode: UIUserNotificationActivationMode { get }
```

```objc
@property (nonatomic, assign, readonly) UIUserNotificationActivationMode activationMode;
```

## Discussion

If the value in this property is [`UIUserNotificationActivationMode.foreground`](../uiusernotificationactivationmode/foreground.md), the value of the [`isAuthenticationRequired`](./isauthenticationrequired.md) property is assumed to be [`true`](../../Swift/true.md) regardless of its actual value.

## See Also

### Getting the action’s configuration
- [var isAuthenticationRequired: Bool](./isauthenticationrequired.md)
  A Boolean value indicating whether the user must unlock the device before the action is performed.
- [var isDestructive: Bool](./isdestructive.md)
  A Boolean value indicating whether the action is destructive.
- [var behavior: UIUserNotificationActionBehavior](./behavior.md)
  The custom behavior (if any) that the action supports.
- [var parameters: [AnyHashable : Any]](./parameters.md)
  A dictionary of additional parameters to include with the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationaction/activationmode)*