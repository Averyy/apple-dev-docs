# VTSuperResolutionScalerConfiguration.QualityPrioritization

**Framework**: Video Toolbox  
**Kind**: enum  
**Role**: Enumeration

Configuration value you set to prioritize quality or performance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum QualityPrioritization
```

```c
enum VTSuperResolutionScalerConfigurationQualityPrioritization : NSInteger;
```

## Topics

### Enumeration Cases
- [VTSuperResolutionScalerConfiguration.QualityPrioritization.normal](./qualityprioritization-swift.enum/normal.md)
### Initializers
- [init?(rawValue: Int)](./qualityprioritization-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var qualityPrioritization: VTSuperResolutionScalerConfiguration.QualityPrioritization](./qualityprioritization-swift.property.md)
  A parameter to control quality and performance levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/qualityprioritization-swift.enum)*