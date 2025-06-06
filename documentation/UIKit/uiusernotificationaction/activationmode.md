# activationMode

**Framework**: UIKit  
**Kind**: property

The mode in which to run the app when the action is performed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var activationMode: UIUserNotificationActivationMode { get }
```

#### Discussion

If the value in this property is [`UIUserNotificationActivationMode.foreground`](uiusernotificationactivationmode/foreground.md), the value of the [`isAuthenticationRequired`](uiusernotificationaction/isauthenticationrequired.md) property is assumed to be [`true`](https://developer.apple.com/documentation/swift/true) regardless of its actual value.

## See Also

- [var isAuthenticationRequired: Bool](uiusernotificationaction/isauthenticationrequired.md)
  A Boolean value indicating whether the user must unlock the device before the action is performed.
- [var isDestructive: Bool](uiusernotificationaction/isdestructive.md)
  A Boolean value indicating whether the action is destructive.
- [var behavior: UIUserNotificationActionBehavior](uiusernotificationaction/behavior.md)
  The custom behavior (if any) that the action supports.
- [var parameters: [AnyHashable : Any]](uiusernotificationaction/parameters.md)
  A dictionary of additional parameters to include with the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationaction/activationmode)*