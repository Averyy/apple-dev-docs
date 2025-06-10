# handleIsOpen

**Framework**: Kernel  
**Kind**: instm

Query whether a client has an open on the interface.

## Declaration

```swift
virtual bool handleIsOpen(
 const IOService *client) const;
```

#### Return_value

true if the specified client, or any client if none (0) is specified, presently has an open on this object.

#### Overview

This method is always called by IOService with the arbitration lock held. Subclasses should not override this method.

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
- [handleOpen](iohideventservice/1812786-handleopen.md)
  Handle a client open on the interface.
- [handleStart](iohideventservice/1812803-handlestart.md)
  Prepare the hardware and driver to support I/O operations.
- [handleStop](iohideventservice/1812816-handlestop.md)
  Quiesce the hardware and stop the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventservice/1812770-handleisopen)*