# VTLowLatencySuperResolutionScalerConfiguration

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
class VTLowLatencySuperResolutionScalerConfiguration
```

#### Overview

VTLowLatencySuperResolutionScalerConfiguration is used to configure a VTFrameProcessor.  This interface can also queried for important operating details, like the pixel buffer attributes required for frames submitted to the processor.

## Topics

### Initializers
- [init(frameWidth: Int, frameHeight: Int, scaleFactor: Float)](vtlowlatencysuperresolutionscalerconfiguration/init(framewidth:frameheight:scalefactor:).md)
### Instance Properties
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtlowlatencysuperresolutionscalerconfiguration/destinationpixelbufferattributes.md)
- [var frameHeight: Int](vtlowlatencysuperresolutionscalerconfiguration/frameheight.md)
- [var frameWidth: Int](vtlowlatencysuperresolutionscalerconfiguration/framewidth.md)
- [var scaleFactor: Float](vtlowlatencysuperresolutionscalerconfiguration/scalefactor.md)
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtlowlatencysuperresolutionscalerconfiguration/sourcepixelbufferattributes.md)
- [var supportedPixelFormats: [OSType]](vtlowlatencysuperresolutionscalerconfiguration/supportedpixelformats.md)
### Type Properties
- [class var isSupported: Bool](vtlowlatencysuperresolutionscalerconfiguration/issupported.md)
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