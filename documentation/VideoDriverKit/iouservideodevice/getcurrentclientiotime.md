# GetCurrentClientIOTime

**Framework**: VideoDriverKit  
**Kind**: method

Gets the current sample/host time pair in the ring buffer written to or read from by the client

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
void GetCurrentClientIOTime(bool in_is_input, uint64_t *out_sample_time, uint64_t *out_host_time);
```

## Parameters

- `in_is_input`: A Boolean value that indicates whether client IO time is for input.  A false value indicates that the time is for output.
- `out_sample_time`: The buffer to set with the current IO sample time of the client.
- `out_host_time`: The buffer to set with the current IO host time of the client.

## See Also

- [StartIO](iouservideodevice/startio.md)
  Tells the device to start IO.
- [StopIO](iouservideodevice/stopio.md)
  Tells the device to stop IO.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
- [SetIOOperationHandler](iouservideodevice/setiooperationhandler.md)
  Sets the IOOperationHandler block on the device.
- [IOOperationHandler](videodriverkit/iooperationhandler.md)
  A block that tells the device to perform a video IO operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/getcurrentclientiotime)*