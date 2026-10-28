# UITouch.Phase.regionMoved

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A touch for the given event is within a window on the screen, but has not yet pressed down.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- tvOS 13.4+
- visionOS 1.0+

## Declaration

```swift
case regionMoved
```

```c
UITouchPhaseRegionMoved
```

## Discussion

The [`UITouch.Phase.regionEntered`](./regionentered.md), [`UITouch.Phase.regionMoved`](./regionmoved.md), and [`UITouch.Phase.regionExited`](./regionexited.md) phases don’t always align with the [`state`](../../uigesturerecognizer/state-swift.property.md) property of a [`UIHoverGestureRecognizer`](../../uihovergesturerecognizer.md). States of the hover gesture recognizer only apply within the context of the gesture’s view, whereas the touch states apply within the window.

## See Also

### Constants
- [UITouch.Phase.began](./began.md)
  A touch for a given event has pressed down on the screen.
- [UITouch.Phase.moved](./moved.md)
  A touch for a given event has moved over the screen.
- [UITouch.Phase.stationary](./stationary.md)
  A touch for a given event is pressed down on the screen, but hasn’t moved since the previous event.
- [UITouch.Phase.ended](./ended.md)
  A touch for a given event has lifted from the screen.
- [UITouch.Phase.cancelled](./cancelled.md)
  The system canceled tracking for a touch, for example, when the user moves the device against their face.
- [UITouch.Phase.regionEntered](./regionentered.md)
  A touch for a given event has entered a window on the screen.
- [UITouch.Phase.regionExited](./regionexited.md)
  A touch for a given event has left a window on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/phase-swift.enum/regionmoved)*