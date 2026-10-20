# usePrecomputedFlow

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

A Boolean value to indicates whether the optical flow will be provided by the user.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var usePrecomputedFlow: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL usePrecomputedFlow;
```

#### Discussion

If `false` this configuration computes the optical flow on the fly.

## See Also

### Inspecting the configuration
- [var frameWidth: Int](./framewidth.md)
  The width of a source frame in pixels.
- [var frameHeight: Int](./frameheight.md)
  The height of a source frame in pixels.
- [var sourcePixelBufferAttributes: [String : any Sendable]](./sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var supportedPixelFormats: [OSType]](./supportedpixelformats.md)
- [var qualityPrioritization: VTFrameRateConversionConfiguration.QualityPrioritization](./qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.
- [VTFrameRateConversionConfiguration.QualityPrioritization](./qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionconfiguration/useprecomputedflow)*