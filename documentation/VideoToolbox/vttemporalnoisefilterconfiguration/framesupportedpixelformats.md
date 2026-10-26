# frameSupportedPixelFormats

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Supported pixel formats for source frames for current configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

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
- [nextFrameCount](./nextframecount.md)
  Maximum number of future reference frames that the processor can use to process a source frame.
- [previousFrameCount](./previousframecount.md)
  Maximum number of past reference frames that the processor can use to process a source frame.
- [var sourcePixelBufferAttributes: [String : any Sendable]](./sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vttemporalnoisefilterconfiguration/framesupportedpixelformats)*