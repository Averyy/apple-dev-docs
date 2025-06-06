# qualityPrioritization

**Framework**: Videotoolbox  
**Kind**: property

A value that specifies whether to prioritize quality or performance.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var qualityPrioritization: VTFrameRateConversionConfiguration.QualityPrioritization { get }
```

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
- [VTFrameRateConversionConfiguration.QualityPrioritization](vtframerateconversionconfiguration/qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionconfiguration/qualityprioritization-swift.property)*