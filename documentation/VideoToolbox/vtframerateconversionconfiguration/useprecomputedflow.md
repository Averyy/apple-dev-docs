# usePrecomputedFlow

**Framework**: Video Toolbox  
**Kind**: property

A Boolean value to indicates whether the optical flow will be provided by the user.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+

## Declaration

```swift
var usePrecomputedFlow: Bool { get }
```

#### Discussion

If `false` this configuration computes the optical flow on the fly.

## See Also

- [var frameWidth: Int](vtframerateconversionconfiguration/framewidth.md)
  The width of a source frame in pixels.
- [var frameHeight: Int](vtframerateconversionconfiguration/frameheight.md)
  The height of a source frame in pixels.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtframerateconversionconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtframerateconversionconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var qualityPrioritization: VTFrameRateConversionConfiguration.QualityPrioritization](vtframerateconversionconfiguration/qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.
- [VTFrameRateConversionConfiguration.QualityPrioritization](vtframerateconversionconfiguration/qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionconfiguration/useprecomputedflow)*