# forwardFlow

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

The forward optical flow pixel that was provided when the object was created.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var forwardFlow: CVPixelBuffer { get }
```

```objc
@property (nonatomic, readonly) CVPixelBufferRef forwardFlow;
```

## See Also

### Inspecting the configuration
- [var backwardFlow: CVPixelBuffer](./backwardflow.md)
  The backward optical flow pixel buffer that was provided when the object was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessoropticalflow/forwardflow)*