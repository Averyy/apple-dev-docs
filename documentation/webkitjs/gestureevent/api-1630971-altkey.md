# altKey

**Framework**: WebKit JS  
**Kind**: instp  
**Role**: Instance Property

A Boolean value indicating whether the alt key is pressed.

**Availability**:
- Safari Desktop 10.1+
- Safari Mobile 2.0+

## Declaration

```
readonly attribute boolean altKey;
```

#### Discussion

If `true`, the alt key is pressed; otherwise, it is not. If there is no keyboard, this value is `false`.

## See Also

### Accessing Properties
- [ctrlKey](./api-1629639-ctrlkey.md)
  A Boolean value indicating whether the control key is pressed.
- [metaKey](./api-1630762-metakey.md)
  A Boolean value indicating whether the meta key is pressed.
- [rotation](./api-1633278-rotation.md)
  The delta rotation since the start of an event, in degrees, where clockwise is positive and counter-clockwise is negative. 
- [scale](./api-1632653-scale.md)
  The distance between two fingers since the start of an event, as a multiplier of the initial distance. 
- [shiftKey](./api-1633677-shiftkey.md)
  A Boolean value indicating whether the shift key is pressed.
- [target](./api-1632473-target.md)
  The target of this gesture.
### Related Documentation
- [Safari Web Content Guide](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/Introduction/Introduction.html#//apple_ref/doc/uid/TP40002051)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/gestureevent/1630971-altkey)*