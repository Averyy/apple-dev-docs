# VTLowLatencyFrameInterpolationConfiguration

**Framework**: Video Toolbox  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class VTLowLatencyFrameInterpolationConfiguration
```

#### Overview

This processor requires a source frame and a previous frame.  It does temporal scaling, interpolating frames between the previous frame and the source frame.  When performing both temporal and spatial interpolation, the processor can only perform 2x upscaling, and a single frame of temporal interpolation.  When performing spatial scaling, the processor will produce upscaled intermediate frames as well as an upscaled sourceFrame but will not upscale the previous reference frame provided.

## Topics

### Initializers
- [init?(frameWidth: Int, frameHeight: Int, numberOfInterpolatedFrames: Int)](vtlowlatencyframeinterpolationconfiguration/init(framewidth:frameheight:numberofinterpolatedframes:).md)
- [init?(frameWidth: Int, frameHeight: Int, spatialScaleFactor: Int)](vtlowlatencyframeinterpolationconfiguration/init(framewidth:frameheight:spatialscalefactor:).md)
### Instance Properties
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtlowlatencyframeinterpolationconfiguration/destinationpixelbufferattributes.md)
- [var frameHeight: Int](vtlowlatencyframeinterpolationconfiguration/frameheight.md)
- [var frameWidth: Int](vtlowlatencyframeinterpolationconfiguration/framewidth.md)
- [var numberOfInterpolatedFrames: Int](vtlowlatencyframeinterpolationconfiguration/numberofinterpolatedframes.md)
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtlowlatencyframeinterpolationconfiguration/sourcepixelbufferattributes.md)
- [var spatialScaleFactor: Int](vtlowlatencyframeinterpolationconfiguration/spatialscalefactor.md)
- [var supportedPixelFormats: [OSType]](vtlowlatencyframeinterpolationconfiguration/supportedpixelformats.md)
### Type Properties
- [class var isSupported: Bool](vtlowlatencyframeinterpolationconfiguration/issupported.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationconfiguration)*