# acceleration

**Framework**: WebKit JS  
**Kind**: instp

The acceleration that the user is giving to the device. 

**Availability**:
- Safari Mobile 4.2+

## Declaration

```swift
readonly attribute Acceleration acceleration;
```

#### Discussion

The acceleration data are expressed in m/s^2 and use the following `x`, `y`, and `z` axis properties represented as doubles:

- **x**: In the plane of the screen, positive towards the right side of the screen.
- **y**: In the plane of the screen, positive towards the top of the screen.
- **z**: Perpendicular to the screen, positive out of the screen. 

This property is `null` if the device cannot provide the user acceleration—that is, if the device does not have a gyroscope. 

Use the [`accelerationIncludingGravity`](devicemotionevent/1629110-accelerationincludinggravity.md) property to get the total acceleration.

> **Note**: If the device does not have a gyroscope, then you may need to implement your own gravity direction detection using a low pass filter.

## See Also

- [accelerationIncludingGravity](devicemotionevent/1629110-accelerationincludinggravity.md)
  The total acceleration of the device, which includes the user acceleration and the gravity.
- [interval](devicemotionevent/1632148-interval.md)
  The interval in milliseconds since the last device motion event.
- [rotationRate](devicemotionevent/1634377-rotationrate.md)
  The rotation rate of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/devicemotionevent/1629483-acceleration)*