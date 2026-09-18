# GetCurrentClientIOTime

**Framework**: VideoDriverKit  
**Kind**: method

Gets the current sample/host time pair in the ring buffer written to or read from by the client

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
void GetCurrentClientIOTime(bool in_is_input, uint64_t *out_sample_time, uint64_t *out_host_time);
```

## Parameters

- `in_is_input`: Bool value indicating if client IO time is for input or output. true for input, false for output

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
  A block that tells the device to perform an IOUserVideoIOOperation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/getcurrentclientiotime)*