# VTOpticalFlowConfiguration.QualityPrioritization

**Framework**: Videotoolbox  
**Kind**: enum

Values that specify whether to prioritize quality or performance.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum QualityPrioritization
```

#### Overview

See VEFrameRateConversionConfigurationQualityPrioritization for more info.

## Topics

### Enumeration Cases
- [VTOpticalFlowConfiguration.QualityPrioritization.normal](vtopticalflowconfiguration/qualityprioritization-swift.enum/normal.md)
  A normal quality prioritization level.
- [VTOpticalFlowConfiguration.QualityPrioritization.quality](vtopticalflowconfiguration/qualityprioritization-swift.enum/quality.md)
  A quality prioritization level.
### Initializers
- [init?(rawValue: Int)](vtopticalflowconfiguration/qualityprioritization-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var frameWidth: Int](vtopticalflowconfiguration/framewidth.md)
  The width of a source frame in pixels.
- [var frameHeight: Int](vtopticalflowconfiguration/frameheight.md)
  The height of source frame in pixels.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtopticalflowconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtopticalflowconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var frameSupportedPixelFormats: [NSNumber]](vtopticalflowconfiguration/framesupportedpixelformats.md)
  A list of source frame supported pixel formats for the current configuration.
- [var qualityPrioritization: VTOpticalFlowConfiguration.QualityPrioritization](vtopticalflowconfiguration/qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowconfiguration/qualityprioritization-swift.enum)*