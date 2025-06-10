# changedTouches

**Framework**: WebKit JS  
**Kind**: instp

A collection of [`Touch`](touch.md) objects representing all touches that changed in this event.

**Availability**:
- Safari Desktop 10.1+
- Safari Mobile 2.0+

## Declaration

```swift
readonly attribute TouchList? changedTouches;
```

#### Discussion

You manipulate this collection using [`TouchList`](touchlist.md) methods.

## See Also

- [altKey](touchevent/1633489-altkey.md)
  A Boolean value indicating whether the alt key is pressed.
- [ctrlKey](touchevent/1629120-ctrlkey.md)
  A Boolean value indicating whether the control key is pressed.
- [metaKey](touchevent/1632828-metakey.md)
  A Boolean value indicating whether the meta key is pressed.
- [shiftKey](touchevent/1634033-shiftkey.md)
  A Boolean value indicating whether the shift key is pressed.
- [targetTouches](touchevent/1632803-targettouches.md)
  A collection of Touch objects representing all touches associated with this target.
- [touches](touchevent/1632644-touches.md)
  A collection of Touch objects representing all touches associated with this event.
- [rotation](touchevent/1634480-rotation.md)
  The delta rotation since the start of an event in degrees where clockwise is positive and counter-clockwise is negative.
- [scale](touchevent/1632169-scale.md)
  The distance between two fingers since the start of an event as a multiplier of the initial distance. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/touchevent/1629351-changedtouches)*