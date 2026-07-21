# GetCurrentClientIOTime

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
void GetCurrentClientIOTime(bool in_is_input, uint64_t *out_sample_time, uint64_t *out_host_time);
```

#### Discussion

Get the current sample/host time pair in the ring buffer written to or read from by the client

## Parameters

- `in_is_input`: Bool value indicating if client IO time is for input or output.  true for input, false for output

## See Also

- [StartIO](iouservideodevice/startio.md)
- [StopIO](iouservideodevice/stopio.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
- [SetIOOperationHandler](iouservideodevice/setiooperationhandler.md)
- [IOOperationHandler](videodriverkit/iooperationhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/getcurrentclientiotime)*