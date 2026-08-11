# VTLowLatencyFrameInterpolationConfiguration

**Framework**: Video Toolbox  
**Kind**: class

Configuration that you use to program Video Toolbox frame processor for low-latency frame interpolation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class VTLowLatencyFrameInterpolationConfiguration
```

#### Overview

This configuration can do either purely temporal interpolation (frame-rate conversion) or temporal and spatial interpolation (scaling and frame-rate conversion). This processor requires a source frame and a previous frame. It does temporal scaling, which interpolates frames between the previous frame and the source frame. When performing both temporal and spatial interpolation, the processor can only perform 2x upscaling, and a single frame of temporal interpolation. When performing spatial scaling, the processor produces upscaled intermediate frames and an upscaled `sourceFrame`, but it does not upscale the previous reference frame you provided.

> ❗ **Important**: When calling [`startSession(configuration:)`](vtframeprocessor/startsession(configuration:).md) to create a `VTLowLatencyFrameInterpolation` session, ML model loading may take longer than a frame time. Avoid blocking the UI thread or stalling frame rendering pipelines during this call.

## Topics

### Creating a frame interpolation configuration
- [init?(frameWidth: Int, frameHeight: Int, numberOfInterpolatedFrames: Int)](vtlowlatencyframeinterpolationconfiguration/init(framewidth:frameheight:numberofinterpolatedframes:).md)
  Creates a new low-latency frame interpolation configuration for frame-rate conversion.
- [init?(frameWidth: Int, frameHeight: Int, spatialScaleFactor: Int)](vtlowlatencyframeinterpolationconfiguration/init(framewidth:frameheight:spatialscalefactor:).md)
  Creates a new low-latency frame interpolation configuration for spatial scaling and temporal scaling.
### Determining processor availability
- [class var isSupported: Bool](vtlowlatencyframeinterpolationconfiguration/issupported.md)
  Reports whether the system supports this processor.
### Inspecting the configuration
- [var frameWidth: Int](vtlowlatencyframeinterpolationconfiguration/framewidth.md)
  Width of source frames in pixels.
- [var frameHeight: Int](vtlowlatencyframeinterpolationconfiguration/frameheight.md)
  Height of source frames in pixels.
- [var numberOfInterpolatedFrames: Int](vtlowlatencyframeinterpolationconfiguration/numberofinterpolatedframes.md)
  Number of uniformly spaced frames for which you configured the processor.
- [var spatialScaleFactor: Int](vtlowlatencyframeinterpolationconfiguration/spatialscalefactor.md)
  Configured spatial scale factor as an integer.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtlowlatencyframeinterpolationconfiguration/sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtlowlatencyframeinterpolationconfiguration/destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.
- [var supportedPixelFormats: [OSType]](vtlowlatencyframeinterpolationconfiguration/supportedpixelformats.md)
### Type Methods
- [class func maximumDimension(forSpatialScaleFactor: Int) -> Int?](vtlowlatencyframeinterpolationconfiguration/maximumdimension(forspatialscalefactor:).md)
  The maximum value for either dimension of the source frame, in pixels, for a given spatial scale factor.
- [class func maximumPixelCount(forSpatialScaleFactor: Int) -> Int?](vtlowlatencyframeinterpolationconfiguration/maximumpixelcount(forspatialscalefactor:).md)
  The maximum total number of pixels in the source frame for a given spatial scale factor.

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

- [class VTLowLatencyFrameInterpolationParameters](vtlowlatencyframeinterpolationparameters.md)
  An object that contains both input and output parameters that the low-latency frame interpolation processor needs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationconfiguration)*