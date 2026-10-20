# IOUserVideoIOOperationBeginRead

**Framework**: VideoDriverKit  
**Kind**: var  
**Role**: Global Variable

This operation is called just prior to reading data from the device’s stream buffers.

**Availability**:
- DriverKit 27.0+

## Declaration

```cpp
constexpr const IOUserVideoIOOperation IOUserVideoIOOperationBeginRead;
```

#### Discussion

It is required that this operation is handled if the device has input streams.

## See Also

### Working with I/O operations
- [IOUserVideoIOOperation](./iouservideoiooperation.md)
  The IO operation being called on the operation handler block.
- [IOUserVideoIOOperationWriteEnd](./iouservideoiooperationwriteend.md)
  This operation is called just after writing data to the device’s stream buffers.
- [IOOperationHandler](./iooperationhandler.md)
  A block that tells the device to perform a video IO operation.
- [IOUserVideoStartStopFlags](./iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoiooperationbeginread)*