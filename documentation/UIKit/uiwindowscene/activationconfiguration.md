# UIWindowScene.ActivationConfiguration

**Framework**: UIKit  
**Kind**: class

An object that provides configuration options for a window scene request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
class ActivationConfiguration
```

#### Overview

Use a [`UIWindowScene.ActivationConfiguration`](uiwindowscene/activationconfiguration.md) object to request a new window scene from the system. An activation configuration requires a [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object that represents the scene’s content. You can specify a preferred presentation style for the new scene by including an optional [`UIWindowScene.ActivationRequestOptions`](uiwindowscene/activationrequestoptions.md) object. The system automatically animates the transition to the new scene, but you can customize the transition by providing an optional targeted preview.

To request scene activation from a view interaction, use an instance of this class with [`UIWindowScene.ActivationInteraction`](uiwindowscene/activationinteraction.md). To request scene activation from a context menu, use an instance of this class with [`UIWindowScene.ActivationAction`](uiwindowscene/activationaction.md).

## Topics

### Creating an activation configuration
- [convenience init(userActivity: NSUserActivity, options: UIWindowScene.ActivationRequestOptions?, preview: UITargetedPreview?)](uiwindowscene/activationconfiguration/init(useractivity:options:preview:).md)
  Creates an activation configuration.
### Getting information about the activation configuration
- [var userActivity: NSUserActivity](uiwindowscene/activationconfiguration/useractivity.md)
  The user activity used to request a scene.
- [var options: UIWindowScene.ActivationRequestOptions?](uiwindowscene/activationconfiguration/options.md)
  Options for customizing the scene request.
- [UIWindowScene.ActivationRequestOptions](uiwindowscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating a new window scene.
- [var preview: UITargetedPreview?](uiwindowscene/activationconfiguration/preview.md)
  An optional targeted preview that the system uses to animate the transition to the new scene.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [UIWindowScene.PresentationStyle](uiwindowscene/presentationstyle.md)
  The placement of a window scene relative to other scenes in the workspace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationconfiguration)*