# VTFrameProcessorConfiguration

**Framework**: Video Toolbox  
**Kind**: protocol

A protocol that describes the configuration of a processor to use during a video processing session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol VTFrameProcessorConfiguration : NSObjectProtocol, Sendable
```

#### Overview

The VTFrameProcessorConfiguration protocol conformance starts a frame processing session. These properties can be queried on an implementation conforming to this protocol without starting a session.

## Topics

### Inspecting the required configuration
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtframeprocessorconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes that define what the source and reference frames passed to the processor must conform to.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtframeprocessorconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes that define which output frames passed to the processor must conform to.
### Instance Properties
- [var nextFrameCount: Int?](vtframeprocessorconfiguration/nextframecount-18e47.md)
  The number of “next” frames that this processor requires for processing.
- [var previousFrameCount: Int?](vtframeprocessorconfiguration/previousframecount-1crhc.md)
  The number of “previous” frames that this processor requires for processing.
### Type Properties
- [static var isSupported: Bool](vtframeprocessorconfiguration/issupported.md)
  Returns a Boolean indicating whether the system supports this processor on the current configuration.
- [static var maximumDimensions: CMVideoDimensions?](vtframeprocessorconfiguration/maximumdimensions-4vmra.md)
  Maximum dimensions for a `sourceFrame` for the processor
- [static var minimumDimensions: CMVideoDimensions?](vtframeprocessorconfiguration/minimumdimensions-42b0h.md)
  Minimum dimensions for a `sourceFrame` for the processor

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [VTFrameRateConversionConfiguration](vtframerateconversionconfiguration.md)
- [VTLowLatencyFrameInterpolationConfiguration](vtlowlatencyframeinterpolationconfiguration.md)
- [VTLowLatencySuperResolutionScalerConfiguration](vtlowlatencysuperresolutionscalerconfiguration.md)
- [VTMotionBlurConfiguration](vtmotionblurconfiguration.md)
- [VTOpticalFlowConfiguration](vtopticalflowconfiguration.md)
- [VTSuperResolutionScalerConfiguration](vtsuperresolutionscalerconfiguration.md)
- [VTTemporalNoiseFilterConfiguration](vttemporalnoisefilterconfiguration.md)

## See Also

- [Enhancing your app with machine learning-based video effects](enhancing-your-app-with-machine-learning-based-video-effects.md)
  Add powerful effects to your videos using the VideoToolbox VTFrameProcessor API.
- [class VTFrameProcessor](vtframeprocessor.md)
  A class that creates a new frame processor for the configured video effect.
- [class VTFrameProcessorFrame](vtframeprocessorframe.md)
  An object that wraps video frames to send to the processor, as source, reference, or output frames.
- [protocol VTFrameProcessorParameters](vtframeprocessorparameters.md)
  The base protocol for input and output processing parameters for a frame processor implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorconfiguration)*