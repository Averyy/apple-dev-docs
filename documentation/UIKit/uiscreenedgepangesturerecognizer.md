# UIScreenEdgePanGestureRecognizer

**Framework**: UIKit  
**Kind**: class

A continuous gesture recognizer that interprets panning gestures that start near an edge of the screen.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UIScreenEdgePanGestureRecognizer
```

## Mentions

- [Handling pan gestures](handling-pan-gestures.md)

#### Overview

The system uses screen edge gestures in some cases to initiate view controller transitions. You can use this class to replicate the same gesture behavior for your own actions.

After creating a screen edge pan gesture recognizer, assign an appropriate value to the [`edges`](uiscreenedgepangesturerecognizer/edges.md) property before attaching the gesture recognizer to your view. You use this property to specify the edges where the gesture can start. This gesture recognizer ignores any touches beyond the first touch.

## Topics

### Specifying the starting edges
- [var edges: UIRectEdge](uiscreenedgepangesturerecognizer/edges.md)
  The acceptable starting edges for the gesture.
- [struct UIRectEdge](uirectedge.md)
  Constants that specify the edges of a rectangle.

## Relationships

### Inherits From
- [UIPanGestureRecognizer](uipangesturerecognizer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [class UIRotationGestureRecognizer](uirotationgesturerecognizer.md)
  A continuous gesture recognizer that interprets rotation gestures involving two touches.
- [class UISwipeGestureRecognizer](uiswipegesturerecognizer.md)
  A discrete gesture recognizer that interprets swiping gestures in one or more directions.
- [class UITapGestureRecognizer](uitapgesturerecognizer.md)
  A discrete gesture recognizer that interprets single or multiple taps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreenedgepangesturerecognizer)*