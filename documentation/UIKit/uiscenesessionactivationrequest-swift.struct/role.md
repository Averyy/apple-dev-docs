# role

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The role to request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
var role: UISceneSession.Role { get }
```

## Discussion

If you created the request using [`init(session:userActivity:options:)`](./init%28session,useractivity,options%29.md), this property reflects the role of the `session`.

## See Also

### Managing request details
- [var options: UIScene.ActivationRequestOptions?](./options.md)
  Activation request options to further customize the request.
- [var session: UISceneSession?](./session.md)
  The specific scene session to activate.
- [var userActivity: NSUserActivity?](./useractivity.md)
  A user activity to send to the newly activated scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/role)*