# UITapGestureRecognizer

**Framework**: UIKit  
**Kind**: class

A discrete gesture recognizer that interprets single or multiple taps.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITapGestureRecognizer
```

## Mentions

- [Handling tap gestures](handling-tap-gestures.md)
- [Preferring one gesture over another](preferring-one-gesture-over-another.md)

#### Overview

[`UITapGestureRecognizer`](uitapgesturerecognizer.md) is a concrete subclass of [`UIGestureRecognizer`](uigesturerecognizer.md).

For gesture recognition, the specified number of fingers must tap the view a specified number of times. Although taps are discrete gestures, they’re discrete for each state of the gesture recognizer. The system sends the associated action message when the gesture begins and then again for each intermediate state until (and including) the ending state of the gesture. Code that handles tap gestures should test for the state of the gesture, for example:

Action methods handling this gesture can get the location of the gesture as a whole by calling the [`UIGestureRecognizer`](uigesturerecognizer.md) method [`location(in:)`](uigesturerecognizer/location(in:).md). If there are multiple taps, this location is the first tap. If there are multiple touches, this location is the centroid of all fingers tapping the view. Clients can get the location of particular touches in the tap by calling [`location(ofTouch:in:)`](uigesturerecognizer/location(oftouch:in:).md). If multiple taps are allowed, this location is the first tap.

## Topics

### Configuring the gesture
- [var buttonMaskRequired: UIEvent.ButtonMask](uitapgesturerecognizer/buttonmaskrequired.md)
  The bit mask of the buttons the user must press for gesture recognition.
- [var numberOfTapsRequired: Int](uitapgesturerecognizer/numberoftapsrequired.md)
  The number of taps necessary for gesture recognition.
- [var numberOfTouchesRequired: Int](uitapgesturerecognizer/numberoftouchesrequired.md)
  The number of fingers that the user must tap for gesture recognition.

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
- [class UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md)
  A continuous gesture recognizer that interprets panning gestures that start near an edge of the screen.
- [class UISwipeGestureRecognizer](uiswipegesturerecognizer.md)
  A discrete gesture recognizer that interprets swiping gestures in one or more directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitapgesturerecognizer)*