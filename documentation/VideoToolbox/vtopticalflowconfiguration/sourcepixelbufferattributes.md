# sourcePixelBufferAttributes

**Framework**: Video Toolbox  
**Kind**: property

A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var sourcePixelBufferAttributes: [String : any Sendable] { get }
```

## See Also

- [var frameWidth: Int](vtopticalflowconfiguration/framewidth.md)
  The width of a source frame in pixels.
- [var frameHeight: Int](vtopticalflowconfiguration/frameheight.md)
  The height of source frame in pixels.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtopticalflowconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var qualityPrioritization: VTOpticalFlowConfiguration.QualityPrioritization](vtopticalflowconfiguration/qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.
- [VTOpticalFlowConfiguration.QualityPrioritization](vtopticalflowconfiguration/qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowconfiguration/sourcepixelbufferattributes)*