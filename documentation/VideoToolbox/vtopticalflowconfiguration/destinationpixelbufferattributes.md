# destinationPixelBufferAttributes

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var destinationPixelBufferAttributes: [String : any Sendable] { get }
```

```objc
@property (nonatomic, readonly) NSDictionary<NSString *,id> * destinationPixelBufferAttributes;
```

## See Also

### Inspecting the configuration
- [var frameWidth: Int](./framewidth.md)
  The width of a source frame in pixels.
- [var frameHeight: Int](./frameheight.md)
  The height of source frame in pixels.
- [var sourcePixelBufferAttributes: [String : any Sendable]](./sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var supportedPixelFormats: [OSType]](./supportedpixelformats.md)
- [var qualityPrioritization: VTOpticalFlowConfiguration.QualityPrioritization](./qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.
- [VTOpticalFlowConfiguration.QualityPrioritization](./qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowconfiguration/destinationpixelbufferattributes)*