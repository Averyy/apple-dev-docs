# VTFrameProcessorConfiguration

**Framework**: Video Toolbox  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol VTFrameProcessorConfiguration <NSObject>
```

## Overview

The VTFrameProcessorConfiguration protocol conformance starts a frame processing session. These properties can be queried on an implementation conforming to this protocol without starting a session.

## Topics

### Determining processor availability
- [static var isSupported: Bool](./vtframeprocessorconfiguration/issupported.md)
  A Boolean value that indicates whether the current configuration supports the processor.
### Inspecting dimension constraints
- [static var maximumDimensions: CMVideoDimensions?](./vtframeprocessorconfiguration/maximumdimensions-4vmra.md)
  The maximum dimensions of a source frame for the processor.
- [static var minimumDimensions: CMVideoDimensions?](./vtframeprocessorconfiguration/minimumdimensions-42b0h.md)
  The minimum dimensions of a source frame for the processor.
### Inspecting pixel buffer attributes
- [var sourcePixelBufferAttributes: [String : any Sendable]](./vtframeprocessorconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes that define what the source and reference frames passed to the processor must conform to.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./vtframeprocessorconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes that define which output frames passed to the processor must conform to.
- [frameSupportedPixelFormats](./vtframeprocessorconfiguration/framesupportedpixelformats.md)
  A list of supported pixel formats for the current configuration.
### Inspecting frame requirements
- [var nextFrameCount: Int?](./vtframeprocessorconfiguration/nextframecount-18e47.md)
  The number of next frames that the processor requires for processing.
- [var previousFrameCount: Int?](./vtframeprocessorconfiguration/previousframecount-1crhc.md)
  The number of previous frames that the processor requires for processing.
### Instance Properties
- [nextFrameCount](./vtframeprocessorconfiguration/nextframecount-533br.md)
  Returns the number of “next” frames that this processor requires for processing.
- [previousFrameCount](./vtframeprocessorconfiguration/previousframecount-20ke2.md)
  Returns the number of “previous” frames that this processor requires for processing.
### Type Properties
- [maximumDimensions](./vtframeprocessorconfiguration/maximumdimensions-1x3l0.md)
  Returns the maximum dimensions for a `sourceFrame` for the processor.
- [minimumDimensions](./vtframeprocessorconfiguration/minimumdimensions-9n9r0.md)
  Returns the minimum dimensions for a `sourceFrame` for the processor.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [VTFrameRateConversionConfiguration](./vtframerateconversionconfiguration.md)
- [VTLowLatencyFrameInterpolationConfiguration](./vtlowlatencyframeinterpolationconfiguration.md)
- [VTLowLatencySuperResolutionScalerConfiguration](./vtlowlatencysuperresolutionscalerconfiguration.md)
- [VTMotionBlurConfiguration](./vtmotionblurconfiguration.md)
- [VTOpticalFlowConfiguration](./vtopticalflowconfiguration.md)
- [VTSuperResolutionScalerConfiguration](./vtsuperresolutionscalerconfiguration.md)
- [VTTemporalNoiseFilterConfiguration](./vttemporalnoisefilterconfiguration.md)

## See Also

### Frame processor
- [Enhancing your app with machine learning-based video effects](./enhancing-your-app-with-machine-learning-based-video-effects.md)
  Add powerful effects to your videos using the VideoToolbox VTFrameProcessor API.
- [class VTFrameProcessor](./vtframeprocessor.md)
  A class that creates a new frame processor for the configured video effect.
- [class VTFrameProcessorFrame](./vtframeprocessorframe.md)
  An object that wraps video frames to send to the processor, as source, reference, or output frames.
- [protocol VTFrameProcessorParameters](./vtframeprocessorparameters.md)
  The base protocol for input and output processing parameters for a frame processor implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorconfiguration)*