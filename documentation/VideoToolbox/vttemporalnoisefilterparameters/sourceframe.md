# sourceFrame

**Framework**: Video Toolbox  
**Kind**: property

Current source frame; must be non `nil`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var sourceFrame: VTFrameProcessorFrame { get }
```

## See Also

- [var nextFrames: [VTFrameProcessorFrame]](vttemporalnoisefilterparameters/nextframes.md)
  Future reference frames in presentation time order that you use to process the source frame.
- [var previousFrames: [VTFrameProcessorFrame]](vttemporalnoisefilterparameters/previousframes.md)
  Past reference frames in presentation time order that you use to process the source frame.
- [var filterStrength: Float](vttemporalnoisefilterparameters/filterstrength.md)
  A parameter to control the strength of noise-filtering. The value can range from the minimum strength of 0.0 to the maximum strength of 1.0. Change in filter strength causes the processor to flush all frames in the queue prior to processing the source frame.
- [var hasDiscontinuity: Bool](vttemporalnoisefilterparameters/hasdiscontinuity.md)
  A Boolean that indicates sequence discontinuity, forcing the processor to reset prior to processing the source frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vttemporalnoisefilterparameters/sourceframe)*