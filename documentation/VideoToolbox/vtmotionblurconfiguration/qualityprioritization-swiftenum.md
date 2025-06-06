# VTMotionBlurConfiguration.QualityPrioritization

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
- [VTMotionBlurConfiguration.QualityPrioritization.normal](vtmotionblurconfiguration/qualityprioritization-swift.enum/normal.md)
  A normal quality prioritization level.
- [VTMotionBlurConfiguration.QualityPrioritization.quality](vtmotionblurconfiguration/qualityprioritization-swift.enum/quality.md)
  A quality prioritization level.
### Initializers
- [init?(rawValue: Int)](vtmotionblurconfiguration/qualityprioritization-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var frameWidth: Int](vtmotionblurconfiguration/framewidth.md)
  The width of a source frame in pixels.
- [var frameHeight: Int](vtmotionblurconfiguration/frameheight.md)
  The height of a source frame in pixels.
- [var frameSupportedPixelFormats: [NSNumber]](vtmotionblurconfiguration/framesupportedpixelformats.md)
  A list of source frame supported pixel formats for the current configuration.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtmotionblurconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtmotionblurconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var qualityPrioritization: VTMotionBlurConfiguration.QualityPrioritization](vtmotionblurconfiguration/qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.
- [var usePrecomputedFlow: Bool](vtmotionblurconfiguration/useprecomputedflow.md)
  A Boolean value to indicates whether the the optical flow will be provided by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurconfiguration/qualityprioritization-swift.enum)*