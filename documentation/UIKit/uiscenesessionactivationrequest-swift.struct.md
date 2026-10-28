# UISceneSessionActivationRequest

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A collection of properties that you use to request activation of a scene.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
struct UISceneSessionActivationRequest
```

## Overview

A `UISceneSessionActiviationRequest` object provides information about how to activate a scene session. Create a request to specify:

- A user activity for the scene session.
- An existing scene session.
- A scene session with a specific role.

You create a `UISceneSessionActivationRequest` object in your code, then you pass it as a parameter when you call [`activateSceneSession(for:errorHandler:)`](./uiapplication/activatescenesession%28for,errorhandler%29.md) to ask the system to activate the scene session.

## Topics

### Creating a request
- [init(role: UISceneSession.Role, userActivity: NSUserActivity?, options: UIScene.ActivationRequestOptions?)](./uiscenesessionactivationrequest-swift.struct/init%28role,useractivity,options%29.md)
  Creates a scene session activation request object with a role, a user activity, and options that you provide.
- [init(session: UISceneSession, userActivity: NSUserActivity?, options: UIScene.ActivationRequestOptions?)](./uiscenesessionactivationrequest-swift.struct/init%28session,useractivity,options%29.md)
  Creates a scene session activation request object with a scene session, a user activity, and options that you provide.
### Managing request details
- [var options: UIScene.ActivationRequestOptions?](./uiscenesessionactivationrequest-swift.struct/options.md)
  Activation request options to further customize the request.
- [var role: UISceneSession.Role](./uiscenesessionactivationrequest-swift.struct/role.md)
  The role to request.
- [var session: UISceneSession?](./uiscenesessionactivationrequest-swift.struct/session.md)
  The specific scene session to activate.
- [var userActivity: NSUserActivity?](./uiscenesessionactivationrequest-swift.struct/useractivity.md)
  A user activity to send to the newly activated scene.
### Initializers
- [init?<D>(hostingDelegateClass: D.Type)](./uiscenesessionactivationrequest-swift.struct/init%28hostingdelegateclass%29.md)
  Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene.
- [init?<D>(hostingDelegateClass: D.Type, id: String)](./uiscenesessionactivationrequest-swift.struct/init%28hostingdelegateclass,id%29.md)
  Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene with the given identifier.
- [init?<H, D>(hostingDelegateClass: H.Type, id: String, value: D)](./uiscenesessionactivationrequest-swift.struct/init%28hostingdelegateclass,id,value%29.md)
  Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene with the given identifier and presented value.
- [init?<H, D>(hostingDelegateClass: H.Type, value: D)](./uiscenesessionactivationrequest-swift.struct/init%28hostingdelegateclass,value%29.md)
  Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene with a presented value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Managing a scene’s life cycle
- [func activateSceneSession(for: UISceneSessionActivationRequest, errorHandler: ((any Error) -> Void)?)](./uiapplication/activatescenesession%28for,errorhandler%29.md)
  Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [func requestSceneSessionDestruction(UISceneSession, options: UISceneDestructionRequestOptions?, errorHandler: ((any Error) -> Void)?)](./uiapplication/requestscenesessiondestruction%28_,options,errorhandler%29.md)
  Asks the system to dismiss an existing scene and remove it from the app switcher.
- [func requestSceneSessionRefresh(UISceneSession)](./uiapplication/requestscenesessionrefresh%28_%29.md)
  Asks the system to update any system UI associated with the specified scene.
- [UIScene.ActivationRequestOptions](./uiscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating the session associated with a scene.
- [class UISceneDestructionRequestOptions](./uiscenedestructionrequestoptions.md)
  An object you pass to UIKit to permanently remove a scene and its associated session from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct)*