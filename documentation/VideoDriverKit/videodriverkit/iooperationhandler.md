# IOOperationHandler

**Framework**: VideoDriverKit  
**Kind**: typealias

A block that tells the device to perform an IOUserVideoIOOperation.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
typedef int (^)(unsigned int, unsigned int, unsigned int, unsigned long long, unsigned long long) IOOperationHandler;
```

#### Discussion

See also `IOUserVideoDevice::SetIOOperationHandler`.

## Parameters

- `in_device`: The object identifier of the device that is performing the IO operation
- `in_io_operation`: The operation that is being performed.
- `in_io_buffer_frame_size`: The number of sample frames that will be processed in the IO operation. For some operations, this is different from the nominal buffer frame size.
- `in_sample_time`: A sample time that indicates the position in the device’s timeline for the operation’s data.

## See Also

- [StartIO](iouservideodevice/startio.md)
  Tells the device to start IO.
- [StopIO](iouservideodevice/stopio.md)
  Tells the device to stop IO.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
- [GetCurrentClientIOTime](iouservideodevice/getcurrentclientiotime.md)
  Gets the current sample/host time pair in the ring buffer written to or read from by the client
- [SetIOOperationHandler](iouservideodevice/setiooperationhandler.md)
  Sets the IOOperationHandler block on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iooperationhandler)*