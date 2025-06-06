# usePrecomputedFlow

**Framework**: Videotoolbox  
**Kind**: property

A Boolean value to indicates whether the the optical flow will be provided by the user.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var usePrecomputedFlow: Bool { get }
```

#### Discussion

If `false` this configuration computes the optical flow on the fly.

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
- [VTMotionBlurConfiguration.QualityPrioritization](vtmotionblurconfiguration/qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurconfiguration/useprecomputedflow)*