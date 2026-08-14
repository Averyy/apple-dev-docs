# VTFrameRateConversionConfiguration.QualityPrioritization

**Framework**: Video Toolbox  
**Kind**: enum

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
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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
- [var supportedPixelFormats: [OSType]](vtframerateconversionconfiguration/supportedpixelformats.md)
- [var qualityPrioritization: VTFrameRateConversionConfiguration.QualityPrioritization](vtframerateconversionconfiguration/qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionconfiguration/qualityprioritization-swift.enum)*