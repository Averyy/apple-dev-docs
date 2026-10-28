# UIWindowSceneDragInteraction

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An interaction you add to a view that enables pan gestures to change the containing window scene’s position.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIWindowSceneDragInteraction
```

```objc
@interface UIWindowSceneDragInteraction : NSObject
```

## Overview

Create and add this interaction to a view that you want to drag to adjust the position of your app’s window. [`UINavigationBar`](./uinavigationbar.md) handles this automatically, so you only need to add this interaction to views in other parts of your window that you want to be draggable.

**Swift**:

```swift
var windowDragInteraction = UIWindowSceneDragInteraction()
draggableView.addInteraction(windowDragInteraction)
```

**Objective-C**:

```objc
UIWindowSceneDragInteraction *windowDragInteraction = [[UIWindowSceneDragInteraction alloc] init];
[self.draggableView addInteraction:windowDragInteraction];
```

## Topics

### Preventing gesture conflicts
- [var gestureForFailureRelationships: UIGestureRecognizer](./uiwindowscenedraginteraction/gestureforfailurerelationships.md)
  The gesture that the drag interaction adds to the view hierarchy.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [UIInteraction](./uiinteraction.md)

## See Also

### Supporting types
- [UIWindowScene.ActivationAction](./uiwindowscene/activationaction.md)
  A menu element that requests a window scene.
- [UIWindowScene.ActivationConfiguration](./uiwindowscene/activationconfiguration.md)
  An object that provides configuration options for a window scene request.
- [UIWindowScene.ActivationInteraction](./uiwindowscene/activationinteraction.md)
  An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [UIWindowScene.ActivationRequestOptions](./uiwindowscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating a new window scene.
- [class UIWindowSceneDestructionRequestOptions](./uiwindowscenedestructionrequestoptions.md)
  An object that contains information to use when removing a window scene from your app.
- [UIWindowScene.DismissalAnimation](./uiwindowscene/dismissalanimation.md)
  Constants that indicate the types of animations available for dismissing a scene’s windows.
- [UIWindowScene.ResizingRestrictions](./uiwindowscene/resizingrestrictions.md)
- [enum UIWindowSceneResizingRestrictions](./uiwindowsceneresizingrestrictions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedraginteraction)*