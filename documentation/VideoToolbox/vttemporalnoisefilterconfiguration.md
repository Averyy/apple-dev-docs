# VTTemporalNoiseFilterConfiguration

**Framework**: Video Toolbox  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
class VTTemporalNoiseFilterConfiguration
```

#### Overview

The class properties of VTTemporalNoiseFilterConfiguration help to identify the capabilities of Temporal Noise Filter Processor on the current platform, prior to initiating a session. The availability of Temporal Noise Filter processor in the current platform can be confirmed by checking the VTTemporalNoiseFilterConfiguration.isSupported class property. Verify the processor’s capability to process source frames by ensuring that the dimensions are no less than VTTemporalNoiseFilterConfiguration.minimumDimensions and no greater than VTTemporalNoiseFilterConfiguration.maximumDimensions. Use the instance properties such as frameSupportedPixelFormats, sourcePixelBufferAttributes, and destinationPixelBufferAttributes to ensure that the input and output pixel buffer formats and attributes of the processor align with the client’s specific requirements. The properties previousFrameCount and nextFrameCount represent the maximum number of preceding and subsequent reference frames, used in the processing of a source frame, to achieve optimum noise reduction quality.

## Topics

### Initializers
- [init(frameWidth: Int, frameHeight: Int)](vttemporalnoisefilterconfiguration/init(framewidth:frameheight:).md)
### Instance Properties
- [var destinationPixelBufferAttributes: [String : any Sendable]](vttemporalnoisefilterconfiguration/destinationpixelbufferattributes.md)
- [var frameHeight: Int](vttemporalnoisefilterconfiguration/frameheight.md)
- [var frameWidth: Int](vttemporalnoisefilterconfiguration/framewidth.md)
- [var sourcePixelBufferAttributes: [String : any Sendable]](vttemporalnoisefilterconfiguration/sourcepixelbufferattributes.md)
- [var supportedPixelFormats: [OSType]](vttemporalnoisefilterconfiguration/supportedpixelformats.md)
### Type Properties
- [class var isSupported: Bool](vttemporalnoisefilterconfiguration/issupported.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vttemporalnoisefilterconfiguration)*