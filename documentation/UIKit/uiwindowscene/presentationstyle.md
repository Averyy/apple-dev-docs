# UIWindowScene.PresentationStyle

**Framework**: UIKit  
**Kind**: enum

The placement of a window scene relative to other scenes in the workspace.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum PresentationStyle
```

## Topics

### Constants
- [UIWindowScene.PresentationStyle.automatic](uiwindowscene/presentationstyle/automatic.md)
  The system determines the most appropriate style.
- [UIWindowScene.PresentationStyle.prominent](uiwindowscene/presentationstyle/prominent.md)
  Presents prominently above others in the current space.
- [UIWindowScene.PresentationStyle.standard](uiwindowscene/presentationstyle/standard.md)
  The default style of the system.
### Initializers
- [init?(rawValue: UInt)](uiwindowscene/presentationstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UIWindowScene.ActivationAction](uiwindowscene/activationaction.md)
  A menu element that requests a window scene.
- [UIWindowScene.ActivationConfiguration](uiwindowscene/activationconfiguration.md)
  An object that provides configuration options for a window scene request.
- [UIWindowScene.ActivationInteraction](uiwindowscene/activationinteraction.md)
  An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [UIWindowScene.ActivationRequestOptions](uiwindowscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating a new window scene.
- [class UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md)
  An object that contains information to use when removing a window scene from your app.
- [UIWindowScene.DismissalAnimation](uiwindowscene/dismissalanimation.md)
  Constants that indicate the types of animations available for dismissing a scene’s windows.
- [class UIWindowSceneDragInteraction](uiwindowscenedraginteraction.md)
  An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [UIWindowScene.ResizingRestrictions](uiwindowscene/resizingrestrictions.md)
- [enum UIWindowSceneResizingRestrictions](uiwindowsceneresizingrestrictions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/presentationstyle)*