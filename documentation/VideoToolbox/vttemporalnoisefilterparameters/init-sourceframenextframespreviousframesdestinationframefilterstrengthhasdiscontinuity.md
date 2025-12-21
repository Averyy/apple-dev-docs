# init(sourceFrame:nextFrames:previousFrames:destinationFrame:filterStrength:hasDiscontinuity:)

**Framework**: Video Toolbox  
**Kind**: init

Creates a new `VTTemporalNoiseFilterParameters` object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
init?(sourceFrame: VTFrameProcessorFrame, nextFrames: [VTFrameProcessorFrame], previousFrames: [VTFrameProcessorFrame], destinationFrame: VTFrameProcessorFrame, filterStrength: Float, hasDiscontinuity: Bool)
```

## Parameters

- `sourceFrame`: Current source frame; must be non  .
- `nextFrames`: Future reference frames in presentation time order to use for processing the source frame. The number   of frames can vary from 0 to the number specified by   property.
- `previousFrames`: Past reference frames in presentation time order to use for processing the source frame. The number   of frames can vary from 0 to the number specified by   property.
- `destinationFrame`: User-allocated pixel buffer that receives the output frame. The pixel format of    must match with that of the  .
- `filterStrength`: Strength of the noise-filtering to use. The value can range from the minimum strength of 0.0 to the   maximum strength of 1.0. Change in filter strength causes the processor to flush all frames in the queue prior to   processing the source frame.
- `hasDiscontinuity`: Marks sequence discontinuity, forcing the processor to reset prior to processing the source frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vttemporalnoisefilterparameters/init(sourceframe:nextframes:previousframes:destinationframe:filterstrength:hasdiscontinuity:))*