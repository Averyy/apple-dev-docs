# userActivity

**Framework**: UIKit  
**Kind**: property

A user activity to send to the newly activated scene.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
var userActivity: NSUserActivity? { get set }
```

#### Discussion

The system sends the `userActivity` to the session’s scene upon activation, regardless of whether the scene session already exists.

If you don’t provide a scene session to activate, the system uses the [`targetContentIdentifier`](https://developer.apple.com/documentation/foundation/nsuseractivity/3238062-targetcontentidentifier) of the user activity to determine which scene session to activate. When the user activity’s [`targetContentIdentifier`](https://developer.apple.com/documentation/foundation/nsuseractivity/3238062-targetcontentidentifier) satisfies the [`prefersToActivateForTargetContentIdentifierPredicate`](uisceneactivationconditions/preferstoactivatefortargetcontentidentifierpredicate.md), the system activates that scene’s session to handle the user activity.

## See Also

- [var options: UIScene.ActivationRequestOptions?](uiscenesessionactivationrequest-swift.struct/options.md)
  Activation request options to further customize the request.
- [var role: UISceneSession.Role](uiscenesessionactivationrequest-swift.struct/role.md)
  The role to request.
- [var session: UISceneSession?](uiscenesessionactivationrequest-swift.struct/session.md)
  The specific scene session to activate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/useractivity)*