# IOUserVideoIOOperation

**Framework**: VideoDriverKit  
**Kind**: typealias

The IO operation being called on the operation handler block.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
typedef uint32_t IOUserVideoIOOperation;
```

#### Discussion

This value is used with [`IOOperationHandler`](videodriverkit/iooperationhandler.md).

## See Also

- [IOUserVideoIOOperationBeginRead](videodriverkit/iouservideoiooperationbeginread.md)
  This operation is called just prior to reading data from the device’s stream buffers.
- [IOUserVideoIOOperationWriteEnd](videodriverkit/iouservideoiooperationwriteend.md)
  This operation is called just after writing data to the device’s stream buffers.
- [IOOperationHandler](videodriverkit/iooperationhandler.md)
  A block that tells the device to perform an IOUserVideoIOOperation.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoiooperation)*