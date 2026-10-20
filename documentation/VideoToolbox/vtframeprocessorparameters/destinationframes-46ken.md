# destinationFrames

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Array of [`VTFrameProcessorFrame`](../vtframeprocessorframe.md) that contains the destination frames for processors which may output more than one processed frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var destinationFrames: [VTFrameProcessorFrame]? { get }
```

## See Also

### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](./sourceframe.md)
  A processor frame that contains the current source frame to use for all processing features.
- [var destinationFrame: VTFrameProcessorFrame?](./destinationframe-5suam.md)
  [`VTFrameProcessorFrame`](../vtframeprocessorframe.md) that contains the destination frame for processors which output a single processed frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorparameters/destinationframes-46ken)*