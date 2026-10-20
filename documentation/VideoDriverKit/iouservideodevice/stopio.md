# StopIO

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Tells the device to stop IO.

**Availability**:
- DriverKit 27.0+

## Declaration

```cpp
virtual kern_return_t StopIO(IOUserVideoStartStopFlags in_flags);
```

#### Discussion

The default implementation always returns `kIOReturnSuccess`. Subclass and override this method to handle any hardware specific things when IO is stopping, then call the superclass implementation to update IO state. StopIO will also be called for all streams that were added to the device.

## Parameters

- `in_flags`: IOUserVideoStartStopFlags to indicate how IO is stopping.

## See Also

### Performing I/O
- [StartIO](./startio.md)
  Tells the device to start IO.
- [IOUserVideoStartStopFlags](../videodriverkit-page/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
- [GetCurrentClientIOTime](./getcurrentclientiotime.md)
  Gets the current sample/host time pair in the ring buffer written to or read from by the client
- [SetIOOperationHandler](./setiooperationhandler.md)
  Sets the IOOperationHandler block on the device.
- [IOOperationHandler](../videodriverkit-page/iooperationhandler.md)
  A block that tells the device to perform a video IO operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/stopio)*