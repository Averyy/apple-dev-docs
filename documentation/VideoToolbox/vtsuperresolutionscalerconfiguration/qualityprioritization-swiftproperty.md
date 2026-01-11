# qualityPrioritization

**Framework**: Video Toolbox  
**Kind**: property

A parameter to control quality and performance levels.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var qualityPrioritization: VTSuperResolutionScalerConfiguration.QualityPrioritization { get }
```

#### Discussion

For more information about supported levels, see [`VTSuperResolutionScalerConfiguration.QualityPrioritization`](vtsuperresolutionscalerconfiguration/qualityprioritization-swift.enum.md).

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
- [var usesPrecomputedFlow: Bool](vtsuperresolutionscalerconfiguration/usesprecomputedflow.md)
  Indicates that you provide optical flow.
- [var usesPrecomputedFlow: Bool](vtsuperresolutionscalerconfiguration/usesprecomputedflow.md)
  Indicates that you provide optical flow.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtsuperresolutionscalerconfiguration/sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtsuperresolutionscalerconfiguration/destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.
- [var supportedPixelFormats: [OSType]](vtsuperresolutionscalerconfiguration/supportedpixelformats.md)
- [VTSuperResolutionScalerConfiguration.QualityPrioritization](vtsuperresolutionscalerconfiguration/qualityprioritization-swift.enum.md)
  Configuration value you set to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/qualityprioritization-swift.property)*