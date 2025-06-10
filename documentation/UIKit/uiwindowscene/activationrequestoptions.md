# UIWindowScene.ActivationRequestOptions

**Framework**: UIKit  
**Kind**: class

An object that contains information you want the system to use when activating a new window scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class ActivationRequestOptions
```

#### Overview

Create a [`UIWindowScene.ActivationRequestOptions`](uiwindowscene/activationrequestoptions.md) object before you activate a scene using the [`activateSceneSession(for:errorHandler:)`](uiapplication/activatescenesession(for:errorhandler:).md) (Swift) or [`activateSceneSessionForRequest:errorHandler:`](uiapplication/activatescenesessionforrequest:errorhandler:.md) (Objective-C) method of [`UIApplication`](uiapplication.md). Use this object to specify the preferred presentation style of the new scene.

## Topics

### Positioning windows
- [var placement: (any UIWindowScenePlacement)?](uiwindowscene/activationrequestoptions/placement.md)
  The placement you prefer when the system activates the window scene.
- [protocol UIWindowScenePlacement](uiwindowsceneplacement-swift.protocol.md)
  The placement of a window scene in the workspace.
- [struct UIWindowSceneProminentPlacement](uiwindowsceneprominentplacement-swift.struct.md)
  A placement that indicates the system should present the window more prominently than others in the space.
- [struct UIWindowSceneStandardPlacement](uiwindowscenestandardplacement-swift.struct.md)
  A placement that indicates the system should present the window using the default style of the system in the space.
- [struct UIWindowScenePushPlacement](uiwindowscenepushplacement-swift.struct.md)
  A placement that indicates the system needs to present the window by pushing it onto another window.
### Deprecated
- [var preferredPresentationStyle: UIWindowScene.PresentationStyle](uiwindowscene/activationrequestoptions/preferredpresentationstyle.md)
  The presentation style of the window scene.
- [struct UIWindowSceneReplacePlacement](uiwindowscenereplaceplacement-swift.struct.md)

## Relationships

### Inherits From
- [UIScene.ActivationRequestOptions](uiscene/activationrequestoptions.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [UIWindowScene.ActivationAction](uiwindowscene/activationaction.md)
  A menu element that requests a window scene.
- [UIWindowScene.ActivationConfiguration](uiwindowscene/activationconfiguration.md)
  An object that provides configuration options for a window scene request.
- [UIWindowScene.ActivationInteraction](uiwindowscene/activationinteraction.md)
  An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [class UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md)
  An object that contains information to use when removing a window scene from your app.
- [UIWindowScene.DismissalAnimation](uiwindowscene/dismissalanimation.md)
  Constants that indicate the types of animations available for dismissing a scene’s windows.
- [class UIWindowSceneDragInteraction](uiwindowscenedraginteraction.md)
  An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [UIWindowScene.ResizingRestrictions](uiwindowscene/resizingrestrictions.md)
- [enum UIWindowSceneResizingRestrictions](uiwindowsceneresizingrestrictions.md)
- [UIWindowScene.PresentationStyle](uiwindowscene/presentationstyle.md)
  The placement of a window scene relative to other scenes in the workspace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationrequestoptions)*