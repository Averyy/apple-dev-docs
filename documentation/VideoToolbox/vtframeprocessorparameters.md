# VTFrameProcessorParameters

**Framework**: Videotoolbox  
**Kind**: protocol

The base protocol for input and output processing parameters for a frame processor implementation.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol VTFrameProcessorParameters : NSObjectProtocol
```

#### Overview

An instance of a class corresponding to this protocol is passed to [`processWithParameters:error:`](vtframeprocessor/processwithparameters:error:.md) calls and for asynchronous versions of those calls, the same instance is returned in the completion.

## Topics

### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](vtframeprocessorparameters/sourceframe.md)
  A processor frame that contains the current source frame to use for all processing features.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [VTFrameRateConversionParameters](vtframerateconversionparameters.md)
- [VTMotionBlurParameters](vtmotionblurparameters.md)
- [VTOpticalFlowParameters](vtopticalflowparameters.md)

## See Also

- [class VTFrameProcessor](vtframeprocessor.md)
  A class that creates a new frame processor for the configured video effect.
- [class VTFrameProcessorFrame](vtframeprocessorframe.md)
  An object that wraps video frames to send to the processor, as source, reference, or output frames.
- [protocol VTFrameProcessorConfiguration](vtframeprocessorconfiguration.md)
  A protocol that describes the configuration of a processor to use during a video processing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorparameters)*