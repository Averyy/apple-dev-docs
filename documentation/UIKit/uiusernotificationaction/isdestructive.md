# isDestructive

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the action is destructive.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var isDestructive: Bool { get }
```

#### Discussion

Use this property to signal to the user whether the action causes destructive behavior to the user’s data or the app. When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the system displays the corresponding button differently to indicate that the action is destructive.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var activationMode: UIUserNotificationActivationMode](uiusernotificationaction/activationmode.md)
  The mode in which to run the app when the action is performed.
- [var isAuthenticationRequired: Bool](uiusernotificationaction/isauthenticationrequired.md)
  A Boolean value indicating whether the user must unlock the device before the action is performed.
- [var behavior: UIUserNotificationActionBehavior](uiusernotificationaction/behavior.md)
  The custom behavior (if any) that the action supports.
- [var parameters: [AnyHashable : Any]](uiusernotificationaction/parameters.md)
  A dictionary of additional parameters to include with the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationaction/isdestructive)*