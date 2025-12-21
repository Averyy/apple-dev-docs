# VTTemporalNoiseFilterConfiguration

**Framework**: Video Toolbox  
**Kind**: class

A configuration object to initiate a frame processor and use temporal noise-filter processor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
class VTTemporalNoiseFilterConfiguration
```

#### Overview

The class properties of `VTTemporalNoiseFilterConfiguration` help to identify the capabilities of temporal noise filter processor on the current platform, prior to initiating a session. You can confirm the availability of temporal noise-filter processor in the current platform by checking the [`isSupported`](vttemporalnoisefilterconfiguration/issupported.md) class property. Verify the processor’s capability to process source frames by ensuring that the dimensions are no less than [`minimumDimensions`](vttemporalnoisefilterconfiguration/minimumdimensions.md) and no greater than [`maximumDimensions`](vttemporalnoisefilterconfiguration/maximumdimensions.md). Use the instance properties such as [`frameSupportedPixelFormats`](vttemporalnoisefilterconfiguration/framesupportedpixelformats.md), [`sourcePixelBufferAttributes`](vttemporalnoisefilterconfiguration/sourcepixelbufferattributes.md), and [`destinationPixelBufferAttributes`](vttemporalnoisefilterconfiguration/destinationpixelbufferattributes.md) to ensure that the input and output pixel buffer formats and attributes of the processor align with the client’s specific requirements. The properties [`previousFrameCount`](vttemporalnoisefilterconfiguration/previousframecount.md) and [`nextFrameCount`](vttemporalnoisefilterconfiguration/nextframecount.md) represent the maximum number of preceding and subsequent reference frames, used in the processing of a source frame, to achieve optimum noise-reduction quality.

## Topics

### Initializers
- [init?(frameWidth: Int, frameHeight: Int, sourcePixelFormat: OSType)](vttemporalnoisefilterconfiguration/init(framewidth:frameheight:sourcepixelformat:).md)
  Creates a new temporal noise-processor configuration.
### Instance Properties
- [var destinationPixelBufferAttributes: [String : any Sendable]](vttemporalnoisefilterconfiguration/destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.
- [var frameHeight: Int](vttemporalnoisefilterconfiguration/frameheight.md)
  Height of source frame in pixels.
- [var frameWidth: Int](vttemporalnoisefilterconfiguration/framewidth.md)
  Width of source frame in pixels.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vttemporalnoisefilterconfiguration/sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var supportedPixelFormats: [OSType]](vttemporalnoisefilterconfiguration/supportedpixelformats.md)
### Type Properties
- [class var isSupported: Bool](vttemporalnoisefilterconfiguration/issupported.md)
  Reports whether the system supports this processor.
- [class var supportedSourcePixelFormats: [OSType]](vttemporalnoisefilterconfiguration/supportedsourcepixelformats-4ipcg.md)

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