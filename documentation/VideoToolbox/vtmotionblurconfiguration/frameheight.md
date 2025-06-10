# frameHeight

**Framework**: Video Toolbox  
**Kind**: property

The height of a source frame in pixels.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+

## Declaration

```swift
var frameHeight: Int { get }
```

#### Discussion

The maximum value is 4320 pixels for macOS, and 2160 pixels for iOS.

## See Also

- [var frameWidth: Int](vtmotionblurconfiguration/framewidth.md)
  The width of a source frame in pixels.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtmotionblurconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtmotionblurconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var qualityPrioritization: VTMotionBlurConfiguration.QualityPrioritization](vtmotionblurconfiguration/qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.
- [VTMotionBlurConfiguration.QualityPrioritization](vtmotionblurconfiguration/qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.
- [var usePrecomputedFlow: Bool](vtmotionblurconfiguration/useprecomputedflow.md)
  A Boolean value to indicates whether the the optical flow will be provided by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurconfiguration/frameheight)*