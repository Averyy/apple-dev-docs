# init(session:userActivity:options:)

**Framework**: UIKit  
**Kind**: init

Creates a scene session activation request object with a scene session, a user activity, and options that you provide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
init(session: UISceneSession, userActivity: NSUserActivity? = nil, options: UIScene.ActivationRequestOptions? = nil)
```

#### Discussion

Create an activation request with this method when you want the system to activate an existing scene session that you provide.

## Parameters

- `session`: The specific scene session to activate.
- `userActivity`: A user activity to send to the newly activated scene.
- `options`: Activation request options to further customize the request.

## See Also

- [init(role: UISceneSession.Role, userActivity: NSUserActivity?, options: UIScene.ActivationRequestOptions?)](uiscenesessionactivationrequest-swift.struct/init(role:useractivity:options:).md)
  Creates a scene session activation request object with a role, a user activity, and options that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(session:useractivity:options:))*