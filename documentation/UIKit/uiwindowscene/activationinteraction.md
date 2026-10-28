# UIWindowScene.ActivationInteraction

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIWindowSceneActivationInteraction : NSObject
```

## Overview

Create a [`UIWindowScene.ActivationInteraction`](./activationinteraction.md) object when you want to facilitate requesting scene activation when the user pinches open on a view. You initialize the interaction with a closure that the system executes when the user triggers the interaction. The closure should return a [`UIWindowScene.ActivationConfiguration`](./activationconfiguration.md) object. You also provide an error-handler closure that the system executes if the scene activation request fails.

To request scene activation from an interaction with a [`UICollectionView`](../uicollectionview.md) cell, use the [`collectionView(_:sceneActivationConfigurationForItemAt:point:)`](../uicollectionviewdelegate/collectionview%28_,sceneactivationconfigurationforitemat,point%29.md) method.

## Topics

### Creating an activation interaction
- [init(UIWindowScene.ActivationInteraction.ConfigurationProvider, errorHandler: (any Error) -> Void)](./activationinteraction/init%28_,errorhandler%29.md)
  Creates an activation interaction.
- [UIWindowScene.ActivationInteraction.ConfigurationProvider](./activationinteraction/configurationprovider.md)
  A type alias defining a closure that provides an activation configuration for the activation interaction.
### Initializers
- [init(configurationProvider: UIWindowScene.ActivationInteraction.ConfigurationProvider, errorHandler: (any Error) -> Void)](./activationinteraction/init%28configurationprovider,errorhandler%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [UIInteraction](../uiinteraction.md)

## See Also

### Supporting types
- [UIWindowScene.ActivationAction](./activationaction.md)
  A menu element that requests a window scene.
- [UIWindowScene.ActivationConfiguration](./activationconfiguration.md)
  An object that provides configuration options for a window scene request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction)*