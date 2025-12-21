# destinationPixelBufferAttributes

**Framework**: Video Toolbox  
**Kind**: property

A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var destinationPixelBufferAttributes: [String : any Sendable] { get }
```

## See Also

- [var frameWidth: Int](vtmotionblurconfiguration/framewidth.md)
  The width of a source frame in pixels.
- [var frameHeight: Int](vtmotionblurconfiguration/frameheight.md)
  The height of a source frame in pixels.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtmotionblurconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var qualityPrioritization: VTMotionBlurConfiguration.QualityPrioritization](vtmotionblurconfiguration/qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.
- [VTMotionBlurConfiguration.QualityPrioritization](vtmotionblurconfiguration/qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.
- [var usePrecomputedFlow: Bool](vtmotionblurconfiguration/useprecomputedflow.md)
  A Boolean value to indicates whether the the optical flow will be provided by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurconfiguration/destinationpixelbufferattributes)*