# sourcePixelBufferAttributes

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A dictionary of pixel buffer attributes that define what the source and reference frames passed to the processor must conform to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var sourcePixelBufferAttributes: [String : any Sendable] { get }
```

```objc
@property (nonatomic, readonly) NSDictionary<NSString *,id> * sourcePixelBufferAttributes;
```

## See Also

### Inspecting pixel buffer attributes
- [var destinationPixelBufferAttributes: [String : any Sendable]](./destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes that define which output frames passed to the processor must conform to.
- [frameSupportedPixelFormats](./framesupportedpixelformats.md)
  A list of supported pixel formats for the current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorconfiguration/sourcepixelbufferattributes)*