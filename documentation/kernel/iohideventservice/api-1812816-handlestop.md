# handleStop

**Framework**: Kernel  
**Kind**: instm

Quiesce the hardware and stop the driver.

## Declaration

```cpp
virtual void handleStop(
 IOService *provider );
```

## Overview

IOHIDEventService will call this method from stop() to signal that the hardware should be quiesced and the driver stopped. A subclass that overrides this method should end its implementation by calling the version in super.

## Parameters

- `provider`: The provider argument passed to stop().

## See Also

### Miscellaneous
- [dispatchDigitizerEvent](./api-1812711-dispatchdigitizerevent.md)
  Dispatch tablet events without orientation
- [dispatchDigitizerEventWithPolarOrientation](./api-1812728-dispatchdigitizereventwithpolaro.md)
  Dispatch tablet events with polar orientation
- [dispatchDigitizerEventWithTiltOrientation](./api-1812735-dispatchdigitizereventwithtiltor.md)
  Dispatch tablet events with tilt orientation
- [dispatchMultiAxisPointerEvent](./api-1812745-dispatchmultiaxispointerevent.md)
  Dispatch multi-axis pointer event
- [handleClose](./api-1812757-handleclose.md)
  Handle a client close on the interface.
- [handleIsOpen](./api-1812770-handleisopen.md)
  Query whether a client has an open on the interface.
- [handleOpen](./api-1812786-handleopen.md)
  Handle a client open on the interface.
- [handleStart](./api-1812803-handlestart.md)
  Prepare the hardware and driver to support I/O operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventservice/1812816-handlestop)*