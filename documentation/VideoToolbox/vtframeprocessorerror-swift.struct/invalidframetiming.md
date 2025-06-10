# invalidFrameTiming

**Framework**: Video Toolbox  
**Kind**: property

A provided frame object has a presentation time stamp which isn’t supported by the processor.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
static var invalidFrameTiming: VTFrameProcessorError.Code { get }
```

#### Discussion

The time stamp is either invalid or out-of-order.

## See Also

- [static var fatalError: VTFrameProcessorError.Code](vtframeprocessorerror-swift.struct/fatalerror.md)
  A fatal error occurred during processing.
- [static var initializationFailed: VTFrameProcessorError.Code](vtframeprocessorerror-swift.struct/initializationfailed.md)
  The session failed to initialize the processing pipeline.
- [static var invalidParameterError: VTFrameProcessorError.Code](vtframeprocessorerror-swift.struct/invalidparametererror.md)
  A provided parameter isn’t valid.
- [static var memoryAllocationFailure: VTFrameProcessorError.Code](vtframeprocessorerror-swift.struct/memoryallocationfailure.md)
  The session or processor is unable to allocate the required memory.
- [static var processingError: VTFrameProcessorError.Code](vtframeprocessorerror-swift.struct/processingerror.md)
  The processor encountered an issue that prevents it from processing the provided frame.
- [static var revisionNotSupported: VTFrameProcessorError.Code](vtframeprocessorerror-swift.struct/revisionnotsupported.md)
  The specified revision isn’t supported by the configured processor.
- [static var sessionAlreadyActive: VTFrameProcessorError.Code](vtframeprocessorerror-swift.struct/sessionalreadyactive.md)
  An attempt is made to start a session that is already started.
- [static var sessionLevelError: VTFrameProcessorError.Code](vtframeprocessorerror-swift.struct/sessionlevelerror.md)
  The processing failed and current session should be stopped.
- [static var sessionNotStarted: VTFrameProcessorError.Code](vtframeprocessorerror-swift.struct/sessionnotstarted.md)
  The session is used to process frames without being started.
- [static var unknownError: VTFrameProcessorError.Code](vtframeprocessorerror-swift.struct/unknownerror.md)
  The processor failed for an unknown reason.
- [static var unsupportedInput: VTFrameProcessorError.Code](vtframeprocessorerror-swift.struct/unsupportedinput.md)
  One or more frames is in a format which isn’t supported by the processor.
- [static var unsupportedResolution: VTFrameProcessorError.Code](vtframeprocessorerror-swift.struct/unsupportedresolution.md)
  The processor failed due to an unsupported resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorerror-swift.struct/invalidframetiming)*