# GestureEvent

**Framework**: WebKit JS  
**Kind**: cl

The `GestureEvent` class encapsulates information about a multi-touch gesture.

**Availability**:
- Safari Desktop 10.1+
- Safari Mobile 2.0+

## Declaration

```swift
interface GestureEvent
```

#### Overview

`GestureEvent` objects are high-level events that encapsulate the low-level [`TouchEvent`](touchevent.md) objects. Both `GestureEvent` and `TouchEvent` events are sent during a multi-touch sequence. Gesture events contain scaling and rotation information allowing gestures to be combined, if supported by the platform. If not supported, one gesture ends before another starts. Listen for `GestureEvent` events if you want to respond to gestures only, not process the low-level `TouchEvent` objects.

The different types of `GestureEvent` objects that can occur are:

For example, for a two finger multi-touch gesture, the events occur in the following sequence:

1. `touchstart` for finger 1. Sent when the first finger touches the surface.
2. `gesturestart`. Sent when the second finger touches the surface.
3. `touchstart` for finger 2. Sent immediately after `gesturestart` when the second finger touches the surface.
4. `gesturechange` for current gesture. Sent when both fingers move while still touching the surface.
5. `gestureend`. Sent when the second finger lifts from the surface.
6. `touchend` for finger 2. Sent immediately after `gestureend` when the second finger lifts from the surface.
7. `touchend` for finger 1. Sent when the first finger lifts from the surface.

See [`TouchEvent`](touchevent.md) if you want to process just low-level `TouchEvent` objects.

## Topics

### Accessing Properties
- [altKey](gestureevent/1630971-altkey.md)
  A Boolean value indicating whether the alt key is pressed.
- [ctrlKey](gestureevent/1629639-ctrlkey.md)
  A Boolean value indicating whether the control key is pressed.
- [metaKey](gestureevent/1630762-metakey.md)
  A Boolean value indicating whether the meta key is pressed.
- [rotation](gestureevent/1633278-rotation.md)
  The delta rotation since the start of an event, in degrees, where clockwise is positive and counter-clockwise is negative. 
- [scale](gestureevent/1632653-scale.md)
  The distance between two fingers since the start of an event, as a multiplier of the initial distance. 
- [shiftKey](gestureevent/1633677-shiftkey.md)
  A Boolean value indicating whether the shift key is pressed.
- [target](gestureevent/1632473-target.md)
  The target of this gesture.
### Initializing
- [initGestureEvent](gestureevent/1634533-initgestureevent.md)
  Initializes a newly created `GestureEvent` object.
### Instance Properties
- [clientX](gestureevent/1777782-clientx.md)
- [clientY](gestureevent/1777798-clienty.md)
- [screenX](gestureevent/1777860-screenx.md)
- [screenY](gestureevent/1777971-screeny.md)

## Relationships

### Inherits From
- [UIEvent](uievent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/gestureevent)*