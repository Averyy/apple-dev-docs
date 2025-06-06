# VTFrameProcessorConfiguration

**Framework**: Videotoolbox  
**Kind**: protocol

A protocol that describes the configuration of a processor to use during a video processing session.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol VTFrameProcessorConfiguration : NSObjectProtocol, Sendable
```

#### Overview

The VTFrameProcessorConfiguration protocol conformance starts a frame processing session. These properties can be queried on an implementation conforming to this protocol without starting a session.

## Topics

### Determining processor availability
- [static var processorSupported: Bool](vtframeprocessorconfiguration/processorsupported.md)
  A Boolean value that indicates whether the current configuration supports the processor.
### Inspecting the required configuration
- [var frameSupportedPixelFormats: [NSNumber]](vtframeprocessorconfiguration/framesupportedpixelformats.md)
  A list of supported pixel formats for the current configuration.
- [var sourcePixelBufferAttributes: [AnyHashable : Any]](vtframeprocessorconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes that define what the source and reference frames passed to the processor must conform to.
- [var destinationPixelBufferAttributes: [AnyHashable : Any]](vtframeprocessorconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes that define which output frames passed to the processor must conform to.
- [var nextFrameCount: Int](vtframeprocessorconfiguration/nextframecount.md)
  The number of next frames that the processor requires for processing.
- [var previousFrameCount: Int](vtframeprocessorconfiguration/previousframecount.md)
  The number of previous frames that the processor requires for processing.
- [static var maximumDimensions: CMVideoDimensions](vtframeprocessorconfiguration/maximumdimensions.md)
  The maximum dimensions of a source frame for the processor.
- [static var minimumDimensions: CMVideoDimensions](vtframeprocessorconfiguration/minimumdimensions.md)
  The minimum dimensions of a source frame for the processor.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [VTFrameRateConversionConfiguration](vtframerateconversionconfiguration.md)
- [VTMotionBlurConfiguration](vtmotionblurconfiguration.md)
- [VTOpticalFlowConfiguration](vtopticalflowconfiguration.md)

## See Also

- [class VTFrameProcessor](vtframeprocessor.md)
  A class that creates a new frame processor for the configured video effect.
- [class VTFrameProcessorFrame](vtframeprocessorframe.md)
  An object that wraps video frames to send to the processor, as source, reference, or output frames.
- [protocol VTFrameProcessorParameters](vtframeprocessorparameters.md)
  The base protocol for input and output processing parameters for a frame processor implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorconfiguration)*