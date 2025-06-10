# handleOpen

**Framework**: Kernel  
**Kind**: instm

Handle a client open on the interface.

## Declaration

```swift
virtual bool handleOpen(
 IOService *client, 
 IOOptionBitsoptions, 
 void *argument);
```

#### Return_value

true to accept the client open, false otherwise.

#### Overview

This method is called by IOService::open() with the arbitration lock held, and must return true to accept the client open. This method will in turn call handleClientOpen() to qualify the client requesting the open.

## Parameters

- `client`: The client object that requested the open.
- `options`: Options passed to IOService::open().
- `argument`: Argument passed to IOService::open().

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
- [handleStart](iohideventservice/1812803-handlestart.md)
  Prepare the hardware and driver to support I/O operations.
- [handleStop](iohideventservice/1812816-handlestop.md)
  Quiesce the hardware and stop the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventservice/1812786-handleopen)*