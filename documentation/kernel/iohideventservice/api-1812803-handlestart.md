# handleStart

**Framework**: Kernel  
**Kind**: instm

Prepare the hardware and driver to support I/O operations.

## Declaration

```swift
virtual bool handleStart(
 IOService *provider );
```

#### Return_value

True on success, or false otherwise. Returning false will cause start() to fail and return false.

#### Overview

IOHIDEventService will call this method from start() before any I/O operations are issued to the concrete subclass. Methods such as getReportElements() are only called after handleStart() has returned true. A subclass that overrides this method should begin its implementation by calling the version in super, and then check the return value.

## Parameters

- `provider`: The provider argument passed to start().

## See Also

- [dispatchDigitizerEvent](iohideventservice/1812711-dispatchdigitizerevent.md)
  Dispatch tablet events without orientation
- [dispatchDigitizerEventWithPolarOrientation](iohideventservice/1812728-dispatchdigitizereventwithpolaro.md)
  Dispatch tablet events with polar orientation
- [dispatchDigitizerEventWithTiltOrientation](iohideventservice/1812735-dispatchdigitizereventwithtiltor.md)
  Dispatch tablet events with tilt orientation
- [dispatchMultiAxisPointerEvent](iohideventservice/1812745-dispatchmultiaxispointerevent.md)
  Dispatch multi-axis pointer event
- [handleClose](iohideventservice/1812757-handleclose.md)
  Handle a client close on the interface.
- [handleIsOpen](iohideventservice/1812770-handleisopen.md)
  Query whether a client has an open on the interface.
- [handleOpen](iohideventservice/1812786-handleopen.md)
  Handle a client open on the interface.
- [handleStop](iohideventservice/1812816-handlestop.md)
  Quiesce the hardware and stop the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventservice/1812803-handlestart)*