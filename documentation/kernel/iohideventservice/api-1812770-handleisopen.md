# handleIsOpen

**Framework**: Kernel  
**Kind**: instm

Query whether a client has an open on the interface.

## Declaration

```cpp
virtual bool handleIsOpen(
 const IOService *client) const;
```

#### Return Value

true if the specified client, or any client if none (0) is specified, presently has an open on this object.

#### Overview

This method is always called by IOService with the arbitration lock held. Subclasses should not override this method.

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
- [handleOpen](./api-1812786-handleopen.md)
  Handle a client open on the interface.
- [handleStart](./api-1812803-handlestart.md)
  Prepare the hardware and driver to support I/O operations.
- [handleStop](./api-1812816-handlestop.md)
  Quiesce the hardware and stop the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventservice/1812770-handleisopen)*