# VTFrameProcessorError.Code.memoryAllocationFailure

**Framework**: Videotoolbox  
**Kind**: case

The session or processor is unable to allocate the required memory.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.8+

## Declaration

```swift
case memoryAllocationFailure
```

## See Also

- [VTFrameProcessorError.Code.fatalError](vtframeprocessorerror-swift.struct/code/fatalerror.md)
  A fatal error occurred during processing.
- [VTFrameProcessorError.Code.initializationFailed](vtframeprocessorerror-swift.struct/code/initializationfailed.md)
  The session failed to initialize the processing pipeline.
- [VTFrameProcessorError.Code.invalidFrameTiming](vtframeprocessorerror-swift.struct/code/invalidframetiming.md)
  A provided frame object has a presentation time stamp which isn’t supported by the processor.
- [VTFrameProcessorError.Code.invalidParameterError](vtframeprocessorerror-swift.struct/code/invalidparametererror.md)
  A provided parameter isn’t valid.
- [VTFrameProcessorError.Code.processingError](vtframeprocessorerror-swift.struct/code/processingerror.md)
  The processor encountered an issue that prevents it from processing the provided frame.
- [VTFrameProcessorError.Code.revisionNotSupported](vtframeprocessorerror-swift.struct/code/revisionnotsupported.md)
  The specified revision isn’t supported by the configured processor.
- [VTFrameProcessorError.Code.sessionAlreadyActive](vtframeprocessorerror-swift.struct/code/sessionalreadyactive.md)
  An attempt is made to start a session that is already started.
- [VTFrameProcessorError.Code.sessionLevelError](vtframeprocessorerror-swift.struct/code/sessionlevelerror.md)
  The processing failed and current session should be stopped.
- [VTFrameProcessorError.Code.sessionNotStarted](vtframeprocessorerror-swift.struct/code/sessionnotstarted.md)
  The session is used to process frames without being started.
- [VTFrameProcessorError.Code.unknownError](vtframeprocessorerror-swift.struct/code/unknownerror.md)
  The processor failed for an unknown reason.
- [VTFrameProcessorError.Code.unsupportedInput](vtframeprocessorerror-swift.struct/code/unsupportedinput.md)
  One or more frames is in a format which isn’t supported by the processor.
- [VTFrameProcessorError.Code.unsupportedResolution](vtframeprocessorerror-swift.struct/code/unsupportedresolution.md)
  The processor failed due to an unsupported resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorerror-swift.struct/code/memoryallocationfailure)*