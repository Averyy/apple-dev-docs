# destinationPixelBufferAttributes

**Framework**: Videotoolbox  
**Kind**: property  
**Required**: Yes

A dictionary of pixel buffer attributes that define which output frames passed to the processor must conform to.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var destinationPixelBufferAttributes: [AnyHashable : Any] { get }
```

## See Also

- [var frameSupportedPixelFormats: [NSNumber]](vtframeprocessorconfiguration/framesupportedpixelformats.md)
  A list of supported pixel formats for the current configuration.
- [var sourcePixelBufferAttributes: [AnyHashable : Any]](vtframeprocessorconfiguration/sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes that define what the source and reference frames passed to the processor must conform to.
- [var nextFrameCount: Int](vtframeprocessorconfiguration/nextframecount.md)
  The number of next frames that the processor requires for processing.
- [var previousFrameCount: Int](vtframeprocessorconfiguration/previousframecount.md)
  The number of previous frames that the processor requires for processing.
- [static var maximumDimensions: CMVideoDimensions](vtframeprocessorconfiguration/maximumdimensions.md)
  The maximum dimensions of a source frame for the processor.
- [static var minimumDimensions: CMVideoDimensions](vtframeprocessorconfiguration/minimumdimensions.md)
  The minimum dimensions of a source frame for the processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorconfiguration/destinationpixelbufferattributes)*