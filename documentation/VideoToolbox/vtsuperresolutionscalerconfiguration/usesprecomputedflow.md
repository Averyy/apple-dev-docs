# usesPrecomputedFlow

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=usesPrecomputedFlow) BOOL precomputedFlow;
```

## See Also

### Inspecting the configuration
- [var frameWidth: Int](./framewidth.md)
  Width of source frame in pixels.
- [var frameHeight: Int](./frameheight.md)
  Height of source frame in pixels.
- [var scaleFactor: Int](./scalefactor.md)
  Indicates the scale factor between input and output.
- [var inputType: VTSuperResolutionScalerConfiguration.InputType](./inputtype-swift.property.md)
  Indicates the type of input.
- [VTSuperResolutionScalerConfiguration.InputType](./inputtype-swift.enum.md)
  Available super-resolution processor input types.
- [var sourcePixelBufferAttributes: [String : any Sendable]](./sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.
- [var supportedPixelFormats: [OSType]](./supportedpixelformats.md)
- [var qualityPrioritization: VTSuperResolutionScalerConfiguration.QualityPrioritization](./qualityprioritization-swift.property.md)
  A parameter to control quality and performance levels.
- [VTSuperResolutionScalerConfiguration.QualityPrioritization](./qualityprioritization-swift.enum.md)
  Configuration value you set to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/usesprecomputedflow)*