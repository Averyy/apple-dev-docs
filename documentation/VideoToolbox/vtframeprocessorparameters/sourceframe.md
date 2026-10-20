# sourceFrame

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A processor frame that contains the current source frame to use for all processing features.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var sourceFrame: VTFrameProcessorFrame { get }
```

```objc
@property (nonatomic, readonly) VTFrameProcessorFrame * sourceFrame;
```

#### Discussion

This property must not be `NULL`.

## See Also

### Inspecting the parameters
- [var destinationFrame: VTFrameProcessorFrame?](./destinationframe-5suam.md)
  [`VTFrameProcessorFrame`](../vtframeprocessorframe.md) that contains the destination frame for processors which output a single processed frame.
- [var destinationFrames: [VTFrameProcessorFrame]?](./destinationframes-46ken.md)
  Array of [`VTFrameProcessorFrame`](../vtframeprocessorframe.md) that contains the destination frames for processors which may output more than one processed frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorparameters/sourceframe)*