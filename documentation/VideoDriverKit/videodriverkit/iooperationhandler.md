# IOOperationHandler

**Framework**: VideoDriverKit  
**Kind**: typealias

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
typedef int (^)(unsigned int, unsigned int, unsigned int, unsigned long long, unsigned long long) IOOperationHandler;
```

#### Return Value

Returns kern_return_t

#### Discussion

A  block that tells the device to perform an IOUserVideoIOOperation. See IOUserVideoDevice::SetIOOperationHandler

## Parameters

- `in_device`: The IOUserVideoObjectID of the device that is performing the IO operation
- `in_io_operation`: The IOUserVideoIOOperation that is being performed
- `in_io_buffer_frame_size`: uint32_t that specifies the number of sample frames that will be processed in the IO operation. Note that for some operations, this will be different than the nominal buffer frame size
- `in_sample_time`: uint64_t sample time that indicates position in the device’s timeline the data for the IO Operation occurs.

## See Also

- [StartIO](iouservideodevice/startio.md)
- [StopIO](iouservideodevice/stopio.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
- [GetCurrentClientIOTime](iouservideodevice/getcurrentclientiotime.md)
- [SetIOOperationHandler](iouservideodevice/setiooperationhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iooperationhandler)*