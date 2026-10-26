# qualityPrioritization

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) VTSuperResolutionScalerConfigurationQualityPrioritization qualityPrioritization;
```

#### Discussion

For more information about supported levels, see [`VTSuperResolutionScalerConfiguration.QualityPrioritization`](./qualityprioritization-swift.enum.md).

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
- [var usesPrecomputedFlow: Bool](./usesprecomputedflow.md)
  Indicates that you provide optical flow.
- [var usesPrecomputedFlow: Bool](./usesprecomputedflow.md)
  Indicates that you provide optical flow.
- [var sourcePixelBufferAttributes: [String : any Sendable]](./sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.
- [var supportedPixelFormats: [OSType]](./supportedpixelformats.md)
- [VTSuperResolutionScalerConfiguration.QualityPrioritization](./qualityprioritization-swift.enum.md)
  Configuration value you set to prioritize quality or performance.
- [frameSupportedPixelFormats](./framesupportedpixelformats.md)
  Available supported pixel formats for source frames for current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/qualityprioritization-swift.property)*