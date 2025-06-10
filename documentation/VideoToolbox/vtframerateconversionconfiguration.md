# VTFrameRateConversionConfiguration

**Framework**: Video Toolbox  
**Kind**: class

An object that enables the frame rate conversion on a frame processing session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+

## Declaration

```swift
class VTFrameRateConversionConfiguration
```

## Topics

### Creating a frame rate conversion configuration
- [init?(frameWidth: Int, frameHeight: Int, usePrecomputedFlow: Bool, qualityPrioritization: VTFrameRateConversionConfiguration.QualityPrioritization, revision: VTFrameRateConversionConfiguration.Revision)](vtframerateconversionconfiguration/init(framewidth:frameheight:useprecomputedflow:qualityprioritization:revision:).md)
  Creates a new frame rate conversion configuration with specified flow width and height.
### Determining processor availability
- [class var processorSupported: Bool](vtframerateconversionconfiguration/processorsupported.md)
  A Boolean value that indicates whether the processor supported on the current configuration.
### Inspecting the configuration
- [var frameWidth: Int](vtframerateconversionconfiguration/framewidth.md)
  The width of a source frame in pixels.
- [var frameHeight: Int](vtframerateconversionconfiguration/frameheight.md)
  The height of a source frame in pixels.
- [var usePrecomputedFlow: Bool](vtframerateconversionconfiguration/useprecomputedflow.md)
  A Boolean value to indicates whether the optical flow will be provided by the user.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtframerateconversionconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtframerateconversionconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var qualityPrioritization: VTFrameRateConversionConfiguration.QualityPrioritization](vtframerateconversionconfiguration/qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.
- [VTFrameRateConversionConfiguration.QualityPrioritization](vtframerateconversionconfiguration/qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.
### Inspecting revision information
- [var revision: VTFrameRateConversionConfiguration.Revision](vtframerateconversionconfiguration/revision-swift.property.md)
  The specific algorithm or configuration revision to use to perform the request.
- [class var defaultRevision: VTFrameRateConversionConfiguration.Revision](vtframerateconversionconfiguration/defaultrevision.md)
  The default revision of a particular algorithm or configuration.
- [class var supportedRevisions: IndexSet](vtframerateconversionconfiguration/supportedrevisions.md)
  The collection of currently-supported algorithms or configuration revisions for the class of configurations.
- [VTFrameRateConversionConfiguration.Revision](vtframerateconversionconfiguration/revision-swift.enum.md)
  The specific algorithm or configuration revision that is to be used to perform the request.
### Instance Properties
- [var frameSupportedPixelFormats: [NSNumber]](vtframerateconversionconfiguration/framesupportedpixelformats-54soi.md)
- [var supportedPixelFormats: [OSType]](vtframerateconversionconfiguration/supportedpixelformats.md)
### Type Properties
- [class var isSupported: Bool](vtframerateconversionconfiguration/issupported.md)

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

- [class VTFrameRateConversionParameters](vtframerateconversionparameters.md)
  An object that contains the required input and output parameters to run a frame rate conversion processor on a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionconfiguration)*