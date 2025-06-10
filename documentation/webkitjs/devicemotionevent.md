# DeviceMotionEvent

**Framework**: WebKit JS  
**Kind**: cl

An instance of `DeviceMotionEvent` is created when significant change in motion occurs. The event object encapsulates the measurements of the interval, rotation rate, and acceleration of a device. 

**Availability**:
- Safari Mobile 4.2+

## Declaration

```swift
interface DeviceMotionEvent
```

#### Overview

The accelerometer measures the sum of two acceleration vectors: gravity and user acceleration. User acceleration is the acceleration that the user imparts to the device. Because the system is able to track the device’s attitude using both the gyroscope and the accelerometer, it can differentiate between gravity and user acceleration.

You register for these types of events using the window’s `addEventListener` method by passing `devicemotion` as the event type.

## Topics

### Creating Motion Events
- [initDeviceMotionEvent](devicemotionevent/1633270-initdevicemotionevent.md)
  Initializes a new device motion event.
### Getting Motion Event Properties
- [acceleration](devicemotionevent/1629483-acceleration.md)
  The acceleration that the user is giving to the device. 
- [accelerationIncludingGravity](devicemotionevent/1629110-accelerationincludinggravity.md)
  The total acceleration of the device, which includes the user acceleration and the gravity.
- [interval](devicemotionevent/1632148-interval.md)
  The interval in milliseconds since the last device motion event.
- [rotationRate](devicemotionevent/1634377-rotationrate.md)
  The rotation rate of the device.

## Relationships

### Inherits From
- [Event](../tvmljs/event.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/devicemotionevent)*