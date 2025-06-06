# VNErrorCode

**Framework**: Vision  
**Kind**: enum

Constants that identify errors from the framework.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum VNErrorCode
```

## Topics

### Error Codes
- [VNErrorCode.turiCoreErrorCode](vnerrorcode/turicoreerrorcode.md)
  An error occurred during Create ML training due to an invalid transformation or image.
- [VNErrorCode.OK](vnerrorcode/ok.md)
  The operation finished without error.
- [VNErrorCode.dataUnavailable](vnerrorcode/dataunavailable.md)
  The data isn’t available.
- [VNErrorCode.internalError](vnerrorcode/internalerror.md)
  An internal error occurred within the framework.
- [VNErrorCode.invalidArgument](vnerrorcode/invalidargument.md)
  An app passed an invalid parameter to a request.
- [VNErrorCode.invalidFormat](vnerrorcode/invalidformat.md)
  The format of the image is invalid.
- [VNErrorCode.invalidImage](vnerrorcode/invalidimage.md)
  The image is invalid.
- [VNErrorCode.invalidModel](vnerrorcode/invalidmodel.md)
  The Core ML model is incompatible with the request.
- [VNErrorCode.invalidOperation](vnerrorcode/invalidoperation.md)
  An app requested an unsupported operation.
- [VNErrorCode.invalidOption](vnerrorcode/invalidoption.md)
  An app specified an invalid option on a request.
- [VNErrorCode.ioError](vnerrorcode/ioerror.md)
  An I/O error for an image, image sequence, or Core ML model.
- [VNErrorCode.missingOption](vnerrorcode/missingoption.md)
  A request is missing a required option.
- [VNErrorCode.notImplemented](vnerrorcode/notimplemented.md)
  The method isn’t implemented in the underlying model.
- [VNErrorCode.operationFailed](vnerrorcode/operationfailed.md)
  The requested operation failed.
- [VNErrorCode.outOfBoundsError](vnerrorcode/outofboundserror.md)
  An app attempted to access data that’s out-of-bounds.
- [VNErrorCode.outOfMemory](vnerrorcode/outofmemory.md)
  The system doesn’t have enough memory to complete the request.
- [VNErrorCode.requestCancelled](vnerrorcode/requestcancelled.md)
  An app canceled the request.
- [VNErrorCode.timeStampNotFound](vnerrorcode/timestampnotfound.md)
  The system can’t find a timestamp.
- [VNErrorCode.unknownError](vnerrorcode/unknownerror.md)
  An unidentified error occurred.
- [VNErrorCode.unsupportedRevision](vnerrorcode/unsupportedrevision.md)
  An app specified an unsupported request revision.
- [VNErrorCode.unsupportedRequest](vnerrorcode/unsupportedrequest.md)
  An app attempted an unsupported request.
- [VNErrorCode.unsupportedComputeDevice](vnerrorcode/unsupportedcomputedevice.md)
  An app requested an unsupported compute device.
- [VNErrorCode.unsupportedComputeStage](vnerrorcode/unsupportedcomputestage.md)
  An app requested an unsupported compute stage.
- [VNErrorCode.timeout](vnerrorcode/timeout.md)
  The requested operation timed out.
### Creating an Error Code
- [init?(rawValue: Int)](vnerrorcode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let VNErrorDomain: String](vnerrordomain.md)
  The domain of errors that the framework generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnerrorcode)*