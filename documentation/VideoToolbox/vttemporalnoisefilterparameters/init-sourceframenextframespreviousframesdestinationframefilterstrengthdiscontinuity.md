# init(sourceFrame:nextFrames:previousFrames:destinationFrame:filterStrength:discontinuity:)

**Framework**: Video Toolbox  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
init(sourceFrame: VTFrameProcessorFrame, nextFrames: [VTFrameProcessorFrame]?, previousFrames: [VTFrameProcessorFrame]?, destinationFrame: VTFrameProcessorFrame, filterStrength: Float, discontinuity: Bool)
```

## Parameters

- `sourceFrame`: Current source frame. Must be non nil.
- `nextFrames`: Future reference frames in presentation time order to be used for processing the source frame. The number of frames can vary from 0 to the number specified by the nextFrameCount property in VTTemporalNoiseFilterConfiguration.
- `previousFrames`: Past reference frames in presentation time order to be used for processing the source frame. The number of frames can vary from 0 to the number specified by the previousFrameCount property in VTTemporalNoiseFilterConfiguration.
- `destinationFrame`: User allocated pixel buffer that will receive the output frame. The pixel format of the destinationFrame must match with that of the sourceFrame.
- `filterStrength`: Used to control strength of the noise filtering. The value can range from the minimum strength of 0.0 to the maximum strength of 1.0. Change in filter strength causes the processor to flush all frames in the queue prior to processing the source frame.
- `discontinuity`: Marks sequence discontinuity, forcing the processor to reset prior to processing the source frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vttemporalnoisefilterparameters/init(sourceframe:nextframes:previousframes:destinationframe:filterstrength:discontinuity:))*