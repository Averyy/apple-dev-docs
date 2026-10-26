# UISceneSessionActivationRequest

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A collection of properties that you use to request activation of a scene.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@interface UISceneSessionActivationRequest : NSObject
```

#### Overview

A `UISceneSessionActiviationRequest` object provides information about how to activate a scene session. Create a request to specify:

- A user activity for the scene session.
- An existing scene session.
- A scene session with a specific role.

You create and configure a `UISceneSessionActivationRequest` object in your code, then you pass it as a parameter when you call [`activateSceneSessionForRequest:errorHandler:`](./uiapplication/activatescenesessionforrequest_errorhandler_.md) to ask the system to activate the scene session.

## Topics

### Creating a request
- [+ request](./uiscenesessionactivationrequest-c.class/request.md)
  Creates a scene session activation request object.
- [+ requestWithRole:](./uiscenesessionactivationrequest-c.class/requestwithrole_.md)
  Creates a scene session activation request object with a role that you provide.
- [+ requestWithSession:](./uiscenesessionactivationrequest-c.class/requestwithsession_.md)
  Creates a scene session activation request object with a scene session that you provide.
### Managing request details
- [options](./uiscenesessionactivationrequest-c.class/options.md)
  Activation request options to further customize the request.
- [role](./uiscenesessionactivationrequest-c.class/role.md)
  The role to request.
- [session](./uiscenesessionactivationrequest-c.class/session.md)
  The specific scene session to activate.
- [userActivity](./uiscenesessionactivationrequest-c.class/useractivity.md)
  A user activity to send to the newly activated scene.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Managing a scene’s life cycle
- [- activateSceneSessionForRequest:errorHandler:](./uiapplication/activatescenesessionforrequest_errorhandler_.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-c.class)*