# sourcePixelBufferAttributes

**Framework**: Video Toolbox  
**Kind**: property

Pixel buffer attributes dictionary that describes requirements for pixel buffers which represent source frames and reference frames.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var sourcePixelBufferAttributes: [String : any Sendable] { get }
```

#### Discussion

Use `CVPixelBufferCreateResolvedAttributesDictionary` to combine this dictionary with your pixel buffer attributes dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationconfiguration/sourcepixelbufferattributes)*