# VTLowLatencySuperResolutionScalerConfiguration

**Framework**: Video Toolbox  
**Kind**: class

An object you use to configure frame processor for low-latency super-resolution scaler processing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class VTLowLatencySuperResolutionScalerConfiguration
```

#### Overview

Use this object to configure a [`VTFrameProcessor`](vtframeprocessor.md). Query this interface also for important operating details, like the pixel buffer attributes required for frames you submit to the processor.

> ❗ **Important**: When calling [`startSession(configuration:)`](vtframeprocessor/startsession(configuration:).md) to create a `VTLowLatencySuperResolutionScaler` session, ML model loading may take longer than a frame time. Avoid blocking the UI thread or stalling frame rendering pipelines during this call.

## Topics

### Initializers
- [init(frameWidth: Int, frameHeight: Int, scaleFactor: Float)](vtlowlatencysuperresolutionscalerconfiguration/init(framewidth:frameheight:scalefactor:).md)
  Creates a new low-latency super-resolution scaler configuration with specified frame width and height.
### Instance Properties
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtlowlatencysuperresolutionscalerconfiguration/destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.
- [var frameHeight: Int](vtlowlatencysuperresolutionscalerconfiguration/frameheight.md)
  Height of source frame in pixels.
- [var frameWidth: Int](vtlowlatencysuperresolutionscalerconfiguration/framewidth.md)
  Width of source frame in pixels.
- [var scaleFactor: Float](vtlowlatencysuperresolutionscalerconfiguration/scalefactor.md)
  Scale factor with which you initialized the configuration.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtlowlatencysuperresolutionscalerconfiguration/sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var supportedPixelFormats: [OSType]](vtlowlatencysuperresolutionscalerconfiguration/supportedpixelformats.md)
### Type Properties
- [class var isSupported: Bool](vtlowlatencysuperresolutionscalerconfiguration/issupported.md)
  Reports whether the system supports this processor on the current configuration.
### Type Methods
- [class func supportedScaleFactors(frameWidth: Int, frameHeight: Int) -> [Float]](vtlowlatencysuperresolutionscalerconfiguration/supportedscalefactors(framewidth:frameheight:).md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencysuperresolutionscalerconfiguration)*