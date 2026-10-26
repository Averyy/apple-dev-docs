# frameSupportedPixelFormats

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Available supported pixel formats for current configuration.

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
  Width of source frames in pixels.
- [var frameHeight: Int](./frameheight.md)
  Height of source frames in pixels.
- [var numberOfInterpolatedFrames: Int](./numberofinterpolatedframes.md)
  Number of uniformly spaced frames for which you configured the processor.
- [var spatialScaleFactor: Int](./spatialscalefactor.md)
  Configured spatial scale factor as an integer.
- [var sourcePixelBufferAttributes: [String : any Sendable]](./sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationconfiguration/framesupportedpixelformats)*