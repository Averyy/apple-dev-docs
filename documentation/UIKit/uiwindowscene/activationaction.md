# UIWindowScene.ActivationAction

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A menu element that requests a window scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
class ActivationAction
```

```objc
@interface UIWindowSceneActivationAction : UIAction
```

#### Overview

Create a [`UIWindowScene.ActivationAction`](./activationaction.md) object to facilitate activating a new window scene from a menu item. You initialize the action with a closure that the system executes when a user selects the item. The closure should return a [`UIWindowScene.ActivationConfiguration`](./activationconfiguration.md) object. You can specify an alternate action to display on iPhone and apps that don’t support multiple windows.

## Topics

### Creating an activation action
- [convenience init(title: String?, subtitle: String?, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, alternate: UIAction?, UIWindowScene.ActivationAction.ConfigurationProvider)](./activationaction/init%28title,subtitle,image,identifier,discoverabilitytitle,attributes,alternate,_%29.md)
  Creates an activation action using the specified parameters.
- [UIWindowScene.ActivationAction.ConfigurationProvider](./activationaction/configurationprovider.md)
  A type alias defining a closure that provides an activation configuration for the activation action.
### Getting information about the activation action
- [var title: String!](./activationaction/title.md)
  The action’s title.

## Relationships

### Inherits From
- [UIAction](../uiaction.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../uiaccessibilityidentification.md)
- [UIMenuLeaf](../uimenuleaf.md)

## See Also

### Supporting types
- [UIWindowScene.ActivationConfiguration](./activationconfiguration.md)
  An object that provides configuration options for a window scene request.
- [UIWindowScene.ActivationInteraction](./activationinteraction.md)
  An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [UIWindowScene.ActivationRequestOptions](./activationrequestoptions.md)
  An object that contains information you want the system to use when activating a new window scene.
- [class UIWindowSceneDestructionRequestOptions](../uiwindowscenedestructionrequestoptions.md)
  An object that contains information to use when removing a window scene from your app.
- [UIWindowScene.DismissalAnimation](./dismissalanimation.md)
  Constants that indicate the types of animations available for dismissing a scene’s windows.
- [class UIWindowSceneDragInteraction](../uiwindowscenedraginteraction.md)
  An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [UIWindowScene.ResizingRestrictions](./resizingrestrictions.md)
- [enum UIWindowSceneResizingRestrictions](../uiwindowsceneresizingrestrictions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationaction)*