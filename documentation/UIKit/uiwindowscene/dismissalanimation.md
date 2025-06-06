# UIWindowScene.DismissalAnimation

**Framework**: UIKit  
**Kind**: enum

Constants that indicate the types of animations available for dismissing a scene’s windows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum DismissalAnimation
```

## Topics

### Animation styles
- [UIWindowScene.DismissalAnimation.standard](uiwindowscene/dismissalanimation/standard.md)
  The standard dismissal animations.
- [UIWindowScene.DismissalAnimation.commit](uiwindowscene/dismissalanimation/commit.md)
  Animations to use when saving changes.
- [UIWindowScene.DismissalAnimation.decline](uiwindowscene/dismissalanimation/decline.md)
  Animations to use when declining changes.
### Initializers
- [init?(rawValue: Int)](uiwindowscene/dismissalanimation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [class UIWindowSceneDragInteraction](uiwindowscenedraginteraction.md)
  An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [UIWindowScene.ResizingRestrictions](uiwindowscene/resizingrestrictions.md)
- [enum UIWindowSceneResizingRestrictions](uiwindowsceneresizingrestrictions.md)
- [UIWindowScene.PresentationStyle](uiwindowscene/presentationstyle.md)
  The placement of a window scene relative to other scenes in the workspace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/dismissalanimation)*