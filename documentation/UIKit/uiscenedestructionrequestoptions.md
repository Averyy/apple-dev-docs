# UISceneDestructionRequestOptions

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object you pass to UIKit to permanently remove a scene and its associated session from your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISceneDestructionRequestOptions
```

```objc
@interface UISceneDestructionRequestOptions : NSObject
```

#### Overview

Create a [`UISceneDestructionRequestOptions`](./uiscenedestructionrequestoptions.md) object before calling the [`requestSceneSessionDestruction(_:options:errorHandler:)`](./uiapplication/requestscenesessiondestruction%28_,options,errorhandler%29.md) method of [`UIApplication`](./uiapplication.md). When destroying a [`UIWindowScene`](./uiwindowscene.md), create a [`UIWindowSceneDestructionRequestOptions`](./uiwindowscenedestructionrequestoptions.md) object instead and use it to configure the dismissal animations.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UIWindowSceneDestructionRequestOptions](./uiwindowscenedestructionrequestoptions.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Managing a scene’s life cycle
- [func activateSceneSession(for: UISceneSessionActivationRequest, errorHandler: ((any Error) -> Void)?)](./uiapplication/activatescenesession%28for,errorhandler%29.md)
  Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [func requestSceneSessionDestruction(UISceneSession, options: UISceneDestructionRequestOptions?, errorHandler: ((any Error) -> Void)?)](./uiapplication/requestscenesessiondestruction%28_,options,errorhandler%29.md)
  Asks the system to dismiss an existing scene and remove it from the app switcher.
- [func requestSceneSessionRefresh(UISceneSession)](./uiapplication/requestscenesessionrefresh%28_%29.md)
  Asks the system to update any system UI associated with the specified scene.
- [struct UISceneSessionActivationRequest](./uiscenesessionactivationrequest-swift.struct.md)
  A collection of properties that you use to request activation of a scene.
- [UIScene.ActivationRequestOptions](./uiscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating the session associated with a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedestructionrequestoptions)*