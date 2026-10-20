# buffer

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

The pixel buffer specified when the object was created.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var buffer: CVPixelBuffer { get }
```

```objc
@property (nonatomic, readonly) CVPixelBufferRef buffer;
```

## See Also

### Inspecting the frame
- [var presentationTimeStamp: CMTime](./presentationtimestamp.md)
  The presentation timestamp specified when the object was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorframe/buffer)*