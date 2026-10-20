# frameWidth

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

The width of a source frame in pixels.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var frameWidth: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger frameWidth;
```

#### Discussion

The maximum value is 8192 pixels for macOS, and 4096 pixels for iOS.

## See Also

### Inspecting the configuration
- [var frameHeight: Int](./frameheight.md)
  The height of a source frame in pixels.
- [var usePrecomputedFlow: Bool](./useprecomputedflow.md)
  A Boolean value to indicates whether the the optical flow will be provided by the user.
- [var sourcePixelBufferAttributes: [String : any Sendable]](./sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing requirements for pixel buffers used as source frames and reference frames.
- [var destinationPixelBufferAttributes: [String : any Sendable]](./destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes describing the requirements for pixel buffers used as destination frames.
- [var supportedPixelFormats: [OSType]](./supportedpixelformats.md)
- [var qualityPrioritization: VTMotionBlurConfiguration.QualityPrioritization](./qualityprioritization-swift.property.md)
  A value that specifies whether to prioritize quality or performance.
- [VTMotionBlurConfiguration.QualityPrioritization](./qualityprioritization-swift.enum.md)
  Values that specify whether to prioritize quality or performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurconfiguration/framewidth)*