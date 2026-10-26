# frameSupportedPixelFormats

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Available supported pixel formats for source frames for current configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * frameSupportedPixelFormats;
```

## See Also

### Inspecting the configuration
- [var frameWidth: Int](./framewidth.md)
  Width of source frame in pixels.
- [var frameHeight: Int](./frameheight.md)
  Height of source frame in pixels.
- [var scaleFactor: Float](./scalefactor.md)
  Scale factor with which you initialized the configuration.
- [var sourcePixelBufferAttributes: [String : any Sendable]](./sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencysuperresolutionscalerconfiguration/framesupportedpixelformats)*