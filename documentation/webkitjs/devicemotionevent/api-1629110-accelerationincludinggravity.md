# accelerationIncludingGravity

**Framework**: Webkitjs  
**Kind**: instp

The total acceleration of the device, which includes the user acceleration and the gravity.

**Availability**:
- Safari Mobile 4.2+

## Declaration

```swift
readonly attribute Acceleration accelerationIncludingGravity;
```

#### Discussion

The acceleration data is expressed in m/s^2 and use the `x`, `y`, and `z` axis properties described in [`acceleration`](devicemotionevent/1629483-acceleration.md). This property is never `null` because every Apple device has an accelerometer.

Use the [`acceleration`](devicemotionevent/1629483-acceleration.md) property to get the user acceleration only.

## See Also

- [acceleration](devicemotionevent/1629483-acceleration.md)
  The acceleration that the user is giving to the device. 
- [interval](devicemotionevent/1632148-interval.md)
  The interval in milliseconds since the last device motion event.
- [rotationRate](devicemotionevent/1634377-rotationrate.md)
  The rotation rate of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/devicemotionevent/1629110-accelerationincludinggravity)*