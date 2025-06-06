# role

**Framework**: UIKit  
**Kind**: property

The role to request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
var role: UISceneSession.Role { get }
```

#### Discussion

If you created the request using [`init(session:userActivity:options:)`](uiscenesessionactivationrequest-swift.struct/init(session:useractivity:options:).md), this property reflects the role of the `session`.

## See Also

- [var options: UIScene.ActivationRequestOptions?](uiscenesessionactivationrequest-swift.struct/options.md)
  Activation request options to further customize the request.
- [var session: UISceneSession?](uiscenesessionactivationrequest-swift.struct/session.md)
  The specific scene session to activate.
- [var userActivity: NSUserActivity?](uiscenesessionactivationrequest-swift.struct/useractivity.md)
  A user activity to send to the newly activated scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/role)*