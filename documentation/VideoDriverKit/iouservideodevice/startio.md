# StartIO

**Framework**: VideoDriverKit  
**Kind**: method

Tells the device to start IO.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual kern_return_t StartIO(IOUserVideoStartStopFlags in_flags);
```

#### Return Value

A kern_return_t value indicating whether IO started successfully.

#### Discussion

The default implementation always returns `kIOReturnSuccess`. Subclass and override this method to handle any hardware-specific things when IO is starting. Then call the superclass implementation to update IO state. This call always completes with a definitive success or failure result. The hardware can take as long as necessary such that it always either succeeds (and returns `kIOReturnSuccess`) or fails. The system also calls StartIO for all streams added to the device.

## Parameters

- `in_flags`: An IOUserVideoStartStopFlags value that indicates how IO is starting.

## See Also

- [StopIO](iouservideodevice/stopio.md)
  Tells the device to stop IO.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
- [GetCurrentClientIOTime](iouservideodevice/getcurrentclientiotime.md)
  Gets the current sample/host time pair in the ring buffer written to or read from by the client
- [SetIOOperationHandler](iouservideodevice/setiooperationhandler.md)
  Sets the IOOperationHandler block on the device.
- [IOOperationHandler](videodriverkit/iooperationhandler.md)
  A block that tells the device to perform an IOUserVideoIOOperation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/startio)*