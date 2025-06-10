# VTOpticalFlowConfiguration

**Framework**: Video Toolbox  
**Kind**: class

A configuration object that enables optical flow on a frame processing session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+

## Declaration

```swift
class VTOpticalFlowConfiguration
```

## Topics

### Creating an optical flow configuration
- [init?(frameWidth: Int, frameHeight: Int, qualityPrioritization: VTOpticalFlowConfiguration.QualityPrioritization, revision: VTOpticalFlowConfiguration.Revision)](vtopticalflowconfiguration/init(framewidth:frameheight:qualityprioritization:revision:).md)
### Determining processor availability
- [class var processorSupported: Bool](vtopticalflowconfiguration/processorsupported.md)
  A boolean value that indicates whether the processor supported on the current configuration.
### Inspecting the configuration
- [var frameWidth: Int](vtopticalflowconfiguration/framewidth.md)
  The width of a source frame in pixels.
- [var frameHeight: Int](vtopticalflowconfiguration/frameheight.md)
  The height of source frame in pixels.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtopticalflowconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtopticalflowconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var qualityPrioritization: VTOpticalFlowConfiguration.QualityPrioritization](vtopticalflowconfiguration/qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.
- [VTOpticalFlowConfiguration.QualityPrioritization](vtopticalflowconfiguration/qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.
### Inspecting revision information
- [var revision: VTOpticalFlowConfiguration.Revision](vtopticalflowconfiguration/revision-swift.property.md)
  The specific algorithm or configuration revision that is to be used to perform the request.
- [class var defaultRevision: VTOpticalFlowConfiguration.Revision](vtopticalflowconfiguration/defaultrevision.md)
  The default revision of a particular algorithm or configuration.
- [class var supportedRevisions: IndexSet](vtopticalflowconfiguration/supportedrevisions.md)
  A boolean value that indicates whether the processor supported on the current configuration.
- [VTOpticalFlowConfiguration.Revision](vtopticalflowconfiguration/revision-swift.enum.md)
  The specific algorithm or configuration revision that is to be used to perform the request.
### Instance Properties
- [var frameSupportedPixelFormats: [NSNumber]](vtopticalflowconfiguration/framesupportedpixelformats-gm6u.md)
- [var supportedPixelFormats: [OSType]](vtopticalflowconfiguration/supportedpixelformats.md)
### Type Properties
- [class var isSupported: Bool](vtopticalflowconfiguration/issupported.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VTFrameProcessorConfiguration](vtframeprocessorconfiguration.md)

## See Also

- [class VTFrameProcessorOpticalFlow](vtframeprocessoropticalflow.md)
  A class to wrap bidirectional optical flow to send to the processor.
- [class VTOpticalFlowParameters](vtopticalflowparameters.md)
  An object that describes frame-level optical flow parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowconfiguration)*