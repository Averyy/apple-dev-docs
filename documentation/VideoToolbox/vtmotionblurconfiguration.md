# VTMotionBlurConfiguration

**Framework**: Video Toolbox  
**Kind**: class

A configuration object to enable motion blur on a frame processing session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+

## Declaration

```swift
class VTMotionBlurConfiguration
```

## Topics

### Creating a motion blur configuration
- [init?(frameWidth: Int, frameHeight: Int, usePrecomputedFlow: Bool, qualityPrioritization: VTMotionBlurConfiguration.QualityPrioritization, revision: VTMotionBlurConfiguration.Revision)](vtmotionblurconfiguration/init(framewidth:frameheight:useprecomputedflow:qualityprioritization:revision:).md)
  Creates a new motion blur configuration with specified flow width and height.
### Determining processor availability
- [class var processorSupported: Bool](vtmotionblurconfiguration/processorsupported.md)
  A Boolean value that indicates whether the processor is supported.
### Inspecting the configuration
- [var frameWidth: Int](vtmotionblurconfiguration/framewidth.md)
  The width of a source frame in pixels.
- [var frameHeight: Int](vtmotionblurconfiguration/frameheight.md)
  The height of a source frame in pixels.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtmotionblurconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtmotionblurconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var qualityPrioritization: VTMotionBlurConfiguration.QualityPrioritization](vtmotionblurconfiguration/qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.
- [VTMotionBlurConfiguration.QualityPrioritization](vtmotionblurconfiguration/qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.
- [var usePrecomputedFlow: Bool](vtmotionblurconfiguration/useprecomputedflow.md)
  A Boolean value to indicates whether the the optical flow will be provided by the user.
### Inspecting revision information
- [var revision: VTMotionBlurConfiguration.Revision](vtmotionblurconfiguration/revision-swift.property.md)
  The specific algorithm or configuration revision that is to be used to perform the request.
- [class var defaultRevision: VTMotionBlurConfiguration.Revision](vtmotionblurconfiguration/defaultrevision.md)
  The default revision of a particular algorithm or configuration.
- [class var supportedRevisions: IndexSet](vtmotionblurconfiguration/supportedrevisions.md)
  The collection of currently-supported algorithms or configuration revisions for the class of configurations.
- [VTMotionBlurConfiguration.Revision](vtmotionblurconfiguration/revision-swift.enum.md)
  The specific algorithm or configuration revision that is to be used to perform the request.
### Instance Properties
- [var frameSupportedPixelFormats: [NSNumber]](vtmotionblurconfiguration/framesupportedpixelformats-1n4uq.md)
- [var supportedPixelFormats: [OSType]](vtmotionblurconfiguration/supportedpixelformats.md)
### Type Properties
- [class var isSupported: Bool](vtmotionblurconfiguration/issupported.md)

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

- [class VTMotionBlurParameters](vtmotionblurparameters.md)
  This object contains both input and output parameters necessary to run the motion blur processor on a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurconfiguration)*