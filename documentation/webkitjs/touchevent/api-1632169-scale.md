# scale

**Framework**: WebKit JS  
**Kind**: instp  
**Role**: Instance Property

The distance between two fingers since the start of an event as a multiplier of the initial distance. 

**Availability**:
- Safari Desktop 10.1+
- Safari Mobile 2.0+

## Declaration

```
readonly attribute float scale;
```

#### Discussion

The initial value is `1.0`. If less than `1.0` the gesture is pinch close to zoom out. If greater than `1.0` the gesture is pinch open to zoom in.

## See Also

### Accessing Properties
- [altKey](./api-1633489-altkey.md)
  A Boolean value indicating whether the alt key is pressed.
- [ctrlKey](./api-1629120-ctrlkey.md)
  A Boolean value indicating whether the control key is pressed.
- [metaKey](./api-1632828-metakey.md)
  A Boolean value indicating whether the meta key is pressed.
- [shiftKey](./api-1634033-shiftkey.md)
  A Boolean value indicating whether the shift key is pressed.
- [changedTouches](./api-1629351-changedtouches.md)
  A collection of [`Touch`](../touch.md) objects representing all touches that changed in this event.
- [targetTouches](./api-1632803-targettouches.md)
  A collection of Touch objects representing all touches associated with this target.
- [touches](./api-1632644-touches.md)
  A collection of Touch objects representing all touches associated with this event.
- [rotation](./api-1634480-rotation.md)
  The delta rotation since the start of an event in degrees where clockwise is positive and counter-clockwise is negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/touchevent/1632169-scale)*