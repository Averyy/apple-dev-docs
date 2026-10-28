# destinationPixelBufferAttributes

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var destinationPixelBufferAttributes: [String : any Sendable] { get }
```

```objc
@property (nonatomic, readonly) NSDictionary<NSString *,id> * destinationPixelBufferAttributes;
```

## Discussion

Use `CVPixelBufferCreateResolvedAttributesDictionary` to combine this dictionary with your pixel buffer attributes dictionary.

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
- [var supportedPixelFormats: [OSType]](./supportedpixelformats.md)
- [frameSupportedPixelFormats](./framesupportedpixelformats.md)
  Available supported pixel formats for source frames for current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencysuperresolutionscalerconfiguration/destinationpixelbufferattributes)*