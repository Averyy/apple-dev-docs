# rotationRate

**Framework**: Webkitjs  
**Kind**: instp

The rotation rate of the device.

**Availability**:
- Safari Mobile 4.2+

## Declaration

```swift
readonly attribute RotationRate rotationRate;
```

#### Discussion

The `RotationRate` object specifies the device’s rate of rotation around three axes. It contains `alpha`, `beta`, and `gamma` properties represented as doubles as described in [`DeviceOrientationEvent`](deviceorientationevent.md).

This property is `null` if the device cannot provide the rate of rotation—that is, if the device does not have a gyroscope. 

## See Also

- [acceleration](devicemotionevent/1629483-acceleration.md)
  The acceleration that the user is giving to the device. 
- [accelerationIncludingGravity](devicemotionevent/1629110-accelerationincludinggravity.md)
  The total acceleration of the device, which includes the user acceleration and the gravity.
- [interval](devicemotionevent/1632148-interval.md)
  The interval in milliseconds since the last device motion event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/devicemotionevent/1634377-rotationrate)*