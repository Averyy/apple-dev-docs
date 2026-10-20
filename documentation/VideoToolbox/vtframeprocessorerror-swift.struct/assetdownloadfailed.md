# assetDownloadFailed

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
static var assetDownloadFailed: VTFrameProcessorError.Code { get }
```

## See Also

### Errors
- [static var fatalError: VTFrameProcessorError.Code](./fatalerror.md)
  A fatal error occurred during processing.
- [static var initializationFailed: VTFrameProcessorError.Code](./initializationfailed.md)
  The session failed to initialize the processing pipeline.
- [static var invalidFrameTiming: VTFrameProcessorError.Code](./invalidframetiming.md)
  A provided frame object has a presentation time stamp which isn’t supported by the processor.
- [static var invalidParameterError: VTFrameProcessorError.Code](./invalidparametererror.md)
  A provided parameter isn’t valid.
- [static var memoryAllocationFailure: VTFrameProcessorError.Code](./memoryallocationfailure.md)
  The session or processor is unable to allocate the required memory.
- [static var processingError: VTFrameProcessorError.Code](./processingerror.md)
  The processor encountered an issue that prevents it from processing the provided frame.
- [static var revisionNotSupported: VTFrameProcessorError.Code](./revisionnotsupported.md)
  The specified revision isn’t supported by the configured processor.
- [static var sessionAlreadyActive: VTFrameProcessorError.Code](./sessionalreadyactive.md)
  An attempt is made to start a session that is already started.
- [static var sessionLevelError: VTFrameProcessorError.Code](./sessionlevelerror.md)
  The processing failed and current session should be stopped.
- [static var sessionNotStarted: VTFrameProcessorError.Code](./sessionnotstarted.md)
  The session is used to process frames without being started.
- [static var unknownError: VTFrameProcessorError.Code](./unknownerror.md)
  The processor failed for an unknown reason.
- [static var unsupportedInput: VTFrameProcessorError.Code](./unsupportedinput.md)
  One or more frames is in a format which isn’t supported by the processor.
- [static var unsupportedResolution: VTFrameProcessorError.Code](./unsupportedresolution.md)
  The processor failed due to an unsupported resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorerror-swift.struct/assetdownloadfailed)*