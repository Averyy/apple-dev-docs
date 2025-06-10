# UIWindowSceneDestructionRequestOptions

**Framework**: UIKit  
**Kind**: class

An object that contains information to use when removing a window scene from your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIWindowSceneDestructionRequestOptions
```

#### Overview

Create a [`UIWindowSceneDestructionRequestOptions`](uiwindowscenedestructionrequestoptions.md) object before you close one of your app’s scenes using the [`requestSceneSessionDestruction(_:options:errorHandler:)`](uiapplication/requestscenesessiondestruction(_:options:errorhandler:).md) method of [`UIApplication`](uiapplication.md). Use this object to specify the dismissal animations to apply to the scene’s UI, if that UI is onscreen.

## Topics

### Configuring the dismissal animation
- [var windowDismissalAnimation: UIWindowScene.DismissalAnimation](uiwindowscenedestructionrequestoptions/windowdismissalanimation.md)
  The animations to use when dismissing the scene’s windows.
- [UIWindowScene.DismissalAnimation](uiwindowscene/dismissalanimation.md)
  Constants that indicate the types of animations available for dismissing a scene’s windows.

## Relationships

### Inherits From
- [UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UISceneActivationConditions](uisceneactivationconditions.md)
  The set of conditions that define when UIKit activates the current scene.
- [UIScene.ActivationRequestOptions](uiscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating the session associated with a scene.
- [class UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md)
  An object you pass to UIKit to permanently remove a scene and its associated session from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedestructionrequestoptions)*