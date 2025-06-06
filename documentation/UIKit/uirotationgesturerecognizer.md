# UIRotationGestureRecognizer

**Framework**: UIKit  
**Kind**: class

A continuous gesture recognizer that interprets rotation gestures involving two touches.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIRotationGestureRecognizer
```

## Mentions

- [Handling rotation gestures](handling-rotation-gestures.md)

#### Overview

[`UIRotationGestureRecognizer`](uirotationgesturerecognizer.md) is a concrete subclass of [`UIGestureRecognizer`](uigesturerecognizer.md).

The user must press two fingers on a view while rotating it. When the user moves the fingers opposite each other in a circular motion, the underlying view rotates in a corresponding direction and speed.

Rotation is a continuous gesture. It begins when the user moves the two fingers enough to create a rotation gesture. The gesture changes when a finger moves while both fingers remain touching. It ends when the user lifts both fingers. At each stage in the gesture, the gesture recognizer sends its action message.

## Topics

### Interpreting the gesture
- [var rotation: CGFloat](uirotationgesturerecognizer/rotation.md)
  The rotation of the gesture in radians.
- [var velocity: CGFloat](uirotationgesturerecognizer/velocity.md)
  The velocity of the rotation gesture in radians per second.

## Relationships

### Inherits From
- [UIGestureRecognizer](uigesturerecognizer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Handling UIKit gestures](handling-uikit-gestures.md)
  Use gesture recognizers to simplify touch handling and create a consistent user experience.
- [Coordinating multiple gesture recognizers](coordinating-multiple-gesture-recognizers.md)
  Discover how to use multiple gesture recognizers on the same view.
- [Adopting hover support for Apple Pencil](adopting-hover-support-for-apple-pencil.md)
  Enhance user feedback for your iPadOS app with a hover preview for Apple Pencil input.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md)
  Enrich your app’s user experience by supporting standard and custom gesture interaction.
- [class UIHoverGestureRecognizer](uihovergesturerecognizer.md)
  A continuous gesture recognizer that interprets pointer movement over a view.
- [class UILongPressGestureRecognizer](uilongpressgesturerecognizer.md)
  A continuous gesture recognizer that interprets long-press gestures.
- [class UIPanGestureRecognizer](uipangesturerecognizer.md)
  A continuous gesture recognizer that interprets panning gestures.
- [class UIPinchGestureRecognizer](uipinchgesturerecognizer.md)
  A continuous gesture recognizer that interprets pinching gestures involving two touches.
- [class UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md)
  A continuous gesture recognizer that interprets panning gestures that start near an edge of the screen.
- [class UISwipeGestureRecognizer](uiswipegesturerecognizer.md)
  A discrete gesture recognizer that interprets swiping gestures in one or more directions.
- [class UITapGestureRecognizer](uitapgesturerecognizer.md)
  A discrete gesture recognizer that interprets single or multiple taps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirotationgesturerecognizer)*