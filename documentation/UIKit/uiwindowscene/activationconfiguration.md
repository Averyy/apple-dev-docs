# UIWindowScene.ActivationConfiguration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIWindowSceneActivationConfiguration : NSObject
```

## Overview

Use a [`UIWindowScene.ActivationConfiguration`](./activationconfiguration.md) object to request a new window scene from the system. An activation configuration requires a [`NSUserActivity`](../../Foundation/nsuseractivity.md) object that represents the scene’s content. You can specify a preferred presentation style for the new scene by including an optional [`UIWindowScene.ActivationRequestOptions`](./activationrequestoptions.md) object. The system automatically animates the transition to the new scene, but you can customize the transition by providing an optional targeted preview.

To request scene activation from a view interaction, use an instance of this class with [`UIWindowScene.ActivationInteraction`](./activationinteraction.md). To request scene activation from a context menu, use an instance of this class with [`UIWindowScene.ActivationAction`](./activationaction.md).

## Topics

### Creating an activation configuration
- [convenience init(userActivity: NSUserActivity, options: UIWindowScene.ActivationRequestOptions?, preview: UITargetedPreview?)](./activationconfiguration/init%28useractivity,options,preview%29.md)
  Creates an activation configuration.
- [- initWithUserActivity:](../uiwindowsceneactivationconfiguration/initwithuseractivity_.md)
  Creates an activation configuration.
### Getting information about the activation configuration
- [var userActivity: NSUserActivity](./activationconfiguration/useractivity.md)
  The user activity used to request a scene.
- [var options: UIWindowScene.ActivationRequestOptions?](./activationconfiguration/options.md)
  Options for customizing the scene request.
- [UIWindowScene.ActivationRequestOptions](./activationrequestoptions.md)
  An object that contains information you want the system to use when activating a new window scene.
- [var preview: UITargetedPreview?](./activationconfiguration/preview.md)
  An optional targeted preview that the system uses to animate the transition to the new scene.

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

## See Also

### Supporting types
- [UIWindowScene.ActivationAction](./activationaction.md)
  A menu element that requests a window scene.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationconfiguration)*