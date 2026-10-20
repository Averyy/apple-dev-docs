# VTOpticalFlowConfiguration.QualityPrioritization

**Framework**: Video Toolbox  
**Kind**: enum  
**Role**: Enumeration

Values that specify whether to prioritize quality or performance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
enum QualityPrioritization
```

```c
enum VTOpticalFlowConfigurationQualityPrioritization : NSInteger;
```

#### Overview

See VEFrameRateConversionConfigurationQualityPrioritization for more info.

## Topics

### Enumeration Cases
- [VTOpticalFlowConfiguration.QualityPrioritization.normal](./qualityprioritization-swift.enum/normal.md)
  A normal quality prioritization level.
- [VTOpticalFlowConfiguration.QualityPrioritization.quality](./qualityprioritization-swift.enum/quality.md)
  A quality prioritization level.
### Initializers
- [init?(rawValue: Int)](./qualityprioritization-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting the configuration
- [var frameWidth: Int](./framewidth.md)
  The width of a source frame in pixels.
- [var frameHeight: Int](./frameheight.md)
  The height of source frame in pixels.
- [var sourcePixelBufferAttributes: [String : any Sendable]](./sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var supportedPixelFormats: [OSType]](./supportedpixelformats.md)
- [var qualityPrioritization: VTOpticalFlowConfiguration.QualityPrioritization](./qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowconfiguration/qualityprioritization-swift.enum)*