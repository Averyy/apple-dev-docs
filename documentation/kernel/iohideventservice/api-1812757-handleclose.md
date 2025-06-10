# handleClose

**Framework**: Kernel  
**Kind**: instm

Handle a client close on the interface.

## Declaration

```swift
virtual void handleClose(
 IOService *client,
 IOOptionBitsoptions);
```

#### Overview

This method is called by IOService::close() with the arbitration lock held. This method will in turn call handleClientClose() to notify interested subclasses about the client close. If this represents the last close, then the interface will also close the controller before this method returns. The controllerWillClose() method will be called before closing the controller. Subclasses should not override this method.

## Parameters

- `client`: The client object that requested the close.
- `options`: Options passed to IOService::close().

## See Also

- [dispatchDigitizerEvent](iohideventservice/1812711-dispatchdigitizerevent.md)
  Dispatch tablet events without orientation
- [dispatchDigitizerEventWithPolarOrientation](iohideventservice/1812728-dispatchdigitizereventwithpolaro.md)
  Dispatch tablet events with polar orientation
- [dispatchDigitizerEventWithTiltOrientation](iohideventservice/1812735-dispatchdigitizereventwithtiltor.md)
  Dispatch tablet events with tilt orientation
- [dispatchMultiAxisPointerEvent](iohideventservice/1812745-dispatchmultiaxispointerevent.md)
  Dispatch multi-axis pointer event
- [handleIsOpen](iohideventservice/1812770-handleisopen.md)
  Query whether a client has an open on the interface.
- [handleOpen](iohideventservice/1812786-handleopen.md)
  Handle a client open on the interface.
- [handleStart](iohideventservice/1812803-handlestart.md)
  Prepare the hardware and driver to support I/O operations.
- [handleStop](iohideventservice/1812816-handlestop.md)
  Quiesce the hardware and stop the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventservice/1812757-handleclose)*