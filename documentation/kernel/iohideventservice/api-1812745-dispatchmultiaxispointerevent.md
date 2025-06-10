# dispatchMultiAxisPointerEvent

**Framework**: Kernel  
**Kind**: instm

Dispatch multi-axis pointer event

## Declaration

```swift
virtual void dispatchMultiAxisPointerEvent( 
 AbsoluteTime timeStamp, 
 UInt32 buttonState, 
 IOFixed x, 
 IOFixed y, 
 IOFixed z, 
 IOFixed rX = 0, 
 IOFixed rY = 0, 
 IOFixed rZ = 0, 
 IOOptionBits options = 0 );
```

#### Overview

This is meant to be used with joysticks or multi-axis pointer devices such as those with with 6 degrees of freedom. This function will generate related relative pointer and scroll event associated with movement.

## Parameters

- `timeStamp`: AbsoluteTime representing origination of event
- `buttonState`: Button mask where bit0 is the primary button, bit1 secondary and so forth
- `x`: Absolute location of pointer along the x-axis from -1.0 to 1.0 in 16:16 fixed point.
- `y`: Absolute location of pointer along the y-axis from -1.0 to 1.0 in 16:16 fixed point.
- `z`: Absolute location of pointer along the z-axis from -1.0 to 1.0 in 16:16 fixed point.
- `rX`: Absolute rotation of pointer around the x-axis from -1.0 to 1.0 in 16:16 fixed point.
- `rY`: Absolute rotation of pointer around the y-axis from -1.0 to 1.0 in 16:16 fixed point.
- `rZ`: Absolute rotation of pointer around the z-axis from -1.0 to 1.0 in 16:16 fixed point.
- `options`: Additional options to be used when dispatching event such as leveraging rotational axis for translation or using the z axis for vertical scrolling.

## See Also

- [dispatchDigitizerEvent](iohideventservice/1812711-dispatchdigitizerevent.md)
  Dispatch tablet events without orientation
- [dispatchDigitizerEventWithPolarOrientation](iohideventservice/1812728-dispatchdigitizereventwithpolaro.md)
  Dispatch tablet events with polar orientation
- [dispatchDigitizerEventWithTiltOrientation](iohideventservice/1812735-dispatchdigitizereventwithtiltor.md)
  Dispatch tablet events with tilt orientation
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventservice/1812745-dispatchmultiaxispointerevent)*