# IOUserVideoIOOperationWriteEnd

**Framework**: VideoDriverKit  
**Kind**: var

This operation is called just after writing data to the device’s stream buffers.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
constexpr const IOUserVideoIOOperation IOUserVideoIOOperationWriteEnd;
```

#### Discussion

It is required that this operation be handled if the device has output streams.

## See Also

- [IOUserVideoIOOperation](videodriverkit/iouservideoiooperation.md)
  The IO operation being called on the operation handler block.
- [IOUserVideoIOOperationBeginRead](videodriverkit/iouservideoiooperationbeginread.md)
  This operation is called just prior to reading data from the device’s stream buffers.
- [IOOperationHandler](videodriverkit/iooperationhandler.md)
  A block that tells the device to perform an IOUserVideoIOOperation.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoiooperationwriteend)*