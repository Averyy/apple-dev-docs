# frameHeight

**Framework**: Videotoolbox  
**Kind**: property

The height of source frame in pixels.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var frameHeight: Int { get }
```

#### Discussion

The maximum value is 8192 pixels for macOS, and 4096 pixels for iOS.

## See Also

- [var frameWidth: Int](vtopticalflowconfiguration/framewidth.md)
  The width of a source frame in pixels.
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtopticalflowconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](vtopticalflowconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var frameSupportedPixelFormats: [NSNumber]](vtopticalflowconfiguration/framesupportedpixelformats.md)
  A list of source frame supported pixel formats for the current configuration.
- [var qualityPrioritization: VTOpticalFlowConfiguration.QualityPrioritization](vtopticalflowconfiguration/qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.
- [VTOpticalFlowConfiguration.QualityPrioritization](vtopticalflowconfiguration/qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowconfiguration/frameheight)*