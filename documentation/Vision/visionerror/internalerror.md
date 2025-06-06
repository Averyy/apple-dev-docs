# VisionError.internalError(_:)

**Framework**: Vision  
**Kind**: case

An error that indicates the framework produces an internal error.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
case internalError(String)
```

## See Also

- [VisionError.ioError(_:)](visionerror/ioerror(_:).md)
  An error that indicates an I/O problem for an image, image sequence, or Core ML model.
- [VisionError.operationFailed(_:)](visionerror/operationfailed(_:).md)
  An error that indicates the operation you request fails.
- [VisionError.outOfBoundsError(_:)](visionerror/outofboundserror(_:).md)
  An error that indicates an app attempts to access data that’s out-of-bounds.
- [VisionError.outOfMemory(_:)](visionerror/outofmemory(_:).md)
  An error that indicates there’s not enough memory to perform the operation.
- [VisionError.pixelBufferCreationFailed(_:)](visionerror/pixelbuffercreationfailed(_:).md)
  An error that indicates a problem occurs when creating a pixel buffer.
- [VisionError.requestCancelled(_:)](visionerror/requestcancelled(_:).md)
  An error that indicates an app cancels the request.
- [VisionError.timeStampNotFound(_:)](visionerror/timestampnotfound(_:).md)
  An error that indicates the system can’t find a timestamp.
- [VisionError.timeout(_:)](visionerror/timeout(_:).md)
  An error that indicates an operation times out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionerror/internalerror(_:))*