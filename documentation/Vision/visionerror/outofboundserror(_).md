# VisionError.outOfBoundsError(_:)

**Framework**: Vision  
**Kind**: case  
**Role**: Case

An error that indicates an app attempts to access data that’s out-of-bounds.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
case outOfBoundsError(String)
```

## See Also

### Getting the error
- [VisionError.internalError(_:)](./internalerror%28_%29.md)
  An error that indicates the framework produces an internal error.
- [VisionError.ioError(_:)](./ioerror%28_%29.md)
  An error that indicates an I/O problem for an image, image sequence, or Core ML model.
- [VisionError.operationFailed(_:)](./operationfailed%28_%29.md)
  An error that indicates the operation you request fails.
- [VisionError.outOfMemory(_:)](./outofmemory%28_%29.md)
  An error that indicates there’s not enough memory to perform the operation.
- [VisionError.pixelBufferCreationFailed(_:)](./pixelbuffercreationfailed%28_%29.md)
  An error that indicates a problem occurs when creating a pixel buffer.
- [VisionError.requestCancelled(_:)](./requestcancelled%28_%29.md)
  An error that indicates an app cancels the request.
- [VisionError.timeStampNotFound(_:)](./timestampnotfound%28_%29.md)
  An error that indicates the system can’t find a timestamp.
- [VisionError.timeout(_:)](./timeout%28_%29.md)
  An error that indicates an operation times out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionerror/outofboundserror(_:))*