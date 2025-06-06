# UISwipeGestureRecognizer

**Framework**: UIKit  
**Kind**: class

A discrete gesture recognizer that interprets swiping gestures in one or more directions.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISwipeGestureRecognizer
```

## Mentions

- [Handling swipe gestures](handling-swipe-gestures.md)

#### Overview

[`UISwipeGestureRecognizer`](uiswipegesturerecognizer.md) is a concrete subclass of [`UIGestureRecognizer`](uigesturerecognizer.md).` `

[`UISwipeGestureRecognizer`](uiswipegesturerecognizer.md) recognizes a swipe when the user moves the specified number of touches ([`numberOfTouchesRequired`](uiswipegesturerecognizer/numberoftouchesrequired.md)) in an allowable direction ([`direction`](uiswipegesturerecognizer/direction-swift.property.md)) far enough to create a swipe. Swipes can be slow or fast. A slow swipe requires high directional precision but a small distance; a fast swipe requires low directional precision but a large distance. Because a swipe is a discrete gesture, the system sends the associated action message just once per gesture.

You can determine the location where a swipe begins by calling the [`UIGestureRecognizer`](uigesturerecognizer.md) methods [`location(in:)`](uigesturerecognizer/location(in:).md) and [`location(ofTouch:in:)`](uigesturerecognizer/location(oftouch:in:).md). The former method provides the centroid if the gesture contains more than one touch; the latter provides the location of a particular touch.

## Topics

### Configuring the gesture
- [var direction: UISwipeGestureRecognizer.Direction](uiswipegesturerecognizer/direction-swift.property.md)
  The permitted direction of the swipe for this gesture recognizer.
- [var numberOfTouchesRequired: Int](uiswipegesturerecognizer/numberoftouchesrequired.md)
  The number of touches necessary for swipe recognition.
- [UISwipeGestureRecognizer.Direction](uiswipegesturerecognizer/direction-swift.struct.md)
  The direction of the swipe.

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
- [class UIRotationGestureRecognizer](uirotationgesturerecognizer.md)
  A continuous gesture recognizer that interprets rotation gestures involving two touches.
- [class UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md)
  A continuous gesture recognizer that interprets panning gestures that start near an edge of the screen.
- [class UITapGestureRecognizer](uitapgesturerecognizer.md)
  A discrete gesture recognizer that interprets single or multiple taps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswipegesturerecognizer)*