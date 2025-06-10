# dispatchDigitizerEventWithTiltOrientation

**Framework**: Kernel  
**Kind**: instm

Dispatch tablet events with tilt orientation

## Declaration

```swift
virtual void dispatchDigitizerEventWithTiltOrientation( 
 AbsoluteTime timeStamp, 
 UInt32 ID, 
 DigitizerTransducerType type, 
 bool inRange, 
 UInt32 buttonState, 
 IOFixed x, 
 IOFixed y, 
 IOFixed z = 0, 
 IOFixed tipPressure = 0, // 0.0-1.0 in 16:16 fixed 
 IOFixed auxPressure = 0, // 0.0-1.0 in 16:16 fixed 
 IOFixed twist = 0, 
 IOFixed tiltX = 0, 
 IOFixed tiltY = 0, 
 IOOptionBits options = 0 );
```

#### Overview

This is meant to be used with transducers that leverage tilt orientation

## Parameters

- `timeStamp`: AbsoluteTime representing origination of event
- `ID`: ID of the transducer generating the event
- `type`: Type of the transducer generating the event
- `inRange`: Details whether the transducer is in promitity to digitizer surface
- `buttonState`: Button mask where bit0 is the primary button, bit1 secondary and so forth
- `x`: Absolute location of transducer along the x-axis from 0.0 to 1.0 in 16:16 fixed point.
- `y`: Absolute location of transducer along the y-axis from 0.0 to 1.0 in 16:16 fixed point.
- `z`: Absolute location of transducer along the z-axis from 0.0 to 1.0 in 16:16 fixed point. This is typically used to determine the distance between the transducer and surface
- `tipPressure`: Absolute pressure exerted on surface by tip from 0.0 to 1.0 in 16:16 fixed point.
- `auxPressure`: Absolute pressure exerted on transducer from 0.0 to 1.0 in 16:16 fixed point.
- `twist`: Absolute clockwise rotation along the transducer's major axis from 0.0 to 360.0 degrees in 16:16 fixed point.
- `tiltX`: Absolute plane angle between the Y-Z plane and the plane containing the transducer axis and the Y axis. A positive X tilt is to the right. Value is represented in degrees from -90.0 to 90.0 in 16:16 fixed point.
- `tiltY`: Absolute plane angle between the X-Z plane and the plane containing the transducer axis and the X axis. A positive Y tilt is towards the user. Value is represented in degrees from -90.0 to 90.0 in 16:16 fixed point.
- `options`: Additional options to be used when dispatching event.

## See Also

- [dispatchDigitizerEvent](iohideventservice/1812711-dispatchdigitizerevent.md)
  Dispatch tablet events without orientation
- [dispatchDigitizerEventWithPolarOrientation](iohideventservice/1812728-dispatchdigitizereventwithpolaro.md)
  Dispatch tablet events with polar orientation
- [dispatchMultiAxisPointerEvent](iohideventservice/1812745-dispatchmultiaxispointerevent.md)
  Dispatch multi-axis pointer event
- [handleClose](iohideventservice/1812757-handleclose.md)
  Handle a client close on the interface.
- [handleIsOpen](iohideventservice/1812770-handleisopen.md)
  Query whether a client has an open on the interface.
- [handleOpen](iohideventservice/1812786-handleopen.md)
  Handle a client open on the interface.
- [handleStart](iohideventservice/1812803-handlestart.md)
  Prepare the hardware and driver to support I/O operations.
- [handleStop](iohideventservice/1812816-handlestop.md)
  Quiesce the hardware and stop the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventservice/1812735-dispatchdigitizereventwithtiltor)*