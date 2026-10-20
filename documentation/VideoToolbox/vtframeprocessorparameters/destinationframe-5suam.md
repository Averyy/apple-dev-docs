# destinationFrame

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

[`VTFrameProcessorFrame`](../vtframeprocessorframe.md) that contains the destination frame for processors which output a single processed frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var destinationFrame: VTFrameProcessorFrame? { get }
```

## See Also

### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](./sourceframe.md)
  A processor frame that contains the current source frame to use for all processing features.
- [var destinationFrames: [VTFrameProcessorFrame]?](./destinationframes-46ken.md)
  Array of [`VTFrameProcessorFrame`](../vtframeprocessorframe.md) that contains the destination frames for processors which may output more than one processed frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorparameters/destinationframe-5suam)*