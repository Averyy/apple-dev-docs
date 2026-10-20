# destinationPixelBufferAttributes

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A dictionary of pixel buffer attributes that define which output frames passed to the processor must conform to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var destinationPixelBufferAttributes: [String : any Sendable] { get }
```

```objc
@property (nonatomic, readonly) NSDictionary<NSString *,id> * destinationPixelBufferAttributes;
```

## See Also

### Inspecting pixel buffer attributes
- [var sourcePixelBufferAttributes: [String : any Sendable]](./sourcepixelbufferattributes.md)
  A dictionary of pixel buffer attributes that define what the source and reference frames passed to the processor must conform to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorconfiguration/destinationpixelbufferattributes)*