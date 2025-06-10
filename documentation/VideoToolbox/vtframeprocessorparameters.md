# VTFrameProcessorParameters

**Framework**: Video Toolbox  
**Kind**: protocol

The base protocol for input and output processing parameters for a frame processor implementation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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
### Instance Properties
- [var destinationFrame: VTFrameProcessorFrame?](vtframeprocessorparameters/destinationframe-5suam.md)
  [`VTFrameProcessorFrame`](vtframeprocessorframe.md) that contains the destination frame for processors which output a single processed frame.
- [var destinationFrames: [VTFrameProcessorFrame]?](vtframeprocessorparameters/destinationframes-46ken.md)
  Array of [`VTFrameProcessorFrame`](vtframeprocessorframe.md) that contains the destination frames for processors which may output more than one processed frame.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [VTFrameRateConversionParameters](vtframerateconversionparameters.md)
- [VTLowLatencyFrameInterpolationParameters](vtlowlatencyframeinterpolationparameters.md)
- [VTLowLatencySuperResolutionScalerParameters](vtlowlatencysuperresolutionscalerparameters.md)
- [VTMotionBlurParameters](vtmotionblurparameters.md)
- [VTOpticalFlowParameters](vtopticalflowparameters.md)
- [VTSuperResolutionScalerParameters](vtsuperresolutionscalerparameters.md)
- [VTTemporalNoiseFilterParameters](vttemporalnoisefilterparameters.md)

## See Also

- [Enhancing your app with machine learning-based video effects](enhancing-your-app-with-machine-learning-based-video-effects.md)
  Add powerful effects to your videos using the VideoToolbox VTFrameProcessor API.
- [class VTFrameProcessor](vtframeprocessor.md)
  A class that creates a new frame processor for the configured video effect.
- [class VTFrameProcessorFrame](vtframeprocessorframe.md)
  An object that wraps video frames to send to the processor, as source, reference, or output frames.
- [protocol VTFrameProcessorConfiguration](vtframeprocessorconfiguration.md)
  A protocol that describes the configuration of a processor to use during a video processing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorparameters)*