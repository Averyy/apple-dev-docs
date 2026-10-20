# backwardFlow

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

The backward optical flow pixel buffer that was provided when the object was created.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var backwardFlow: CVPixelBuffer { get }
```

```objc
@property (nonatomic, readonly) CVPixelBufferRef backwardFlow;
```

## See Also

### Inspecting the configuration
- [var forwardFlow: CVPixelBuffer](./forwardflow.md)
  The forward optical flow pixel that was provided when the object was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessoropticalflow/backwardflow)*