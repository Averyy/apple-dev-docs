# UIWindowScene.ActivationInteraction

**Framework**: UIKit  
**Kind**: class

An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class ActivationInteraction
```

#### Overview

Create a [`UIWindowScene.ActivationInteraction`](uiwindowscene/activationinteraction.md) object when you want to facilitate requesting scene activation when the user pinches open on a view. You initialize the interaction with a closure that the system executes when the user triggers the interaction. The closure should return a [`UIWindowScene.ActivationConfiguration`](uiwindowscene/activationconfiguration.md) object. You also provide an error-handler closure that the system executes if the scene activation request fails.

To request scene activation from an interaction with a [`UICollectionView`](uicollectionview.md) cell, use the [`collectionView(_:sceneActivationConfigurationForItemAt:point:)`](uicollectionviewdelegate/collectionview(_:sceneactivationconfigurationforitemat:point:).md) method.

## Topics

### Creating an activation interaction
- [init(UIWindowScene.ActivationInteraction.ConfigurationProvider, errorHandler: (any Error) -> Void)](uiwindowscene/activationinteraction/init(_:errorhandler:).md)
  Creates an activation interaction.
- [UIWindowScene.ActivationInteraction.ConfigurationProvider](uiwindowscene/activationinteraction/configurationprovider.md)
  A type alias defining a closure that provides an activation configuration for the activation interaction.

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
- [Sendable](../Swift/Sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [UIWindowScene.ActivationAction](uiwindowscene/activationaction.md)
  A menu element that requests a window scene.
- [UIWindowScene.ActivationConfiguration](uiwindowscene/activationconfiguration.md)
  An object that provides configuration options for a window scene request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction)*