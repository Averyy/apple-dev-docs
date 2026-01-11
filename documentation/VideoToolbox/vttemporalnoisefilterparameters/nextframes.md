# nextFrames

**Framework**: Video Toolbox  
**Kind**: property

Future reference frames in presentation time order that you use to process the source frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var nextFrames: [VTFrameProcessorFrame] { get }
```

#### Discussion

The number of frames can vary from 0 to the number specified by the `nextFrameCount` property in `VTTemporalNoiseFilterConfiguration`.

## See Also

- [var sourceFrame: VTFrameProcessorFrame](vttemporalnoisefilterparameters/sourceframe.md)
  Current source frame; must be non `nil`.
- [var previousFrames: [VTFrameProcessorFrame]](vttemporalnoisefilterparameters/previousframes.md)
  Past reference frames in presentation time order that you use to process the source frame.
- [var filterStrength: Float](vttemporalnoisefilterparameters/filterstrength.md)
  A parameter to control the strength of noise-filtering. The value can range from the minimum strength of 0.0 to the maximum strength of 1.0. Change in filter strength causes the processor to flush all frames in the queue prior to processing the source frame.
- [var hasDiscontinuity: Bool](vttemporalnoisefilterparameters/hasdiscontinuity.md)
  A Boolean that indicates sequence discontinuity, forcing the processor to reset prior to processing the source frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vttemporalnoisefilterparameters/nextframes)*