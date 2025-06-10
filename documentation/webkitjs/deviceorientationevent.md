# DeviceOrientationEvent

**Framework**: WebKit JS  
**Kind**: cl

Instances of the `DeviceOrientationEvent` class are fired only when the device has a gyroscope and while the user is changing the orientation. The `DeviceOrientationEvent` class encapsulates the angles of rotation in degrees and heading. 

**Availability**:
- Safari Mobile 4.2+

## Declaration

```swift
interface DeviceOrientationEvent
```

#### Overview

The angles of rotation—the [`alpha`](deviceorientationevent/1629200-alpha.md), [`beta`](deviceorientationevent/1631254-beta.md), and [`gamma`](deviceorientationevent/1631656-gamma.md) properties—do not represent the real world orientation. They are defined as an offset from an arbitrary direction—typically, the direction in which the device was held when the orientation was first obtained. Therefore, you can only use the angles to track changes in orientation, you cannot derive the direction in which the device is currently facing. To track changes, save the first device orientation event and use it as a reference for subsequent values. If you want a real world heading, use the [`webkitCompassHeading`](deviceorientationevent/1804777-webkitcompassheading.md) property.

Because some devices may not have a gyroscope, you can listen for this event. If it does not occur, use the  [`DeviceMotionEvent`](devicemotionevent.md) class to receive raw accelerometer events. From these events you can determine an approximate orientation.

You register for device orientation events using the window’s `addEventListener` method by passing `deviceorientation` as the event type.

## Topics

### Creating Orientation Events
- [initDeviceOrientationEvent](deviceorientationevent/1629184-initdeviceorientationevent.md)
  Initializes a new device orientation event.
### Getting Orientation Event Properties
- [alpha](deviceorientationevent/1629200-alpha.md)
  The rotation, in degrees, of the device frame around its z-axis.
- [beta](deviceorientationevent/1631254-beta.md)
  The rotation, in degrees, of the device frame around its x-axis.
- [gamma](deviceorientationevent/1631656-gamma.md)
  The rotation, in degrees, of the device frame around its y-axis.
### Getting Compass Properties
- [webkitCompassAccuracy](deviceorientationevent/1804769-webkitcompassaccuracy.md)
  The accuracy of the compass data in degrees.
- [webkitCompassHeading](deviceorientationevent/1804777-webkitcompassheading.md)
  A direction that is measured in degrees relative to magnetic north.
### Instance Properties
- [absolute](deviceorientationevent/1632681-absolute.md)

## Relationships

### Inherits From
- [Event](../tvmljs/event.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/deviceorientationevent)*