# IOUserVideoIOOperation

**Framework**: VideoDriverKit  
**Kind**: typealias  
**Role**: Type Alias

The IO operation being called on the operation handler block.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
typedef uint32_t IOUserVideoIOOperation;
```

#### Discussion

This value is used with [`IOOperationHandler`](./iooperationhandler.md).

## See Also

### Working with I/O operations
- [IOUserVideoIOOperationBeginRead](./iouservideoiooperationbeginread.md)
  This operation is called just prior to reading data from the device’s stream buffers.
- [IOUserVideoIOOperationWriteEnd](./iouservideoiooperationwriteend.md)
  This operation is called just after writing data to the device’s stream buffers.
- [IOOperationHandler](./iooperationhandler.md)
  A block that tells the device to perform a video IO operation.
- [IOUserVideoStartStopFlags](./iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoiooperation)*