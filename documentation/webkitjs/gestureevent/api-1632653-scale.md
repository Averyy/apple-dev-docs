# scale

**Framework**: WebKit JS  
**Kind**: instp  
**Role**: Instance Property

The distance between two fingers since the start of an event, as a multiplier of the initial distance. 

**Availability**:
- Safari Desktop 10.1+
- Safari Mobile 2.0+

## Declaration

```
readonly attribute float scale;
```

#### Discussion

The initial value is `1.0`. If less than `1.0`, the gesture is pinch close (to zoom out). If greater than `1.0`, the gesture is pinch open (to zoom in).

## See Also

### Accessing Properties
- [altKey](./api-1630971-altkey.md)
  A Boolean value indicating whether the alt key is pressed.
- [ctrlKey](./api-1629639-ctrlkey.md)
  A Boolean value indicating whether the control key is pressed.
- [metaKey](./api-1630762-metakey.md)
  A Boolean value indicating whether the meta key is pressed.
- [rotation](./api-1633278-rotation.md)
  The delta rotation since the start of an event, in degrees, where clockwise is positive and counter-clockwise is negative. 
- [shiftKey](./api-1633677-shiftkey.md)
  A Boolean value indicating whether the shift key is pressed.
- [target](./api-1632473-target.md)
  The target of this gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/gestureevent/1632653-scale)*