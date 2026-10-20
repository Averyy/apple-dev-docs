# UIWindowScene.DismissalAnimation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIWindowSceneDismissalAnimation : NSInteger;
```

## Topics

### Animation styles
- [UIWindowScene.DismissalAnimation.standard](./dismissalanimation/standard.md)
  The standard dismissal animations.
- [UIWindowScene.DismissalAnimation.commit](./dismissalanimation/commit.md)
  Animations to use when saving changes.
- [UIWindowScene.DismissalAnimation.decline](./dismissalanimation/decline.md)
  Animations to use when declining changes.
### Initializers
- [init?(rawValue: Int)](./dismissalanimation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [UIWindowScene.ActivationAction](./activationaction.md)
  A menu element that requests a window scene.
- [UIWindowScene.ActivationConfiguration](./activationconfiguration.md)
  An object that provides configuration options for a window scene request.
- [UIWindowScene.ActivationInteraction](./activationinteraction.md)
  An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [UIWindowScene.ActivationRequestOptions](./activationrequestoptions.md)
  An object that contains information you want the system to use when activating a new window scene.
- [class UIWindowSceneDestructionRequestOptions](../uiwindowscenedestructionrequestoptions.md)
  An object that contains information to use when removing a window scene from your app.
- [class UIWindowSceneDragInteraction](../uiwindowscenedraginteraction.md)
  An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [UIWindowScene.ResizingRestrictions](./resizingrestrictions.md)
- [enum UIWindowSceneResizingRestrictions](../uiwindowsceneresizingrestrictions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/dismissalanimation)*