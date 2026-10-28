# init(role:userActivity:options:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a scene session activation request object with a role, a user activity, and options that you provide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
init(role: UISceneSession.Role = .windowApplication, userActivity: NSUserActivity? = nil, options: UIScene.ActivationRequestOptions? = nil)
```

## Discussion

Create an activation request with this method when you want the system to activate a scene session appropriate for the `role` and `userActivity` you provide. The system activates an existing scene session when the scene session’s [`role`](../uiscenesession/role-swift.property.md) matches the [`role`](./role.md) you request, and the user activity’s [`targetContentIdentifier`](../../Foundation/nsuseractivity/targetcontentidentifier.md) satisfies the scene’s [`activationConditions`](../uiscene/activationconditions.md). Otherwise, the system activates a new scene session.

## Parameters

- `role`: The role to request.
- `userActivity`: A user activity to send to the newly activated scene.
- `options`: Activation request options to further customize the request.

## See Also

### Creating a request
- [init(session: UISceneSession, userActivity: NSUserActivity?, options: UIScene.ActivationRequestOptions?)](./init%28session,useractivity,options%29.md)
  Creates a scene session activation request object with a scene session, a user activity, and options that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(role:useractivity:options:))*