# frameHeight

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Height of source frames in pixels.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var frameHeight: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger frameHeight;
```

## See Also

### Inspecting the configuration
- [var frameWidth: Int](./framewidth.md)
  Width of source frames in pixels.
- [var numberOfInterpolatedFrames: Int](./numberofinterpolatedframes.md)
  Number of uniformly spaced frames for which you configured the processor.
- [var spatialScaleFactor: Int](./spatialscalefactor.md)
  Configured spatial scale factor as an integer.
- [var sourcePixelBufferAttributes: [String : any Sendable]](./sourcepixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./destinationpixelbufferattributes.md)
  Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent destination frames.
- [var supportedPixelFormats: [OSType]](./supportedpixelformats.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationconfiguration/frameheight)*