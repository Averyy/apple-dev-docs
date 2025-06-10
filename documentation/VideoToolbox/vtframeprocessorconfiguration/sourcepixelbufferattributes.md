# sourcePixelBufferAttributes

**Framework**: Video Toolbox  
**Kind**: property  
**Required**: Yes

A dictionary of pixel buffer attributes that define what the source and reference frames passed to the processor must conform to.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var sourcePixelBufferAttributes: [String : any Sendable] { get }
```

## See Also

- [var destinationPixelBufferAttributes: [String : any Sendable]](vtframeprocessorconfiguration/destinationpixelbufferattributes.md)
  A dictionary of pixel buffer attributes that define which output frames passed to the processor must conform to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorconfiguration/sourcepixelbufferattributes)*