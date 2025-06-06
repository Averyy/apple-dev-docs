# Touch

**Framework**: Webkitjs  
**Kind**: cl

A [`Touch`](touch.md) object represents a single user touch on the screen of the device. A touch is the presence or movement of a finger and is part of a unique multi-touch sequence. Use the [`changedTouches`](touchevent/1629351-changedtouches.md) method to get all the touch objects that changed in a [`TouchEvent`](touchevent.md) object.

**Availability**:
- Safari Desktop 10.1+
- Safari Mobile 2.0+

## Declaration

```swift
interface Touch
```

#### Overview

Starting in iOS 9, on devices that support 3D Touch, you can get the [`force`](touch/1630754-force.md) property of the [`Touch`](touch.md) class to obtain a value representing the force at which the user is pressing on the screen. For more information about 3D Touch, see .

## Topics

### Accessing Properties
- [target](touch/1629748-target.md)
  The target of this touch.
- [identifier](touch/1628867-identifier.md)
  The unique identifier for this touch object.
- [clientX](touch/1632255-clientx.md)
  The x-coordinate of the touch’s location relative to the window’s viewport.
- [clientY](touch/1630038-clienty.md)
  The y-coordinate of the touch’s location relative to the window’s viewport.
- [pageX](touch/1629191-pagex.md)
  The x-coordinate of the touch’s location in page coordinates.
- [pageY](touch/1633811-pagey.md)
  The y-coordinate of the touch’s location in page coordinates.
- [screenX](touch/1631242-screenx.md)
  The x-coordinate of the touch’s location in screen coordinates.
- [screenY](touch/1632944-screeny.md)
  The y-coordinate of the touch’s location in screen coordinates.
- [force](touch/1630754-force.md)
  The force of the touch, using a positive linear scale where a value of `0.0` indicates the absence of force.
### Instance Properties
- [altitudeAngle](touch/2871469-altitudeangle.md)
- [azimuthAngle](touch/2871247-azimuthangle.md)
- [radiusX](touch/2871255-radiusx.md)
- [radiusY](touch/2871212-radiusy.md)
- [rotationAngle](touch/2871378-rotationangle.md)
- [touchType](touch/2871460-touchtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/touch)*