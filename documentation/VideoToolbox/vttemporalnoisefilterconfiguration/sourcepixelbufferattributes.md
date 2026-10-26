# sourcePixelBufferAttributes

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var sourcePixelBufferAttributes: [String : any Sendable] { get }
```

```objc
@property (nonatomic, readonly) NSDictionary<NSString *,id> * sourcePixelBufferAttributes;
```

#### Discussion

Use `CVPixelBufferCreateResolvedAttributesDictionary` to combine this dictionary with your pixel buffer attributes dictionary.

## See Also

### Inspecting the configuration
- [var frameWidth: Int](./framewidth.md)
  Width of source frame in pixels.
- [var frameHeight: Int](./frameheight.md)
  Height of source frame in pixels.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.
- [var supportedPixelFormats: [OSType]](./supportedpixelformats.md)
- [class var supportedSourcePixelFormats: [OSType]](./supportedsourcepixelformats-4ipcg.md)
- [nextFrameCount](./nextframecount.md)
  Maximum number of future reference frames that the processor can use to process a source frame.
- [previousFrameCount](./previousframecount.md)
  Maximum number of past reference frames that the processor can use to process a source frame.
- [frameSupportedPixelFormats](./framesupportedpixelformats.md)
  Supported pixel formats for source frames for current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vttemporalnoisefilterconfiguration/sourcepixelbufferattributes)*