# isDestructive

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the action is destructive.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIUserNotificationAction`](../uiusernotificationaction.md).

## Declaration

```swift
var isDestructive: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isDestructive) BOOL destructive;
```

#### Discussion

Use this property to signal to the user whether the action causes destructive behavior to the user’s data or the app. When the value of this property is [`true`](../../Swift/true.md), the system displays the corresponding button differently to indicate that the action is destructive.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Getting the action’s configuration
- [var activationMode: UIUserNotificationActivationMode](./activationmode.md)
  The mode in which to run the app when the action is performed.
- [var isAuthenticationRequired: Bool](./isauthenticationrequired.md)
  A Boolean value indicating whether the user must unlock the device before the action is performed.
- [var behavior: UIUserNotificationActionBehavior](./behavior.md)
  The custom behavior (if any) that the action supports.
- [var parameters: [AnyHashable : Any]](./parameters.md)
  A dictionary of additional parameters to include with the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationaction/isdestructive)*