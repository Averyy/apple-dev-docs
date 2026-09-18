# SetIOOperationHandler

**Framework**: VideoDriverKit  
**Kind**: method

Sets the IOOperationHandler block on the device.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetIOOperationHandler(IOOperationHandler in_io_operation_block);
```

#### Return Value

`kIOReturnSuccess` if the IOOperationHandler block was successfuly set on the device

#### Discussion

The IOOperationHandler will be invoked when a IO operation is performed by the host. The handler will be called on a real time priority thread, so any work should only call real-time safe operations and never block. Many of the calls to various IOUserVideoObjects are syncrhonized against the work queue, so any necessary information to perform IO should be cached and captured in the block.

## Parameters

- `in_io_operation_block`: The IOOperationHandler block to be called when the host performs an IO operation.

## See Also

- [StartIO](iouservideodevice/startio.md)
  Tells the device to start IO.
- [StopIO](iouservideodevice/stopio.md)
  Tells the device to stop IO.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
- [GetCurrentClientIOTime](iouservideodevice/getcurrentclientiotime.md)
  Gets the current sample/host time pair in the ring buffer written to or read from by the client
- [IOOperationHandler](videodriverkit/iooperationhandler.md)
  A block that tells the device to perform an IOUserVideoIOOperation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setiooperationhandler)*