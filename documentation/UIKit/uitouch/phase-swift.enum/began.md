# UITouch.Phase.began

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A touch for a given event has pressed down on the screen.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
case began
```

```c
UITouchPhaseBegan
```

## See Also

### Constants
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
- [UITouch.Phase.regionMoved](./regionmoved.md)
  A touch for the given event is within a window on the screen, but has not yet pressed down.
- [UITouch.Phase.regionExited](./regionexited.md)
  A touch for a given event has left a window on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/phase-swift.enum/began)*