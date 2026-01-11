# usesPrecomputedFlow

**Framework**: Video Toolbox  
**Kind**: property

Indicates that you provide optical flow.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var usesPrecomputedFlow: Bool { get }
```

## See Also

- [var frameWidth: Int](vtsuperresolutionscalerconfiguration/framewidth.md)
  Width of source frame in pixels.
- [var frameHeight: Int](vtsuperresolutionscalerconfiguration/frameheight.md)
  Height of source frame in pixels.
- [var scaleFactor: Int](vtsuperresolutionscalerconfiguration/scalefactor.md)
  Indicates the scale factor between input and output.
- [var inputType: VTSuperResolutionScalerConfiguration.InputType](vtsuperresolutionscalerconfiguration/inputtype-swift.property.md)
  Indicates the type of input.
- [VTSuperResolutionScalerConfiguration.InputType](vtsuperresolutionscalerconfiguration/inputtype-swift.enum.md)
  Available super-resolution processor input types.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtsuperresolutionscalerconfiguration/sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtsuperresolutionscalerconfiguration/destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.
- [var supportedPixelFormats: [OSType]](vtsuperresolutionscalerconfiguration/supportedpixelformats.md)
- [var qualityPrioritization: VTSuperResolutionScalerConfiguration.QualityPrioritization](vtsuperresolutionscalerconfiguration/qualityprioritization-swift.property.md)
  A parameter to control quality and performance levels.
- [VTSuperResolutionScalerConfiguration.QualityPrioritization](vtsuperresolutionscalerconfiguration/qualityprioritization-swift.enum.md)
  Configuration value you set to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/usesprecomputedflow)*