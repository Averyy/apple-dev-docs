# scale

**Framework**: WebKit JS  
**Kind**: instp

The distance between two fingers since the start of an event, as a multiplier of the initial distance. 

**Availability**:
- Safari Desktop 10.1+
- Safari Mobile 2.0+

## Declaration

```swift
readonly attribute float scale;
```

#### Discussion

The initial value is `1.0`. If less than `1.0`, the gesture is pinch close (to zoom out). If greater than `1.0`, the gesture is pinch open (to zoom in).

## See Also

- [altKey](gestureevent/1630971-altkey.md)
  A Boolean value indicating whether the alt key is pressed.
- [ctrlKey](gestureevent/1629639-ctrlkey.md)
  A Boolean value indicating whether the control key is pressed.
- [metaKey](gestureevent/1630762-metakey.md)
  A Boolean value indicating whether the meta key is pressed.
- [rotation](gestureevent/1633278-rotation.md)
  The delta rotation since the start of an event, in degrees, where clockwise is positive and counter-clockwise is negative. 
- [shiftKey](gestureevent/1633677-shiftkey.md)
  A Boolean value indicating whether the shift key is pressed.
- [target](gestureevent/1632473-target.md)
  The target of this gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/gestureevent/1632653-scale)*