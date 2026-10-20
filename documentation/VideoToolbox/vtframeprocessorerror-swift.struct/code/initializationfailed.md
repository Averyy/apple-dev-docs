# VTFrameProcessorError.Code.initializationFailed

**Framework**: Video Toolbox  
**Kind**: case  
**Role**: Case

The session failed to initialize the processing pipeline.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
case initializationFailed
```

```c
VTFrameProcessorInitializationFailed
```

## See Also

### Enumeration Cases
- [VTFrameProcessorError.Code.fatalError](./fatalerror.md)
  A fatal error occurred during processing.
- [VTFrameProcessorError.Code.invalidFrameTiming](./invalidframetiming.md)
  A provided frame object has a presentation time stamp which isn’t supported by the processor.
- [VTFrameProcessorError.Code.invalidParameterError](./invalidparametererror.md)
  A provided parameter isn’t valid.
- [VTFrameProcessorError.Code.memoryAllocationFailure](./memoryallocationfailure.md)
  The session or processor is unable to allocate the required memory.
- [VTFrameProcessorError.Code.processingError](./processingerror.md)
  The processor encountered an issue that prevents it from processing the provided frame.
- [VTFrameProcessorError.Code.revisionNotSupported](./revisionnotsupported.md)
  The specified revision isn’t supported by the configured processor.
- [VTFrameProcessorError.Code.sessionAlreadyActive](./sessionalreadyactive.md)
  An attempt is made to start a session that is already started.
- [VTFrameProcessorError.Code.sessionLevelError](./sessionlevelerror.md)
  The processing failed and current session should be stopped.
- [VTFrameProcessorError.Code.sessionNotStarted](./sessionnotstarted.md)
  The session is used to process frames without being started.
- [VTFrameProcessorError.Code.unknownError](./unknownerror.md)
  The processor failed for an unknown reason.
- [VTFrameProcessorError.Code.unsupportedInput](./unsupportedinput.md)
  One or more frames is in a format which isn’t supported by the processor.
- [VTFrameProcessorError.Code.unsupportedResolution](./unsupportedresolution.md)
  The processor failed due to an unsupported resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorerror-swift.struct/code/initializationfailed)*