# IOUserVideoIOOperationBeginRead

**Framework**: VideoDriverKit  
**Kind**: var

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
constexpr const IOUserVideoIOOperation IOUserVideoIOOperationBeginRead;
```

#### Discussion

IOUserVideoIOOperationBeginRead

This operation is called just prior to reading data from the device’s stream buffers. It is required that this operation is handled if the device has input streams.

## See Also

- [IOUserVideoIOOperation](videodriverkit/iouservideoiooperation.md)
- [IOUserVideoIOOperationWriteEnd](videodriverkit/iouservideoiooperationwriteend.md)
- [IOOperationHandler](videodriverkit/iooperationhandler.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoiooperationbeginread)*