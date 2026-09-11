# StopIO

**Framework**: VideoDriverKit  
**Kind**: method

Tells the device to stop IO.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual kern_return_t StopIO(IOUserVideoStartStopFlags in_flags);
```

#### Discussion

The default implementation always returns `kIOReturnSuccess`. Subclass and override this method to handle any hardware specific things when IO is stopping, then call the superclass implementation to update IO state. StopIO will also be called for all streams that were added to the device.

## Parameters

- `in_flags`: IOUserVideoStartStopFlags to indicate how IO is stopping.

## See Also

- [StartIO](iouservideodevice/startio.md)
  Tells the device to start IO.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
- [GetCurrentClientIOTime](iouservideodevice/getcurrentclientiotime.md)
  Gets the current sample/host time pair in the ring buffer written to or read from by the client
- [SetIOOperationHandler](iouservideodevice/setiooperationhandler.md)
  Sets the IOOperationHandler block on the device.
- [IOOperationHandler](videodriverkit/iooperationhandler.md)
  A block that tells the device to perform an IOUserVideoIOOperation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/stopio)*