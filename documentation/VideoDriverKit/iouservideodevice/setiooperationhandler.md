# SetIOOperationHandler

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetIOOperationHandler(IOOperationHandler in_io_operation_block);
```

#### Return Value

Returns kIOReturnSuccess if the IOOperationHandler block was successfuly set on the device

#### Discussion

Set the IOOperationHandler block on the device.

The IOOperationHandler will be invoked when a IO operation is performed by the host. The handler will be called on a real time priority thread, so any work should only call real-time safe operations and never block. Many of the calls to various IOUserVideoObjects are syncrhonized against the work queue, so any necessary information to perform IO should be cached and captured in the block.

## Parameters

- `in_io_operation_block`: The IOOperationHandler block to be called when the host performs an IO operation.

## See Also

- [StartIO](iouservideodevice/startio.md)
- [StopIO](iouservideodevice/stopio.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
- [GetCurrentClientIOTime](iouservideodevice/getcurrentclientiotime.md)
- [IOOperationHandler](videodriverkit/iooperationhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setiooperationhandler)*