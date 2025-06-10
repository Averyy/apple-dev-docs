# VisionError

**Framework**: Vision  
**Kind**: enum

The errors that the framework produces.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum VisionError
```

## Topics

### Getting the error
- [VisionError.internalError(_:)](visionerror/internalerror(_:).md)
  An error that indicates the framework produces an internal error.
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
### Getting the invalid error
- [VisionError.invalidArgument(_:)](visionerror/invalidargument(_:).md)
  An error that indicates a request has an invalid value.
- [VisionError.invalidFormat(_:)](visionerror/invalidformat(_:).md)
  An error that indicates a request has data that’s formatted incorrectly.
- [VisionError.invalidImage(_:)](visionerror/invalidimage(_:).md)
  An error that indicates the input image is invalid.
- [VisionError.invalidModel(_:)](visionerror/invalidmodel(_:).md)
  An error that indicates the Core ML model isn’t compatible with the request.
- [VisionError.invalidOperation(_:)](visionerror/invalidoperation(_:).md)
  An error that indicates an app requests an unsupported operation.
### Getting the data-unavailable error
- [VisionError.dataUnavailable(_:)](visionerror/dataunavailable(_:).md)
  An error that indicates the required data is missing.
### Getting the unsupported error
- [VisionError.unsupportedComputeDevice(_:)](visionerror/unsupportedcomputedevice(_:).md)
  An error that indicates an app requests a compute device the framework doesn’t support.
- [VisionError.unsupportedComputeStage(_:)](visionerror/unsupportedcomputestage(_:).md)
  An error that indicates an app requests a compute stage the framework doesn’t support.
- [VisionError.unsupportedRequest(_:)](visionerror/unsupportedrequest(_:).md)
  An error that indicates an app attempts a request the framework doesn’t support.
- [VisionError.unsupportedRevision(_:)](visionerror/unsupportedrevision(_:).md)
  An error that indicates an app specifies a request revision the framework doesn’t support.
### Instance Properties
- [var description: String](visionerror/description.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionerror)*