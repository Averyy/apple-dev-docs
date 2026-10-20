# VTLowLatencySuperResolutionScalerConfiguration

**Framework**: Video Toolbox  
**Kind**: class  
**Role**: Class

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

```objc
@interface VTLowLatencySuperResolutionScalerConfiguration : NSObject
```

#### Overview

Use this object to configure a [`VTFrameProcessor`](./vtframeprocessor.md). Query this interface also for important operating details, like the pixel buffer attributes required for frames you submit to the processor.

> ❗ **Important**: When calling [`startSession(configuration:)`](./vtframeprocessor/startsession%28configuration%29.md) to create a `VTLowLatencySuperResolutionScaler` session, ML model loading may take longer than a frame time. Avoid blocking the UI thread or stalling frame rendering pipelines during this call.

## Topics

### Creating a super resolution scaler configuration
- [init(frameWidth: Int, frameHeight: Int, scaleFactor: Float)](./vtlowlatencysuperresolutionscalerconfiguration/init%28framewidth,frameheight,scalefactor%29.md)
  Creates a new low-latency super-resolution scaler configuration with specified frame width and height.
### Determining processor availability
- [class var isSupported: Bool](./vtlowlatencysuperresolutionscalerconfiguration/issupported.md)
  Reports whether the system supports this processor on the current configuration.
- [class func supportedScaleFactors(frameWidth: Int, frameHeight: Int) -> [Float]](./vtlowlatencysuperresolutionscalerconfiguration/supportedscalefactors%28framewidth,frameheight%29.md)
### Inspecting the configuration
- [var frameWidth: Int](./vtlowlatencysuperresolutionscalerconfiguration/framewidth.md)
  Width of source frame in pixels.
- [var frameHeight: Int](./vtlowlatencysuperresolutionscalerconfiguration/frameheight.md)
  Height of source frame in pixels.
- [var scaleFactor: Float](./vtlowlatencysuperresolutionscalerconfiguration/scalefactor.md)
  Scale factor with which you initialized the configuration.
- [var sourcePixelBufferAttributes: [String : any Sendable]](./vtlowlatencysuperresolutionscalerconfiguration/sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./vtlowlatencysuperresolutionscalerconfiguration/destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.
- [var supportedPixelFormats: [OSType]](./vtlowlatencysuperresolutionscalerconfiguration/supportedpixelformats.md)
### Type Properties
- [class var supportedScaleFactors: [Float]](./vtlowlatencysuperresolutionscalerconfiguration/supportedscalefactors-27vjh.md)
### Type Methods
- [class func maximumDimension(forSpatialScaleFactor: Float) -> Int?](./vtlowlatencysuperresolutionscalerconfiguration/maximumdimension%28forspatialscalefactor%29.md)
  The maximum value for either dimension of the source frame, in pixels, for a given spatial scale factor.
- [class func maximumPixelCount(forSpatialScaleFactor: Float) -> Int?](./vtlowlatencysuperresolutionscalerconfiguration/maximumpixelcount%28forspatialscalefactor%29.md)
  The maximum total number of pixels in the source frame for a given spatial scale factor.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [VTFrameProcessorConfiguration](./vtframeprocessorconfiguration.md)

## See Also

### Low-latency super resolution
- [class VTLowLatencySuperResolutionScalerParameters](./vtlowlatencysuperresolutionscalerparameters.md)
  An object that contains both input and output parameters that the low-latency super-resolution scaler frame processor needs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencysuperresolutionscalerconfiguration)*