# TouchEvent

**Framework**: Webkitjs  
**Kind**: cl

The `TouchEvent` class encapsulates information about a touch event.

**Availability**:
- Safari Desktop 10.1+
- Safari Mobile 2.0+

## Declaration

```swift
interface TouchEvent
```

#### Overview

The system continually sends `TouchEvent` objects to an application as fingers touch and move across a surface. A touch event provides a snapshot of all touches during a multi-touch sequence, most importantly the touches that are new or have changed for a particular target. A multi-touch sequence begins when a finger first touches the surface. Other fingers may subsequently touch the surface, and all fingers may move across the surface. The sequence ends when the last of these fingers is lifted from the surface. An application receives touch event objects during each phase of any touch.

The different types of `TouchEvent` objects that can occur are:

`TouchEvent` objects are combined together to form high-level `GestureEvent` objects that are also sent during a multi-touch sequence. See [`GestureEvent`](gestureevent.md) for details on `GestureEvent` objects and an example of the events sent for a two finger multi-touch gesture.

## Topics

### Accessing Properties
- [altKey](touchevent/1633489-altkey.md)
  A Boolean value indicating whether the alt key is pressed.
- [ctrlKey](touchevent/1629120-ctrlkey.md)
  A Boolean value indicating whether the control key is pressed.
- [metaKey](touchevent/1632828-metakey.md)
  A Boolean value indicating whether the meta key is pressed.
- [shiftKey](touchevent/1634033-shiftkey.md)
  A Boolean value indicating whether the shift key is pressed.
- [changedTouches](touchevent/1629351-changedtouches.md)
  A collection of [`Touch`](touch.md) objects representing all touches that changed in this event.
- [targetTouches](touchevent/1632803-targettouches.md)
  A collection of Touch objects representing all touches associated with this target.
- [touches](touchevent/1632644-touches.md)
  A collection of Touch objects representing all touches associated with this event.
- [rotation](touchevent/1634480-rotation.md)
  The delta rotation since the start of an event in degrees where clockwise is positive and counter-clockwise is negative.
- [scale](touchevent/1632169-scale.md)
  The distance between two fingers since the start of an event as a multiplier of the initial distance. 
### Initializing
- [initTouchEvent](touchevent/1631943-inittouchevent.md)
  Initializes a newly created `TouchEvent` object.

## Relationships

### Inherits From
- [UIEvent](uievent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/touchevent)*