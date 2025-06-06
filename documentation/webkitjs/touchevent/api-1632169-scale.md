# scale

**Framework**: Webkitjs  
**Kind**: instp

The distance between two fingers since the start of an event as a multiplier of the initial distance. 

**Availability**:
- Safari Desktop 10.1+
- Safari Mobile 2.0+

## Declaration

```swift
readonly attribute float scale;
```

#### Discussion

The initial value is `1.0`. If less than `1.0` the gesture is pinch close to zoom out. If greater than `1.0` the gesture is pinch open to zoom in.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/touchevent/1632169-scale)*