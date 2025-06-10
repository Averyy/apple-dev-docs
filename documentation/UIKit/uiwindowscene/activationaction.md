# UIWindowScene.ActivationAction

**Framework**: UIKit  
**Kind**: class

A menu element that requests a window scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class ActivationAction
```

#### Overview

Create a [`UIWindowScene.ActivationAction`](uiwindowscene/activationaction.md) object to facilitate activating a new window scene from a menu item. You initialize the action with a closure that the system executes when a user selects the item. The closure should return a [`UIWindowScene.ActivationConfiguration`](uiwindowscene/activationconfiguration.md) object. You can specify an alternate action to display on iPhone and apps that don’t support multiple windows.

## Topics

### Creating an activation action
- [convenience init(title: String?, subtitle: String?, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, alternate: UIAction?, UIWindowScene.ActivationAction.ConfigurationProvider)](uiwindowscene/activationaction/init(title:subtitle:image:identifier:discoverabilitytitle:attributes:alternate:_:).md)
  Creates an activation action using the specified parameters.
- [UIWindowScene.ActivationAction.ConfigurationProvider](uiwindowscene/activationaction/configurationprovider.md)
  A type alias defining a closure that provides an activation configuration for the activation action.
### Getting information about the activation action
- [var title: String!](uiwindowscene/activationaction/title.md)
  The action’s title.

## Relationships

### Inherits From
- [UIAction](uiaction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIMenuLeaf](uimenuleaf.md)

## See Also

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
- [UIWindowScene.PresentationStyle](uiwindowscene/presentationstyle.md)
  The placement of a window scene relative to other scenes in the workspace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationaction)*