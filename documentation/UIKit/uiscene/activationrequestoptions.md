# UIScene.ActivationRequestOptions

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UISceneActivationRequestOptions : NSObject
```

#### Overview

Create a [`UIScene.ActivationRequestOptions`](./activationrequestoptions.md) object before you activate or create a scene using the [`activateSceneSession(for:errorHandler:)`](../uiapplication/activatescenesession%28for,errorhandler%29.md) (Swift) or [`activateSceneSessionForRequest:errorHandler:`](../uiapplication/activatescenesessionforrequest_errorhandler_.md) (Objective-C) method of [`UIApplication`](../uiapplication.md). Use this object to specify which of your app’s existing scenes originated the request for the new scene.

## Topics

### Specifying the originator of the request
- [var requestingScene: UIScene?](./activationrequestoptions/requestingscene.md)
  The scene object that requested the activation of a different scene.
### Specifying collection join behavior
- [var collectionJoinBehavior: UISceneCollectionJoinBehavior](./activationrequestoptions/collectionjoinbehavior.md)
  The behavior that specifies how a new scene joins a scene collection.
- [enum UISceneCollectionJoinBehavior](../uiscenecollectionjoinbehavior.md)
  A set of behaviors that specify how a new scene joins a scene collection.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UIWindowScene.ActivationRequestOptions](../uiwindowscene/activationrequestoptions.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Managing a scene’s life cycle
- [func activateSceneSession(for: UISceneSessionActivationRequest, errorHandler: ((any Error) -> Void)?)](../uiapplication/activatescenesession%28for,errorhandler%29.md)
  Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [func requestSceneSessionDestruction(UISceneSession, options: UISceneDestructionRequestOptions?, errorHandler: ((any Error) -> Void)?)](../uiapplication/requestscenesessiondestruction%28_,options,errorhandler%29.md)
  Asks the system to dismiss an existing scene and remove it from the app switcher.
- [func requestSceneSessionRefresh(UISceneSession)](../uiapplication/requestscenesessionrefresh%28_%29.md)
  Asks the system to update any system UI associated with the specified scene.
- [struct UISceneSessionActivationRequest](../uiscenesessionactivationrequest-swift.struct.md)
  A collection of properties that you use to request activation of a scene.
- [class UISceneDestructionRequestOptions](../uiscenedestructionrequestoptions.md)
  An object you pass to UIKit to permanently remove a scene and its associated session from your app.
- [- activateSceneSessionForRequest:errorHandler:](../uiapplication/activatescenesessionforrequest_errorhandler_.md)
  Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-c.class.md)
  A collection of properties that you use to request activation of a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/activationrequestoptions)*