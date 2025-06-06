# behavior

**Framework**: UIKit  
**Kind**: property

The custom behavior (if any) that the action supports.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var behavior: UIUserNotificationActionBehavior { get }
```

#### Discussion

The default value of this property is [`UIUserNotificationActionBehavior.default`](uiusernotificationactionbehavior/default.md).

## See Also

- [var activationMode: UIUserNotificationActivationMode](uiusernotificationaction/activationmode.md)
  The mode in which to run the app when the action is performed.
- [var isAuthenticationRequired: Bool](uiusernotificationaction/isauthenticationrequired.md)
  A Boolean value indicating whether the user must unlock the device before the action is performed.
- [var isDestructive: Bool](uiusernotificationaction/isdestructive.md)
  A Boolean value indicating whether the action is destructive.
- [var parameters: [AnyHashable : Any]](uiusernotificationaction/parameters.md)
  A dictionary of additional parameters to include with the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationaction/behavior)*