# VTFrameRateConversionConfiguration.QualityPrioritization

**Framework**: Videotoolbox  
**Kind**: enum

Values that specify whether to prioritize quality or performance.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum QualityPrioritization
```

## Topics

### Priorities
- [VTFrameRateConversionConfiguration.QualityPrioritization.normal](vtframerateconversionconfiguration/qualityprioritization-swift.enum/normal.md)
  A normal quality prioritization level.
- [VTFrameRateConversionConfiguration.QualityPrioritization.quality](vtframerateconversionconfiguration/qualityprioritization-swift.enum/quality.md)
  A quality prioritization level.
### Initializers
- [init?(rawValue: Int)](vtframerateconversionconfiguration/qualityprioritization-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var frameWidth: Int](vtframerateconversionconfiguration/framewidth.md)
  The width of a source frame in pixels.
- [var frameHeight: Int](vtframerateconversionconfiguration/frameheight.md)
  The height of a source frame in pixels.
- [var usePrecomputedFlow: Bool](vtframerateconversionconfiguration/useprecomputedflow.md)
  A Boolean value to indicates whether the optical flow will be provided by the user.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtframerateconversionconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtframerateconversionconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var frameSupportedPixelFormats: [NSNumber]](vtframerateconversionconfiguration/framesupportedpixelformats.md)
  A list of source frame supported pixel formats for the current configuration.
- [var qualityPrioritization: VTFrameRateConversionConfiguration.QualityPrioritization](vtframerateconversionconfiguration/qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionconfiguration/qualityprioritization-swift.enum)*