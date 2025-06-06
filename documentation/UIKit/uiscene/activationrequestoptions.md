# UIScene.ActivationRequestOptions

**Framework**: UIKit  
**Kind**: class

An object that contains information you want the system to use when activating the session associated with a scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class ActivationRequestOptions
```

#### Overview

Create a [`UIScene.ActivationRequestOptions`](uiscene/activationrequestoptions.md) object before you activate or create a scene using the [`activateSceneSession(for:errorHandler:)`](uiapplication/activatescenesession(for:errorhandler:).md) (Swift) or [`activateSceneSessionForRequest:errorHandler:`](uiapplication/activatescenesessionforrequest:errorhandler:.md) (Objective-C) method of [`UIApplication`](uiapplication.md). Use this object to specify which of your app’s existing scenes originated the request for the new scene.

## Topics

### Specifying the originator of the request
- [var requestingScene: UIScene?](uiscene/activationrequestoptions/requestingscene.md)
  The scene object that requested the activation of a different scene.
### Specifying collection join behavior
- [var collectionJoinBehavior: UISceneCollectionJoinBehavior](uiscene/activationrequestoptions/collectionjoinbehavior.md)
  The behavior that specifies how a new scene joins a scene collection.
- [enum UISceneCollectionJoinBehavior](uiscenecollectionjoinbehavior.md)
  A set of behaviors that specify how a new scene joins a scene collection.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIWindowScene.ActivationRequestOptions](uiwindowscene/activationrequestoptions.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func activateSceneSession(for: UISceneSessionActivationRequest, errorHandler: ((any Error) -> Void)?)](uiapplication/activatescenesession(for:errorhandler:).md)
  Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [func requestSceneSessionDestruction(UISceneSession, options: UISceneDestructionRequestOptions?, errorHandler: ((any Error) -> Void)?)](uiapplication/requestscenesessiondestruction(_:options:errorhandler:).md)
  Asks the system to dismiss an existing scene and remove it from the app switcher.
- [func requestSceneSessionRefresh(UISceneSession)](uiapplication/requestscenesessionrefresh(_:).md)
  Asks the system to update any system UI associated with the specified scene.
- [struct UISceneSessionActivationRequest](uiscenesessionactivationrequest-swift.struct.md)
  A collection of properties that you use to request activation of a scene.
- [class UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md)
  An object you pass to UIKit to permanently remove a scene and its associated session from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/activationrequestoptions)*