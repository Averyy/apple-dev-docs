# scaleFactor

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Scale factor with which you initialized the configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var scaleFactor: Float { get }
```

```objc
@property (nonatomic, readonly) float scaleFactor;
```

## See Also

### Inspecting the configuration
- [var frameWidth: Int](./framewidth.md)
  Width of source frame in pixels.
- [var frameHeight: Int](./frameheight.md)
  Height of source frame in pixels.
- [var sourcePixelBufferAttributes: [String : any Sendable]](./sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.
- [var supportedPixelFormats: [OSType]](./supportedpixelformats.md)
- [frameSupportedPixelFormats](./framesupportedpixelformats.md)
  Available supported pixel formats for source frames for current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencysuperresolutionscalerconfiguration/scalefactor)*